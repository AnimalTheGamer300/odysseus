# `src/chat_processor.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_clean_search_query` — function, line 16
- **called from:**
- `src/chat_processor.py:476`
- `tests/test_web_search_query_sanitization.py:36`
- `tests/test_web_search_query_sanitization.py:50`
- `tests/test_web_search_query_sanitization.py:62`
- `tests/test_web_search_query_sanitization.py:75`
- `tests/test_web_search_query_sanitization.py:76`

## `_content_tokens` — function, line 77
- **called from:**
- `src/chat_processor.py:177`
- `src/chat_processor.py:198`

## `ChatProcessor` — class, line 83
- **called from:**
- `src/app_initializer.py:129`
- `tests/test_c5_rag_disable.py:50`
- `tests/test_chat_processor_pinned_memory.py:27`
- `tests/test_chat_processor_web_search.py:13`
- `tests/test_chat_processor_web_search.py:36`
- `tests/test_chat_processor_web_search.py:58`
- `tests/test_chat_processor_web_search.py:81`
- `tests/test_chat_url_prefetch_failure_context.py:12`
- `tests/test_user_time.py:149`
- `tests/test_web_search_query_sanitization.py:143`
- `tests/test_web_search_query_sanitization.py:173`
- `tests/test_web_search_query_sanitization.py:197`

## `ChatProcessor.__init__` — method, line 84
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

## `ChatProcessor._is_core_memory` — method, line 99
- **called from:**
- `src/chat_processor.py:130`

## `ChatProcessor._select_pinned_memories` — method, line 116
- **called from:**
- `src/chat_processor.py:353`

## `ChatProcessor._is_memory_management_request` — method, line 156
- decorator: `staticmethod`
- **called from:**
- `src/chat_processor.py:346`
- `tests/test_chat_processor_pinned_memory.py:203`
- `tests/test_chat_processor_pinned_memory.py:204`
- `tests/test_chat_processor_pinned_memory.py:205`

## `ChatProcessor._hybrid_retrieve` — method, line 167
- **called from:**
- `src/chat_processor.py:139`
- `src/chat_processor.py:370`

## `ChatProcessor._bm25_score` — method, line 208
- **called from:**
- `src/chat_processor.py:242`

## `ChatProcessor.build_context_preface` — method, line 285
- **called from:**
- `routes/chat_helpers.py:1409`
- `tests/test_chat_processor_pinned_memory.py:55`
- `tests/test_chat_processor_pinned_memory.py:86`
- `tests/test_chat_processor_pinned_memory.py:111`
- `tests/test_chat_processor_pinned_memory.py:134`
- `tests/test_chat_processor_pinned_memory.py:170`
- `tests/test_chat_processor_pinned_memory.py:191`
- `tests/test_chat_processor_web_search.py:16`
- `tests/test_chat_processor_web_search.py:39`
- `tests/test_chat_processor_web_search.py:61`
- `tests/test_chat_processor_web_search.py:84`
- `tests/test_chat_url_prefetch_failure_context.py:29`
- `tests/test_chat_url_prefetch_failure_context.py:64`
- `tests/test_chat_url_prefetch_failure_context.py:99`
- `tests/test_chat_url_prefetch_failure_context.py:118`
- `tests/test_chat_url_prefetch_failure_context.py:140`
- `tests/test_chat_url_prefetch_failure_context.py:162`
- `tests/test_user_time.py:151`
- `tests/test_web_search_query_sanitization.py:144`
- `tests/test_web_search_query_sanitization.py:174`
- `tests/test_web_search_query_sanitization.py:198`
