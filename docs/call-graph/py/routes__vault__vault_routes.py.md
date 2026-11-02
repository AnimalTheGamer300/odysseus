# `routes/vault/vault_routes.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_find_bw` — function, line 27
- **called from:**
- `routes/vault/vault_routes.py:92`
- `routes/vault/vault_routes.py:235`

## `_load_config` — function, line 62
- **called from:**
- `mcp_servers/email_server.py:147`
- `mcp_servers/email_server.py:379`
- `mcp_servers/email_server.py:806`
- `mcp_servers/email_server.py:1224`
- `mcp_servers/email_server.py:1317`
- `mcp_servers/email_server.py:1324`
- `mcp_servers/email_server.py:1332`
- `mcp_servers/email_server.py:1482`
- `mcp_servers/email_server.py:1624`
- `mcp_servers/email_server.py:1624`
- `mcp_servers/email_server.py:1752`
- `mcp_servers/email_server.py:2049`
- `mcp_servers/email_server.py:2057`
- `mcp_servers/email_server.py:2517`
- `mcp_servers/email_server.py:2524`
- `mcp_servers/email_server.py:2867`
- `mcp_servers/email_server.py:2871`
- `mcp_servers/email_server.py:2881`
- `routes/vault/vault_routes.py:133`
- `routes/vault/vault_routes.py:146`
- `routes/vault/vault_routes.py:162`
- `routes/vault/vault_routes.py:199`
- `routes/vault/vault_routes.py:209`
- `routes/vault/vault_routes.py:222`
- `tests/test_mcp_email_decode_header_spaces.py:175`
- `tests/test_vault_password_not_in_argv.py:117`

## `_save_config` — function, line 72
- **called from:**
- `routes/vault/vault_routes.py:155`
- `routes/vault/vault_routes.py:165`
- `routes/vault/vault_routes.py:180`
- `routes/vault/vault_routes.py:202`
- `routes/vault/vault_routes.py:212`
- `routes/vault/vault_routes.py:226`

## `_run_bw` — function (async), line 80
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

## `VaultConfig` — class, line 112
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VaultUnlockRequest` — class, line 117
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VaultLoginRequest` — class, line 121
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_vault_routes` — function, line 126
- **called from:**
- `app.py:880`

## `get_config` — function (async), line 130
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `save_config` — function (async), line 143
- **route:** `POST /config`
- decorator: `router.post("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `login` — function (async), line 159
- **route:** `POST /login`
- decorator: `router.post("/login")`
- **called from:**
- `mcp_servers/email_server.py:405`
- `mcp_servers/email_server.py:1369`
- `routes/email_helpers.py:178`
- `routes/email_helpers.py:1237`
- `routes/email_routes.py:5903`
- `routes/email_routes.py:5966`
- `scripts/demo_email/seed_demo_emails.py:60`
- `scripts/diffusion_server.py:365`
- `tests/test_auth_event_loop.py:111`

## `unlock` — function (async), line 184
- **route:** `POST /unlock`
- decorator: `router.post("/unlock")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `lock` — function (async), line 206
- **route:** `POST /lock`
- decorator: `router.post("/lock")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `logout` — function (async), line 218
- **route:** `POST /logout`
- decorator: `router.post("/logout")`
- **called from:**
- `mcp_servers/email_server.py:682`
- `mcp_servers/email_server.py:727`
- `mcp_servers/email_server.py:1042`
- `mcp_servers/email_server.py:1152`
- `mcp_servers/email_server.py:1272`
- `mcp_servers/email_server.py:1533`
- `mcp_servers/email_server.py:1733`
- `mcp_servers/email_server.py:1885`
- `mcp_servers/email_server.py:1936`
- `mcp_servers/email_server.py:1964`
- `mcp_servers/email_server.py:1998`
- `mcp_servers/email_server.py:2013`
- `mcp_servers/email_server.py:2043`
- `mcp_servers/email_server.py:2070`
- `routes/email_helpers.py:1304`
- `routes/email_helpers.py:1447`
- `routes/email_helpers.py:1777`
- `routes/email_helpers.py:1922`
- `routes/email_pollers.py:444`
- `routes/email_pollers.py:1365`
- `routes/email_routes.py:1571`
- `routes/email_routes.py:1575`
- `routes/email_routes.py:1585`
- `routes/email_routes.py:5906`
- `scripts/demo_email/seed_demo_emails.py:388`
- `src/builtin_actions.py:1266`
- `src/builtin_actions.py:1626`
- `src/builtin_actions.py:1700`
- `src/builtin_actions.py:1853`
- `src/builtin_actions.py:2678`
- `src/service_health.py:329`

## `_check_bw_installed` — function (async), line 232
- **called from:**
- `routes/vault/vault_routes.py:139`
