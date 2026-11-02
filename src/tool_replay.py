"""Prior-turn tool output replay for chat context.

Persisted history stores each assistant turn as ONE message carrying
metadata.tool_events = [{round, tool, desc, command, output, exit_code}, ...].
Raw role=tool results are only ever fed back WITHIN the current turn
(agent_loop._append_tool_results); on the NEXT turn the model sees just its
own prose narration of them. When it doubted that narration it had nothing
to check against, so it re-ran the same commands turn after turn purely to
re-verify outputs it had already received — or second-guessed accurate
recall entirely (the 2026-10-20 "14:32 boot time" incident).

prior_tool_outputs_context_message() rebuilds those persisted outputs into a
single tail context message so earlier tool results stay readable for the
whole session. Request-only: nothing here mutates saved history.

Turn labels ("turn -1", "turn -2", ...) are relative ordering among the
tool-using turns of the session, counted from newest.
"""

from __future__ import annotations

import hashlib
import json

from typing import Dict, List, Optional

# Per-output fidelity window before head+tail truncation kicks in.
OUTPUT_MAX_CHARS = 4000
OUTPUT_HEAD_CHARS = 2800
OUTPUT_TAIL_CHARS = 800
# Whole-digest cap; newest turns win, oldest are dropped first.
DIGEST_MAX_CHARS = 24000
# Command echo cap (a giant pasted heredoc is not worth replaying in full).
COMMAND_MAX_CHARS = 500

_HEADER = (
    "[Context: tool results from earlier turns in this session. These "
    "tools/commands already ran; the outputs below are authoritative. Do not "
    "re-run them just to re-verify — only call a tool again when you need "
    "NEW or different data.]"
)

# Native replay (2026-10-30): persisted tool_events are reconstructed as real
# assistant tool_calls + role=tool results in request history, so the model
# sees its own past calls in the exact shape the provider API expects. Without
# this, cross-turn history is prose-only and long sessions teach the model
# that turns end with narration instead of tool calls (the "announces the
# hunt, never fires the tool" failure — never occurs in a fresh session).
NATIVE_REPLAY_NOTE = (
    "[Context: earlier turns' tool calls and their outputs are replayed in "
    "history as native tool messages. They already ran — do not re-run them "
    "just to re-verify; only call a tool again when you need NEW or "
    "different data.]"
)
# Per-assistant-turn caps for native replay. Both are deterministic per
# message, so a given turn renders byte-identically on every request and
# local KV-cache prefixes survive (same slot reasoning as the digest above).
NATIVE_REPLAY_MAX_EVENTS_PER_TURN = 12
NATIVE_REPLAY_MAX_CHARS_PER_TURN = 16000


def _format_output(output) -> str:
    text = str(output or "").strip()
    if not text:
        return ""
    if len(text) <= OUTPUT_MAX_CHARS:
        return text
    dropped = len(text) - OUTPUT_HEAD_CHARS - OUTPUT_TAIL_CHARS
    return (
        text[:OUTPUT_HEAD_CHARS].rstrip()
        + f"\n[... {dropped} chars trimmed ...]\n"
        + text[-OUTPUT_TAIL_CHARS:].lstrip()
    )


def _format_event(event: Dict) -> str:
    tool = str(event.get("tool") or event.get("desc") or "tool").strip()
    command = str(event.get("command") or "").strip()
    if len(command) > COMMAND_MAX_CHARS:
        command = command[:COMMAND_MAX_CHARS].rstrip() + " ..."
    output = _format_output(event.get("output"))
    exit_code = event.get("exit_code")
    lines = [f"[{tool}]"]
    if command:
        lines.append(f"cmd: {command}")
    if output:
        lines.append(f"out:\n{output}")
    if exit_code not in (None, 0, "0"):
        lines.append(f"exit_code: {exit_code}")
    return "\n".join(lines)


def collect_prior_tool_event_groups(messages: List[Dict]) -> List[List[Dict]]:
    """Group persisted tool events per assistant turn, oldest first."""
    groups: List[List[Dict]] = []
    for message in messages or []:
        if not isinstance(message, dict):
            continue
        metadata = message.get("metadata")
        if not isinstance(metadata, dict):
            continue
        raw = metadata.get("tool_events")
        if not isinstance(raw, list):
            continue
        events = [e for e in raw if isinstance(e, dict)]
        if events:
            groups.append(events)
    return groups


