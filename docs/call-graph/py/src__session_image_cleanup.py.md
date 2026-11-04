# `src/session_image_cleanup.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_database_models` — function, line 16
- **called from:**
- `src/session_image_cleanup.py:48`
- `src/session_image_cleanup.py:86`

## `_generated_image_path_for_cleanup` — function, line 23
- **called from:**
- `routes/session_routes.py:822`
- `src/session_image_cleanup.py:107`

## `_image_filename_from_url` — function, line 39
- **called from:**
- `src/session_image_cleanup.py:77`

## `session_image_refs` — function, line 46
- **called from:**
- `routes/session_routes.py:803`
- `src/session_image_cleanup.py:90`

## `cleanup_session_images` — function, line 84
- **called from:**
- `core/session_manager.py:953`
- `tests/test_session_image_cleanup.py:69`
