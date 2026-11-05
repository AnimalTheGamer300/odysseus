# `routes/signature_routes.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalize_signature_png` — function, line 32
- **called from:**
- `routes/signature_routes.py:104`
- `tests/test_signature_route_hardening.py:50`
- `tests/test_signature_route_hardening.py:51`
- `tests/test_signature_route_hardening.py:66`

## `_signature_dimension` — function, line 56
- **called from:**
- `routes/signature_routes.py:105`
- `routes/signature_routes.py:106`
- `tests/test_signature_route_hardening.py:74`

## `SignatureCreate` — class, line 64
- **called from:**
- `tests/test_signature_route_hardening.py:87`

## `_to_dict` — function, line 72
- **called from:**
- `routes/signature_routes.py:97`
- `routes/signature_routes.py:122`

## `setup_signature_routes` — function, line 83
- **called from:**
- `app.py:852`
- `tests/test_signature_route_hardening.py:40`

## `list_signatures` — function (async), line 87
- **route:** `GET /api/signatures`
- decorator: `router.get("/api/signatures")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_signature` — function (async), line 102
- **route:** `POST /api/signatures`
- decorator: `router.post("/api/signatures")`
- **called from:**
- `tests/test_signature_route_hardening.py:85`

## `delete_signature` — function (async), line 131
- **route:** `DELETE /api/signatures/{sig_id}`
- decorator: `router.delete("/api/signatures/{sig_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
