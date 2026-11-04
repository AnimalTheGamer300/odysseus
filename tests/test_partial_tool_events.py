"""2026-10-11 defenestration fix: a force-stopped agent turn must keep the
tool calls that already executed.

Before the fix, tool_events/round_texts only escaped stream_agent_loop via
the final metrics event — a client disconnect (aclose) killed the generator
before that event fired, and _persist_stream_partial saved text+thinking
only. The partial_sink now publishes live handles so the stop path can
snapshot executed tool calls instead of saving narration-without-calls.
"""
import asyncio
import json

import src.agent_loop as al
from routes.chat_routes import _persist_stream_partial, _sink_tool_state


class _FakeSess:
    def __init__(self):
        self.messages = []

    def add_message(self, msg):
        self.messages.append(msg)


class _FakeSM:
    def __init__(self):
        self.saved = 0

    def save_sessions(self):
        self.saved += 1


def test_sink_tool_state_empty():
    assert _sink_tool_state(None) == ([], [])
    assert _sink_tool_state({}) == ([], [])


def test_sink_tool_state_snapshots_and_appends_inflight():
    sink = {
        "tool_events": [{"round": 1, "tool": "bash", "command": "ls", "output": "ok", "exit_code": 0}],
        "round_texts": ["first round"],
        "current_round_text": "  partial second  ",
    }
    events, texts = _sink_tool_state(sink)
    assert events[0]["tool"] == "bash"
    assert texts == ["first round", "partial second"]
    # Snapshot copies the lists — later sink mutation must not leak in.
    sink["tool_events"].append({"round": 2, "tool": "read_file"})
    assert len(events) == 1


def test_sink_tool_state_skips_blank_inflight():
    sink = {"tool_events": [], "round_texts": ["done"], "current_round_text": "   "}
    assert _sink_tool_state(sink) == ([], ["done"])


def test_persist_partial_keeps_tool_events():
    sess, sm = _FakeSess(), _FakeSM()
    ok = _persist_stream_partial(
        sess, sm, "s1", "reply text", "",
        tool_events=[{"round": 1, "tool": "bash", "command": "ls", "output": "ok", "exit_code": 0}],
        round_texts=["round one"],
    )
    assert ok and sm.saved == 1
    msg = sess.messages[-1]
    assert msg.metadata["stopped"] is True
    assert msg.metadata["tool_events"][0]["command"] == "ls"
    assert msg.metadata["round_texts"] == ["round one"]


def test_persist_partial_without_tool_state_unchanged():
    sess, sm = _FakeSess(), _FakeSM()
    assert _persist_stream_partial(sess, sm, "s1", "reply", "")
    msg = sess.messages[-1]
    assert msg.metadata["stopped"] is True
    assert "tool_events" not in msg.metadata
    assert "round_texts" not in msg.metadata


def test_agent_loop_sink_captures_tools_on_early_close(monkeypatch):
    """End-to-end: close the generator mid-round-2 exactly like a dropped SSE
    client; the sink must still hold round 1's executed tool call + texts."""
    monkeypatch.setattr(al, "get_setting", lambda key, default=None: default, raising=False)
    monkeypatch.setattr(al, "get_mcp_manager", lambda: None, raising=False)
    monkeypatch.setattr(al, "estimate_tokens", lambda *a, **k: 10, raising=False)

    async def _fast_exec(block, *a, progress_cb=None, **k):
        return ("bash", {"output": "ok", "exit_code": 0})

    monkeypatch.setattr(al, "execute_tool_block", _fast_exec, raising=False)

    calls = {"n": 0}

    def _fake_stream(_candidates, messages, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            async def _g1():
                yield f'data: {json.dumps({"delta": "Running it now."})}\n\n'
                yield f'data: {json.dumps({"type": "tool_calls", "calls": [{"name": "bash", "arguments": json.dumps({"command": "ls"})}]})}\n\n'
                yield "data: [DONE]\n\n"
            return _g1()

        async def _g2():
            yield f'data: {json.dumps({"delta": "partial round two text"})}\n\n'
            yield f'data: {json.dumps({"delta": " more"})}\n\n'
            yield "data: [DONE]\n\n"
        return _g2()

    monkeypatch.setattr(al, "stream_llm_with_fallback", _fake_stream, raising=False)

    async def _run():
        sink = {}
        gen = al.stream_agent_loop(
            "https://api.openai.com/v1", "gpt-4o",
            [{"role": "user", "content": "run ls"}],
            max_rounds=2,
            relevant_tools={"bash"},
            partial_sink=sink,
        )
        saw_tool_output = False
        async for chunk in gen:
            if '"type": "tool_output"' in chunk:
                saw_tool_output = True
                break
        assert saw_tool_output, "never saw the tool execute"
        # Resume into round 2 until a delta streams, then drop the client the
        # same way a stopped SSE consumer would.
        seen_delta = False
        for _ in range(8):
            try:
                chunk = await gen.__anext__()
            except StopAsyncIteration:
                break
            if '"delta"' in chunk:
                seen_delta = True
                break
        await gen.aclose()
        return sink, seen_delta

    sink, seen_delta = asyncio.run(_run())
    assert sink.get("tool_events"), "executed tool call was defenestrated on close"
    assert sink["tool_events"][0]["tool"] == "bash"
    assert sink.get("round_texts") and "Running it now." in sink["round_texts"][0]
    if seen_delta:
        assert "partial round two" in (sink.get("current_round_text") or "")
