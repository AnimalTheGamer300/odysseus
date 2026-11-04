"""agent_jobs.py — background (fire-and-forget) sub-agents.

Tier-2 multi-agent primitive: ``spawn_agent`` with ``background=true`` launches
a full sub-agent loop (WITH tool access) as an asyncio task and returns an
agent id IMMEDIATELY, so the parent can keep working. When the worker
finishes, an always-on monitor delivers the report by re-invoking the agent in
the parent session (the bg_monitor "auto-continue" pattern) — and/or the
parent can poll actively via the ``check_agents`` tool.

Design (mirrors src/bg_jobs.py + src/bg_monitor.py where it fits):

  * Registry: data/agent_jobs.json via atomic writes. Finished results
    survive a restart; RUNNING entries cannot (they live as asyncio tasks in
    this process), so on load they are marked ``interrupted`` and still get a
    follow-up ("was interrupted by a restart") — the parent always hears back.
  * Delivery: exactly-once semantics via the ``delivered`` flag. The monitor
    injects the report into the parent session; check_agents collection also
    marks delivered (the parent already saw it — a later wake-up would just
    repeat news).
  * Busy-deferral: never write into a session mid-stream (agent_runs.is_active
    check, same as bg_monitor) — deferred follow-ups retry on the next tick.
  * Idempotent: ``delivered`` is only set AFTER the follow-up run succeeds, so
    a transient failure retries on the next tick.
  * Bounded: delivered entries are pruned after 1h; hard cap on stored jobs.

The worker itself is run_subagent() from spawn_agent_tools (same guards:
depth limit, semaphore, round cap, timeout) — background agents share the
sub-agent concurrency budget with blocking spawns.
"""

from __future__ import annotations

import asyncio
import json
import logging
import time
import uuid
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from core.atomic_io import atomic_write_json
from src.constants import AGENT_JOBS_FILE

logger = logging.getLogger(__name__)

_JOB_FILE = Path(AGENT_JOBS_FILE)
_MAX_STORED_JOBS = 40
_RETENTION_S = 3600  # 1h after delivery, like bg_jobs
_POLL_INTERVAL_S = 5
_FOLLOWUP_MAX_ROUNDS = 12  # bg_monitor parity: the continuation gets a few rounds
_MAX_TASK_CHARS = 2000  # stored task text cap (the worker gets the full task)

_JOBS: Dict[str, Dict] = {}
_LOADED = False
_LIVE_TASKS: Dict[str, asyncio.Task] = {}
_monitor_task = None


# ---------------------------------------------------------------------------
# Registry persistence
# ---------------------------------------------------------------------------

def _ensure_loaded() -> None:
    if not _LOADED:
        _load_registry()


def _load_registry() -> None:
    global _LOADED
    _LOADED = True
    try:
        if _JOB_FILE.exists():
            data = json.loads(_JOB_FILE.read_text(encoding="utf-8")) or {}
            if isinstance(data, dict):
                now = time.time()
                for jid, rec in data.items():
                    if not isinstance(rec, dict):
                        continue
                    if rec.get("status") == "running":
                        # asyncio tasks don't survive a restart — the worker
                        # died with the old process. Report it honestly.
                        rec["status"] = "interrupted"
                        rec["finished_at"] = rec.get("finished_at") or now
                        rec["error"] = "Odysseus restarted while this agent was running."
                        if not (rec.get("result") or "").strip():
                            rec["result"] = (
                                "(background agent was interrupted by an app "
                                "restart before it could finish.)"
                            )
                    _JOBS[str(jid)] = rec
    except Exception as e:
        logger.warning("[agent_jobs] registry load failed: %s", e)


def _save_registry() -> None:
    try:
        now = time.time()
        recs = list(_JOBS.values())
        # Prune delivered entries past retention, then enforce the cap
        # (oldest delivered go first — undelivered results are the precious ones).
        keep = [
            r for r in recs
            if not (r.get("delivered") and (now - (r.get("finished_at") or now)) > _RETENTION_S)
        ]
        if len(keep) > _MAX_STORED_JOBS:
            keep.sort(key=lambda r: (bool(r.get("delivered")), r.get("launched_at", 0)))
            keep = keep[-_MAX_STORED_JOBS:]
        _JOBS.clear()
        for r in keep:
            _JOBS[r["id"]] = r
        atomic_write_json(str(_JOB_FILE), _JOBS, indent=2)
    except Exception as e:
        logger.warning("[agent_jobs] registry save failed: %s", e)


def _reset_for_tests() -> None:
    """Test hook: wipe in-memory state so each test starts from a clean slate."""
    global _LOADED, _monitor_task
    _JOBS.clear()
    _LIVE_TASKS.clear()
    _LOADED = False
    _monitor_task = None


# ---------------------------------------------------------------------------
# Launch + worker
# ---------------------------------------------------------------------------

