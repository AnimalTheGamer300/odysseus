"""Tests for context_compactor.py — constants and prompt templates.
Uses mock imports to avoid loading the full app stack."""

import asyncio
import sys
from unittest.mock import MagicMock

import pytest

# Mock heavy dependencies before importing
for mod in [
    'sqlalchemy', 'sqlalchemy.orm', 'sqlalchemy.ext', 'sqlalchemy.ext.declarative',
    'sqlalchemy.ext.hybrid', 'sqlalchemy.sql', 'sqlalchemy.sql.expression',
    'src.database',
    'core.models', 'core.database',
]:
    if mod not in sys.modules:
        sys.modules[mod] = MagicMock()

import src.context_compactor as cc
from src.context_compactor import (
    COMPACT_THRESHOLD,
    SELF_SUMMARY_SYSTEM_PROMPT,
    SUMMARY_MAX_TOKENS,
    SUMMARY_MAX_TOKENS_HARD,
    _content_as_text,
    maybe_compact,
    trim_for_context,
)


class TestCompactThreshold:
    def test_value(self):
        assert COMPACT_THRESHOLD == 0.85

    def test_summary_max_tokens(self):
        # 2048 (was 1024): 1024 left no room for a dense multi-turn summary —
        # and with a thinking model, the whole budget burned on chain-of-thought.
        assert SUMMARY_MAX_TOKENS == 2048

    def test_summary_hard_cap(self):
        # The ceiling bounds how much freed context a summary may re-consume.
        # Cranked 4096 -> 16384 on request (2026-08-09): free/self-hosted
        # models make big summaries costless, so let big compactions breathe.
        assert SUMMARY_MAX_TOKENS_HARD == 16384

    def test_budget_placeholder(self):
        # The prompt announces the adaptive token budget to the summarizer.
        assert "{budget}" in SELF_SUMMARY_SYSTEM_PROMPT


class TestSelfSummaryPrompt:
    def test_contains_goal_section(self):
        assert "### User Goal" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_contains_what_was_done_section(self):
        assert "### What Was Done" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_contains_current_state_section(self):
        assert "### Current State" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_contains_pending_section(self):
        assert "### Pending / Next Steps" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_contains_key_context_section(self):
        assert "### Key Context" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_count_placeholder(self):
        assert "{count}" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_n_placeholder(self):
        assert "{n}" in SELF_SUMMARY_SYSTEM_PROMPT

    def test_mentions_compactions(self):
        assert "Compactions so far" in SELF_SUMMARY_SYSTEM_PROMPT


class TestTrimForContext:
    def test_system_truncation_preserves_internal_route_metadata(self):
        messages = [
            {
                "role": "system",
                "content": "persona\n\n" + ("agent prompt " * 2000),
                "_agent_injected": "merged_prompt",
                "_agent_base_message": {"role": "system", "content": "persona"},
            },
            {"role": "user", "content": "latest"},
        ]

        trimmed = trim_for_context(messages, context_length=1024, reserve_tokens=256)

        system = next(message for message in trimmed if message.get("role") == "system")
        assert system["_agent_injected"] == "merged_prompt"
        assert system["_agent_base_message"] == {"role": "system", "content": "persona"}

    def test_keeps_current_large_user_message_by_truncating(self):
        huge = "A" * 20000
        messages = [
            {"role": "system", "content": "You are helpful."},
            {"role": "user", "content": huge},
        ]

        trimmed = trim_for_context(messages, context_length=2048, reserve_tokens=512)

        user_msgs = [m for m in trimmed if m.get("role") == "user"]
        assert len(user_msgs) == 1
        content = user_msgs[0]["content"]
        assert "pasted message was too large" in content
        assert content.startswith("A")
        assert len(content) < len(huge)

    def test_drops_older_messages_before_latest_user_paste(self):
        huge = "B" * 12000
        messages = [{"role": "system", "content": "You are helpful."}]
        messages.extend({"role": "user", "content": f"old-{i} " + ("x" * 1000)} for i in range(8))
        messages.append({"role": "user", "content": huge})

        trimmed = trim_for_context(messages, context_length=2048, reserve_tokens=512)

        assert trimmed[-1]["role"] == "user"
        assert "pasted message was too large" in trimmed[-1]["content"]
        assert "old-0" not in "\n".join(str(m.get("content", "")) for m in trimmed)


