"""Smoke tests for the spawn_agent tool (Tier-1 multi-agent primitive).

Pure-unit: no network, no DB writes. Verifies registry wiring, schema
conversion, prompt-catalog visibility, recursion-guard plumbing, and the
content parser. Run: ./venv/bin/python -m pytest tests/test_spawn_agent.py -q
"""

import json

from src.agent_tools import TOOL_HANDLERS, TOOL_TAGS
from src.tool_schemas import FUNCTION_TOOL_SCHEMAS, function_call_to_tool_block
from src.agent_tools.spawn_agent_tools import _parse_args, run_subagent


def _schema_names():
    return {
        (s.get("function") or {}).get("name")
        for s in FUNCTION_TOOL_SCHEMAS
    }


def test_registered_everywhere():
    assert "spawn_agent" in TOOL_HANDLERS
    assert "spawn_agent" in TOOL_TAGS
    assert "spawn_agent" in _schema_names()


def test_native_call_conversion():
    block = function_call_to_tool_block(
        "spawn_agent",
        json.dumps({"task": "count files", "model": "qwen3-32b", "max_rounds": 5}),
    )
    assert block is not None
    assert block.tool_type == "spawn_agent"
    args = json.loads(block.content)
    assert args["task"] == "count files"
    assert args["model"] == "qwen3-32b"
    assert args["max_rounds"] == 5


def test_native_call_requires_task():
    assert function_call_to_tool_block("spawn_agent", json.dumps({"model": "x"})) is None


def test_parse_args_json_and_raw():
    parsed = _parse_args('{"task": "do a thing", "timeout_minutes": 2}')
    assert parsed["task"] == "do a thing"
    assert parsed["timeout_minutes"] == 2
    # Raw text (fence callers ignoring the JSON shape) → whole content is task
    parsed = _parse_args("go count the files in /tmp")
    assert parsed["task"] == "go count the files in /tmp"
    # Malformed JSON that starts with { → falls back to raw task text
    parsed = _parse_args('{"task": broken json')
    assert "broken" in parsed["task"]


def test_prompt_catalog_visibility_and_recursion_guard():
    from src.agent_loop import _assemble_prompt

    shown = _assemble_prompt({"spawn_agent", "bash"}, set())
    assert "- `spawn_agent` —" in shown

    # Recursion guard: disabled tools vanish from the sub-agent's catalog.
    hidden = _assemble_prompt({"spawn_agent", "bash"}, {"spawn_agent"})
    assert "- `spawn_agent` —" not in hidden


def test_depth_guard_refuses_nested_spawn():
    import asyncio

    async def _run():
        return await run_subagent(
            task="anything",
            model_spec="whatever",
            subagent_depth=1,  # sub-agents may not spawn
        )

    result = asyncio.run(_run())
    assert "error" in result
    assert "depth" in result["error"]


def test_empty_task_refused():
    import asyncio

    async def _run():
        return await run_subagent(task="  ", model_spec="x")

    result = asyncio.run(_run())
    assert "error" in result


def test_end_to_end_subagent_run(monkeypatch):
    """Full round-trip: spawn_agent → inner stream_agent_loop → tool exec → report."""
    import asyncio

    import src.agent_loop as al
    import src.settings as settings_mod
    from src.agent_tools.spawn_agent_tools import run_subagent

    # Sub-agent model resolution: no subagent_model setting → parent's brain.
    monkeypatch.setattr(settings_mod, "get_setting", lambda key, default=None: default, raising=False)

    # Inner loop environment: skip RAG/MCP, fake tool execution.
    monkeypatch.setattr(al, "get_setting", lambda key, default=None: default, raising=False)
    monkeypatch.setattr(al, "get_mcp_manager", lambda: None, raising=False)
    monkeypatch.setattr(al, "estimate_tokens", lambda *a, **k: 10, raising=False)

    async def _fake_exec(block, *a, **k):
        return ("bash", {"output": "42 files", "exit_code": 0})

    monkeypatch.setattr(al, "execute_tool_block", _fake_exec, raising=False)

    calls = {"n": 0}

    async def _fake_stream(_candidates, messages, **kwargs):
        calls["n"] += 1
        if calls["n"] == 1:
            # Native tool-call channel (the loop's current protocol): a text
            # delta plus a {"type": "tool_calls"} event, as llm_core emits.
            yield 'data: {"delta": "Let me count."}\n\n'
            yield ('data: {"type": "tool_calls", "calls": [{"name": "bash", '
                   '"arguments": "{\\"command\\": \\"echo counting\\"}"}]}\n\n')
            yield "data: [DONE]\n\n"
        else:
            yield 'data: {"delta": "SUBAGENT_REPORT_DONE: 42 files counted."}\n\n'
            yield "data: [DONE]\n\n"

    monkeypatch.setattr(al, "stream_llm_with_fallback", _fake_stream, raising=False)

    async def _run():
        return await run_subagent(
            task="count the files",
            session_id="parent-1",
            owner=None,
            parent_endpoint="http://x/v1",
            parent_model="m",
            parent_headers={},
        )

    result = asyncio.run(_run())
    assert "error" not in result, result
    assert "SUBAGENT_REPORT_DONE" in result["response"]
    assert result["model"] == "m"
    # Tool trace footer proves the inner loop executed tools.
    assert "bash×1" in result["response"]
    assert result["truncated"] is False
    assert calls["n"] == 2  # tool round + final report round


