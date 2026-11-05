# `routes/vault/vault_routes.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_find_bw` — function, line 28
- **called from:**
- `routes/vault/vault_routes.py:106`
- `routes/vault/vault_routes.py:250`

## `_load_config` — function, line 63
- **called from:**
- `mcp_servers/email_server.py:174`
- `mcp_servers/email_server.py:409`
- `mcp_servers/email_server.py:959`
- `mcp_servers/email_server.py:2047`
- `mcp_servers/email_server.py:2412`
- `mcp_servers/email_server.py:2508`
- `mcp_servers/email_server.py:2515`
- `mcp_servers/email_server.py:2523`
- `mcp_servers/email_server.py:2673`
- `mcp_servers/email_server.py:2815`
- `mcp_servers/email_server.py:2815`
- `mcp_servers/email_server.py:2999`
- `mcp_servers/email_server.py:3408`
- `mcp_servers/email_server.py:3418`
- `mcp_servers/email_server.py:3491`
- `mcp_servers/email_server.py:3573`
- `mcp_servers/email_server.py:4133`
- `mcp_servers/email_server.py:4153`
- `mcp_servers/email_server.py:4633`
- `mcp_servers/email_server.py:4637`
- `mcp_servers/email_server.py:4647`
- `routes/vault/vault_routes.py:147`
- `routes/vault/vault_routes.py:160`
- `routes/vault/vault_routes.py:177`
- `routes/vault/vault_routes.py:214`
- `routes/vault/vault_routes.py:224`
- `routes/vault/vault_routes.py:237`
- `tests/test_mcp_email_decode_header_spaces.py:188`
- `tests/test_vault_password_not_in_argv.py:117`

## `_save_config` — function, line 73
- **called from:**
- `routes/vault/vault_routes.py:170`
- `routes/vault/vault_routes.py:180`
- `routes/vault/vault_routes.py:195`
- `routes/vault/vault_routes.py:217`
- `routes/vault/vault_routes.py:227`
- `routes/vault/vault_routes.py:241`

## `_bind_config_owner` — function, line 81
- **called from:**
- `routes/vault/vault_routes.py:161`
- `tests/test_owned_resource_identity.py:335`
- `tests/test_owned_resource_identity.py:339`

## `_run_bw` — function (async), line 94
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

## `VaultConfig` — class, line 126
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VaultUnlockRequest` — class, line 131
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `VaultLoginRequest` — class, line 135
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_vault_routes` — function, line 140
- **called from:**
- `app.py:965`

## `get_config` — function (async), line 144
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `save_config` — function (async), line 157
- **route:** `POST /config`
- decorator: `router.post("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `login` — function (async), line 174
- **route:** `POST /login`
- decorator: `router.post("/login")`
- **called from:**
- `mcp_servers/email_server.py:435`
- `mcp_servers/email_server.py:2560`
- `routes/email/email_helpers.py:270`
- `routes/email/email_helpers.py:1384`
- `routes/email/email_routes.py:7637`
- `routes/email/email_routes.py:7701`
- `scripts/demo_email/seed_demo_emails.py:60`
- `scripts/diffusion_server.py:365`
- `scripts/run_sft_environment_expansion.py:696`
- `scripts/run_sft_environment_expansion.py:733`
- `scripts/run_sft_overnight_fixture_flows.py:774`
- `scripts/sft_email_overseer.py:651`
- `tests/test_auth_event_loop.py:111`

## `unlock` — function (async), line 199
- **route:** `POST /unlock`
- decorator: `router.post("/unlock")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `lock` — function (async), line 221
- **route:** `POST /lock`
- decorator: `router.post("/lock")`
- **called from:**
- `src/agent_tools/web_tools_prewave3.py:2650`

## `logout` — function (async), line 233
- **route:** `POST /logout`
- decorator: `router.post("/logout")`
- **called from:**
- `mcp_servers/email_server.py:794`
- `mcp_servers/email_server.py:870`
- `mcp_servers/email_server.py:1893`
- `mcp_servers/email_server.py:2340`
- `mcp_servers/email_server.py:2463`
- `mcp_servers/email_server.py:2724`
- `mcp_servers/email_server.py:2980`
- `mcp_servers/email_server.py:3149`
- `mcp_servers/email_server.py:3212`
- `mcp_servers/email_server.py:3256`
- `mcp_servers/email_server.py:3340`
- `mcp_servers/email_server.py:3368`
- `mcp_servers/email_server.py:3398`
- `mcp_servers/email_server.py:3566`
- `routes/email/email_helpers.py:1451`
- `routes/email/email_helpers.py:1594`
- `routes/email/email_helpers.py:1926`
- `routes/email/email_helpers.py:2071`
- `routes/email/email_pollers.py:559`
- `routes/email/email_pollers.py:1565`
- `routes/email/email_routes.py:1780`
- `routes/email/email_routes.py:1784`
- `routes/email/email_routes.py:1794`
- `routes/email/email_routes.py:1817`
- `routes/email/email_routes.py:7640`
- `scripts/demo_email/seed_demo_emails.py:388`
- `src/builtin_actions.py:1429`
- `src/builtin_actions.py:1801`
- `src/builtin_actions.py:1879`
- `src/builtin_actions.py:2064`
- `src/builtin_actions.py:2942`
- `src/service_health.py:343`
- `tests/test_codeql_python_residual_closure.py:204`
- `tests/test_codeql_python_residual_closure.py:268`

## `_check_bw_installed` — function (async), line 247
- **called from:**
- `routes/vault/vault_routes.py:153`