class TestContentAsText:
    def test_string_passthrough(self):
        assert _content_as_text("hello") == "hello"

    def test_none_returns_empty(self):
        # Assistant turns that carried only native tool_calls persist
        # content as None — flattening must not raise.
        assert _content_as_text(None) == ""

    def test_list_content_joins_text_blocks(self):
        content = [
            {"type": "text", "text": "describe this"},
            {"type": "image_url", "image_url": {"url": "data:..."}},
        ]
        assert _content_as_text(content) == "describe this"

    def test_unknown_type_returns_empty(self):
        assert _content_as_text(42) == ""


class TestStripThinkBlocks:
    def test_strips_think_tags(self):
        text = "Some real summary.\n<think>I need to produce a summary...</think>\nFinal."
        out = cc._strip_think_blocks(text)
        assert "<think>" not in out
        assert "I need to produce" not in out
        assert "Some real summary." in out and "Final." in out

    def test_strips_mm_think_tags(self):
        text = "<mm:think attr=1>reasoning here</mm:think>Actual content"
        out = cc._strip_think_blocks(text)
        assert "reasoning here" not in out
        assert "Actual content" in out

    def test_no_think_tags_unchanged(self):
        text = "Plain summary text."
        assert cc._strip_think_blocks(text) == "Plain summary text."

    def test_empty_input(self):
        assert cc._strip_think_blocks("") == ""
        assert cc._strip_think_blocks(None) is None


class TestNormalizeCompactionSummary:
    def test_strips_think_blocks_from_summary(self):
        # Regression: a gateway serving CoT as <think> content tags must not
        # leak the reasoning into the persisted summary.
        raw = "<think>We need to produce the conversation summary. We're at turn 52?</think>\n## Conversation Summary\n**Turns summarized:** 52"
        out = cc.normalize_compaction_summary(raw)
        assert "We need to produce" not in out
        assert "Turns summarized:** 52" in out


class TestMessageExcerpt:
    def test_short_message_untouched(self):
        assert cc._message_excerpt("hello") == "hello"

    def test_long_message_keeps_head_and_tail(self):
        long_text = ("A" * 1000) + ("Z" * 1000)
        out = cc._message_excerpt(long_text, max_chars=800)
        assert len(out) < 2000
        assert out.startswith("A")
        # The tail (where decisions usually land) is preserved.
        assert out.rstrip().endswith("Z")

    def test_non_string_returns_empty(self):
        assert cc._message_excerpt(None) == ""
        assert cc._message_excerpt(42) == ""


class TestBuildConvoText:
    def test_global_budget_drops_oldest_with_notice(self):
        older = [
            {"role": "user", "content": f"message-{i} " + ("x" * 200)}
            for i in range(10)
        ]
        out = cc._build_convo_text(older, max_chars=900)
        assert "omitted" in out
        # Oldest dropped, newest present.
        assert "message-0" not in out
        assert "message-9" in out

    def test_no_budget_keeps_all(self):
        older = [{"role": "user", "content": f"m{i}"} for i in range(5)]
        out = cc._build_convo_text(older)
        for i in range(5):
            assert f"m{i}" in out


