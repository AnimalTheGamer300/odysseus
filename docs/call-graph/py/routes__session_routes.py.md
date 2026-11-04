# `routes/session_routes.py` — definitions & call sites

39 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sanitize_export_filename` — function, line 27
- **called from:**
- `routes/session_routes.py:1036`
- `tests/test_security_regressions.py:1159`
- `tests/test_security_regressions.py:1170`
- `tests/test_security_regressions.py:1171`
- `tests/test_session_export_filename.py:10`
- `tests/test_session_export_filename.py:11`
- `tests/test_session_export_filename.py:15`

## `_public_model` — function, line 40
- **called from:**
- `routes/session_routes.py:372`
- `tests/test_blind_compare_redaction.py:49`
- `tests/test_blind_compare_redaction.py:50`
- `tests/test_blind_compare_redaction.py:57`
- `tests/test_blind_compare_redaction.py:63`
- `tests/test_blind_compare_redaction.py:64`
- `tests/test_blind_compare_redaction.py:65`

## `_content_to_text` — function, line 50
- **called from:**
- `routes/session_routes.py:117`
- `routes/session_routes.py:625`
- `routes/session_routes.py:675`
- `routes/session_routes.py:1057`
- `routes/session_routes.py:1080`
- `routes/session_routes.py:1099`
- `tests/test_session_export_nonstring_content.py:19`
- `tests/test_session_export_nonstring_content.py:20`
- `tests/test_session_export_nonstring_content.py:29`
- `tests/test_session_export_nonstring_content.py:34`
- `tests/test_session_export_nonstring_content.py:38`
- `tests/test_session_export_nonstring_content.py:39`
- `tests/test_session_export_nonstring_content.py:45`

## `_clean_title` — function, line 82
- **called from:**
- `routes/session_routes.py:669`

## `_message_role` — function, line 102
- **called from:**
- `routes/history/history_routes.py:1120`
- `routes/session_routes.py:624`
- `routes/session_routes.py:674`
- `services/memory/memory_extractor.py:292`

## `_message_text` — function, line 110
- **called from:**
- `routes/history/history_routes.py:1121`
- `routes/session_routes.py:1225`
- `services/memory/memory_extractor.py:294`

## `_message_metadata` — function, line 120
- **called from:**
- `routes/session_routes.py:1225`

## `_reject_compact_during_active_run` — function, line 130
- **called from:**
- `routes/history/history_routes.py:1095`
- `routes/session_routes.py:1192`

## `_verify_session_owner` — function, line 136
- **called from:**
- `routes/chat_routes.py:946`
- `routes/chat_routes.py:1340`
- `routes/chat_routes.py:3081`
- `routes/chat_routes.py:3097`
- `routes/chat_routes.py:3107`
- `routes/chat_routes.py:3125`
- `routes/chat_routes.py:3227`
- `routes/history/history_routes.py:277`
- `routes/history/history_routes.py:420`
- `routes/history/history_routes.py:472`
- `routes/history/history_routes.py:490`
- `routes/history/history_routes.py:561`
- `routes/history/history_routes.py:639`
- `routes/history/history_routes.py:694`
- `routes/history/history_routes.py:745`
- `routes/history/history_routes.py:866`
- `routes/history/history_routes.py:982`
- `routes/history/history_routes.py:1032`
- `routes/history/history_routes.py:1088`
- `routes/session_routes.py:534`
- `routes/session_routes.py:615`
- `routes/session_routes.py:688`
- `routes/session_routes.py:738`
- `routes/session_routes.py:762`
- `routes/session_routes.py:885`
- `routes/session_routes.py:899`
- `routes/session_routes.py:913`
- `routes/session_routes.py:951`
- `routes/session_routes.py:1028`
- `routes/session_routes.py:1150`
- `routes/session_routes.py:1187`
- `routes/session_routes.py:1569`
- `tests/test_session_ghost_delete.py:80`
- `tests/test_session_ghost_delete.py:88`
- `tests/test_session_ghost_delete.py:96`
- `tests/test_session_ghost_delete.py:104`
- `tests/test_session_ghost_delete.py:111`
- `tests/test_session_owner_attribution.py:109`
- `tests/test_session_owner_attribution.py:117`
- `tests/test_session_owner_attribution.py:124`
- `tests/test_session_owner_attribution.py:131`
- `tests/test_session_owner_attribution.py:138`
- `tests/test_session_owner_attribution.py:148`

## `_current_user_is_admin` — function, line 172
- **called from:**
- `routes/session_routes.py:201`

## `_reject_raw_endpoint_url_for_non_admin` — function, line 187
- **called from:**
- `routes/compare/compare_routes.py:160`
- `routes/session_routes.py:411`
- `routes/session_routes.py:558`
- `tests/test_session_endpoint_owner_scope.py:30`
- `tests/test_session_endpoint_owner_scope.py:41`
- `tests/test_session_endpoint_owner_scope.py:47`
- `tests/test_session_endpoint_owner_scope.py:59`
- `tests/test_session_endpoint_owner_scope.py:70`

## `_reject_delegated_session_options` — function, line 205
- **called from:**
- `routes/session_routes.py:404`
- `tests/test_session_endpoint_owner_scope.py:87`

## `_persist_session_headers` — function, line 221
- **called from:**
- `routes/session_routes.py:511`

## `_pick_endpoint_for_sort` — function, line 248
- **called from:**
- `routes/session_routes.py:1438`

## `setup_session_routes` — function, line 269
- **called from:**
- `app.py:682`
- `tests/test_archived_sessions_model_filter.py:67`
- `tests/test_history_compact_tool_calls.py:164`
- `tests/test_history_display_model_hydration.py:158`
- `tests/test_session_list_owner_scope.py:68`
- `tests/test_session_list_owner_scope.py:121`

## `list_sessions` — function, line 283
- **route:** `GET /sessions`
- decorator: `router.get("/sessions")`
- **called from:**
- `src/agent_tools/session_tools.py:303`
- `src/agent_tools/session_tools.py:483`

## `create_session` — function, line 392
- **route:** `POST /session`
- decorator: `router.post("/session", response_model=SessionResponse)`
- **called from:**
- `core/session_manager.py:1308`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:885`
- `routes/research/research_routes.py:737`
- `routes/session_routes.py:494`
- `routes/session_routes.py:1133`
- `routes/webhook/webhook_routes.py:306`
- `routes/webhook/webhook_routes.py:367`
- `src/agent_tools/session_tools.py:50`
- `src/agent_tools/session_tools.py:437`
- `src/agent_tools/session_tools.py:478`
- `tests/test_auth_session_revocation.py:51`
- `tests/test_auth_session_revocation.py:52`
- `tests/test_auth_session_revocation.py:53`
- `tests/test_auth_session_revocation.py:65`
- `tests/test_auth_session_revocation.py:66`
- `tests/test_auth_session_revocation.py:79`
- `tests/test_auth_session_revocation.py:80`
- `tests/test_delete_user_revokes_api_tokens.py:120`
- `tests/test_session_discovery_message_count.py:33`
- `tests/test_truncate_message_count_regression.py:37`
- `tests/test_truncate_message_count_regression.py:67`

