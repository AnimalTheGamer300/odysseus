"""Temporal grounding stamps (2026-11-01).

LLM-bound history gets a [HH:MM:SS] prefix per user/assistant message (from
persisted metadata.timestamp, user-local clock) and tool results carry
[HH:MM:SS | elapsed]. System messages, untrusted-guarded context blocks, and
non-string content are never stamped; stamping is idempotent and never mutates
the input list or the session history objects behind it.
"""
import re

from src.user_time import (
    _STAMP_RE,
    clock_stamp,
    format_duration_ms,
    message_stamp,
    parse_message_timestamp,
    stamp_context_messages,
    tool_event_stamp,
)


def test_parse_message_timestamp_formats():
    assert parse_message_timestamp(None) is None
    assert parse_message_timestamp("") is None
    dt = parse_message_timestamp("2026-11-01T04:01:51+00:00")
    assert dt is not None and dt.year == 2026 and dt.hour == 4
    dt_z = parse_message_timestamp("2026-11-01T04:01:51Z")
    assert dt_z == dt
    naive = parse_message_timestamp("2026-11-01 04:01:51")
    assert naive is not None and naive.tzinfo is not None
    epoch = parse_message_timestamp(1772500000)
    assert epoch is not None
    assert parse_message_timestamp("not a date") is None


def test_format_duration_ms():
    assert format_duration_ms(621) == "621ms"
    assert format_duration_ms(999) == "999ms"
    assert format_duration_ms(4200) == "4.2s"
    assert format_duration_ms(65000) == "1m 05s"
    assert format_duration_ms(None) == ""
    assert format_duration_ms("junk") == ""


def test_tool_event_stamp_with_duration():
    stamp = tool_event_stamp({"ts": "2026-11-01T04:02:33+00:00", "duration_ms": 621})
    assert re.fullmatch(r"\[\d{2}:\d{2}:\d{2} \| 621ms\]", stamp), stamp


def test_tool_event_stamp_bare_clock_fallback():
    stamp = tool_event_stamp({})
    assert re.fullmatch(r"\[\d{2}:\d{2}:\d{2}\]", stamp), stamp


def test_message_stamp_uses_metadata_timestamp():
    stamp = message_stamp({"timestamp": "2026-11-01T04:01:51+00:00"})
    assert re.fullmatch(r"\[\d{2}:\d{2}:\d{2}\]", stamp), stamp


def test_stamp_context_messages_basic():
    msgs = [
        {"role": "system", "content": "sys prompt"},
        {"role": "user", "content": "hello", "metadata": {"timestamp": "2026-11-01T04:01:51+00:00"}},
        {"role": "assistant", "content": "hi", "metadata": {"timestamp": "2026-11-01T04:02:03+00:00"}},
        {"role": "tool", "tool_call_id": "c1", "content": "out"},
    ]
    out = stamp_context_messages(msgs)
    assert out[0]["content"] == "sys prompt"  # system untouched
    assert _STAMP_RE.match(out[1]["content"]) and out[1]["content"].endswith("hello")
    assert _STAMP_RE.match(out[2]["content"]) and out[2]["content"].endswith("hi")
    assert _STAMP_RE.match(out[3]["content"]) and out[3]["content"].endswith("out")
    # input not mutated
    assert msgs[1]["content"] == "hello"
    assert msgs[3]["content"] == "out"


def test_stamp_context_messages_skips_untrusted_and_non_string():
    guarded = "UNTRUSTED SOURCE DATA\n<<<UNTRUSTED_SOURCE_DATA>>>\nbody\n<<<END_UNTRUSTED_SOURCE_DATA>>>"
    msgs = [
        {"role": "user", "content": guarded, "metadata": {"trusted": False, "source": "web"}},
        {"role": "user", "content": [{"type": "text", "text": "vision"}]},
        {"role": "assistant", "content": ""},
    ]
    out = stamp_context_messages(msgs)
    assert out[0]["content"] == guarded  # guard header must stay first
    assert out[1]["content"] == [{"type": "text", "text": "vision"}]
    assert out[2]["content"] == ""


def test_stamp_context_messages_idempotent():
    msgs = [{"role": "user", "content": "hello", "metadata": {"timestamp": "2026-11-01T04:01:51Z"}}]
    once = stamp_context_messages(msgs)
    twice = stamp_context_messages(once)
    assert once == twice
    assert once[0]["content"].count("[") == 1  # no double stamp


def test_stamp_context_messages_missing_timestamp_uses_now():
    out = stamp_context_messages([{"role": "user", "content": "live message"}])
    assert _STAMP_RE.match(out[0]["content"])
    assert out[0]["content"].endswith("live message")


def test_clock_stamp_format():
    assert re.fullmatch(r"\[\d{2}:\d{2}:\d{2}\]", clock_stamp())
