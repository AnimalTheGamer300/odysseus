# src/chat_helpers.py
"""URL extraction, message/upload validation, request parsing."""

import re
import os
import json
import time
import ipaddress
import logging
import httpx
from urllib.parse import urlparse
from fastapi import HTTPException
from fastapi import UploadFile
from typing import List, Optional

from src.upload_limits import format_byte_limit, get_chat_upload_max_bytes

logger = logging.getLogger(__name__)


def extract_urls(text: str) -> List[str]:
    """Extract URLs from text using regex pattern."""
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(url_pattern, text)
    cleaned_urls = []
    for url in urls:
        # Strip trailing sentence punctuation, but keep a balanced ')' so URLs
        # that legitimately end in one are preserved, e.g. the Wikipedia link
        # ".../Python_(programming_language)". A ')' is only dropped when it is
        # unbalanced (more ')' than '('), which is the prose-glued case such as
        # "(see https://example.com)".
        url = re.sub(r'[.,;:!?]+$', '', url)
        while url.endswith(')') and url.count(')') > url.count('('):
            url = re.sub(r'[.,;:!?]+$', '', url[:-1])
        cleaned_urls.append(url)
    return cleaned_urls


# Model-name substrings that signal native image input. A missed match here
# silently drops the image from the chat request (it gets swapped for a text
# caption), so the model never sees it. Keep this broad, especially for local
# models (Ollama/llama.cpp) that ship under many names. See issue #124.
_VISION_MODEL_KEYWORDS = (
    # hosted
    "gpt-4o", "gpt-4.1", "gpt-4.5", "gpt-4-turbo", "gpt-4-vision",
    "claude-sonnet", "claude-opus", "claude-haiku", "gemini",
    # open / local
    "vision", "multimodal", "llava", "bakllava", "moondream", "pixtral", "minicpm",
    "internvl", "cogvlm", "qwen-vl", "qwen2-vl", "qwen3-vl", "qwen3vl",
    # multimodal families whose names don't contain "vision"/"vl" but DO accept
    # images — without these the image is silently dropped for common Ollama tags
    # like gemma3:4b or gemma4:12b (issue #1274). Gemma 3/4 (4b+), Llama 4 (all),
    # Mistral Small 3.1/3.2, and Phi-4 multimodal are vision-capable; per the
    # err-toward-True policy (#124) a rare text-only tag being treated as vision is
    # the safer failure than silently dropping a real image.
    "gemma-3", "gemma3", "gemma-4", "gemma4",
    "llama-4", "llama4",
    "mistral-small-3.1", "mistral-small3.1", "mistral-small-3.2", "mistral-small3.2",
    # Microsoft Phi-4 ships a dedicated multimodal variant ("phi-4-multimodal-instruct")
    # but users often load it under the bare "phi-4" or "phi4" Ollama tag.
    "phi-4", "phi4",
    # zhipu / glm (glm-4.5v, glm-4.6v, glm-5v-turbo, etc.)
    "glm-4.5v", "glm-4.6v", "glm-5v",
    # GLM 5.3 dropped the "-v" suffix for its multimodal flash tier:
    # glm-5.3-flash is native multimodal (text+image+video -> text) while the
    # flagship glm-5.3 is text-only (text -> text), per Z.ai's published model
    # metadata. Without this, "z-ai/glm-5.3-flash" matched no keyword and its
    # images were silently swapped for a VLM caption.
    "glm-5.3-flash",
)
# Catches the "*-VL-*" / "*VL*" family not covered by a literal keyword above
# (e.g. Qwen2.5-VL and various tags): a standalone "vl" token, plus "vlm".
_VISION_VL_RE = re.compile(r'(?<![a-z])vl(?![a-z])|vlm')


def is_vision_model(model_name: str) -> bool:
    """Best-effort check of whether a model can natively accept images.

    Decides whether image attachments get passed through to the model or
    swapped for a separate caption. Err toward True, since a false negative
    drops the image entirely. See issue #124.
    """
    m = (model_name or "").lower()
    if any(kw in m for kw in _VISION_MODEL_KEYWORDS):
        return True
    return bool(_VISION_VL_RE.search(m))


