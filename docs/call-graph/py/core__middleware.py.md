# `core/middleware.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `get_application_route_path` — function, line 24
- **called from:**
- `app.py:365`
- `tests/test_auth_root_path.py:94`

## `with_asgi_root_path` — function, line 35
- **called from:**
- `app.py:410`
- `app.py:475`
- `tests/test_auth_root_path.py:110`

## `path_is_route_or_child` — function, line 43
- **called from:**
- `app.py:294`
- `tests/test_auth_root_path.py:114`
- `tests/test_auth_root_path.py:115`
- `tests/test_auth_root_path.py:116`

## `is_cors_preflight` — function, line 48
- **called from:**
- `app.py:373`
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
- `routes/codex_routes.py:123`
- `routes/cookbook_routes.py:927`
- `routes/cookbook_routes.py:936`
- `routes/cookbook_routes.py:967`
- `routes/cookbook_routes.py:1069`
- `routes/cookbook_routes.py:1408`
- `routes/cookbook_routes.py:1972`
- `routes/cookbook_routes.py:2840`
- `routes/cookbook_routes.py:3160`
- `routes/cookbook_routes.py:3324`
- `routes/cookbook_routes.py:3370`
- `routes/cookbook_routes.py:3410`
- `routes/cookbook_routes.py:4204`
- `routes/device_flow.py:149`
- `routes/device_flow.py:161`
- `routes/device_flow.py:189`
- `routes/diagnostics_routes.py:28`
- `routes/diagnostics_routes.py:34`
- `routes/diagnostics_routes.py:58`
- `routes/diagnostics_routes.py:68`
- `routes/diagnostics_routes.py:75`
- `routes/diagnostics_routes.py:96`
- `routes/mcp/mcp_routes.py:123`
- `routes/mcp/mcp_routes.py:173`
- `routes/mcp/mcp_routes.py:290`
- `routes/mcp/mcp_routes.py:326`
- `routes/mcp/mcp_routes.py:359`
- `routes/mcp/mcp_routes.py:377`
- `routes/mcp/mcp_routes.py:384`
- `routes/mcp/mcp_routes.py:407`
- `routes/mcp/mcp_routes.py:431`
- `routes/mcp/mcp_routes.py:486`
- `routes/mcp/mcp_routes.py:500`
- `routes/model_routes.py:1683`
- `routes/model_routes.py:1759`
- `routes/model_routes.py:1799`
- `routes/model_routes.py:1844`
- `routes/model_routes.py:1915`
- `routes/model_routes.py:1927`
- `routes/model_routes.py:1934`
- `routes/model_routes.py:2010`
- `routes/model_routes.py:2234`
- `routes/model_routes.py:2260`
- `routes/model_routes.py:2316`
- `routes/model_routes.py:2371`
- `routes/model_routes.py:2499`
- `routes/model_routes.py:2661`
- `routes/model_routes.py:2666`
- `routes/model_routes.py:2713`
- `routes/session_routes.py:793`
- … +18 more (grep the name in repo)

## `SecurityHeadersMiddleware` — class, line 85
- **called from:**
- `tests/test_document_render_pdf_iframe.py:44`

## `SecurityHeadersMiddleware.dispatch` — method (async), line 88
- **called from:**
- `tests/test_document_render_pdf_iframe.py:47`
