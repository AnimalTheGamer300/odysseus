# `routes/chat_routes.py` — definitions & call sites

45 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_stream_failure_status` — function, line 87
- **called from:**
- `routes/chat_routes.py:2372`
- `tests/test_foreground_model_routing.py:86`

## `_reject_delegated_tool_approval` — function, line 101
- **called from:**
- `routes/chat_routes.py:1350`
- `tests/test_api_token_tool_authority.py:162`
- `tests/test_api_token_tool_authority.py:170`

## `_mark_tool_approval_resolved` — function, line 118
- **called from:**
- `routes/chat_routes.py:1391`
- `tests/test_tool_approval_task_scope.py:281`

## `_tool_approval_resolution_stream` — function (async), line 177
- **called from:**
- `routes/chat_routes.py:1402`
- `tests/test_tool_approval_task_scope.py:299`

## `_chat_candidate_request_factory` — function, line 182
- **called from:**
- `routes/chat_routes.py:1047`
- `routes/chat_routes.py:2085`

## `factory` — function (async), line 199
- **called from:**
- `tests/test_calendar_default_transaction.py:79`
- `tests/test_calendar_default_transaction.py:180`
- `tests/test_calendar_default_transaction.py:225`
- `tests/test_calendar_default_transaction.py:251`
- `tests/test_calendar_default_transaction.py:295`
- `tests/test_calendar_default_transaction.py:499`
- `tests/test_calendar_default_transaction.py:511`
- `tests/test_calendar_default_transaction.py:526`
- `tests/test_email_account_default_serialization.py:66`
- `tests/test_email_account_default_serialization.py:85`
- `tests/test_foreground_model_routing.py:567`
- `tests/test_foreground_model_routing.py:621`
- `tests/test_foreground_model_routing.py:3059`
- `tests/test_foreground_model_routing.py:3250`
- `tests/test_foreground_model_routing.py:3361`
- `tests/test_foreground_model_routing.py:3452`
- `tests/test_foreground_model_routing.py:3587`
- `tests/test_notes_fail_closed_auth.py:112`
- `tests/test_notes_fail_closed_auth.py:141`
- `tests/test_notes_fail_closed_auth.py:180`
- `tests/test_pr6020_rebase_regressions.py:200`
- `tests/test_pr6020_rebase_regressions.py:218`

## `_candidate_index` — function, line 229
- **called from:**
- `routes/chat_routes.py:1064`

## `_stream_set` — function, line 236
- **called from:**
- `routes/chat_routes.py:1975`
- `routes/chat_routes.py:2266`
- `routes/chat_routes.py:2455`
- `routes/chat_routes.py:2576`
- `routes/chat_routes.py:2585`
- `routes/chat_routes.py:2754`
- `routes/chat_routes.py:2853`
- `routes/chat_routes.py:2955`
- `routes/chat_routes.py:2964`

## `_persist_stream_partial` — function, line 249
- **called from:**
- `routes/chat_routes.py:2596`
- `routes/chat_routes.py:2614`
- `routes/chat_routes.py:2631`
- `routes/chat_routes.py:2975`
- `routes/chat_routes.py:3000`
- `routes/chat_routes.py:3021`
- `tests/test_partial_tool_events.py:59`
- `tests/test_partial_tool_events.py:73`

## `_persist_continue_separator` — function, line 324
- **called from:**
- `routes/chat_routes.py:1347`

## `_sink_tool_state` — function, line 360
- **called from:**
- `routes/chat_routes.py:2048`
- `routes/chat_routes.py:2973`
- `routes/chat_routes.py:2994`
- `routes/chat_routes.py:3016`
- `tests/test_partial_tool_events.py:34`
- `tests/test_partial_tool_events.py:35`
- `tests/test_partial_tool_events.py:44`
- `tests/test_partial_tool_events.py:54`

## `_checkpoint_draft` — function, line 378
- **called from:**
- `routes/chat_routes.py:2053`

## `_message_plain_text` — function, line 405
- **called from:**
- `routes/chat_routes.py:422`
- `routes/chat_routes.py:485`

## `_last_user_plain_text` — function, line 419
- **called from:**
- `routes/chat_routes.py:431`

## `_ensure_current_request_is_latest_user` — function, line 426
- **called from:**
- `routes/chat_routes.py:1987`

## `_recent_session_text` — function, line 478
- **called from:**
- `routes/chat_routes.py:495`
- `routes/chat_routes.py:502`

## `_is_contextual_web_followup` — function, line 491
- **called from:**
- `routes/chat_routes.py:1457`

## `_is_contextual_browser_followup` — function, line 498
- **called from:**
- `routes/chat_routes.py:1468`

## `_resolve_request_workspace` — function, line 505
- **called from:**
- `routes/chat_routes.py:1182`
- `tests/test_workspace_confine.py:527`
- `tests/test_workspace_confine.py:528`
- `tests/test_workspace_confine.py:532`
- `tests/test_workspace_confine.py:533`

## `_resolve_workspace_from_message_path` — function, line 541
- **called from:**
- `routes/chat_routes.py:1476`

## `_session_url_matches_endpoint` — function, line 572
- **called from:**
- `routes/chat_helpers.py:535`
- `routes/chat_routes.py:597`
- `routes/chat_routes.py:664`
- `routes/chat_routes.py:731`
- `routes/chat_routes.py:849`

## `_clear_orphaned_session_endpoint` — function, line 585
- **called from:**
- `routes/chat_routes.py:953`
- `routes/chat_routes.py:1437`

## `_endpoint_cache_contains_model` — function, line 617
- **called from:**
- `routes/chat_routes.py:666`

## `_is_image_generation_session` — function, line 637
- **called from:**
- `routes/chat_routes.py:1528`
- `tests/test_chat_image_routing.py:60`
- `tests/test_chat_image_routing.py:69`
- `tests/test_chat_image_routing.py:78`
- `tests/test_chat_image_routing.py:88`
- `tests/test_chat_image_routing.py:97`

## `_first_image_attachment` — function, line 675
- **called from:**
- `routes/chat_routes.py:2123`

## `_recover_empty_session_model` — function, line 698
- **called from:**
- `routes/chat_routes.py:959`
- `routes/chat_routes.py:1445`

## `_reconcile_selected_route_from_request` — function, line 811
- **called from:**
- `routes/chat_routes.py:1436`

## `_set_user_time_from_request` — function, line 889
- **called from:**
- `routes/chat_routes.py:931`
- `routes/chat_routes.py:1137`

## `setup_chat_routes` — function, line 909
- **called from:**
- `app.py:702`
- `tests/test_api_token_tool_authority.py:200`
- `tests/test_foreground_model_routing.py:234`
- `tests/test_foreground_model_routing.py:1157`
- `tests/test_history_display_model_hydration.py:509`

## `chat_endpoint` — function (async), line 929
- **route:** `POST /api/chat`
- decorator: `router.post("/api/chat", response_model=Dict[str, Any])`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stream` — function (async), line 1123
- **route:** `POST /api/chat_stream`
- decorator: `router.post("/api/chat_stream")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `stream_with_save` — function (async), line 1812
- **called from:**
- `routes/chat_routes.py:3040`

## `_on_research_done` — function, line 1889
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_checkpoint` — function, line 2018
- **called from:**
- `routes/chat_routes.py:2582`
- `routes/chat_routes.py:2961`