class TestMaybeCompactReasoningRegression:
    """Compaction summary must never contain chain-of-thought.

    Root cause (2026-08-09): the session model deepseek-v4-flash-free runs
    with thinking ON (ODYSSEUS_DEEPSEEK_V4_THINKING=1). llm_call_async fell
    back to reasoning_content when content was empty, so the compactor
    persisted the model's cut-off internal monologue ("We need to produce the
    conversation summary. We're at turn 52? ...") as the [Conversation
    summary] — and the 1024-token cap sliced it mid-thought before any real
    summary was written.
    """

    def _make_harness(self, fake_summary):
        """Return (run, captured_kwargs) with llm_call_async stubbed."""
        orig_ctx = cc.get_context_length
        orig_call = cc.llm_call_async
        orig_resolve = cc.resolve_endpoint
        orig_update = cc._update_session_history
        captured = {}

        async def _fake(*a, **k):
            captured.update(k)
            return fake_summary

        cc.get_context_length = lambda url, model: 1000  # crosses the 85% threshold with the test convo
        cc.llm_call_async = _fake
        cc.resolve_endpoint = lambda which, owner=None: (None, None, None)
        cc._update_session_history = lambda *a, **k: None

        def run(messages):
            return asyncio.run(
                maybe_compact(
                    session=None,
                    endpoint_url="http://local/v1/chat/completions",
                    model="deepseek-v4-flash-free",
                    messages=list(messages),
                    headers={},
                )
            )

        def restore():
            cc.get_context_length = orig_ctx
            cc.llm_call_async = orig_call
            cc.resolve_endpoint = orig_resolve
            cc._update_session_history = orig_update

        return run, captured, restore

    def _convo(self):
        return [
            {"role": "system", "content": "You are helpful. " * 100},
        ] + [
            {"role": "user" if i % 2 == 0 else "assistant", "content": f"turn {i} " + ("x" * 100)}
            for i in range(10)
        ]

    def test_summary_call_forces_thinking_off(self):
        run, captured, restore = self._make_harness("## Conversation Summary\n**Turns summarized:** 5")
        try:
            result = run(self._convo())
        finally:
            restore()
        assert result[2] is True
        assert captured.get("disable_thinking") is True
        assert captured.get("max_tokens") == SUMMARY_MAX_TOKENS

    def test_empty_summary_skips_compaction_gracefully(self):
        # A thinking model that ignores thinking-off returns content="";
        # compaction must NOT proceed (it would persist an empty/CoT summary
        # and drop the older half).
        messages = self._convo()
        run, _, restore = self._make_harness("")
        try:
            compacted, _, was_compacted = run(messages)
        finally:
            restore()
        assert was_compacted is False
        assert len(compacted) == len(messages)  # history untouched

    def test_chain_of_thought_never_persisted(self):
        # Even if a gateway returns CoT in content (defense-in-depth), the
        # think blocks are stripped and the raw monologue is not the summary.
        cot = (
            "<think>We need to produce the conversation summary. We're at turn 52? "
            "The prompt says Turns summarized: 52.</think>\n"
            "## Conversation Summary\n**Turns summarized:** 5\n### User Goal\nship it"
        )
        run, _, restore = self._make_harness(cot)
        try:
            compacted, _, was_compacted = run(self._convo())
        finally:
            restore()
        assert was_compacted is True
        joined = " ".join(m.get("content", "") for m in compacted)
        assert "We need to produce" not in joined
        assert "### User Goal" in joined


class TestMaybeCompactFourthMessage:
    """Regression: a multi-message conversation must not crash compaction when
    a prior assistant turn used native tool_calls (content == None). This was
    the '4th message stops working' bug — on a small-context model the soft
    85% threshold is crossed after a few turns, and the older half being
    summarized contained a None-content assistant message, which raised
    TypeError: 'NoneType' object is not subscriptable and broke the request."""

    def _run(self, messages, *, context_length=500):
        # Force compaction to trigger and stub the summary LLM call so the test
        # is hermetic (no network, no real endpoint resolution).
        orig_ctx = cc.get_context_length
        orig_call = cc.llm_call_async
        orig_resolve = cc.resolve_endpoint
        orig_update = cc._update_session_history

        async def _fake_summary(*a, **k):
            return "compact summary text"

        cc.get_context_length = lambda url, model: context_length
        cc.llm_call_async = _fake_summary
        cc.resolve_endpoint = lambda which, owner=None: (None, None, None)
        cc._update_session_history = lambda *a, **k: None
        try:
            return asyncio.run(
                maybe_compact(
                    session=None,
                    endpoint_url="http://local/v1/chat/completions",
                    model="local-model",
                    messages=list(messages),
                    headers={},
                )
            )
        finally:
            cc.get_context_length = orig_ctx
            cc.llm_call_async = orig_call
            cc.resolve_endpoint = orig_resolve
            cc._update_session_history = orig_update

    def _four_turn_history_with_tool_call(self):
        # Large system prompt so the conversation crosses the 85% threshold of
        # the tiny (context_length=500) window used in _run, forcing the real
        # compaction branch to execute.
        return [
            {"role": "system", "content": "You are a helpful agent. " * 200},
            {"role": "user", "content": "turn 1: search the web"},
            # Native tool call → content is None (matches agent_loop persistence)
            {"role": "assistant", "content": None,
             "tool_calls": [{"id": "c1", "type": "function",
                             "function": {"name": "web_search", "arguments": "{}"}}]},
            {"role": "tool", "tool_call_id": "c1", "content": "search results"},
            {"role": "assistant", "content": "Here is what I found."},
            {"role": "user", "content": "turn 2"},
            {"role": "assistant", "content": "reply 2"},
            {"role": "user", "content": "turn 3"},
            {"role": "assistant", "content": "reply 3"},
            {"role": "user", "content": "turn 4 — previously broke here"},
        ]

    def test_does_not_crash_on_none_content_turn(self):
        # Must not raise TypeError; returns the 3-tuple contract.
        result = self._run(self._four_turn_history_with_tool_call())
        assert isinstance(result, tuple) and len(result) == 3
        compacted_messages, context_length, was_compacted = result
        assert isinstance(compacted_messages, list)
        assert was_compacted is True
        # The summary the model produced is present and a system message.
        assert any(
            m.get("role") == "system" and "compact summary text" in (m.get("content") or "")
            for m in compacted_messages
        )

    def test_handles_multimodal_list_content(self):
        messages = self._four_turn_history_with_tool_call()
        messages[1] = {"role": "user", "content": [
            {"type": "text", "text": "look at this image"},
            {"type": "image_url", "image_url": {"url": "data:image/png;base64,xxxx"}},
        ]}
        result = self._run(messages)
        assert len(result) == 3 and result[2] is True


