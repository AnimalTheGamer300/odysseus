# `src/task_action_policy.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `is_admin_only_task_action` — function, line 13
- **called from:**
- `routes/task/task_routes.py:434`
- `routes/task/task_routes.py:1058`
- `src/task_scheduler.py:841`

## `owner_has_admin_task_privileges` — function, line 17
- **called from:**
- `routes/task/task_routes.py:431`
- `routes/task/task_routes.py:1059`
- `src/task_scheduler.py:842`