def prior_tool_outputs_context_message(messages: List[Dict]) -> Optional[Dict]:
    """Build the replay message, or None when history has no tool events.

    Newest turns are kept under the char budget; when the budget runs out,
    the oldest turns are dropped and noted in the header.
    """
    groups = collect_prior_tool_event_groups(messages)
    if not groups:
        return None

    # The digest exists to carry OUTPUTS; an event whose output was never
    # persisted (empty) adds nothing re-verifiable and is skipped even if
    # it has a command echo.
    group_parts: List[List[str]] = []
    for g in groups:
        parts: List[str] = []
        for e in g:
            if not _format_output(e.get("output")):
                continue
            formatted = _format_event(e)
            if formatted.strip():
                parts.append(formatted)
        group_parts.append(parts)

    total = len(group_parts)
    budget = DIGEST_MAX_CHARS - len(_HEADER) - 64
    kept: List[str] = []  # newest first
    for idx in range(total - 1, -1, -1):
        parts = group_parts[idx]
        if not parts:
            continue
        block = f"--- turn -{total - idx} ---\n" + "\n\n".join(parts)
        if len(block) <= budget:
            kept.append(block)
            budget -= len(block) + 2
            continue
        if budget > 800:
            kept.append(block[:budget].rstrip() + "\n[... truncated ...]")
        break

    if not kept:
        return None

    contentful = sum(1 for p in group_parts if p)
    dropped_turns = contentful - len(kept)
    body = "\n\n".join(reversed(kept))
    header = _HEADER
    if dropped_turns > 0:
        header += (
            f" ({dropped_turns} earlier turn(s) with tool output omitted "
            f"for space)"
        )
    return {"role": "user", "content": f"{header}\n\n{body}"}


def _stable_call_id(content: str, tool: str, event_index: int, command: str) -> str:
    """Deterministic tool_call id derived from message content.

    Random ids would re-render history differently on every request and
    invalidate local KV-cache prefixes; a content-derived id keeps the
    rendered bytes stable across requests.
    """
    basis = f"{content[:200]}|{tool}|{event_index}|{command[:200]}"
    return "hist_" + hashlib.md5(basis.encode("utf-8", "ignore")).hexdigest()[:16]


def _native_args_for_event(command: str) -> str:
    """Best-effort arguments JSON for a persisted event's command echo.

    Most agent tools take a single ``command`` string; a few persist their
    full args dict as JSON (e.g. app_api). Pass JSON dicts through as-is,
    fall back to ``{"command": ...}`` otherwise. Historical arguments are
    not schema-validated by providers — the structural pattern (call +
    result pair) is what the model needs to see.
    """
    text = (command or "").strip()
    if text:
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict) and parsed:
                return json.dumps(parsed, ensure_ascii=False)
        except Exception:
            pass
    return json.dumps({"command": text}, ensure_ascii=False)


def replay_tool_events_as_native(messages: List[Dict]) -> int:
    """Reconstruct persisted metadata.tool_events as native assistant
    tool_calls + role=tool result messages, in place.

    For each assistant turn carrying tool_events, attach a tool_calls list
    built from the newest events (per-turn caps above) and splice matching
    role=tool result messages right after it. Deterministic per message:
    stable call ids, fixed truncation, fixed event selection — so rendered
    history stays byte-identical across requests.

    Returns the number of assistant messages augmented. Request-only:
    nothing here mutates saved history.
    """
    if not messages:
        return 0
    built: List[Dict] = []
    augmented = 0
    for message in messages:
        built.append(message)
        if not isinstance(message, dict) or message.get("role") != "assistant":
            continue
        if message.get("tool_calls"):
            continue  # already native — never double-replay
        metadata = message.get("metadata")
        if not isinstance(metadata, dict):
            continue
        raw = metadata.get("tool_events")
        if not isinstance(raw, list):
            continue
        events = [
            e for e in raw
            if isinstance(e, dict) and str(e.get("tool") or "").strip()
        ]
        if not events:
            continue
        # Newest events of the turn win when caps bite; the kept count is
        # deterministic per message, so re-renders stay stable.
        kept = events[-NATIVE_REPLAY_MAX_EVENTS_PER_TURN:]
        content = str(message.get("content") or "")
        calls: List[Dict] = []
        results: List[Dict] = []
        for ei, ev in enumerate(kept):
            tool = str(ev.get("tool")).strip()
            command = str(ev.get("command") or "")
            call_id = _stable_call_id(content, tool, ei, command)
            calls.append({
                "id": call_id,
                "type": "function",
                "function": {"name": tool, "arguments": _native_args_for_event(command)},
            })
            out = _format_output(ev.get("output")) or "(no output persisted)"
            exit_code = ev.get("exit_code")
            if exit_code not in (None, 0, "0"):
                out = f"{out}\n[exit_code: {exit_code}]"
            results.append({"role": "tool", "tool_call_id": call_id, "content": out})
        # Per-turn char budget: drop the oldest kept events until under cap
        # (never below one — a single oversized result still replays).
        while len(calls) > 1:
            total = sum(
                len(r.get("content") or "") + len(c["function"]["arguments"])
                for c, r in zip(calls, results)
            )
            if total <= NATIVE_REPLAY_MAX_CHARS_PER_TURN:
                break
            calls.pop(0)
            results.pop(0)
        if not calls:
            continue
        message["tool_calls"] = calls
        augmented += 1
        built.extend(results)
    if augmented:
        messages[:] = built
    return augmented


