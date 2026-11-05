# `src/mcp_manager.py` — definitions & call sites

30 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `browser_mcp_call_timeout` — function, line 24
- **called from:**
- `src/mcp_manager.py:597`

## `_format_mcp_connection_error` — function, line 33
- **called from:**
- `src/mcp_manager.py:206`
- `tests/test_mcp_manager.py:8`
- `tests/test_mcp_manager.py:22`

## `_sanitize_schema_token` — function, line 59
- **called from:**
- `src/mcp_manager.py:97`
- `src/mcp_manager.py:97`
- `tests/test_mcp_param_hint_hardening.py:43`
- `tests/test_mcp_param_hint_hardening.py:44`
- `tests/test_mcp_param_hint_hardening.py:49`

## `_format_mcp_params` — function, line 73
- **called from:**
- `src/mcp_manager.py:856`
- `tests/test_mcp_param_hint_hardening.py:23`
- `tests/test_mcp_param_hint_hardening.py:35`
- `tests/test_mcp_param_hint_hardening.py:56`
- `tests/test_mcp_param_hint_hardening.py:66`
- `tests/test_mcp_param_hint_hardening.py:71`
- `tests/test_mcp_param_hint_hardening.py:72`
- `tests/test_mcp_param_hint_hardening.py:73`
- `tests/test_mcp_tool_params_in_prompt.py:69`
- `tests/test_mcp_tool_params_in_prompt.py:70`
- `tests/test_mcp_tool_params_in_prompt.py:71`
- `tests/test_mcp_tool_params_in_prompt.py:77`

## `mcp_tool_is_readonly` — function, line 120
- **called from:**
- `src/mcp_manager.py:768`
- `src/tool_capabilities.py:438`
- `src/tool_capabilities.py:1063`

## `McpManager` — class, line 148
- **called from:**
- `app.py:918`
- `scripts/dump_agent_prompt.py:397`
- `tests/test_browser_lifecycle.py:321`
- `tests/test_external_context_tool_gate.py:290`
- `tests/test_local_mcp_capabilities.py:112`
- `tests/test_local_mcp_capabilities.py:864`
- `tests/test_mcp_cache_invalidation.py:14`
- `tests/test_mcp_cache_invalidation.py:86`
- `tests/test_mcp_manager.py:33`
- `tests/test_mcp_manager.py:86`
- `tests/test_mcp_manager.py:104`
- `tests/test_mcp_tool_params_in_prompt.py:15`
- `tests/test_multiple_mcp_servers_timeout.py:35`
- `tests/test_multiple_mcp_servers_timeout.py:102`
- `tests/test_product_turn_contract_route.py:22`
- `tests/test_remote_resource_identity.py:45`

## `McpManager.__init__` — method, line 151
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `McpManager.connect_server` — method (async), line 173
- **called from:**
- `routes/mcp/mcp_routes.py:283`
- `routes/mcp/mcp_routes.py:321`
- `routes/mcp/mcp_routes.py:360`
- `routes/mcp/mcp_routes.py:623`
- `src/agent_tools/admin_tools.py:293`
- `src/agent_tools/admin_tools.py:339`
- `src/builtin_mcp.py:174`
- `src/builtin_mcp.py:238`
- `src/mcp_manager.py:525`
- `src/mcp_manager.py:683`
- `tests/test_local_mcp_capabilities.py:865`
- `tests/test_mcp_manager.py:39`

## `McpManager._connect_stdio` — method (async), line 211
- **called from:**
- `src/mcp_manager.py:193`

## `McpManager._connect_sse` — method (async), line 287
- **called from:**
- `src/mcp_manager.py:195`

## `McpManager._start_http_connect` — method (async), line 342
- **called from:**
- `src/mcp_manager.py:197`
- `tests/test_mcp_manager.py:88`
- `tests/test_mcp_manager.py:107`

