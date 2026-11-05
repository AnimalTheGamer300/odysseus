# `routes/chatgpt_subscription_routes.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_owner_scope` — function, line 34
- **called from:**
- `routes/chatgpt_subscription_routes.py:40`
- `routes/chatgpt_subscription_routes.py:167`
- `routes/chatgpt_subscription_routes.py:254`
- `routes/chatgpt_subscription_routes.py:326`
- `scripts/demo_email/demo_account.py:83`
- `scripts/demo_email/demo_account.py:121`

## `_owner_chatgpt_auths` — function, line 38
- **called from:**
- `routes/chatgpt_subscription_routes.py:59`
- `routes/chatgpt_subscription_routes.py:79`
- `routes/chatgpt_subscription_routes.py:425`

## `_endpoints_for_auth` — function, line 43
- **called from:**
- `routes/chatgpt_subscription_routes.py:64`
- `routes/chatgpt_subscription_routes.py:86`
- `routes/chatgpt_subscription_routes.py:402`
- `routes/chatgpt_subscription_routes.py:424`

## `_display_label` — function, line 47
- **called from:**
- `routes/chatgpt_subscription_routes.py:62`
- `routes/chatgpt_subscription_routes.py:65`
- `routes/chatgpt_subscription_routes.py:84`
- `routes/chatgpt_subscription_routes.py:87`
- `routes/chatgpt_subscription_routes.py:206`
- `routes/chatgpt_subscription_routes.py:373`

## `_assert_label_available` — function, line 55
- **called from:**
- `routes/chatgpt_subscription_routes.py:142`
- `routes/chatgpt_subscription_routes.py:146`
- `routes/chatgpt_subscription_routes.py:258`
- `routes/chatgpt_subscription_routes.py:263`

## `_default_new_label` — function, line 72
- **called from:**
- `routes/chatgpt_subscription_routes.py:145`

## `_new_id` — function, line 98
- **called from:**
- `routes/chatgpt_subscription_routes.py:148`
- `routes/chatgpt_subscription_routes.py:178`

## `_provision_endpoint` — function, line 106
- **called from:**
- `routes/chatgpt_subscription_routes.py:345`
- `routes/copilot_routes.py:149`
- `tests/test_chatgpt_subscription_routes.py:36`
- `tests/test_chatgpt_subscription_routes.py:56`
- `tests/test_chatgpt_subscription_routes.py:87`
- `tests/test_chatgpt_subscription_routes.py:248`
- `tests/test_chatgpt_subscription_routes.py:256`
- `tests/test_chatgpt_zero_native_tools.py:211`
- `tests/test_chatgpt_zero_native_tools.py:212`
- `tests/test_chatgpt_zero_native_tools.py:214`
- `tests/test_copilot_routes.py:29`
- `tests/test_copilot_routes.py:51`
- `tests/test_copilot_routes.py:52`
- `tests/test_copilot_routes.py:73`

## `_form_value` — function, line 222
- **called from:**
- `routes/chatgpt_subscription_routes.py:233`
- `routes/chatgpt_subscription_routes.py:236`
- `routes/chatgpt_subscription_routes.py:237`

## `_start_device_flow` — function, line 230
- **called from:**
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:57`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:77`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:81`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:89`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:103`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:108`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:173`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:188`

## `_poll_device_flow` — function, line 313
- **called from:**
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:136`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:153`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:179`

## `_account_summary` — function, line 369
- **called from:**
- `routes/chatgpt_subscription_routes.py:403`
- `routes/chatgpt_subscription_routes.py:424`

## `usage_error_payload` — function, line 382
- **called from:**
- `routes/chatgpt_subscription_routes.py:445`
- `routes/chatgpt_subscription_routes.py:450`

## `_load_owned_account` — function, line 393
- **called from:**
- `routes/chatgpt_subscription_routes.py:439`

## `setup_chatgpt_subscription_routes` — function, line 408
- **called from:**
- `app.py:832`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:200`
- `tests/test_chatgpt_subscription_usage.py:337`

## `list_accounts` — function, line 418
- **route:** `GET /accounts`
- decorator: `router.get("/accounts")`
- **called from:**
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:205`
- `tests/test_email_oauth.py:858`

## `account_usage` — function, line 431
- **route:** `GET /accounts/{auth_id}/usage`
- decorator: `router.get("/accounts/{auth_id}/usage")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
