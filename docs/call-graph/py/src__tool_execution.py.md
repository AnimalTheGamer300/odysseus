# `src/tool_execution.py` — definitions & call sites

52 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_MissingToolSecurityContext` — class, line 62
- **called from:**
- `src/tool_execution.py:70`

## `_NoToolSecurityContext` — class, line 66
- **called from:**
- `src/tool_execution.py:71`

## `AgentExecutionBridge` — class, line 88
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/chat_routes.py:848`
- `tests/test_agent_external_tool_schemas.py:358`
- `tests/test_agent_external_tool_schemas.py:426`
- `tests/test_api_token_tool_authority.py:133`
- `tests/test_api_token_tool_authority.py:259`
- `tests/test_api_token_tool_authority.py:364`
- `tests/test_execution_bridge.py:63`
- `tests/test_execution_bridge.py:112`
- `tests/test_execution_bridge.py:144`
- `tests/test_execution_bridge.py:173`
- `tests/test_execution_bridge.py:193`
- `tests/test_execution_bridge.py:260`
- `tests/test_remote_resource_identity.py:238`
- `tests/test_request_authority.py:39`
- `tests/test_turn_contract_integration.py:111`
- `tests/test_turn_contract_integration.py:112`
- `tests/test_turn_contract_integration.py:144`
- `tests/test_turn_contract_integration.py:145`

