# `static/js/editor/precision-guides.js` — definitions & call sites

18 definitions (regex-based, best-effort).
**Exports:** `RULER_SIZE`, `chooseRulerStep`, `createPrecisionGuides`, `pointerToDocument`

## `chooseRulerStep` — function, line 6
- **called from:**
- `static/js/editor/precision-guides.js:6`
- `static/js/editor/precision-guides.js:93`

## `pointerToDocument` — function, line 17
- **called from:**
- `static/js/editor/precision-guides.js:17`
- `static/js/editor/precision-guides.js:191`

## `normalizedGuides` — function, line 26
- **called from:**
- `static/js/editor/precision-guides.js:26`
- `static/js/editor/precision-guides.js:168`
- `static/js/editor/precision-guides.js:214`
- `static/js/editor/precision-guides.js:250`
- `static/js/editor/precision-guides.js:262`

## `createPrecisionGuides` — function, line 33
- **called from:**
- `static/js/editor/precision-guides.js:33`
- `static/js/galleryEditor.js:10512`

## `themeColors` — function, line 47
- **called from:**
- `static/js/editor/precision-guides.js:47`
- `static/js/editor/precision-guides.js:73`

## `prepareRuler` — function, line 56
- **called from:**
- `static/js/editor/precision-guides.js:56`
- `static/js/editor/precision-guides.js:70`

## `drawRuler` — function, line 68
- **called from:**
- `static/js/editor/precision-guides.js:68`
- `static/js/editor/precision-guides.js:138`
- `static/js/editor/precision-guides.js:139`

## `redrawRulers` — function, line 129
- **called from:**
- `static/js/editor/precision-guides.js:129`
- `static/js/editor/precision-guides.js:227`
- `static/js/editor/precision-guides.js:240`
- `static/js/editor/precision-guides.js:257`
- `static/js/editor/precision-guides.js:260`
- `static/js/editor/precision-guides.js:268`
- `static/js/galleryEditor.js:5321`
- `static/js/galleryEditor.js:9699`
- `static/js/galleryEditor.js:10552`

## `drawDocumentOverlay` — function, line 144
- **called from:**
- `static/js/editor/precision-guides.js:144`
- `static/js/galleryEditor.js:3992`

## `updateDrag` — function, line 189
- **called from:**
- `static/js/editor/precision-guides.js:189`
- `static/js/editor/precision-guides.js:209`
- `static/js/editor/precision-guides.js:212`

## `beginGuide` — function, line 204
- **called from:**
- `static/js/editor/precision-guides.js:204`
- `static/js/editor/precision-guides.js:235`
- `static/js/editor/precision-guides.js:236`

## `move` — arrow, line 209
- **called from:**
- `routes/personal_routes.py:96`
- `static/js/actionMenuOrder.js:10`
- `static/js/windowResize.js:154`
- `static/js/windowResize.js:218`
- `static/js/windowResize.js:233`

