# `static/js/editor/tools/stroke.js` — definitions & call sites

8 definitions (regex-based, best-effort).
**Exports:** `createStrokeTool`

## `strokeLabel` — function, line 39
- **called from:**
- `static/js/editor/tools/stroke.js:39`
- `static/js/editor/tools/stroke.js:122`

## `pointerPressure` — function, line 50
- **called from:**
- `static/js/editor/tools/stroke.js:50`
- `static/js/editor/tools/stroke.js:57`

## `eventSample` — function, line 55
- **called from:**
- `static/js/editor/tools/stroke.js:55`
- `static/js/editor/tools/stroke.js:124`
- `static/js/editor/tools/stroke.js:137`
- `static/js/editor/tools/stroke.js:148`

## `createStrokeTool` — function, line 60
- **called from:**
- `static/js/editor/tools/stroke.js:60`
- `static/js/galleryEditor.js:7186`

## `tryBegin` — method?, line 70
- **called from:**
- `static/js/editor/tools/stroke.js:70`
- `static/js/editor/tools/transform-drag.js:52`
- `static/js/galleryEditor.js:5562`
- `static/js/galleryEditor.js:5601`

## `tryContinue` — method?, line 132
- **called from:**
- `static/js/editor/tools/stroke.js:132`
- `static/js/editor/tools/transform-drag.js:99`
- `static/js/galleryEditor.js:5660`
- `static/js/galleryEditor.js:5667`

## `tryEnd` — method?, line 144
- **called from:**
- `static/js/editor/tools/stroke.js:144`
- `static/js/editor/tools/transform-drag.js:249`
- `static/js/galleryEditor.js:5339`
- `static/js/galleryEditor.js:5687`
- `static/js/galleryEditor.js:5699`
- `static/js/galleryEditor.js:9946`
- `static/js/galleryEditor.js:9953`

## `cancel` — method?, line 158
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
