# `services/skills/prompts.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_skill_test_task` — function, line 5
- **called from:**
- `routes/skills_routes.py:104`
- `routes/skills_routes.py:621`
- `services/skills/prompts.py:21`
- `src/builtin_actions.py:2199`
- `tests/test_skill_audit_utility.py:16`
- `tests/test_skills_audit_services.py:81`
- `tests/test_skills_routes_nondict.py:22`
- `tests/test_skills_routes_nondict.py:23`

## `_skill_baseline_task` — function, line 19
- **called from:**
- `tests/test_skill_audit_utility.py:16`
- `tests/test_skills_audit_services.py:153`

## `_skill_test_messages` — function, line 24
- **called from:**
- `tests/test_skills_audit_services.py:97`
- `tests/test_skills_audit_services.py:120`
- `tests/test_skills_audit_services.py:122`
- `tests/test_skills_audit_services.py:123`
- `tests/test_skills_audit_services.py:135`
- `tests/test_skills_routes_nondict.py:31`

## `_skill_baseline_messages` — function, line 41
- **called from:**
- `tests/test_skills_audit_services.py:98`
- `tests/test_skills_audit_services.py:121`
- `tests/test_skills_audit_services.py:148`