## `_image_progress_callback` — function (async), line 2129
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_commit_chat_compaction` — function, line 2215
- **called from:**
- `routes/chat_routes.py:2245`
- `routes/chat_routes.py:2278`
- `routes/chat_routes.py:2287`
- `routes/chat_routes.py:2301`
- `routes/chat_routes.py:2442`
- `routes/chat_routes.py:2510`

## `_safe_stream` — function (async), line 3036
- **called from:**
- `routes/chat_routes.py:3066`
- `routes/chat_routes.py:3068`

## `chat_resume` — function (async), line 3080
- **route:** `GET /api/chat/resume/{session_id}`
- decorator: `router.get("/api/chat/resume/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stop` — function (async), line 3096
- **route:** `POST /api/chat/stop/{session_id}`
- decorator: `router.post("/api/chat/stop/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stream_status` — function (async), line 3106
- **route:** `GET /api/chat/stream_status/{session_id}`
- decorator: `router.get("/api/chat/stream_status/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inject_context` — function (async), line 3124
- **route:** `POST /api/inject_context/{session_id}`
- decorator: `router.post("/api/inject_context/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_messages` — function (async), line 3139
- **route:** `GET /api/search`
- decorator: `router.get("/api/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reasoning_control` — function (async), line 3163
- **route:** `GET /api/chat/reasoning-control`
- decorator: `router.get("/api/chat/reasoning-control")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `rewrite_message` — function (async), line 3209
- **route:** `POST /api/rewrite`
- decorator: `router.post("/api/rewrite")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `stream_rewrite` — function (async), line 3246
- **called from:**
- `routes/chat_routes.py:3318`
