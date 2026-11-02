# `routes/font_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_split_family_token` — function, line 11
- **called from:**
- `routes/font_routes.py:29`

## `_derive_family` — function, line 19
- **called from:**
- `routes/font_routes.py:45`
- `tests/test_font_routes.py:5`
- `tests/test_font_routes.py:9`
- `tests/test_font_routes.py:10`
- `tests/test_font_routes.py:11`

## `setup_font_routes` — function, line 33
- **called from:**
- `app.py:826`

## `list_custom_fonts` — function (async), line 37
- **route:** `GET /custom`
- decorator: `router.get("/custom")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
