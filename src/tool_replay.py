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
