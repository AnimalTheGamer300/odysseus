# `src/runtime_paths.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `get_app_root` — function, line 7
- **called from:**
- `core/database.py:66`
- `src/builtin_mcp.py:169`
- `src/config.py:23`
- `src/config.py:141`
- `src/constants.py:9`
- `src/constants.py:19`
- `src/constants.py:39`
- `src/constants.py:54`
- `src/mcp_manager.py:676`
- `src/runtime_paths.py:30`
- `tests/test_runtime_paths.py:11`
- `tests/test_runtime_paths.py:22`
- `tests/test_runtime_paths.py:34`
- `tests/test_runtime_paths.py:42`

## `get_default_data_dir` — function, line 20
- **called from:**
- `src/constants.py:56`
- `tests/test_runtime_paths.py:41`
- `tests/test_runtime_paths.py:48`
