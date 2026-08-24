#!/usr/bin/env python3
"""
dump_agent_prompt.py — print the VERBATIM request payload Odysseus Agent mode
sends to the LLM (persona/system prompt, messages, tools, every param).

Mirrors the agent-round setup in src/agent_loop.py line-for-line:
  1. endpoint classification   (supports_tools DB lookup -> _is_api_model -> compact)
  2. _build_system_prompt()    (the REAL function, not a reimplementation)
  3. plan-mode / approved-plan / guide-only directive prepends
  4. all_tool_schemas selection (force_answer / api-model / local-model branches)
  5. llm_core._stream_llm_inner() payload construction (the REAL builders:
     _sanitize_llm_messages, system-message consolidation, provider-specific
     payload, cache-affinity / generation-stability / reasoning scrubs)

Output is the actual JSON body that would be POSTed to the endpoint (auth
headers omitted). The [Context — current date/time] message is elided by
default — add --include-datetime to restore it.

Usage:
    python3 scripts/dump_agent_prompt.py
    python3 scripts/dump_agent_prompt.py --endpoint-url http://localhost:1234/v1 \
        --model nvidia-nemotron-3.5-lightning-30b-a3b
    python3 scripts/dump_agent_prompt.py --endpoint-url https://integrate.api.nvidia.com/v1 \
        --model nemotron-3-ultra
    python3 scripts/dump_agent_prompt.py --connect-mcp            # attach real MCP servers, like the app does
    python3 scripts/dump_agent_prompt.py --mcp-schemas mcp.json   # inject a saved MCP schema dump instead
    python3 scripts/dump_agent_prompt.py --history convo.json     # include a conversation (JSON array of {role, content})
    python3 scripts/dump_agent_prompt.py --json > dump.json       # machine-readable, payload included
    python3 scripts/dump_agent_prompt.py --brief                  # condensed view (truncated previews)

Notes:
  * The live MCP schemas (e.g. browser tools) live in the running app's memory.
    In a standalone process the MCP manager starts empty, so pass --connect-mcp
    (spawns the enabled MCP servers) or --mcp-schemas FILE to see them.
  * Memory / conversation history are per-chat; pass --history FILE.json
    (a JSON array of {role, content} messages) to include them.
"""
import argparse
import json
import os
import sys

_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)

# ── real app modules (same code the server runs) ────────────────────────────
import src.agent_loop as al                       # noqa: E402
import src.llm_core as lc                          # noqa: E402
from src.tool_schemas import FUNCTION_TOOL_SCHEMAS  # noqa: E402
from src.tool_utils import get_mcp_manager        # noqa: E402
from src.model_context import estimate_tokens     # noqa: E402
from core.database import SessionLocal as _SL, ModelEndpoint as _ME  # noqa: E402

# Exact content prefix of the datetime context message (src/user_time.py:211).
_DATETIME_MARKER = "[Context — current date/time, refreshed each turn; not part of your instructions]"

# Inline keyword lists — copied verbatim from src/agent_loop.py (~line 3740).
_MODEL_SUPPORTS_TOOLS_KW = (
    "gpt-4", "gpt-5", "gpt-o", "claude", "gemini", "gemma",
    "qwen3", "qwen2.5", "mixtral", "mistral", "llama-3.1", "llama-3.2",
    "llama-3.3", "llama-4", "llama3.1", "llama3.2", "llama3.3", "llama4",
    "minimax", "kimi", "yi-", "phi-3", "phi-4", "command-r",
    "glm-4", "internlm", "hermes",
    "deepseek-v", "deepseek-chat",
)
_MODEL_NO_TOOLS_KW = ("deepseek-r1", "gpt-oss")