## `rename_session` — function, line 528
- **route:** `PATCH /session/{sid}`
- decorator: `router.patch("/session/{sid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `retitle_session` — function (async), line 606
- **route:** `POST /session/{sid}/retitle`
- decorator: `router.post("/session/{sid}/retitle")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inject_messages` — function (async), line 686
- **route:** `POST /session/{sid}/inject_messages`
- decorator: `router.post("/session/{sid}/inject_messages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_session_beacon` — function, line 722
- **route:** `POST /session/{sid}/delete`
- decorator: `router.post("/session/{sid}/delete")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `bulk_delete_sessions` — function (async), line 727
- **route:** `POST /sessions/bulk-delete`
- decorator: `router.post("/sessions/bulk-delete")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_session` — function, line 756
- **route:** `DELETE /session/{sid}`
- decorator: `router.delete("/session/{sid}")`
- **called from:**
- `core/session_manager.py:1181`
- `routes/session_routes.py:312`
- `routes/session_routes.py:724`
- `routes/session_routes.py:1335`
- `src/agent_tools/session_tools.py:383`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `delete_all_sessions` — function, line 799
- **route:** `DELETE /sessions/all`
- decorator: `router.delete("/sessions/all")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_trash_sessions` — function, line 856
- **route:** `GET /sessions/trash`
- decorator: `router.get("/sessions/trash")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `empty_trash` — function, line 866
- **route:** `DELETE /sessions/trash`
- decorator: `router.delete("/sessions/trash")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `untrash_session` — function, line 883
- **route:** `POST /session/{sid}/untrash`
- decorator: `router.post("/session/{sid}/untrash")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `purge_session_route` — function, line 897
- **route:** `DELETE /session/{sid}/purge`
- decorator: `router.delete("/session/{sid}/purge")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `archive_session` — function, line 911
- **route:** `POST /session/{sid}/archive`
- decorator: `router.post("/session/{sid}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unarchive_session` — function, line 949
- **route:** `POST /session/{sid}/unarchive`
- decorator: `router.post("/session/{sid}/unarchive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_archived_sessions` — function, line 979
- **route:** `GET /sessions/archived`
- decorator: `router.get("/sessions/archived")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_session` — function, line 1023
- **route:** `GET /session/{sid}/export`
- decorator: `router.get("/session/{sid}/export")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sessions_save_now` — function, line 1113
- **route:** `POST /sessions/save`
- decorator: `router.post("/sessions/save")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_session_openai` — function, line 1121
- **route:** `POST /session/openai`
- decorator: `router.post("/session/openai")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_session_important` — function (async), line 1148
- **route:** `POST /session/{session_id}/important`
- decorator: `router.post("/session/{session_id}/important")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compact_session` — function (async), line 1185
- **route:** `POST /session/{session_id}/compact`
- decorator: `router.post("/session/{session_id}/compact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `auto_sort_sessions` — function, line 1279
- **route:** `POST /sessions/auto-sort`
- decorator: `router.post("/sessions/auto-sort")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_loads_lenient` — function, line 1471
- **called from:**
- `routes/session_routes.py:1482`
- `routes/session_routes.py:1487`
- `routes/session_routes.py:1493`

## `get_context_info` — function (async), line 1567
- **route:** `GET /session/{session_id}/context_info`
- decorator: `router.get("/session/{session_id}/context_info")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
