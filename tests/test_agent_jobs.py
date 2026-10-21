"""Tests for background (fire-and-forget) sub-agents — src/agent_jobs.py.

Covers: registry persistence + interrupted-on-restart marking, the launch →
complete lifecycle, check_agents collection semantics (exactly-once delivery),
pruning, and the follow-up injection path (deliver / defer-when-busy /
skip-when-session-gone).
"""
import asyncio
import json
import time

import pytest

from src import agent_jobs as aj


def _rec(jid, status="done", delivered=False, finished_delta=None, result="R", **over):
    now = time.time()
    base = {
        "id": jid,
        "task": "do a thing",
        "model": "m",
        "status": status,
        "parent_session_id": "s1",
        "launched_at": now - 120,
        "finished_at": (now + finished_delta) if finished_delta is not None else now,
        "result": result,
        "rounds": 1,
        "truncated": False,
        "error": None,
        "delivered": delivered,
        "collected": False,
    }
    base.update(over)
    return base


@pytest.fixture(autouse=True)
def _clean_registry(tmp_path, monkeypatch):
    aj._reset_for_tests()
    monkeypatch.setattr(aj, "_JOB_FILE", tmp_path / "agent_jobs.json")
    yield
    aj._reset_for_tests()


# ---------------------------------------------------------------------------
# Registry persistence
# ---------------------------------------------------------------------------

def test_running_entry_marked_interrupted_on_load(tmp_path):
    f = tmp_path / "agent_jobs.json"
    f.write_text(json.dumps({"ag-deadbeef": _rec("ag-deadbeef", status="running",
                                                 finished_delta=None, result="")}),
                 encoding="utf-8")
    text = aj.collect_status()  # triggers load
    assert "ag-deadbeef" in text and "interrupted" in text
    rec = aj._JOBS["ag-deadbeef"]
    assert rec["status"] == "interrupted"
    assert "restarted" in rec["error"]
    assert "interrupted by an app restart" in rec["result"]


def test_registry_survives_roundtrip(tmp_path):
    aj._ensure_loaded()
    aj._JOBS["ag-aa"] = _rec("ag-aa", status="done", delivered=True, result="kept")
    aj._save_registry()
    aj._reset_for_tests()
    text = aj.collect_status()
    assert "ag-aa" in text
    # already delivered → report NOT re-delivered
    assert "kept" not in text


def test_prune_drops_old_delivered_keeps_fresh(tmp_path):
    aj._ensure_loaded()
    aj._JOBS["ag-old"] = _rec("ag-old", delivered=True, finished_delta=-(aj._RETENTION_S + 60))
    aj._JOBS["ag-new"] = _rec("ag-new", delivered=True, finished_delta=-10)
    aj._JOBS["ag-undelivered"] = _rec("ag-undelivered", delivered=False,
                                      finished_delta=-(aj._RETENTION_S * 10))
    aj._save_registry()
    assert "ag-old" not in aj._JOBS
    assert "ag-new" in aj._JOBS
    # undelivered results are precious — retention must not touch them
    assert "ag-undelivered" in aj._JOBS
    data = json.loads((tmp_path / "agent_jobs.json").read_text(encoding="utf-8"))
    assert set(data.keys()) == {"ag-new", "ag-undelivered"}


# ---------------------------------------------------------------------------
# Launch lifecycle
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_launch_completes_and_collects_once(monkeypatch):
    import src.agent_tools.spawn_agent_tools as sat

    async def fake_resolve(spec, owner, pe, pm, ph):
        return ("http://x/v1", "fake-model", {})

    async def fake_run_subagent(**kwargs):
        return {"model": "fake-model", "response": "THE_REPORT", "rounds": 3,
                "truncated": False}

    monkeypatch.setattr(sat, "_resolve_subagent_model", fake_resolve)
    monkeypatch.setattr(sat, "run_subagent", fake_run_subagent)

    rec = await aj.launch_background_agent(task="do a thing", parent_session_id="sess-1")
    assert not rec.get("error")
    jid = rec["id"]
    assert rec["status"] == "running"
    assert "launched" in rec["launch_message"]
    assert jid in aj._LIVE_TASKS  # strong ref held

    await aj._LIVE_TASKS[jid]
    assert aj._JOBS[jid]["status"] == "done"
    assert aj._JOBS[jid]["result"] == "THE_REPORT"
    assert aj._JOBS[jid]["delivered"] is False
    assert jid not in aj._LIVE_TASKS  # done callback cleaned up

    out = aj.collect_status()
    assert "THE_REPORT" in out
    # exactly-once: second listing must not repeat the report
    out2 = aj.collect_status()
    assert "THE_REPORT" not in out2
    assert aj._JOBS[jid]["delivered"] is True


