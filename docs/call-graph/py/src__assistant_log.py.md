# `src/assistant_log.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_session_manager` — function, line 22
- **called from:**
- `src/app_initializer.py:93`

## `log_to_assistant` — function, line 34
- **called from:**
- `routes/cookbook_routes.py:1270`
- `routes/cookbook_routes.py:2699`
- `src/task_scheduler.py:1369`
- `src/tools/vault.py:130`
