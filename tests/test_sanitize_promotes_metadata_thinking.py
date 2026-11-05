"""Regression: _sanitize_llm_messages must promote metadata thinking blobs back.

GARBO stores the thinking blob in message metadata (frontend <think> rebuild).
DeepSeek / Moonshot-Kimi thinking mode requires prior `reasoning_content` to be
passed back on every follow-up request; without promotion the history goes out
naked and the upstream 400s with:

    The `reasoning_content` in the thinking mode must be passed back to the API.

This is the across-turn half of the fix (in-loop half: the tool_calls-aware
strip in agent_loop._append_tool_results).
"""
import sys
from unittest.mock import MagicMock

# Mock heavy dependencies before importing.
for mod in [
    'sqlalchemy', 'sqlalchemy.orm', 'sqlalchemy.ext', 'sqlalchemy.ext.declarative',
    'sqlalchemy.ext.hybrid', 'sqlalchemy.sql', 'sqlalchemy.sql.expression',
    'src.database', 'src.agent_tools', 'core.models', 'core.database',
]:
    if mod not in sys.modules:
        sys.modules[mod] = MagicMock()

from src.llm_core import _sanitize_llm_messages, _disable_deepseek_v4_thinking  # noqa: E402


def test_promotes_metadata_thinking_to_reasoning_content():
    messages = [
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "answer", "metadata": {"thinking": "inner monologue"}},
    ]
    out = _sanitize_llm_messages(messages)
    asst = next(m for m in out if m["role"] == "assistant")
    assert asst.get("reasoning_content") == "inner monologue", (
        "persisted thinking blob was not promoted to reasoning_content; "
        "DeepSeek thinking mode will 400 on the next turn"
    )
    assert "metadata" not in asst, "metadata must stay stripped from the wire"


def test_top_level_reasoning_content_wins_over_metadata():
    messages = [
        {"role": "assistant", "content": "a",
         "reasoning_content": "fresh", "metadata": {"thinking": "stale"}},
    ]
    out = _sanitize_llm_messages(messages)
    assert out[0]["reasoning_content"] == "fresh"


def test_no_promotion_for_user_or_tool_messages():
    messages = [
        {"role": "user", "content": "q", "metadata": {"thinking": "nope"}},
        {"role": "tool", "content": "r", "tool_call_id": "c1", "metadata": {"thinking": "nope"}},
    ]
    out = _sanitize_llm_messages(messages)
    assert out, "expected sanitized output"
    for m in out:
        assert "reasoning_content" not in m


def test_no_promotion_when_metadata_has_no_thinking():
    messages = [{"role": "assistant", "content": "a", "metadata": {"source": "slash"}}]
    out = _sanitize_llm_messages(messages)
    assert "reasoning_content" not in out[0]


def test_disable_thinking_scrubs_reasoning_from_payload():
    # Explicit force (picker Off / utility call) injects the off-switch and
    # scrubs reasoning_content history.
    payload = {"messages": [
        {"role": "assistant", "content": "a", "reasoning_content": "x"},
        {"role": "user", "content": "b"},
    ]}
    _disable_deepseek_v4_thinking(payload, "deepseek-v4-flash@opencode.ai", force=True)
    assert payload.get("thinking") == {"type": "disabled"}
    for m in payload["messages"]:
        assert "reasoning_content" not in m, (
            "reasoning_content must be scrubbed when thinking is disabled"
        )


def test_disable_thinking_leaves_other_models_alone():
    payload = {"messages": [{"role": "assistant", "content": "a", "reasoning_content": "x"}]}
    _disable_deepseek_v4_thinking(payload, "claude-opus-4-7", force=True)
    assert "thinking" not in payload
    assert payload["messages"][0]["reasoning_content"] == "x"


def test_disable_thinking_no_force_is_noop():
    # (2026-11-05) Without force the DS V4 server-side default (thinking on)
    # stands — the env-var forced-off mechanism is gone.
    payload = {"messages": [{"role": "assistant", "content": "a", "reasoning_content": "x"}]}
    _disable_deepseek_v4_thinking(payload, "deepseek-v4-flash@opencode.ai")
    assert "thinking" not in payload
    assert payload["messages"][0]["reasoning_content"] == "x"
