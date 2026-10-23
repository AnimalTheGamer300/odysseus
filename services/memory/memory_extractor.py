"""
memory_extractor.py

Background auto-extraction of facts from chat conversations.
After each LLM response, this module sends the last few messages to the LLM
asking it to extract memorable facts, then stores them in both memory.json
and the FAISS vector index.

Periodically audits all memories via LLM to consolidate duplicates,
rewrite vague entries, and remove junk.
"""

import hashlib
import json
import logging
import os
import re
from typing import Optional

from src.memory import MemoryStoreUnreadable

logger = logging.getLogger(__name__)


def _tidy_state_path(memory_manager) -> str:
    """Sidecar JSON next to memory.json that remembers the fingerprint of
    the last successfully-audited state per owner. Lets the audit short-
    circuit when nothing has changed since the previous tidy — running
    the LLM again on an already-clean list was wasting 30-120s per call
    and occasionally timing out on the second pass."""
    return os.path.join(os.path.dirname(memory_manager.memory_file), "memory_tidy_state.json")


def _fingerprint_entries(entries) -> str:
    """Stable hash of an owner's memories — order-independent, depends
    only on id+text+category. Any add/edit/delete invalidates it."""
    items = sorted(
        (str(e.get("id", "")), e.get("text", ""), e.get("category", ""))
        for e in _memory_dicts(entries)
    )
    h = hashlib.sha256()
    for triple in items:
        h.update(("\x1f".join(triple) + "\x1e").encode("utf-8"))
    return h.hexdigest()


def _memory_dicts(entries):
    for entry in entries or []:
        if isinstance(entry, dict):
            yield entry


def _load_tidy_state(memory_manager) -> dict:
    path = _tidy_state_path(memory_manager)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_tidy_state(memory_manager, owner: Optional[str], fingerprint: str) -> None:
    path = _tidy_state_path(memory_manager)
    state = _load_tidy_state(memory_manager)
    state[owner or ""] = {"fingerprint": fingerprint}
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except OSError as e:
        logger.warning(f"Could not persist tidy fingerprint: {e}")


_EXTRACT_STATE_FILE = "memory_extract_state.json"


def _extract_state_path(memory_manager) -> Optional[str]:
    """Sidecar JSON next to memory.json that remembers, per session, how many
    messages extraction already consumed (the novelty gate) and, per owner,
    how many new memories have accumulated since the last auto-audit. Both
    counters previously lived only in process memory — the audit counter
    silently reset on every restart, starving the auto-audit forever."""
    memory_file = getattr(memory_manager, "memory_file", None)
    if not memory_file:
        return None
    return os.path.join(os.path.dirname(memory_file), _EXTRACT_STATE_FILE)


def _load_extract_state(memory_manager) -> dict:
    path = _extract_state_path(memory_manager)
    if not path:
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_extract_state(memory_manager, state: dict) -> None:
    path = _extract_state_path(memory_manager)
    if not path:
        return
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except OSError as e:
        logger.warning(f"Could not persist memory extract state: {e}")


def _last_extracted_count(memory_manager, session_id: str) -> int:
    state = _load_extract_state(memory_manager)
    return int(state.get("sessions", {}).get(session_id, {}).get("last_count", 0))


def _set_last_extracted_count(memory_manager, session_id: str, count: int) -> None:
    state = _load_extract_state(memory_manager)
    state.setdefault("sessions", {})[session_id] = {"last_count": count}
    _save_extract_state(memory_manager, state)


def _pending_audit_count(memory_manager, owner: Optional[str]) -> int:
    state = _load_extract_state(memory_manager)
    return int(state.get("counters", {}).get(owner or "", 0))


def _set_pending_audit_count(memory_manager, owner: Optional[str], count: int) -> None:
    state = _load_extract_state(memory_manager)
    state.setdefault("counters", {})[owner or ""] = count
    _save_extract_state(memory_manager, state)