@pytest.mark.asyncio
async def test_launch_bad_model_fails_fast(monkeypatch):
    import src.agent_tools.spawn_agent_tools as sat

    async def fake_resolve(spec, owner, pe, pm, ph):
        raise ValueError("Unknown model 'nope'")

    monkeypatch.setattr(sat, "_resolve_subagent_model", fake_resolve)
    rec = await aj.launch_background_agent(task="t")
    assert "nope" in rec.get("error", "")
    assert aj._JOBS == {}  # nothing registered, no dead job left behind


@pytest.mark.asyncio
async def test_launch_empty_task_rejected():
    rec = await aj.launch_background_agent(task="   ")
    assert "No task" in rec.get("error", "")


@pytest.mark.asyncio
async def test_worker_error_maps_to_failed(monkeypatch):
    import src.agent_tools.spawn_agent_tools as sat

    async def fake_resolve(spec, owner, pe, pm, ph):
        return ("http://x/v1", "m", {})

    async def fake_run(**kwargs):
        return {"error": "boom"}

    monkeypatch.setattr(sat, "_resolve_subagent_model", fake_resolve)
    monkeypatch.setattr(sat, "run_subagent", fake_run)
    rec = await aj.launch_background_agent(task="t")
    await aj._LIVE_TASKS[rec["id"]]
    assert aj._JOBS[rec["id"]]["status"] == "failed"
    out = aj.collect_status()
    assert "boom" in out


@pytest.mark.asyncio
async def test_worker_timeout_maps_to_timeout_status(monkeypatch):
    import src.agent_tools.spawn_agent_tools as sat

    async def fake_resolve(spec, owner, pe, pm, ph):
        return ("http://x/v1", "m", {})

    async def fake_run(**kwargs):
        return {"model": "m", "response": "partial", "rounds": 9, "truncated": True}

    monkeypatch.setattr(sat, "_resolve_subagent_model", fake_resolve)
    monkeypatch.setattr(sat, "run_subagent", fake_run)
    rec = await aj.launch_background_agent(task="t")
    await aj._LIVE_TASKS[rec["id"]]
    assert aj._JOBS[rec["id"]]["status"] == "timeout"


# ---------------------------------------------------------------------------
# Follow-up delivery (bg_monitor pattern)
# ---------------------------------------------------------------------------

class _FakeSess:
    id = "s1"
    model = "parent-model"
    endpoint_url = "http://x/v1"
    headers = {}
    owner = None

    def get_context_messages(self):
        return [{"role": "user", "content": "hi"}]


class _FakeSM:
    def __init__(self, sess=None):
        self._sess = sess
        self.saved = []

    def get_session(self, sid):
        return self._sess if sid == "s1" else None

    def add_message(self, sid, msg):
        self.saved.append((sid, msg))

    def save_sessions(self):
        pass


@pytest.mark.asyncio
async def test_followup_delivers_report(monkeypatch):
    aj._ensure_loaded()
    aj._JOBS["ag-abc"] = _rec("ag-abc", status="done", delivered=False, result="REPORT-R")
    fake_sm = _FakeSM(sess=_FakeSess())
    monkeypatch.setattr("src.ai_interaction.get_session_manager", lambda: fake_sm)

    async def fake_drain(sess, messages):
        inject = messages[-1]["content"]
        assert "ag-abc" in inject and "REPORT-R" in inject
        assert "Continue the original task" in inject
        return "Continued!", [{"round": 1, "tool": "bash"}]

    monkeypatch.setattr("src.bg_monitor._drain_agent", fake_drain)

    ok = await aj._run_followup(aj._JOBS["ag-abc"])
    assert ok is True
    # _run_followup does NOT set delivered — the monitor does after success
    assert aj._JOBS["ag-abc"]["delivered"] is False
    sid, msg = fake_sm.saved[0]
    assert sid == "s1"
    assert msg.content == "Continued!"
    assert msg.metadata["agent_job_id"] == "ag-abc"
    assert "REPORT-R" in msg.metadata["agent_result"]


