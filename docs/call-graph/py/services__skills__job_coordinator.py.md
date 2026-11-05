# `services/skills/job_coordinator.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `start_test_job` — function, line 16
- **called from:**
- `routes/skills_routes.py:654`

## `continue_test_job` — function, line 55
- **called from:**
- `routes/skills_routes.py:712`

## `test_status` — function, line 127
- **called from:**
- `routes/skills_routes.py:724`

## `select_audit_names` — function, line 141
- **called from:**
- `routes/skills_routes.py:757`
- `tests/test_skills_audit_services.py:402`

## `start_audit_job` — function, line 177
- **called from:**
- `routes/skills_routes.py:760`

## `audit_status` — function, line 194
- **called from:**
- `routes/skills_routes.py:768`

## `cancel_audit` — function, line 207
- **called from:**
- `routes/skills_routes.py:773`