def classify_endpoint(endpoint_url: str, model: str) -> dict:
    """Replicates the _is_api_model computation in agent_loop.py:3749-3774."""
    _model_lc = (model or "").lower()
    endpoint_supports = None
    try:
        _db = _SL()
        try:
            _ep = None
            for _key in al._endpoint_lookup_keys(endpoint_url):
                _ep = _db.query(_ME).filter(_ME.base_url == _key).first()
                if _ep is not None:
                    break
            if _ep is not None:
                endpoint_supports = _ep.supports_tools
        finally:
            _db.close()
    except Exception:
        pass
    model_supports_tools = any(kw in _model_lc for kw in _MODEL_SUPPORTS_TOOLS_KW)
    model_no_tools = any(kw in _model_lc for kw in _MODEL_NO_TOOLS_KW)
    is_ollama_native = al._is_ollama_native_url(endpoint_url or "")
    ollama_openai_compat = al._is_ollama_openai_compat_url(endpoint_url or "")

    if endpoint_supports is True:
        is_api_model, reason = True, "endpoint supports_tools=True (DB override)"
    elif (
        endpoint_supports is False
        or model_no_tools
        or is_ollama_native
        or ollama_openai_compat
    ):
        is_api_model, reason = False, (
            "endpoint supports_tools=False" if endpoint_supports is False else
            "model in no-tools list" if model_no_tools else
            "Ollama native endpoint" if is_ollama_native else
            "Ollama OpenAI-compat endpoint"
        )
    else:
        _host_hit = any(h in endpoint_url for h in al._API_HOSTS)
        is_api_model = _host_hit or model_supports_tools
        reason = f"host in _API_HOSTS ({_host_hit}) or model keyword ({model_supports_tools})"
    compact = is_api_model or is_ollama_native or ollama_openai_compat
    return {
        "endpoint_supports": endpoint_supports,
        "model_supports_tools": model_supports_tools,
        "model_no_tools": model_no_tools,
        "is_ollama_native": is_ollama_native,
        "ollama_openai_compat": ollama_openai_compat,
        "is_api_model": is_api_model,
        "compact": compact,
        "reason": reason,
    }


def pick_finetune_mode(model: str, flag: str) -> str:
    """odysseus-qwen fine-tunes force one of doc/notes/general; see 3603-3645."""
    if not (model or "").lower().startswith("odysseus-qwen3"):
        return "off"
    if flag and flag != "auto":
        return flag
    # auto: no intent/document context in a dump, so general is the default.
    return "general"


