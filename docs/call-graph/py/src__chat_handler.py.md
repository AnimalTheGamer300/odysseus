# `src/chat_handler.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sync_upload_vision_to_gallery` — function, line 32
- **called from:**
- `src/chat_handler.py:259`
- `src/chat_handler.py:279`
- `src/chat_handler.py:291`

## `ChatHandler` — class, line 60
- **called from:**
- `src/app_initializer.py:133`
- `tests/test_chat_preprocess_tool_policy.py:32`
- `tests/test_security_regressions.py:414`
- `tests/test_vision_description_provenance.py:55`

## `ChatHandler.__init__` — method, line 63
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

## `ChatHandler.validate_and_extract_preset` — method, line 83
- **called from:**
- `routes/chat_helpers.py:839`

## `ChatHandler.enhance_message_if_needed` — method, line 120
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatHandler.preprocess_message` — method (async), line 128
- **called from:**
- `routes/chat_helpers.py:858`
- `tests/test_chat_preprocess_tool_policy.py:42`
- `tests/test_security_regressions.py:418`
- `tests/test_vision_description_provenance.py:61`

## `ChatHandler.update_session_name_if_needed` — method, line 346
- **called from:**
- `routes/chat_helpers.py:953`

## `ChatHandler.trim_history_if_needed` — method, line 351
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatHandler.handle_memory_command` — method (async), line 355
- **called from:**
- `routes/chat_routes.py:2504`
