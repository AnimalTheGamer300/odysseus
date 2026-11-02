# `routes/auth_routes.py` — definitions & call sites

45 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `LoginRequest` — class, line 43
- **called from:**
- `tests/test_auth_event_loop.py:109`
- `tests/test_auth_policy.py:266`
- `tests/test_auth_policy.py:281`
- `tests/test_auth_policy.py:298`
- `tests/test_auth_session_revocation.py:129`

## `SetupRequest` — class, line 50
- **called from:**
- `tests/test_auth_policy.py:154`
- `tests/test_auth_policy.py:201`
- `tests/test_auth_policy.py:212`

## `SignupRequest` — class, line 55
- **called from:**
- `tests/test_auth_policy.py:169`

## `ChangePasswordRequest` — class, line 60
- **called from:**
- `tests/test_auth_policy.py:188`
- `tests/test_auth_session_revocation.py:148`
- `tests/test_auth_session_revocation.py:167`

## `CreateUserRequest` — class, line 65
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DeleteUserRequest` — class, line 71
- **called from:**
- `tests/test_delete_user_invalidates_token_cache.py:54`
- `tests/test_delete_user_invalidates_token_cache.py:64`
- `tests/test_delete_user_invalidates_token_cache.py:77`

## `RenameUserRequest` — class, line 75
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SetAdminRequest` — class, line 79
- **called from:**
- `tests/test_set_admin.py:251`
- `tests/test_set_admin.py:268`
- `tests/test_set_admin.py:284`
- `tests/test_set_admin.py:299`
- `tests/test_set_admin.py:314`

## `SetOpenRegistrationRequest` — class, line 83
- **called from:**
- `tests/test_auth_regressions.py:127`
- `tests/test_auth_regressions.py:132`
- `tests/test_auth_regressions.py:147`
- `tests/test_auth_regressions.py:152`
- `tests/test_auth_regressions.py:166`

## `_secure_cookie` — function, line 89
- **called from:**
- `routes/auth_routes.py:189`

## `setup_auth_routes` — function, line 116
- **called from:**
- `app.py:640`
- `tests/test_auth_event_loop.py:80`
- `tests/test_auth_policy.py:86`
- `tests/test_auth_policy.py:119`
- `tests/test_auth_policy.py:131`
- `tests/test_auth_policy.py:143`
- `tests/test_auth_policy.py:238`
- `tests/test_auth_regressions.py:101`
- `tests/test_auth_session_revocation.py:98`
- `tests/test_auth_session_revocation.py:110`
- `tests/test_delete_user_invalidates_token_cache.py:52`
- `tests/test_delete_user_invalidates_token_cache.py:61`
- `tests/test_delete_user_invalidates_token_cache.py:74`
- `tests/test_email_account_default_serialization.py:411`
- `tests/test_integrations_store_shape.py:33`
- `tests/test_rename_user_owner_sync.py:70`
- `tests/test_rename_user_owner_sync.py:394`
- `tests/test_rename_user_owner_sync.py:654`
- `tests/test_rename_user_owner_sync.py:682`
- `tests/test_rename_user_owner_sync.py:745`
- `tests/test_rename_user_token_cache.py:47`
- `tests/test_retired_settings_interfaces.py:65`
- `tests/test_set_admin.py:221`

## `_get_current_user` — function, line 123
- **called from:**
- `routes/auth_routes.py:229`
- `routes/auth_routes.py:248`
- `routes/auth_routes.py:271`
- `routes/auth_routes.py:285`
- `routes/auth_routes.py:295`
- `routes/auth_routes.py:303`
- `routes/auth_routes.py:310`
- `routes/auth_routes.py:326`
- `routes/auth_routes.py:337`
- `routes/auth_routes.py:618`
- `routes/auth_routes.py:645`
- `routes/auth_routes.py:654`
- `routes/auth_routes.py:662`
- `routes/auth_routes.py:702`
- `routes/auth_routes.py:720`
- `routes/auth_routes.py:729`
- `routes/auth_routes.py:765`
- `routes/auth_routes.py:781`
- `routes/auth_routes.py:791`
- `routes/auth_routes.py:803`
- `routes/auth_routes.py:814`

