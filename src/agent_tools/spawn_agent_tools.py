"""spawn_agent_tools.py — the spawn_agent tool: run a full sub-agent loop.

Unlike chat_with_model (a bare LLM completion with no tools), spawn_agent runs
a complete stream_agent_loop WITH tool access for the sub-agent, headless, and
returns the sub-agent's final report to the parent. This is the Tier-1
multi-agent primitive: delegation with tools. Parallel fan-out, agent teams,
and debate patterns all build on it.

The headless consumption pattern mirrors task_scheduler._run_agent_task
(collect delta text + tool_output summaries from the SSE event stream), but
with different guards because a sub-agent runs MID-parent-turn:

  - No interactive gate: the parent IS the interactive run, so waiting for
    "interactive quiet" would deadlock. Inference-server contention is the
    server's problem, not ours.
  - Depth limit: the inner loop gets spawn_agent in disabled_tools (hidden
    from its catalog AND blocked at its execution gate), and the handler
    additionally refuses when ctx carries subagent_depth >= 1 (threaded from
    stream_agent_loop's _subagent_depth via extra_ctx). Two independent locks
    on the same door — fork-bombing the RAM needs both to fail.
  - Concurrency: module semaphore caps simultaneous sub-agents; extra spawns
    queue inside the caller's timeout budget rather than failing.
  - Per-spawn round cap + wall-clock timeout.

Model resolution order: explicit `model` arg → `subagent_model` setting →
the parent's own endpoint/model (via extra_ctx). Fresh context, same brain by
default — "clone myself with a clean slate" is the predictable semantic.
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Dict, Optional, Tuple

logger = logging.getLogger(__name__)

# v1 depth limit: parents may spawn; sub-agents may not. Tier 2 (nested
# spawning) relaxes this by decrementing depth instead of refusing.
_MAX_SUBAGENT_DEPTH = 1
_MAX_CONCURRENT_SUBAGENTS = 3
_SUBAGENT_SEM = asyncio.Semaphore(_MAX_CONCURRENT_SUBAGENTS)

_DEFAULT_MAX_ROUNDS = 15
_HARD_MAX_ROUNDS = 30
_DEFAULT_TIMEOUT_MIN = 10.0
_HARD_MAX_TIMEOUT_MIN = 30.0
_MAX_REPORT_CHARS = 12000

_SUBAGENT_SYSTEM_PROMPT = (
    "You are a focused sub-agent spawned by a parent AI agent to complete one "
    "task autonomously. Use your tools to complete the task thoroughly, then "
    "produce a clear, self-contained final report — the parent agent sees ONLY "
    "your final report, not your intermediate steps. You cannot ask the user "
    "questions and you cannot spawn further sub-agents. If the task turns out "
    "to be impossible, state exactly what failed and what you tried."
)


def _parse_args(content: str) -> Dict:
    """Accept JSON args (native function calls) or raw text (fence callers).

    Fence-model callers were taught the JSON shape in the tool catalog, but a
    bare task string is accepted as a graceful fallback: whole content = task.
    """
    c = (content or "").strip()
    if c.startswith("{"):
        try:
            data = json.loads(c)
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    return {"task": c}


def _headers_for_endpoint(endpoint_url: str, owner: Optional[str]) -> Dict:
    """Best-effort auth headers for a parent endpoint URL (task_scheduler pattern)."""
    try:
        from core.database import SessionLocal, ModelEndpoint
        from src.endpoint_resolver import normalize_base, build_headers
        from src.auth_helpers import owner_filter

        db = SessionLocal()
        try:
            q = db.query(ModelEndpoint).filter(ModelEndpoint.is_enabled == True)
            q = owner_filter(q, ModelEndpoint, owner)
            for ep in q.all():
                if normalize_base(ep.base_url) in endpoint_url or endpoint_url in normalize_base(ep.base_url):
                    return build_headers(ep.api_key, normalize_base(ep.base_url))
        finally:
            db.close()
    except Exception as e:
        logger.debug("[spawn_agent] header lookup failed for %s: %s", endpoint_url, e)
    return {}


async def _resolve_subagent_model(
    model_spec: str,
    owner: Optional[str],
    parent_endpoint: Optional[str],
    parent_model: Optional[str],
    parent_headers: Optional[Dict],
) -> Optional[Tuple[str, str, Dict]]:
    """Shared model resolution: explicit spec → subagent_model setting → the
    parent's own brain. Returns (url, model, headers), or None when no model
    is available. Raises ValueError on a bad explicit spec."""
    from src.ai_interaction import _resolve_model
    from src.settings import get_setting

    spec = (model_spec or "").strip() or (get_setting("subagent_model", "") or "").strip()
    if spec:
        url, model, headers = await asyncio.to_thread(_resolve_model, spec, owner=owner)
        return url, model, headers
    if parent_endpoint and parent_model:
        return parent_endpoint, parent_model, (parent_headers or _headers_for_endpoint(parent_endpoint, owner))
    return None


async def run_subagent(
    task: str,
    model_spec: str = "",
    system_prompt: str = "",
    max_rounds: int = _DEFAULT_MAX_ROUNDS,
    timeout_minutes: float = _DEFAULT_TIMEOUT_MIN,
    session_id: Optional[str] = None,
    owner: Optional[str] = None,
    parent_endpoint: Optional[str] = None,
    parent_model: Optional[str] = None,
    parent_headers: Optional[Dict] = None,
    preresolved: Optional[Tuple[str, str, Dict]] = None,
    subagent_depth: int = 0,
) -> Dict:
    """Run a full agent loop for `task` and return the sub-agent's report."""
    task = (task or "").strip()
    if not task:
        return {"error": "No task provided."}
    if subagent_depth >= _MAX_SUBAGENT_DEPTH:
        return {"error": "spawn_agent is not available to sub-agents (depth limit)."}

    # --- Resolve the sub-agent's brain -------------------------------------
    # (background launches resolve eagerly so a bad model spec fails fast at
    # launch time instead of producing a dead job — they pass preresolved.)
    if preresolved is not None:
        url, model, headers = preresolved
    else:
        try:
            resolved = await _resolve_subagent_model(
                model_spec, owner, parent_endpoint, parent_model, parent_headers
            )
        except ValueError as e:
            return {"error": str(e)}
        if resolved is None:
            return {
                "error": "No model for sub-agent: pass 'model', set the subagent_model "
                "setting, or spawn from an agent session."
            }
        url, model, headers = resolved

    # --- Clamp guards -------------------------------------------------------
    try:
        max_rounds = min(max(int(max_rounds or _DEFAULT_MAX_ROUNDS), 1), _HARD_MAX_ROUNDS)
    except (TypeError, ValueError):
        max_rounds = _DEFAULT_MAX_ROUNDS
    try:
        timeout_s = min(max(float(timeout_minutes or _DEFAULT_TIMEOUT_MIN), 0.5), _HARD_MAX_TIMEOUT_MIN) * 60
    except (TypeError, ValueError):
        timeout_s = _DEFAULT_TIMEOUT_MIN * 60

    now = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M (%Z)").strip()
    system = (system_prompt or "").strip() or _SUBAGENT_SYSTEM_PROMPT
    if now:
        system = f"{system}\n\nCurrent date/time: {now}"
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": task},
    ]
    # Synthetic session id: llm_core uses session_id for local cache-slot
    # affinity only; run registration lives in chat_routes, so this creates
    # no DB rows and cannot collide with the parent's active run.
    sub_session_id = f"{session_id or 'sub'}-subagent-{uuid.uuid4().hex[:8]}"

    from src.agent_loop import stream_agent_loop  # lazy: avoids import cycle

    full_text = ""
    tool_counts: Dict[str, int] = {}
    tool_samples = []
    rounds = 0
    truncated = False

    async with _SUBAGENT_SEM:
        try:
            async with asyncio.timeout(timeout_s):
                async for event_str in stream_agent_loop(
                    endpoint_url=url,
                    model=model,
                    messages=messages,
                    headers=headers,
                    max_rounds=max_rounds,
                    session_id=sub_session_id,
                    owner=owner,
                    disabled_tools={"spawn_agent"},
                    workload="background",
                    _is_teacher_run=True,  # reuse the existing "not the primary chat" flag
                    _subagent_depth=subagent_depth + 1,
                ):
                    if not event_str.startswith("data: ") or event_str.startswith("data: [DONE]"):
                        continue
                    try:
                        data = json.loads(event_str[6:])
                    except json.JSONDecodeError:
                        continue
                    if "delta" in data:
                        if data.get("thinking"):
                            continue
                        full_text += data["delta"]
                    elif data.get("type") == "tool_output":
                        t = data.get("tool", "?")
                        tool_counts[t] = tool_counts.get(t, 0) + 1
                        sample = (
                            data.get("stdout") or data.get("output")
                            or data.get("result") or data.get("response") or ""
                        )
                        if isinstance(sample, str) and sample.strip():
                            tool_samples.append(f"[{t}] {sample.strip()[:300]}")
                    elif data.get("type") == "agent_step":
                        try:
                            rounds = max(rounds, int(data.get("round", 0)))
                        except (TypeError, ValueError):
                            pass
        except TimeoutError:
            truncated = True
        except asyncio.CancelledError:
            # Parent turn cancelled (user hit stop) — propagate, don't swallow.
            raise
        except Exception as e:
            logger.error("[spawn_agent] sub-agent loop failed: %s", e)
            return {"error": f"Sub-agent failed: {e}"}

    # --- Grace fallbacks (task_scheduler pattern) ---------------------------
    if not full_text.strip():
        if tool_samples:
            full_text = (
                "(sub-agent hit its limit before writing a final report. "
                "Last tool outputs:\n" + "\n".join(tool_samples[-5:]) + ")"
            )
        else:
            full_text = "(sub-agent produced no output" + (" — timed out" if truncated else "") + ")"
    elif truncated:
        full_text += "\n\n[NOTE: sub-agent hit the timeout mid-work; report may be incomplete.]"

    if tool_counts:
        counts = ", ".join(f"{t}×{n}" for t, n in sorted(tool_counts.items(), key=lambda kv: -kv[1]))
        full_text += f"\n\n[sub-agent tools used: {counts}; rounds: {rounds}]"

    if len(full_text) > _MAX_REPORT_CHARS:
        full_text = full_text[:_MAX_REPORT_CHARS] + "\n... (truncated)"

    return {"model": model, "response": full_text, "rounds": rounds, "truncated": truncated}


