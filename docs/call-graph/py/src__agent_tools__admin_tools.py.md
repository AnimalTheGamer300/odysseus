# `src/agent_tools/admin_tools.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_endpoints` — function (async), line 22
- **called from:**
- `src/tools/cookbook.py:1358`

## `_mcp_allowed_commands` — function, line 135
- **called from:**
- `src/agent_tools/admin_tools.py:174`

## `_validate_mcp_command` — function, line 144
- **called from:**
- `src/agent_tools/admin_tools.py:260`
- `tests/test_manage_mcp_command_allowlist.py:74`
- `tests/test_manage_mcp_command_allowlist.py:79`
- `tests/test_manage_mcp_command_allowlist.py:84`
- `tests/test_manage_mcp_command_allowlist.py:94`
- `tests/test_manage_mcp_command_allowlist.py:102`
- `tests/test_manage_mcp_command_allowlist.py:106`
- `tests/test_manage_mcp_command_allowlist.py:110`

## `do_manage_mcp` — function (async), line 218
- **called from:**
- `tests/test_manage_mcp_command_allowlist.py:117`
- `tests/test_mcp_reconnect_args.py:33`

## `do_manage_webhooks` — function (async), line 373
- **called from:**
- `tests/test_review_regressions.py:1292`

## `do_manage_tokens` — function (async), line 445
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_manage_settings` — function (async), line 498
- **called from:**
- `tests/test_manage_settings_token_budget.py:14`
- `tests/test_retired_settings_interfaces.py:107`
- `tests/test_retired_settings_interfaces.py:114`
- `tests/test_review_regressions.py:829`
- `tests/test_review_regressions.py:849`

## `_is_secret` — function, line 526
- **called from:**
- `src/agent_tools/admin_tools.py:633`
- `src/agent_tools/admin_tools.py:661`
- `src/agent_tools/admin_tools.py:694`

## `_resolve` — function, line 566
- **called from:**
- `src/agent_tools/admin_tools.py:645`
- `src/agent_tools/admin_tools.py:658`
- `src/agent_tools/admin_tools.py:691`
- `tests/cli/test_logs_cli_resolve_nonstring.py:12`
- `tests/cli/test_logs_cli_resolve_nonstring.py:13`
- `tests/test_compare_endpoint_owner_scope.py:80`
- `tests/test_compare_endpoint_owner_scope.py:85`
- `tests/test_compare_endpoint_owner_scope.py:91`
- `tests/test_compare_endpoint_owner_scope.py:97`
- `tests/test_compare_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:92`
- `tests/test_research_endpoint_owner_scope.py:97`
- `tests/test_research_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:109`
- `tests/test_research_endpoint_owner_scope.py:117`
- `tests/test_research_endpoint_owner_scope.py:123`
- `tests/test_research_endpoint_owner_scope.py:130`
- `tests/test_ui_visibility_js.py:85`
- `tests/test_ui_visibility_js.py:94`
- `tests/test_ui_visibility_js.py:101`
- `tests/test_ui_visibility_js.py:108`
- `tests/test_ui_visibility_js.py:113`
- `tests/test_ui_visibility_js.py:122`
- `tests/test_ui_visibility_js.py:127`
- `tests/test_ui_visibility_js.py:133`
- `tests/test_ui_visibility_js.py:138`

## `_is_managed_key` — function, line 572
- **called from:**
- `src/agent_tools/admin_tools.py:640`
- `src/agent_tools/admin_tools.py:648`
- `src/agent_tools/admin_tools.py:659`
- `src/agent_tools/admin_tools.py:692`

## `_coerce` — function, line 579
- **called from:**
- `routes/skills_routes.py:203`
- `routes/skills_routes.py:216`
- `src/agent_tools/admin_tools.py:671`

## `_model_slug` — function, line 586
- **called from:**
- `src/agent_tools/admin_tools.py:602`
- `src/agent_tools/admin_tools.py:603`
- `src/agent_tools/admin_tools.py:618`

## `_endpoint_model_from_cache` — function, line 590
- **called from:**
- `src/agent_tools/admin_tools.py:679`

## `_mask` — function, line 632
- **called from:**
- `src/agent_tools/admin_tools.py:638`
- `src/agent_tools/admin_tools.py:651`
- `src/agent_tools/admin_tools.py:651`

## `_owner_adapter` — function, line 793
- **called from:**
- `src/agent_tools/admin_tools.py:801`
- `src/agent_tools/admin_tools.py:802`
- `src/agent_tools/admin_tools.py:803`
- `src/agent_tools/admin_tools.py:804`
- `src/agent_tools/admin_tools.py:805`
- `tests/test_admin_tools_registry.py:43`
- `tests/test_admin_tools_registry.py:56`

## `_execute` — function (async), line 795
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
