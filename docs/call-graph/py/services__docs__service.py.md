# `services/docs/service.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `DocChunk` — class, line 12
- decorator: `dataclass`
- **called from:**
- `services/docs/service.py:84`

## `IndexResult` — class, line 21
- decorator: `dataclass`
- **called from:**
- `services/docs/service.py:105`

## `DocsService` — class, line 28
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `DocsService.__init__` — method, line 38
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `DocsService.query` — method (async), line 41
- **called from:**
- `app.py:361`
- `app.py:487`
- `app.py:586`
- `app.py:592`
- `app.py:601`
- `app.py:1206`
- `app.py:1208`
- `app.py:1352`
- `companion/routes.py:135`
- `core/auth.py:327`
- `core/auth.py:472`
- `core/database.py:564`
- `core/database.py:3015`
- `core/database.py:3027`
- `core/database.py:3028`
- `core/database.py:3029`
- `core/database.py:3030`
- `core/database.py:3031`
- `core/database.py:3056`
- `core/database.py:3071`
- `core/database.py:3084`
- `core/database.py:3093`
- `core/database.py:3105`
- `core/database.py:3124`
- `core/session_manager.py:137`
- `core/session_manager.py:149`
- `core/session_manager.py:258`
- `core/session_manager.py:370`
- `core/session_manager.py:464`
- `core/session_manager.py:498`
- `core/session_manager.py:527`
- `core/session_manager.py:532`
- `core/session_manager.py:597`
- `core/session_manager.py:630`
- `core/session_manager.py:639`
- `core/session_manager.py:674`
- `core/session_manager.py:706`
- `core/session_manager.py:843`
- `core/session_manager.py:863`
- `core/session_manager.py:882`
- `core/session_manager.py:909`
- `core/session_manager.py:989`
- `core/session_manager.py:994`
- `core/session_manager.py:997`
- `core/session_manager.py:1033`
- `core/session_manager.py:1053`
- `core/session_manager.py:1070`
- `core/session_manager.py:1134`
- `mcp_servers/email_server.py:2837`
- `routes/admin_wipe/admin_wipe_routes.py:79`
- `routes/admin_wipe/admin_wipe_routes.py:80`
- `routes/admin_wipe/admin_wipe_routes.py:81`
- `routes/admin_wipe/admin_wipe_routes.py:90`
- `routes/admin_wipe/admin_wipe_routes.py:91`
- `routes/admin_wipe/admin_wipe_routes.py:127`
- `routes/admin_wipe/admin_wipe_routes.py:128`
- `routes/admin_wipe/admin_wipe_routes.py:134`
- `routes/admin_wipe/admin_wipe_routes.py:135`
- `routes/admin_wipe/admin_wipe_routes.py:136`
- `routes/admin_wipe/admin_wipe_routes.py:142`
- … +844 more (grep the name in repo)

## `DocsService.index` — method (async), line 94
- **called from:**
- `routes/api_token_routes.py:63`
- `routes/calendar_routes.py:593`
- `routes/cookbook_helpers.py:325`
- `routes/cookbook_routes.py:530`
- `routes/history/history_routes.py:614`
- `scripts/eval_exact_file_routing.py:74`
- `scripts/eval_followup_domain_continuity.py:83`
- `scripts/generate_env_reference.py:254`
- `services/hwfit/profiles.py:155`
- `services/youtube/youtube_handler.py:198`
- `src/agent_evidence.py:945`
- `src/agent_runtime/identity.py:125`
- `src/agent_tools/document_tools.py:897`
- `src/agent_tools/document_tools.py:1036`
- `src/builtin_mcp.py:267`
- `src/llm_core.py:1946`
- `src/report_math.py:40`
- `src/tools/system.py:323`
- `src/webhook_manager.py:292`
- `tests/containment_helpers.py:19`
- `tests/containment_helpers.py:23`
- `tests/helpers/document_source.py:105`
- `tests/test_action_menu_order.py:99`
- `tests/test_action_menu_order.py:100`
- `tests/test_action_menu_order.py:133`
- `tests/test_action_menu_order.py:134`
- `tests/test_action_menu_order.py:184`
- `tests/test_action_menu_order.py:184`
- `tests/test_action_menu_order.py:193`
- `tests/test_action_menu_order.py:193`
- `tests/test_action_menu_order.py:193`
- `tests/test_action_menu_order.py:194`
- `tests/test_action_menu_order.py:194`
- `tests/test_action_menu_order.py:200`
- `tests/test_action_menu_order.py:200`
- `tests/test_action_menu_order.py:215`
- `tests/test_action_menu_order.py:216`
- `tests/test_action_menu_order.py:228`
- `tests/test_action_menu_order.py:229`
- `tests/test_action_menu_order.py:239`
- `tests/test_action_menu_order.py:240`
- `tests/test_action_menu_order.py:246`
- `tests/test_action_menu_order.py:247`
- `tests/test_action_menu_order.py:250`
- `tests/test_action_menu_order.py:250`
- `tests/test_action_menu_order.py:252`
- `tests/test_action_menu_order.py:253`
- `tests/test_action_menu_order.py:260`
- `tests/test_action_menu_order.py:261`
- `tests/test_action_menu_order.py:269`
- `tests/test_action_menu_order.py:270`
- `tests/test_action_menu_order.py:273`
- `tests/test_action_menu_order.py:273`
- `tests/test_action_menu_order.py:273`
- `tests/test_action_menu_order.py:280`
- `tests/test_action_menu_order.py:281`
- `tests/test_action_menu_order.py:291`
- `tests/test_action_menu_order.py:292`
- `tests/test_action_menu_order.py:302`
- `tests/test_action_menu_order.py:303`
- … +1069 more (grep the name in repo)

## `DocsService.add_document` — method (async), line 111
- **called from:**
- `routes/personal_routes.py:367`
- `services/docs/service.py:113`
- `src/rag_manager.py:66`
- `src/rag_vector.py:540`
- `tests/test_embedding_lanes_rag.py:26`

## `DocsService.get_stats` — method, line 115
- **called from:**
- `routes/diagnostics_routes.py:70`
- `routes/stt_routes.py:20`
- `routes/tts_routes.py:25`
- `scripts/index_documents.py:103`
- `services/docs/service.py:117`
- `services/research/research_handler.py:281`
- `src/rag_manager.py:62`
- `src/research_handler.py:382`
- `src/research_handler.py:406`
- `src/research_handler.py:1074`
- `src/task_scheduler.py:2275`
- `tests/test_deep_research_action_planning.py:490`
- `tests/test_tts_cache_stats.py:10`
- `tests/test_tts_speed_malformed.py:22`

## `DocsService.rebuild_index` — method, line 119
- **called from:**
- `services/docs/service.py:121`
- `src/rag_manager.py:58`
- `tests/test_embedding_lanes_rag.py:106`
