# `src/shutdown.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `is_shutting_down` — function, line 20
- **called from:**
- `routes/chat_routes.py:4213`
- `routes/chat_routes.py:5491`
- `routes/chat_routes.py:5737`
- `routes/editor_agent_routes.py:1589`
- `routes/email/email_routes.py:6863`
- `routes/research/research_routes.py:668`
- `routes/shell_routes.py:1029`
- `routes/shell_routes.py:1146`
- `routes/shell_routes.py:1271`
- `tests/test_shutdown_signal.py:20`
- `tests/test_shutdown_signal.py:22`
- `tests/test_shutdown_signal.py:25`
- `tests/test_shutdown_signal.py:28`

## `request_shutdown` — function, line 25
- **called from:**
- `app.py:1525`
- `tests/test_shutdown_signal.py:21`
- `tests/test_shutdown_signal.py:24`

## `reset` — function, line 32
- **called from:**
- `mcp_servers/email_server.py:1985`
- `mcp_servers/email_server.py:4696`
- `mcp_servers/email_server.py:4697`
- `services/search/core.py:521`
- `src/agent_runtime/authority.py:554`
- `src/agent_runtime/journal.py:157`
- `src/agent_runtime/journal.py:158`
- `src/agent_runtime/journal.py:237`
- `src/agent_runtime/journal.py:280`
- `src/agent_runtime/owned_resources.py:443`
- `src/agent_runtime/process_resources.py:349`
- `src/agent_runtime/remote_resources.py:238`
- `src/agent_runtime/resource_binding.py:218`
- `src/agent_tools/web_tools_prewave3.py:2677`
- `src/browser_identity.py:609`
- `src/clean_agent_preview.py:7892`
- `src/teacher_escalation.py:86`
- `src/tool_execution.py:131`
- `src/tool_execution.py:2029`
- `src/turn_contract.py:6494`
- `tests/test_agent_state_dir_confinement.py:70`
- `tests/test_agent_state_dir_confinement.py:161`
- `tests/test_agent_state_dir_confinement.py:508`
- `tests/test_agent_state_dir_confinement.py:551`
- `tests/test_codeql_python_residual_closure.py:93`
- `tests/test_execution_bridge.py:33`
- `tests/test_execution_bridge.py:53`
- `tests/test_execution_bridge.py:241`
- `tests/test_extract_text_tool.py:41`
- `tests/test_extract_text_tool.py:67`
- `tests/test_extract_text_tool.py:86`
- `tests/test_extract_text_tool.py:116`
- `tests/test_extract_text_tool.py:136`
- `tests/test_filesystem_tool_argument_validation.py:107`
- `tests/test_grep_followup_integrity.py:35`
- `tests/test_grep_followup_integrity.py:71`
- `tests/test_inspect_media_percent_ranges.py:40`
- `tests/test_inspect_media_probe_recovery.py:60`
- `tests/test_inspect_media_tool.py:88`
- `tests/test_inspect_media_tool.py:116`
- `tests/test_inspect_media_tool.py:143`
- `tests/test_inspect_media_tool.py:164`
- `tests/test_inspect_media_tool.py:189`
- `tests/test_inspect_media_tool.py:218`
- `tests/test_inspect_media_tool.py:240`
- `tests/test_inspect_media_tool.py:267`
- `tests/test_inspect_media_tool.py:286`
- `tests/test_inspect_media_tool.py:304`
- `tests/test_inspect_media_tool.py:318`
- `tests/test_inspect_media_tool.py:330`
- `tests/test_inspect_media_tool.py:346`
- `tests/test_inspect_media_tool.py:361`
- `tests/test_inspect_media_tool.py:375`
- `tests/test_inspect_media_tool.py:390`
- `tests/test_inspect_media_tool.py:403`
- `tests/test_inspect_media_tool.py:416`
- `tests/test_inspect_media_tool.py:430`
- `tests/test_inspect_media_tool.py:454`
- `tests/test_inspect_media_tool.py:493`
- `tests/test_inspect_media_tool.py:523`
- … +111 more (grep the name in repo)
