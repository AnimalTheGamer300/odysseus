# `src/settings_scrub.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_canonical_key_name` — function, line 31
- **called from:**
- `src/settings_scrub.py:40`

## `is_secret_key` — function, line 39
- **called from:**
- `src/settings_scrub.py:55`
- `src/settings_scrub.py:61`
- `tests/test_settings_scrub.py:49`
- `tests/test_settings_scrub.py:58`

## `_scrub_value` — function, line 48
- **called from:**
- `src/settings_scrub.py:56`
- `src/settings_scrub.py:60`
- `src/settings_scrub.py:70`

## `scrub_settings` — function, line 66
- **called from:**
- `routes/auth_routes.py:724`
- `tests/test_settings_scrub.py:16`
- `tests/test_settings_scrub.py:23`
- `tests/test_settings_scrub.py:28`
- `tests/test_settings_scrub.py:34`
- `tests/test_settings_scrub.py:45`
- `tests/test_settings_scrub.py:50`
- `tests/test_settings_scrub.py:54`
- `tests/test_settings_scrub.py:64`
- `tests/test_settings_scrub.py:71`
- `tests/test_settings_scrub.py:76`
- `tests/test_settings_scrub.py:93`
- `tests/test_settings_scrub.py:94`
