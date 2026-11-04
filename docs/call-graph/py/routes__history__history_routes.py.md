# `routes/history/history_routes.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_history_display_content` — function, line 33
- **called from:**
- `routes/history/history_routes.py:151`
- `routes/history/history_routes.py:236`
- `routes/history/history_routes.py:357`
- `routes/history/history_routes.py:366`

## `_merge_continue_rows_to_delete` — function, line 99
- **called from:**
- `routes/history/history_routes.py:791`
- `tests/test_merge_last_assistant_rows.py:21`
- `tests/test_merge_last_assistant_rows.py:29`
- `tests/test_merge_last_assistant_rows.py:35`
- `tests/test_merge_last_assistant_rows.py:40`

## `setup_history_routes` — function, line 124
- **called from:**
- `app.py:716`
- `tests/test_fork_session_metadata.py:75`
- `tests/test_history_compact_tool_calls.py:123`
- `tests/test_history_compact_tool_calls.py:165`
- `tests/test_history_display_model_hydration.py:106`
- `tests/test_history_display_model_hydration.py:159`
- `tests/test_history_display_model_hydration.py:367`
- `tests/test_history_topics_owner_scope.py:168`

## `_reserve_message_uploads` — function, line 130
- **called from:**
- `routes/history/history_routes.py:466`
- `routes/history/history_routes.py:555`

## `_db_history_entry` — function, line 150
- **called from:**
- `routes/history/history_routes.py:400`

## `_db_message_metadata` — function, line 169
- **called from:**
- `routes/history/history_routes.py:208`
- `routes/history/history_routes.py:226`
- `routes/history/history_routes.py:256`

## `_draft_is_live` — function, line 184
- **called from:**
- `routes/history/history_routes.py:211`
- `routes/history/history_routes.py:228`

## `_finalize_or_hide_draft` — function, line 194
- **called from:**
- `routes/history/history_routes.py:324`

## `_entry_or_none` — function, line 221
- **called from:**
- `routes/history/history_routes.py:327`
- `routes/history/history_routes.py:391`

## `_hydrate_session_history_from_db` — function, line 241
- **called from:**
- `routes/history/history_routes.py:325`
- `routes/history/history_routes.py:397`

## `_session_needs_db_history_hydration` — function, line 261
- **called from:**
- `routes/history/history_routes.py:309`

## `get_session_history` — function (async), line 269
- **route:** `GET /api/history/{session_id}`
- decorator: `router.get("/api/history/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `truncate_session` — function (async), line 417
- **route:** `POST /api/session/{session_id}/truncate`
- decorator: `router.post("/api/session/{session_id}/truncate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_message` — function (async), line 456
- **route:** `POST /api/session/{session_id}/message`
- decorator: `router.post("/api/session/{session_id}/message")`
- **called from:**
- `routes/chat_helpers.py:470`
- `routes/chat_helpers.py:1312`
- `routes/chat_routes.py:319`
- `routes/chat_routes.py:1094`
- `routes/chat_routes.py:1904`
- `routes/chat_routes.py:2200`
- `routes/chat_routes.py:3129`
- `routes/history/history_routes.py:468`
- `routes/history/history_routes.py:873`
- `routes/research/research_routes.py:770`
- `routes/session_routes.py:713`
- `routes/webhook/webhook_routes.py:377`
- `routes/webhook/webhook_routes.py:385`
- `src/agent_jobs.py:326`
- `src/agent_tools/session_tools.py:229`
- `src/agent_tools/session_tools.py:230`
- `src/agent_tools/session_tools.py:452`
- `src/bg_monitor.py:131`
- `src/chat_handler.py:351`
- `src/chat_handler.py:352`
- `src/task_scheduler.py:1752`
- `src/task_scheduler.py:1760`
- `tests/test_session_concurrent.py:32`
- `tests/test_session_concurrent.py:62`
- `tests/test_session_concurrent.py:92`
- `tests/test_session_concurrent.py:104`
- `tests/test_session_context_excludes_slash.py:15`
- `tests/test_session_context_excludes_slash.py:16`
- `tests/test_session_context_excludes_slash.py:17`
- `tests/test_session_context_excludes_slash.py:18`
- `tests/test_session_context_excludes_slash.py:42`
- `tests/test_session_context_excludes_slash.py:43`
- `tests/test_session_discovery_message_count.py:41`
- `tests/test_session_manager.py:52`
- `tests/test_session_manager.py:53`
- `tests/test_session_manager.py:67`
- `tests/test_session_manager.py:68`
- `tests/test_session_manager.py:78`
- `tests/test_session_manager.py:81`
- `tests/test_session_manager.py:121`
- `tests/test_session_manager.py:133`
- `tests/test_session_manager.py:135`
- `tests/test_session_manager.py:149`
- `tests/test_session_manager.py:163`
- `tests/test_session_manager.py:164`
- `tests/test_session_manager.py:165`
- `tests/test_session_manager.py:175`
- `tests/test_session_manager.py:190`
- `tests/test_truncate_message_count_regression.py:40`
- `tests/test_truncate_message_count_regression.py:70`

## `delete_messages` — function (async), line 474
- **route:** `POST /api/session/{session_id}/delete-messages`
- decorator: `router.post("/api/session/{session_id}/delete-messages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_db_id` — function, line 493
- **called from:**
- `routes/history/history_routes.py:509`

## `edit_message` — function (async), line 545
- **route:** `POST /api/session/{session_id}/edit-message`
- decorator: `router.post("/api/session/{session_id}/edit-message")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_stopped` — function (async), line 600
- **route:** `POST /api/session/{session_id}/mark-stopped`
- decorator: `router.post("/api/session/{session_id}/mark-stopped")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_last_meta` — function (async), line 655
- **route:** `POST /api/session/{session_id}/update-last-meta`
- decorator: `router.post("/api/session/{session_id}/update-last-meta")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `merge_last_assistant` — function (async), line 706
- **route:** `POST /api/session/{session_id}/merge-last-assistant`
- decorator: `router.post("/api/session/{session_id}/merge-last-assistant")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fork_session` — function (async), line 816
- **route:** `POST /api/session/{session_id}/fork`
- decorator: `router.post("/api/session/{session_id}/fork")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_conversation_topics` — function (async), line 929
- **route:** `GET /api/conversations/topics`
- decorator: `router.get("/api/conversations/topics")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_session_context_usage` — function (async), line 938
- **route:** `GET /api/session/{session_id}/context`
- decorator: `router.get("/api/session/{session_id}/context")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `uncompact_session` — function (async), line 987
- **route:** `POST /api/session/{session_id}/uncompact`
- decorator: `router.post("/api/session/{session_id}/uncompact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compact_session` — function (async), line 1049
- **route:** `POST /api/session/{session_id}/compact`
- decorator: `router.post("/api/session/{session_id}/compact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
