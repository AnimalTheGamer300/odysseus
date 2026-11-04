# `routes/admin_wipe/admin_wipe_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_wipe_memory_files` — function, line 39
- **called from:**
- `routes/admin_wipe/admin_wipe_routes.py:93`

## `_rmtree_quiet` — function, line 56
- **called from:**
- `routes/admin_wipe/admin_wipe_routes.py:116`
- `routes/admin_wipe/admin_wipe_routes.py:154`
- `routes/admin_wipe/admin_wipe_routes.py:155`

## `setup_admin_wipe_routes` — function, line 65
- **called from:**
- `app.py:691`
- `tests/test_admin_wipe_gallery.py:39`

## `wipe` — function, line 72
- **route:** `DELETE /wipe/{kind}`
- decorator: `router.delete("/wipe/{kind}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
