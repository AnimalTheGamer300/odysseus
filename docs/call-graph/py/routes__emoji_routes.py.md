# `routes/emoji_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_safe_svg` — function, line 57
- **called from:**
- `routes/emoji_routes.py:86`
- `routes/emoji_routes.py:98`
- `tests/test_emoji_svg_hardening.py:15`
- `tests/test_emoji_svg_hardening.py:19`
- `tests/test_emoji_svg_hardening.py:20`
- `tests/test_emoji_svg_hardening.py:21`
- `tests/test_emoji_svg_hardening.py:22`

## `setup_emoji_routes` — function, line 69
- **called from:**
- `app.py:755`
- `tests/test_emoji_svg_hardening.py:7`

## `_blank` — function, line 72
- **called from:**
- `routes/emoji_routes.py:79`
- `routes/emoji_routes.py:91`
- `routes/emoji_routes.py:107`

## `emoji_svg` — function (async), line 76
- **route:** `GET /{code}.svg`
- decorator: `router.get("/{code}.svg")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
