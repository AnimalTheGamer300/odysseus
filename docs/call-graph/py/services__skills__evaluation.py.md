# `services/skills/evaluation.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `verdict_efficiency` — function, line 23
- **called from:**
- `services/skills/agent_runner.py:181`
- `services/skills/audit_workflow.py:217`
- `services/skills/audit_workflow.py:230`
- `services/skills/audit_workflow.py:257`
- `services/skills/audit_workflow.py:294`
- `services/skills/audit_workflow.py:311`

## `parse_run_verdict` — function, line 45
- **called from:**
- `services/skills/evaluation.py:243`

## `_coerce` — function, line 58
- **called from:**
- `services/skills/evaluation.py:69`
- `services/skills/evaluation.py:82`
- `src/agent_tools/admin_tools.py:690`

## `evaluate_run` — function (async), line 132
- **called from:**
- `routes/skills_routes.py:119`
- `services/skills/agent_runner.py:154`
- `services/skills/agent_runner.py:297`
- `services/skills/audit_workflow.py:161`
- `tests/test_skills_audit_services.py:164`

## `_clip` — function, line 193
- **called from:**
- `services/skills/evaluation.py:207`
- `services/skills/evaluation.py:211`

## `evaluate_necessity` — function (async), line 253
- **called from:**
- `routes/skills_routes.py:128`
- `services/skills/audit_workflow.py:66`

## `should_check_retrieval_precision` — function, line 318
- **called from:**
- `services/skills/audit_workflow.py:82`

## `evaluate_retrieval_precision` — function (async), line 342
- **called from:**
- `routes/skills_routes.py:141`
- `services/skills/audit_workflow.py:83`

## `improve_markdown` — function (async), line 413
- **called from:**
- `routes/skills_routes.py:227`
- `services/skills/audit_workflow.py:90`
- `services/skills/audit_workflow.py:204`
- `services/skills/audit_workflow.py:238`
- `services/skills/audit_workflow.py:273`
- `tests/test_skills_audit_services.py:174`
