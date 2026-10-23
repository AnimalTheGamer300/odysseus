"""
context_compactor.py

Auto-compacts conversation history when approaching context window limits.
Summarizes older messages via the same LLM, preserving key context.
"""

import json
import logging
import re
from typing import Any, Dict, List, Optional

from src.model_context import get_context_length, estimate_tokens
from src.llm_core import llm_call_async
from src.endpoint_resolver import resolve_endpoint
from core.models import ChatMessage

logger = logging.getLogger(__name__)


def _content_as_text(content: Any) -> str:
    """Flatten a message's content to plain text.

    Handles the three shapes that flow through history: a plain string, a
    multimodal list of content blocks (vision/image attachments), and None
    (assistant turns that carried only native tool_calls persist content as
    None). Returns "" for anything without text so callers can safely slice
    the result.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            b.get("text", "") for b in content
            if isinstance(b, dict) and b.get("text")
        )
    return ""


COMPACT_THRESHOLD = 0.85  # Trigger compaction at 85% of context window
SUMMARY_MAX_TOKENS = 2048  # Floor: small compactions stay cheap and tight.
# Ceiling: the summary must never re-consume a large share of the context it
# just freed. 16384 tokens ≈ 64KB ≈ 12k words — beyond any session's genuinely
# non-redundant state (file paths, decisions, todos); past that the marginal
# bullets are mostly rephrasing. Cranked from 4096 on request 2026-08-09.
SUMMARY_MAX_TOKENS_HARD = 16384
# Adaptive budget: scales with how much context the summary replaces, capped at
# 12.5% of the freed tokens (older // 8) and clamped to [floor, ceiling].
# A big coding-session compaction legitimately gets more room; a small chat
# stays cheap. Cost is moot (free models), but determinism isn't — an uncapped
# summary would re-fill the window it just emptied and skew the next
# compaction's split math.
SUMMARY_REPLACE_FRACTION = 8
SMALL_CONTEXT_LIMIT = 8192  # Models with context <= this get aggressive trimming

# Cursor-style self-summarization prompt — produces structured, dense summaries
SELF_SUMMARY_SYSTEM_PROMPT = """You are summarizing a conversation to preserve context after compaction. Produce a structured summary that lets the conversation continue seamlessly.

Use this format:

## Conversation Summary
**Turns summarized:** {count}  |  **Compactions so far:** {n}

### User Goal
One sentence describing what the user is trying to accomplish.

### What Was Done
- Bullet points of completed actions, decisions made, and key outputs
- Include specific file paths, function names, variable names, URLs, and config values
- Note any errors encountered and how they were resolved

### Current State
What is the system/code/task state right now? What was the last thing discussed?

### Pending / Next Steps
- What remains to be done
- Any open questions or blockers

### Key Context
- Important constraints, preferences, or decisions that must not be forgotten
- Specific values: model names, ports, paths, credentials references, versions

