"""Tests for prior-turn tool output replay (src/tool_replay.py)."""

from src.tool_replay import (
    DIGEST_MAX_CHARS,
    OUTPUT_MAX_CHARS,
    _format_output,
    prior_tool_outputs_context_message,
)


def _assistant_with_events(events, content="done"):
    return {"role": "assistant", "content": content, "metadata": {"tool_events": events}}


def test_no_tool_events_returns_none():
    messages = [
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello", "metadata": {}},
        {"role": "assistant", "content": "no metadata"},
    ]
    assert prior_tool_outputs_context_message(messages) is None
    assert prior_tool_outputs_context_message([]) is None
    assert prior_tool_outputs_context_message(None) is None


def test_single_turn_replay_contains_output():
    events = [{
        "round": 1, "tool": "shell", "desc": "boot time",
        "command": "last -2 | head", "output": "reboot   system boot  14:32", "exit_code": 0,
    }]
    messages = [
        {"role": "user", "content": "when did the box boot"},
        _assistant_with_events(events),
        {"role": "user", "content": "you sure?"},
    ]
    msg = prior_tool_outputs_context_message(messages)
    assert msg is not None
    assert msg["role"] == "user"
    assert "last -2 | head" in msg["content"]
    assert "reboot   system boot  14:32" in msg["content"]
    assert "turn -1" in msg["content"]
    # exit_code 0 is not noise-worthy
    assert "exit_code" not in msg["content"]


def test_multiple_turns_ordered_oldest_first():
    old = [{"round": 1, "tool": "shell", "command": "uptime", "output": "up 5 min", "exit_code": 0}]
    new = [{"round": 1, "tool": "shell", "command": "free -h", "output": "total: 32G", "exit_code": 0}]
    messages = [
        {"role": "user", "content": "a"},
        _assistant_with_events(old),
        {"role": "user", "content": "b"},
        _assistant_with_events(new),
        {"role": "user", "content": "c"},
    ]
    msg = prior_tool_outputs_context_message(messages)
    assert "uptime" in msg["content"] and "free -h" in msg["content"]
    assert msg["content"].index("uptime") < msg["content"].index("free -h")
    assert "turn -2" in msg["content"] and "turn -1" in msg["content"]


def test_nonzero_exit_code_surfaced():
    events = [{"round": 1, "tool": "shell", "command": "systemctl status foo", "output": "not found", "exit_code": 4}]
    msg = prior_tool_outputs_context_message([_assistant_with_events(events)])
    assert "exit_code: 4" in msg["content"]


def test_oversized_output_head_tail_truncated():
    body = "A" * (OUTPUT_MAX_CHARS + 2000) + "TAIL" + "B" * 500
    out = _format_output(body)
    assert len(out) < len(body)
    assert "chars trimmed" in out
    assert out.endswith("B" * 500)
    assert out.startswith("A" * 100)


def test_digest_budget_drops_oldest_and_notes_it():
    big = "x" * 9000
    groups = [
        {"round": 1, "tool": "shell", "command": f"cmd-old-{i}", "output": big, "exit_code": 0}
        for i in range(8)  # per-output cap keeps each ~3.7k; 8 of them bust the 24k digest
    ]
    messages = []
    for g in groups:
        messages.append({"role": "user", "content": "q"})
        messages.append(_assistant_with_events([g]))
    msg = prior_tool_outputs_context_message(messages)
    assert msg is not None
    assert len(msg["content"]) <= DIGEST_MAX_CHARS + 200
    assert "omitted for space" in msg["content"]
    # newest turn survives, oldest dropped
    assert "cmd-old-3" in msg["content"]
    assert "cmd-old-0" not in msg["content"]


def test_empty_outputs_only_returns_none():
    events = [{"round": 1, "tool": "shell", "command": "thing", "output": "", "exit_code": 0}]
    msg = prior_tool_outputs_context_message([_assistant_with_events(events)])
    assert msg is None


def test_input_messages_not_mutated():
    events = [{"round": 1, "tool": "shell", "command": "ls", "output": "file.txt", "exit_code": 0}]
    assistant = _assistant_with_events(events)
    messages = [{"role": "user", "content": "q"}, assistant]
    prior_tool_outputs_context_message(messages)
    assert len(messages) == 2
    assert messages[1] is assistant
