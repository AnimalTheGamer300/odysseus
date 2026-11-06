# `static/js/streamingRenderer.js` — definitions & call sites

17 definitions (regex-based, best-effort).
**Exports:** `createStreamRenderer`

## `createStreamRenderer` — function, line 29
- **called from:**
- `static/js/chat.js:1599`
- `static/js/chat.js:4494`
- `static/js/chat.js:4542`
- `static/js/streamingRenderer.js:29`

## `start` — function, line 41
- **called from:**
- `app.py:1410`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `mcp_servers/email_server.py:2023`
- `routes/auth_routes.py:895`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:1714`
- `routes/chat_helpers.py:1777`
- `routes/chat_helpers.py:1778`
- `routes/chat_helpers.py:1779`
- `routes/chat_routes.py:5541`
- `routes/cookbook_routes.py:3584`
- `routes/email/email_helpers.py:399`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1596`
- `routes/email/email_routes.py:1898`
- `routes/model_routes.py:1666`
- `scripts/add_hwfit_models.py:117`
- `scripts/css_snapshot.py:211`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:411`
- `services/search/core.py:800`
- `services/skills/evaluation.py:463`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:245`
- `src/agent_evidence.py:308`
- `src/agent_loop.py:1143`
- `src/agent_loop.py:2639`
- `src/agent_loop.py:2644`
- `src/agent_loop.py:2652`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:3180`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9169`
- `src/agent_loop.py:12041`
- `src/agent_loop.py:12044`
- `src/agent_loop.py:14160`
- `src/agent_loop.py:14164`
- `src/agent_runtime/completion.py:90`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:94`
- `src/agent_tools/document_tools.py:240`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:431`
- `src/agent_tools/document_tools.py:729`
- `src/agent_tools/document_tools.py:734`
- `src/agent_tools/document_tools.py:898`
- `src/agent_tools/filesystem_tools.py:1153`
- `src/agent_tools/filesystem_tools.py:1154`
- `src/agent_tools/filesystem_tools.py:1266`
- `src/agent_tools/web_tools.py:954`
- `src/agent_tools/web_tools.py:975`
- `src/agent_tools/web_tools.py:978`
- `src/agent_tools/web_tools_prewave3.py:958`
- … +213 more (grep the name in repo)

## `highlight` — function, line 48
- **called from:**
- `static/js/documentLibrary.js:941`
- `static/js/documentLibrary.js:1183`
- `static/js/editor/layer-panel.js:167`
- `static/js/editor/layer-panel.js:174`
- `static/js/features/notes/application/reminders.js:122`
- `static/js/streamingRenderer.js:48`
- `static/js/streamingRenderer.js:61`
- `static/js/streamingRenderer.js:166`

## `clearTail` — function, line 52
- **called from:**
- `static/js/streamingRenderer.js:52`
- `static/js/streamingRenderer.js:73`
- `static/js/streamingRenderer.js:115`
- `static/js/streamingRenderer.js:232`
- `static/js/streamingRenderer.js:241`
- `static/js/streamingRenderer.js:270`

## `freeze` — function, line 58
- **called from:**
- `static/js/document.js:10464`
- `static/js/document.js:10473`
- `static/js/document.js:10474`
- `static/js/document.js:10483`
- `static/js/document.js:11253`
- `static/js/editor/actions-panel.js:11`
- `static/js/editor/color-mode.js:10`
- `static/js/editor/color-mode.js:11`
- `static/js/editor/fx/develop.js:22`
- `static/js/editor/panel-visibility.js:13`
- `static/js/editor/panels/studio-panels.js:11`
- `static/js/editor/panels/studio-panels.js:35`
- `static/js/editor/placed-layer.js:3`
- `static/js/editor/shape-boolean.js:3`
- `static/js/editor/shape-boolean.js:5`
- `static/js/editor/shape-layer.js:7`
- `static/js/editor/shape-layer.js:23`
- `static/js/editor/shape-layer.js:25`
- `static/js/editor/text-layer.js:3`
- `static/js/editor/text-layer.js:26`
- `static/js/editor/text-layer.js:29`
- `static/js/editor/text-layer.js:36`
- `static/js/editor/tool-shortcuts.js:2`
- `static/js/editor/workspaces.js:11`
- `static/js/editor/workspaces.js:12`
- `static/js/editor/workspaces.js:12`
- `static/js/editor/workspaces.js:13`
- `static/js/editor/workspaces.js:13`
- `static/js/editor/workspaces.js:14`
- `static/js/editor/workspaces.js:14`
- `static/js/editor/workspaces.js:15`
- `static/js/editor/workspaces.js:15`
- `static/js/editor/workspaces.js:16`
- `static/js/editor/workspaces.js:16`
- `static/js/emailLibrary/index.js:2309`
- `static/js/emailLibrary/index.js:5890`
- `static/js/emailLibrary/utils.js:33`
- `static/js/features/notes/application/state.js:54`
- `static/js/features/notes/application/state.js:55`
- `static/js/settings/registry.js:9`
- `static/js/settings/registry.js:13`
- `static/js/settings/registry.js:17`
- `static/js/settings/registry.js:21`
- `static/js/settings/registry.js:46`
- `static/js/streamingRenderer.js:58`
- `static/js/streamingRenderer.js:233`
- `static/js/streamingRenderer.js:273`

