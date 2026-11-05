# `routes/auth_routes.py` — definitions & call sites

49 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `LoginRequest` — class, line 46
- **called from:**
- `tests/test_auth_event_loop.py:109`
- `tests/test_auth_policy.py:266`
- `tests/test_auth_policy.py:281`
- `tests/test_auth_policy.py:298`
- `tests/test_auth_session_revocation.py:174`

## `SetupRequest` — class, line 53
- **called from:**
- `tests/test_auth_policy.py:154`
- `tests/test_auth_policy.py:201`
- `tests/test_auth_policy.py:212`
- `tests/test_auth_username_policy.py:35`

## `SignupRequest` — class, line 58
- **called from:**
- `tests/test_auth_policy.py:169`
- `tests/test_auth_username_policy.py:49`

## `ChangePasswordRequest` — class, line 63
- **called from:**
- `tests/test_auth_policy.py:188`
- `tests/test_auth_session_revocation.py:193`
- `tests/test_auth_session_revocation.py:212`

## `CreateUserRequest` — class, line 68
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DeleteUserRequest` — class, line 74
- **called from:**
- `tests/test_delete_user_invalidates_token_cache.py:56`
- `tests/test_delete_user_invalidates_token_cache.py:66`
- `tests/test_delete_user_invalidates_token_cache.py:76`

## `RenameUserRequest` — class, line 78
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SetAdminRequest` — class, line 82
- **called from:**
- `tests/test_set_admin.py:251`
- `tests/test_set_admin.py:268`
- `tests/test_set_admin.py:284`
- `tests/test_set_admin.py:299`
- `tests/test_set_admin.py:314`

## `ResetUserPasswordRequest` — class, line 86
- **called from:**
- `tests/test_auth_session_revocation.py:83`

## `SetOpenRegistrationRequest` — class, line 90
- **called from:**
- `tests/test_auth_regressions.py:129`
- `tests/test_auth_regressions.py:134`
- `tests/test_auth_regressions.py:149`
- `tests/test_auth_regressions.py:154`
- `tests/test_auth_regressions.py:168`

## `_secure_cookie` — function, line 96
- **called from:**
- `routes/auth_routes.py:213`

## `setup_auth_routes` — function, line 123
- **called from:**
- `app.py:718`
- `tests/test_admin_routes_auth_disabled.py:97`
- `tests/test_auth_event_loop.py:80`
- `tests/test_auth_policy.py:86`
- `tests/test_auth_policy.py:119`
- `tests/test_auth_policy.py:131`
- `tests/test_auth_policy.py:143`
- `tests/test_auth_policy.py:238`
- `tests/test_auth_regressions.py:103`
- `tests/test_auth_session_revocation.py:80`
- `tests/test_auth_session_revocation.py:143`
- `tests/test_auth_session_revocation.py:155`
- `tests/test_delete_user_invalidates_token_cache.py:54`
- `tests/test_delete_user_invalidates_token_cache.py:63`
- `tests/test_delete_user_invalidates_token_cache.py:73`
- `tests/test_email_account_default_serialization.py:411`
- `tests/test_integrations_store_shape.py:33`
- `tests/test_publication_plan_b.py:127`
- `tests/test_rename_user_owner_sync.py:70`
- `tests/test_rename_user_owner_sync.py:394`
- `tests/test_rename_user_owner_sync.py:654`
- `tests/test_rename_user_owner_sync.py:682`
- `tests/test_rename_user_owner_sync.py:745`
- `tests/test_rename_user_token_cache.py:47`
- `tests/test_retired_settings_interfaces.py:66`
- `tests/test_retired_settings_interfaces.py:135`
- `tests/test_retired_settings_interfaces.py:164`
- `tests/test_set_admin.py:221`

## `_get_current_user` — function, line 130
- **called from:**
- `routes/auth_routes.py:142`
- `routes/auth_routes.py:253`
- `routes/auth_routes.py:272`
- `routes/auth_routes.py:295`
- `routes/auth_routes.py:309`
- `routes/auth_routes.py:319`
- `routes/auth_routes.py:327`
- `routes/auth_routes.py:334`
- `routes/auth_routes.py:351`
- `routes/auth_routes.py:365`
- `routes/auth_routes.py:384`
- `routes/auth_routes.py:668`
- `routes/auth_routes.py:706`
- `routes/auth_routes.py:715`
- `routes/auth_routes.py:723`
- `routes/auth_routes.py:779`

## `_require_admin_user` — function, line 134
- **called from:**
- `routes/auth_routes.py:763`
- `routes/auth_routes.py:793`
- `routes/auth_routes.py:838`
- `routes/auth_routes.py:917`
- `routes/auth_routes.py:931`
- `routes/auth_routes.py:941`
- `routes/auth_routes.py:953`
- `routes/auth_routes.py:962`

