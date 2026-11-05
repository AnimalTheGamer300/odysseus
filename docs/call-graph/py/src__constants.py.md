# `src/constants.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_build_version` — function, line 14
- **called from:**
- `src/constants.py:28`

## `_load_source_commit` — function, line 31
- **called from:**
- `src/constants.py:51`

## `internal_api_base` — function, line 186
- **called from:**
- `routes/task/task_routes.py:75`
- `routes/task/task_routes.py:100`
- `routes/task/task_routes.py:117`
- `src/builtin_actions.py:3552`
- `src/cookbook_serve_lifecycle.py:50`
- `src/cookbook_serve_lifecycle.py:97`
- `src/tools/_common.py:17`
- `tests/smoke/conftest.py:76`
- `tests/smoke/conftest.py:246`
- `tests/test_internal_api_base.py:15`