class TestMaybeCompactTruncationAndBudget:
    """Adaptive summary budget + finish_reason truncation detection (2026-08-09).

    - max_tokens scales with the size of the summarized half (older//8,
      clamped to [2048, 16384]) so a big coding-session compaction
      legitimately gets more room while a small chat stays cheap.
    - a "length"/"max_tokens" finish_reason (output hit the cap) triggers one
      retry at the 16384 ceiling when the budget was below it; if it still
      truncates, the summary is visibly marked instead of silently amputating
      its tail (usually the "Pending / Next Steps" section).
    """

    def _harness(self, fake_summary, *, est_tokens=10000):
        """Return (run, calls, restore); calls records max_tokens per call."""
        orig_ctx = cc.get_context_length
        orig_est = cc.estimate_tokens
        orig_call = cc.llm_call_async
        orig_resolve = cc.resolve_endpoint
        orig_update = cc._update_session_history
        calls = []

        async def _fake(*a, **k):
            calls.append(k.get("max_tokens"))
            if callable(fake_summary):
                return fake_summary(k.get("max_tokens"))
            return fake_summary

        cc.get_context_length = lambda url, model: 1000
        cc.estimate_tokens = (
            est_tokens if callable(est_tokens) else (lambda msgs: est_tokens)
        )
        cc.llm_call_async = _fake
        cc.resolve_endpoint = lambda which, owner=None: (None, None, None)
        cc._update_session_history = lambda *a, **k: None

        def run(messages):
            return asyncio.run(
                maybe_compact(
                    session=None,
                    endpoint_url="http://local/v1/chat/completions",
                    model="deepseek-v4-flash-free",
                    messages=list(messages),
                    headers={},
                )
            )

        def restore():
            cc.get_context_length = orig_ctx
            cc.estimate_tokens = orig_est
            cc.llm_call_async = orig_call
            cc.resolve_endpoint = orig_resolve
            cc._update_session_history = orig_update

        return run, calls, restore

    def _convo(self):
        return [
            {"role": "system", "content": "You are helpful. " * 100},
        ] + [
            {"role": "user" if i % 2 == 0 else "assistant", "content": f"turn {i} " + ("x" * 100)}
            for i in range(10)
        ]

    def test_budget_scales_with_older_half(self):
        # 20000 freed tokens -> 2500 budget (12.5%), inside [2048, 4096].
        run, calls, restore = self._harness(("summary", "stop"), est_tokens=20000)
        try:
            run(self._convo())
        finally:
            restore()
        assert calls == [2500]

    def test_budget_capped_at_ceiling(self):
        # 200000 freed tokens -> 25000 raw -> capped at 16384, no more.
        run, calls, restore = self._harness(("summary", "stop"), est_tokens=200000)
        try:
            run(self._convo())
        finally:
            restore()
        assert calls == [SUMMARY_MAX_TOKENS_HARD]

    def test_budget_floor_for_small_compaction(self):
        # Tiny older half -> the 2048 floor, not a tiny budget. (used must still
        # exceed the 85% trigger — only the older half being summarized is small.)
        est = lambda msgs: 10000 if len(msgs) >= 10 else 500
        run, calls, restore = self._harness(("summary", "stop"), est_tokens=est)
        try:
            run(self._convo())
        finally:
            restore()
        assert calls == [SUMMARY_MAX_TOKENS]

    def test_truncation_retries_once_at_ceiling_then_marks(self):
        # Truncated at 2048 -> retry at 16384; still truncated -> marked.
        est = lambda msgs: 10000 if len(msgs) >= 10 else 500
        run, calls, restore = self._harness(
            lambda mk: ("summary-b", "length"), est_tokens=est
        )
        try:
            compacted, _, was_compacted = run(self._convo())
        finally:
            restore()
        assert calls == [SUMMARY_MAX_TOKENS, SUMMARY_MAX_TOKENS_HARD]
        assert was_compacted is True
        joined = " ".join(m.get("content", "") for m in compacted)
        assert "summary-b" in joined
        assert "truncated" in joined.lower()

    def test_truncation_at_ceiling_marked_without_retry(self):
        # Already at the ceiling: no second call, still visibly marked.
        run, calls, restore = self._harness(
            lambda mk: ("summary-c", "length"), est_tokens=200000
        )
        try:
            compacted, _, _ = run(self._convo())
        finally:
            restore()
        assert calls == [SUMMARY_MAX_TOKENS_HARD]
        joined = " ".join(m.get("content", "") for m in compacted)
        assert "summary-c" in joined
        assert "truncated" in joined.lower()

    def test_untruncated_summary_single_call_no_marker(self):
        run, calls, restore = self._harness(("summary-ok", "stop"), est_tokens=20000)
        try:
            compacted, _, _ = run(self._convo())
        finally:
            restore()
        assert calls == [2500]
        joined = " ".join(m.get("content", "") for m in compacted)
        assert "summary-ok" in joined
        assert "truncated" not in joined.lower()