class SpawnAgentTool:
    async def execute(self, content: str, ctx: dict) -> Dict:
        args = _parse_args(content)
        if args.get("background"):
            # Tier-2 fire-and-forget: return an agent id immediately; the
            # report is delivered to the parent session when the worker
            # finishes (agent_jobs monitor) or via check_agents polling.
            from src import agent_jobs
            rec = await agent_jobs.launch_background_agent(
                task=str(args.get("task") or ""),
                model_spec=str(args.get("model") or ""),
                system_prompt=str(args.get("system_prompt") or ""),
                max_rounds=args.get("max_rounds") or _DEFAULT_MAX_ROUNDS,
                timeout_minutes=args.get("timeout_minutes") or _DEFAULT_TIMEOUT_MIN,
                parent_session_id=ctx.get("session_id"),
                owner=ctx.get("owner"),
                parent_endpoint=ctx.get("endpoint_url"),
                parent_model=ctx.get("model"),
                parent_headers=ctx.get("headers"),
            )
            if rec.get("error"):
                return {"error": rec["error"]}
            return {
                "output": rec.get("launch_message") or f"Background agent {rec.get('id')} launched.",
                "exit_code": 0,
            }
        return await run_subagent(
            task=str(args.get("task") or ""),
            model_spec=str(args.get("model") or ""),
            system_prompt=str(args.get("system_prompt") or ""),
            max_rounds=args.get("max_rounds") or _DEFAULT_MAX_ROUNDS,
            timeout_minutes=args.get("timeout_minutes") or _DEFAULT_TIMEOUT_MIN,
            session_id=ctx.get("session_id"),
            owner=ctx.get("owner"),
            parent_endpoint=ctx.get("endpoint_url"),
            parent_model=ctx.get("model"),
            parent_headers=ctx.get("headers"),
            subagent_depth=int(ctx.get("subagent_depth") or 0),
        )


class CheckAgentsTool:
    """Status + collection for background sub-agents (spawn_agent background=true)."""

    async def execute(self, content: str, ctx: dict) -> Dict:
        from src import agent_jobs
        agent_id = (content or "").strip()
        if agent_id.startswith("{"):
            # Native callers may arrive as JSON {"agent_id": "..."}.
            try:
                data = json.loads(agent_id)
                if isinstance(data, dict):
                    agent_id = str(data.get("agent_id") or "").strip()
            except json.JSONDecodeError:
                pass
        return {"output": agent_jobs.collect_status(agent_id or None), "exit_code": 0}
