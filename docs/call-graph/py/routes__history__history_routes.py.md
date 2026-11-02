# `routes/history/history_routes.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_history_display_content` — function, line 33
- **called from:**
- `routes/history/history_routes.py:151`
- `routes/history/history_routes.py:238`
- `routes/history/history_routes.py:359`
- `routes/history/history_routes.py:368`

## `_merge_continue_rows_to_delete` — function, line 99
- **called from:**
- `routes/history/history_routes.py:828`
- `tests/test_merge_last_assistant_rows.py:21`
- `tests/test_merge_last_assistant_rows.py:29`
- `tests/test_merge_last_assistant_rows.py:35`
- `tests/test_merge_last_assistant_rows.py:40`

## `setup_history_routes` — function, line 124
- **called from:**
- `app.py:716`
- `tests/test_delete_message_after_refresh.py:165`
- `tests/test_delete_message_after_refresh.py:194`
- `tests/test_delete_message_after_refresh.py:218`
- `tests/test_delete_message_after_refresh.py:259`
- `tests/test_delete_message_after_refresh.py:283`
- `tests/test_fork_session_metadata.py:75`
- `tests/test_history_compact_tool_calls.py:123`
- `tests/test_history_compact_tool_calls.py:165`
- `tests/test_history_display_model_hydration.py:106`
- `tests/test_history_display_model_hydration.py:159`
- `tests/test_history_display_model_hydration.py:367`
- `tests/test_history_topics_owner_scope.py:168`

## `_reserve_message_uploads` — function, line 130
- **called from:**
- `routes/history/history_routes.py:480`
- `routes/history/history_routes.py:573`

## `_db_history_entry` — function, line 150
- **called from:**
- `routes/history/history_routes.py:402`

## `_db_message_metadata` — function, line 157
- **called from:**
- `routes/history/history_routes.py:152`
- `routes/history/history_routes.py:210`
- `routes/history/history_routes.py:228`
- `routes/history/history_routes.py:258`

## `_draft_is_live` — function, line 186
- **called from:**
- `routes/history/history_routes.py:213`
- `routes/history/history_routes.py:230`

## `_finalize_or_hide_draft` — function, line 196
- **called from:**
- `routes/history/history_routes.py:326`

## `_entry_or_none` — function, line 223
- **called from:**
- `routes/history/history_routes.py:329`
- `routes/history/history_routes.py:393`

## `_hydrate_session_history_from_db` — function, line 243
- **called from:**
- `routes/history/history_routes.py:327`
- `routes/history/history_routes.py:399`

## `_session_needs_db_history_hydration` — function, line 263
- **called from:**
- `routes/history/history_routes.py:311`

## `get_session_history` — function (async), line 271
- **route:** `GET /api/history/{session_id}`
- decorator: `router.get("/api/history/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `truncate_session` — function (async), line 419
- **route:** `POST /api/session/{session_id}/truncate`
- decorator: `router.post("/api/session/{session_id}/truncate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_message` — function (async), line 470
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
- `routes/history/history_routes.py:482`
- `routes/history/history_routes.py:910`
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
- `tests/test_draft_promotion_keeps_live_media.py:74`
- `tests/test_draft_promotion_keeps_live_media.py:120`
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

## `delete_messages` — function (async), line 488
- **route:** `POST /api/session/{session_id}/delete-messages`
- decorator: `router.post("/api/session/{session_id}/delete-messages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_db_id` — function, line 507
- **called from:**
- `routes/history/history_routes.py:523`

## `edit_message` — function (async), line 559
- **route:** `POST /api/session/{session_id}/edit-message`
- decorator: `router.post("/api/session/{session_id}/edit-message")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_stopped` — function (async), line 637
- **route:** `POST /api/session/{session_id}/mark-stopped`
- decorator: `router.post("/api/session/{session_id}/mark-stopped")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_last_meta` — function (async), line 692
- **route:** `POST /api/session/{session_id}/update-last-meta`
- decorator: `router.post("/api/session/{session_id}/update-last-meta")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `merge_last_assistant` — function (async), line 743
- **route:** `POST /api/session/{session_id}/merge-last-assistant`
- decorator: `router.post("/api/session/{session_id}/merge-last-assistant")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fork_session` — function (async), line 853
- **route:** `POST /api/session/{session_id}/fork`
- decorator: `router.post("/api/session/{session_id}/fork")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_conversation_topics` — function (async), line 966
- **route:** `GET /api/conversations/topics`
- decorator: `router.get("/api/conversations/topics")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_session_context_usage` — function (async), line 975
- **route:** `GET /api/session/{session_id}/context`
- decorator: `router.get("/api/session/{session_id}/context")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `uncompact_session` — function (async), line 1024
- **route:** `POST /api/session/{session_id}/uncompact`
- decorator: `router.post("/api/session/{session_id}/uncompact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compact_session` — function (async), line 1086
- **route:** `POST /api/session/{session_id}/compact`
- decorator: `router.post("/api/session/{session_id}/compact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
