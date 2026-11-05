# `routes/copilot_routes.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_provision_endpoint` — function, line 45
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

## `_start_device_flow` — function, line 102
- **called from:**
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:57`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:77`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:81`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:89`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:103`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:108`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:173`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:188`

## `_poll_device_flow` — function, line 139
- **called from:**
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:136`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:153`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:179`

## `setup_copilot_routes` — function, line 166
- **called from:**
- `app.py:828`
