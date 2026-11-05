# `core/middleware.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `get_application_route_path` — function, line 24
- **called from:**
- `app.py:406`
- `tests/test_auth_root_path.py:93`

## `with_asgi_root_path` — function, line 35
- **called from:**
- `app.py:451`
- `app.py:516`
- `tests/test_auth_root_path.py:109`

## `path_is_route_or_child` — function, line 43
- **called from:**
- `app.py:334`
- `tests/test_auth_root_path.py:113`
- `tests/test_auth_root_path.py:114`
- `tests/test_auth_root_path.py:115`

## `is_cors_preflight` — function, line 48
- **called from:**
- `app.py:414`
- `tests/test_cors_preflight.py:19`
- `tests/test_cors_preflight.py:24`
- `tests/test_cors_preflight.py:30`

## `require_admin` — function, line 57
- **called from:**
- `companion/routes.py:176`
- `companion/routes.py:202`
- `routes/admin_wipe/admin_wipe_routes.py:73`
- `routes/api_token_routes.py:81`
- `routes/api_token_routes.py:109`
- `routes/api_token_routes.py:122`
- `routes/api_token_routes.py:157`
- `routes/api_token_routes.py:197`
- `routes/backup_routes.py:22`
- `routes/backup_routes.py:66`
- `routes/chatgpt_subscription_routes.py:395`
- `routes/chatgpt_subscription_routes.py:419`
- `routes/codex_routes.py:135`
- `routes/cookbook_routes.py:801`
- `routes/cookbook_routes.py:810`
- `routes/cookbook_routes.py:841`
- `routes/cookbook_routes.py:944`
- `routes/cookbook_routes.py:1283`
- `routes/cookbook_routes.py:1882`
- `routes/cookbook_routes.py:2719`
- `routes/cookbook_routes.py:3039`
- `routes/cookbook_routes.py:3203`
- `routes/cookbook_routes.py:3249`
- `routes/cookbook_routes.py:3289`
- `routes/cookbook_routes.py:4110`
- `routes/device_flow.py:149`
- `routes/device_flow.py:161`
- `routes/device_flow.py:189`
- `routes/diagnostics_routes.py:28`
- `routes/diagnostics_routes.py:34`
- `routes/diagnostics_routes.py:58`
- `routes/diagnostics_routes.py:68`
- `routes/diagnostics_routes.py:75`
- `routes/diagnostics_routes.py:96`
- `routes/editor_agent_routes.py:1300`
- `routes/mcp/mcp_routes.py:136`
- `routes/mcp/mcp_routes.py:186`
- `routes/mcp/mcp_routes.py:310`
- `routes/mcp/mcp_routes.py:346`
- `routes/mcp/mcp_routes.py:379`
- `routes/mcp/mcp_routes.py:397`
- `routes/mcp/mcp_routes.py:404`
- `routes/mcp/mcp_routes.py:427`
- `routes/mcp/mcp_routes.py:456`
- `routes/mcp/mcp_routes.py:526`
- `routes/mcp/mcp_routes.py:537`
- `routes/model_routes.py:1831`
- `routes/model_routes.py:1907`
- `routes/model_routes.py:1947`
- `routes/model_routes.py:1992`
- `routes/model_routes.py:2065`
- `routes/model_routes.py:2077`
- `routes/model_routes.py:2084`
- `routes/model_routes.py:2165`
- `routes/model_routes.py:2419`
- `routes/model_routes.py:2460`
- `routes/model_routes.py:2516`
- `routes/model_routes.py:2573`
- `routes/model_routes.py:2645`
- `routes/model_routes.py:2865`
- … +22 more (grep the name in repo)

## `SecurityHeadersMiddleware` — class, line 85
- **called from:**
- `tests/test_document_render_pdf_iframe.py:44`

## `SecurityHeadersMiddleware.dispatch` — method (async), line 88
- **called from:**
- `tests/test_browser_identity_transport.py:86`
- `tests/test_browser_identity_transport.py:101`
- `tests/test_browser_identity_transport.py:110`
- `tests/test_browser_identity_transport.py:132`
- `tests/test_browser_identity_transport.py:157`
- `tests/test_browser_resource_identity.py:128`
- `tests/test_browser_resource_identity.py:257`
- `tests/test_browser_resource_identity.py:260`
- `tests/test_browser_resource_identity.py:273`
- `tests/test_browser_resource_identity.py:286`
- `tests/test_document_render_pdf_iframe.py:47`
- `tests/test_owned_resource_identity.py:100`
- `tests/test_owned_resource_identity.py:113`
- `tests/test_owned_resource_identity.py:146`
- `tests/test_owned_resource_identity.py:155`
- `tests/test_owned_resource_identity.py:169`
- `tests/test_owned_resource_identity.py:171`
- `tests/test_owned_resource_identity.py:172`
- `tests/test_owned_resource_identity.py:185`
- `tests/test_owned_resource_identity.py:188`
- `tests/test_owned_resource_identity.py:189`
- `tests/test_owned_resource_identity.py:300`
- `tests/test_owned_resource_identity.py:302`
- `tests/test_owned_resource_identity.py:314`
- `tests/test_owned_resource_identity.py:350`
- `tests/test_owned_resource_identity.py:384`
- `tests/test_owned_resource_identity.py:399`
- `tests/test_owned_resource_identity.py:402`
- `tests/test_owned_resource_identity.py:409`
- `tests/test_remote_resource_identity.py:69`
- `tests/test_remote_resource_identity.py:77`
- `tests/test_remote_resource_identity.py:80`
- `tests/test_remote_resource_identity.py:100`
- `tests/test_remote_resource_identity.py:122`
- `tests/test_remote_resource_identity.py:134`
- `tests/test_remote_resource_identity.py:136`
- `tests/test_remote_resource_identity.py:148`
- `tests/test_remote_resource_identity.py:190`
- `tests/test_remote_resource_identity.py:223`
- `tests/test_remote_resource_identity.py:246`
- `tests/test_remote_resource_identity.py:248`
- `tests/test_remote_resource_identity.py:253`
- `tests/test_remote_resource_identity.py:261`
- `tests/test_remote_resource_identity.py:266`
- `tests/test_remote_resource_identity.py:269`
- `tests/test_remote_resource_identity.py:287`
- `tests/test_remote_resource_identity.py:304`
- `tests/test_remote_resource_identity.py:317`
- `tests/test_remote_resource_identity.py:328`
- `tests/test_remote_resource_identity.py:337`
- `tests/test_remote_resource_identity.py:355`
- `tests/test_remote_resource_identity.py:367`
- `tests/test_remote_resource_identity.py:377`
- `tests/test_remote_resource_identity.py:392`
- `tests/test_remote_resource_identity.py:397`
- `tests/test_resource_identity.py:166`
- `tests/test_resource_identity.py:201`
- `tests/test_resource_identity.py:213`
- `tests/test_resource_identity.py:224`
- `tests/test_resource_identity.py:254`
- … +51 more (grep the name in repo)