async def launch_background_agent(
    task: str,
    model_spec: str = "",
    system_prompt: str = "",
    max_rounds: int = 15,
    timeout_minutes: float = 10.0,
    parent_session_id: Optional[str] = None,
    owner: Optional[str] = None,
    parent_endpoint: Optional[str] = None,
    parent_model: Optional[str] = None,
    parent_headers: Optional[Dict] = None,
) -> Dict:
    """Launch a sub-agent in the background. Returns the registry record with
    a ``launch_message`` (or ``{"error": ...}``) — never blocks on the work."""
    from src.agent_tools.spawn_agent_tools import _resolve_subagent_model

    _ensure_loaded()
    task = (task or "").strip()
    if not task:
        return {"error": "No task provided."}
    try:
        resolved = await _resolve_subagent_model(
            model_spec, owner, parent_endpoint, parent_model, parent_headers
        )
    except ValueError as e:
        return {"error": str(e)}
    if resolved is None:
        return {
            "error": "No model for background agent: pass 'model', set the "
            "subagent_model setting, or spawn from an agent session."
        }
    url, model, headers = resolved

    job_id = f"ag-{uuid.uuid4().hex[:8]}"
    rec: Dict = {
        "id": job_id,
        "task": task[:_MAX_TASK_CHARS],
        "model": model,
        "status": "running",
        "parent_session_id": parent_session_id or "",
        "launched_at": time.time(),
        "finished_at": None,
        "result": "",
        "rounds": 0,
        "truncated": False,
        "error": None,
        "delivered": False,
        "collected": False,
    }
    _JOBS[job_id] = rec
    _save_registry()

    t = asyncio.create_task(_run_agent_job(
        job_id, task, url, model, headers, system_prompt,
        max_rounds, timeout_minutes, parent_session_id, owner,
    ))
    _LIVE_TASKS[job_id] = t  # strong ref — an unreferenced task can be GC'd mid-run
    t.add_done_callback(lambda _t, _id=job_id: _LIVE_TASKS.pop(_id, None))
    logger.info("[agent_jobs] launched %s (model %s, parent session %s)",
                job_id, model, parent_session_id)

    rec["launch_message"] = (
        f"Background agent {job_id} launched (model: {model}). It runs with full "
        f"tool access; its report will be delivered to this conversation "
        f"automatically when it finishes — or check progress anytime with "
        f"check_agents."
    )
    return rec


async def _run_agent_job(
    job_id: str,
    task: str,
    url: str,
    model: str,
    headers: Dict,
    system_prompt: str,
    max_rounds: int,
    timeout_minutes: float,
    parent_session_id: Optional[str],
    owner: Optional[str],
) -> None:
    from src.agent_tools.spawn_agent_tools import run_subagent

    try:
        res = await run_subagent(
            task=task,
            model_spec="",  # already resolved — preresolved skips resolution
            system_prompt=system_prompt,
            max_rounds=max_rounds,
            timeout_minutes=timeout_minutes,
            session_id=parent_session_id,
            owner=owner,
            parent_endpoint=url,
            parent_model=model,
            parent_headers=headers,
            preresolved=(url, model, headers),
        )
        rec = _JOBS.get(job_id)
        if rec is None:
            return
        rec["finished_at"] = time.time()
        if res.get("error"):
            rec["status"] = "failed"
            rec["error"] = str(res["error"])[:500]
            rec["result"] = f"(background agent failed: {res['error']})"
        else:
            rec["status"] = "timeout" if res.get("truncated") else "done"
            rec["result"] = res.get("response", "")
            rec["rounds"] = res.get("rounds", 0)
            rec["truncated"] = bool(res.get("truncated"))
        logger.info("[agent_jobs] %s -> %s (%d chars)",
                    job_id, rec["status"], len(rec.get("result") or ""))
    except asyncio.CancelledError:
        rec = _JOBS.get(job_id)
        if rec is not None and rec.get("status") == "running":
            rec["status"] = "interrupted"
            rec["finished_at"] = time.time()
            rec["error"] = "cancelled"
            _save_registry()
        raise
    except Exception as e:  # noqa: BLE001 — a worker must never take the monitor down
        rec = _JOBS.get(job_id)
        if rec is not None:
            rec["status"] = "failed"
            rec["finished_at"] = time.time()
            rec["error"] = str(e)[:500]
            rec["result"] = f"(background agent failed: {e})"
            logger.error("[agent_jobs] %s failed: %s", job_id, e)
    finally:
        _save_registry()


# ---------------------------------------------------------------------------
# Delivery: monitor + follow-up (bg_monitor pattern)
# ---------------------------------------------------------------------------

def pending_deliveries() -> List[Dict]:
    """Finished jobs whose report the parent session hasn't received yet."""
    _ensure_loaded()
    return [
        r for r in _JOBS.values()
        if r.get("status") not in ("running", None) and not r.get("delivered")
    ]