_PROVIDER_FINGERPRINT_TTL = 60.0
# (host, port) -> (models_list | None, expiry); list = LM Studio, None = not LM Studio.
_lmstudio_models_cache: dict = {}


def _is_local_host(host: Optional[str]) -> bool:
    """True for loopback/LAN/Tailscale hosts (never public domains)."""
    host = (host or "").lower()
    if not host:
        return False
    if host in {"localhost", "host.docker.internal"} or host.endswith(".local"):
        return True
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return "." not in host
    if ip.is_loopback or ip.is_private or ip.is_link_local:
        return True
    return ip in ipaddress.ip_network("100.64.0.0/10")


def _probe_lmstudio_models(url: str) -> Optional[list]:
    """Return LM Studio's native /api/v1/models list, or None when the endpoint
    isn't LM Studio or is unreachable (short-TTL cached; transient errors uncached)."""
    parsed = urlparse(url)
    host = parsed.hostname or ""
    key = (host, parsed.port)
    now = time.time()
    cached = _lmstudio_models_cache.get(key)
    if cached is not None and cached[1] > now:
        return cached[0]
    authority = host if parsed.port is None else f"{host}:{parsed.port}"
    probe_url = f"{parsed.scheme or 'http'}://{authority}/api/v1/models"
    try:
        r = httpx.get(probe_url, timeout=1.0)
    except Exception:
        return None
    try:
        data = r.json() if r.is_success else {}
    except Exception:
        data = {}
    models = data.get("models")
    valid = (
        isinstance(models, list) and bool(models)
        and isinstance(models[0], dict)
        and "key" in models[0] and "architecture" in models[0]
    )
    models = models if valid else None
    _lmstudio_models_cache[key] = (models, now + _PROVIDER_FINGERPRINT_TTL)
    return models


def lmstudio_supports_vision(url: str, model: str) -> Optional[bool]:
    """Read `model`'s capabilities.vision flag from LM Studio, or None when the
    endpoint isn't LM Studio or doesn't report it (so callers fall back)."""
    if not model:
        return None
    # Never probe a remote provider; LM Studio is always a local/LAN host.
    if not _is_local_host(urlparse(url).hostname):
        return None
    models = _probe_lmstudio_models(url)
    if not models:
        return None
    want = model.strip().lower()
    for m in models:
        if not isinstance(m, dict):
            continue
        names = {str(m.get("key", "")).lower(), str(m.get("display_name", "")).lower()}
        if want in names:
            caps = m.get("capabilities")
            if isinstance(caps, dict) and "vision" in caps:
                return bool(caps.get("vision"))
            return None
    return None


# ── Generic /models modality probe ─────────────────────────────────────
# Many OpenAI-compatible providers advertise per-model input modalities on
# their standard GET /models list (OpenRouter: architecture.input_modalities;
# Ollama-compatible servers: capabilities[]; vLLM-ish servers: various).
# Reading that beats name-guessing for models whose names carry no vision
# hint. TTL-cached per endpoint; failures cached briefly so a dead endpoint
# doesn't add a multi-second stall to every message.
_MODALITY_MODELS_TTL = 900.0
_MODALITY_FAILURE_TTL = 60.0
_MODELS_MODALITY_CACHE: dict = {}  # (scheme, host, port, path) -> (list | None, expiry)

# Tail segments of a chat-completions URL — stripped before appending /models.
_COMPLETIONS_SUFFIXES = (
    "/chat/completions", "/completions", "/messages", "/responses", "/embeddings",
)


def _models_list_url(endpoint_url: str) -> str:
    """Derive the models-list URL from a chat-completions (or base) URL."""
    u = (endpoint_url or "").strip().rstrip("/")
    for suf in _COMPLETIONS_SUFFIXES:
        if u.endswith(suf):
            u = u[: -len(suf)]
            break
    return u + "/models"


