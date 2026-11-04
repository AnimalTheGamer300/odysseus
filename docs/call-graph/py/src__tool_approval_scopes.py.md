# `src/tool_approval_scopes.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_grant_key` — function, line 30
- **called from:**
- `src/tool_approval_scopes.py:52`

## `sign_chat_session_grant` — function, line 45
- **called from:**
- `src/tool_approval_scopes.py:110`
- `src/tool_approval_scopes.py:139`

## `sanitize_client_message_metadata` — function, line 74
- **called from:**
- `routes/history/history_routes.py:465`
- `routes/session_routes.py:716`
- `tests/test_api_token_tool_authority.py:283`
- `tests/test_api_token_tool_authority.py:297`
- `tests/test_api_token_tool_authority.py:298`

## `stamp_chat_session_grant` — function, line 94
- **called from:**
- `routes/chat_routes.py:142`
- `tests/test_api_token_tool_authority.py:70`
- `tests/test_api_token_tool_authority.py:93`
- `tests/test_api_token_tool_authority.py:312`
- `tests/test_tool_approval_task_scope.py:117`

## `verify_chat_session_grant` — function, line 119
- **called from:**
- `core/models.py:67`
- `tests/test_api_token_tool_authority.py:123`

## `ToolApprovalScope` — class, line 145
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `scope_for_decision` — function, line 154
- **called from:**
- `src/tool_approvals.py:461`
