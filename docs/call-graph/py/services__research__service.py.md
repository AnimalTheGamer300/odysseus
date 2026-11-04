# `services/research/service.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ResearchSource` — class, line 16
- decorator: `dataclass`
- **called from:**
- `services/research/service.py:88`
- `services/research/service.py:144`

## `ResearchResult` — class, line 25
- decorator: `dataclass`
- **called from:**
- `services/research/service.py:97`
- `services/research/service.py:107`

## `ResearchService` — class, line 35
- **called from:**
- `tests/test_research_service.py:64`
- `tests/test_research_service.py:133`

## `ResearchService.__init__` — method, line 45
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

## `ResearchService.research` — method (async), line 49
- **called from:**
- `services/research/research_handler.py:278`
- `src/research_handler.py:837`
- `src/task_scheduler.py:2078`
- `tests/test_research_service.py:70`
- `tests/test_research_service.py:75`
- `tests/test_research_service.py:81`
- `tests/test_research_service.py:91`
- `tests/test_research_service.py:97`
- `tests/test_research_service.py:102`
- `tests/test_research_service.py:149`
- `static/js/research/panel.js:1213`

## `ResearchService._parse_sources` — method, line 115
- decorator: `staticmethod`
- **called from:**
- `services/research/service.py:110`
- `tests/test_research_service.py:109`
- `tests/test_research_service.py:113`
- `tests/test_research_service.py:125`

## `ResearchService.start_background` — method, line 148
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ResearchService.get_status` — method, line 161
- **called from:**
- `routes/chat_routes.py:1943`
- `routes/research/research_routes.py:284`
- `routes/research/research_routes.py:589`
- `services/research/service.py:163`
- `tests/test_research_handler_path_confinement.py:54`
- `tests/test_research_status_avg_duration.py:22`
- `tests/test_research_status_avg_duration.py:34`
- `tests/test_research_status_avg_duration.py:35`
- `tests/test_research_status_avg_duration.py:36`

## `ResearchService.cancel` — method, line 165
- **called from:**
- `app.py:1283`
- `routes/shell_routes.py:723`
- `routes/shell_routes.py:1108`
- `routes/skills_routes.py:1800`
- `services/research/research_handler.py:140`
- `services/research/research_handler.py:143`
- `services/shell/service.py:163`
- `src/agent_loop.py:5124`
- `src/agent_loop.py:6401`
- `src/agent_runs.py:84`
- `src/agent_runs.py:195`
- `src/agent_runs.py:198`
- `src/agent_runs.py:237`
- `src/agent_runs.py:286`
- `src/agent_tools/subprocess_tools.py:273`
- `src/agent_tools/subprocess_tools.py:275`
- `src/agent_tools/subprocess_tools.py:279`
- `src/ai_interaction.py:1379`
- `src/ai_interaction.py:1646`
- `src/llm_core.py:109`
- `src/mcp_manager.py:400`
- `src/mcp_oauth.py:63`
- `src/research_handler.py:456`
- `src/research_handler.py:459`
- `src/task_scheduler.py:100`
- `src/task_scheduler.py:591`
- `src/task_scheduler.py:599`
- `src/task_scheduler.py:917`
- `src/task_scheduler.py:1012`
- `src/task_scheduler.py:2272`
- `src/task_scheduler.py:2296`
- `tests/test_builtin_mcp_bg_tasks.py:101`
- `tests/test_compare_stop_disconnect_poll.py:376`
- `tests/test_compare_stop_disconnect_poll.py:433`
- `tests/test_email_summary_llm.py:192`
- `tests/test_email_urgency_checkpoint.py:419`
- `tests/test_email_urgency_checkpoint.py:554`
- `tests/test_task_scheduler_cache.py:34`
- `tests/test_task_scheduler_cache.py:70`
- `static/js/chat.js:2841`
- `static/js/chat.js:5741`
- `static/js/chat.js:5756`
- `static/js/documentLibrary.js:180`
- `static/js/gallery.js:2576`
- `static/js/gallery.js:2584`
- `static/js/liveThinkingThrottle.js:20`
- `static/js/liveThinkingThrottle.js:22`
- `static/js/liveThinkingThrottle.js:193`
- `static/js/liveThinkingThrottle.js:198`
- `static/js/liveThinkingThrottle.js:199`
- `static/js/settings.js:883`
- `static/js/slashCommands.js:2439`
- `static/js/tasks.js:1076`
- `static/js/tts-ai.js:241`
- `static/js/windowDrag.js:157`