## `AgentExecutionBridge.__post_init__` — method, line 103
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AgentExecutionBridge.resource_identity` — method, line 109
- **called from:**
- `src/agent_runtime/authority.py:428`
- `src/agent_runtime/remote_resources.py:111`
- `src/agent_runtime/remote_resources.py:135`
- `src/mcp_manager.py:589`
- `src/tool_capabilities.py:1002`
- `src/tool_capabilities.py:1053`
- `tests/test_agent_external_tool_schemas.py:439`
- `tests/test_agent_external_tool_schemas.py:440`

## `bind_execution_bridge` — function, line 122
- decorator: `contextmanager`
- **called from:**
- `routes/chat_routes.py:863`
- `tests/test_agent_external_tool_schemas.py:364`
- `tests/test_agent_external_tool_schemas.py:436`
- `tests/test_api_token_tool_authority.py:133`
- `tests/test_api_token_tool_authority.py:259`
- `tests/test_api_token_tool_authority.py:368`
- `tests/test_execution_bridge.py:65`
- `tests/test_execution_bridge.py:119`
- `tests/test_execution_bridge.py:149`
- `tests/test_execution_bridge.py:176`
- `tests/test_execution_bridge.py:200`
- `tests/test_execution_bridge.py:265`
- `tests/test_remote_resource_identity.py:240`
- `tests/test_remote_resource_identity.py:252`
- `tests/test_remote_resource_identity.py:286`
- `tests/test_request_authority.py:39`
- `tests/test_turn_contract_integration.py:118`
- `tests/test_turn_contract_integration.py:160`

## `get_active_execution_bridge` — function, line 134
- **called from:**
- `src/agent_loop.py:21967`
- `src/agent_runtime/remote_resources.py:109`
- `src/tool_execution.py:2156`
- `tests/test_execution_bridge.py:120`
- `tests/test_execution_bridge.py:134`
- `tests/test_execution_bridge.py:141`
- `tests/test_execution_bridge.py:162`
- `tests/test_turn_contract_integration.py:117`
- `tests/test_turn_contract_integration.py:125`
- `tests/test_turn_contract_integration.py:128`
- `tests/test_turn_contract_integration.py:129`
- `tests/test_turn_contract_integration.py:151`
- `tests/test_turn_contract_integration.py:159`
- `tests/test_turn_contract_integration.py:173`
- `tests/test_turn_contract_integration.py:176`

## `_tui_host_bridge_endpoint_url` — function, line 138
- **called from:**
- `src/tool_execution.py:164`
- `src/tool_execution.py:240`
- `src/tool_execution.py:307`

## `_tui_host_bridge_patch_url` — function, line 144
- **called from:**
- `src/agent_runtime/remote_resources.py:47`
- `src/tool_execution.py:171`
- `src/tool_execution.py:2289`
- `src/tool_execution.py:2328`
- `tests/test_tool_execution_bridge_security.py:120`
- `tests/test_tool_execution_bridge_security.py:201`
- `tests/test_tool_execution_bridge_security.py:204`
- `tests/test_tui_host_patch.py:10`
- `tests/test_tui_host_patch.py:20`

## `_apply_patch_via_tui_host_bridge` — function (async), line 167
- **called from:**
- `src/tool_execution.py:2331`
- `tests/test_tool_execution_bridge_security.py:64`
- `tests/test_tool_execution_bridge_security.py:122`
- `tests/test_tool_execution_bridge_security.py:146`
- `tests/test_tool_execution_bridge_security.py:181`
- `tests/test_tool_execution_bridge_security.py:310`
- `tests/test_tui_host_patch.py:51`
- `tests/test_tui_host_patch.py:91`
- `tests/test_tui_host_patch.py:137`
- `tests/test_tui_host_patch.py:178`
- `tests/test_tui_host_patch.py:214`
- `tests/test_tui_host_patch.py:248`

## `_bridge_post` — function (async), line 231
- **called from:**
- `src/tool_execution.py:409`
- `src/tool_execution.py:423`
- `src/tool_execution.py:450`
- `src/tool_execution.py:501`
- `src/tool_execution.py:542`
- `src/tool_execution.py:594`
- `src/tool_execution.py:653`
- `src/tool_execution.py:705`
- `src/tool_execution.py:765`
- `tests/test_client_tool_routing.py:647`
- `tests/test_client_tool_routing.py:673`
- `tests/test_client_tool_routing.py:714`
- `tests/test_client_tool_routing.py:715`
- `tests/test_client_tool_routing.py:753`
- `tests/test_client_tool_routing.py:756`
- `tests/test_client_tool_routing.py:788`
- `tests/test_client_tool_routing.py:823`
- `tests/test_client_tool_routing.py:859`
- `tests/test_tool_execution_bridge_security.py:66`
- `tests/test_tool_execution_bridge_security.py:123`
- `tests/test_tool_execution_bridge_security.py:148`
- `tests/test_tool_execution_bridge_security.py:311`

## `_cancel_bridge_request` — function (async), line 300
- **called from:**
- `src/tool_execution.py:221`
- `src/tool_execution.py:287`
- `tests/test_tool_execution_bridge_security.py:40`
- `tests/test_tool_execution_bridge_security.py:69`
- `tests/test_tool_execution_bridge_security.py:125`
- `tests/test_tool_execution_bridge_security.py:151`
- `tests/test_tool_execution_bridge_security.py:313`

## `_client_bridge` — function, line 321
- **called from:**
- `src/agent_runtime/remote_resources.py:46`
- `src/tool_execution.py:377`
- `src/tool_execution.py:2241`
- `tests/test_client_tool_routing.py:47`
- `tests/test_client_tool_routing.py:48`
- `tests/test_client_tool_routing.py:49`
- `tests/test_client_tool_routing.py:53`
- `tests/test_client_tool_routing.py:54`
- `tests/test_client_tool_routing.py:55`
- `tests/test_client_tool_routing.py:56`
- `tests/test_tool_execution_bridge_security.py:121`

## `_text_write_to_binary_artifact_result` — function, line 350
- **called from:**
- `src/tool_execution.py:751`
- `src/tool_execution.py:2197`

## `_route_tool_via_bridge` — function (async), line 374
- **called from:**
- `src/tool_execution.py:2242`
- `tests/test_execution_bridge.py:31`
- `tests/test_execution_bridge.py:51`
- `tests/test_execution_bridge.py:233`
- `tests/test_tui_host_edit_routing.py:17`
- `tests/test_tui_host_edit_routing.py:58`

## `_path_within` — function, line 810
- **called from:**
- `src/agent_tools/filesystem_tools.py:1014`
- `src/agent_tools/filesystem_tools.py:1028`
- `src/agent_tools/filesystem_tools.py:1060`
- `src/tool_execution.py:926`
- `src/tool_execution.py:927`
- `src/tool_execution.py:953`
- `src/tool_execution.py:990`

## `_path_within_conservative` — function, line 844
- **called from:**
- `src/tool_execution.py:950`

## `_agent_readable_data_subdirs` — function, line 855
- **called from:**
- `src/tool_execution.py:954`
- `src/tool_execution.py:991`
- `src/tool_execution.py:1004`
- `src/tool_execution.py:1269`
- `tests/test_agent_state_dir_confinement.py:533`
- `tests/test_agent_state_dir_confinement.py:545`
- `tests/test_agent_state_dir_confinement.py:549`
- `tests/test_agent_state_dir_confinement.py:652`
- `tests/test_agent_state_dir_confinement.py:715`
- `tests/test_agent_state_dir_confinement.py:737`

## `_is_app_state_path` — function, line 935
- **called from:**
- `src/agent_runtime/resources.py:143`
- `src/tool_execution.py:976`
- `src/tool_execution.py:986`
- `src/tool_execution.py:1077`
- `src/tool_execution.py:1127`

## `_is_hardlinked_regular_file` — function, line 958
- **called from:**
- `src/agent_runtime/resources.py:143`
- `src/tool_execution.py:977`
- `src/tool_execution.py:1086`
- `src/tool_execution.py:1136`

## `_is_denied_tool_path` — function, line 967
- **called from:**
- `src/agent_tools/filesystem_tools.py:814`
- `src/agent_tools/filesystem_tools.py:892`
- `src/agent_tools/filesystem_tools.py:922`
- `src/agent_tools/filesystem_tools.py:1014`
- `src/agent_tools/filesystem_tools.py:1065`
- `src/tool_execution.py:1062`
- `src/tool_execution.py:1089`
- `src/tool_execution.py:1139`
- `src/tool_execution.py:1234`
- `src/tool_execution.py:1292`
- `src/tool_execution.py:1305`

## `_can_traverse_tool_path` — function, line 982
- **called from:**
- `src/agent_tools/filesystem_tools.py:903`
- `src/agent_tools/filesystem_tools.py:914`
- `src/agent_tools/filesystem_tools.py:1049`
- `src/agent_tools/filesystem_tools.py:1064`

## `_tool_path_roots` — function, line 995
- **called from:**
- `src/tool_execution.py:1092`
- `src/tool_execution.py:1303`
- `tests/test_agent_state_dir_confinement.py:586`

## `_resolve_tool_path` — function, line 1044
- **called from:**
- `routes/chat_helpers.py:891`
- `src/agent_tools/filesystem_tools.py:232`
- `src/agent_tools/filesystem_tools.py:297`
- `src/agent_tools/filesystem_tools.py:426`
- `src/agent_tools/filesystem_tools.py:579`
- `src/agent_tools/web_tools.py:844`
- `src/agent_tools/web_tools.py:2570`
- `src/agent_tools/web_tools_prewave3.py:848`
- `src/agent_tools/web_tools_prewave3.py:2603`
- `src/tool_execution.py:1308`
- `tests/test_agent_state_dir_confinement.py:78`
- `tests/test_agent_state_dir_confinement.py:123`
- `tests/test_agent_state_dir_confinement.py:136`
- `tests/test_agent_state_dir_confinement.py:154`
- `tests/test_agent_state_dir_confinement.py:219`
- `tests/test_agent_state_dir_confinement.py:238`
- `tests/test_agent_state_dir_confinement.py:300`
- `tests/test_agent_state_dir_confinement.py:361`
- `tests/test_agent_state_dir_confinement.py:381`
- `tests/test_agent_state_dir_confinement.py:387`
- `tests/test_agent_state_dir_confinement.py:411`
- `tests/test_agent_state_dir_confinement.py:422`
- `tests/test_agent_state_dir_confinement.py:428`
- `tests/test_agent_state_dir_confinement.py:452`
- `tests/test_agent_state_dir_confinement.py:458`
- `tests/test_agent_state_dir_confinement.py:463`
- `tests/test_agent_state_dir_confinement.py:475`
- `tests/test_agent_state_dir_confinement.py:538`
- `tests/test_agent_state_dir_confinement.py:540`
- `tests/test_agent_state_dir_confinement.py:583`
- `tests/test_agent_state_dir_confinement.py:655`
- `tests/test_agent_state_dir_confinement.py:670`
- `tests/test_agent_state_dir_confinement.py:687`
- `tests/test_agent_state_dir_confinement.py:717`
- `tests/test_agent_state_dir_confinement.py:1015`
- `tests/test_resource_identity.py:439`
- `tests/test_resource_identity.py:441`
- `tests/test_resource_identity.py:445`
- `tests/test_resource_identity.py:447`
- `tests/test_tool_path_confinement.py:100`
- `tests/test_tool_path_confinement.py:106`
- `tests/test_tool_path_confinement.py:112`
- `tests/test_tool_path_confinement.py:120`
- `tests/test_tool_path_confinement.py:127`
- `tests/test_tool_path_confinement.py:142`
- `tests/test_tool_path_confinement.py:150`
- `tests/test_tool_path_confinement.py:156`
- `tests/test_tool_path_confinement.py:162`
- `tests/test_tool_path_confinement.py:168`
- `tests/test_tool_path_confinement.py:174`
- `tests/test_tool_path_confinement.py:188`
- `tests/test_tool_path_confinement.py:201`
- `tests/test_tool_path_confinement.py:208`
- `tests/test_tool_path_confinement.py:210`
- `tests/test_tool_path_confinement.py:223`
- `tests/test_tool_path_confinement.py:234`
- `tests/test_workspace_confine.py:92`
- `tests/test_workspace_confine.py:94`
- `tests/test_workspace_confine.py:104`

## `_resolve_tool_path_in_workspace` — function, line 1100
- **called from:**
- `src/agent_loop.py:17139`
- `src/tool_execution.py:1067`
- `src/tool_execution.py:1301`
- `tests/test_workspace_artifact_tool_floor.py:1810`
- `tests/test_workspace_confine.py:67`
- `tests/test_workspace_confine.py:68`
- `tests/test_workspace_confine.py:71`
- `tests/test_workspace_confine.py:73`
- `tests/test_workspace_confine.py:79`

## `get_active_user_text` — function, line 1187
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_active_workspace` — function, line 1192
- **called from:**
- `src/agent_tools/filesystem_tools.py:1358`
- `src/agent_tools/media_tools.py:152`
- `src/agent_tools/media_tools.py:2206`
- `src/tool_execution.py:1065`
- `src/tool_execution.py:1201`
- `src/tool_execution.py:1256`
- `src/tool_execution.py:1296`
- `tests/test_resource_identity.py:487`
- `tests/test_resource_identity.py:511`
- `tests/test_workspace_confine.py:90`
- `tests/test_workspace_confine.py:101`
- `tests/test_workspace_confine.py:325`

