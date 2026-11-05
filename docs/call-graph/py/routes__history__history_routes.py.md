# `routes/history/history_routes.py` — definitions & call sites

36 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sft_trace_file_for_owner` — function, line 35
- **called from:**
- `routes/history/history_routes.py:56`

## `_remove_deleted_sft_trace_rows` — function, line 49
- **called from:**
- `routes/history/history_routes.py:626`
- `routes/history/history_routes.py:738`

## `_deleted_sft_pairs_from_db_rows` — function, line 105
- **called from:**
- `routes/history/history_routes.py:622`
- `routes/history/history_routes.py:686`

## `_history_display_content` — function, line 134
- **called from:**
- `routes/history/history_routes.py:299`
- `routes/history/history_routes.py:376`
- `routes/history/history_routes.py:498`
- `routes/history/history_routes.py:507`

## `_merge_continue_rows_to_delete` — function, line 200
- **called from:**
- `routes/history/history_routes.py:1010`
- `tests/test_merge_last_assistant_rows.py:21`
- `tests/test_merge_last_assistant_rows.py:29`
- `tests/test_merge_last_assistant_rows.py:35`
- `tests/test_merge_last_assistant_rows.py:40`

## `_is_continue_interruption_message` — function, line 225
- **called from:**
- `routes/history/history_routes.py:246`

## `_has_immediate_continue_marker` — function, line 245
- **called from:**
- `routes/history/history_routes.py:933`
- `routes/history/history_routes.py:1001`
- `tests/test_merge_last_assistant_rows.py:46`
- `tests/test_merge_last_assistant_rows.py:53`
- `tests/test_resume_history_merge.py:11`

## `_keep_count_before_message` — function, line 249
- **called from:**
- `routes/history/history_routes.py:607`
- `routes/history/history_routes.py:1066`
- `tests/test_resend_message_nondestructive.py:98`
- `tests/test_resend_message_nondestructive.py:99`
- `tests/test_resend_message_nondestructive.py:100`

## `_effort_mode` — function, line 260
- **called from:**
- `routes/history/history_routes.py:1360`
- `routes/history/history_routes.py:1364`

## `setup_history_routes` — function, line 272
- **called from:**
- `app.py:795`
- `tests/test_fork_session_metadata.py:77`
- `tests/test_fork_session_metadata.py:114`
- `tests/test_history_add_message_validation.py:21`
- `tests/test_history_compact_tool_calls.py:127`
- `tests/test_history_compact_tool_calls.py:180`
- `tests/test_history_display_model_hydration.py:106`
- `tests/test_history_display_model_hydration.py:163`
- `tests/test_history_display_model_hydration.py:371`
- `tests/test_history_topics_owner_scope.py:168`
- `tests/test_history_truncate_validation.py:32`

## `_reserve_message_uploads` — function, line 278
- **called from:**
- `routes/history/history_routes.py:657`
- `routes/history/history_routes.py:763`

## `_db_history_entry` — function, line 298
- **called from:**
- `routes/history/history_routes.py:541`

## `_db_message_metadata` — function, line 313
- **called from:**
- `routes/history/history_routes.py:348`
- `routes/history/history_routes.py:366`
- `routes/history/history_routes.py:396`

## `_draft_is_live` — function, line 324
- **called from:**
- `routes/history/history_routes.py:351`
- `routes/history/history_routes.py:368`

## `_finalize_or_hide_draft` — function, line 334
- **called from:**
- `routes/history/history_routes.py:464`

## `_entry_or_none` — function, line 361
- **called from:**
- `routes/history/history_routes.py:467`
- `routes/history/history_routes.py:532`

## `_hydrate_session_history_from_db` — function, line 381
- **called from:**
- `routes/history/history_routes.py:465`
- `routes/history/history_routes.py:538`

## `_session_needs_db_history_hydration` — function, line 401
- **called from:**
- `routes/history/history_routes.py:449`

## `get_session_history` — function (async), line 409
- **route:** `GET /api/history/{session_id}`
- decorator: `router.get("/api/history/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `truncate_session` — function (async), line 559
- **route:** `POST /api/session/{session_id}/truncate`
- decorator: `router.post("/api/session/{session_id}/truncate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_message` — function (async), line 641
- **route:** `POST /api/session/{session_id}/message`
- decorator: `router.post("/api/session/{session_id}/message")`
- **called from:**
- `routes/chat_helpers.py:952`
- `routes/chat_helpers.py:1967`
- `routes/chat_routes.py:1515`
- `routes/chat_routes.py:2606`
- `routes/chat_routes.py:4175`
- `routes/chat_routes.py:4476`
- `routes/chat_routes.py:5604`
- `routes/history/history_routes.py:659`
- `routes/history/history_routes.py:1111`
- `routes/research/research_routes.py:882`
- `routes/session_routes.py:907`
- `routes/webhook/webhook_routes.py:377`
- `routes/webhook/webhook_routes.py:385`
- `src/agent_jobs.py:326`
- `src/agent_tools/session_tools.py:250`
- `src/agent_tools/session_tools.py:251`
- `src/agent_tools/session_tools.py:475`
- `src/bg_monitor.py:199`
- `src/chat_handler.py:367`
- `src/chat_handler.py:368`
- `src/task_scheduler.py:1914`
- `src/task_scheduler.py:1922`
- `tests/test_database_test_isolation.py:45`
- `tests/test_database_test_isolation.py:46`
- `tests/test_history_add_message_validation.py:44`
- `tests/test_history_add_message_validation.py:59`
- `tests/test_history_truncate_validation.py:23`
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
- `tests/test_truncate_message_count_regression.py:31`
- `tests/test_truncate_message_count_regression.py:61`

## `delete_messages` — function (async), line 665
- **route:** `POST /api/session/{session_id}/delete-messages`
- decorator: `router.post("/api/session/{session_id}/delete-messages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_get_db_id` — function, line 696
- **called from:**
- `routes/history/history_routes.py:712`

## `edit_message` — function (async), line 753
- **route:** `POST /api/session/{session_id}/edit-message`
- decorator: `router.post("/api/session/{session_id}/edit-message")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_stopped` — function (async), line 808
- **route:** `POST /api/session/{session_id}/mark-stopped`
- decorator: `router.post("/api/session/{session_id}/mark-stopped")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_last_meta` — function (async), line 863
- **route:** `POST /api/session/{session_id}/update-last-meta`
- decorator: `router.post("/api/session/{session_id}/update-last-meta")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `merge_last_assistant` — function (async), line 914
- **route:** `POST /api/session/{session_id}/merge-last-assistant`
- decorator: `router.post("/api/session/{session_id}/merge-last-assistant")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fork_session` — function (async), line 1035
- **route:** `POST /api/session/{session_id}/fork`
- decorator: `router.post("/api/session/{session_id}/fork")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_conversation_topics` — function (async), line 1167
- **route:** `GET /api/conversations/topics`
- decorator: `router.get("/api/conversations/topics")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_session_context_usage` — function (async), line 1176
- **route:** `GET /api/session/{session_id}/context`
- decorator: `router.get("/api/session/{session_id}/context")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_session_memory_extraction` — function (async), line 1238
- **route:** `POST /api/session/{session_id}/memory-extraction`
- decorator: `router.post("/api/session/{session_id}/memory-extraction")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_session_skill_injection` — function (async), line 1274
- **route:** `POST /api/session/{session_id}/skill-injection`
- decorator: `router.post("/api/session/{session_id}/skill-injection")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_session_memory_injection` — function (async), line 1313
- **route:** `POST /api/session/{session_id}/memory-injection`
- decorator: `router.post("/api/session/{session_id}/memory-injection")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_session_generation_settings` — function (async), line 1350
- **route:** `POST /api/session/{session_id}/generation-settings`
- decorator: `router.post("/api/session/{session_id}/generation-settings")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `uncompact_session` — function (async), line 1406
- **route:** `POST /api/session/{session_id}/uncompact`
- decorator: `router.post("/api/session/{session_id}/uncompact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compact_session` — function (async), line 1469
- **route:** `POST /api/session/{session_id}/compact`
- decorator: `router.post("/api/session/{session_id}/compact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