def build(messages, model, mcp_mgr, args, cls) -> dict:
    disabled_tools = set(args.disable_tool or [])
    # Mirrors the production loop (stream_agent_loop): the global settings
    # disabled_tools list (manage_settings disable_tool / Settings panel)
    # applies to every run, so a dump without --disable-tool flags still
    # reflects what the app actually ships.
    try:
        from src.settings import get_setting
        _global_disabled = get_setting("disabled_tools", [])
        if isinstance(_global_disabled, list):
            disabled_tools.update(_global_disabled)
    except Exception:
        pass
    relevant_tools = None  # production chat: RAG is disabled -> all-tools mode
    finetune = pick_finetune_mode(model, args.finetune)
    # --force-full renders the LOCAL-model variant (fenced-block preamble +
    # full rules, MCP-only schemas) regardless of the endpoint flag.
    prompt_compact = cls["compact"] and not args.force_full
    is_api = cls["is_api_model"] and not args.force_full

    messages, mcp_schemas = al._build_system_prompt(
        messages, model, None, mcp_mgr, disabled_tools,
        needs_admin=args.admin,
        relevant_tools=relevant_tools,
        mcp_disabled_map=None,
        compact=prompt_compact,
        owner=None,
        suppress_local_context=args.guide_only,
        suppress_skills=False,
        active_email=None,
        workspace=args.workspace,
    )

    # odysseus-qwen finetune minimal-prompt branches (agent_loop.py:3771-3804)
    if finetune == "doc":
        _tools = {"edit_document", "update_document", "suggest_document",
                  "ask_user", "update_plan"} if args.active_document else \
                 {"create_document", "ask_user", "update_plan"}
        relevant_tools = _tools
        mcp_schemas = []
        disabled_tools = set()
    elif finetune == "notes":
        relevant_tools = {"manage_notes", "manage_calendar", "manage_tasks",
                          "ask_user", "update_plan"}
        disabled_tools.difference_update(
            {"manage_notes", "manage_calendar", "manage_tasks"})
        mcp_schemas = []
    elif finetune == "general":
        relevant_tools = set()
        try:
            from src.tool_policy import known_tool_names
            disabled_tools.update(known_tool_names())
        except Exception:
            pass
        mcp_schemas = []

    # plan-mode / approved-plan / guide-only prepends (agent_loop.py:3807-3824)
    if args.plan_mode and not args.guide_only:
        if messages and messages[0].get("role") == "system":
            messages[0]["content"] = al.PLAN_MODE_DIRECTIVE + "\n\n" + \
                (messages[0].get("content") or "")
        else:
            messages.insert(0, {"role": "system", "content": al.PLAN_MODE_DIRECTIVE})
    if args.approved_plan and not args.guide_only:
        _plan_note = al.build_active_plan_note(args.approved_plan)
        if messages and messages[0].get("role") == "system":
            messages[0]["content"] = _plan_note + "\n\n" + \
                (messages[0].get("content") or "")
        else:
            messages.insert(0, {"role": "system", "content": _plan_note})
    if args.guide_only:
        if messages and messages[0].get("role") == "system":
            messages[0]["content"] = al.GUIDE_ONLY_DIRECTIVE + "\n\n" + \
                (messages[0].get("content") or "")
        else:
            messages.insert(0, {"role": "system", "content": al.GUIDE_ONLY_DIRECTIVE})

    # all_tool_schemas selection (agent_loop.py:4000-4045)
    _ody_qwen_finetune_model = (model or "").lower().startswith("odysseus-qwen3")
    if args.force_answer:
        all_tool_schemas = []
    elif is_api:
        if relevant_tools:
            _schema_names = set(relevant_tools)
            if args.admin:
                _schema_names |= al._ADMIN_TOOLS
            base_schemas = [
                s for s in FUNCTION_TOOL_SCHEMAS
                if s.get("function", {}).get("name") in _schema_names
            ]
            _mcp_filtered = [
                s for s in mcp_schemas
                if s.get("function", {}).get("name") in relevant_tools
            ]
            all_tool_schemas = base_schemas + _mcp_filtered
        else:
            base_schemas = FUNCTION_TOOL_SCHEMAS if args.admin else [
                s for s in FUNCTION_TOOL_SCHEMAS
                if s.get("function", {}).get("name") not in al._ADMIN_SCHEMA_NAMES
            ]
            all_tool_schemas = base_schemas + mcp_schemas
        if _ody_qwen_finetune_model:
            all_tool_schemas = []
        if disabled_tools:
            all_tool_schemas = [
                t for t in all_tool_schemas
                if t.get("function", {}).get("name") not in disabled_tools
                and t.get("name") not in disabled_tools
            ]
    else:
        # local models: MCP schemas only; native tools stay prompt-only.
        # Disabled tools are filtered out exactly like the API branch.
        all_tool_schemas = mcp_schemas or []
        if disabled_tools:
            all_tool_schemas = [
                t for t in all_tool_schemas
                if t.get("function", {}).get("name") not in disabled_tools
                and t.get("name") not in disabled_tools
            ]

    tool_names = [t.get("function", {}).get("name") for t in (all_tool_schemas or [])
                  if t.get("function")]
    return {
        "messages": messages,
        "mcp_schemas": mcp_schemas,
        "all_tool_schemas": all_tool_schemas,
        "tool_names": tool_names,
        "finetune": finetune,
        "tokens_messages": estimate_tokens(messages),
    }


def drop_datetime_message(messages):
    """Elide the per-turn [Context — current date/time] message (user-role)."""
    return [m for m in messages
            if not (m.get("role") == "user"
                    and str(m.get("content") or "").startswith(_DATETIME_MARKER))]


