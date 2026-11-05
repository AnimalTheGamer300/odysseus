# `src/tools/vault.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_vault_config` — function, line 15
- **called from:**
- `src/agent_runtime/owned_resources.py:119`
- `src/agent_runtime/owned_resources.py:138`
- `src/agent_runtime/owned_resources.py:149`
- `src/tools/vault.py:57`
- `src/tools/vault.py:109`

## `_run_bw` — function (async), line 27
- **called from:**
- `routes/vault/vault_routes.py:166`
- `routes/vault/vault_routes.py:182`
- `routes/vault/vault_routes.py:205`
- `routes/vault/vault_routes.py:229`
- `routes/vault/vault_routes.py:236`
- `src/tools/vault.py:62`
- `src/tools/vault.py:114`
- `src/tools/vault.py:166`
- `tests/test_vault_password_not_in_argv.py:74`
- `tests/test_vault_password_not_in_argv.py:86`

## `do_vault_search` — function (async), line 47
- **called from:**
- `src/tool_execution.py:2486`

## `do_vault_get` — function (async), line 96
- **called from:**
- `src/tool_execution.py:2489`

## `do_vault_unlock` — function (async), line 154
- **called from:**
- `src/tool_execution.py:2492`
