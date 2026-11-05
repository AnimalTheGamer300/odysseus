# `src/agent_tools/admin_tools.py` — definitions & call sites

16 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_endpoints` — function (async), line 22
- **called from:**
- `src/tools/cookbook.py:1746`
- `tests/test_manage_endpoints_ssrf.py:129`
- `tests/test_manage_endpoints_ssrf.py:143`
- `tests/test_manage_endpoints_ssrf.py:162`
- `tests/test_manage_endpoints_ssrf.py:177`
- `tests/test_manage_endpoints_ssrf.py:191`
- `tests/test_manage_endpoints_ssrf.py:206`
- `tests/test_manage_endpoints_ssrf.py:220`
- `tests/test_manage_endpoints_ssrf.py:234`
- `tests/test_manage_endpoints_ssrf.py:253`

## `_mcp_allowed_commands` — function, line 149
- **called from:**
- `src/agent_tools/admin_tools.py:188`

## `_validate_mcp_command` — function, line 158
- **called from:**
- `src/agent_tools/admin_tools.py:274`
- `tests/test_manage_mcp_command_allowlist.py:74`
- `tests/test_manage_mcp_command_allowlist.py:79`
- `tests/test_manage_mcp_command_allowlist.py:84`
- `tests/test_manage_mcp_command_allowlist.py:94`
- `tests/test_manage_mcp_command_allowlist.py:102`
- `tests/test_manage_mcp_command_allowlist.py:106`
- `tests/test_manage_mcp_command_allowlist.py:110`

## `do_manage_mcp` — function (async), line 232
- **called from:**
- `tests/test_manage_mcp_command_allowlist.py:117`
- `tests/test_mcp_reconnect_args.py:33`

## `do_manage_webhooks` — function (async), line 387
- **called from:**
- `tests/test_review_regressions.py:1537`

## `do_manage_tokens` — function (async), line 459
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_manage_settings` — function (async), line 512
- **called from:**
- `tests/test_manage_settings_denylist_hard.py:40`
- `tests/test_manage_settings_token_budget.py:14`
- `tests/test_retired_settings_interfaces.py:108`
- `tests/test_retired_settings_interfaces.py:115`
- `tests/test_review_regressions.py:1038`
- `tests/test_review_regressions.py:1060`

## `_is_secret` — function, line 540
- **called from:**
- `src/agent_tools/admin_tools.py:652`
- `src/agent_tools/admin_tools.py:680`
- `src/agent_tools/admin_tools.py:713`

## `_resolve` — function, line 583
- **called from:**
- `src/agent_runtime/resource_binding.py:144`
- `src/agent_tools/admin_tools.py:664`
- `src/agent_tools/admin_tools.py:677`
- `src/agent_tools/admin_tools.py:710`
- `tests/cli/test_logs_cli_resolve_nonstring.py:12`
- `tests/cli/test_logs_cli_resolve_nonstring.py:13`
- `tests/test_compare_endpoint_owner_scope.py:80`
- `tests/test_compare_endpoint_owner_scope.py:85`
- `tests/test_compare_endpoint_owner_scope.py:91`
- `tests/test_compare_endpoint_owner_scope.py:97`
- `tests/test_compare_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:98`
- `tests/test_research_endpoint_owner_scope.py:103`
- `tests/test_research_endpoint_owner_scope.py:109`
- `tests/test_research_endpoint_owner_scope.py:115`
- `tests/test_research_endpoint_owner_scope.py:123`
- `tests/test_research_endpoint_owner_scope.py:129`
- `tests/test_research_endpoint_owner_scope.py:136`
- `tests/test_ui_visibility_js.py:86`
- `tests/test_ui_visibility_js.py:95`
- `tests/test_ui_visibility_js.py:102`
- `tests/test_ui_visibility_js.py:109`
- `tests/test_ui_visibility_js.py:114`
- `tests/test_ui_visibility_js.py:123`
- `tests/test_ui_visibility_js.py:128`
- `tests/test_ui_visibility_js.py:134`
- `tests/test_ui_visibility_js.py:139`

## `_is_managed_key` — function, line 589
- **called from:**
- `src/agent_tools/admin_tools.py:659`
- `src/agent_tools/admin_tools.py:667`
- `src/agent_tools/admin_tools.py:678`
- `src/agent_tools/admin_tools.py:711`

## `_coerce` — function, line 598
- **called from:**
- `services/skills/evaluation.py:69`
- `services/skills/evaluation.py:82`
- `src/agent_tools/admin_tools.py:690`

## `_model_slug` — function, line 605
- **called from:**
- `src/agent_tools/admin_tools.py:621`
- `src/agent_tools/admin_tools.py:622`
- `src/agent_tools/admin_tools.py:637`

## `_endpoint_model_from_cache` — function, line 609
- **called from:**
- `src/agent_tools/admin_tools.py:698`

## `_mask` — function, line 651
- **called from:**
- `src/agent_tools/admin_tools.py:657`
- `src/agent_tools/admin_tools.py:670`
- `src/agent_tools/admin_tools.py:670`

## `_owner_adapter` — function, line 832
- **called from:**
- `src/agent_tools/admin_tools.py:840`
- `src/agent_tools/admin_tools.py:841`
- `src/agent_tools/admin_tools.py:842`
- `src/agent_tools/admin_tools.py:843`
- `src/agent_tools/admin_tools.py:844`
- `tests/test_admin_tools_registry.py:43`
- `tests/test_admin_tools_registry.py:56`

## `_execute` — function (async), line 834
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