## `renderTail` — function, line 66
- **called from:**
- `static/js/streamingRenderer.js:66`
- `static/js/streamingRenderer.js:101`
- `static/js/streamingRenderer.js:245`

## `scheduleTailRender` — function, line 89
- **called from:**
- `static/js/streamingRenderer.js:89`
- `static/js/streamingRenderer.js:247`

## `appendOpenFence` — function, line 113
- **called from:**
- `static/js/streamingRenderer.js:69`
- `static/js/streamingRenderer.js:113`

## `that` — class, line 135
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fadeNewText` — function, line 138
- **called from:**
- `static/js/streamingRenderer.js:80`
- `static/js/streamingRenderer.js:138`

## `fullRender` — function, line 164
- **called from:**
- `static/js/streamingRenderer.js:164`
- `static/js/streamingRenderer.js:171`

## `safeFullRender` — function, line 169
- **called from:**
- `static/js/streamingRenderer.js:105`
- `static/js/streamingRenderer.js:169`
- `static/js/streamingRenderer.js:216`
- `static/js/streamingRenderer.js:253`
- `static/js/streamingRenderer.js:265`
- `static/js/streamingRenderer.js:280`

## `cancelPendingTail` — function, line 180
- **called from:**
- `static/js/streamingRenderer.js:180`
- `static/js/streamingRenderer.js:190`
- `static/js/streamingRenderer.js:215`
- `static/js/streamingRenderer.js:231`
- `static/js/streamingRenderer.js:240`
- `static/js/streamingRenderer.js:244`
- `static/js/streamingRenderer.js:250`
- `static/js/streamingRenderer.js:263`

## `resetDom` — function, line 189
- **called from:**
- `static/js/streamingRenderer.js:189`
- `static/js/streamingRenderer.js:199`
- `static/js/streamingRenderer.js:226`

## `reset` — function, line 198
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

## `update` — function, line 212
- **called from:**
- `app.py:487`
- `app.py:1336`
- `app.py:1356`
- `core/database.py:3084`
- `core/session_manager.py:989`
- `routes/auth_routes.py:474`
- `routes/auth_routes.py:487`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:919`
- `routes/chat_helpers.py:1062`
- `routes/chat_helpers.py:1079`
- `routes/chat_helpers.py:1096`
- `routes/chat_routes.py:1442`
- `routes/chat_routes.py:1493`
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
- `routes/cookbook_routes.py:3264`
- `routes/cookbook_routes.py:3268`
- `routes/cookbook_routes.py:3271`
- `routes/cookbook_routes.py:3386`
- `routes/cookbook_routes.py:4121`
- `routes/device_flow.py:156`
- `routes/email/email_pollers.py:969`
- `routes/email/email_routes.py:187`
- `routes/email/email_routes.py:1307`
- `routes/email/email_routes.py:2526`
- `routes/email/email_routes.py:2872`
- `routes/email/email_routes.py:4906`
- `routes/email/email_routes.py:4976`
- `routes/email/email_routes.py:5502`
- `routes/email/email_routes.py:5503`
- `routes/email/email_routes.py:5506`
- `routes/email/email_routes.py:5511`
- `routes/email/email_routes.py:6640`
- … +547 more (grep the name in repo)

## `finalize` — function, line 262
- **called from:**
- `static/js/chat.js:1725`
- `static/js/streamingRenderer.js:222`
- `static/js/streamingRenderer.js:262`
