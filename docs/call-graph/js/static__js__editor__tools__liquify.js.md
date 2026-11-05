# `static/js/editor/tools/liquify.js` — definitions & call sites

14 definitions (regex-based, best-effort).
**Exports:** `createLiquifyTool`

## `createLiquifyTool` — function, line 17
- **called from:**
- `static/js/editor/tools/liquify.js:17`
- `static/js/galleryEditor.js:6644`

## `radius` — arrow, line 20
- **called from:**
- `static/js/editor/canvas-context-menu.js:92`
- `static/js/editor/state.js:116`
- `static/js/editor/tools/liquify.js:68`
- `static/js/editor/tools/liquify.js:132`
- `static/js/editor/wire-topbar-menus.js:298`
- `static/js/editor/wire-topbar-menus.js:302`
- `static/js/galleryEditor.js:5766`

## `strength` — arrow, line 21
- **called from:**
- `static/js/editor/tools/liquify.js:79`
- `static/js/galleryEditor.js:2582`

## `mode` — arrow, line 22
- **called from:**
- `static/app.js:1869`
- `static/app.js:2807`
- `static/app.js:2875`
- `static/app.js:4127`
- `static/js/compare/index.js:174`
- `static/js/cookbook-hwfit.js:946`
- `static/js/document.js:13887`
- `static/js/editor/tools/liquify.js:79`
- `static/js/editor/tools/liquify.js:153`
- `static/js/features/notes/ui/editor.js:459`
- `static/js/galleryEditor.js:636`
- `static/js/galleryEditor.js:1383`
- `static/js/galleryEditor.js:2797`
- `static/js/galleryEditor.js:2849`
- `static/js/galleryEditor.js:2893`
- `static/js/galleryEditor.js:12609`
- `static/js/keyboard-shortcuts.js:72`
- `static/js/research/panel.js:1168`
- `static/js/slashCommands.js:6531`
- `static/js/streamingRenderer.js:16`
- `static/js/tasks.js:675`
- `static/js/workspace.js:30`

## `requestComposite` — arrow, line 24
- **called from:**
- `static/js/editor/tools/liquify.js:137`
- `static/js/editor/tools/liquify.js:153`

## `layerPoint` — function, line 31
- **called from:**
- `static/js/editor/tools/liquify.js:31`
- `static/js/editor/tools/liquify.js:149`
- `static/js/editor/tools/liquify.js:159`

## `sampleBilinear` — function, line 37
- **called from:**
- `static/js/editor/tools/liquify.js:37`
- `static/js/editor/tools/liquify.js:119`

## `average3x3` — function, line 52
- **called from:**
- `static/js/editor/tools/liquify.js:52`
- `static/js/editor/tools/liquify.js:111`

## `dab` — function, line 65
- **called from:**
- `static/js/editor/brush-engine.js:30`
- `static/js/editor/tools/liquify.js:65`
- `static/js/editor/tools/liquify.js:135`
- `static/js/editor/tools/liquify.js:153`

## `strokeTo` — function, line 125
- **called from:**
- `static/js/editor/stroke-pipeline.js:396`
- `static/js/editor/tools/liquify.js:125`
- `static/js/editor/tools/liquify.js:160`
- `static/js/editor/tools/stroke.js:137`

## `begin` — method?, line 141
- **called from:**
- `core/database.py:1399`
- `core/database.py:1517`
- `core/database.py:2249`
- `core/database.py:2375`
- `tests/test_chatgpt_session_binding.py:151`
- `tests/test_chatgpt_session_binding.py:157`
- `tests/test_cookbook_endpoint_registration.py:303`
- `tests/test_email_account_default_serialization.py:241`
- `tests/test_email_account_default_serialization.py:278`
- `tests/test_request_authority.py:375`
- `static/js/editor/brush-engine.js:62`
- `static/js/editor/direct-manipulation-session.js:24`
- `static/js/editor/render-cancellation.js:5`
- `static/js/editor/stroke-pipeline.js:390`
- `static/js/editor/tools/clone.js:7`
- `static/js/editor/tools/clone.js:25`
- `static/js/editor/tools/crop.js:51`
- `static/js/editor/tools/crop.js:61`
- `static/js/editor/tools/crop.js:72`
- `static/js/editor/tools/gradient.js:58`
- `static/js/editor/tools/lasso.js:84`
- `static/js/editor/tools/liquify.js:141`
- `static/js/editor/tools/marquee.js:51`
- `static/js/editor/tools/marquee.js:61`
- `static/js/editor/tools/marquee.js:80`
- `static/js/editor/tools/move.js:47`
- `static/js/editor/tools/patch.js:6`
- `static/js/editor/tools/pen-path.js:37`
- `static/js/editor/tools/pen-selection.js:50`
- `static/js/editor/tools/stroke.js:16`
- `static/js/editor/tools/transform-drag.js:75`
- `static/js/editor/tools/transform-drag.js:86`
- `static/js/galleryEditor.js:4016`
- `static/js/galleryEditor.js:5572`
- `static/js/galleryEditor.js:5573`
- `static/js/galleryEditor.js:5574`
- `static/js/galleryEditor.js:5575`
- `static/js/galleryEditor.js:5590`
- `static/js/galleryEditor.js:5591`
- `static/js/galleryEditor.js:5592`
- `static/js/galleryEditor.js:5596`
- `static/js/galleryEditor.js:5597`
- `static/js/galleryEditor.js:7164`
- `static/js/windowResize.js:124`
- `static/js/windowResize.js:197`

## `drag` — method?, line 156
- **called from:**
- `static/js/dragSort.js:138`
- `static/js/editor/state.js:247`
- `static/js/editor/tools/crop.js:75`
- `static/js/editor/tools/gradient.js:71`
- `static/js/editor/tools/lasso.js:95`
- `static/js/editor/tools/liquify.js:156`
- `static/js/editor/tools/marquee.js:83`
- `static/js/editor/tools/move.js:84`
- `static/js/editor/tools/patch.js:6`
- `static/js/editor/tools/pen-path.js:43`
- `static/js/editor/tools/pen-selection.js:65`
- `static/js/galleryEditor.js:5560`
- `static/js/galleryEditor.js:5612`
- `static/js/galleryEditor.js:5613`
- `static/js/galleryEditor.js:5620`
- `static/js/galleryEditor.js:5669`
- `static/js/galleryEditor.js:5670`
- `static/js/galleryEditor.js:5672`
- `static/js/galleryEditor.js:5673`
- `static/js/galleryEditor.js:5674`
- `static/js/galleryEditor.js:7165`
- `static/js/windowDrag.js:24`
- `static/js/windowDrag.js:30`

## `end` — method?, line 163
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
- `src/agent_loop.py:25736`
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

## `cancel` — method?, line 172
- **called from:**
- `app.py:1459`
- `app.py:1470`
- `routes/editor_agent_routes.py:1414`
- `routes/email/email_routes.py:6869`
- `routes/shell_routes.py:957`
- `routes/shell_routes.py:1342`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `services/skills/job_coordinator.py:215`
- `src/agent_loop.py:26017`
- `src/agent_loop.py:34321`
- `src/agent_runs.py:86`
- `src/agent_runs.py:207`
- `src/agent_runs.py:210`
- `src/agent_runs.py:249`
- `src/agent_runs.py:298`
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
- `tests/test_nested_invocation_ownership.py:453`
- `tests/test_review_calendar_invitation.py:135`
- … +82 more (grep the name in repo)
