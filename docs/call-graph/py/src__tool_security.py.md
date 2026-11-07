# `src/tool_security.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `plan_mode_disabled_tools` — function, line 192
- **called from:**
- `routes/chat_routes.py:3761`
- `src/agent_loop.py:21694`
- `src/agent_loop.py:21955`
- `tests/test_email_registry_sync.py:53`
- `tests/test_plan_mode.py:31`
- `tests/test_plan_mode.py:42`
- `tests/test_plan_mode.py:52`
- `tests/test_plan_mode.py:58`
- `tests/test_plan_mode.py:86`
- `tests/test_review_regressions.py:1262`

## `email_tool_policy_names` — function, line 223
- **called from:**
- `src/agent_loop.py:24183`
- `src/agent_loop.py:28195`
- `src/agent_loop.py:33949`
- `src/tool_execution.py:1786`
- `src/tool_execution.py:2090`
- `tests/test_email_registry_sync.py:76`
- `tests/test_email_registry_sync.py:79`
- `tests/test_email_registry_sync.py:84`
- `tests/test_email_registry_sync.py:85`
- `tests/test_email_registry_sync.py:86`

## `is_public_blocked_tool` — function, line 245
- **called from:**
- `src/tool_capabilities.py:922`
- `src/tool_execution.py:2178`
- `tests/test_ask_user_tool.py:118`
- `tests/test_edit_file.py:30`
- `tests/test_public_blocked_tool_nonstring.py:14`
- `tests/test_public_blocked_tool_nonstring.py:15`
- `tests/test_public_blocked_tool_nonstring.py:16`
- `tests/test_public_blocked_tool_nonstring.py:20`
- `tests/test_public_blocked_tool_nonstring.py:21`
- `tests/test_public_blocked_tool_nonstring.py:25`
- `tests/test_update_plan_tool.py:52`

## `owner_is_admin_or_single_user` — function, line 260
- **called from:**
- `routes/chat_routes.py:1856`
- `routes/chat_routes.py:1897`
- `routes/email/email_helpers.py:188`
- `routes/email/email_helpers.py:1969`
- `routes/session_routes.py:1717`
- `routes/workspace_routes.py:28`
- `routes/workspace_routes.py:79`
- `routes/workspace_routes.py:94`
- `src/agent_runtime/local_model_control.py:53`
- `src/builtin_actions.py:961`
- `src/tool_execution.py:1340`
- `src/tool_security.py:292`
- `tests/test_review_regressions.py:1441`
- `tests/test_review_regressions.py:1467`
- `tests/test_review_regressions.py:1495`

## `blocked_tools_for_owner` — function, line 290
- **called from:**
- `routes/chat_routes.py:3843`
- `routes/session_routes.py:1730`
- `src/agent_loop.py:21934`
- `tests/test_cookbook_readonly_tools_admin_gate.py:75`
- `tests/test_cookbook_readonly_tools_admin_gate.py:83`
- `tests/test_edit_file.py:35`
- `tests/test_edit_file.py:39`
- `tests/test_review_regressions.py:1408`
- `tests/test_review_regressions.py:1442`
- `tests/test_review_regressions.py:1468`
- `tests/test_review_regressions.py:1496`

## `delegated_credential_blocked_tools` — function, line 297
- **called from:**
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3845`
- `routes/session_routes.py:1732`
- `src/agent_loop.py:21688`
- `src/agent_loop.py:21943`
- `src/clean_agent_preview.py:5672`
- `tests/test_api_token_tool_authority.py:631`
- `tests/test_cookbook_readonly_tools_admin_gate.py:78`
