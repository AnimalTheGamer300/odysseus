# `src/chatgpt_subscription.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_database_handles` — function, line 34
- **called from:**
- `src/chatgpt_subscription.py:255`

## `_refresh_lock_for` — function, line 39
- **called from:**
- `src/chatgpt_subscription.py:270`

## `ChatGPTSubscriptionError` — class, line 48
- **called from:**
- `src/chatgpt_subscription.py:154`
- `src/chatgpt_subscription.py:162`
- `src/chatgpt_subscription.py:164`
- `src/chatgpt_subscription.py:177`

## `ChatGPTSubscriptionReauthRequired` — class, line 52
- **called from:**
- `src/chatgpt_subscription.py:153`
- `src/chatgpt_subscription.py:211`
- `src/chatgpt_subscription.py:218`
- `src/chatgpt_subscription.py:231`

## `ChatGPTSubscriptionRateLimited` — class, line 56
- **called from:**
- `src/chatgpt_subscription.py:149`

## `ChatGPTSubscriptionAuthNotFound` — class, line 60
- **called from:**
- `src/chatgpt_subscription.py:266`

## `is_chatgpt_subscription_base` — function, line 64
- **called from:**
- `routes/chat_helpers.py:513`
- `routes/chat_routes.py:713`
- `routes/chat_routes.py:739`
- `src/llm_core.py:1017`
- `src/llm_core.py:1153`

## `chatgpt_headers` — function, line 78
- **called from:**
- `src/chatgpt_subscription.py:96`
- `src/endpoint_resolver.py:332`

## `fetch_available_models` — function, line 90
- **called from:**
- `routes/chat_routes.py:764`
- `routes/chatgpt_subscription_routes.py:32`
- `routes/model_routes.py:968`

## `_raise_for_oauth_response` — function, line 128
- **called from:**
- `src/chatgpt_subscription.py:158`

## `_json_or_error` — function, line 157
- **called from:**
- `src/chatgpt_subscription.py:175`
- `src/chatgpt_subscription.py:193`
- `src/chatgpt_subscription.py:209`
- `src/chatgpt_subscription.py:229`

## `request_device_code` — function, line 168
- **called from:**
- `routes/chatgpt_subscription_routes.py:111`
- `routes/copilot_routes.py:108`
- `tests/test_copilot.py:159`

## `poll_device_auth` — function, line 184
- **called from:**
- `routes/chatgpt_subscription_routes.py:137`

## `exchange_authorization_code` — function, line 196
- **called from:**
- `routes/chatgpt_subscription_routes.py:146`

## `refresh_oauth_tokens` — function, line 215
- **called from:**
- `src/chatgpt_subscription.py:275`

## `_decode_jwt_payload` — function, line 235
- **called from:**
- `src/chatgpt_subscription.py:248`

## `access_token_is_expiring` — function, line 246
- **called from:**
- `src/chatgpt_subscription.py:269`
- `src/chatgpt_subscription.py:274`

## `resolve_runtime_credentials` — function, line 254
- **called from:**
- `src/endpoint_resolver.py:159`

## `to_http_exception` — function, line 294
- **called from:**
- `routes/chatgpt_subscription_routes.py:113`
- `routes/chatgpt_subscription_routes.py:150`

## `build_responses_input` — function, line 302
- **called from:**
- `src/llm_core.py:1315`