## `_display_tool_path` — function, line 1197
- **called from:**
- `src/agent_tools/filesystem_tools.py:541`
- `src/agent_tools/filesystem_tools.py:542`
- `src/agent_tools/filesystem_tools.py:826`
- `src/agent_tools/filesystem_tools.py:941`
- `src/agent_tools/filesystem_tools.py:942`
- `src/agent_tools/filesystem_tools.py:1099`
- `src/agent_tools/filesystem_tools.py:1319`
- `src/agent_tools/filesystem_tools.py:1342`
- `src/agent_tools/filesystem_tools.py:1344`
- `src/agent_tools/web_tools.py:1823`
- `src/agent_tools/web_tools_prewave3.py:1827`

## `vet_workspace` — function, line 1217
- **called from:**
- `routes/chat_routes.py:1861`
- `routes/chat_routes.py:1909`
- `routes/session_routes.py:148`
- `routes/workspace_routes.py:65`
- `routes/workspace_routes.py:82`
- `routes/workspace_routes.py:104`
- `src/agent_runtime/completion.py:224`
- `src/tool_execution.py:1253`
- `src/tool_execution.py:1258`
- `src/tool_execution.py:1269`
- `src/tool_execution.py:1933`
- `tests/test_agent_state_dir_confinement.py:401`
- `tests/test_agent_state_dir_confinement.py:406`
- `tests/test_workspace_confine.py:509`
- `tests/test_workspace_confine.py:519`
- `tests/test_workspace_confine.py:524`
- `tests/test_workspace_confine.py:525`
- `tests/test_workspace_confine.py:526`
- `tests/test_workspace_confine.py:527`
- `tests/test_workspace_confine.py:534`