EXTRACT_SYSTEM_PROMPT = (
    "You are a memory extraction assistant. Analyze the conversation and extract ONLY "
    "durable personal facts about the user that would be useful across many future conversations.\n\n"
    "Good examples: name, job title, city, family members, long-term projects, strong preferences.\n"
    "Bad examples: what they asked about today, temporary moods, generic statements, "
    "things the assistant said, one-off tasks, opinions on the current topic.\n\n"
    "Rules:\n"
    "- MAX 3 facts per conversation — only the most important\n"
    "- Only extract facts the USER stated or clearly implied\n"
    "- Each fact must make sense ALONE, to someone who was NOT in this conversation: "
    "name the subject fully, never use unexplained abbreviations or pronouns, and "
    "include the context needed to stand on its own (one or two sentences, 15-50 words)\n"
    "- Only extract facts that would still be useful in a DIFFERENT future conversation — "
    "durable preferences, projects, possessions, life details. Skip transient statements, "
    "passing opinions, or anything that only matters in this exact chat\n"
    "- If a fact is similar to something likely already known, skip it\n"
    "- If nothing durable was revealed, return []\n\n"
    "Return a JSON array of objects with 'text' and 'category' fields.\n"
    "Categories: 'identity', 'preference', 'fact', 'contact', 'project', 'goal'\n\n"
    "Return ONLY valid JSON, no markdown fences."
)

# How many recent messages to include for extraction
CONTEXT_WINDOW = 6

AUDIT_SYSTEM_PROMPT = (
    "You are a memory database curator. Be CONSERVATIVE: remove only TRUE "
    "duplicates and clearly useless entries. Every distinct fact must survive. "
    "When in doubt, KEEP the entry. Return the cleaned list.\n\n"
    "Rules:\n"
    "1. MERGE only entries that state the SAME fact in different words. If you "
    "are not sure two entries are the same fact, KEEP BOTH.\n"
    "   Merge: 'User's name is Sam' + 'The user is called Sam' -> one.\n"
    "   Do NOT merge related-but-distinct facts: 'Likes Python' and 'Uses "
    "Python at work' are DIFFERENT — keep both.\n"
    "2. REMOVE only entries that are genuinely worthless: about what the AI did "
    "(not the user), empty, or meaningless. Do NOT drop a real fact just "
    "because it seems minor or niche.\n"
    "3. Keep the original wording. Only lightly trim obvious redundancy — do "
    "NOT aggressively rewrite or shorten. EXCEPTION: if an entry is a fragment "
    "that cannot stand alone (missing subject, unexplained abbreviation, dangling "
    "pronoun, e.g. \"User prefers DRLs too\"), rewrite it into a self-contained "
    "sentence. Restore clarity — never invent facts; if the meaning is "
    "genuinely unknowable, leave it unchanged.\n"
    "4. Preserve the 'id' of the entry you keep when merging.\n"
    "5. Never invent facts. When unsure, KEEP.\n\n"
    "Return a JSON array of objects with fields: id, text, category.\n"
    "Return ONLY valid JSON, no markdown fences."
)

AUDIT_INTERVAL = 5  # audit every N new memories added

# How many NEW messages must a session accumulate since the last extraction
# run before it is looked at again. The cadence trigger fires on message
# count alone; without this gate every run re-analyzes a sliding window that
# overlaps the previous run and re-extracts the same facts rephrased.
NOVELTY_MIN_MESSAGES = 2


def _message_text(message) -> str:
    content = getattr(message, "content", None)
    if content is None and isinstance(message, dict):
        content = message.get("content")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                parts.append(str(item.get("text") or item.get("content") or ""))
            else:
                parts.append(str(item))
        return " ".join(p for p in parts if p).strip()
    return ""


def _message_role(message) -> str:
    role = getattr(message, "role", None)
    if role is None and isinstance(message, dict):
        role = message.get("role")
    return str(role or "").lower()


def _clean_memory_value(value: str, max_len: int = 200) -> str:
    value = re.sub(r"\s+", " ", value or "").strip(" .,!?:;\"'`“”‘’")
    value = re.sub(r"^(?:the|a|an)\s+", "", value, flags=re.I)
    if not value or len(value) > max_len:
        return ""
    if re.search(r"https?://|@|[{}<>]", value):
        return ""
    return value


