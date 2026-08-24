"""Always-on tool documentation (RAG tool selection is permanently disabled).

Generates ``data/TOOLS.md`` — the agent-readable full reference for every
enabled tool — plus a ``docs/TOOLS.md`` mirror in the repo for humans/git.
The agent system prompt carries a one-line "what it does + how to use" summary
per tool and a pointer to this file, so the model reads the full description
only when it needs it. Every enabled tool is ALWAYS known to the model; no
retrieval/keyword/domain filtering based on the user's message (user
directive 2026-08-07).

This module is intentionally dependency-free of ``agent_loop``: callers pass
the tool sections / schemas in, avoiding an import cycle.
"""

import json
import logging
import os

from src.constants import DATA_DIR

logger = logging.getLogger(__name__)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_TOOLS_PATH = os.path.join(DATA_DIR, "TOOLS.md")
DOCS_TOOLS_PATH = os.path.join(REPO_ROOT, "docs", "TOOLS.md")


def _schema_sketch(schema: dict) -> str:
    """Human-readable parameter list for an OpenAI-style function schema."""
    fn = schema.get("function") or {}
    params = fn.get("parameters") or {}
    props = params.get("properties") or {}
    if not props:
        return ""
    lines = []
    for pname, pmeta in props.items():
        ptype = pmeta.get("type", "any")
        enum = pmeta.get("enum")
        desc = (pmeta.get("description") or "").strip()
        bits = f"- `{pname}` ({ptype}"
        if enum:
            bits += ": " + ", ".join(repr(e) for e in enum)
        bits += ")"
        if desc:
            bits += f" — {desc}"
        lines.append(bits)
    out = "\n".join(lines)
    req = params.get("required") or []
    if req:
        out += f"\n\nRequired: {', '.join(f'`{r}`' for r in req)}"
    return out


def _build_tools_doc(sections, schemas, overrides=None, mcp_mgr=None, disabled_map=None) -> str:
    overrides = overrides or {}
    parts = [
        "# Odysseus tool reference",
        "",
        "Full descriptions for every tool the assistant can call. The system "
        "prompt carries a one-line summary of each tool; read this file for "
        "the complete usage details (examples, parameters, caveats).",
        "",
    ]

    schema_by_name = {}
    for s in schemas:
        fn = s.get("function") or {}
        if fn.get("name"):
            schema_by_name[fn["name"]] = s

    parts.append("## Builtin tools")
    parts.append("")
    ordered = list(sections.keys()) + sorted(set(schema_by_name) - set(sections))
    for name in ordered:
        parts.append(f"### {name}")
        parts.append("")
        text = ""
        if name in sections:
            ov = overrides.get(name)
            text = ov if isinstance(ov, str) and ov.strip() else sections[name]
        if text and text.strip():
            parts.append(text.strip())
        else:
            parts.append("(No prose section; see schema below.)")
        if name in schema_by_name:
            sketch = _schema_sketch(schema_by_name[name])
            if sketch:
                parts.append("")
                parts.append("**Parameters:**")
                parts.append(sketch)
        parts.append("")

    if mcp_mgr is not None:
        try:
            parts.append("## MCP tools")
            parts.append("")
            tools = mcp_mgr.get_all_tools(disabled_map or {})
            by_server = {}
            for t in tools:
                if mcp_mgr.is_builtin(t["server_id"]) and t["server_id"] != "builtin_browser":
                    continue
                if t.get("is_disabled"):
                    continue
                by_server.setdefault(t["server_name"], []).append(t)
            for server_name, server_tools in sorted(by_server.items()):
                parts.append(f"### Server: {server_name}")
                parts.append("")
                for t in server_tools:
                    parts.append(f"#### {t['name']} (`mcp__{t['server_id']}__{t['name']}`)")
                    parts.append("")
                    parts.append(t.get("description") or "(no description)")
                    ischema = t.get("input_schema") or {}
                    if ischema:
                        parts.append("")
                        parts.append("```json")
                        parts.append(json.dumps(ischema, indent=2))
                        parts.append("```")
                    parts.append("")
        except Exception as e:  # pragma: no cover - defensive
            logger.warning("MCP tools doc section skipped: %s", e)

    return "\n".join(parts).strip() + "\n"


def ensure_tools_doc(sections, schemas, overrides=None, mcp_mgr=None, disabled_map=None) -> str:
    """Regenerate the TOOLS.md files when the content changed.

    Returns the absolute path of the data/ copy (the one the agent is always
    allowed to read — DATA_DIR is a default tool-path root).
    """
    content = _build_tools_doc(sections, schemas, overrides, mcp_mgr, disabled_map)
    try:
        existing = ""
        if os.path.exists(DATA_TOOLS_PATH):
            with open(DATA_TOOLS_PATH, "r", encoding="utf-8") as f:
                existing = f.read()
        if existing != content:
            with open(DATA_TOOLS_PATH, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info("[tools-doc] wrote %s (%d chars)", DATA_TOOLS_PATH, len(content))
    except Exception as e:  # pragma: no cover - defensive
        logger.warning("[tools-doc] data/TOOLS.md write failed (non-fatal): %s", e)

    # docs/ mirror — best-effort (docs dir may be read-only in some installs).
    try:
        existing = ""
        if os.path.exists(DOCS_TOOLS_PATH):
            with open(DOCS_TOOLS_PATH, "r", encoding="utf-8") as f:
                existing = f.read()
        if existing != content:
            with open(DOCS_TOOLS_PATH, "w", encoding="utf-8") as f:
                f.write(content)
    except Exception as e:  # pragma: no cover - defensive
        logger.warning("[tools-doc] docs/TOOLS.md mirror skipped: %s", e)

    return DATA_TOOLS_PATH


def tools_doc_pointer() -> str:
    """Prompt line pointing the model at the full tool reference file."""
    return (
        "Full usage documentation for every tool (examples, parameters, caveats) is in "
        f"`TOOLS.md` in the app data folder — absolute path `{DATA_TOOLS_PATH}` "
        "(same content at `docs/TOOLS.md` in the repo). Use read_file to open it "
        "whenever you need details beyond these one-liners."
    )