## `agent_cwd` — function, line 1245
- **called from:**
- `src/agent_tools/subprocess_tools.py:529`
- `src/agent_tools/subprocess_tools.py:534`
- `src/agent_tools/subprocess_tools.py:638`
- `src/agent_tools/subprocess_tools.py:661`
- `src/agent_tools/subprocess_tools.py:710`
- `src/agent_tools/subprocess_tools.py:934`
- `src/agent_tools/subprocess_tools.py:938`
- `src/tool_execution.py:385`
- `src/tool_execution.py:2255`
- `tests/process_resource_helpers.py:94`
- `tests/test_agent_state_dir_confinement.py:469`
- `tests/test_agent_state_dir_confinement.py:537`
- `tests/test_workspace_confine.py:91`
- `tests/test_workspace_confine.py:102`

## `default_agent_workspace` — function, line 1265
- **called from:**
- `src/agent_runtime/authority.py:154`
- `src/tool_approvals.py:433`
- `src/tool_approvals.py:464`
- `src/tool_execution.py:1262`

## `get_mcp_manager` — function, line 1274
- **called from:**
- `routes/chat_routes.py:3842`
- `routes/task/task_routes.py:1075`
- `scripts/dump_agent_prompt.py:391`
- `scripts/ody_eval_email_fixture.py:36`
- `src/agent_loop.py:21466`
- `src/agent_loop.py:21880`
- `src/agent_runtime/authority.py:390`
- `src/agent_runtime/authority.py:506`
- `src/agent_runtime/remote_resources.py:134`
- `src/agent_tools/admin_tools.py:242`
- `src/agent_tools/admin_tools.py:289`
- `src/agent_tools/admin_tools.py:313`
- `src/agent_tools/admin_tools.py:327`
- `src/agent_tools/admin_tools.py:371`
- `src/task_scheduler.py:1602`
- `src/task_scheduler.py:2388`
- `src/tool_capabilities.py:382`
- `src/tool_capabilities.py:389`
- `src/tool_execution.py:1276`
- `src/tool_execution.py:1488`
- `src/tool_execution.py:2497`
- `src/tool_execution.py:2544`
- `tests/test_local_mcp_capabilities.py:228`
- `tests/test_local_mcp_capabilities.py:410`
- `tests/test_local_mcp_capabilities.py:436`
- `tests/test_local_mcp_capabilities.py:512`
- `tests/test_local_mcp_capabilities.py:748`
- `tests/test_local_mcp_capabilities.py:774`
- `tests/test_product_turn_contract_route.py:21`
- `tests/test_product_turn_contract_route.py:33`

