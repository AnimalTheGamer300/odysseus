# `routes/cleanup/cleanup_routes.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_cleanup_routes` — function, line 10
- **called from:**
- `app.py:732`
- `tests/test_cleanup_owner_scope.py:159`
- `tests/test_cleanup_owner_scope.py:181`

## `cleanup_preview` — function (async), line 23
- **route:** `GET /preview`
- decorator: `router.get("/preview")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_endpoint` — function (async), line 39
- decorator: `router.post("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
