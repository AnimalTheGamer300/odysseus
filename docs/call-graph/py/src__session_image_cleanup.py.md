# `src/session_image_cleanup.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_database_models` — function, line 16
- **called from:**
- `src/session_image_cleanup.py:44`
- `src/session_image_cleanup.py:82`
- `src/session_image_cleanup.py:105`
- `src/session_image_cleanup.py:113`

## `_generated_image_path_for_cleanup` — function, line 23
- **called from:**
- `routes/session_routes.py:1032`
- `src/session_image_cleanup.py:123`

## `_image_filename_from_url` — function, line 35
- **called from:**
- `src/session_image_cleanup.py:73`

## `session_image_refs` — function, line 42
- **called from:**
- `routes/session_routes.py:1013`
- `src/session_image_cleanup.py:83`

## `session_gallery_images` — function, line 80
- **called from:**
- `routes/session_routes.py:957`
- `src/session_image_cleanup.py:117`
- `tests/test_chat_image_preservation.py:55`

## `preserve_session_images` — function, line 103
- **called from:**
- `core/session_manager.py:984`

## `cleanup_session_images` — function, line 111
- **called from:**
- `core/session_manager.py:982`
- `tests/test_chat_image_preservation.py:56`
- `tests/test_session_image_cleanup.py:69`
