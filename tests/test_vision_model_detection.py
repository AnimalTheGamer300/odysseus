"""Tests for is_vision_model (issue #124).

Local vision models served through Ollama/llama.cpp show up under many
names. If one isn't recognized as vision-capable, the image attachment is
stripped from the request before it reaches the model, so it silently never
sees the picture.
"""
from src.chat_helpers import is_vision_model


def test_recognizes_local_and_hosted_vision_models():
    for name in [
        # the ones #124 missed
        "moondream", "moondream:latest",
        "llama3.2-vision:11b", "granite3.2-vision",
        "qwen2.5-vl:7b", "qwen2.5vl", "internvl2.5", "cogvlm",
        # already worked, keep them working
        "llava", "llava:7b", "bakllava", "minicpm-v",
        "gpt-4o", "claude-sonnet-4", "gemini-2.0-flash", "pixtral-12b",
    ]:
        assert is_vision_model(name), f"{name!r} should be detected as vision-capable"


def test_text_only_models_not_flagged():
    for name in ["qwen2.5:3b", "mistral", "llama3.1:8b", "deepseek-r1", "phi3", "vicuna", ""]:
        assert not is_vision_model(name), f"{name!r} should not be flagged as vision"


def test_none_is_safe():
    assert is_vision_model(None) is False


def test_recognizes_multimodal_families_without_vision_in_name():
    # issue #1274: these are vision-capable but their names don't contain
    # "vision"/"vl", so they were dropped and the model never saw the image.
    for name in [
        "gemma3:4b", "gemma3", "gemma-3-27b-it",
        "llama4:scout", "llama4", "llama-4-maverick",
        "mistral-small3.1", "mistral-small-3.2",
        "phi-4-multimodal", "phi4-multimodal",
    ]:
        assert is_vision_model(name), f"{name!r} should be detected as vision-capable"


def test_new_keywords_do_not_overmatch_text_models():
    # The added families must not flag their text-only siblings.
    for name in ["gemma2:9b", "gemma:7b", "llama3.3", "mistral-small", "phi-3-mini"]:
        assert not is_vision_model(name), f"{name!r} should not be flagged as vision"


def test_glm_5_3_flash_is_multimodal():
    # GLM 5.3 dropped the "-v" suffix on its multimodal flash tier
    # (text+image+video -> text). "z-ai/glm-5.3-flash" used to match no
    # keyword, so its images were swapped for a VLM caption.
    for name in ["z-ai/glm-5.3-flash", "glm-5.3-flash", "GLM-5.3-Flash"]:
        assert is_vision_model(name), f"{name!r} should be detected as vision-capable"


def test_glm_5_3_flagship_is_text_only():
    # The non-flash glm-5.3 is text-only (text -> text) — it must stay on
    # the VLM-caption path even though its name resembles the flash tier.
    for name in ["z-ai/glm-5.3", "glm-5.3", "glm-4.6", "glm-4.5-air", "glm-4-32b-0414", "z-ai/glm-5"]:
        assert not is_vision_model(name), f"{name!r} should not be flagged as vision"
