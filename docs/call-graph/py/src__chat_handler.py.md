# `src/chat_handler.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sync_upload_vision_to_gallery` — function, line 32
- **called from:**
- `src/chat_handler.py:249`
- `src/chat_handler.py:269`
- `src/chat_handler.py:281`

## `ChatHandler` — class, line 60
- **called from:**
- `src/app_initializer.py:133`
- `tests/test_chat_preprocess_tool_policy.py:32`
- `tests/test_security_regressions.py:413`

## `ChatHandler.__init__` — method, line 63
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

## `ChatHandler.validate_and_extract_preset` — method, line 83
- **called from:**
- `routes/chat_helpers.py:373`

## `ChatHandler.enhance_message_if_needed` — method, line 115
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatHandler.preprocess_message` — method (async), line 123
- **called from:**
- `routes/chat_helpers.py:390`
- `tests/test_chat_preprocess_tool_policy.py:42`
- `tests/test_security_regressions.py:417`

## `ChatHandler.update_session_name_if_needed` — method, line 330
- **called from:**
- `routes/chat_helpers.py:471`

## `ChatHandler.trim_history_if_needed` — method, line 335
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ChatHandler.handle_memory_command` — method (async), line 339
- **called from:**
- `routes/chat_routes.py:978`