def _fetch_models_with_modality(endpoint_url: str) -> Optional[list]:
    """GET the endpoint's OpenAI-style /models list, or None when unreachable.
    Successes cached 15 min, failures 60 s (transient errors shouldn't stick)."""
    parsed = urlparse(endpoint_url)
    key = (parsed.scheme, parsed.hostname, parsed.port, parsed.path)
    now = time.time()
    cached = _MODELS_MODALITY_CACHE.get(key)
    if cached is not None and cached[1] > now:
        return cached[0]
    models = None
    try:
        r = httpx.get(_models_list_url(endpoint_url), timeout=2.0)
        if r.is_success:
            data = r.json()
        else:
            data = {}
        if isinstance(data, dict) and isinstance(data.get("data"), list):
            models = data["data"]
        elif isinstance(data, list):
            models = data
    except Exception:
        models = None
    _MODELS_MODALITY_CACHE[key] = (
        models,
        now + (_MODALITY_MODELS_TTL if models is not None else _MODALITY_FAILURE_TTL),
    )
    return models


def _model_entry_supports_vision(entry: dict) -> Optional[bool]:
    """Extract image-input capability from one /models entry, or None when the
    entry carries no modality metadata we understand."""
    arch = entry.get("architecture") if isinstance(entry.get("architecture"), dict) else {}
    # OpenRouter style: architecture.input_modalities: ["text", "image", ...]
    mods = arch.get("input_modalities") or entry.get("input_modalities")
    if isinstance(mods, list) and mods:
        return "image" in [str(m).lower() for m in mods]
    # architecture.modality: "text+image+video->text"
    modality = arch.get("modality") or entry.get("modality")
    if isinstance(modality, str) and "->" in modality:
        return "image" in modality.split("->", 1)[0].lower()
    # Ollama style: capabilities: ["vision", ...] or {"vision": true}
    caps = entry.get("capabilities")
    if isinstance(caps, dict) and "vision" in caps:
        return bool(caps.get("vision"))
    if isinstance(caps, list) and caps:
        return "vision" in [str(c).lower() for c in caps]
    return None


def _entry_matches_model(entry_id: str, model: str) -> bool:
    """Loose id match: exact, or equal ignoring an Ollama-style :tag
    ("z-ai/glm-5.3-flash:free" matches "z-ai/glm-5.3-flash")."""
    a = (entry_id or "").strip().lower()
    b = (model or "").strip().lower()
    if not a or not b:
        return False
    return a == b or a.split(":", 1)[0] == b.split(":", 1)[0]


def advertised_supports_vision(endpoint_url: str, model: str) -> Optional[bool]:
    """Best-effort read of a model's image-input capability from the endpoint's
    own /models metadata. True/False when the endpoint definitively advertises
    it, None when there's nothing usable (unknown model, no metadata, error)."""
    if not endpoint_url or not model:
        return None
    models = _fetch_models_with_modality(endpoint_url)
    if not models:
        return None
    want = model.strip().lower()
    for entry in models:
        if not isinstance(entry, dict):
            continue
        ids = {
            str(entry[k]).lower()
            for k in ("id", "model", "key")
            if entry.get(k)
        }
        if not any(_entry_matches_model(i, want) for i in ids):
            continue
        cap = _model_entry_supports_vision(entry)
        if cap is not None:
            return cap
    return None


def model_supports_vision(model_name: str, endpoint_url: str = "") -> bool:
    """Whether a model accepts images, using the endpoint's reported
    capability when available (LM Studio) and falling back to name-based
    detection otherwise."""
    # Operator overrides win over every heuristic. `text_only_models` forces
    # the caption path even for a vision-named model; `vision_capable_models`
    # rescues multimodal models whose names carry no vision/vl hint (the
    # keyword list can't cover every family). Both accept a list or a
    # comma-separated string of case-insensitive substrings.
    try:
        from src.settings import get_setting
        if _matches_override_pattern(get_setting("text_only_models", []), model_name):
            return False
        if _matches_override_pattern(get_setting("vision_capable_models", []), model_name):
            return True
    except Exception:
        pass
    if endpoint_url:
        try:
            advertised = lmstudio_supports_vision(endpoint_url, model_name or "")
        except Exception:
            advertised = None
        if advertised is not None:
            return advertised
        try:
            advertised = advertised_supports_vision(endpoint_url, model_name or "")
        except Exception:
            advertised = None
        if advertised is not None:
            return advertised
    return is_vision_model(model_name)


