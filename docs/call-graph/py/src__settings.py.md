# `src/settings.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_invalidate_caches` — function, line 31
- **called from:**
- `src/settings.py:279`
- `src/settings.py:364`
- `tests/test_settings_store_shape.py:8`
- `tests/test_settings_store_shape.py:18`

## `without_retired_settings` — function, line 233
- **called from:**
- `routes/auth_routes.py:721`
- `routes/auth_routes.py:755`

## `load_settings` — function, line 257
- **called from:**
- `mcp_servers/image_gen_server.py:65`
- `routes/backup_routes.py:35`
- `routes/backup_routes.py:196`
- `routes/cookbook_routes.py:1559`
- `routes/cookbook_routes.py:1581`
- `routes/note/note_routes.py:162`
- `routes/skills_routes.py:1328`
- `routes/skills_routes.py:1342`
- `services/search/providers.py:36`
- `services/stt/stt_service.py:32`
- `services/tts/tts_service.py:55`
- `src/agent_tools/admin_tools.py:636`
- `src/agent_tools/admin_tools.py:650`
- `src/agent_tools/admin_tools.py:676`
- `src/agent_tools/admin_tools.py:696`
- `src/agent_tools/admin_tools.py:752`
- `src/ai_interaction.py:967`
- `src/ai_interaction.py:1215`
- `src/ai_interaction.py:1485`
- `src/builtin_actions.py:1073`
- `src/builtin_actions.py:2265`
- `src/document_processor.py:307`
- `src/endpoint_resolver.py:364`
- `src/endpoint_resolver.py:616`
- `src/model_context.py:289`
- `src/service_health.py:422`
- `src/settings.py:284`
- `tests/test_budget_auto_sentinel.py:37`
- `tests/test_settings_error_paths.py:34`
- `tests/test_settings_error_paths.py:43`
- `tests/test_settings_error_paths.py:77`
- `tests/test_settings_store_shape.py:10`

## `save_settings` — function, line 275
- **called from:**
- `routes/backup_routes.py:198`
- `routes/cookbook_routes.py:1562`
- `routes/cookbook_routes.py:1585`
- `routes/skills_routes.py:1334`
- `routes/skills_routes.py:1347`
- `src/agent_tools/admin_tools.py:685`
- `src/agent_tools/admin_tools.py:698`
- `src/agent_tools/admin_tools.py:763`
- `tests/test_budget_auto_sentinel.py:39`

## `get_setting` — function, line 282
- **called from:**
- `app.py:1249`
- `app.py:1259`
- `app.py:1261`
- `mcp_servers/email_server.py:1388`
- `mcp_servers/image_gen_server.py:62`
- `mcp_servers/image_gen_server.py:129`
- `routes/chat_routes.py:1752`
- `routes/chat_routes.py:2116`
- `routes/chat_routes.py:2664`
- `routes/chat_routes.py:2670`
- `routes/skills_routes.py:557`
- `routes/skills_routes.py:1128`
- `routes/skills_routes.py:1129`
- `scripts/dump_agent_prompt.py:141`
- `services/research/research_handler.py:271`
- `src/agent_loop.py:810`
- `src/agent_loop.py:3083`
- `src/agent_loop.py:3089`
- `src/agent_loop.py:3330`
- `src/agent_loop.py:4054`
- `src/agent_loop.py:4280`
- `src/agent_loop.py:4729`
- `src/agent_loop.py:4736`
- `src/agent_loop.py:5044`
- `src/agent_loop.py:5333`
- `src/agent_loop.py:6007`
- `src/agent_tools/admin_tools.py:736`
- `src/agent_tools/model_interaction_tools.py:92`
- `src/agent_tools/spawn_agent_tools.py:112`
- `src/chat_handler.py:207`
- `src/chat_handler.py:262`
- `src/chat_helpers.py:289`
- `src/chat_helpers.py:291`
- `src/llm_core.py:1508`
- `src/research_handler.py:277`
- `src/research_handler.py:791`
- `src/research_handler.py:793`
- `src/research_handler.py:799`
- `src/research_handler.py:805`
- `src/research_handler.py:811`
- `src/settings.py:337`
- `src/task_scheduler.py:1622`
- `src/task_scheduler.py:2062`
- `src/task_scheduler.py:2063`
- `src/task_scheduler.py:2064`
- `src/teacher_escalation.py:491`
- `src/teacher_escalation.py:493`
- `src/teacher_escalation.py:508`
- `src/teacher_escalation.py:561`
- `src/teacher_escalation.py:563`
- `src/teacher_escalation.py:588`
- `src/tool_execution.py:336`
- `tests/test_agent_tool_budget_nonnumeric.py:67`
- `tests/test_budget_auto_sentinel.py:50`
- `tests/test_context_budget.py:111`
- `tests/test_context_budget.py:117`

## `is_setting_overridden` — function, line 287
- **called from:**
- `tests/test_budget_auto_sentinel.py:49`
- `tests/test_context_budget.py:47`
- `tests/test_context_budget.py:48`
- `tests/test_context_budget.py:51`
- `tests/test_settings_store_shape.py:11`

## `get_user_setting` — function, line 321
- **called from:**
- `src/endpoint_resolver.py:370`
- `src/endpoint_resolver.py:617`

## `load_features` — function, line 342
- **called from:**
- `routes/backup_routes.py:38`
- `routes/backup_routes.py:203`
- `tests/test_load_features_permission_error.py:25`
- `tests/test_settings_store_shape.py:20`

## `save_features` — function, line 360
- **called from:**
- `routes/backup_routes.py:205`