# --- Continue separator ------------------------------------------------------
# Synthetic tool pair injected on Continue (agent mode) so a stopped assistant
# row is never glued directly to the resumed generation: two adjacent
# assistant messages confuse models, and some providers reject them outright.
# Request-only, like the replay above — nothing here mutates saved history.
# The tool name is deliberately NOT in FUNCTION_TOOL_SCHEMAS, so the model can
# never call it; it only ever appears as injected history.

CONTINUE_SEPARATOR_TOOL = "odysseus_continue"
CONTINUE_SEPARATOR_OUTPUT = (
    "This tool call was auto-generated by Odysseus for the Continue function; "
    "the model did not call it. The assistant message above was interrupted "
    "mid-stream (e.g. HTTP 502/504) and is a partial reply — resume the response "
    "from where it stopped. Tool calls whose results already appear above have "
    "run; do not re-run them just to re-verify."
)


def inject_continue_separator(messages: List[Dict], is_api_model: bool) -> int:
    """Append a synthetic tool pair marking a Continue turn at the tail.

    API models: attach the synthetic call to the trailing assistant message
    (on a copy — never mutate the history row in place) or append a fresh
    assistant message, then the matching role=tool result, so the pair stays
    adjacent and the sanitizer sees an answered tool_call. Fenced/local
    models have no native tool role, so a plain user note separates the
    turns instead. Returns 1 when injected, 0 otherwise.
    """
    if not messages:
        return 0
    # Already persisted on the stopped row and replayed into this request?
    # Then the boundary exists — don't double-inject.
    for m in messages:
        for c in (m.get("tool_calls") or []):
            if isinstance(c, dict) and (c.get("function") or {}).get("name") == CONTINUE_SEPARATOR_TOOL:
                return 0
    call_id = "call_odysseus_continue"
    call = {
        "id": call_id,
        "type": "function",
        "function": {"name": CONTINUE_SEPARATOR_TOOL, "arguments": "{}"},
    }
    if is_api_model:
        last = messages[-1]
        if last.get("role") == "assistant":
            new_last = dict(last)
            calls = list(new_last.get("tool_calls") or [])
            calls.append(call)
            new_last["tool_calls"] = calls
            messages[-1] = new_last
        else:
            messages.append({"role": "assistant", "content": "", "tool_calls": [call]})
        messages.append({"role": "tool", "tool_call_id": call_id, "content": CONTINUE_SEPARATOR_OUTPUT})
    else:
        messages.append({
            "role": "user",
            "content": f"[Odysseus Continue] {CONTINUE_SEPARATOR_OUTPUT}",
        })
    return 1


def build_continue_separator_event(round_num: int = 1) -> Dict:
    """Synthetic tool_event persisted on a stopped assistant row at Continue.

    (2026-11-01) Renders in the UI through the normal tool_events path and
    replays as a native tool pair for API models, so the stopped row is never
    glued directly to the resumed generation — in the transcript or in context.
    The command is a JSON dict so native replay passes it through as arguments.
    """
    return {
        "tool": CONTINUE_SEPARATOR_TOOL,
        "command": json.dumps({"note": "auto-generated by Odysseus for the Continue function"}),
        "output": CONTINUE_SEPARATOR_OUTPUT,
        "exit_code": 0,
        "round": round_num,
        "synthetic": True,
    }