# Deictic / discourse-dependent tokens that make a captured "preference"
# non-durable. "I like THAT idea", "I like how you…", "I like this approach"
# are about the current conversation; "I like pizza" is a lasting preference.
# Bare pronouns ("I like it") and empty shells ("the idea", "the plan",
# "the vibe") fall in the same bucket.
_DEICTIC_TOKENS = {
    "that", "this", "these", "those", "it", "them", "they",
    "here", "there", "so", "such", "then", "now",
    "you", "your", "yours", "yourself", "me", "my", "mine", "myself",
    "i", "we", "our", "ours", "us", "ourselves",
    "when", "how", "whether", "whatever", "whichever", "whoever",
    "idea", "ideas", "suggestion", "suggestions", "approach",
    "plan", "plans", "option", "options", "choice", "choices",
    "thing", "things", "bit", "stuff", "vibe", "vibes", "look", "feel",
}


def _is_deictic_preference(text: str) -> bool:
    """True when a captured preference object is discourse-dependent — about
    the current conversation rather than a lasting preference. Keeps "I like
    that idea"-style junk out of the store without dropping real preferences.
    """
    tokens = set(re.findall(r"[a-z']+", text.lower()))
    return bool(tokens & _DEICTIC_TOKENS)


_CORE_IDENTITY_RE = re.compile(
    r"\b(?:"
    r"name|names|called|call me|goes by|"
    r"lives? in|lives? at|from|"
    r"works? at|works? for|works? as|job|occupation|profession|"
    r"age|years old|born|birthday|pronouns"
    r")\b",
    re.I,
)


def _is_pinnable_identity(text: str) -> bool:
    """True when an 'identity'-category fact states a CORE identity fact
    (name, location, job, age, pronouns) that belongs in always-injected
    context. Vague identity guesses ("User identifies as X", "User is into
    Y") stay unpinned and live in normal retrieval instead."""
    return bool(_CORE_IDENTITY_RE.search(text))


def _fallback_memory_candidates(messages) -> list[dict]:
    """Extract obvious durable facts without relying on the LLM.

    This is deliberately narrow. The LLM remains the main extractor, but
    simple identity/preference/goal statements should not silently vanish just
    because the background model judged them too conversational.
    """
    candidates = []
    seen = set()

    def add(text: str, category: str):
        text = _clean_memory_value(text, 120)
        if not text:
            return
        key = text.lower()
        if key in seen:
            return
        seen.add(key)
        candidates.append({"text": text, "category": category})

    for msg in messages:
        if _message_role(msg) != "user":
            continue
        text = _message_text(msg)
        if not text:
            continue

        m = re.search(r"\bmy name is\s+([A-Za-z][A-Za-z0-9 .'\-]{1,50})\b", text, re.I)
        if m:
            name = _clean_memory_value(m.group(1), 50)
            if name:
                add(f"User's name is {name}.", "identity")

        m = re.search(r"\bcall me\s+([A-Za-z][A-Za-z0-9 .'\-]{1,50})\b", text, re.I)
        if m:
            name = _clean_memory_value(m.group(1), 50)
            if name:
                add(f"User wants to be called {name}.", "identity")

        m = re.search(r"\bi (?:live in|am from|'m from)\s+([^.!?\n]{2,80})", text, re.I)
        if m:
            place = _clean_memory_value(m.group(1), 80)
            if place:
                add(f"User lives in {place}.", "identity")

        m = re.search(r"\bi\s+(prefer|like|love|hate|do not like|don't like|enjoy)\s+([^.!?\n]{4,200})", text, re.I)
        if m:
            verb = m.group(1).lower()
            # All positives normalize to "prefers", all negatives to
            # "dislikes" — raw verb forms ("likes"/"hates") made near-duplicate
            # facts ("User likes X" vs "User prefers X") dodge the fuzzy dedup.
            verb_map = {
                "prefer": "prefers",
                "like": "prefers",
                "love": "prefers",
                "enjoy": "prefers",
                "hate": "dislikes",
                "do not like": "dislikes",
                "don't like": "dislikes",
            }
            preference = _clean_memory_value(m.group(2), 200)
            # Strip first/second-person possessives ("my new keyboard" ->
            # "new keyboard") so the stored fact reads like a fact about the
            # user instead of a quote with the wrong pronoun.
            if preference:
                preference = re.sub(r"\b(?:my|mine|our|ours|your|yours)\b", " ", preference)
                preference = _clean_memory_value(preference, 200)
            if preference and not _is_deictic_preference(preference):
                add(f"User {verb_map.get(verb, 'prefers')} {preference}.", "preference")

        m = re.search(
            r"\bi (?:(?:want|would like|plan|hope) to|wanna) "
            r"(?:go|travel|move|visit) to\s+([^.!?\n]{2,80})",
            text,
            re.I,
        )
        if m:
            destination = _clean_memory_value(m.group(1), 80)
            if destination:
                add(f"User wants to visit {destination}.", "goal")

    return candidates[:2]


