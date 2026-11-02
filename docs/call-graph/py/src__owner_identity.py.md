# `src/owner_identity.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `auth_disabled` — function, line 17
- **called from:**
- `app.py:258`
- `core/middleware.py:76`
- `src/auth_helpers.py:100`
- `src/owner_identity.py:49`
- `tests/test_owner_identity.py:86`

## `normalize_owner` — function, line 22
- **called from:**
- `src/owner_identity.py:29`
- `src/owner_identity.py:44`

## `owner_key` — function, line 28
- **called from:**
- `src/owner_identity.py:34`
- `src/owner_identity.py:56`

## `is_request_sentinel_owner` — function, line 33
- **called from:**
- `src/owner_identity.py:46`

## `effective_storage_owner` — function, line 37
- **called from:**
- `src/auth_helpers.py:110`
- `tests/test_owner_identity.py:10`
- `tests/test_owner_identity.py:11`
- `tests/test_owner_identity.py:12`
- `tests/test_owner_identity.py:14`
- `tests/test_owner_identity.py:15`
- `tests/test_owner_identity.py:18`
- `tests/test_owner_identity.py:19`
- `tests/test_owner_identity.py:20`
- `tests/test_owner_identity.py:22`
- `tests/test_owner_identity.py:100`
- `tests/test_owner_identity.py:101`

## `is_default_local_owner` — function, line 55
- **called from:**
- `tests/test_owner_identity.py:102`
