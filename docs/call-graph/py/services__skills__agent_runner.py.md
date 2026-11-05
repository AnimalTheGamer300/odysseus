# `services/skills/agent_runner.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SkillAuditUnavailable` — class, line 14
- **called from:**
- `services/skills/agent_runner.py:226`
- `services/skills/agent_runner.py:260`
- `tests/test_skill_audit_unavailable.py:33`

## `run_test_job` — function (async), line 18
- **called from:**
- `routes/skills_routes.py:169`
- `services/skills/job_coordinator.py:49`
- `services/skills/job_coordinator.py:110`
- `tests/test_skills_audit_services.py:239`

## `_flush_say` — function, line 49
- **called from:**
- `services/skills/agent_runner.py:77`
- `services/skills/agent_runner.py:83`
- `services/skills/agent_runner.py:105`
- `services/skills/agent_runner.py:124`
- `services/skills/agent_runner.py:126`

## `run_audit_arm` — function (async), line 194
- **called from:**
- `routes/skills_routes.py:215`
- `tests/test_skills_audit_services.py:211`

## `run_test_once` — function (async), line 264
- **called from:**
- `routes/skills_routes.py:220`
- `services/skills/audit_workflow.py:244`
- `services/skills/audit_workflow.py:280`