## `first_run_setup` — function (async), line 150
- **route:** `POST /setup`
- decorator: `router.post("/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `signup` — function (async), line 169
- **route:** `POST /signup`
- decorator: `router.post("/signup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `login` — function (async), line 190
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

## `logout` — function (async), line 222
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

## `auth_status` — function (async), line 230
- **route:** `GET /status`
- decorator: `router.get("/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `auth_policy` — function (async), line 247
- **route:** `GET /policy`
- decorator: `router.get("/policy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `change_password` — function (async), line 252
- **route:** `POST /change-password`
- decorator: `router.post("/change-password")`
- **called from:**
- `tests/test_auth_session_revocation.py:113`
- `tests/test_auth_session_revocation.py:122`

## `totp_setup` — function (async), line 270
- **route:** `POST /2fa/setup`
- decorator: `router.post("/2fa/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TotpVerifyRequest` — class, line 289
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `totp_confirm` — function (async), line 293
- **route:** `POST /2fa/confirm`
- decorator: `router.post("/2fa/confirm")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TotpDisableRequest` — class, line 303
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `totp_disable` — function (async), line 307
- **route:** `POST /2fa/disable`
- decorator: `router.post("/2fa/disable")`
- **called from:**
- `routes/auth_routes.py:312`

## `totp_status` — function (async), line 317
- **route:** `GET /2fa/status`
- decorator: `router.get("/2fa/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_users` — function (async), line 326
- **route:** `GET /users`
- decorator: `router.get("/users")`
- **called from:**
- `routes/auth_routes.py:330`

## `admin_create_user` — function (async), line 333
- **route:** `POST /users`
- decorator: `router.post("/users")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reset_user_password` — function (async), line 350
- **route:** `PUT /users/{username}/password`
- decorator: `router.put("/users/{username}/password")`
- **called from:**
- `tests/test_auth_session_revocation.py:54`
- `tests/test_auth_session_revocation.py:55`
- `tests/test_auth_session_revocation.py:56`
- `tests/test_auth_session_revocation.py:58`

## `update_user_privileges` — function (async), line 364
- **route:** `PUT /users/{username}/privileges`
- decorator: `router.put("/users/{username}/privileges")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `rename_user` — function (async), line 383
- **route:** `PUT /users/{username}/rename`
- decorator: `router.put("/users/{username}/rename")`
- **called from:**
- `routes/auth_routes.py:405`
- `routes/auth_routes.py:414`
- `tests/test_auth_config_lock_concurrency.py:142`
- `tests/test_auth_config_lock_concurrency.py:177`
- `tests/test_auth_session_revocation.py:133`
- `tests/test_email_account_default_serialization.py:452`
- `tests/test_rename_user_case_insensitive.py:45`
- `tests/test_reserved_username_admin_escalation.py:64`

## `_rollback_auth_rename` — function, line 409
- **called from:**
- `routes/auth_routes.py:499`

## `set_user_admin` — function (async), line 661
- **route:** `PUT /users/{username}/admin`
- decorator: `router.put("/users/{username}/admin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_signup` — function (async), line 697
- **route:** `POST /signup-toggle`
- decorator: `router.post("/signup-toggle", deprecated=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_signup_enabled` — function (async), line 713
- **route:** `PUT /open-signup`
- decorator: `router.put("/open-signup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `admin_delete_user` — function (async), line 722
- **route:** `DELETE /users`
- decorator: `router.delete("/users")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_invalidate_api_token_cache` — function, line 727
- **called from:**
- `routes/auth_routes.py:741`
- `routes/auth_routes.py:750`

## `get_features` — function (async), line 756
- **route:** `GET /features`
- decorator: `router.get("/features")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_features` — function (async), line 761
- **route:** `POST /features`
- decorator: `router.post("/features")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_settings` — function (async), line 775
- **route:** `GET /settings`
- decorator: `router.get("/settings")`
- **called from:**
- `tests/test_retired_settings_interfaces.py:70`
- `tests/test_retired_settings_interfaces.py:71`
- `tests/test_retired_settings_interfaces.py:168`
- `tests/test_retired_settings_interfaces.py:172`
- `tests/test_retired_settings_interfaces.py:178`

## `set_settings` — function (async), line 791
- **route:** `POST /settings`
- decorator: `router.post("/settings")`
- **called from:**
- `tests/test_retired_settings_interfaces.py:77`
- `tests/test_retired_settings_interfaces.py:138`
- `tests/test_retired_settings_interfaces.py:144`
- `tests/test_retired_settings_interfaces.py:151`

## `extract_document_writing_style` — function (async), line 833
- **route:** `POST /settings/document-style/extract`
- decorator: `router.post("/settings/document-style/extract")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_integrations_route` — function (async), line 915
- **route:** `GET /integrations`
- decorator: `router.get("/integrations")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_presets` — function (async), line 924
- **route:** `GET /integrations/presets`
- decorator: `router.get("/integrations/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_integration` — function (async), line 929
- **route:** `POST /integrations`
- decorator: `router.post("/integrations")`
- **called from:**
- `tests/test_integrations_store_shape.py:62`
- `tests/test_integrations_store_shape.py:77`
- `tests/test_integrations_store_shape.py:98`
- `tests/test_integrations_store_shape.py:188`

## `update_integration_route` — function (async), line 939
- **route:** `PUT /integrations/{integration_id}`
- decorator: `router.put("/integrations/{integration_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_integration_route` — function (async), line 951
- **route:** `DELETE /integrations/{integration_id}`
- decorator: `router.delete("/integrations/{integration_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_integration_route` — function (async), line 960
- **route:** `POST /integrations/{integration_id}/test`
- decorator: `router.post("/integrations/{integration_id}/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
