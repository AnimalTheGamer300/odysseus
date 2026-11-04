# `src/url_security.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_resolve_hostname_ips` — function, line 39
- **called from:**
- `services/search/content.py:33`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_blocked_ip` — function, line 47
- **called from:**
- `src/url_security.py:64`
- `src/url_security.py:71`

## `_host_resolves_publicly` — function, line 59
- **called from:**
- `src/url_security.py:78`

## `is_public_http_url` — function, line 74
- **called from:**
- `src/url_security.py:92`
- `tests/test_api_chat_security.py:27`

## `validate_public_http_url` — function, line 81
- **called from:**
- `routes/webhook/webhook_routes.py:289`
- `tests/test_api_chat_security.py:39`
- `tests/test_api_chat_security.py:52`