# Tokens too cheap to count in similarity: "prefers the dark theme" vs
# "prefers dark theme" should match. Kept minimal so real distinctions
# (positive vs negative objects) still register.
_DEDUP_STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "to", "in", "for", "on",
    "with", "at", "by", "is", "are", "was", "were",
}


def _dedup_tokens(text: str) -> set:
    """Normalized token set for Jaccard: lowercase, punctuation stripped
    (periods, commas, possessives), stopwords dropped — so rephrased
    duplicates of the same fact land above threshold instead of slipping past
    as separate memories."""
    text = re.sub(r"'s\b", "", (text or "").lower())  # user's -> user
    tokens = re.findall(r"[a-z0-9]+", text)
    return {t for t in tokens if t not in _DEDUP_STOPWORDS}


def _is_text_duplicate(new_text: str, existing: list, threshold: float = 0.55) -> bool:
    """Check if new_text is too similar to any existing memory (Jaccard similarity)."""
    new_tokens = _dedup_tokens(new_text)
    if not new_tokens:
        return False
    for entry in _memory_dicts(existing):
        old_tokens = _dedup_tokens(entry.get("text", ""))
        if not old_tokens:
            continue
        intersection = new_tokens & old_tokens
        union = new_tokens | old_tokens
        if len(intersection) / len(union) >= threshold:
            return True
    return False


def _parse_extraction_json(raw: str) -> list:
    """Parse the extraction LLM's reply into a list of facts, tolerating
    reasoning-model noise.

    The model emits <think>…</think> (and sometimes a prose preamble or a
    ```json fence) AROUND the JSON array; without stripping it, json.loads
    bombs and the run silently yields "0 candidates". Pure str -> list (no
    LLM/network); returns [] on any parse failure instead of raising.
    """
    text = (raw or "").strip()
    try:
        from src.text_helpers import strip_think as _strip_think
        text = _strip_think(text, prose=True, prompt_echo=True).strip()
    except Exception:
        pass
    if text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    # JSON may still be embedded in surrounding commentary (leading prose or
    # trailing remarks like "[...] Done!") — slice from the first '[' to the
    # last ']' whenever both exist. Slice unconditionally: a reply that starts
    # with '[' can still carry trailing commentary that breaks json.loads.
    _start = text.find("[")
    _end = text.rfind("]")
    if 0 <= _start < _end:
        text = text[_start : _end + 1]

    try:
        facts = json.loads(text)
    except json.JSONDecodeError:
        logger.debug("Memory extraction returned non-JSON: %r", (raw or "")[:120])
        return []
    except Exception:
        logger.debug("Memory extraction returned non-JSON: %r", (raw or "")[:120])
        return []
    return facts if isinstance(facts, list) else []