@pytest.mark.asyncio
async def test_followup_empty_continuation_still_delivers_raw_report(monkeypatch):
    aj._ensure_loaded()
    aj._JOBS["ag-xyz"] = _rec("ag-xyz", status="done", delivered=False, result="RAW-R")
    fake_sm = _FakeSM(sess=_FakeSess())
    monkeypatch.setattr("src.ai_interaction.get_session_manager", lambda: fake_sm)

    async def fake_drain(sess, messages):
        return "", []

    monkeypatch.setattr("src.bg_monitor._drain_agent", fake_drain)
    ok = await aj._run_followup(aj._JOBS["ag-xyz"])
    assert ok is True
    _, msg = fake_sm.saved[0]
    assert "RAW-R" in msg.content  # user still sees the result


@pytest.mark.asyncio
async def test_followup_defers_when_session_busy(monkeypatch):
    aj._ensure_loaded()
    aj._JOBS["ag-busy"] = _rec("ag-busy", status="done", delivered=False)
    fake_sm = _FakeSM(sess=_FakeSess())
    monkeypatch.setattr("src.ai_interaction.get_session_manager", lambda: fake_sm)
    monkeypatch.setattr("src.agent_runs.is_active", lambda sid: True)
    ok = await aj._run_followup(aj._JOBS["ag-busy"])
    assert ok is False  # retry on next tick
    assert fake_sm.saved == []


@pytest.mark.asyncio
async def test_followup_skips_when_session_gone(monkeypatch):
    aj._ensure_loaded()
    aj._JOBS["ag-gone"] = _rec("ag-gone", status="done", delivered=False)
    fake_sm = _FakeSM(sess=None)
    monkeypatch.setattr("src.ai_interaction.get_session_manager", lambda: fake_sm)
    ok = await aj._run_followup(aj._JOBS["ag-gone"])
    assert ok is True  # considered handled — no infinite retry
    assert fake_sm.saved == []


@pytest.mark.asyncio
async def test_followup_no_session_manager_retries(monkeypatch):
    aj._ensure_loaded()
    aj._JOBS["ag-wait"] = _rec("ag-wait", status="done", delivered=False)
    monkeypatch.setattr("src.ai_interaction.get_session_manager", lambda: None)
    ok = await aj._run_followup(aj._JOBS["ag-wait"])
    assert ok is False


# ---------------------------------------------------------------------------
# check_agents collection API
# ---------------------------------------------------------------------------

def test_collect_status_lists_running_and_finished():
    aj._ensure_loaded()
    aj._JOBS["ag-run"] = _rec("ag-run", status="running", finished_delta=None)
    aj._JOBS["ag-fin"] = _rec("ag-fin", status="done", delivered=False, result="FIN-R")
    text = aj.collect_status()
    assert "ag-run" in text and "running" in text
    assert "FIN-R" in text
    assert aj._JOBS["ag-fin"]["delivered"] is True


def test_collect_status_unknown_id():
    aj._ensure_loaded()
    text = aj.collect_status("ag-nope")
    assert "No background agent" in text


def test_collect_status_specific_id():
    aj._ensure_loaded()
    aj._JOBS["ag-one"] = _rec("ag-one", status="done", delivered=False, result="ONE-R")
    text = aj.collect_status("ag-one")
    assert "ONE-R" in text
    assert aj._JOBS["ag-one"]["delivered"] is True


def test_collect_status_empty_registry():
    aj._ensure_loaded()
    assert "No background agents" in aj.collect_status()
