"""Regression: stream_agent_loop emits `rounds_exhausted` only when the round
cap is hit while still working, and NOT on a normal finish.

The decision is a `for/else` in the loop: the `else` runs only if no `break`
fired (break = done / budget / error). A refactor that adds a stray break or
return, or moves the done-break, could silently flip this. See PR #1999 / #1997.
"""

import asyncio
import json

import src.agent_loop as al


def _collect(gen):
    async def _run():
        return [c async for c in gen]
    return asyncio.run(_run())


def _types(chunks):
    out = []
    for c in chunks:
        if c.startswith("data: ") and not c.startswith("data: [DONE]"):
            try:
                out.append(json.loads(c[6:]))
            except Exception:
                pass
    return out


def _patch_common(monkeypatch):
    # Skip RAG/tool-index, MCP, and settings lookups; keep the real loop body,
    # _resolve_tool_blocks, and parse_tool_blocks.
    monkeypatch.setattr(al, "get_setting", lambda key, default=None: default, raising=False)
    monkeypatch.setattr(al, "get_mcp_manager", lambda: None, raising=False)
    monkeypatch.setattr(al, "estimate_tokens", lambda *a, **k: 10, raising=False)

    async def _fake_exec(block, *a, **k):
        return (block.tool_type, {"output": "ok", "exit_code": 0})
    monkeypatch.setattr(al, "execute_tool_block", _fake_exec, raising=False)


def _run_loop(monkeypatch, round_text, max_rounds=2):
    async def _fake_stream(_candidates, messages, **kwargs):
        yield f'data: {json.dumps({"delta": round_text})}\n\n'
        yield "data: [DONE]\n\n"
    monkeypatch.setattr(al, "stream_llm_with_fallback", _fake_stream, raising=False)

    gen = al.stream_agent_loop(
        "http://x/v1", "m",
        [{"role": "user", "content": "do a long multi-step task"}],
        max_rounds=max_rounds,
        relevant_tools={"bash"},
    )
    return _types(_collect(gen))


def test_emits_rounds_exhausted_when_cap_hit_mid_task(monkeypatch):
    _patch_common(monkeypatch)
    # Use a system-owned interaction result so this remains a loop-control test:
    # Bash output is workspace-derived and now correctly pauses for exact user
    # approval before a later Bash call.
    events = _run_loop(
        monkeypatch,
        '```update_plan\n{"plan":"- [ ] keep going"}\n```',
        max_rounds=2,
    )
    assert any(e.get("type") == "rounds_exhausted" for e in events), events


def test_no_rounds_exhausted_on_normal_finish(monkeypatch):
    _patch_common(monkeypatch)
    # A plain answer (no tool block) -> done-break on round 1 -> no event.
    events = _run_loop(monkeypatch, "All done, here is your answer.", max_rounds=2)
    assert not any(e.get("type") == "rounds_exhausted" for e in events), events


def test_intent_without_action_is_flagged_not_nudged_or_killed(monkeypatch):
    """2026-10-31: the intent-without-action guard is PASSIVE. It must not
    emit intent_nudge_exhausted, must not burn rounds re-asking the model,
    and must flag the message instead (visible ⚠ note + metrics flag)."""
    _patch_common(monkeypatch)

    events = _run_loop(monkeypatch, "Let me check the logs", max_rounds=5)

    assert not any(e.get("type") == "intent_nudge_exhausted" for e in events), events
    assert not any(e.get("type") == "rounds_exhausted" for e in events), events
    assert any("⚠" in (e.get("delta") or "") for e in events), events
    assert any(
        e.get("type") == "metrics" and e.get("data", {}).get("tool_claims_unverified")
        for e in events
    ), events


def test_hallucinated_work_log_with_zero_tools_is_flagged(monkeypatch):
    """A work-log narration with zero tools run is still flagged (passively)."""
    _patch_common(monkeypatch)

    events = _run_loop(
        monkeypatch,
        "Updating the tally, then batch 8. Applied the edits and saved the file.",
        max_rounds=5,
    )
    assert any("⚠" in (e.get("delta") or "") for e in events), events
    assert not any(e.get("type") == "intent_nudge_exhausted" for e in events), events


def test_wrap_up_summary_after_real_tools_is_not_flagged(monkeypatch):
    """Corroborated wrap-up summary (tools ran earlier + conclusion language)
    is the model FINISHING — not flagged, not nudged, not killed.
    Regression for specimen 6c157fb3 (rounds 27-29 re-written summaries)."""
    _patch_common(monkeypatch)

    rounds = iter([
        '```update_plan\n{"plan":"- [ ] fix the popup"}\n```',
        "Fixed and verified — all done. No restart needed, just reload the page.",
    ])

    async def _fake_stream(_candidates, messages, **kwargs):
        yield f'data: {json.dumps({"delta": next(rounds)})}\n\n'
        yield "data: [DONE]\n\n"

    monkeypatch.setattr(al, "stream_llm_with_fallback", _fake_stream, raising=False)
    gen = al.stream_agent_loop(
        "http://x/v1", "m",
        [{"role": "user", "content": "fix the thinking popup in the chat box"}],
        max_rounds=5,
        relevant_tools={"bash"},
    )
    events = _types(_collect(gen))
    assert not any("⚠" in (e.get("delta") or "") for e in events), events
    assert not any(
        e.get("type") == "metrics" and e.get("data", {}).get("tool_claims_unverified")
        for e in events
    ), events


def test_emits_loop_breaker_triggered_when_loop_breaker_trips(monkeypatch):
    _patch_common(monkeypatch)

    events = _run_loop(
        monkeypatch,
        '```update_plan\n{"plan":"- [ ] keep going"}\n```',
        max_rounds=6,
    )

    guard = next((e for e in events if e.get("type") == "loop_breaker_triggered"), None)
    assert guard is not None, events
    assert guard["reason"] == "loop_breaker_stall"
