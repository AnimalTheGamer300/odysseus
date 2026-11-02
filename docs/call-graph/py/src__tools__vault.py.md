# `src/tools/vault.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_vault_config` — function, line 15
- **called from:**
- `src/tools/vault.py:57`
- `src/tools/vault.py:105`

## `_run_bw` — function (async), line 27
- **called from:**
- `routes/vault/vault_routes.py:151`
- `routes/vault/vault_routes.py:167`
- `routes/vault/vault_routes.py:190`
- `routes/vault/vault_routes.py:214`
- `routes/vault/vault_routes.py:221`
- `src/tools/vault.py:62`
- `src/tools/vault.py:110`
- `src/tools/vault.py:162`
- `tests/test_vault_password_not_in_argv.py:74`
- `tests/test_vault_password_not_in_argv.py:86`

## `do_vault_search` — function (async), line 47
- **called from:**
- `src/tool_execution.py:1302`

## `do_vault_get` — function (async), line 92
- **called from:**
- `src/tool_execution.py:1305`

## `do_vault_unlock` — function (async), line 150
- **called from:**
- `src/tool_execution.py:1308`
