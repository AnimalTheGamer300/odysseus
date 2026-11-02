# `src/cookbook_serve_lifecycle.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_internal_headers` — function, line 28
- **called from:**
- `src/cookbook_serve_lifecycle.py:71`
- `src/cookbook_serve_lifecycle.py:83`
- `src/cookbook_serve_lifecycle.py:119`
- `src/tools/cookbook.py:96`
- `src/tools/cookbook.py:159`
- `src/tools/cookbook.py:267`
- `src/tools/cookbook.py:305`
- `src/tools/cookbook.py:648`
- `src/tools/cookbook.py:733`
- `src/tools/cookbook.py:802`
- `src/tools/cookbook.py:913`
- `src/tools/cookbook.py:1034`
- `src/tools/cookbook.py:1153`
- `src/tools/cookbook.py:1205`
- `src/tools/cookbook.py:1270`
- `src/tools/cookbook.py:1420`
- `src/tools/cookbook.py:1469`
- `src/tools/cookbook.py:1514`
- `src/tools/cookbook.py:1551`
- `src/tools/image.py:132`
- `src/tools/research.py:124`
- `src/tools/system.py:629`
- `src/tools/system.py:703`

## `_delete_endpoint_for_task` — function (async), line 33
- **called from:**
- `src/cookbook_serve_lifecycle.py:180`

## `_stop_serve` — function (async), line 93
- **called from:**
- `src/cookbook_serve_lifecycle.py:170`

## `_tick` — function (async), line 137
- **called from:**
- `src/cookbook_serve_lifecycle.py:216`
- `tests/test_cookbook_serve_lifecycle.py:41`

## `cookbook_serve_lifecycle_loop` — function (async), line 211
- **called from:**
- `app.py:1276`
