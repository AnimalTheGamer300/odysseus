# `routes/backup_routes.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_backup_routes` — function, line 16
- **called from:**
- `app.py:823`
- `tests/test_backup_import_cross_user_dedup.py:38`
- `tests/test_backup_import_skills.py:36`
- `tests/test_backup_import_skills_dedup.py:81`

## `export_data` — function (async), line 20
- **route:** `GET /api/export`
- decorator: `router.get("/api/export")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_data` — function (async), line 64
- **route:** `POST /api/import`
- decorator: `router.post("/api/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
