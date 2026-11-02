# `src/tool_execution.py` — definitions & call sites

33 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_MissingToolSecurityContext` — class, line 43
- **called from:**
- `src/tool_execution.py:51`

## `_NoToolSecurityContext` — class, line 47
- **called from:**
- `src/tool_execution.py:52`

## `_is_sensitive_path` — function, line 109
- **called from:**
- `src/agent_tools/filesystem_tools.py:737`
- `src/tool_execution.py:249`
- `src/tool_execution.py:290`
- `src/tool_execution.py:298`
- `src/tool_execution.py:380`
- `src/tool_execution.py:421`
- `src/tool_execution.py:500`
- `tests/test_tool_path_confinement.py:31`
- `tests/test_tool_path_confinement.py:32`
- `tests/test_tool_path_confinement.py:37`
- `tests/test_tool_path_confinement.py:42`
- `tests/test_tool_path_confinement.py:43`
- `tests/test_tool_path_confinement.py:44`
- `tests/test_tool_path_confinement.py:49`
- `tests/test_tool_path_confinement.py:50`
- `tests/test_tool_path_confinement.py:51`
- `tests/test_tool_path_confinement.py:56`
- `tests/test_tool_path_confinement.py:57`
- `tests/test_tool_path_confinement.py:68`
- `tests/test_tool_path_confinement.py:69`
- `tests/test_tool_path_confinement.py:71`
- `tests/test_tool_path_confinement.py:72`
- `tests/test_tool_path_confinement.py:73`
- `tests/test_tool_path_confinement.py:74`
- `tests/test_tool_path_confinement.py:76`
- `tests/test_tool_path_confinement.py:78`

## `_path_within` — function, line 130
- **called from:**
- `src/agent_tools/filesystem_tools.py:726`
- `src/agent_tools/filesystem_tools.py:733`
- `src/agent_tools/filesystem_tools.py:766`
- `src/agent_tools/filesystem_tools.py:767`
- `src/agent_tools/filesystem_tools.py:808`
- `src/agent_tools/filesystem_tools.py:997`
- `src/tool_execution.py:246`
- `src/tool_execution.py:247`
- `src/tool_execution.py:273`
- `src/tool_execution.py:303`

## `_path_within_conservative` — function, line 164
- **called from:**
- `src/tool_execution.py:270`

## `_agent_readable_data_subdirs` — function, line 175
- **called from:**
- `src/agent_tools/filesystem_tools.py:764`
- `src/tool_execution.py:274`
- `src/tool_execution.py:304`
- `src/tool_execution.py:317`
- `src/tool_execution.py:522`
- `tests/test_agent_state_dir_confinement.py:382`
- `tests/test_agent_state_dir_confinement.py:394`
- `tests/test_agent_state_dir_confinement.py:398`
- `tests/test_agent_state_dir_confinement.py:501`
- `tests/test_agent_state_dir_confinement.py:564`
- `tests/test_agent_state_dir_confinement.py:586`

## `_is_app_state_path` — function, line 255
- **called from:**
- `src/tool_execution.py:291`
- `src/tool_execution.py:300`
- `src/tool_execution.py:385`
- `src/tool_execution.py:426`
- `src/tool_execution.py:504`

## `_is_hardlinked_regular_file` — function, line 278
- **called from:**
- `src/tool_execution.py:292`
- `src/tool_execution.py:389`
- `src/tool_execution.py:430`

## `_is_denied_tool_path` — function, line 287
- **called from:**
- `src/agent_tools/filesystem_tools.py:547`
- `src/agent_tools/filesystem_tools.py:626`
- `src/agent_tools/filesystem_tools.py:655`
- `src/agent_tools/filesystem_tools.py:737`
- `src/agent_tools/filesystem_tools.py:808`
- `src/agent_tools/filesystem_tools.py:997`
- `src/tool_execution.py:552`

## `_can_traverse_tool_path` — function, line 296
- **called from:**
- `src/agent_tools/filesystem_tools.py:636`
- `src/agent_tools/filesystem_tools.py:647`

## `_tool_path_roots` — function, line 308
- **called from:**
- `src/tool_execution.py:392`
- `src/tool_execution.py:550`
- `tests/test_agent_state_dir_confinement.py:435`

## `_resolve_tool_path` — function, line 357
- **called from:**
- `routes/chat_helpers.py:423`
- `src/agent_tools/filesystem_tools.py:196`
- `src/agent_tools/filesystem_tools.py:256`
- `src/agent_tools/filesystem_tools.py:314`
- `src/agent_tools/filesystem_tools.py:371`
- `src/tool_execution.py:555`
- `tests/test_agent_state_dir_confinement.py:78`
- `tests/test_agent_state_dir_confinement.py:85`
- `tests/test_agent_state_dir_confinement.py:93`
- `tests/test_agent_state_dir_confinement.py:105`
- `tests/test_agent_state_dir_confinement.py:124`
- `tests/test_agent_state_dir_confinement.py:151`
- `tests/test_agent_state_dir_confinement.py:212`
- `tests/test_agent_state_dir_confinement.py:232`
- `tests/test_agent_state_dir_confinement.py:238`
- `tests/test_agent_state_dir_confinement.py:262`
- `tests/test_agent_state_dir_confinement.py:273`
- `tests/test_agent_state_dir_confinement.py:279`
- `tests/test_agent_state_dir_confinement.py:301`
- `tests/test_agent_state_dir_confinement.py:307`
- `tests/test_agent_state_dir_confinement.py:312`
- `tests/test_agent_state_dir_confinement.py:324`
- `tests/test_agent_state_dir_confinement.py:387`
- `tests/test_agent_state_dir_confinement.py:389`
- `tests/test_agent_state_dir_confinement.py:432`
- `tests/test_agent_state_dir_confinement.py:504`
- `tests/test_agent_state_dir_confinement.py:519`
- `tests/test_agent_state_dir_confinement.py:536`
- `tests/test_agent_state_dir_confinement.py:566`
- `tests/test_agent_state_dir_confinement.py:864`
- `tests/test_tool_path_confinement.py:87`
- `tests/test_tool_path_confinement.py:93`
- `tests/test_tool_path_confinement.py:99`
- `tests/test_tool_path_confinement.py:107`
- `tests/test_tool_path_confinement.py:114`
- `tests/test_tool_path_confinement.py:129`
- `tests/test_tool_path_confinement.py:137`
- `tests/test_tool_path_confinement.py:143`
- `tests/test_tool_path_confinement.py:149`
- `tests/test_tool_path_confinement.py:155`
- `tests/test_tool_path_confinement.py:161`
- `tests/test_tool_path_confinement.py:175`
- `tests/test_tool_path_confinement.py:186`
- `tests/test_tool_path_confinement.py:193`
- `tests/test_tool_path_confinement.py:195`
- `tests/test_tool_path_confinement.py:208`
- `tests/test_tool_path_confinement.py:219`
- `tests/test_workspace_confine.py:87`
- `tests/test_workspace_confine.py:89`
- `tests/test_workspace_confine.py:99`

## `_resolve_tool_path_in_workspace` — function, line 406
- **called from:**
- `src/tool_execution.py:374`
- `src/tool_execution.py:548`
- `tests/test_workspace_confine.py:62`
- `tests/test_workspace_confine.py:63`
- `tests/test_workspace_confine.py:66`
- `tests/test_workspace_confine.py:68`
- `tests/test_workspace_confine.py:74`

## `get_active_user_text` — function, line 477
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_active_workspace` — function, line 482
- **called from:**
- `src/agent_tools/filesystem_tools.py:1033`
- `src/tool_execution.py:372`
- `src/tool_execution.py:518`
- `src/tool_execution.py:543`
- `tests/test_workspace_confine.py:85`
- `tests/test_workspace_confine.py:96`
- `tests/test_workspace_confine.py:292`

