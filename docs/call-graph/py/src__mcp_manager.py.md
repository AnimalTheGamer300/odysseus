# `src/mcp_manager.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_format_mcp_connection_error` — function, line 20
- **called from:**
- `src/mcp_manager.py:178`
- `tests/test_mcp_manager.py:8`
- `tests/test_mcp_manager.py:22`

## `_sanitize_schema_token` — function, line 46
- **called from:**
- `src/mcp_manager.py:84`
- `src/mcp_manager.py:84`
- `tests/test_mcp_param_hint_hardening.py:43`
- `tests/test_mcp_param_hint_hardening.py:44`
- `tests/test_mcp_param_hint_hardening.py:49`

## `_format_mcp_params` — function, line 60
- **called from:**
- `src/mcp_manager.py:716`
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

## `mcp_tool_is_readonly` — function, line 107
- **called from:**
- `src/mcp_manager.py:636`

## `McpManager` — class, line 135
- **called from:**
- `app.py:834`
- `scripts/dump_agent_prompt.py:397`
- `tests/test_external_context_tool_gate.py:221`
- `tests/test_mcp_cache_invalidation.py:14`
- `tests/test_mcp_manager.py:33`
- `tests/test_mcp_tool_params_in_prompt.py:15`
- `tests/test_multiple_mcp_servers_timeout.py:35`
- `tests/test_multiple_mcp_servers_timeout.py:102`

## `McpManager.__init__` — method, line 138
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `McpManager.connect_server` — method (async), line 152
- **called from:**
- `routes/mcp/mcp_routes.py:263`
- `routes/mcp/mcp_routes.py:301`
- `routes/mcp/mcp_routes.py:340`
- `routes/mcp/mcp_routes.py:576`
- `src/agent_tools/admin_tools.py:279`
- `src/agent_tools/admin_tools.py:325`
- `src/builtin_mcp.py:174`
- `src/builtin_mcp.py:237`
- `src/mcp_manager.py:448`
- `src/mcp_manager.py:555`
- `tests/test_mcp_manager.py:39`

## `McpManager._connect_stdio` — method (async), line 183
- **called from:**
- `src/mcp_manager.py:165`

## `McpManager._connect_sse` — method (async), line 258
- **called from:**
- `src/mcp_manager.py:167`

## `McpManager._start_http_connect` — method (async), line 312
- **called from:**
- `src/mcp_manager.py:169`

## `McpManager._connect_http` — method (async), line 339
- **called from:**
- `src/mcp_manager.py:318`

## `McpManager._on_redirect` — method, line 347
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `McpManager.disconnect_server` — method (async), line 394
- **called from:**
- `routes/mcp/mcp_routes.py:297`
- `routes/mcp/mcp_routes.py:350`
- `routes/mcp/mcp_routes.py:366`
- `src/agent_tools/admin_tools.py:302`
- `src/agent_tools/admin_tools.py:317`
- `src/mcp_manager.py:424`
- `src/mcp_manager.py:552`
- `tests/test_mcp_cache_invalidation.py:34`
- `tests/test_mcp_cache_invalidation.py:58`

## `McpManager.disconnect_all` — method (async), line 420
- **called from:**
- `app.py:1300`

## `McpManager.connect_all_enabled` — method (async), line 427
- **called from:**
- `app.py:1082`
- `scripts/dump_agent_prompt.py:407`
- `tests/test_multiple_mcp_servers_timeout.py:89`
- `tests/test_multiple_mcp_servers_timeout.py:173`

## `McpManager._connect_with_timeout` — method (async), line 442
- **called from:**
- `src/mcp_manager.py:433`

## `McpManager.call_tool` — method (async), line 467
- **called from:**
- `mcp_servers/email_server.py:2454`
- `mcp_servers/image_gen_server.py:44`
- `mcp_servers/memory_server.py:143`
- `mcp_servers/rag_server.py:68`
- `src/mcp_manager.py:511`
- `src/task_scheduler.py:1474`
- `src/task_scheduler.py:2234`
- `src/tool_execution.py:713`
- `src/tool_execution.py:1351`
- `src/tool_execution.py:1366`
- `tests/test_mcp_email_decode_header_spaces.py:100`
- `tests/test_mcp_email_decode_header_spaces.py:114`
- `tests/test_mcp_email_decode_header_spaces.py:130`
- `tests/test_mcp_email_decode_header_spaces.py:143`
- `tests/test_mcp_email_decode_header_spaces.py:210`
- `tests/test_mcp_email_decode_header_spaces.py:228`
- `tests/test_mcp_email_decode_header_spaces.py:259`
- `tests/test_mcp_email_decode_header_spaces.py:314`
- `tests/test_mcp_memory_owner_scope.py:22`
- `tests/test_memory_store_unreadable_no_wipe.py:218`
- `tests/test_rag_server_directory_nonstring.py:18`

## `McpManager._do_call` — method (async), line 509
- **called from:**
- `src/mcp_manager.py:484`
- `src/mcp_manager.py:494`
- `tests/test_external_context_tool_gate.py:221`

## `McpManager._reconnect_builtin` — method (async), line 539
- **called from:**
- `src/mcp_manager.py:489`

## `McpManager.get_all_openai_schemas` — method, line 570
- **called from:**
- `src/agent_loop.py:2706`

## `McpManager.get_all_tools` — method, line 605
- **called from:**
- `routes/mcp/mcp_routes.py:379`
- `routes/mcp/mcp_routes.py:395`
- `routes/task/task_routes.py:1005`
- `src/agent_loop.py:92`
- `src/agent_tools/admin_tools.py:360`
- `src/mcp_manager.py:681`
- `src/tools_doc.py:97`
- `tests/test_mcp_tool_params_in_prompt.py:37`

## `McpManager.plan_mode_blocked_mcp` — method, line 623
- **called from:**
- `src/agent_loop.py:4441`

## `McpManager.is_builtin` — method, line 641
- **called from:**
- `src/mcp_manager.py:487`
- `src/mcp_manager.py:580`
- `src/mcp_manager.py:690`
- `src/task_scheduler.py:1452`
- `src/tools_doc.py:100`

## `McpManager.get_server_status` — method, line 650
- **called from:**
- `routes/mcp/mcp_routes.py:129`
- `routes/mcp/mcp_routes.py:273`
- `routes/mcp/mcp_routes.py:311`
- `routes/mcp/mcp_routes.py:587`
- `routes/mcp/mcp_routes.py:595`
- `src/agent_tools/admin_tools.py:237`
- `src/agent_tools/admin_tools.py:284`
- `src/agent_tools/admin_tools.py:334`

## `McpManager.get_all_statuses` — method, line 654
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `McpManager.get_tool_descriptions_for_prompt` — method, line 661
- **called from:**
- `src/agent_loop.py:3178`
- `src/tool_index.py:256`
- `tests/test_mcp_cache_invalidation.py:54`
- `tests/test_mcp_cache_invalidation.py:65`
- `tests/test_mcp_tool_params_in_prompt.py:42`
- `tests/test_mcp_tool_params_in_prompt.py:50`
- `tests/test_mcp_tool_params_in_prompt.py:58`
- `tests/test_mcp_tool_params_in_prompt.py:59`
- `tests/test_mcp_tool_params_in_prompt.py:60`