# ---------------------------------------------------------------------------
# Tier-2: background launches + check_agents tool surface
# ---------------------------------------------------------------------------
import asyncio  # noqa: E402 — used by the Tier-2 tests below
import json  # noqa: E402

def test_background_param_and_check_agents_registered():
    from src.agent_tools import TOOL_HANDLERS, TOOL_TAGS
    from src.tool_schemas import FUNCTION_TOOL_SCHEMAS, _REQUIRED_NATIVE_TOOL_ARGS

    assert "check_agents" in TOOL_HANDLERS and "check_agents" in TOOL_TAGS
    names = {s["function"]["name"] for s in FUNCTION_TOOL_SCHEMAS}
    assert {"spawn_agent", "check_agents"} <= names
    spawn = next(s for s in FUNCTION_TOOL_SCHEMAS if s["function"]["name"] == "spawn_agent")
    assert "background" in spawn["function"]["parameters"]["properties"]
    assert _REQUIRED_NATIVE_TOOL_ARGS.get("check_agents") == ()


def test_spawn_agent_tool_background_branch(monkeypatch):
    from src.agent_tools.spawn_agent_tools import SpawnAgentTool

    captured = {}

    async def fake_launch(**kwargs):
        captured.update(kwargs)
        return {"id": "ag-fake123", "status": "running", "model": "m",
                "launch_message": "Background agent ag-fake123 launched (model: m)."}

    import src.agent_jobs as aj
    monkeypatch.setattr(aj, "launch_background_agent", fake_launch)

    result = asyncio.run(SpawnAgentTool().execute(
        json.dumps({"task": "t", "background": True, "max_rounds": 5}),
        {"session_id": "s1", "owner": None, "endpoint_url": "http://x/v1",
         "model": "m", "headers": {}},
    ))
    assert "ag-fake123" in result["output"]
    assert captured["parent_session_id"] == "s1"
    assert captured["max_rounds"] == 5


def test_spawn_agent_tool_background_error_passthrough(monkeypatch):
    from src.agent_tools.spawn_agent_tools import SpawnAgentTool

    async def fake_launch(**kwargs):
        return {"error": "Unknown model 'nope'"}

    import src.agent_jobs as aj
    monkeypatch.setattr(aj, "launch_background_agent", fake_launch)
    result = asyncio.run(SpawnAgentTool().execute(
        json.dumps({"task": "t", "background": True}), {},
    ))
    assert "nope" in result["error"]


def test_check_agents_tool_collects(monkeypatch):
    from src.agent_tools.spawn_agent_tools import CheckAgentsTool

    import src.agent_jobs as aj
    monkeypatch.setattr(aj, "collect_status",
                        lambda agent_id=None: f"listing for {agent_id}")
    result = asyncio.run(CheckAgentsTool().execute("ag-xyz", {}))
    assert result["output"] == "listing for ag-xyz"
    # JSON content form (native callers)
    result2 = asyncio.run(CheckAgentsTool().execute('{"agent_id": "ag-json"}', {}))
    assert result2["output"] == "listing for ag-json"
