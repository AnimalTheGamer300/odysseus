# `src/tool_security.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `plan_mode_disabled_tools` — function, line 169
- **called from:**
- `routes/chat_routes.py:1791`
- `src/agent_loop.py:4089`
- `tests/test_email_registry_sync.py:53`
- `tests/test_plan_mode.py:31`
- `tests/test_plan_mode.py:42`
- `tests/test_plan_mode.py:52`
- `tests/test_plan_mode.py:58`
- `tests/test_plan_mode.py:86`
- `tests/test_review_regressions.py:1011`

## `email_tool_policy_names` — function, line 200
- **called from:**
- `src/agent_loop.py:6223`
- `src/tool_execution.py:1047`
- `tests/test_email_registry_sync.py:76`
- `tests/test_email_registry_sync.py:79`
- `tests/test_email_registry_sync.py:84`
- `tests/test_email_registry_sync.py:85`
- `tests/test_email_registry_sync.py:86`

## `is_public_blocked_tool` — function, line 222
- **called from:**
- `src/tool_capabilities.py:658`
- `src/tool_execution.py:1097`
- `tests/test_ask_user_tool.py:115`
- `tests/test_edit_file.py:22`
- `tests/test_public_blocked_tool_nonstring.py:14`
- `tests/test_public_blocked_tool_nonstring.py:15`
- `tests/test_public_blocked_tool_nonstring.py:16`
- `tests/test_public_blocked_tool_nonstring.py:20`
- `tests/test_public_blocked_tool_nonstring.py:21`
- `tests/test_public_blocked_tool_nonstring.py:25`
- `tests/test_update_plan_tool.py:49`

## `owner_is_admin_or_single_user` — function, line 237
- **called from:**
- `routes/chat_routes.py:525`
- `routes/chat_routes.py:554`
- `routes/email_helpers.py:1820`
- `routes/workspace_routes.py:28`
- `routes/workspace_routes.py:79`
- `src/builtin_actions.py:827`
- `src/tool_execution.py:577`
- `src/tool_security.py:269`
- `tests/test_review_regressions.py:1196`
- `tests/test_review_regressions.py:1222`
- `tests/test_review_regressions.py:1250`

## `blocked_tools_for_owner` — function, line 267
- **called from:**
- `src/agent_loop.py:4073`
- `tests/test_edit_file.py:27`
- `tests/test_edit_file.py:31`
- `tests/test_review_regressions.py:1163`
- `tests/test_review_regressions.py:1197`
- `tests/test_review_regressions.py:1223`
- `tests/test_review_regressions.py:1251`

## `delegated_credential_blocked_tools` — function, line 274
- **called from:**
- `routes/chat_routes.py:1681`
- `src/agent_loop.py:4077`
- `tests/test_api_token_tool_authority.py:268`
