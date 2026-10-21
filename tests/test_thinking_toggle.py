"""Regression: the `thinking_enabled` master toggle must reach every backend.

`thinking_enabled` (data/settings.json, Settings panel, in-bot settings tool)
is folded into llm_core's existing disable_thinking machinery:

- Ollama native /api/chat       -> "think": False (via _build_ollama_payload)
- Ollama OpenAI-compat /v1      -> "think": False for thinking models (pre-existing)
- DeepSeek V4                   -> thinking {"type": "disabled"} (force=True)
- Mistral reasoning models      -> reasoning_effort "minimal"
- NVIDIA NIM / self-hosted vLLM -> chat_template_kwargs {"enable_thinking": false}
- OpenRouter                    -> reasoning {"enabled": false}
- Groq                          -> reasoning_effort "none"
- api.openai.com                -> reasoning_effort "minimal" (reasoning families only)

Internal utility calls (compaction, summaries, titles) pass
disable_thinking=True explicitly and are unaffected by the toggle: they
stay thinking-off whether the toggle is on or off.
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

import src.llm_core as lc  # noqa: E402
from src.llm_core import (  # noqa: E402
    _apply_thinking_off_openai_compat,
    _disable_deepseek_v4_thinking,
    _thinking_setting_off,
)


# ── _thinking_setting_off ────────────────────────────────────────────

def test_thinking_setting_off_default_is_on(monkeypatch):
    import src.settings as settings_mod
    monkeypatch.setattr(
        settings_mod, "get_setting",
        lambda key, default=None: True if key == "thinking_enabled" else default)
    assert _thinking_setting_off() is False


def test_thinking_setting_off_when_disabled(monkeypatch):
    import src.settings as settings_mod
    monkeypatch.setattr(
        settings_mod, "get_setting",
        lambda key, default=None: False if key == "thinking_enabled" else default)
    assert _thinking_setting_off() is True


def test_thinking_setting_off_survives_broken_settings(monkeypatch):
    import src.settings as settings_mod

    def boom(key, default=None):
        raise RuntimeError("settings file unreadable")

    monkeypatch.setattr(settings_mod, "get_setting", boom)
    # A broken settings file must not silently flip model behavior.
    assert _thinking_setting_off() is False


def test_thinking_enabled_key_exists_with_on_default():
    import src.settings as settings_mod
    assert settings_mod.DEFAULT_SETTINGS.get("thinking_enabled") is True


# ── _apply_thinking_off_openai_compat ────────────────────────────────

def _provider_payload(url, model):
    payload = {"messages": [{"role": "user", "content": "hi"}]}
    _apply_thinking_off_openai_compat(payload, url, model)
    return payload


def test_nvidia_nim_gets_chat_template_kwargs():
    payload = _provider_payload("https://integrate.api.nvidia.com/v1",
                                "z-ai/glm-5.3-flash")
    assert payload.get("chat_template_kwargs") == {"enable_thinking": False}


def test_self_hosted_vllm_gets_chat_template_kwargs():
    payload = _provider_payload("http://127.0.0.1:8000/v1", "Qwen/Qwen3-32B")
    assert payload.get("chat_template_kwargs") == {"enable_thinking": False}


def test_openrouter_gets_reasoning_disabled():
    payload = _provider_payload("https://openrouter.ai/api/v1", "z-ai/glm-5.3-flash")
    assert payload.get("reasoning") == {"enabled": False}
    assert "chat_template_kwargs" not in payload


def test_groq_gets_reasoning_effort_none():
    payload = _provider_payload("https://api.groq.com/openai/v1", "qwen/qwen3-32b")
    assert payload.get("reasoning_effort") == "none"


def test_openai_reasoning_models_floor_at_minimal():
    payload = _provider_payload("https://api.openai.com/v1", "o3-mini")
    assert payload.get("reasoning_effort") == "minimal"


def test_openai_non_reasoning_models_untouched():
    payload = _provider_payload("https://api.openai.com/v1", "gpt-4o")
    assert "reasoning_effort" not in payload
    assert "chat_template_kwargs" not in payload


def test_unknown_cloud_gets_no_experimental_fields():
    # Strict unknown hosts: an unrecognized field risks a hard 400 on
    # every request — worse than a model that keeps thinking.
    payload = _provider_payload("https://llm.example.net/v1", "some/model")
    assert "chat_template_kwargs" not in payload
    assert "reasoning" not in payload
    assert "reasoning_effort" not in payload


# ── DeepSeek force semantics (the fold target) ───────────────────────

def test_deepseek_force_disable_overrides_env_optin(monkeypatch):
    # The toggle folds into disable_thinking=True; force must win over the
    # user's shell exporting ODYSSEUS_DEEPSEEK_V4_THINKING=1.
    monkeypatch.setattr(lc, "_DEEPSEEK_V4_THINKING", "1")
    payload = {"messages": [
        {"role": "assistant", "content": "a", "reasoning_content": "x"},
        {"role": "user", "content": "b"},
    ]}
    _disable_deepseek_v4_thinking(payload, "deepseek-v4-flash@opencode.ai", force=True)
    assert payload.get("thinking") == {"type": "disabled"}
    for m in payload["messages"]:
        assert "reasoning_content" not in m


def test_deepseek_env_optin_still_wins_without_force(monkeypatch):
    # Toggle ON (no force): the env opt-in must keep working.
    monkeypatch.setattr(lc, "_DEEPSEEK_V4_THINKING", "1")
    payload = {"messages": [{"role": "user", "content": "b"}]}
    _disable_deepseek_v4_thinking(payload, "deepseek-v4-flash@opencode.ai", force=False)
    assert "thinking" not in payload