def build_verbatim_payload(endpoint_url, model, messages, tools, temperature,
                           max_tokens, tool_choice_none=False) -> dict:
    """Replicates llm_core._stream_llm_inner() payload construction exactly.

    Returns {provider, target_url, payload} where payload is the JSON body
    that stream_llm would POST (auth headers omitted).
    """
    provider = lc._detect_provider(endpoint_url)
    messages_copy = lc._sanitize_llm_messages(messages)

    # Consolidate multiple system messages into one at the start (some models,
    # e.g. Qwen3.5, reject system messages that aren't first).
    sys_parts, non_sys = [], []
    for m in messages_copy:
        if m.get("role") == "system":
            sys_parts.append(m.get("content") or "")
        else:
            non_sys.append(m)
    if sys_parts:
        messages_copy = [{"role": "system", "content": "\n\n".join(sys_parts)}] + non_sys
    else:
        messages_copy = non_sys

    if provider == "anthropic":
        target_url = lc._normalize_anthropic_url(endpoint_url)
        payload = lc._build_anthropic_payload(
            model, messages_copy, temperature, max_tokens, stream=True, tools=tools)
    elif provider == "ollama":
        target_url = lc._normalize_ollama_url(endpoint_url)
        payload = lc._build_ollama_payload(
            model, messages_copy, temperature, max_tokens,
            stream=True, tools=tools, num_ctx=lc.get_context_length(endpoint_url, model))
    elif provider == "chatgpt-subscription":
        target_url = lc._normalize_chatgpt_subscription_url(endpoint_url)
        payload = lc._build_chatgpt_responses_payload(
            model, messages_copy, temperature, max_tokens, stream=True)
    else:
        target_url = lc._normalize_openai_chat_url(endpoint_url)
        payload = {
            "model": model,
            "messages": messages_copy,
            "temperature": temperature,
            "stream": True,
        }
        if lc._omit_temperature(provider, model):
            payload.pop("temperature", None)
        if provider not in {"openrouter", "groq"}:
            payload["stream_options"] = {"include_usage": True}
        if max_tokens and max_tokens > 0:
            tok_key = "max_completion_tokens" if lc._uses_max_completion_tokens(model) else "max_tokens"
            payload[tok_key] = max_tokens
        if tools:
            payload["tools"] = tools
        elif tool_choice_none:
            payload["tool_choice"] = "none"
        if provider == "mistral" and lc._supports_thinking(model):
            payload["reasoning_effort"] = lc._MISTRAL_REASONING_EFFORT
        if lc._is_ollama_openai_compat_url(endpoint_url) and lc._supports_thinking(model):
            payload["think"] = False
        lc._disable_deepseek_v4_thinking(payload, model)
        lc._apply_local_cache_affinity(payload, endpoint_url, None)  # session_id: caller-side
        lc._apply_local_generation_stability(payload, target_url, model)
        lc._scrub_openai_chat_tool_reasoning(payload, target_url, model)

    return {"provider": provider, "target_url": target_url, "payload": payload}


