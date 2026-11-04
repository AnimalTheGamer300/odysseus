# `src/chat_processor.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_clean_search_query` — function, line 16
- **called from:**
- `src/chat_processor.py:458`
- `tests/test_web_search_query_sanitization.py:36`
- `tests/test_web_search_query_sanitization.py:50`
- `tests/test_web_search_query_sanitization.py:62`
- `tests/test_web_search_query_sanitization.py:75`
- `tests/test_web_search_query_sanitization.py:76`

## `_content_tokens` — function, line 77
- **called from:**
- `src/chat_processor.py:171`
- `src/chat_processor.py:192`

## `ChatProcessor` — class, line 83
- **called from:**
- `src/app_initializer.py:129`
- `tests/test_chat_processor_pinned_memory.py:27`
- `tests/test_chat_processor_web_search.py:13`
- `tests/test_chat_processor_web_search.py:36`
- `tests/test_chat_processor_web_search.py:58`
- `tests/test_chat_processor_web_search.py:81`
- `tests/test_chat_url_prefetch_failure_context.py:12`
- `tests/test_user_time.py:99`
- `tests/test_web_search_query_sanitization.py:143`
- `tests/test_web_search_query_sanitization.py:173`
- `tests/test_web_search_query_sanitization.py:197`

## `ChatProcessor.__init__` — method, line 84
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

## `ChatProcessor._is_core_memory` — method, line 98
- **called from:**
- `src/chat_processor.py:134`

## `ChatProcessor._select_pinned_memories` — method, line 115
- **called from:**
- `src/chat_processor.py:335`

## `ChatProcessor._recent_first` — method, line 127
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatProcessor._hybrid_retrieve` — method, line 161
- **called from:**
- `src/chat_processor.py:145`
- `src/chat_processor.py:352`

## `ChatProcessor._bm25_score` — method, line 202
- **called from:**
- `src/chat_processor.py:236`

## `ChatProcessor.build_context_preface` — method, line 279
- **called from:**
- `routes/chat_helpers.py:839`
- `tests/test_chat_processor_pinned_memory.py:55`
- `tests/test_chat_processor_pinned_memory.py:86`
- `tests/test_chat_processor_pinned_memory.py:111`
- `tests/test_chat_processor_pinned_memory.py:144`
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
- `tests/test_user_time.py:101`
- `tests/test_web_search_query_sanitization.py:144`
- `tests/test_web_search_query_sanitization.py:174`
- `tests/test_web_search_query_sanitization.py:198`
