"""Temporal grounding as structured payload fields (2026-11-01 rework).

Design: the timestamp lives in its own DB column (chat_messages.timestamp,
surfaced as metadata.timestamp; tool executions add ts/duration_ms inside the
same row's metadata.tool_events). At the LLM payload boundary,
llm_core._sanitize_llm_messages injects those as structured "timestamp" /
"duration_ms" fields on the outgoing message. Message CONTENT is never
modified — so a stamp can't be mimicked into model replies, persisted into
the DB, or rendered in the UI (the earlier content-prefix version leaked via
model mimicry; see the screenshot regression).
"""

import re

import src.llm_core as llm_core
from src.agent_loop import _append_tool_results
from src.tool_replay import replay_tool_events_as_native
from src.user_time import now_iso, parse_message_timestamp

TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def test_sanitize_injects_timestamp_field_and_leaves_content_clean():
    messages = [
        {"role": "system", "content": "sys"},
        {"role": "user", "content": "hello", "metadata": {"timestamp": "2026-11-01T22:12:14+00:00"}},
        {"role": "assistant", "content": "hi there", "metadata": {"timestamp": "2026-11-01T22:12:40+00:00"}},
    ]
    out = llm_core._sanitize_llm_messages(messages)
    assert out[0].get("timestamp") is None, "system messages must stay KV-stable (no field)"
    assert out[1]["timestamp"] == "2026-11-01T22:12:14+00:00"
    assert out[2]["timestamp"] == "2026-11-01T22:12:40+00:00"
    # content untouched — no [HH:MM:SS] prefix anywhere
    assert out[1]["content"] == "hello"
    assert out[2]["content"] == "hi there"
    assert "metadata" not in out[1]


def test_sanitize_tool_message_gets_timestamp_and_duration_ms():
    # tool message must follow its assistant tool_calls parent (repair loop
    # drops orphans)
    messages = [
        {"role": "assistant", "content": "running", "tool_calls": [
            {"id": "c1", "type": "function", "function": {"name": "bash", "arguments": "{}"}},
        ]},
        {"role": "tool", "tool_call_id": "c1", "content": "ok",
         "metadata": {"ts": "2026-11-01T22:12:33+00:00", "duration_ms": 621, "trusted": False}},
    ]
    out = llm_core._sanitize_llm_messages(messages)
    tool = next(m for m in out if m["role"] == "tool")
    assert tool["timestamp"] == "2026-11-01T22:12:33+00:00"
    assert tool["duration_ms"] == 621
    assert tool["content"] == "ok"
    assert "metadata" not in tool


def test_sanitize_falls_back_to_now_for_live_messages_without_metadata():
    out = llm_core._sanitize_llm_messages([{"role": "user", "content": "live turn"}])
    assert TS_RE.match(out[0]["timestamp"]), out[0].get("timestamp")
    assert out[0]["content"] == "live turn"


def test_sanitize_history_prefix_is_byte_stable_across_calls():
    msg = {"role": "user", "content": "old", "metadata": {"timestamp": "2026-10-30T10:00:00+00:00"}}
    a = llm_core._sanitize_llm_messages([msg])[0]
    b = llm_core._sanitize_llm_messages([dict(msg)])[0]
    assert a == b, "stored timestamps must produce identical payload bytes (KV-cache)"


def test_append_tool_results_attaches_metadata_not_content_stamps():
    messages = [{"role": "user", "content": "run it"}]
    calls = [{"id": "call_0_0", "type": "function", "function": {"name": "bash", "arguments": "{}"}}]
    records = [{"tool_name": "bash", "content": "ls", "result": {"output": "x"},
                "text": "x", "ts": "2026-11-01T22:12:33+00:00", "duration_ms": 42}]
    _append_tool_results(messages, "done", calls, ["x"], ["x"], True, 0,
                         tool_result_records=records)
    assistant = next(m for m in messages if m["role"] == "assistant")
    tool = next(m for m in messages if m["role"] == "tool")
    assert assistant["content"] == "done"  # clean — no [HH:MM:SS] prefix
    assert TS_RE.match(assistant["metadata"]["timestamp"])
    assert tool["content"] == "x"  # clean
    assert tool["metadata"]["ts"] == "2026-11-01T22:12:33+00:00"
    assert tool["metadata"]["duration_ms"] == 42
    # and the boundary turns them into payload fields
    out = llm_core._sanitize_llm_messages(messages)
    tool_out = next(m for m in out if m["role"] == "tool")
    assert tool_out["duration_ms"] == 42
    assert TS_RE.match(tool_out["timestamp"])


def test_native_replay_attaches_metadata_not_content_stamps():
    events = [{"tool": "bash", "command": "ls", "output": "file.txt", "exit_code": 0,
               "ts": "2026-11-01T22:12:33+00:00", "duration_ms": 621}]
    messages = [
        {"role": "user", "content": "list files"},
        {"role": "assistant", "content": "listing", "metadata": {"tool_events": events}},
    ]
    n = replay_tool_events_as_native(messages)
    assert n == 1
    tool = next(m for m in messages if m["role"] == "tool")
    assert "file.txt" in tool["content"]
    assert not re.match(r"^\[\d{2}:\d{2}:\d{2}", tool["content"]), "content must stay clean"
    assert tool["metadata"]["duration_ms"] == 621
    assert tool["metadata"]["ts"] == "2026-11-01T22:12:33+00:00"
    # and the payload boundary turns them into structured fields
    out = llm_core._sanitize_llm_messages(messages)
    tool_out = next(m for m in out if m["role"] == "tool")
    assert tool_out["duration_ms"] == 621
    assert TS_RE.match(tool_out["timestamp"])


def test_parse_message_timestamp_variants():
    assert parse_message_timestamp(None) is None
    assert parse_message_timestamp("") is None
    assert parse_message_timestamp("garbage") is None
    dt = parse_message_timestamp("2026-11-01T22:12:14Z")
    assert dt is not None and dt.utcoffset().total_seconds() == 0
    dt2 = parse_message_timestamp(1798000000)
    assert dt2 is not None
    assert TS_RE.match(now_iso())