async def extract_and_store(
    session,
    memory_manager,
    memory_vector,
    endpoint_url: str,
    model: str,
    headers: Optional[dict] = None,
):
    """Extract facts from recent conversation and store them.

    Designed to run as a background task (asyncio.create_task).
    Errors are logged, never raised.
    """
    if not endpoint_url or not model:
        logger.debug("[memory-extract] No model or URL provided, skipping")
        return

    try:
        from src.llm_core import llm_call_async

        # Get last N messages from session
        messages = session.get_context_messages()
        recent = messages[-CONTEXT_WINDOW:] if len(messages) > CONTEXT_WINDOW else messages

        if len(recent) < 2:
            return  # Need at least a user message and assistant response

        # Novelty gate: never re-analyze a window we already consumed. The
        # cadence trigger fires on message count alone, so without this every
        # run re-sees 2-4 of the previous run's messages and re-extracts the
        # same facts rephrased. The baseline clamps to the current length so
        # context compaction (which shrinks history) can't wedge the gate shut.
        _session_id = (
            getattr(session, "session_id", None)
            or getattr(session, "name", None)
            or "default"
        )
        _baseline = min(_last_extracted_count(memory_manager, _session_id), len(messages))
        if len(messages) - _baseline < NOVELTY_MIN_MESSAGES:
            logger.debug(
                f"[memory-extract] session {_session_id}: "
                f"{len(messages) - _baseline} new messages since last run — skipping"
            )
            return

        # Strip media (images/audio) from messages — background memory extraction
        # only needs the text. The VL-generated descriptions are already in the
        # text content of the messages. This avoids sending image tokens to
        # non-vision models and prevents accidental "vision grounding" triggers.
        stripped_recent = []
        for msg in recent:
            role = msg.get("role")
            content = msg.get("content", "")
            if isinstance(content, list):
                # Filter out multimodal blocks that aren't text
                text_only = [b for b in content if isinstance(b, dict) and b.get("type") == "text"]
                if not text_only and content:
                    continue
                content = text_only
            stripped_recent.append({"role": role, "content": content})

        if not stripped_recent:
            return

        # Flatten the window into a SINGLE user message instead of appending the
        # raw alternating role messages. Passed as raw chat messages, the model
        # treats the window as a conversation to CONTINUE rather than a transcript
        # to ANALYZE, so it reliably extracts nothing — typically returning `[]`
        # (and, depending on the input, sometimes an empty or <think>-only
        # completion when the window ends on an assistant turn). This was the real
        # cause of auto-memory logging "0 candidates" on every run. Reframing it as
        # one "analyze this transcript, return the JSON array" user message makes
        # the model actually extract. Controlled repro on this model: 0/6 trials
        # with the old structure vs 6/6 with this one. The skill extractor flattens
        # for the same reason.
        def _flatten_msg(m):
            c = m.get("content", "")
            if isinstance(c, list):
                c = " ".join(
                    b.get("text", "") for b in c
                    if isinstance(b, dict) and b.get("type") == "text"
                )
            return f"{m.get('role', '?')}: {c}"

        transcript = "\n\n".join(_flatten_msg(m) for m in stripped_recent)
        extraction_messages = [
            {"role": "system", "content": EXTRACT_SYSTEM_PROMPT},
            {"role": "user", "content": (
                "Conversation to analyze:\n\n" + transcript
                + "\n\nReturn the JSON array of durable facts now (or [] if none)."
            )},
        ]

        facts = []
        try:
            raw = await llm_call_async(
                endpoint_url,
                model,
                extraction_messages,
                temperature=0.1,
                # A reasoning model spends most of its budget on <think> tokens
                # BEFORE emitting the JSON, so the old 500 truncated the response
                # before any JSON appeared → every run logged "0 candidates". The
                # audit path hit the same wall and raised to 16384; extraction's
                # output (a short facts list) is small, so an ample ceiling is
                # enough once thinking has room.
                max_tokens=4096,
                headers=headers,
            )

            # The model saw this window — advance the novelty baseline so the
            # next cadence tick doesn't re-analyze the same messages. Only on
            # success: a raised call leaves the window un-consumed so a later
            # trigger retries it.
            _set_last_extracted_count(memory_manager, _session_id, len(messages))

            # Parse JSON, tolerating reasoning-model noise (<think> blocks, a
            # ```json fence, and leading/trailing commentary). See
            # _parse_extraction_json — returns [] rather than raising.
            facts = _parse_extraction_json(raw)
        except Exception as e:
            logger.warning(f"LLM memory extraction failed: {e}")

        if not isinstance(facts, list):
            facts = []

        # The regex fallback is the LAST resort, not a second opinion: it only
        # gets a chance when the LLM path produced nothing (a raised call, an
        # unparseable reply, or a deliberate "nothing durable here"). It is
        # never stacked on top of facts the LLM already extracted — that
        # double-standard append is what flooded the store with "I like that
        # idea"-style junk the model had just rejected.
        if not facts:
            fallback_facts = _fallback_memory_candidates(stripped_recent)
            facts = list(facts) + fallback_facts

        if not facts:
            logger.info("Auto memory extraction ran: 0 candidates")
            return

        # Get owner from session
        _owner = getattr(session, 'owner', None)

        # Strict load: this is a read-modify-write. Degrading to [] here would
        # save only the newly extracted facts and drop the entire store.
        try:
            existing = memory_manager.load_all_for_update()
        except MemoryStoreUnreadable as e:
            logger.error("Skipping auto memory extraction, store unreadable: %s", e)
            return
        added = 0

        for fact in facts:
            if isinstance(fact, str):
                fact_text = fact
                category = "fact"
            elif isinstance(fact, dict):
                fact_text = fact.get("text", "").strip()
                category = fact.get("category", "fact")
            else:
                continue

            if not fact_text or len(fact_text) < 5:
                continue

            # Dedup: check vector similarity first (fast), then exact text match.
            # A runtime embedding/ChromaDB failure (backend OOM, model evicted,
            # remote endpoint down) must not abort the whole batch — fall through
            # to the text/fuzzy dedup below instead of losing every validated
            # fact extracted this session. (`.healthy` is only set at init, so
            # it does not catch failures that develop later.)
            if memory_vector and memory_vector.healthy:
                try:
                    existing_id = memory_vector.find_similar(fact_text, threshold=0.72)
                except Exception as e:
                    logger.warning(f"Memory dedup (vector) unavailable, using text fallback: {e}")
                    existing_id = None
                if existing_id:
                    # The vector store is a single shared collection with no
                    # owner metadata, so find_similar can return ANOTHER
                    # tenant's memory. Only treat it as a duplicate when the
                    # match is this user's own (or a legacy unowned) memory —
                    # otherwise the user's freshly-extracted fact would be
                    # silently dropped. Mirror the owner predicate used by the
                    # text dedup below; cross-tenant/stale matches fall through.
                    _match = next((e for e in existing if e.get("id") == existing_id), None)
                    if _match is not None and (_match.get("owner") == _owner or _match.get("owner") is None):
                        logger.debug(f"Memory dedup (vector): '{fact_text[:50]}' matches {existing_id}")
                        continue

            # Text dedup fallback: exact match + fuzzy similarity
            user_existing = [e for e in existing if e.get("owner") == _owner or e.get("owner") is None] if _owner else existing
            if memory_manager.find_duplicates(fact_text, user_existing):
                continue
            # Fuzzy text similarity check (catches rephrased duplicates when vector index is unavailable)
            if _is_text_duplicate(fact_text, user_existing):
                logger.debug(f"Memory dedup (fuzzy): '{fact_text[:50]}' too similar to existing")
                continue

            entry = memory_manager.add_entry(fact_text, source="auto", category=category, owner=_owner)
            # Auto-pin CORE identity facts (name, location, job, age,
            # pronouns) — always-injected context. A bare category guess of
            # "identity" is not enough to permanently pin something into
            # every prompt; the fact text has to actually state a core fact.
            if category == "identity" and _is_pinnable_identity(fact_text):
                entry["pinned"] = True
            if hasattr(session, "session_id"):
                entry["session_id"] = session.session_id
            elif hasattr(session, "name"):
                entry["session_id"] = session.name

            existing.append(entry)

            # Add to vector index. The JSON store (saved below) is the source of
            # truth and the keyword path can still retrieve this entry, so a vector
            # write failure must not drop the fact or abort the remaining batch.
            if memory_vector and memory_vector.healthy:
                try:
                    memory_vector.add(entry["id"], fact_text)
                except Exception as e:
                    logger.warning(f"Memory vector add failed for {entry['id']}: {e}")

            added += 1

        if added > 0:
            memory_manager.save(existing)
            try:
                from src.event_bus import fire_event
                for _ in range(added):
                    fire_event("memory_added", _owner)
            except Exception:
                logger.debug("memory_added event dispatch failed", exc_info=True)
            logger.info(f"Auto-extracted {added} memories from session")

            # Persisted across restarts — the old process-global counter
            # reset on every restart, silently starving the auto-audit forever.
            _pending = _pending_audit_count(memory_manager, _owner) + added
            if _pending >= AUDIT_INTERVAL:
                _pending = 0
                logger.info("Audit threshold reached, running memory audit")
                await audit_memories(
                    memory_manager, memory_vector, endpoint_url, model, headers, owner=_owner
                )
            _set_pending_audit_count(memory_manager, _owner, _pending)
        else:
            logger.info("Auto memory extraction ran: 0 added")

    except Exception as e:
        logger.error(f"Memory extraction failed: {e}")


