# `src/rag_manager.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `RAGManager` — class, line 23
- **called from:**
- `scripts/index_documents.py:48`
- `services/docs/service.py:39`
- `tests/test_rag_search_signature.py:13`

## `RAGManager.__init__` — method, line 29
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

## `RAGManager.search` — method, line 35
- **called from:**
- `mcp_servers/email_server.py:63`
- `mcp_servers/email_server.py:457`
- `mcp_servers/email_server.py:463`
- `mcp_servers/email_server.py:476`
- `mcp_servers/email_server.py:560`
- `mcp_servers/email_server.py:629`
- `mcp_servers/email_server.py:1351`
- `mcp_servers/email_server.py:1354`
- `mcp_servers/email_server.py:2720`
- `routes/calendar_routes.py:1881`
- `routes/chat_helpers.py:39`
- `routes/chat_helpers.py:152`
- `routes/chat_helpers.py:698`
- `routes/chat_helpers.py:1379`
- `routes/chat_helpers.py:1776`
- `routes/chat_helpers.py:1804`
- `routes/chat_routes.py:247`
- `routes/chat_routes.py:256`
- `routes/chat_routes.py:266`
- `routes/chat_routes.py:276`
- `routes/chat_routes.py:291`
- `routes/chat_routes.py:314`
- `routes/chat_routes.py:325`
- `routes/chat_routes.py:346`
- `routes/chat_routes.py:347`
- `routes/chat_routes.py:355`
- `routes/chat_routes.py:359`
- `routes/chat_routes.py:388`
- `routes/chat_routes.py:389`
- `routes/chat_routes.py:1209`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1705`
- `routes/chat_routes.py:1818`
- `routes/chat_routes.py:1819`
- `routes/chat_routes.py:1822`
- `routes/chat_routes.py:1893`
- `routes/chat_routes.py:2776`
- `routes/chat_routes.py:2782`
- `routes/chat_routes.py:2798`
- `routes/chat_routes.py:2801`
- `routes/chat_routes.py:3466`
- `routes/chat_routes.py:3616`
- `routes/chat_routes.py:3617`
- `routes/contacts/contacts_routes.py:617`
- `routes/contacts/contacts_routes.py:621`
- `routes/contacts/contacts_routes.py:625`
- `routes/cookbook_helpers.py:684`
- `routes/cookbook_helpers.py:1302`
- `routes/cookbook_helpers.py:1305`
- `routes/cookbook_helpers.py:1623`
- `routes/cookbook_helpers.py:1625`
- `routes/cookbook_helpers.py:1625`
- `routes/cookbook_output.py:70`
- `routes/cookbook_routes.py:136`
- `routes/cookbook_routes.py:159`
- `routes/cookbook_routes.py:792`
- `routes/cookbook_routes.py:864`
- `routes/cookbook_routes.py:1423`
- `routes/cookbook_routes.py:1716`
- `routes/cookbook_routes.py:1717`
- … +2629 more (grep the name in repo)

## `RAGManager.index_personal_documents` — method, line 39
- **called from:**
- `mcp_servers/rag_server.py:116`
- `routes/personal_routes.py:218`
- `scripts/index_documents.py:85`
- `services/docs/service.py:104`
- `src/ai_interaction.py:666`
- `src/personal_docs.py:306`
- `src/personal_docs.py:463`
- `src/personal_docs.py:479`
- `src/rag_manager.py:46`
- `src/rag_vector.py:605`
- `tests/test_rag_index_hidden_dirs.py:46`
- `tests/test_rag_index_hidden_dirs.py:60`
- `tests/test_rag_index_hidden_dirs.py:75`
- `tests/test_rag_manager_owner_compat.py:25`

## `RAGManager.retrieve` — method, line 52
- **called from:**
- `src/rag_manager.py:54`
- `src/tool_index.py:620`
- `src/tool_index.py:857`
- `tests/test_embedding_lanes_tool_index.py:33`
- `tests/test_embedding_lanes_tool_index.py:116`
- `tests/test_embedding_lanes_tool_index.py:178`

## `RAGManager.rebuild_index` — method, line 56
- **called from:**
- `services/docs/service.py:121`
- `src/rag_manager.py:58`
- `tests/test_embedding_lanes_rag.py:106`

## `RAGManager.get_stats` — method, line 60
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

## `RAGManager.add_document` — method, line 64
- **called from:**
- `routes/personal_routes.py:367`
- `services/docs/service.py:113`
- `src/rag_manager.py:66`
- `src/rag_vector.py:540`
- `tests/test_embedding_lanes_rag.py:26`

## `RAGManager.add_documents_batch` — method, line 68
- **called from:**
- `src/rag_manager.py:70`
- `tests/test_embedding_lanes_rag.py:47`
- `tests/test_embedding_lanes_rag.py:69`
