# `routes/workspace_routes.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_workspace_routes` — function, line 14
- **called from:**
- `app.py:807`
- `tests/test_workspace_confine.py:437`
- `tests/test_workspace_confine.py:487`

## `browse` — function, line 18
- **route:** `GET /browse`
- decorator: `router.get("/browse")`
- **called from:**
- `tests/test_workspace_confine.py:443`
- `tests/test_workspace_confine.py:447`
- `tests/test_workspace_confine.py:494`
- `tests/test_workspace_confine.py:496`

## `vet` — function, line 69
- **route:** `GET /vet`
- decorator: `router.get("/vet")`
- **called from:**
- `tests/test_workspace_confine.py:499`
- `tests/test_workspace_confine.py:501`
- `tests/test_workspace_confine.py:506`
