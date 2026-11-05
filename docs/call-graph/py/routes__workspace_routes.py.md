# `routes/workspace_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_workspace_routes` — function, line 14
- **called from:**
- `app.py:891`
- `tests/test_workspace_confine.py:490`
- `tests/test_workspace_confine.py:540`

## `browse` — function, line 18
- **route:** `GET /browse`
- decorator: `router.get("/browse")`
- **called from:**
- `tests/test_workspace_confine.py:496`
- `tests/test_workspace_confine.py:500`
- `tests/test_workspace_confine.py:548`
- `tests/test_workspace_confine.py:550`

## `vet` — function, line 69
- **route:** `GET /vet`
- decorator: `router.get("/vet")`
- **called from:**
- `tests/test_workspace_confine.py:553`
- `tests/test_workspace_confine.py:555`
- `tests/test_workspace_confine.py:560`

## `default_workspace` — function, line 86
- **route:** `GET /default`
- decorator: `router.get("/default")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