## `_resolve_search_root` — function, line 1281
- **called from:**
- `src/agent_tools/filesystem_tools.py:799`
- `src/agent_tools/filesystem_tools.py:865`
- `src/agent_tools/filesystem_tools.py:981`
- `tests/test_agent_state_dir_confinement.py:157`
- `tests/test_agent_state_dir_confinement.py:305`
- `tests/test_agent_state_dir_confinement.py:395`
- `tests/test_agent_state_dir_confinement.py:536`
- `tests/test_agent_state_dir_confinement.py:585`
- `tests/test_resource_identity.py:444`
- `tests/test_workspace_confine.py:95`

## `_owner_is_admin` — function, line 1338
- **called from:**
- `src/tool_execution.py:2150`
- `src/tool_execution.py:2179`

## `_parse_qualified_mcp_args` — function, line 1360
- **called from:**
- `src/tool_execution.py:2547`

## `_parse_generate_image` — function, line 1378
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_parse_manage_memory` — function, line 1387
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_parse_write_file` — function, line 1408
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_build_mcp_args` — function, line 1451
- **called from:**
- `src/tool_execution.py:1496`
- `tests/test_generate_image_native_schema.py:40`
- `tests/test_image_creation_routing.py:187`
- `tests/test_review_regressions.py:1156`
- `tests/test_review_regressions.py:1159`
- `tests/test_review_regressions.py:1162`

## `_normalize_mcp_text_error` — function, line 1468
- **called from:**
- `src/task_scheduler.py:2439`
- `src/tool_execution.py:1506`
- `src/tool_execution.py:2562`
- `tests/test_mcp_text_error_normalization.py:5`
- `tests/test_mcp_text_error_normalization.py:16`

## `_call_mcp_tool` — function (async), line 1478
- **called from:**
- `src/tool_execution.py:2315`
- `tests/test_generated_image_ownership.py:328`
- `tests/test_generated_image_ownership.py:342`
- `tests/test_generated_image_ownership.py:364`
- `tests/test_generated_image_ownership.py:387`
- `tests/test_generated_image_ownership.py:392`
- `tests/test_generated_image_ownership.py:447`
- `tests/test_generated_image_ownership.py:451`
- `tests/test_promote_image_fields.py:74`

## `_promote_image_fields` — function, line 1525
- **called from:**
- `src/tool_execution.py:1520`
- `src/tool_execution.py:2564`
- `tests/test_promote_image_fields.py:30`
- `tests/test_promote_image_fields.py:43`
- `tests/test_promote_image_fields.py:51`
- `tests/test_promote_image_fields.py:59`

## `_split_bg_marker` — function, line 1551
- **called from:**
- `src/bg_jobs.py:97`
- `src/tool_execution.py:397`
- `src/tool_execution.py:2249`

## `_agent_subprocess_env` — function, line 1583
- **called from:**
- `src/agent_runtime/process_resources.py:58`
- `src/agent_tools/subprocess_tools.py:512`
- `src/tool_execution.py:1603`
- `src/tool_execution.py:1630`
- `src/tool_execution.py:2255`
- `tests/test_wave3_subprocess_environment.py:11`

## `_legacy_private_browser_enabled` — function, line 1595
- **called from:**
- `src/tool_execution.py:1804`
- `tests/test_legacy_browser_authority.py:14`

## `_legacy_private_browser` — function (async), line 1599
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_direct_fallback` — function (async), line 1620
- **called from:**
- `src/tool_execution.py:1487`
- `src/tool_execution.py:1492`
- `src/tool_execution.py:1510`
- `src/tool_execution.py:2299`
- `src/tool_execution.py:2309`
- `src/tool_execution.py:2320`
- `src/tool_execution.py:2335`
- `src/tool_execution.py:2340`
- `src/tool_execution.py:2411`
- `src/tool_execution.py:2470`
- `src/tool_execution.py:2573`
- `tests/test_code_nav_tools.py:14`

