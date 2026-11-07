# `routes/session_routes.py` — definitions & call sites

40 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_sanitize_export_filename` — function, line 29
- **called from:**
- `routes/session_routes.py:1182`
- `tests/test_security_regressions.py:1161`
- `tests/test_security_regressions.py:1172`
- `tests/test_security_regressions.py:1173`
- `tests/test_session_export_filename.py:10`
- `tests/test_session_export_filename.py:11`
- `tests/test_session_export_filename.py:15`

## `_public_model` — function, line 42
- **called from:**
- `routes/session_routes.py:527`
- `tests/test_blind_compare_redaction.py:49`
- `tests/test_blind_compare_redaction.py:50`
- `tests/test_blind_compare_redaction.py:57`
- `tests/test_blind_compare_redaction.py:63`
- `tests/test_blind_compare_redaction.py:64`
- `tests/test_blind_compare_redaction.py:65`

## `_content_to_text` — function, line 52
- **called from:**
- `routes/session_routes.py:227`
- `routes/session_routes.py:819`
- `routes/session_routes.py:869`
- `routes/session_routes.py:1203`
- `routes/session_routes.py:1226`
- `routes/session_routes.py:1245`
- `tests/test_session_export_nonstring_content.py:19`
- `tests/test_session_export_nonstring_content.py:20`
- `tests/test_session_export_nonstring_content.py:29`
- `tests/test_session_export_nonstring_content.py:34`
- `tests/test_session_export_nonstring_content.py:38`
- `tests/test_session_export_nonstring_content.py:39`
- `tests/test_session_export_nonstring_content.py:45`

## `_context_info_skill_inventory` — function, line 73
- **called from:**
- `routes/session_routes.py:1710`
- `tests/test_session_context_info_skills.py:29`
- `tests/test_session_context_info_skills.py:42`

## `_context_info_tool_inventory` — function, line 119
- **called from:**
- `routes/session_routes.py:1711`
- `tests/test_session_context_info_tools.py:27`
- `tests/test_session_context_info_tools.py:41`

## `_context_info_agents_md_inventory` — function, line 140
- **called from:**
- `routes/session_routes.py:1718`
- `tests/test_session_context_info_agents_md.py:13`
- `tests/test_session_context_info_agents_md.py:24`

## `_clean_title` — function, line 192
- **called from:**
- `routes/session_routes.py:863`

## `_message_role` — function, line 212
- **called from:**
- `routes/history/history_routes.py:1519`
- `routes/session_routes.py:818`
- `routes/session_routes.py:868`
- `services/memory/memory_extractor.py:336`

## `_message_text` — function, line 220
- **called from:**
- `routes/history/history_routes.py:1520`
- `routes/session_routes.py:1378`
- `routes/session_routes.py:1429`
- `services/memory/memory_extractor.py:338`

## `_message_metadata` — function, line 230
- **called from:**
- `routes/session_routes.py:1378`

## `_reject_compact_during_active_run` — function, line 240
- **called from:**
- `routes/history/history_routes.py:1494`
- `routes/session_routes.py:1338`

## `_verify_session_owner` — function, line 246
- **called from:**
- `routes/chat_routes.py:2433`
- `routes/chat_routes.py:2993`
- `routes/chat_routes.py:5561`
- `routes/chat_routes.py:5581`
- `routes/chat_routes.py:5589`
- `routes/chat_routes.py:5599`
- `routes/chat_routes.py:5622`
- `routes/chat_routes.py:5724`
- `routes/history/history_routes.py:422`
- `routes/history/history_routes.py:567`
- `routes/history/history_routes.py:659`
- `routes/history/history_routes.py:683`
- `routes/history/history_routes.py:771`
- `routes/history/history_routes.py:826`
- `routes/history/history_routes.py:881`
- `routes/history/history_routes.py:932`
- `routes/history/history_routes.py:1064`
- `routes/history/history_routes.py:1199`
- `routes/history/history_routes.py:1256`
- `routes/history/history_routes.py:1292`
- `routes/history/history_routes.py:1331`
- `routes/history/history_routes.py:1367`
- `routes/history/history_routes.py:1430`
- `routes/history/history_routes.py:1487`
- `routes/session_routes.py:701`
- `routes/session_routes.py:809`
- `routes/session_routes.py:882`
- `routes/session_routes.py:932`
- `routes/session_routes.py:953`
- `routes/session_routes.py:965`
- `routes/session_routes.py:1058`
- `routes/session_routes.py:1096`
- `routes/session_routes.py:1174`
- `routes/session_routes.py:1296`
- `routes/session_routes.py:1333`
- `routes/session_routes.py:1705`
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

## `_current_user_is_admin` — function, line 282
- **called from:**
- `routes/session_routes.py:311`

## `_reject_raw_endpoint_url_for_non_admin` — function, line 297
- **called from:**
- `routes/compare/compare_routes.py:160`
- `routes/session_routes.py:573`
- `routes/session_routes.py:738`
- `tests/test_session_endpoint_owner_scope.py:30`
- `tests/test_session_endpoint_owner_scope.py:41`
- `tests/test_session_endpoint_owner_scope.py:47`
- `tests/test_session_endpoint_owner_scope.py:59`
- `tests/test_session_endpoint_owner_scope.py:70`

## `_reject_delegated_session_options` — function, line 315
- **called from:**
- `routes/session_routes.py:566`
- `tests/test_session_endpoint_owner_scope.py:87`

## `_persist_session_headers` — function, line 331
- **called from:**
- `routes/session_routes.py:676`

## `_is_hidden_session_name` — function, line 374
- **called from:**
- `routes/session_routes.py:473`

## `_pick_endpoint_for_sort` — function, line 384
- **called from:**
- `routes/session_routes.py:1566`

## `setup_session_routes` — function, line 405
- **called from:**
- `app.py:760`
- `tests/test_archived_sessions_model_filter.py:67`
- `tests/test_chat_tidy_content_preservation.py:35`
- `tests/test_chatgpt_session_binding.py:124`
- `tests/test_chatgpt_session_binding.py:142`
- `tests/test_codeql_python_residual_security.py:59`
- `tests/test_history_compact_tool_calls.py:179`
- `tests/test_history_display_model_hydration.py:162`
- `tests/test_session_context_info_tools.py:13`
- `tests/test_session_list_owner_scope.py:69`
- `tests/test_session_list_owner_scope.py:112`
- `tests/test_session_list_owner_scope.py:163`
- `tests/test_session_list_owner_scope.py:205`
- `tests/test_session_list_owner_scope.py:276`

## `list_sessions` — function, line 420
- **route:** `GET /sessions`
- decorator: `router.get("/sessions")`
- **called from:**
- `src/agent_tools/session_tools.py:324`
- `src/agent_tools/session_tools.py:506`

## `create_session` — function, line 553
- **route:** `POST /session`
- decorator: `router.post("/session", response_model=SessionResponse)`
- **called from:**
- `core/session_manager.py:1113`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:1101`
- `routes/research/research_routes.py:849`
- `routes/session_routes.py:656`
- `routes/session_routes.py:1279`
- `routes/webhook/webhook_routes.py:306`
- `routes/webhook/webhook_routes.py:367`
- `scripts/eval_odysseus_contextual_tool_use.py:880`
- `scripts/odysseus_conversation_qa.py:796`
- `scripts/run_sft_environment_expansion.py:697`
- `scripts/run_sft_overnight_fixture_flows.py:570`
- `scripts/sft_email_overseer.py:653`
- `src/agent_tools/session_tools.py:61`
- `src/agent_tools/session_tools.py:460`
- `src/agent_tools/session_tools.py:501`
- `tests/test_admin_listing_authorization.py:45`
- `tests/test_auth_session_revocation.py:52`
- `tests/test_auth_session_revocation.py:53`
- `tests/test_auth_session_revocation.py:96`
- `tests/test_auth_session_revocation.py:97`
- `tests/test_auth_session_revocation.py:98`
- `tests/test_auth_session_revocation.py:110`
- `tests/test_auth_session_revocation.py:111`
- `tests/test_auth_session_revocation.py:124`
- `tests/test_auth_session_revocation.py:125`
- `tests/test_chat_document_owner_context.py:80`
- `tests/test_chatgpt_session_binding.py:42`
- `tests/test_database_test_isolation.py:43`
- `tests/test_delete_user_revokes_api_tokens.py:120`
- `tests/test_history_add_message_validation.py:41`
- `tests/test_history_add_message_validation.py:57`
- `tests/test_history_truncate_validation.py:21`
- `tests/test_odysseus_conversation_qa.py:103`
- `tests/test_session_cwd_persistence.py:24`
- `tests/test_session_discovery_message_count.py:33`
- `tests/test_session_header_persistence.py:23`
- `tests/test_truncate_message_count_regression.py:28`
- `tests/test_truncate_message_count_regression.py:58`