## `first_run_setup` — function (async), line 128
- **route:** `POST /setup`
- decorator: `router.post("/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `signup` — function (async), line 146
- **route:** `POST /signup`
- decorator: `router.post("/signup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `login` — function (async), line 166
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

## `logout` — function (async), line 198
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

## `auth_status` — function (async), line 206
- **route:** `GET /status`
- decorator: `router.get("/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `auth_policy` — function (async), line 223
- **route:** `GET /policy`
- decorator: `router.get("/policy")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `change_password` — function (async), line 228
- **route:** `POST /change-password`
- decorator: `router.post("/change-password")`
- **called from:**
- `tests/test_auth_session_revocation.py:68`
- `tests/test_auth_session_revocation.py:77`

## `totp_setup` — function (async), line 246
- **route:** `POST /2fa/setup`
- decorator: `router.post("/2fa/setup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TotpVerifyRequest` — class, line 265
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `totp_confirm` — function (async), line 269
- **route:** `POST /2fa/confirm`
- decorator: `router.post("/2fa/confirm")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TotpDisableRequest` — class, line 279
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `totp_disable` — function (async), line 283
- **route:** `POST /2fa/disable`
- decorator: `router.post("/2fa/disable")`
- **called from:**
- `routes/auth_routes.py:288`

## `totp_status` — function (async), line 293
- **route:** `GET /2fa/status`
- decorator: `router.get("/2fa/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_users` — function (async), line 302
- **route:** `GET /users`
- decorator: `router.get("/users")`
- **called from:**
- `routes/auth_routes.py:306`

## `admin_create_user` — function (async), line 309
- **route:** `POST /users`
- decorator: `router.post("/users")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_user_privileges` — function (async), line 325
- **route:** `PUT /users/{username}/privileges`
- decorator: `router.put("/users/{username}/privileges")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `rename_user` — function (async), line 336
- **route:** `PUT /users/{username}/rename`
- decorator: `router.put("/users/{username}/rename")`
- **called from:**
- `routes/auth_routes.py:355`
- `routes/auth_routes.py:364`
- `tests/test_auth_config_lock_concurrency.py:142`
- `tests/test_auth_config_lock_concurrency.py:177`
- `tests/test_auth_session_revocation.py:88`
- `tests/test_email_account_default_serialization.py:452`
- `tests/test_rename_user_case_insensitive.py:45`
- `tests/test_reserved_username_admin_escalation.py:64`

## `_rollback_auth_rename` — function, line 359
- **called from:**
- `routes/auth_routes.py:449`

## `set_user_admin` — function (async), line 611
- **route:** `PUT /users/{username}/admin`
- decorator: `router.put("/users/{username}/admin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_signup` — function (async), line 636
- **route:** `POST /signup-toggle`
- decorator: `router.post("/signup-toggle", deprecated=True)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_signup_enabled` — function (async), line 652
- **route:** `PUT /open-signup`
- decorator: `router.put("/open-signup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `admin_delete_user` — function (async), line 661
- **route:** `DELETE /users`
- decorator: `router.delete("/users")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_invalidate_api_token_cache` — function, line 666
- **called from:**
- `routes/auth_routes.py:680`
- `routes/auth_routes.py:689`

## `get_features` — function (async), line 695
- **route:** `GET /features`
- decorator: `router.get("/features")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_features` — function (async), line 700
- **route:** `POST /features`
- decorator: `router.post("/features")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_settings` — function (async), line 716
- **route:** `GET /settings`
- decorator: `router.get("/settings")`
- **called from:**
- `tests/test_retired_settings_interfaces.py:69`
- `tests/test_retired_settings_interfaces.py:70`

## `set_settings` — function (async), line 727
- **route:** `POST /settings`
- decorator: `router.post("/settings")`
- **called from:**
- `tests/test_retired_settings_interfaces.py:76`

## `list_integrations_route` — function (async), line 763
- **route:** `GET /integrations`
- decorator: `router.get("/integrations")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_presets` — function (async), line 774
- **route:** `GET /integrations/presets`
- decorator: `router.get("/integrations/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_integration` — function (async), line 779
- **route:** `POST /integrations`
- decorator: `router.post("/integrations")`
- **called from:**
- `tests/test_integrations_store_shape.py:62`
- `tests/test_integrations_store_shape.py:77`
- `tests/test_integrations_store_shape.py:98`

## `update_integration_route` — function (async), line 789
- **route:** `PUT /integrations/{integration_id}`
- decorator: `router.put("/integrations/{integration_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_integration_route` — function (async), line 801
- **route:** `DELETE /integrations/{integration_id}`
- decorator: `router.delete("/integrations/{integration_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_integration_route` — function (async), line 812
- **route:** `POST /integrations/{integration_id}/test`
- decorator: `router.post("/integrations/{integration_id}/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