## `McpManager._connect_http` — method (async), line 369
- **called from:**
- `src/mcp_manager.py:348`

## `McpManager._on_redirect` — method, line 377
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `McpManager.disconnect_server` — method (async), line 434
- **called from:**
- `routes/mcp/mcp_routes.py:317`
- `routes/mcp/mcp_routes.py:370`
- `routes/mcp/mcp_routes.py:386`
- `src/agent_tools/admin_tools.py:316`
- `src/agent_tools/admin_tools.py:331`
- `src/mcp_manager.py:501`
- `src/mcp_manager.py:680`
- `tests/test_local_mcp_capabilities.py:924`
- `tests/test_mcp_cache_invalidation.py:34`
- `tests/test_mcp_cache_invalidation.py:58`
- `tests/test_mcp_cache_invalidation.py:96`
- `tests/test_mcp_manager.py:108`

## `McpManager.hold_owned_connection` — method (async), line 478
- **called from:**
- `src/builtin_mcp.py:184`
- `src/builtin_mcp.py:248`
- `tests/test_mcp_cache_invalidation.py:92`

## `McpManager.disconnect_all` — method (async), line 497
- **called from:**
- `app.py:1487`

## `McpManager.connect_all_enabled` — method (async), line 504
- **called from:**
- `app.py:1255`
- `scripts/dump_agent_prompt.py:407`
- `tests/test_multiple_mcp_servers_timeout.py:89`
- `tests/test_multiple_mcp_servers_timeout.py:173`

## `McpManager._connect_with_timeout` — method (async), line 519
- **called from:**
- `src/mcp_manager.py:510`

## `McpManager._register_resource_connection` — method, line 544
- **called from:**
- `src/mcp_manager.py:258`
- `src/mcp_manager.py:318`
- `src/mcp_manager.py:411`
- `tests/test_local_mcp_capabilities.py:147`
- `tests/test_remote_resource_identity.py:57`

## `McpManager.resource_identity` — method, line 551
- **called from:**
- `src/agent_runtime/authority.py:428`
- `src/agent_runtime/remote_resources.py:111`
- `src/agent_runtime/remote_resources.py:135`
- `src/mcp_manager.py:589`
- `src/tool_capabilities.py:1002`
- `src/tool_capabilities.py:1053`
- `tests/test_agent_external_tool_schemas.py:439`
- `tests/test_agent_external_tool_schemas.py:440`

## `McpManager.call_tool` — method (async), line 571
- **called from:**
- `mcp_servers/email_server.py:4038`
- `mcp_servers/image_gen_server.py:44`
- `mcp_servers/memory_server.py:143`
- `mcp_servers/rag_server.py:68`
- `src/mcp_manager.py:639`
- `src/task_scheduler.py:1628`
- `src/task_scheduler.py:2436`
- `src/tool_execution.py:1501`
- `src/tool_execution.py:2539`
- `src/tool_execution.py:2562`
- `tests/test_browser_lifecycle.py:332`
- `tests/test_email_search_folder_contract.py:24`
- `tests/test_generated_image_ownership.py:480`
- `tests/test_generated_image_ownership.py:488`
- `tests/test_image_quality_defaults.py:64`
- `tests/test_mcp_email_decode_header_spaces.py:99`
- `tests/test_mcp_email_decode_header_spaces.py:113`
- `tests/test_mcp_email_decode_header_spaces.py:127`
- `tests/test_mcp_email_decode_header_spaces.py:143`
- `tests/test_mcp_email_decode_header_spaces.py:156`
- `tests/test_mcp_email_decode_header_spaces.py:223`
- `tests/test_mcp_email_decode_header_spaces.py:241`
- `tests/test_mcp_email_decode_header_spaces.py:272`
- `tests/test_mcp_email_decode_header_spaces.py:327`
- `tests/test_mcp_email_search_dates.py:47`
- `tests/test_mcp_email_search_dates.py:77`
- `tests/test_mcp_email_search_dates.py:107`
- `tests/test_mcp_email_search_dates.py:129`
- `tests/test_mcp_email_search_dates.py:145`
- `tests/test_mcp_email_search_dates.py:158`
- `tests/test_mcp_email_search_dates.py:182`
- `tests/test_mcp_email_search_dates.py:210`
- `tests/test_mcp_email_search_error_transport.py:10`
- `tests/test_mcp_memory_owner_scope.py:22`
- `tests/test_memory_store_unreadable_no_wipe.py:218`
- `tests/test_memory_tool_contract.py:33`
- `tests/test_memory_tool_contract.py:42`
- `tests/test_rag_server_directory_nonstring.py:18`
- `tests/test_remote_resource_identity.py:177`
- `tests/test_remote_resource_identity.py:180`

