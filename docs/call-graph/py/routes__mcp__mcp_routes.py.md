# `routes/mcp/mcp_routes.py` — definitions & call sites

23 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_mcp_oauth_base_dir` — function, line 25
- **called from:**
- `routes/mcp/mcp_routes.py:36`

## `_resolve_mcp_oauth_path` — function, line 30
- **called from:**
- `routes/mcp/mcp_routes.py:61`
- `routes/mcp/mcp_routes.py:73`
- `routes/mcp/mcp_routes.py:230`
- `routes/mcp/mcp_routes.py:235`
- `tests/test_security_regressions.py:1062`
- `tests/test_security_regressions.py:1080`
- `tests/test_security_regressions.py:1090`
- `tests/test_security_regressions.py:1092`

## `_sanitize_mcp_oauth_config` — function, line 52
- **called from:**
- `routes/mcp/mcp_routes.py:220`
- `routes/mcp/mcp_routes.py:465`
- `routes/mcp/mcp_routes.py:580`
- `tests/test_security_regressions.py:1099`

## `_mcp_oauth_token_missing` — function, line 68
- **called from:**
- `routes/mcp/mcp_routes.py:146`
- `routes/mcp/mcp_routes.py:279`

## `_apply_mcp_oauth_env` — function, line 82
- **called from:**
- `routes/mcp/mcp_routes.py:223`
- `tests/test_security_regressions.py:1106`

## `_load_disabled_map` — function, line 94
- **called from:**
- `routes/mcp/mcp_routes.py:398`

## `_mcp_oauth_redirect_uri` — function, line 112
- **called from:**
- `routes/mcp/mcp_routes.py:481`
- `routes/mcp/mcp_routes.py:592`
- `tests/test_security_regressions.py:1053`

## `_is_legacy_google_flow` — function, line 118
- **called from:**
- `routes/mcp/mcp_routes.py:525`
- `routes/mcp/mcp_routes.py:562`

## `setup_mcp_routes` — function, line 130
- **called from:**
- `app.py:920`
- `tests/test_admin_listing_authorization.py:79`
- `tests/test_manage_settings_denylist_hard.py:201`
- `tests/test_mcp_add_server_args_validation.py:51`
- `tests/test_mcp_oauth.py:305`
- `tests/test_mcp_oauth.py:336`
- `tests/test_mcp_oauth.py:393`
- `tests/test_mcp_oauth.py:438`
- `tests/test_mcp_oauth.py:465`
- `tests/test_mcp_oauth.py:486`

## `list_servers` — function, line 134
- **route:** `GET /servers`
- decorator: `router.get("/servers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_server` — function (async), line 172
- **route:** `POST /servers`
- decorator: `router.post("/servers")`
- **called from:**
- `tests/test_mcp_add_server_args_validation.py:65`
- `tests/test_mcp_add_server_args_validation.py:86`
- `tests/test_mcp_add_server_args_validation.py:113`
- `tests/test_mcp_add_server_args_validation.py:135`

## `reconnect_server` — function (async), line 308
- **route:** `POST /servers/{server_id}/reconnect`
- decorator: `router.post("/servers/{server_id}/reconnect")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_server` — function (async), line 344
- **route:** `PATCH /servers/{server_id}`
- decorator: `router.patch("/servers/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_server` — function (async), line 377
- **route:** `DELETE /servers/{server_id}`
- decorator: `router.delete("/servers/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_tools` — function, line 395
- **route:** `GET /tools`
- decorator: `router.get("/tools")`
- **called from:**
- `mcp_servers/email_server.py:3586`
- `mcp_servers/image_gen_server.py:24`
- `mcp_servers/memory_server.py:115`
- `mcp_servers/rag_server.py:46`
- `src/mcp_manager.py:233`
- `src/mcp_manager.py:303`
- `src/mcp_manager.py:393`
- `tests/test_clean_agent_preview.py:4319`
- `tests/test_generate_image_native_schema.py:56`

## `list_server_tools` — function, line 402
- **route:** `GET /servers/{server_id}/tools`
- decorator: `router.get("/servers/{server_id}/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_disabled_tools` — function (async), line 422
- **route:** `PATCH /servers/{server_id}/tools`
- decorator: `router.patch("/servers/{server_id}/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_authorize` — function, line 454
- **route:** `GET /oauth/authorize/{server_id}`
- decorator: `router.get("/oauth/authorize/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_callback` — function (async), line 508
- **route:** `GET /oauth/callback`
- decorator: `router.get("/oauth/callback")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_exchange` — function (async), line 535
- **route:** `POST /oauth/exchange/{server_id}`
- decorator: `router.post("/oauth/exchange/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_exchange_and_connect` — function (async), line 570
- **called from:**
- `routes/mcp/mcp_routes.py:527`
- `routes/mcp/mcp_routes.py:563`

## `_oauth_authorize_page` — function, line 659
- **called from:**
- `routes/mcp/mcp_routes.py:503`
- `tests/test_mcp_oauth.py:186`

## `_oauth_result_page` — function, line 728
- **called from:**
- `routes/mcp/mcp_routes.py:512`
- `routes/mcp/mcp_routes.py:514`
- `routes/mcp/mcp_routes.py:518`
- `routes/mcp/mcp_routes.py:529`
- `routes/mcp/mcp_routes.py:543`
- `routes/mcp/mcp_routes.py:545`
- `routes/mcp/mcp_routes.py:549`
- `routes/mcp/mcp_routes.py:555`
- `routes/mcp/mcp_routes.py:565`
- `routes/mcp/mcp_routes.py:576`
- `routes/mcp/mcp_routes.py:578`
- `routes/mcp/mcp_routes.py:609`
- `routes/mcp/mcp_routes.py:636`
- `routes/mcp/mcp_routes.py:643`
- `routes/mcp/mcp_routes.py:649`
- `routes/mcp/mcp_routes.py:652`