def _matches_override_pattern(patterns, model_name: str) -> bool:
    """True when `model_name` contains any of the configured substrings.
    Accepts a list or a comma-separated string; blank entries ignored."""
    if not patterns or not model_name:
        return False
    if isinstance(patterns, str):
        patterns = patterns.split(",")
    m = model_name.strip().lower()
    if not m:
        return False
    for pat in patterns:
        if not isinstance(pat, str):
            continue
        p = pat.strip().lower()
        if p and p in m:
            return True
    return False


def validate_message(message: str) -> str:
    """Validate message input."""
    if not message:
        raise HTTPException(status_code=400, detail="Message is required")

    message = message.strip()
    if len(message) == 0:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    if len(message) > 50000:
        raise HTTPException(status_code=400, detail="Message exceeds maximum length")

    return message


def validate_file_upload(file: UploadFile) -> UploadFile:
    """Validate uploaded file meets requirements."""
    if not file or not file.filename:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "INVALID_FILE",
                "message": "No file uploaded or invalid filename"
            }
        )

    try:
        file.file.seek(0, 2)
        file_size = file.file.tell()
        file.file.seek(0)

        if file_size == 0:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "EMPTY_FILE",
                    "message": "File is empty"
                }
            )

        upload_limit = get_chat_upload_max_bytes()
        if file_size > upload_limit:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "FILE_TOO_LARGE",
                    "message": f"File size exceeds {format_byte_limit(upload_limit)} limit"
                }
            )
    except IOError as e:
        logger.error(f"Error reading file size for {file.filename}: {e}")
        raise HTTPException(
            status_code=500,
            detail={
                "error": "FILE_READ_ERROR",
                "message": "Error reading uploaded file"
            }
        )

    allowed_extensions = {'.txt', '.py', '.html', '.md', '.json', '.csv', '.js',
                         '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.pdf',
                         '.webm', '.wav', '.mp3', '.m4a', '.ogg',
                         '.mp4', '.mov', '.mkv', '.m4v', '.avi'}

    _, ext = os.path.splitext(file.filename.lower())

    if ext not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "UNSUPPORTED_FILE_TYPE",
                "message": f"File type '{ext}' not allowed",
                "allowed_types": sorted(allowed_extensions)
            }
        )

    return file


def coerce_message_and_session(req_json: dict | None, message: str | None,
                               session: str | None, session_manager,
                               allow_empty: bool = False):
    """Extract message and session from request, with validation.

    If allow_empty=True (e.g. attachment-only sends), the message-required
    check is skipped and an empty/whitespace message is normalized to "".
    """
    try:
        if message is None or session is None:
            if req_json is None:
                raise HTTPException(
                    status_code=400,
                    detail={
                        "error": "MISSING_PARAMETERS",
                        "message": "Missing 'message' and/or 'session' in request"
                    }
                )
            message = message or req_json.get("message")
            session = session or req_json.get("session")

        if allow_empty and (message is None or not str(message).strip()):
            message = ""
        else:
            message = validate_message(message)

        if not session:
            raise HTTPException(
                status_code=400,
                detail={
                    "error": "VALIDATION_ERROR",
                    "message": "Session ID is required"
                }
            )
        try:
            session_manager.get_session(session)
        except KeyError:
            raise HTTPException(
                status_code=404,
                detail={
                    "error": "SESSION_NOT_FOUND",
                    "message": f"Session '{session}' not found"
                }
            )

        return message, session
    except HTTPException:
        raise
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        raise HTTPException(
            status_code=400,
            detail={
                "error": "INVALID_JSON",
                "message": "Invalid JSON in request body"
            }
        )
    except Exception as e:
        logger.error(f"Unexpected error in coerce_message_and_session: {e}")
        raise HTTPException(
            status_code=400,
            detail={
                "error": "REQUEST_PROCESSING_ERROR",
                "message": "Error processing request"
            }
        )
