# `routes/api_token_routes.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalize_scopes` — function, line 39
- **called from:**
- `routes/api_token_routes.py:127`
- `routes/api_token_routes.py:178`

## `ensure_before` — function, line 60
- **called from:**
- `routes/api_token_routes.py:66`
- `routes/api_token_routes.py:67`
- `routes/api_token_routes.py:68`
- `routes/api_token_routes.py:69`
- `routes/api_token_routes.py:70`
- `routes/api_token_routes.py:71`

## `setup_api_token_routes` — function, line 76
- **called from:**
- `app.py:936`
- `tests/test_api_token_routes.py:90`

## `list_tokens` — function, line 80
- **route:** `GET /tokens`
- decorator: `router.get("/tokens")`
- **called from:**
- `tests/test_api_token_routes.py:265`

## `_invalidate_cache` — function, line 98
- **called from:**
- `routes/api_token_routes.py:144`
- `routes/api_token_routes.py:192`
- `routes/api_token_routes.py:206`

## `token_profiles` — function, line 108
- **route:** `GET /tokens/profiles`
- decorator: `router.get("/tokens/profiles")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_token` — function, line 116
- **route:** `POST /tokens`
- decorator: `router.post("/tokens")`
- **called from:**
- `tests/test_api_token_routes.py:172`
- `tests/test_api_token_routes.py:205`
- `tests/test_api_token_routes.py:220`

## `update_token` — function (async), line 156
- **route:** `PATCH /tokens/{token_id}`
- decorator: `router.patch("/tokens/{token_id}")`
- **called from:**
- `tests/test_api_token_routes.py:367`
- `tests/test_api_token_routes.py:390`
- `tests/test_api_token_routes.py:407`
- `tests/test_api_token_routes.py:443`
- `tests/test_api_token_routes.py:484`
- `tests/test_api_token_routes.py:528`
- `tests/test_api_token_routes.py:552`
- `tests/test_api_token_routes.py:574`

## `delete_token` — function, line 196
- **route:** `DELETE /tokens/{token_id}`
- decorator: `router.delete("/tokens/{token_id}")`
- **called from:**
- `tests/test_api_token_routes.py:298`
- `tests/test_api_token_routes.py:325`
- `tests/test_api_token_routes.py:463`
- `tests/test_api_token_routes.py:502`
