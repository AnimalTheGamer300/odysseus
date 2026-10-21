"""Tests for LM Studio vision-capability passthrough: reading capabilities.vision
from the native /api/v1/models endpoint, with no probing of cloud providers."""
import pytest

from src import chat_helpers


class _FakeResponse:
    def __init__(self, payload, ok=True):
        self._payload = payload
        self.is_success = ok

    def json(self):
        return self._payload


# ════════════════════════════════════════════════════════════
# lmstudio_supports_vision — reads capabilities.vision
# ════════════════════════════════════════════════════════════

class TestLmStudioSupportsVision:
    # A vision finetune whose NAME has no vision keyword — the case the
    # name-based heuristic gets wrong (the issue this fixes).
    PAYLOAD = {"models": [
        {"key": "qwen3.6-27b-custom-finetune", "architecture": "qwen35",
         "capabilities": {"vision": True, "trained_for_tool_use": True}},
        {"key": "text-only-llm", "architecture": "qwen35",
         "capabilities": {"vision": False}},
        {"key": "no-caps-model", "architecture": "qwen35"},
    ]}
    URL = "http://localhost:1234/v1/chat/completions"

    @pytest.fixture(autouse=True)
    def _clear_cache(self):
        chat_helpers._lmstudio_models_cache.clear()
        yield
        chat_helpers._lmstudio_models_cache.clear()

    def _serve(self, monkeypatch, payload):
        monkeypatch.setattr(chat_helpers.httpx, "get",
                            lambda url, timeout=None: _FakeResponse(payload))

    def test_vision_true_from_capabilities(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.lmstudio_supports_vision(self.URL, "qwen3.6-27b-custom-finetune") is True

    def test_vision_false_from_capabilities(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.lmstudio_supports_vision(self.URL, "text-only-llm") is False

    def test_model_without_capabilities_returns_none(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.lmstudio_supports_vision(self.URL, "no-caps-model") is None

    def test_unknown_model_returns_none(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.lmstudio_supports_vision(self.URL, "not-listed") is None

    def test_non_lmstudio_endpoint_returns_none(self, monkeypatch):
        self._serve(monkeypatch, {"data": [{"id": "gpt-4o"}]})
        assert chat_helpers.lmstudio_supports_vision(self.URL, "gpt-4o") is None

    def test_empty_model_returns_none(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.lmstudio_supports_vision(self.URL, "") is None

    def test_remote_endpoint_never_probed(self, monkeypatch):
        calls = {"n": 0}

        def tracking_get(url, timeout=None):
            calls["n"] += 1
            return _FakeResponse(self.PAYLOAD)

        monkeypatch.setattr(chat_helpers.httpx, "get", tracking_get)
        # A cloud provider host must short-circuit to None with no network probe.
        assert chat_helpers.lmstudio_supports_vision(
            "https://api.openai.com/v1/chat/completions", "gpt-4o") is None
        assert calls["n"] == 0


# ════════════════════════════════════════════════════════════
# model_supports_vision — endpoint capability wins, name is fallback
# ════════════════════════════════════════════════════════════

class TestModelSupportsVision:
    """Endpoint-aware vision check: API capability wins, name heuristic is the fallback."""

    def test_api_capability_overrides_name_heuristic(self, monkeypatch):
        # Name has no vision keyword, but the endpoint advertises vision=True.
        monkeypatch.setattr(chat_helpers, "is_vision_model", lambda n: False)
        monkeypatch.setattr(chat_helpers, "lmstudio_supports_vision", lambda url, m: True)
        assert chat_helpers.model_supports_vision("qwen3.6-27b-finetune",
                                                  "http://localhost:1234/v1/chat/completions") is True

    def test_falls_back_to_name_when_no_endpoint(self):
        # No endpoint URL → pure name heuristic.
        assert chat_helpers.model_supports_vision("llava-1.6", "") is True
        assert chat_helpers.model_supports_vision("mistral-7b", "") is False

    def test_falls_back_to_name_when_endpoint_unknown(self, monkeypatch):
        # Neither probe advertises (None) → name heuristic decides.
        monkeypatch.setattr(chat_helpers, "lmstudio_supports_vision", lambda url, m: None)
        monkeypatch.setattr(chat_helpers, "advertised_supports_vision", lambda url, m: None)
        assert chat_helpers.model_supports_vision("qwen2-vl-7b", "http://host/v1") is True
        assert chat_helpers.model_supports_vision("plain-llm", "http://host/v1") is False


# ══════════════════════════════════════════════════════════
# advertised_supports_vision — generic /models modality probe
# ══════════════════════════════════════════════════════════

class TestAdvertisedSupportsVision:
    """OpenAI-compatible endpoints that advertise input modalities on their
    standard /models list (OpenRouter-style architecture fields, Ollama-style
    capabilities) let multimodal-but-plainly-named models keep their images."""

    PAYLOAD = {"data": [
        {"id": "z-ai/glm-5.3-flash",
         "architecture": {"input_modalities": ["text", "image", "video"]}},
        {"id": "z-ai/glm-5.3",
         "architecture": {"input_modalities": ["text"]}},
        {"id": "modality-string-model",
         "architecture": {"modality": "text+image->text"}},
        {"id": "ollama-vision", "capabilities": ["completion", "vision"]},
        {"id": "no-metadata"},
    ]}
    URL = "https://integrate.api.nvidia.com/v1/chat/completions"

    @pytest.fixture(autouse=True)
    def _clear_cache(self):
        chat_helpers._MODELS_MODALITY_CACHE.clear()
        yield
        chat_helpers._MODELS_MODALITY_CACHE.clear()

    def _serve(self, monkeypatch, payload, ok=True):
        monkeypatch.setattr(chat_helpers.httpx, "get",
                            lambda url, timeout=None: _FakeResponse(payload, ok=ok))

    def test_openrouter_style_input_modalities(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "z-ai/glm-5.3-flash") is True

    def test_text_only_modalities_advertise_false(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "z-ai/glm-5.3") is False

    def test_modality_string_parsed(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "modality-string-model") is True

    def test_ollama_style_capabilities_list(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "ollama-vision") is True

    def test_entry_without_metadata_returns_none(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "no-metadata") is None

    def test_unknown_model_returns_none(self, monkeypatch):
        self._serve(monkeypatch, self.PAYLOAD)
        assert chat_helpers.advertised_supports_vision(self.URL, "not-listed") is None

    def test_http_failure_returns_none(self, monkeypatch):
        self._serve(monkeypatch, {}, ok=False)
        assert chat_helpers.advertised_supports_vision(self.URL, "z-ai/glm-5.3-flash") is None

    def test_models_url_derivation(self):
        assert chat_helpers._models_list_url(
            "https://integrate.api.nvidia.com/v1/chat/completions") == \
            "https://integrate.api.nvidia.com/v1/models"
        assert chat_helpers._models_list_url("http://localhost:1234/v1") == \
            "http://localhost:1234/v1/models"


# ══════════════════════════════════════════════════════════
# model_supports_vision — operator overrides win over everything
# ══════════════════════════════════════════════════════════

class TestVisionOverrides:
    """vision_capable_models / text_only_models settings are the final word."""

    @staticmethod
    def _settings(monkeypatch, capable=None, text_only=None):
        table = {"vision_capable_models": capable or [], "text_only_models": text_only or []}
        monkeypatch.setattr("src.settings.get_setting", lambda k, d=None: table.get(k, d))

    def test_vision_capable_override_rescues_plain_name(self, monkeypatch):
        self._settings(monkeypatch, capable=["my-custom-multimodal"])
        assert chat_helpers.model_supports_vision("my-custom-multimodal", "") is True

    def test_text_only_override_forces_caption_path(self, monkeypatch):
        # Name screams vision; the operator says the deployment is text-only.
        self._settings(monkeypatch, text_only=["llava-broken"])
        assert chat_helpers.model_supports_vision("llava-broken:7b", "") is False

    def test_text_only_wins_over_vision_override(self, monkeypatch):
        self._settings(monkeypatch, capable=["dual"], text_only=["dual"])
        assert chat_helpers.model_supports_vision("dual-model", "") is False

    def test_override_wins_over_endpoint_advertisement(self, monkeypatch):
        self._settings(monkeypatch, text_only=["z-ai/glm-5.3-flash"])
        monkeypatch.setattr(chat_helpers, "lmstudio_supports_vision", lambda url, m: True)
        assert chat_helpers.model_supports_vision(
            "z-ai/glm-5.3-flash", "http://localhost:1234/v1") is False

    def test_comma_separated_string_accepted(self, monkeypatch):
        self._settings(monkeypatch, capable="a-model, b-model")
        assert chat_helpers.model_supports_vision("B-Model-xl", "") is True