## `rename_session` — function, line 694
- **route:** `PATCH /session/{sid}`
- decorator: `router.patch("/session/{sid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `retitle_session` — function (async), line 800
- **route:** `POST /session/{sid}/retitle`
- decorator: `router.post("/session/{sid}/retitle")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inject_messages` — function (async), line 880
- **route:** `POST /session/{sid}/inject_messages`
- decorator: `router.post("/session/{sid}/inject_messages")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_session_beacon` — function, line 916
- **route:** `POST /session/{sid}/delete`
- decorator: `router.post("/session/{sid}/delete")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `bulk_delete_sessions` — function (async), line 921
- **route:** `POST /sessions/bulk-delete`
- decorator: `router.post("/sessions/bulk-delete")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `session_deletion_info` — function, line 952
- **route:** `GET /session/{sid}/deletion-info`
- decorator: `router.get("/session/{sid}/deletion-info")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_session` — function, line 963
- **route:** `DELETE /session/{sid}`
- decorator: `router.delete("/session/{sid}")`
- **called from:**
- `routes/session_routes.py:449`
- `routes/session_routes.py:918`
- `routes/session_routes.py:943`
- `routes/session_routes.py:980`
- `routes/session_routes.py:981`
- `routes/session_routes.py:1483`
- `routes/session_routes.py:1496`
- `scripts/run_sft_environment_expansion.py:740`
- `scripts/run_sft_overnight_fixture_flows.py:580`
- `src/agent_tools/session_tools.py:404`
- `tests/test_chat_image_preservation.py:28`
- `tests/test_chat_image_preservation.py:31`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `delete_all_sessions` — function, line 1000
- **route:** `DELETE /sessions/all`
- decorator: `router.delete("/sessions/all")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `archive_session` — function, line 1056
- **route:** `POST /session/{sid}/archive`
- decorator: `router.post("/session/{sid}/archive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unarchive_session` — function, line 1094
- **route:** `POST /session/{sid}/unarchive`
- decorator: `router.post("/session/{sid}/unarchive")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_archived_sessions` — function, line 1124
- **route:** `GET /sessions/archived`
- decorator: `router.get("/sessions/archived")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_session` — function, line 1169
- **route:** `GET /session/{sid}/export`
- decorator: `router.get("/session/{sid}/export")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sessions_save_now` — function, line 1259
- **route:** `POST /sessions/save`
- decorator: `router.post("/sessions/save")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_session_openai` — function, line 1267
- **route:** `POST /session/openai`
- decorator: `router.post("/session/openai")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_session_important` — function (async), line 1294
- **route:** `POST /session/{session_id}/important`
- decorator: `router.post("/session/{session_id}/important")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compact_session` — function (async), line 1331
- **route:** `POST /session/{session_id}/compact`
- decorator: `router.post("/session/{session_id}/compact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `auto_sort_sessions` — function, line 1441
- **route:** `POST /sessions/auto-sort`
- decorator: `router.post("/sessions/auto-sort")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_loads_lenient` — function, line 1603
- **called from:**
- `routes/session_routes.py:1614`
- `routes/session_routes.py:1619`
- `routes/session_routes.py:1625`

## `get_context_info` — function (async), line 1699
- **route:** `GET /session/{session_id}/context_info`
- decorator: `router.get("/session/{session_id}/context_info")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
