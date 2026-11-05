# `src/task_action_policy.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `is_admin_only_task_action` — function, line 13
- **called from:**
- `routes/task/task_routes.py:443`
- `routes/task/task_routes.py:1130`
- `src/task_scheduler.py:987`
- `src/tools/system.py:343`

## `owner_has_admin_task_privileges` — function, line 17
- **called from:**
- `routes/task/task_routes.py:440`
- `routes/task/task_routes.py:1131`
- `src/task_scheduler.py:988`
- `src/tools/system.py:343`
- `tests/test_manage_tasks_admin_action_policy.py:271`
- `tests/test_manage_tasks_admin_action_policy.py:272`
- `tests/test_manage_tasks_admin_action_policy.py:286`
- `tests/test_manage_tasks_admin_action_policy.py:287`
- `tests/test_manage_tasks_admin_action_policy.py:288`
- `tests/test_manage_tasks_admin_action_policy.py:289`
