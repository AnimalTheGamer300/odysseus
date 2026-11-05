# `scripts/demo_email/demo_account.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_owner_scope` — function, line 41
- **called from:**
- `routes/chatgpt_subscription_routes.py:40`
- `routes/chatgpt_subscription_routes.py:167`
- `routes/chatgpt_subscription_routes.py:254`
- `routes/chatgpt_subscription_routes.py:326`
- `scripts/demo_email/demo_account.py:83`
- `scripts/demo_email/demo_account.py:121`

## `_discover_demo_scopes` — function, line 47
- **called from:**
- `scripts/demo_email/demo_account.py:101`
- `scripts/demo_email/demo_account.py:155`

## `_lock_and_load_demo_rows` — function, line 61
- **called from:**
- `scripts/demo_email/demo_account.py:104`
- `scripts/demo_email/demo_account.py:158`

## `_promote_oldest_enabled` — function, line 82
- **called from:**
- `scripts/demo_email/demo_account.py:119`
- `scripts/demo_email/demo_account.py:167`

## `setup` — function, line 99
- **called from:**
- `scripts/demo_email/demo_account.py:178`
- `tests/test_reserved_username_admin_escalation.py:55`
- `tests/test_token_cache_atomic_swap.py:34`

## `teardown` — function, line 154
- **called from:**
- `scripts/demo_email/demo_account.py:180`
- `tests/test_email_account_default_serialization.py:521`
- `static/js/document.js:6713`
- `static/js/documentLibrary.js:351`
- `static/js/documentLibrary.js:375`
- `static/js/keyboard-shortcuts.js:74`
