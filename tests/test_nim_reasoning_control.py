"""Per-model NIM reasoning_effort mapping — live-verified 2026-11-01.

Acceptance (HTTP 200) and off-effect (0 reasoning_content chars on trivial AND
hard prompts) were probed per model against integrate.api.nvidia.com:
  nemotron (any): accepts all values; OFF = "none"
  glm-5.x:        accepts none/minimal/low/medium/high/max but none/minimal
                  do NOT suppress; OFF = "low"
  minimax m3.1:   accepts all; none/minimal don't suppress; OFF = "low" (best)
  mistral-large-4: accepts ONLY low/medium/high (400 otherwise); OFF = "low"
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.llm_core import (
    _apply_request_reasoning_effort,
    _apply_thinking_off_openai_compat,
    _nim_clamp_level,
    _request_reasoning,
    nim_reasoning_levels,
    nim_reasoning_off_value,
    normalize_reasoning_override,
    set_request_reasoning,
)

NVIDIA = "https://integrate.api.nvidia.com/v1/chat/completions"


def test_off_value_per_family():
    assert nim_reasoning_off_value("nvidia/nemotron-3.5-super-vl-120b-a12b") == "none"
    assert nim_reasoning_off_value("nvidia/nemotron-3-ultra-550b-a55b") == "none"
    assert nim_reasoning_off_value("nvidia/nemotron-3-nano-omni-30b-a3b-reasoning") == "none"
    assert nim_reasoning_off_value("z-ai/glm-5.3-flash") == "low"
    assert nim_reasoning_off_value("minimaxai/minimax-m3.1-flash") == "low"
    assert nim_reasoning_off_value("mistralai/mistral-large-4-1t-a52b") == "low"
    assert nim_reasoning_off_value("some/unknown-model") == "low"


def test_levels_per_family():
    assert "xhigh" in nim_reasoning_levels("nvidia/nemotron-3-ultra-550b-a55b")
    assert "max" in nim_reasoning_levels("z-ai/glm-5.3-flash")
    assert "xhigh" not in nim_reasoning_levels("z-ai/glm-5.3-flash")
    assert nim_reasoning_levels("mistralai/mistral-large-4-1t-a52b") == ("low", "medium", "high")
    assert "max" not in nim_reasoning_levels("mistralai/mistral-large-4-1t-a52b")
    assert "xhigh" in nim_reasoning_levels("minimaxai/minimax-m3.1-flash")


def test_clamp_avoids_400s():
    assert _nim_clamp_level("mistralai/mistral-large-4-1t-a52b", "max") == "high"
    assert _nim_clamp_level("mistralai/mistral-large-4-1t-a52b", "xhigh") == "high"
    assert _nim_clamp_level("mistralai/mistral-large-4-1t-a52b", "low") == "low"
    assert _nim_clamp_level("z-ai/glm-5.3-flash", "max") == "max"
    assert _nim_clamp_level("nvidia/nemotron-3-ultra-550b-a55b", "xhigh") == "xhigh"
    assert _nim_clamp_level("some/unknown", "max") == "high"


def test_normalize_accepts_xhigh():
    assert normalize_reasoning_override("xhigh") == "xhigh"
    assert normalize_reasoning_override("MAX") == "max"
    assert normalize_reasoning_override("default") is None
    assert normalize_reasoning_override("none") == "off"


def _payload(model, override):
    set_request_reasoning(override)
    p = {"model": model, "messages": [{"role": "user", "content": "hi"}]}
    if _request_reasoning() == "off":
        _apply_thinking_off_openai_compat(p, NVIDIA, model)
    _apply_request_reasoning_effort(p, NVIDIA, model)
    set_request_reasoning(None)
    return p


def test_off_payload_per_model():
    assert _payload("nvidia/nemotron-3.5-super-vl-120b-a12b", "off")["reasoning_effort"] == "none"
    assert _payload("z-ai/glm-5.3-flash", "off")["reasoning_effort"] == "low"
    assert _payload("mistralai/mistral-large-4-1t-a52b", "off")["reasoning_effort"] == "low"
    # template kwarg still sent alongside (harmless on NIM, helps self-hosted)
    assert _payload("z-ai/glm-5.3-flash", "off")["chat_template_kwargs"] == {"enable_thinking": False}


def test_level_payload_per_model():
    assert _payload("nvidia/nemotron-3-ultra-550b-a55b", "max")["reasoning_effort"] == "max"
    assert _payload("nvidia/nemotron-3-ultra-550b-a55b", "xhigh")["reasoning_effort"] == "xhigh"
    assert _payload("z-ai/glm-5.3-flash", "max")["reasoning_effort"] == "max"
    assert _payload("mistralai/mistral-large-4-1t-a52b", "max")["reasoning_effort"] == "high"
    assert _payload("minimaxai/minimax-m3.1-flash", "xhigh")["reasoning_effort"] == "xhigh"
    assert "reasoning_effort" not in _payload("z-ai/glm-5.3-flash", None)
