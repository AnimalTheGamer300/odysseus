# `routes/mcp/mcp_routes.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_mcp_oauth_base_dir` — function, line 24
- **called from:**
- `routes/mcp/mcp_routes.py:35`

## `_resolve_mcp_oauth_path` — function, line 29
- **called from:**
- `routes/mcp/mcp_routes.py:60`
- `routes/mcp/mcp_routes.py:72`
- `routes/mcp/mcp_routes.py:210`
- `routes/mcp/mcp_routes.py:215`
- `tests/test_security_regressions.py:1060`
- `tests/test_security_regressions.py:1078`
- `tests/test_security_regressions.py:1088`
- `tests/test_security_regressions.py:1090`

## `_sanitize_mcp_oauth_config` — function, line 51
- **called from:**
- `routes/mcp/mcp_routes.py:200`
- `routes/mcp/mcp_routes.py:440`
- `routes/mcp/mcp_routes.py:533`
- `tests/test_security_regressions.py:1097`

## `_mcp_oauth_token_missing` — function, line 67
- **called from:**
- `routes/mcp/mcp_routes.py:133`
- `routes/mcp/mcp_routes.py:259`

## `_apply_mcp_oauth_env` — function, line 81
- **called from:**
- `routes/mcp/mcp_routes.py:203`
- `tests/test_security_regressions.py:1104`

## `_load_disabled_map` — function, line 93
- **called from:**
- `routes/mcp/mcp_routes.py:378`

## `_mcp_oauth_redirect_uri` — function, line 111
- **called from:**
- `routes/mcp/mcp_routes.py:456`
- `routes/mcp/mcp_routes.py:545`
- `tests/test_security_regressions.py:1051`

## `setup_mcp_routes` — function, line 117
- **called from:**
- `app.py:836`

## `list_servers` — function, line 121
- **route:** `GET /servers`
- decorator: `router.get("/servers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_server` — function (async), line 159
- **route:** `POST /servers`
- decorator: `router.post("/servers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reconnect_server` — function (async), line 288
- **route:** `POST /servers/{server_id}/reconnect`
- decorator: `router.post("/servers/{server_id}/reconnect")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_server` — function (async), line 324
- **route:** `PATCH /servers/{server_id}`
- decorator: `router.patch("/servers/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_server` — function (async), line 357
- **route:** `DELETE /servers/{server_id}`
- decorator: `router.delete("/servers/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_tools` — function, line 375
- **route:** `GET /tools`
- decorator: `router.get("/tools")`
- **called from:**
- `mcp_servers/email_server.py:2088`
- `mcp_servers/image_gen_server.py:24`
- `mcp_servers/memory_server.py:115`
- `mcp_servers/rag_server.py:46`
- `src/mcp_manager.py:205`
- `src/mcp_manager.py:274`
- `src/mcp_manager.py:362`

## `list_server_tools` — function, line 382
- **route:** `GET /servers/{server_id}/tools`
- decorator: `router.get("/servers/{server_id}/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_disabled_tools` — function (async), line 402
- **route:** `PATCH /servers/{server_id}/tools`
- decorator: `router.patch("/servers/{server_id}/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_authorize` — function, line 429
- **route:** `GET /oauth/authorize/{server_id}`
- decorator: `router.get("/oauth/authorize/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_callback` — function (async), line 483
- **route:** `GET /oauth/callback`
- decorator: `router.get("/oauth/callback")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `oauth_exchange` — function (async), line 498
- **route:** `POST /oauth/exchange/{server_id}`
- decorator: `router.post("/oauth/exchange/{server_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_exchange_and_connect` — function (async), line 523
- **called from:**
- `routes/mcp/mcp_routes.py:495`
- `routes/mcp/mcp_routes.py:521`

## `_oauth_authorize_page` — function, line 612
- **called from:**
- `routes/mcp/mcp_routes.py:478`
- `tests/test_mcp_oauth.py:186`

## `_oauth_result_page` — function, line 681
- **called from:**
- `routes/mcp/mcp_routes.py:489`
- `routes/mcp/mcp_routes.py:506`
- `routes/mcp/mcp_routes.py:508`
- `routes/mcp/mcp_routes.py:515`
- `routes/mcp/mcp_routes.py:529`
- `routes/mcp/mcp_routes.py:531`
- `routes/mcp/mcp_routes.py:562`
- `routes/mcp/mcp_routes.py:589`
- `routes/mcp/mcp_routes.py:596`
- `routes/mcp/mcp_routes.py:602`
- `routes/mcp/mcp_routes.py:605`