@pytest.mark.asyncio
async def test_deferred_compaction_persists_only_after_route_commit(monkeypatch):
    updates = []
    state = {}
    messages = [
        {"role": "system", "content": "system " * 100},
        {"role": "user", "content": "one"},
        {"role": "assistant", "content": "two"},
        {"role": "user", "content": "three"},
        {"role": "assistant", "content": "four"},
        {"role": "user", "content": "five"},
    ]

    monkeypatch.setattr(cc, "get_context_length", lambda *args: 100)
    monkeypatch.setattr(cc, "resolve_endpoint", lambda *args, **kwargs: (None, None, None))

    async def fake_summary(*args, **kwargs):
        return "route-specific summary"

    monkeypatch.setattr(cc, "llm_call_async", fake_summary)
    monkeypatch.setattr(
        cc,
        "_update_session_history",
        lambda *args, **kwargs: updates.append((args, kwargs)),
    )

    _compacted, _context, was_compacted = await cc.maybe_compact(
        object(),
        "https://candidate.example/v1",
        "candidate-model",
        messages,
        persist=False,
        compaction_state=state,
    )

    assert was_compacted is True
    assert updates == []
    assert state["summary"] == "route-specific summary"
    assert cc.apply_compaction_state(object(), state) is True
    assert len(updates) == 1
    assert cc.apply_compaction_state(object(), state) is False
    assert len(updates) == 1


class TestResearchPrimerPreserved:
    """A research-spinoff primer (metadata research_spinoff_from) must never be
    trimmed away — it is the Discuss chat's sole knowledge base (drift fix)."""

    def _messages(self):
        return [
            {"role": "system", "content": "You are Odysseus."},
            {"role": "system", "content": "Prompt-safety policy: data not instructions."},
            {"role": "system", "content": "saved memory: pinned " + "m" * 600},
            {"role": "system", "content": "RETRIEVED-DOCS-MARKER " + "r" * 6000},
            {"role": "system",
             "content": "=== REPORT ===\nPRIMER-MARKER " + "z" * 1500,
             "metadata": {"research_spinoff_from": "rp-abc123"}},
        ] + [
            {"role": "user", "content": f"q{i} " + ("x" * 500)} for i in range(8)
        ] + [
            {"role": "assistant", "content": "a" * 500},
            {"role": "user", "content": "latest question"},
        ]

    def test_primer_kept_when_over_budget(self):
        trimmed = trim_for_context(self._messages(), context_length=1024, reserve_tokens=256)
        joined = "\n".join(str(m.get("content", "")) for m in trimmed)
        assert "PRIMER-MARKER" in joined

    def test_bulky_non_primer_system_dropped_but_primer_kept(self):
        trimmed = trim_for_context(self._messages(), context_length=1024, reserve_tokens=256)
        joined = "\n".join(str(m.get("content", "")) for m in trimmed)
        assert "PRIMER-MARKER" in joined
        assert "RETRIEVED-DOCS-MARKER" not in joined

    def test_leading_preset_kept_when_no_primer_metadata(self):
        msgs = self._messages()
        del msgs[4]["metadata"]
        trimmed = trim_for_context(msgs, context_length=1024, reserve_tokens=256)
        joined = "\n".join(str(m.get("content", "")) for m in trimmed)
        assert "You are Odysseus." in joined
