# `src/settings.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_invalidate_caches` — function, line 31
- **called from:**
- `src/settings.py:292`
- `src/settings.py:392`
- `tests/test_settings_store_shape.py:8`
- `tests/test_settings_store_shape.py:18`

## `without_retired_settings` — function, line 246
- **called from:**
- `routes/auth_routes.py:780`
- `routes/auth_routes.py:830`

## `load_settings` — function, line 270
- **called from:**
- `mcp_servers/image_gen_server.py:65`
- `routes/backup_routes.py:35`
- `routes/backup_routes.py:196`
- `routes/cookbook_routes.py:1458`
- `routes/cookbook_routes.py:1481`
- `routes/gallery/gallery_routes.py:670`
- `routes/note/note_routes.py:165`
- `routes/skills_routes.py:437`
- `routes/skills_routes.py:451`
- `services/search/providers.py:37`
- `services/stt/stt_service.py:32`
- `services/tts/tts_service.py:55`
- `src/agent_tools/admin_tools.py:655`
- `src/agent_tools/admin_tools.py:669`
- `src/agent_tools/admin_tools.py:695`
- `src/agent_tools/admin_tools.py:715`
- `src/agent_tools/admin_tools.py:794`
- `src/ai_interaction.py:1186`
- `src/ai_interaction.py:1280`
- `src/ai_interaction.py:1579`
- `src/ai_interaction.py:1933`
- `src/builtin_actions.py:1219`
- `src/builtin_actions.py:2346`
- `src/builtin_actions.py:2609`
- `src/clean_agent_preview.py:5816`
- `src/document_processor.py:413`
- `src/editor_agent_model.py:59`
- `src/editor_agent_model.py:678`
- `src/editor_image_settings.py:6`
- `src/endpoint_resolver.py:461`
- `src/endpoint_resolver.py:713`
- `src/model_context.py:294`
- `src/service_health.py:440`
- `src/settings.py:297`
- `src/tools/image.py:126`
- `src/tools/image.py:155`
- `src/utility_effort.py:45`
- `tests/test_budget_auto_sentinel.py:37`
- `tests/test_settings_error_paths.py:34`
- `tests/test_settings_error_paths.py:43`
- `tests/test_settings_error_paths.py:77`
- `tests/test_settings_store_shape.py:10`

## `save_settings` — function, line 288
- **called from:**
- `routes/backup_routes.py:198`
- `routes/cookbook_routes.py:1461`
- `routes/cookbook_routes.py:1485`
- `routes/skills_routes.py:443`
- `routes/skills_routes.py:456`
- `src/agent_tools/admin_tools.py:704`
- `src/agent_tools/admin_tools.py:717`
- `src/agent_tools/admin_tools.py:802`
- `tests/test_budget_auto_sentinel.py:39`

## `get_setting` — function, line 295
- **called from:**
- `mcp_servers/email_server.py:2579`
- `mcp_servers/image_gen_server.py:62`
- `mcp_servers/image_gen_server.py:129`
- `routes/chat_routes.py:3722`
- `routes/chat_routes.py:4413`
- `routes/chat_routes.py:4983`
- `routes/chat_routes.py:4989`
- `routes/editor_agent_routes.py:1699`
- `scripts/dump_agent_prompt.py:141`
- `services/memory/skills.py:68`
- `services/research/research_handler.py:271`
- `services/skills/model_selection.py:66`
- `services/skills/model_selection.py:67`
- `services/skills/publication.py:20`
- `src/agent_loop.py:8465`
- `src/agent_loop.py:10618`
- `src/agent_loop.py:10628`
- `src/agent_loop.py:15284`
- `src/agent_loop.py:15290`
- `src/agent_loop.py:15586`
- `src/agent_loop.py:17386`
- `src/agent_loop.py:21900`
- `src/agent_loop.py:22834`
- `src/agent_loop.py:24620`
- `src/agent_loop.py:24627`
- `src/agent_loop.py:25860`
- `src/agent_loop.py:26800`
- `src/agent_loop.py:31350`
- `src/agent_tools/admin_tools.py:777`
- `src/agent_tools/model_interaction_tools.py:92`
- `src/agent_tools/spawn_agent_tools.py:112`
- `src/bg_monitor.py:185`
- `src/chat_handler.py:212`
- `src/chat_handler.py:272`
- `src/chat_helpers.py:348`
- `src/chat_helpers.py:350`
- `src/context_compactor.py:193`
- `src/deep_research.py:813`
- `src/deep_research.py:1456`
- `src/llm_core.py:1855`
- `src/research_handler.py:293`
- `src/research_handler.py:1019`
- `src/research_handler.py:1021`
- `src/research_handler.py:1027`
- `src/research_handler.py:1033`
- `src/research_handler.py:1039`
- `src/settings.py:344`
- `src/settings.py:365`
- `src/task_scheduler.py:1386`
- `src/task_scheduler.py:1782`
- `src/task_scheduler.py:2195`
- `src/teacher_escalation.py:547`
- `src/teacher_escalation.py:549`
- `src/teacher_escalation.py:564`
- `src/teacher_escalation.py:622`
- `src/teacher_escalation.py:624`
- `src/teacher_escalation.py:649`
- `src/tool_execution.py:1023`
- `tests/test_agent_tool_budget_nonnumeric.py:67`
- `tests/test_budget_auto_sentinel.py:50`
- … +2 more (grep the name in repo)

## `is_setting_overridden` — function, line 300
- **called from:**
- `tests/test_budget_auto_sentinel.py:49`
- `tests/test_context_budget.py:74`
- `tests/test_context_budget.py:75`
- `tests/test_context_budget.py:78`
- `tests/test_settings_store_shape.py:11`

## `get_user_setting` — function, line 335
- **called from:**
- `src/ai_interaction.py:1186`
- `src/ai_interaction.py:1290`
- `src/ai_interaction.py:1295`
- `src/ai_interaction.py:1297`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1588`
- `src/editor_agent_model.py:679`
- `src/editor_image_settings.py:10`
- `src/editor_image_settings.py:11`
- `src/endpoint_resolver.py:467`
- `src/endpoint_resolver.py:714`
- `src/utility_effort.py:36`
- `src/utility_effort.py:46`
- `tests/test_editor_generation_model_routing.py:315`
- `tests/test_editor_generation_model_routing.py:370`
- `tests/test_editor_generation_model_routing.py:424`
- `tests/test_editor_generation_model_routing.py:500`

## `load_features` — function, line 370
- **called from:**
- `routes/backup_routes.py:38`
- `routes/backup_routes.py:203`
- `tests/test_load_features_permission_error.py:25`
- `tests/test_settings_store_shape.py:20`

## `save_features` — function, line 388
- **called from:**
- `routes/backup_routes.py:205`