## `vet_workspace` — function, line 487
- **called from:**
- `routes/chat_routes.py:528`
- `routes/chat_routes.py:566`
- `routes/workspace_routes.py:65`
- `routes/workspace_routes.py:82`
- `src/tool_execution.py:908`
- `tests/test_agent_state_dir_confinement.py:252`
- `tests/test_agent_state_dir_confinement.py:257`
- `tests/test_workspace_confine.py:456`
- `tests/test_workspace_confine.py:466`
- `tests/test_workspace_confine.py:471`
- `tests/test_workspace_confine.py:472`
- `tests/test_workspace_confine.py:473`
- `tests/test_workspace_confine.py:474`
- `tests/test_workspace_confine.py:481`

## `agent_cwd` — function, line 515
- **called from:**
- `src/agent_tools/subprocess_tools.py:312`
- `src/agent_tools/subprocess_tools.py:341`
- `src/agent_tools/subprocess_tools.py:369`
- `src/tool_execution.py:1118`
- `tests/test_agent_state_dir_confinement.py:318`
- `tests/test_agent_state_dir_confinement.py:386`
- `tests/test_workspace_confine.py:86`
- `tests/test_workspace_confine.py:97`

## `get_mcp_manager` — function, line 527
- **called from:**
- `routes/task/task_routes.py:1003`
- `scripts/dump_agent_prompt.py:391`
- `src/agent_loop.py:4042`
- `src/agent_tools/admin_tools.py:228`
- `src/agent_tools/admin_tools.py:275`
- `src/agent_tools/admin_tools.py:299`
- `src/agent_tools/admin_tools.py:313`
- `src/agent_tools/admin_tools.py:357`
- `src/task_scheduler.py:1448`
- `src/task_scheduler.py:2193`
- `src/tool_execution.py:529`
- `src/tool_execution.py:706`
- `src/tool_execution.py:1313`
- `src/tool_execution.py:1356`