async def _run_followup(rec: Dict) -> bool:
    """Inject the finished agent's report into the parent session and run a
    short headless continuation. Returns True when handled (delivered or
    nothing to do) — False defers to the next tick."""
    from src.ai_interaction import get_session_manager
    from core.models import ChatMessage

    sm = get_session_manager()
    if not sm:
        return False  # app still starting — retry
    sess = sm.get_session(rec.get("parent_session_id") or "")
    if not sess:
        logger.info("[agent_jobs] parent session gone for %s — skipping delivery",
                    rec.get("id"))
        return True  # nothing to deliver to; consider it handled

    # Never write into a session mid-stream — the follow-up appends to history
    # and a concurrent live turn does the same; they'd interleave. Defer.
    try:
        from src import agent_runs
        if agent_runs.is_active(sess.id):
            logger.info("[agent_jobs] session %s busy — deferring %s",
                        sess.id, rec.get("id"))
            return False
    except Exception:
        pass

    status = rec.get("status", "done")
    report = (rec.get("result") or "").strip() or f"(error: {rec.get('error')})"
    inject = (
        f"[Background agent {rec['id']} finished — status: {status}]\n\n"
        f"Task it was given: {(rec.get('task') or '')[:500]}\n\n"
        f"{report}\n\n"
        "Continue the original task using this result. Don't repeat work the "
        "agent already did. If everything is complete, give the user a concise "
        "summary."
    )

    from src.bg_monitor import _drain_agent  # reuse the headless SSE consumer

    context = sess.get_context_messages()
    context.append({"role": "user", "content": inject})
    full, tool_events = await _drain_agent(sess, context)
    if not (full or "").strip():
        # Continuation produced nothing (model hiccup) — deliver the raw report
        # itself so the result always reaches the user.
        full = f"[Background agent {rec['id']} — {status}]\n\n{report}"
        tool_events = []

    # Persist ONLY the assistant continuation so it renders as a normal agent
    # turn (bg_monitor pattern); the trigger isn't saved as its own bubble.
    sm.add_message(sess.id, ChatMessage(
        "assistant", full,
        metadata={
            "tool_events": tool_events,
            "model": getattr(sess, "model", ""),
            "agent_job_id": rec["id"],
            "agent_result": report[:4000],
        },
    ))
    sm.save_sessions()
    logger.info("[agent_jobs] delivered %s to session %s (%d chars, %d tools)",
                rec["id"], sess.id, len(full), len(tool_events))
    return True


async def _loop() -> None:
    while True:
        try:
            for rec in pending_deliveries():
                try:
                    if await _run_followup(rec):
                        rec["delivered"] = True
                        _save_registry()
                except Exception as e:
                    # Idempotent: delivered stays False, next tick retries.
                    logger.warning("[agent_jobs] delivery failed for %s (will retry): %s",
                                   rec.get("id"), e)
        except Exception as e:  # noqa: BLE001 — the monitor must never die
            logger.warning("[agent_jobs] monitor tick error: %s", e)
        await asyncio.sleep(_POLL_INTERVAL_S)


def start_agent_job_monitor():
    """Idempotent — start the always-on background-agent delivery monitor."""
    global _monitor_task
    if _monitor_task and not _monitor_task.done():
        return _monitor_task
    _monitor_task = asyncio.create_task(_loop())
    logger.info("Background-agent monitor started (poll %ds)", _POLL_INTERVAL_S)
    return _monitor_task


# ---------------------------------------------------------------------------
# check_agents: status listing + active collection
# ---------------------------------------------------------------------------

def _fmt_age(seconds: float) -> str:
    s = max(0, int(seconds))
    if s < 60:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}m"
    return f"{s // 3600}h {(s % 3600) // 60}m"


def _fmt_rec(rec: Dict, now: float, full: bool) -> str:
    status = rec.get("status", "?")
    age = _fmt_age(now - rec.get("launched_at", now))
    task = (rec.get("task") or "").replace("\n", " ")[:80]
    head = f"- {rec.get('id', '?')} [{status}] \"{task}\" ({age}"
    if status == "running":
        return head + f", model {rec.get('model', '?')})"
    fin = _fmt_age(now - (rec.get("finished_at") or now))
    head += f", finished {fin} ago, model {rec.get('model', '?')})"
    if not full:
        return head
    body = (rec.get("result") or "").strip() or f"(error: {rec.get('error')})"
    return head + "\n  Report:\n" + body


def collect_status(agent_id: Optional[str] = None) -> str:
    """Status text for the check_agents tool. Finished-but-undelivered reports
    are returned in full and marked delivered (the parent has now seen them)."""
    _ensure_loaded()
    now = time.time()
    if agent_id:
        rec = _JOBS.get(agent_id)
        if not rec:
            return (f"No background agent with id '{agent_id}'. "
                    "Call check_agents with no arguments to list known agents.")
        full = rec.get("status") != "running" and not rec.get("delivered")
        text = _fmt_rec(rec, now, full=full)
        if full:
            rec["delivered"] = True
            rec["collected"] = True
            _save_registry()
        return text

    if not _JOBS:
        return "No background agents have been launched in this Odysseus instance."
    recs = sorted(_JOBS.values(), key=lambda r: r.get("launched_at", 0), reverse=True)
    lines = [f"Background agents ({len(recs)}):"]
    changed = False
    for r in recs:
        full = r.get("status") != "running" and not r.get("delivered")
        lines.append(_fmt_rec(r, now, full=full))
        if full:
            r["delivered"] = True
            r["collected"] = True
            changed = True
    if changed:
        _save_registry()
    return "\n".join(lines)
