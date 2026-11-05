# `routes/font_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_split_family_token` — function, line 11
- **called from:**
- `routes/font_routes.py:30`

## `_derive_family` — function, line 19
- **called from:**
- `routes/font_routes.py:46`
- `tests/test_font_routes.py:10`
- `tests/test_font_routes.py:14`
- `tests/test_font_routes.py:15`
- `tests/test_font_routes.py:16`
- `tests/test_font_routes.py:31`

## `setup_font_routes` — function, line 34
- **called from:**
- `app.py:910`
- `tests/test_font_routes.py:41`

## `list_custom_fonts` — function (async), line 38
- **route:** `GET /custom`
- decorator: `router.get("/custom")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