## `_resolve_search_root` — function, line 534
- **called from:**
- `src/agent_tools/filesystem_tools.py:534`
- `src/agent_tools/filesystem_tools.py:595`
- `src/agent_tools/filesystem_tools.py:711`
- `tests/test_agent_state_dir_confinement.py:156`
- `tests/test_agent_state_dir_confinement.py:246`
- `tests/test_agent_state_dir_confinement.py:385`
- `tests/test_agent_state_dir_confinement.py:434`
- `tests/test_workspace_confine.py:90`

## `_owner_is_admin` — function, line 575
- **called from:**
- `src/tool_execution.py:1091`
- `src/tool_execution.py:1097`

## `_parse_qualified_mcp_args` — function, line 596
- **called from:**
- `src/tool_execution.py:1359`

## `_parse_generate_image` — function, line 613
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_parse_manage_memory` — function, line 622
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_parse_write_file` — function, line 643
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_build_mcp_args` — function, line 686
- **called from:**
- `src/tool_execution.py:712`
- `tests/test_review_regressions.py:940`
- `tests/test_review_regressions.py:943`
- `tests/test_review_regressions.py:946`

## `_call_mcp_tool` — function (async), line 700
- **called from:**
- `src/tool_execution.py:1143`

## `_promote_image_fields` — function, line 732
- **called from:**
- `src/tool_execution.py:727`
- `tests/test_promote_image_fields.py:27`
- `tests/test_promote_image_fields.py:40`
- `tests/test_promote_image_fields.py:48`
- `tests/test_promote_image_fields.py:56`

## `_split_bg_marker` — function, line 758
- **called from:**
- `src/tool_execution.py:1115`

## `_direct_fallback` — function (async), line 771
- **called from:**
- `src/tool_execution.py:708`
- `src/tool_execution.py:717`
- `src/tool_execution.py:1148`
- `src/tool_execution.py:1153`
- `src/tool_execution.py:1158`
- `src/tool_execution.py:1229`
- `src/tool_execution.py:1286`
- `src/tool_execution.py:1375`
- `tests/test_code_nav_tools.py:14`

## `_document_tool_dispatch` — function (async), line 804
- **called from:**
- `src/tool_execution.py:1163`
- `src/tool_execution.py:1187`
- `src/tool_execution.py:1196`
- `src/tool_execution.py:1203`
- `src/tool_execution.py:1211`

## `execute_tool_block` — function (async), line 834
- **called from:**
- `src/agent_loop.py:5087`
- `src/agent_loop.py:6360`
- `tests/test_ask_user_tool.py:17`
- `tests/test_edit_file.py:50`
- `tests/test_external_context_tool_gate.py:751`
- `tests/test_external_context_tool_gate.py:766`
- `tests/test_external_context_tool_gate.py:783`
- `tests/test_external_context_tool_gate.py:789`
- `tests/test_review_regressions.py:19`
- `tests/test_temporal_grounding_stamps.py:197`
- `tests/test_tool_approvals.py:171`
- `tests/test_tool_approvals.py:225`
- `tests/test_tool_approvals.py:269`
- `tests/test_tool_approvals.py:376`
- `tests/test_tool_approvals.py:412`
- `tests/test_tool_approvals.py:448`
- `tests/test_tool_path_confinement.py:244`
- `tests/test_tool_path_confinement.py:273`
- `tests/test_tool_path_confinement.py:302`
- `tests/test_tool_policy.py:197`
- `tests/test_update_plan_tool.py:17`
- `tests/test_workspace_confine.py:106`
- `tests/test_workspace_confine.py:108`
- `tests/test_workspace_confine.py:113`
- `tests/test_workspace_confine.py:126`
- `tests/test_workspace_confine.py:129`
- `tests/test_workspace_confine.py:148`
- `tests/test_workspace_confine.py:166`
- `tests/test_workspace_confine.py:183`
- `tests/test_workspace_confine.py:199`
- `tests/test_workspace_confine.py:202`
- `tests/test_workspace_confine.py:204`
- `tests/test_workspace_confine.py:206`
- `tests/test_workspace_confine.py:218`
- `tests/test_workspace_confine.py:231`
- `tests/test_workspace_confine.py:233`
- `tests/test_workspace_confine.py:256`
- `tests/test_workspace_confine.py:265`
- `tests/test_workspace_confine.py:272`
- `tests/test_workspace_confine.py:281`
- `tests/test_workspace_confine.py:283`
- `tests/test_workspace_confine.py:291`

## `_execute_tool_block_impl` — function (async), line 991
- **called from:**
- `src/tool_execution.py:956`

## `format_tool_result` — function, line 1418
- **called from:**
- `src/agent_loop.py:5286`
- `src/agent_loop.py:6812`
- `tests/test_external_context_tool_gate.py:151`
- `tests/test_external_context_tool_gate.py:176`