async def audit_memories(
    memory_manager,
    memory_vector,
    endpoint_url: str,
    model: str,
    headers: Optional[dict] = None,
    owner: Optional[str] = None,
):
    """Send all memories to the LLM for deduplication and consolidation.

    - Merges near-duplicate entries
    - Rewrites vague entries to be concise
    - Removes junk / non-personal entries
    - Rebuilds the vector index afterwards

    Safe to call manually or from the automatic trigger in extract_and_store.
    Errors are logged, never raised.
    """
    try:
        from src.llm_core import llm_call_async

        existing = memory_manager.load(owner=owner)
        if not existing:
            logger.info("Memory audit: nothing to audit")
            return {"before": 0, "after": 0}

        before_count = len(existing)

        # Skip the LLM call entirely when this exact set of memories was
        # already audited — the previous tidy left them in a clean state
        # and nothing has changed since. Returns instantly so the UI shows
        # "Already clean" without spending 30-120s on a wasted LLM round.
        # The fingerprint includes id+text+category; any add/edit/delete
        # invalidates it and the audit runs normally.
        current_fp = _fingerprint_entries(existing)
        last_state = _load_tidy_state(memory_manager).get(owner or "") or {}
        if last_state.get("fingerprint") == current_fp:
            logger.info("Memory audit: state unchanged since last tidy — skipping LLM")
            return {
                "before": before_count,
                "after": before_count,
                "already_tidy": True,
            }

        # Build payload: list of {id, text, category} for the LLM
        memory_payload = [
            {"id": m["id"], "text": m["text"], "category": m.get("category", "fact")}
            for m in existing
        ]

        audit_messages = [
            {"role": "system", "content": AUDIT_SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(memory_payload, ensure_ascii=False)},
        ]

        raw = await llm_call_async(
            endpoint_url,
            model,
            audit_messages,
            temperature=0.1,
            # 16384 (was 2000): the deduped list of all memories can be large,
            # and a reasoning model spends tokens thinking first — 2000 truncated
            # the JSON so it never parsed ("bad_json").
            max_tokens=16384,
            headers=headers,
            # Bound the call so the Tidy whirlpool can't spin indefinitely on a
            # slow/large generation.
            timeout=120,
        )

        # Parse the JSON list, tolerating reasoning-model noise: <think> blocks,
        # markdown fences, leading prose, and trailing commas.
        import re as _re
        text = (raw or "").strip()
        text = _re.sub(r'<think(?:ing)?>[\s\S]*?</think(?:ing)?>', '', text, flags=_re.I).strip()

        def _loads_list(s):
            if not s:
                return None
            for cand in (s, _re.sub(r',(\s*[}\]])', r'\1', s)):
                try:
                    v = json.loads(cand)
                    if isinstance(v, list):
                        return v
                except Exception:
                    continue
            return None

        cleaned = _loads_list(text)
        if cleaned is None:
            _m = _re.search(r'```(?:json)?\s*\n?([\s\S]*?)```', text)
            if _m:
                cleaned = _loads_list(_m.group(1).strip())
        if cleaned is None:
            _a, _b = text.find('['), text.rfind(']')
            if _a >= 0 and _b > _a:
                cleaned = _loads_list(text[_a:_b + 1])
        if cleaned is None:
            logger.error(f"Memory audit returned non-JSON: {text[:300]}")
            return {"before": before_count, "after": before_count, "error": "bad_json"}

        # Build lookup of original entries by ID so we can preserve metadata
        originals = {m["id"]: m for m in existing}

        final_entries = []
        for item in cleaned:
            if not isinstance(item, dict):
                continue
            mid = item.get("id", "")
            new_text = item.get("text", "").strip()
            if not new_text:
                continue

            if mid in originals:
                # Preserve original metadata, update text + category
                entry = originals[mid].copy()
                entry["text"] = new_text
                if item.get("category"):
                    entry["category"] = item["category"]
            else:
                # ID not found — skip to avoid inventing entries
                logger.debug(f"Audit returned unknown id {mid}, skipping")
                continue

            final_entries.append(entry)

        after_count = len(final_entries)

        # Safety net against catastrophic over-deletion. A conservative tidy
        # should never wipe out half the store in one pass — if the model
        # returned far fewer entries than it was given (over-consolidation, a
        # dropped/truncated list, or it ignored ids), treat it as a misfire and
        # DON'T save. Better to no-op than to silently lose memories.
        if before_count >= 8 and after_count < before_count * 0.5:
            logger.warning(
                f"Memory audit would cut {before_count} -> {after_count} "
                f"(>50% removed) — refusing as unsafe, keeping originals"
            )
            return {"before": before_count, "after": before_count, "error": "unsafe_removal"}

        # Merge audited entries back with other users' entries
        if owner:
            # Strict load: the merge below reconstructs the whole file. If this
            # degraded to [] we would save only this owner's audited slice and
            # destroy every other tenant's memories.
            try:
                all_entries = memory_manager.load_all_for_update()
            except MemoryStoreUnreadable as e:
                logger.error("Aborting memory audit save, store unreadable: %s", e)
                return {
                    "before": before_count,
                    "after": before_count,
                    "error": "store_unreadable",
                }
            audited_ids = {e["id"] for e in final_entries}
            other_entries = [e for e in all_entries if e.get("owner") != owner and (e.get("owner") is not None)]
            # Also keep legacy entries that weren't part of this audit
            for e in all_entries:
                if e.get("owner") is None and e["id"] not in audited_ids and e["id"] not in {o["id"] for o in other_entries}:
                    other_entries.append(e)
            saved_entries = final_entries + other_entries
        else:
            saved_entries = final_entries
        memory_manager.save(saved_entries)
        logger.info(
            f"Memory audit complete: {before_count} -> {after_count} entries "
            f"({before_count - after_count} removed/merged)"
        )

        # Rebuild vector index from the full saved set, not just this owner's
        # slice — otherwise the shared collection is wiped of every other
        # owner's entries until they happen to run their own audit.
        if memory_vector and memory_vector.healthy:
            memory_vector.rebuild(saved_entries)

        # Persist the post-tidy fingerprint so the next call short-circuits
        # if nothing has changed in the meantime.
        _save_tidy_state(memory_manager, owner, _fingerprint_entries(final_entries))

        return {"before": before_count, "after": after_count}

    except Exception as e:
        logger.error(f"Memory audit failed: {e}")
        return {"error": str(e)}