Use the token budget available ({budget} tokens max) — be dense, every token should carry information. Spend more of the budget when the session was long or high-stakes (file paths, function names, decisions, config values); spend less when little happened. Do not include pleasantries or meta-commentary."""


_THINK_BLOCK_RE = re.compile(
    r"<mm:think[^>]*>.*?</mm:think>|<think>.*?</think>",
    re.DOTALL | re.IGNORECASE,
)


def _strip_think_blocks(text: str) -> str:
    """Remove visible reasoning blocks (<think>…</think>, <mm:think>…</mm:think>).

    Some gateways serve a thinking model's chain-of-thought as content tags
    instead of a reasoning_content field; those blocks must never land in a
    persisted compaction summary. Defense-in-depth on top of the compactor's
    disable_thinking=True summary call.
    """
    if not text:
        return text
    return _THINK_BLOCK_RE.sub("", text).strip()


def _message_excerpt(text: str, max_chars: int = 1600) -> str:
    """Keep head+tail of a long message so decisions at the END aren't lost.

    The old compactor cut every message at its first 2000 chars — for a long
    user paste or a big tool result, the resolution/result at the bottom was
    silently dropped from the summary input. Head+tail keeps both ends with a
    visible ellipsis marker.
    """
    if not isinstance(text, str) or not text:
        return ""
    if len(text) <= max_chars:
        return text
    head = max(200, int(max_chars * 0.65))
    tail = max(120, max_chars - head)
    return (
        text[:head].rstrip()
        + "\n…[middle truncated]…\n"
        + text[-tail:].lstrip()
    )


def _build_convo_text(older: List[Dict], max_chars: Optional[int] = None,
                      per_msg_chars: int = 1600) -> str:
    """Flatten the older half into the summarizer's input text.

    Each message is head+tail truncated (``_message_excerpt``). When
    ``max_chars`` is set, messages are dropped from the OLDEST end once the
    total exceeds it, with a visible notice — so a huge conversation can't
    blow the summary model's own context window, and the most recent (most
    relevant) context is the last to go.
    """
    lines = []
    total = 0
    for msg in older:
        line = f"{msg.get('role', 'user').upper()}: {_message_excerpt(_content_as_text(msg.get('content')), per_msg_chars)}"
        lines.append(line)
        total += len(line) + 1
    if max_chars is not None and max_chars > 0 and total > max_chars:
        # Drop from the OLDEST end: recent context matters more than old.
        dropped = 0
        while lines and total > max_chars:
            removed = lines.pop(0)
            total -= len(removed) + 1
            dropped += 1
        if dropped:
            lines.insert(
                0,
                f"…[{dropped} earliest message(s) omitted — summary input budget reached]…",
            )
    return "\n".join(lines)


def normalize_compaction_summary(summary: str) -> str:
    """Remove redundant leading title text before adding our wrapper."""
    text = (summary or "").strip()
    text = _strip_think_blocks(text)
    text = re.sub(r"^(?:#{1,3}\s*)?Conversation Summary\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^\*\*Conversation Summary\*\*\s*", "", text, flags=re.IGNORECASE)
    return text.lstrip()


def normalize_compaction_summary(summary: str) -> str:
    """Remove redundant leading title text before adding our wrapper."""
    text = (summary or "").strip()
    text = re.sub(r"^(?:#{1,3}\s*)?Conversation Summary\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^\*\*Conversation Summary\*\*\s*", "", text, flags=re.IGNORECASE)
    return text.lstrip()


def _sanitize_tool_messages(msgs: List[Dict]) -> List[Dict]:
    """Drop orphaned `tool` messages and dangling assistant `tool_calls`.

    OpenAI's API requires every `role:"tool"` message to immediately
    follow an assistant message that carries `tool_calls` (or another
    tool message in the same batch). Front-trimming the history can cut
    the assistant `tool_calls` parent while keeping its tool responses,
    which triggers: "messages with role 'tool' must be a response to a
    preceding message with 'tool_calls'". This pass repairs that:
      - drops `tool` messages with no valid preceding tool_calls
      - drops assistant `tool_calls` messages whose tool responses were
        all trimmed away (some providers reject unanswered tool_calls)
    """
    # Pass 1: drop orphan tool messages.
    cleaned: List[Dict] = []
    in_batch = False  # are we right after an assistant tool_calls (or mid-batch)?
    for m in msgs:
        role = m.get("role")
        if role == "tool":
            if in_batch:
                cleaned.append(m)
            # else: orphan — drop
            continue
        if role == "assistant" and m.get("tool_calls"):
            in_batch = True
        else:
            in_batch = False
        cleaned.append(m)

    # Pass 2: drop assistant tool_calls messages that have NO following
    # tool response (dangling) — walk backwards so we know what follows.
    out: List[Dict] = []
    for i, m in enumerate(cleaned):
        if m.get("role") == "assistant" and m.get("tool_calls"):
            nxt = cleaned[i + 1] if i + 1 < len(cleaned) else None
            if not (nxt and nxt.get("role") == "tool"):
                # Dangling tool_calls — keep the message but strip the
                # tool_calls so it's a plain assistant turn (preserves any
                # text content the model produced alongside the calls).
                m = {k: v for k, v in m.items() if k != "tool_calls"}
                if not (m.get("content") or "").strip():
                    continue  # nothing left worth keeping
        out.append(m)
    return out


def _message_text_token_estimate(text: str) -> int:
    if not isinstance(text, str):
        return 4
    return int(len(text) * 0.3) + 4


def _truncate_text_to_token_budget(text: str, token_budget: int) -> str:
    """Trim a too-large current user message instead of dropping it entirely."""
    if token_budget <= 32:
        return "[Current user message omitted: it exceeded the model context window.]"

    if not isinstance(text, str):
        # This helper is typed/used as text downstream, so return an empty
        # string rather than the raw non-string (which would move the crash
        # into the caller that concatenates/measures the result).
        return ""
    # Match src.model_context.estimate_tokens' rough chars * 0.3 estimate.
    max_chars = max(200, int((token_budget - 16) / 0.3))
    if len(text) <= max_chars:
        return text

    notice = (
        "\n\n[Notice: the pasted message was too large for this model's context "
        "window, so Odysseus kept the beginning and end.]"
    )
    keep_chars = max(200, max_chars - len(notice))
    head_len = max(100, int(keep_chars * 0.7))
    tail_len = max(80, keep_chars - head_len)
    return text[:head_len].rstrip() + notice + "\n\n" + text[-tail_len:].lstrip()


def _truncate_tool_call_args(msg: Dict[str, Any], token_budget: int) -> Dict[str, Any]:
    """Shrink oversized assistant ``tool_calls`` arguments to fit ``token_budget``.

    A tool-only turn persists ``content=None`` with its whole payload in
    ``tool_calls[].function.arguments`` (e.g. a large create_document body), which
    the text-content truncation can't reach — so the message could stay over
    budget and the upstream call would 400. Replace each argument string that
    overflows its share of the budget with a small valid-JSON placeholder,
    preserving ``id``/``type``/``function.name`` so tool/result pairing and
    provider validation are unaffected. Returns msg unchanged when there is
    nothing oversized.
    """
    tool_calls = msg.get("tool_calls")
    if not isinstance(tool_calls, list) or not tool_calls:
        return msg
    # Budget left after whatever content survived (estimate_tokens counts tool
    # arguments too, so measure content alone here).
    content_tokens = estimate_tokens([{"role": msg.get("role", "assistant"), "content": msg.get("content")}])
    per_call = max(16, (max(0, token_budget - content_tokens)) // len(tool_calls))
    new_calls = []
    changed = False
    for tc in tool_calls:
        fn = tc.get("function") if isinstance(tc, dict) else None
        args = fn.get("arguments") if isinstance(fn, dict) else None
        if isinstance(args, str) and int(len(args) * 0.3) > per_call:
            new_fn = dict(fn)
            new_fn["arguments"] = json.dumps({"_truncated_for_context": len(args)})
            new_tc = dict(tc)
            new_tc["function"] = new_fn
            new_calls.append(new_tc)
            changed = True
        else:
            new_calls.append(tc)
    if not changed:
        return msg
    out = dict(msg)
    out["tool_calls"] = new_calls
    return out


def _truncate_message_to_token_budget(msg: Dict[str, Any], token_budget: int) -> Dict[str, Any]:
    """Return a copy of msg whose text content (and tool-call args) fit token_budget."""
    out = dict(msg)
    content = out.get("content", "")
    if isinstance(content, str):
        out["content"] = _truncate_text_to_token_budget(content, token_budget)
    elif isinstance(content, list):
        remaining = token_budget
        new_content = []
        for item in content:
            if not isinstance(item, dict) or item.get("type") != "text":
                new_content.append(item)
                continue
            text = item.get("text", "")
            truncated = _truncate_text_to_token_budget(text, remaining)
            cloned = dict(item)
            cloned["text"] = truncated
            new_content.append(cloned)
            remaining -= _message_text_token_estimate(truncated)
        out["content"] = new_content
    # A tool-only turn (content=None) carries its payload in tool_calls args,
    # which the branches above can't shrink — handle it so the message can fit.
    return _truncate_tool_call_args(out, token_budget)


def trim_for_context(messages: List[Dict], context_length: int, reserve_tokens: int = 512) -> List[Dict]:
    """Trim system messages to fit within context_length.

    For small-context models, progressively strips:
    1. RAG/memory system messages (keep preset system prompt)
    2. Older conversation turns
    Reserves space for the response.
    """
    budget = context_length - reserve_tokens
    used = estimate_tokens(messages)
    if used <= budget:
        return messages

    logger.info(f"Trimming messages: {used} tokens > {budget} budget (ctx={context_length})")

    # Separate system messages from conversation.
    # Messages marked _protected (e.g. active document) are never trimmed.
    system_msgs = []
    protected_msgs = []
    convo_msgs = []
    for msg in messages:
        if msg.get("_protected"):
            protected_msgs.append(msg)
        elif msg.get("role") == "system":
            system_msgs.append(msg)
        else:
            convo_msgs.append(msg)

    # Protected messages count toward budget but are never dropped
    protected_tokens = estimate_tokens(protected_msgs)
    budget -= protected_tokens

    # Priority: keep first system msg (preset prompt), drop others (memory, RAG, memo).
    # Exception: a research-spinoff primer (the seeded report that grounds a
    # "Discuss" chat) must never be dropped — it is the conversation's whole
    # knowledge base. Treat any system message carrying research_spinoff_from
    # metadata as essential alongside the leading system prompt.
    def _is_research_primer(m):
        return bool((m.get("metadata") or {}).get("research_spinoff_from"))
    _primers = [m for m in system_msgs if _is_research_primer(m)]
    _non_primer = [m for m in system_msgs if not _is_research_primer(m)]
    essential_system = (_non_primer[:1] if _non_primer else []) + _primers
    extra_system = _non_primer[1:]

    # Try dropping extra system messages one by one (from the end)
    trimmed = essential_system + convo_msgs
    if estimate_tokens(trimmed) <= budget:
        # Dropping extras was enough — try adding back some
        result = list(essential_system)
        for msg in extra_system:
            candidate = result + [msg] + convo_msgs
            if estimate_tokens(candidate) <= budget:
                result.append(msg)
            else:
                break
        return _sanitize_tool_messages(result + protected_msgs + convo_msgs)

    # Still too big — truncate the first system message (but keep more than 500 chars)
    if essential_system:
        sys_text = essential_system[0].get("content", "")
        if len(sys_text) > 2000:
            truncated_system = dict(essential_system[0])
            truncated_system["content"] = sys_text[:2000] + "\n[System prompt truncated for context limits]"
            essential_system[0] = truncated_system
            trimmed = essential_system + convo_msgs
            if estimate_tokens(trimmed) <= budget:
                return _sanitize_tool_messages(essential_system + protected_msgs + convo_msgs)

    # Still too big — drop older conversation turns BUT always keep the current
    # user turn. If a pasted message alone exceeds the model context, truncate
    # that message with a visible notice instead of dropping it; otherwise the
    # model appears to "ignore" large pastes because it never receives them.
    # Hermes-style: recent context matters more than old context.
    PROTECT_RECENT = 10
    current_msg = convo_msgs[-1:] if convo_msgs else []
    prior_convo = convo_msgs[:-1] if convo_msgs else []
    if len(prior_convo) >= PROTECT_RECENT:
        old_msgs = prior_convo[:-(PROTECT_RECENT - 1)]
        recent_msgs = prior_convo[-(PROTECT_RECENT - 1):] + current_msg
        while old_msgs and estimate_tokens(essential_system + old_msgs + recent_msgs) > budget:
            old_msgs.pop(0)
        convo_msgs = old_msgs + recent_msgs
    else:
        convo_msgs = prior_convo + current_msg
        while prior_convo and estimate_tokens(essential_system + prior_convo + current_msg) > budget:
            prior_convo.pop(0)
        convo_msgs = prior_convo + current_msg

    # If the current message itself is too large, shrink only that message.
    if current_msg and estimate_tokens(essential_system + protected_msgs + convo_msgs) > budget:
        prefix = essential_system + protected_msgs + convo_msgs[:-1]
        available_for_current = max(64, budget - estimate_tokens(prefix))
        convo_msgs[-1] = _truncate_message_to_token_budget(convo_msgs[-1], available_for_current)

    result = _sanitize_tool_messages(essential_system + protected_msgs + convo_msgs)
    logger.info(f"Trimmed to {estimate_tokens(result)} tokens ({len(result)} messages)")
    return result


async def maybe_compact(
    session,
    endpoint_url: str,
    model: str,
    messages: List[Dict],
    headers: Optional[Dict] = None,
    force_threshold_tokens: Optional[int] = None,
    owner: Optional[str] = None,
    *,
    persist: bool = True,
    compaction_state: Optional[Dict[str, Any]] = None,
) -> tuple:
    """Check context usage and compact if above threshold.

    With `force_threshold_tokens` set, compaction triggers on the absolute
    accumulated token count instead of a percentage of the model context
    window (used by the agent loop to bound a single multi-round request).

    Returns (messages, context_length, was_compacted).
    """
    context_length = get_context_length(endpoint_url, model)
    used = estimate_tokens(messages)
    pct = (used / context_length) * 100 if context_length else 0

    if force_threshold_tokens is not None:
        if used < force_threshold_tokens:
            return messages, context_length, False
        logger.info(
            f"Context at {used} tokens — force-compacting (threshold={force_threshold_tokens})"
        )
    else:
        if pct < COMPACT_THRESHOLD * 100:
            return messages, context_length, False
        logger.info(
            f"Context at {pct:.1f}% ({used}/{context_length} tokens) — compacting"
        )

    # Split into system preface and conversation
    system_msgs = []
    convo_msgs = []
    for msg in messages:
        if msg.get("role") == "system":
            system_msgs.append(msg)
        else:
            convo_msgs.append(msg)

    if len(convo_msgs) < 4:
        return messages, context_length, False

    # Split conversation: summarize older half, keep recent half
    split_point = len(convo_msgs) // 2
    older = convo_msgs[:split_point]
    recent = convo_msgs[split_point:]

    # Build the text to summarize
    # Use utility model if configured, otherwise fall back to session model
    util_url, util_model, util_headers = resolve_endpoint("utility", owner=owner)
    compact_url = util_url or endpoint_url
    compact_model = util_model or model
    compact_headers = util_headers if util_url else headers

    # Cap the summarizer's INPUT so a huge older half can't blow the summary
    # model's own context window (which would 400 or silently truncate).
    # Reserve ~45% of the window for the summary prompt + the generated
    # summary itself; chars ≈ tokens / 0.3 under our estimate.
    _summary_ctx = get_context_length(compact_url, compact_model)
    _input_budget_chars = int(_summary_ctx * 0.55 / 0.3)
    convo_text = _build_convo_text(older, max_chars=_input_budget_chars)

    # Count prior compactions from existing summary messages
    compaction_count = sum(
        1 for m in system_msgs
        if "[Conversation summary" in m.get("content", "")
    )

    # Adaptive summary budget: scale with the size of what's being replaced, so
    # a big coding-session compaction legitimately gets more room while a small
    # chat stays cheap. Clamped to [SUMMARY_MAX_TOKENS, SUMMARY_MAX_TOKENS_HARD]
    # so the summary can never re-consume more than ~12.5% of the context it
    # just freed.
    older_tokens = estimate_tokens(older)
    summary_budget = max(
        SUMMARY_MAX_TOKENS,
        min(SUMMARY_MAX_TOKENS_HARD, older_tokens // SUMMARY_REPLACE_FRACTION),
    )

    prompt = SELF_SUMMARY_SYSTEM_PROMPT.replace(
        "{count}", str(len(older))
    ).replace(
        "{n}", str(compaction_count + 1)
    ).replace(
        "{budget}", str(summary_budget)
    )
    summary_messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": convo_text},
    ]

    try:
        # finish_reason detection: a summary cut at max_tokens silently
        # amputates the tail — usually the "Pending / Next Steps" section,
        # exactly what the next turn needs. Detect it, retry once at the
        # ceiling when the budget was below it, and if it still truncates,
        # mark the summary so the incompleteness is visible downstream.
        async def _summarize(max_tok):
            _r = await llm_call_async(
                compact_url,
                compact_model,
                summary_messages,
                temperature=0.2,
                max_tokens=max_tok,
                headers=compact_headers,
                timeout=30,
                # Never let the summarizer reason: a thinking model emits
                # chain-of-thought into reasoning_content (content stays
                # empty), which the old code returned as the "summary" — a
                # cut-off internal monologue instead of a summary — and it
                # burns the whole max_tokens budget on thinking before the
                # real summary is written
                # (ODYSSEUS_DEEPSEEK_V4_THINKING=1 + reasoning_content
                # fallback; fixed 2026-08-09).
                disable_thinking=True,
                return_finish_reason=True,
            )
            if isinstance(_r, tuple):
                return _r
            # Defensive: a stubbed/cached caller may return bare text —
            # treat it as untruncated.
            return _r, None

        summary, finish_reason = await _summarize(summary_budget)
        if finish_reason in ("length", "max_tokens") and summary_budget < SUMMARY_MAX_TOKENS_HARD:
            logger.info(
                f"Summary truncated at {summary_budget} tokens (finish_reason="
                f"{finish_reason}) — retrying once at the "
                f"{SUMMARY_MAX_TOKENS_HARD}-token ceiling"
            )
            summary, finish_reason = await _summarize(SUMMARY_MAX_TOKENS_HARD)
        if finish_reason in ("length", "max_tokens"):
            logger.warning(
                f"Compaction summary truncated at {SUMMARY_MAX_TOKENS_HARD} tokens "
                f"(finish_reason={finish_reason}) — summary may be incomplete"
            )
            summary = summary.rstrip() + (
                "\n\n[Summary truncated at max tokens — some details may be missing]"
            )
    except Exception as e:
        logger.error(f"Compaction summary failed: {e}")
        # Degrade gracefully: keep the conversation intact rather than
        # silently dropping the older half. was_compacted=False signals the
        # caller nothing was summarized; trim_for_context handles length.
        return messages, context_length, False
    summary = normalize_compaction_summary(summary)
    if not summary.strip():
        logger.error(
            "Compaction summary empty (model %s returned no content with "
            "thinking disabled) — skipping compaction instead of persisting "
            "an empty summary", compact_model,
        )
        return messages, context_length, False

    summary_msg = {
        "role": "system",
        "content": f"[Conversation summary — earlier messages were compacted]\n{summary}",
    }

    compacted = system_msgs + [summary_msg] + recent

    # Update session history to match. split_point is indexed against
    # convo_msgs, which mixes ephemeral preface injections (memory, RAG,
    # search context, date context) into the conversation — a raw
    # system_msg_count offset assumed the message list mirrored history and
    # shifted the slice, permanently dropping recent turns from the
    # persisted transcript (2026-08-08, see changelog). Map the split onto
    # session.history via _db_id matching; if the mapping can't be
    # established, leave history untouched rather than risk corrupting it.
    # Deferred routes (persist=False) record the plan in compaction_state
    # and apply it after the winning route commits — the mapping then runs
    # against the resolved session (it may be None at construction time).
    history_split = (
        _map_convo_split_to_history(session, messages, split_point)
        if session is not None else None
    )
    if compaction_state is not None:
        compaction_state.update({
            "split_point": split_point,
            "messages": messages,
            "history_split": history_split,
            "summary": summary,
            "applied": False,
        })
    if persist:
        if history_split is not None:
            _update_session_history(session, history_split, summary)
            if compaction_state is not None:
                compaction_state["applied"] = True

    new_used = estimate_tokens(compacted)
    logger.info(
        f"Compacted: {used} -> {new_used} tokens "
        f"({len(older)} messages summarized, {len(recent)} kept)"
    )

    return compacted, context_length, True


def _map_convo_split_to_history(session, messages, split_point):
    """Map a convo_msgs split index back to an index into session.history.

    `messages` = ephemeral preface (system prompts + user-role injections
    like search context / date context) + the persisted history, so the
    split computed on convo_msgs does not translate directly to
    session.history. History messages are matched by ``_db_id`` metadata
    (falling back to role+content for never-persisted messages) and
    counted in order across the summarized range; leading system messages
    in history (prior compaction summaries) fold into the summarized
    portion.

    Returns None when the mapping can't be established — the caller then
    leaves history untouched (safe) instead of corrupting it.
    """
    if not session or not getattr(session, "history", None):
        return None
    convo_msgs = [m for m in messages if m.get("role") != "system"]
    if split_point <= 0 or split_point >= len(convo_msgs):
        return None

    hist_msgs = [
        m for m in session.history
        if (m.metadata or {}).get("source") != "slash"
    ]
    if not hist_msgs:
        return None

    anchor_idx = next(
        (i for i, m in enumerate(hist_msgs) if m.role != "system"), None
    )
    if anchor_idx is None:
        return None
    anchor = hist_msgs[anchor_idx]

    def _same_message(hist_msg, convo_msg):
        hid = (hist_msg.metadata or {}).get("_db_id")
        cid = (convo_msg.get("metadata") or {}).get("_db_id")
        if hid and cid:
            return hid == cid
        return (
            hist_msg.role == convo_msg.get("role")
            and hist_msg.content == convo_msg.get("content")
        )

    # Locate the first history message inside convo_msgs
    start = None
    for i, cm in enumerate(convo_msgs):
        if _same_message(anchor, cm):
            start = i
            break
    if start is None:
        return None

    # Walk the summarized range, counting history messages it covers.
    # Ephemeral wedges (date context, etc.) don't match and don't advance.
    idx = anchor_idx
    count = 0
    for k in range(start, split_point):
        if idx >= len(hist_msgs):
            break
        if _same_message(hist_msgs[idx], convo_msgs[k]):
            count += 1
            idx += 1
    if count == 0:
        return None

    # Leading system messages (prior compaction summaries) are replaced by
    # this summary, so they count toward the summarized portion too.
    return anchor_idx + count


def _update_session_history(session, history_split: int, summary: str):
    """Replace the older portion of session.history with the summary.

    `history_split` is an index into session.history: everything before it
    is summarized away, everything from it on is kept verbatim. The
    summary is prepended so the transcript reads [summary, recent…] — the
    same layout as the manual compact path.
    """
    if not session or not hasattr(session, "history"):
        return
    if history_split <= 0 or history_split >= len(session.history):
        logger.warning(
            "Compaction: skipping history rewrite (history_split=%s, history_len=%s)",
            history_split, len(session.history),
        )
        return

    summary = normalize_compaction_summary(summary)
    summary_msg = ChatMessage(
        role="system",
        content=f"[Conversation summary]\n{summary}",
        metadata={"compacted": True, "summarized_count": history_split},
    )
    new_history = [summary_msg] + list(session.history[history_split:])
    if len(new_history) >= len(session.history):
        logger.warning(
            "Compaction: refusing non-shrinking history rewrite "
            "(history_split=%s, history_len=%s)",
            history_split, len(session.history),
        )
        return
    try:
        from core.models import get_session_manager_instance
        manager = get_session_manager_instance()
    except Exception:
        manager = None
    if manager and getattr(session, "id", None):
        if manager.replace_messages(session.id, new_history):
            return
    session.history = new_history


def apply_compaction_state(session, compaction_state: Optional[Dict[str, Any]]) -> bool:
    """Persist a route-specific compaction after that route commits output.

    Candidate prompts may be compacted speculatively while an explicit
    foreground fallback chain is being tried.  Persisting at construction time
    would let an unavailable route rewrite history before another route answers,
    so callers hold this small plan and apply only the winning route's plan.

    The plan stores the convo-index split plus the message list it was computed
    against; the convo-to-history mapping (2026-08-08) runs here against the
    resolved session — either eagerly recorded at construction time (session
    was available) or deferred to now (session was None during speculation).
    """
    state = compaction_state if isinstance(compaction_state, dict) else None
    if not state or state.get("applied"):
        return False
    summary = state.get("summary")
    split_point = state.get("split_point")
    if not isinstance(summary, str) or not isinstance(split_point, int):
        return False
    history_split = state.get("history_split")
    if not isinstance(history_split, int):
        messages = state.get("messages")
        if not isinstance(messages, list):
            return False
        history_split = _map_convo_split_to_history(session, messages, split_point)
        if history_split is None:
            logger.warning(
                "Compaction: deferred plan dropped — history mapping failed "
                "(split_point=%s, history_len=%s)",
                split_point, len(getattr(session, "history", []) or []),
            )
            return False
        state["history_split"] = history_split
    _update_session_history(session, history_split, summary)
    state["applied"] = True
    return True


def apply_compaction_state_for_session(
    session_id: Optional[str],
    compaction_state: Optional[Dict[str, Any]],
) -> bool:
    """Resolve an in-memory session and apply a deferred compaction plan."""
    if not session_id:
        return False
    try:
        from core.models import get_session_manager_instance

        manager = get_session_manager_instance()
        session = manager.get_session(session_id) if manager else None
    except Exception:
        session = None
    return apply_compaction_state(session, compaction_state) if session else False
