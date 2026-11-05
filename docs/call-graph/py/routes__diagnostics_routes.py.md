# `routes/diagnostics_routes.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_diagnostics_routes` — function, line 16
- **called from:**
- `app.py:808`
- `tests/test_admin_listing_authorization.py:133`
- `tests/test_diagnostics_logs.py:22`
- `tests/test_diagnostics_service_route.py:38`

## `get_service_health` — function (async), line 25
- **route:** `GET /api/diagnostics/services`
- decorator: `router.get("/api/diagnostics/services")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_diagnostics_logs` — function (async), line 33
- **route:** `GET /api/diagnostics/logs`
- decorator: `router.get("/api/diagnostics/logs")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_database_stats` — function (async), line 57
- **route:** `GET /api/db/stats`
- decorator: `router.get("/api/db/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_rag_stats` — function (async), line 67
- **route:** `GET /api/rag/stats`
- decorator: `router.get("/api/rag/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_youtube` — function (async), line 74
- **route:** `GET /api/test/youtube`
- decorator: `router.get("/api/test/youtube")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_research` — function (async), line 95
- **route:** `POST /api/test-research`
- decorator: `router.post("/api/test-research")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
