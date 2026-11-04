"""
This module intentionally imports NOTHING from the project (except
src.constants which imports nothing from src). Adding a project import here
will reintroduce the circular dependency that this module exists to break.
"""

import hashlib
import json
import os

from src.constants import DATA_DIR, MAX_OUTPUT_CHARS

_mcp_manager = None
_upload_handler = None

# ---------------------------------------------------------------------------
# MCP Manager singleton
# ---------------------------------------------------------------------------

def set_mcp_manager(manager):
    """Set the global MCP manager instance."""
    global _mcp_manager
    _mcp_manager = manager

def get_mcp_manager():
    """Get the global MCP manager instance."""
    return _mcp_manager


# ---------------------------------------------------------------------------
# Shared upload lifecycle handler
# ---------------------------------------------------------------------------

def set_upload_handler(handler):
    """Register the process's UploadHandler without importing app modules."""
    global _upload_handler
    _upload_handler = handler


def get_upload_handler():
    """Return the shared UploadHandler used by route and agent writers."""
    return _upload_handler

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _truncate(text: str, limit: int = MAX_OUTPUT_CHARS) -> str:
    """
    Truncate text to *limit* characters, keeping BOTH ends (head + tail)
    with an explicit elision marker in the middle. Head-only truncation
    drops the tail of a log, which is usually where the error lives.

    Callers treat the result as text, so always return a string: coerce a
    non-string (None -> "", otherwise str(...)) instead of returning it raw,
    which would just move the crash downstream.
    """
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    if len(text) <= limit:
        return text
    head = limit // 2
    tail = limit - head
    elided = len(text) - limit
    return (
        text[:head]
        + f"\n... [{elided} chars elided from the middle] ...\n"
        + text[-tail:]
        + f"\n... (truncated, {len(text)} chars total)"
    )


_TOOL_OUTPUT_CACHE_DIR = os.path.join(DATA_DIR, "tool_output_cache")


def truncate_tool_output(text: str, limit: int = MAX_OUTPUT_CHARS, tool_name: str = "tool") -> str:
    """_truncate plus persistence of the full output for paged re-reads.

    Over-limit output is elided head+tail in the message, and the complete
    text is written once to DATA_DIR/tool_output_cache/<sha1>.txt (DATA_DIR
    is a default tool-path root, so read_file can page through it) instead
    of forcing the model to re-run the command.
    """
    if not isinstance(text, str):
        text = "" if text is None else str(text)
    if len(text) <= limit:
        return text
    path = None
    try:
        os.makedirs(_TOOL_OUTPUT_CACHE_DIR, exist_ok=True)
        digest = hashlib.sha1(text.encode("utf-8", "replace")).hexdigest()[:16]
        path = os.path.join(_TOOL_OUTPUT_CACHE_DIR, f"{digest}.txt")
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
    except Exception:
        path = None
    body = _truncate(text, limit)
    if path:
        body += (
            f"\n[Full {tool_name} output ({len(text)} chars) saved to {path} — "
            "page through it with read_file offset/limit instead of re-running]"
        )
    return body


def _parse_tool_args(content):
    """Parse a tool-call argument blob.

    Accepts either a JSON string or an already-decoded dict. Unwraps the
    common `{"body": {...}}` envelope that smaller models emit when they
    read tool descriptions like "Body is JSON: {...}" literally and
    pass `body` as a field name rather than treating it as a noun.

    Returns a dict on success, raises ValueError on bad JSON.
    """
    if isinstance(content, str):
        try:
            args = json.loads(content) if content.strip() else {}
            if not isinstance(args, dict):
                args = {}
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(str(e))
    elif isinstance(content, dict):
        args = content
    else:
        args = {}
    # Unwrap {"body": {...}} envelope, but only if `body` is the sole key
    # and points at a dict. We don't want to clobber a legitimate `body`
    # field on tools where it's a real arg (e.g. send_email body text).
    if (
        isinstance(args, dict)
        and len(args) == 1
        and "body" in args
        and isinstance(args["body"], dict)
        and "action" in args["body"]  # extra safety: only unwrap if the inner dict looks like a tool call
    ):
        args = args["body"]
    return args
