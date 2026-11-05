# `src/builtin_mcp.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_find_npx` — function, line 22
- **called from:**
- `src/builtin_mcp.py:201`

## `_spawn_bg` — function, line 100
- **called from:**
- `routes/chat_helpers.py:2174`
- `routes/chat_helpers.py:2189`
- `src/builtin_mcp.py:198`
- `src/builtin_mcp.py:256`
- `tests/test_builtin_mcp_bg_tasks.py:57`

## `_find_browser_executable` — function, line 107
- **called from:**
- `src/builtin_mcp.py:136`

## `_browser_mcp_args` — function, line 132
- **called from:**
- `src/builtin_mcp.py:211`
- `tests/test_builtin_mcp_npx_cache.py:57`
- `tests/test_builtin_mcp_npx_cache.py:70`
- `tests/test_builtin_mcp_npx_cache.py:80`
- `tests/test_builtin_mcp_npx_cache.py:93`

## `builtin_python_env` — function, line 148
- **called from:**
- `src/builtin_mcp.py:180`
- `src/mcp_manager.py:689`
- `tests/test_builtin_mcp_pythonpath.py:12`
- `tests/test_builtin_mcp_pythonpath.py:22`

## `register_builtin_servers` — function (async), line 163
- **called from:**
- `app.py:1251`
- `scripts/dump_agent_prompt.py:406`

## `_connect_python_server` — function (async), line 172
- **called from:**
- `src/builtin_mcp.py:198`

## `_start_npx_servers` — function (async), line 204
- **called from:**
- `src/builtin_mcp.py:256`

## `_npx_package_from_args` — function, line 259
- **called from:**
- `src/builtin_mcp.py:212`
- `tests/test_builtin_mcp_npx_cache.py:34`

## `_is_npx_package_cached` — function (async), line 277
- **called from:**
- `src/builtin_mcp.py:213`
- `tests/test_builtin_mcp_bg_tasks.py:98`
- `tests/test_builtin_mcp_npx_cache.py:122`
- `tests/test_builtin_mcp_npx_cache.py:149`
- `tests/test_builtin_mcp_npx_cache.py:180`

## `_is_package_in_npx_cache` — function, line 326
- **called from:**
- `src/builtin_mcp.py:284`

## `_npx_package_name` — function, line 339
- **called from:**
- `src/builtin_mcp.py:328`

## `_npm_cache_roots` — function, line 351
- **called from:**
- `src/builtin_mcp.py:332`

## `_npx_cache_contains_package` — function, line 363
- **called from:**
- `src/builtin_mcp.py:334`

## `_cached_package_name` — function, line 382
- **called from:**
- `src/builtin_mcp.py:376`
