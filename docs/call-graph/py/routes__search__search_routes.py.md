# `routes/search/search_routes.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_request_values` — function (async), line 17
- **called from:**
- `routes/search/search_routes.py:52`
- `routes/search/search_routes.py:90`

## `setup_search_routes` — function, line 39
- **called from:**
- `app.py:720`

## `get_search_settings` — function (async), line 43
- **route:** `GET /api/search/config`
- decorator: `router.get("/api/search/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_web_search` — function (async), line 47
- **route:** `POST /api/search`
- decorator: `router.post("/api/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_search_providers` — function (async), line 69
- **route:** `GET /api/search/providers`
- decorator: `router.get("/api/search/providers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_with_provider` — function (async), line 88
- **route:** `POST /api/search/query`
- decorator: `router.post("/api/search/query")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