## `_document_tool_dispatch` — function (async), line 1659
- **called from:**
- `src/tool_execution.py:2345`
- `src/tool_execution.py:2369`
- `src/tool_execution.py:2378`
- `src/tool_execution.py:2385`
- `src/tool_execution.py:2393`

## `execute_tool_block` — function (async), line 1707
- decorator: `record_action`
- **called from:**
- `src/agent_loop.py:594`
- `src/agent_loop.py:22171`
- `src/agent_loop.py:22280`
- `src/agent_loop.py:22597`
- `src/agent_loop.py:26000`
- `src/agent_loop.py:27237`
- `src/agent_loop.py:27437`
- `src/agent_loop.py:27559`
- `src/agent_loop.py:27871`
- `src/agent_loop.py:27942`
- `src/agent_loop.py:34652`
- `src/agent_loop.py:35963`
- `src/agent_loop.py:38358`
- `src/clean_agent_preview.py:7170`
- `src/clean_agent_preview.py:7875`
- `tests/test_api_token_tool_authority.py:33`
- `tests/test_api_token_tool_authority.py:136`
- `tests/test_api_token_tool_authority.py:262`
- `tests/test_ask_user_tool.py:20`
- `tests/test_background_containment.py:101`
- `tests/test_client_tool_routing.py:101`
- `tests/test_client_tool_routing.py:125`
- `tests/test_client_tool_routing.py:147`
- `tests/test_client_tool_routing.py:169`
- `tests/test_client_tool_routing.py:197`
- `tests/test_client_tool_routing.py:217`
- `tests/test_client_tool_routing.py:238`
- `tests/test_client_tool_routing.py:261`
- `tests/test_client_tool_routing.py:285`
- `tests/test_client_tool_routing.py:308`
- `tests/test_client_tool_routing.py:333`
- `tests/test_client_tool_routing.py:353`
- `tests/test_client_tool_routing.py:382`
- `tests/test_client_tool_routing.py:401`
- `tests/test_client_tool_routing.py:426`
- `tests/test_client_tool_routing.py:445`
- `tests/test_client_tool_routing.py:457`
- `tests/test_client_tool_routing.py:483`
- `tests/test_client_tool_routing.py:507`
- `tests/test_client_tool_routing.py:529`
- `tests/test_client_tool_routing.py:533`
- `tests/test_client_tool_routing.py:556`
- `tests/test_client_tool_routing.py:593`
- `tests/test_client_tool_routing.py:1235`
- `tests/test_cookbook_readonly_tools_admin_gate.py:104`
- `tests/test_cookbook_readonly_tools_admin_gate.py:126`
- `tests/test_edit_file.py:60`
- `tests/test_effect_resource_bindings.py:41`
- `tests/test_effect_resource_bindings.py:460`
- `tests/test_exact_approval_ungranted_process.py:39`
- `tests/test_execution_bridge.py:68`
- `tests/test_execution_bridge.py:93`
- `tests/test_execution_bridge.py:121`
- `tests/test_execution_bridge.py:150`
- `tests/test_execution_bridge.py:177`
- `tests/test_execution_bridge.py:201`
- `tests/test_execution_bridge.py:266`
- `tests/test_external_context_tool_gate.py:848`
- `tests/test_external_context_tool_gate.py:863`
- `tests/test_external_context_tool_gate.py:880`
- … +83 more (grep the name in repo)

## `_execute_tool_block_impl` — function (async), line 2032
- **called from:**
- `src/tool_execution.py:1999`
- `tests/test_generated_image_ownership.py:412`
- `tests/test_generated_image_ownership.py:420`

## `_compact_binary_like_output` — function, line 2626
- **called from:**
- `src/tool_execution.py:2663`
- `src/tool_execution.py:2667`
- `src/tool_execution.py:2672`
- `src/tool_execution.py:2678`

## `format_tool_result` — function, line 2646
- **called from:**
- `src/agent_loop.py:26415`
- `src/agent_loop.py:36473`
- `src/agent_loop.py:38404`
- `tests/test_agent_loop_tool_output_truncation.py:50`
- `tests/test_agent_loop_tool_output_truncation.py:60`
- `tests/test_document_read_pagination.py:48`
- `tests/test_document_read_pagination.py:65`
- `tests/test_document_read_pagination.py:85`
- `tests/test_external_context_tool_gate.py:220`
- `tests/test_external_context_tool_gate.py:245`
- `tests/test_host_shell_polling.py:63`
- `tests/test_tool_result_binary_compaction.py:7`
- `tests/test_tool_result_binary_compaction.py:20`
