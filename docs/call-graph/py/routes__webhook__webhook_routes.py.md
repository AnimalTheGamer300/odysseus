# `routes/webhook/webhook_routes.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_select_api_chat_fallback_endpoint` — function, line 30
- **called from:**
- `routes/webhook/webhook_routes.py:318`
- `tests/test_api_chat_security.py:341`
- `tests/test_api_chat_security.py:358`
- `tests/test_null_owner_gates.py:292`

## `_caller_owns_session` — function, line 45
- **called from:**
- `routes/webhook/webhook_routes.py:276`
- `tests/test_null_owner_gates.py:198`
- `tests/test_null_owner_gates.py:203`
- `tests/test_null_owner_gates.py:210`
- `tests/test_null_owner_gates.py:211`
- `tests/test_null_owner_gates.py:216`

## `setup_webhook_routes` — function, line 64
- **called from:**
- `app.py:848`
- `tests/test_api_chat_security.py:258`

## `list_webhooks` — function, line 72
- **route:** `GET /webhooks`
- decorator: `router.get("/webhooks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_webhook` — function, line 96
- **route:** `POST /webhooks`
- decorator: `router.post("/webhooks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_webhook` — function (async), line 142
- **route:** `POST /webhooks/{webhook_id}/test`
- decorator: `router.post("/webhooks/{webhook_id}/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `toggle_webhook` — function, line 157
- **route:** `PATCH /webhooks/{webhook_id}`
- decorator: `router.patch("/webhooks/{webhook_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_webhook` — function, line 171
- **route:** `DELETE /webhooks/{webhook_id}`
- decorator: `router.delete("/webhooks/{webhook_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_resolve_base_url` — function, line 218
- **called from:**
- `routes/webhook/webhook_routes.py:294`

## `SyncChatRequest` — class, line 229
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sync_chat` — function (async), line 238
- **route:** `POST /v1/chat`
- decorator: `router.post("/v1/chat")`
- **called from:**
- `tests/test_api_chat_security.py:292`
- `tests/test_api_chat_security.py:323`
- `tests/test_api_chat_security.py:399`
