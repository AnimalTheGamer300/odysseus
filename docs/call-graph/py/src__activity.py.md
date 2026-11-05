# `src/activity.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `begin_image_op` — function, line 20
- **called from:**
- `app.py:260`
- `src/activity.py:39`
- `tests/test_activity.py:7`
- `tests/test_activity.py:8`

## `end_image_op` — function, line 27
- **called from:**
- `app.py:273`
- `src/activity.py:43`
- `tests/test_activity.py:10`
- `tests/test_activity.py:12`
- `tests/test_activity.py:15`

## `image_op` — function, line 38
- decorator: `contextmanager`
- **called from:**
- `tests/test_activity.py:21`
- `tests/test_activity.py:32`

## `activity` — function, line 46
- **called from:**
- `app.py:1051`
- `tests/test_activity.py:23`
- `tests/test_activity.py:27`

## `heavy_image_ops_active` — function, line 55
- **called from:**
- `app.py:1050`
- `src/activity.py:61`
- `tests/test_activity.py:6`
- `tests/test_activity.py:9`
- `tests/test_activity.py:11`
- `tests/test_activity.py:13`
- `tests/test_activity.py:16`
- `tests/test_activity.py:36`

## `busy` — function, line 60
- **called from:**
- `tests/test_activity.py:20`
- `tests/test_activity.py:22`
- `tests/test_activity.py:26`
- `static/js/backgroundToolJobs.js:116`