def prompt_composition_note(cls, finetune):
    """Which building blocks made the system prompt (agent_loop.py:886-931)."""
    if finetune != "off":
        return f"odysseus-qwen minimal prompt ({finetune} mode) — not _assemble_prompt"
    if cls["compact"]:
        return ("compact variant: hardcoded opener + tool catalog + _API_AGENT_RULES "
                "+ domain rules (_assemble_prompt compact=True)")
    return ("full variant: _AGENT_PREAMBLE + tool catalog + _AGENT_RULES "
            "+ domain rules (_assemble_prompt compact=False)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--endpoint-url", default="http://localhost:1234/v1",
                    help="endpoint URL to classify (default: localhost LM Studio)")
    ap.add_argument("--model", default="nvidia-nemotron-3.5-lightning-30b-a3b",
                    help="model name (default: local Nemotron 3.5 Lightning)")
    ap.add_argument("--temperature", type=float, default=lc.LLMConfig.DEFAULT_TEMPERATURE,
                    help=f"temperature (default: {lc.LLMConfig.DEFAULT_TEMPERATURE})")
    ap.add_argument("--max-tokens", type=int, default=lc.LLMConfig.DEFAULT_MAX_TOKENS,
                    help=f"max_tokens (default: {lc.LLMConfig.DEFAULT_MAX_TOKENS})")
    ap.add_argument("--admin", action="store_true", help="needs_admin=True (full schema list incl. admin tools)")
    ap.add_argument("--force-answer", action="store_true", help="loop-breaker mode: ship NO tools")
    ap.add_argument("--force-full", action="store_true",
                    help="render the LOCAL-model variant (fenced-block preamble + full rules, MCP-only schemas) "
                         "instead of the classified API/compact one")
    ap.add_argument("--plan-mode", action="store_true", help="prepend PLAN_MODE_DIRECTIVE")
    ap.add_argument("--approved-plan", help="pin an approved plan note at top of context")
    ap.add_argument("--guide-only", action="store_true", help="guide-only turn (suppress local context + directive)")
    ap.add_argument("--workspace", help="workspace path (adds workspace coding rules to prompt)")
    ap.add_argument("--active-document", action="store_true", help="(finetune doc) treat as doc-active turn")
    ap.add_argument("--finetune", choices=["auto", "doc", "notes", "general", "off"], default="auto",
                    help="odysseus-qwen finetune mode (default auto)")
    ap.add_argument("--last-user", default="hi", help="last user message (used by intent heuristics)")
    ap.add_argument("--history", help="JSON file with a conversation message array ({role, content})")
    ap.add_argument("--connect-mcp", action="store_true", help="connect enabled MCP servers like the app does")
    ap.add_argument("--mcp-schemas", help="inject MCP schemas from a saved JSON dump (list of OpenAI schemas)")
    ap.add_argument("--disable-tool", action="append", help="tool name to disable (repeatable)")
    ap.add_argument("--include-datetime", action="store_true",
                    help="keep the [Context — current date/time] message in the dump (elided by default)")
    ap.add_argument("--brief", action="store_true", help="condensed view (truncated previews, no full payload)")
    ap.add_argument("--json", action="store_true", help="machine-readable JSON output")
    args = ap.parse_args()

    # history
    messages = []
    if args.history:
        with open(args.history) as f:
            messages = json.load(f)

    # MCP: connect like the app, or inject a saved dump
    mcp_mgr = get_mcp_manager()
    if mcp_mgr is None:
        # mirror app.py:810-811 — the app constructs the manager and sets it
        # as the global at startup; get_mcp_manager() otherwise returns None
        from src.mcp_manager import McpManager
        from src.tool_utils import set_mcp_manager as _set_mcp_manager
        mcp_mgr = McpManager()
        _set_mcp_manager(mcp_mgr)
    if args.connect_mcp:
        import asyncio
        try:
            async def _connect_like_app():
                # mirrors app.py startup: register built-in servers (python
                # stdio servers + NPX browser) then admin-configured DB rows
                from src.builtin_mcp import register_builtin_servers
                await register_builtin_servers(mcp_mgr)
                await mcp_mgr.connect_all_enabled()
                # builtins spawn background tasks; poll until they register
                # (browser has a 3s head start + npx spawn, so allow ~45s)
                wanted = {"image_gen", "memory", "rag", "email", "builtin_browser"}
                for _ in range(45):
                    if wanted.issubset(set(mcp_mgr._tools.keys())):
                        return
                    await asyncio.sleep(1)
            asyncio.run(_connect_like_app())
        except Exception as e:
            print(f"[warn] MCP connect failed: {e}", file=sys.stderr)
    _saved = None
    if args.mcp_schemas:
        with open(args.mcp_schemas) as f:
            _saved = json.load(f)

    cls = classify_endpoint(args.endpoint_url, args.model)
    out = build(messages, args.model, mcp_mgr, args, cls)
    out["classification"] = cls
    out["endpoint_url"] = args.endpoint_url
    out["model"] = args.model

    # overlay saved MCP schemas (post-build, same as a connected manager would give)
    if _saved is not None:
        out["mcp_schemas"] = _saved
        _was_api = cls["is_api_model"] and not args.force_full
        if args.force_answer:
            out["all_tool_schemas"] = []
        elif _was_api:
            base = FUNCTION_TOOL_SCHEMAS if args.admin else [
                s for s in FUNCTION_TOOL_SCHEMAS
                if s.get("function", {}).get("name") not in al._ADMIN_SCHEMA_NAMES]
            out["all_tool_schemas"] = base + _saved
        else:
            out["all_tool_schemas"] = _saved
        out["tool_names"] = [t.get("function", {}).get("name")
                             for t in out["all_tool_schemas"] if t.get("function")]

    # verbatim payload (datetime elided unless --include-datetime)
    payload_messages = out["messages"]
    if not args.include_datetime:
        payload_messages = drop_datetime_message(payload_messages)
        out["datetime_elided"] = True
    verbatim = build_verbatim_payload(
        args.endpoint_url, args.model, payload_messages,
        out["all_tool_schemas"] or None,
        args.temperature, args.max_tokens,
        tool_choice_none=(out["finetune"] == "doc"),
    )
    out["verbatim"] = verbatim
    out["payload_bytes"] = len(json.dumps(verbatim["payload"]))
    out["tokens_payload_messages"] = estimate_tokens(payload_messages)

    if args.json:
        print(json.dumps({
            "endpoint_url": out["endpoint_url"],
            "model": out["model"],
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "classification": out["classification"],
            "finetune": out["finetune"],
            "provider": verbatim["provider"],
            "target_url": verbatim["target_url"],
            "payload": verbatim["payload"],
            "messages": out["messages"],
            "tool_names": out["tool_names"],
            "tokens_messages": out["tokens_messages"],
            "tokens_payload_messages": out["tokens_payload_messages"],
            "payload_bytes": out["payload_bytes"],
            "datetime_elided": out.get("datetime_elided", False),
        }, indent=2))
        return

    cls = out["classification"]
    print("=" * 72)
    print("ODYSSEUS AGENT PROMPT DUMP — VERBATIM")
    print("=" * 72)
    print(f"endpoint : {out['endpoint_url']}")
    print(f"model    : {out['model']}")
    print(f"finetune : {out['finetune']}")
    print()
    print("── classification (agent_loop.py:3749-3774) ──")
    if args.force_full:
        print(f"  {'render':<22} --force-full: LOCAL-model variant (fenced-block prompt, MCP-only schemas)")
    for k in ("endpoint_supports", "model_supports_tools", "model_no_tools",
              "is_ollama_native", "ollama_openai_compat", "is_api_model", "compact"):
        print(f"  {k:<22} {cls[k]}")
    print(f"  {'reason':<22} {cls['reason']}")
    print(f"  [agent-debug] _is_api_model={cls['is_api_model']} "
          f"tools_sent={len(out['tool_names'])} tool_names={out['tool_names'][:15]}")
    print()
    print(f"prompt build: {prompt_composition_note(cls, out['finetune'])}")
    try:
        _ov = al.get_builtin_overrides() or {}
        if _ov:
            print(f"builtin overrides active: {sorted(_ov.keys())}")
    except Exception:
        pass
    if out.get("datetime_elided"):
        print("datetime context message elided (--include-datetime to restore)")
    print()

    print("── VERBATIM HTTP PAYLOAD (JSON body POSTed to the LLM; auth headers omitted) ──")
    print(f"provider    : {verbatim['provider']}")
    print(f"target_url  : {verbatim['target_url']}")
    print(f"payload size: {out['payload_bytes']} bytes, "
          f"~{out['tokens_payload_messages']} prompt tokens (messages)")
    print("-" * 72)
    if args.brief:
        print("(--brief: payload omitted — run without it for the full verbatim JSON)")
    else:
        print(json.dumps(verbatim["payload"], indent=2))
    print("-" * 72)

    print()
    print("── message array summary ──")
    for i, m in enumerate(out["messages"]):
        content = m.get("content") or ""
        tag = ""
        if str(content).startswith(_DATETIME_MARKER):
            tag = "  <-- datetime context"
        print(f"  [{i}] {m.get('role')}  ({len(content)} chars, ~{estimate_tokens([m])} tok){tag}")
    print(f"  prompt tokens (messages): {out['tokens_messages']}")
    print()
    print("── tools array (payload['tools'] if present) ──")
    if not out["all_tool_schemas"]:
        print("  (no tool schemas — model must answer in prose / fenced blocks)")
    for t in out["all_tool_schemas"]:
        fn = t.get("function", {})
        name = fn.get("name") or t.get("name", "?")
        src = "native" if name in {s.get("function", {}).get("name") for s in FUNCTION_TOOL_SCHEMAS} else "MCP"
        print(f"  - {name}  [{src}]")
    print(f"  total schemas sent to LLM : {len(out['all_tool_schemas'])} "
          f"(native={sum(1 for t in out['all_tool_schemas'] if t.get('function', {}).get('name') in {s.get('function', {}).get('name') for s in FUNCTION_TOOL_SCHEMAS})}, "
          f"mcp={len(out['mcp_schemas'])})")


if __name__ == "__main__":
    main()