## `cancel` — arrow, line 210
- **called from:**
- `app.py:1459`
- `app.py:1470`
- `routes/editor_agent_routes.py:1414`
- `routes/email/email_routes.py:6869`
- `routes/history/history_routes.py:613`
- `routes/shell_routes.py:957`
- `routes/shell_routes.py:1342`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `services/skills/job_coordinator.py:215`
- `src/agent_loop.py:26037`
- `src/agent_loop.py:34341`
- `src/agent_runs.py:86`
- `src/agent_runs.py:207`
- `src/agent_runs.py:210`
- `src/agent_runs.py:249`
- `src/agent_runs.py:298`
- `src/agent_runs.py:315`
- `src/ai_interaction.py:1822`
- `src/ai_interaction.py:2094`
- `src/clean_agent_preview.py:5609`
- `src/clean_agent_preview.py:5617`
- `src/containment.py:1172`
- `src/containment.py:1182`
- `src/llm_core.py:141`
- `src/mcp_manager.py:440`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:502`
- `src/research_handler.py:505`
- `src/task_scheduler.py:122`
- `src/task_scheduler.py:733`
- `src/task_scheduler.py:741`
- `src/task_scheduler.py:1063`
- `src/task_scheduler.py:1145`
- `src/task_scheduler.py:2470`
- `src/task_scheduler.py:2495`
- `tests/test_agent_editor_routes.py:1008`
- `tests/test_agent_editor_routes.py:1962`
- `tests/test_agent_editor_routes.py:1971`
- `tests/test_browser_identity_transport.py:39`
- `tests/test_browser_identity_transport.py:75`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_client_tool_routing.py:867`
- `tests/test_compare_stop_disconnect_poll.py:377`
- `tests/test_compare_stop_disconnect_poll.py:434`
- `tests/test_completion_boundary.py:319`
- `tests/test_completion_boundary.py:324`
- `tests/test_containment_enforcement.py:382`
- `tests/test_containment_enforcement.py:384`
- `tests/test_containment_enforcement.py:408`
- `tests/test_containment_enforcement.py:410`
- `tests/test_cookbook_cache_scan_isolation.py:102`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:457`
- `tests/test_email_urgency_checkpoint.py:592`
- `tests/test_host_shell_polling.py:198`
- `tests/test_nested_invocation_ownership.py:93`
- `tests/test_nested_invocation_ownership.py:96`
- `tests/test_nested_invocation_ownership.py:448`
- … +84 more (grep the name in repo)

## `finish` — arrow, line 211
- **called from:**
- `src/agent_loop.py:32996`
- `src/agent_loop.py:33009`
- `src/agent_loop.py:33017`
- `src/agent_loop.py:34877`
- `src/agent_runtime/journal.py:267`
- `src/agent_runtime/journal.py:269`
- `src/containment.py:1512`
- `src/containment.py:1518`
- `src/containment.py:1527`
- `src/containment.py:1542`
- `src/containment.py:1545`
- `src/pdf_forms.py:338`
- `tests/test_effect_verification_adapters.py:55`
- `tests/test_effect_verification_adapters.py:121`
- `tests/test_effect_verification_adapters.py:215`
- `tests/test_effect_verification_adapters.py:431`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:2122`
- `static/js/colorPicker.js:237`
- `static/js/colorPicker.js:243`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:211`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/ai-inpaint.js:280`
- `static/js/editor/ai-operation.js:19`
- `static/js/editor/ai-tool-runner.js:164`
- `static/js/editor/ai-tools-misc.js:157`
- `static/js/editor/ai-tools-misc.js:206`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:372`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-panel.js:1424`
- `static/js/editor/layer-panel.js:1426`
- `static/js/editor/layer-panel.js:1431`
- `static/js/editor/precision-guides.js:210`
- `static/js/editor/precision-guides.js:229`
- `static/js/editor/tools/pen-path.js:39`
- `static/js/editor/tools/pen-path.js:46`
- `static/js/features/notes/ui/cardInteractions.js:234`
- `static/js/features/notes/ui/cardInteractions.js:238`
- `static/js/features/notes/ui/colors.js:63`
- `static/js/features/notes/ui/colors.js:71`
- `static/js/features/notes/ui/colors.js:72`
- `static/js/features/notes/ui/colors.js:75`
- `static/js/fileHandler.js:96`
- `static/js/fileHandler.js:134`
- `static/js/fileHandler.js:135`
- `static/js/fileHandler.js:172`
- `static/js/fileHandler.js:175`
- `static/js/gallery.js:2484`
- `static/js/gallery.js:2487`
- `static/js/galleryEditor.js:430`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4573`
- `static/js/galleryEditor.js:4575`
- `static/js/galleryEditor.js:4655`
- `static/js/galleryEditor.js:4659`
- … +4 more (grep the name in repo)

## `end` — arrow, line 229
- **called from:**
- `mcp_servers/email_server.py:2023`
- `routes/chat_helpers.py:1715`
- `routes/chat_helpers.py:1727`
- `routes/chat_routes.py:347`
- `routes/cookbook_helpers.py:778`
- `routes/email/email_helpers.py:397`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1593`
- `routes/email/email_routes.py:1594`
- `routes/email/email_routes.py:1598`
- `scripts/add_hwfit_models.py:117`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:800`
- `src/agent_evidence.py:234`
- `src/agent_evidence.py:247`
- `src/agent_loop.py:954`
- `src/agent_loop.py:1142`
- `src/agent_loop.py:2319`
- `src/agent_loop.py:2324`
- `src/agent_loop.py:2605`
- `src/agent_loop.py:2621`
- `src/agent_loop.py:2629`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:2666`
- `src/agent_loop.py:2697`
- `src/agent_loop.py:2815`
- `src/agent_loop.py:2819`
- `src/agent_loop.py:3207`
- `src/agent_loop.py:4872`
- `src/agent_loop.py:4876`
- `src/agent_loop.py:4881`
- `src/agent_loop.py:4885`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:13312`
- `src/agent_loop.py:13313`
- `src/agent_loop.py:13326`
- `src/agent_loop.py:13329`
- `src/agent_loop.py:13341`
- `src/agent_loop.py:13851`
- `src/agent_loop.py:13854`
- `src/agent_loop.py:13854`
- `src/agent_loop.py:14155`
- `src/agent_loop.py:18329`
- `src/agent_loop.py:18331`
- `src/agent_loop.py:18437`
- `src/agent_loop.py:25756`
- `src/agent_runtime/completion.py:91`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:438`
- `src/agent_tools/document_tools.py:730`
- `src/agent_tools/document_tools.py:735`
- `src/agent_tools/filesystem_tools.py:66`
- `src/agent_tools/web_tools.py:892`
- `src/agent_tools/web_tools_prewave3.py:896`
- `src/builtin_actions.py:1329`
- `src/clean_agent_preview.py:843`
- `src/clean_agent_preview.py:950`
- `src/clean_agent_preview.py:977`
- `src/clean_agent_preview.py:1841`
- … +105 more (grep the name in repo)

## `addGuide` — method?, line 245
- **called from:**
- `static/js/editor/precision-guides.js:245`

## `syncVisibility` — method?, line 260
- **called from:**
- `static/js/editor/precision-guides.js:260`
- `static/js/editor/wire-view-menu.js:52`
- `static/js/galleryEditor.js:5108`

## `clearGuides` — method?, line 261
- **called from:**
- `static/js/editor/precision-guides.js:261`
- `static/js/editor/wire-view-menu.js:50`