## `McpManager._do_call` — method (async), line 637
- **called from:**
- `src/mcp_manager.py:600`
- `src/mcp_manager.py:612`
- `src/mcp_manager.py:622`
- `tests/test_external_context_tool_gate.py:290`

## `McpManager._reconnect_builtin` — method (async), line 667
- **called from:**
- `src/mcp_manager.py:617`

## `McpManager.get_all_openai_schemas` — method, line 698
- **called from:**
- `routes/chat_routes.py:3837`
- `src/agent_loop.py:14864`
- `src/agent_loop.py:21467`
- `src/agent_loop.py:24853`

## `McpManager.get_all_tools` — method, line 737
- **called from:**
- `routes/mcp/mcp_routes.py:399`
- `routes/mcp/mcp_routes.py:415`
- `routes/task/task_routes.py:1077`
- `src/agent_loop.py:4581`
- `src/agent_loop.py:4618`
- `src/agent_tools/admin_tools.py:374`
- `src/mcp_manager.py:817`
- `src/tools_doc.py:97`
- `tests/test_mcp_tool_params_in_prompt.py:37`
- `tests/test_private_browser_tool.py:432`
- `tests/test_private_browser_tool.py:438`

## `McpManager.plan_mode_blocked_mcp` — method, line 755
- **called from:**
- `src/agent_loop.py:23052`

## `McpManager.is_builtin` — method, line 774
- decorator: `staticmethod`
- **called from:**
- `src/agent_runtime/authority.py:423`
- `src/mcp_manager.py:615`
- `src/mcp_manager.py:712`
- `src/mcp_manager.py:827`
- `src/task_scheduler.py:1606`
- `src/tool_capabilities.py:413`
- `src/tool_capabilities.py:976`
- `src/tool_capabilities.py:993`
- `src/tools_doc.py:100`

## `McpManager.get_server_status` — method, line 785
- **called from:**
- `routes/mcp/mcp_routes.py:142`
- `routes/mcp/mcp_routes.py:293`
- `routes/mcp/mcp_routes.py:331`
- `routes/mcp/mcp_routes.py:634`
- `routes/mcp/mcp_routes.py:642`
- `src/agent_runtime/authority.py:425`
- `src/agent_tools/admin_tools.py:251`
- `src/agent_tools/admin_tools.py:298`
- `src/agent_tools/admin_tools.py:348`
- `src/tool_capabilities.py:996`

## `McpManager.get_all_statuses` — method, line 789
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `McpManager.get_tool_descriptions_for_prompt` — method, line 796
- **called from:**
- `src/agent_loop.py:15417`
- `src/tool_index.py:318`
- `tests/test_mcp_cache_invalidation.py:54`
- `tests/test_mcp_cache_invalidation.py:65`
- `tests/test_mcp_tool_params_in_prompt.py:42`
- `tests/test_mcp_tool_params_in_prompt.py:50`
- `tests/test_mcp_tool_params_in_prompt.py:58`
- `tests/test_mcp_tool_params_in_prompt.py:59`
- `tests/test_mcp_tool_params_in_prompt.py:60`
