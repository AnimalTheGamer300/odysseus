# `static/js/settings/search.js` — definitions & call sites

8 definitions (regex-based, best-effort).
**Exports:** `bindSettingsSearch`

## `groupLabelFor` — function, line 9
- **called from:**
- `static/js/settings/search.js:9`
- `static/js/settings/search.js:116`

## `clearResults` — function, line 14
- **called from:**
- `static/js/settings/search.js:14`
- `static/js/settings/search.js:68`
- `static/js/settings/search.js:167`

## `getResultButtons` — function, line 20
- **called from:**
- `static/js/settings/search.js:20`
- `static/js/settings/search.js:26`
- `static/js/settings/search.js:133`

## `setActiveResult` — function, line 25
- **called from:**
- `static/js/settings/search.js:25`
- `static/js/settings/search.js:147`
- `static/js/settings/search.js:153`

## `bindSettingsSearch` — function, line 46
- **called from:**
- `static/js/settings.js:1911`
- `static/js/settings/search.js:46`

## `reset` — function, line 65
- **called from:**
- `mcp_servers/email_server.py:1985`
- `mcp_servers/email_server.py:4696`
- `mcp_servers/email_server.py:4697`
- `services/search/core.py:521`
- `src/agent_runtime/authority.py:582`
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

## `activateResult` — function, line 71
- **called from:**
- `static/js/settings/search.js:71`
- `static/js/settings/search.js:119`
- `static/js/settings/search.js:161`

## `render` — function, line 79
- **called from:**
- `scripts/generate_env_reference.py:1219`
- `src/agent_tools/media_tools.py:493`
- `src/agent_tools/media_tools.py:1002`
- `tests/test_audit_c5_benchmark_evidence.py:2875`
- `tests/test_audit_c5_benchmark_evidence.py:2882`
- `tests/test_audit_c5_benchmark_evidence.py:2892`
- `tests/test_audit_c5_benchmark_evidence.py:2906`
- `tests/test_audit_c5_benchmark_evidence.py:2925`
- `tests/test_audit_c5_benchmark_evidence.py:2933`
- `tests/test_audit_c5_benchmark_evidence.py:2935`
- `tests/test_audit_c5_benchmark_evidence.py:2978`
- `tests/test_audit_c5_benchmark_evidence.py:3001`
- `tests/test_audit_c5_benchmark_evidence.py:3006`
- `tests/test_env_reference.py:168`
- `tests/test_env_reference.py:179`
- `static/js/calendar.js:1664`
- `static/js/calendar.js:2653`
- `static/js/chat.js:3712`
- `static/js/chat.js:4812`
- `static/js/chat.js:5173`
- `static/js/chat.js:6073`
- `static/js/chat.js:6217`
- `static/js/chat.js:7371`
- `static/js/documentLibrary.js:108`
- `static/js/documentLibrary.js:124`
- `static/js/editor/adjustments-worker.js:5`
- `static/js/editor/adjustments-worker.js:20`
- `static/js/editor/build/command-palette.js:22`
- `static/js/editor/build/command-palette.js:56`
- `static/js/editor/build/command-palette.js:64`
- `static/js/editor/build/command-palette.js:67`
- `static/js/editor/build/command-palette.js:68`
- `static/js/editor/layer-panel.js:186`
- `static/js/editor/layer-panel.js:302`
- `static/js/editor/layer-panel.js:440`
- `static/js/editor/layer-panel.js:490`
- `static/js/editor/layer-panel.js:581`
- `static/js/editor/layer-panel.js:613`
- `static/js/editor/layer-panel.js:672`
- `static/js/editor/layer-panel.js:711`
- `static/js/editor/layer-panel.js:725`
- `static/js/editor/layer-panel.js:739`
- `static/js/editor/layer-panel.js:751`
- `static/js/editor/layer-panel.js:795`
- `static/js/editor/layer-panel.js:807`
- `static/js/editor/layer-panel.js:839`
- `static/js/editor/layer-panel.js:918`
- `static/js/editor/layer-panel.js:929`
- `static/js/editor/layer-panel.js:942`
- `static/js/editor/layer-panel.js:962`
- `static/js/editor/layer-panel.js:992`
- `static/js/editor/layer-panel.js:1042`
- `static/js/editor/layer-panel.js:1056`
- `static/js/editor/layer-panel.js:1079`
- `static/js/editor/layer-panel.js:1101`
- `static/js/editor/layer-panel.js:1118`
- `static/js/editor/layer-panel.js:1132`
- `static/js/editor/layer-panel.js:1139`
- `static/js/editor/layer-panel.js:1315`
- `static/js/editor/layer-panel.js:1342`
- … +104 more (grep the name in repo)
