# `routes/search/search_routes.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_request_values` — function (async), line 20
- **called from:**
- `routes/search/search_routes.py:153`
- `routes/search/search_routes.py:191`

## `setup_search_routes` — function, line 42
- **called from:**
- `app.py:800`
- `tests/test_codeql_python_residual_closure.py:527`
- `tests/test_codeql_python_residual_security.py:29`

## `web_search_page` — function (async), line 46
- **route:** `GET /search/web`
- decorator: `router.get("/search/web", response_class=HTMLResponse)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_search_settings` — function (async), line 144
- **route:** `GET /api/search/config`
- decorator: `router.get("/api/search/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_web_search` — function (async), line 148
- **route:** `POST /api/search`
- decorator: `router.post("/api/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_search_providers` — function (async), line 170
- **route:** `GET /api/search/providers`
- decorator: `router.get("/api/search/providers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_with_provider` — function (async), line 189
- **route:** `POST /api/search/query`
- decorator: `router.post("/api/search/query")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
