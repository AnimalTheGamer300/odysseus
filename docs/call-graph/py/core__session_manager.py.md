# `core/session_manager.py` — definitions & call sites

39 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_commit_draft_with_retry` — function, line 44
- **called from:**
- `core/session_manager.py:483`
- `core/session_manager.py:507`

## `_message_timestamp_iso` — function, line 72
- **called from:**
- `core/session_manager.py:257`
- `core/session_manager.py:277`
- `core/session_manager.py:403`
- `core/session_manager.py:467`
- `core/session_manager.py:556`

## `_parse_msg_content` — function, line 81
- **called from:**
- `core/session_manager.py:260`
- `core/session_manager.py:280`

## `SessionManager` — class, line 107
- **called from:**
- `src/app_initializer.py:92`
- `tests/test_session_concurrent.py:21`
- `tests/test_session_concurrent.py:51`
- `tests/test_session_concurrent.py:83`
- `tests/test_session_discovery_message_count.py:23`
- `tests/test_session_discovery_message_count.py:55`
- `tests/test_session_manager.py:34`
- `tests/test_topic_analyzer.py:85`
- `tests/test_truncate_message_count_regression.py:29`
- `tests/test_upload_handler_cleanup.py:681`

## `SessionManager.__init__` — method, line 118
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

## `SessionManager.load_sessions` — method, line 128
- **called from:**
- `core/session_manager.py:122`
- `tests/test_history_display_model_hydration.py:360`
- `tests/test_history_display_model_hydration.py:444`

## `SessionManager._db_to_session_meta` — method, line 180
- **called from:**
- `core/session_manager.py:163`
- `core/session_manager.py:1003`

## `SessionManager._session_has_live_stream` — method, line 206
- decorator: `staticmethod`
- **called from:**
- `core/session_manager.py:235`
- `core/session_manager.py:972`

## `SessionManager._db_to_session` — method, line 222
- **called from:**
- `core/session_manager.py:997`
- `src/task_scheduler.py:2104`

## `SessionManager._draft_ok` — method, line 226
- **called from:**
- `core/session_manager.py:254`
- `core/session_manager.py:274`

## `SessionManager.add_message` — method, line 320
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

## `SessionManager._persist_message` — method, line 359
- **called from:**
- `core/models.py:153`
- `core/session_manager.py:345`
- `core/session_manager.py:539`
- `tests/test_session_manager_persist_guard.py:28`
- `tests/test_session_manager_persist_guard.py:44`
- `tests/test_upload_handler_cleanup.py:683`

## `SessionManager.create_draft` — method, line 453
- **called from:**
- `routes/chat_routes.py:401`
- `tests/test_draft_promotion_keeps_live_media.py:76`
- `tests/test_draft_promotion_keeps_live_media.py:121`

## `SessionManager._create` — method, line 461
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.update_draft` — method, line 488
- **called from:**
- `routes/chat_routes.py:399`

## `SessionManager._update` — method, line 495
- **called from:**
- `src/mcp_oauth.py:144`
- `src/mcp_oauth.py:152`
- `tests/test_mcp_oauth.py:131`

## `SessionManager.promote_draft` — method, line 512
- **called from:**
- `routes/chat_helpers.py:1308`
- `routes/chat_routes.py:315`
- `tests/test_draft_promotion_keeps_live_media.py:85`

## `SessionManager.append_to_last_assistant` — method, line 584
- **called from:**
- `routes/chat_helpers.py:1293`
- `routes/chat_routes.py:309`
- `routes/chat_routes.py:350`

## `SessionManager.finalize_orphan_draft` — method, line 656
- **called from:**
- `core/session_manager.py:240`
- `routes/history/history_routes.py:218`
- `routes/history/history_routes.py:235`

## `SessionManager.truncate_messages` — method, line 691
- **called from:**
- `routes/history/history_routes.py:459`
- `src/agent_tools/session_tools.py:415`
- `tests/test_truncate_message_count_regression.py:43`
- `tests/test_truncate_message_count_regression.py:72`

## `SessionManager._archived` — method, line 715
- **called from:**
- `core/session_manager.py:721`

## `SessionManager.replace_messages` — method, line 762
- **called from:**
- `routes/session_routes.py:1268`
- `src/context_compactor.py:728`
- `tests/test_parse_msg_content_jsonlike_string.py:55`
- `tests/test_parse_msg_content_jsonlike_string.py:84`
- `tests/test_replace_messages_multimodal.py:62`
- `tests/test_replace_messages_multimodal.py:100`
- `tests/test_replace_messages_multimodal.py:111`
- `tests/test_replace_messages_upload_reservations.py:128`
- `tests/test_replace_messages_upload_reservations.py:170`

## `SessionManager.get_session` — method, line 886
- **called from:**
- `core/session_manager.py:339`
- `core/session_manager.py:522`
- `core/session_manager.py:594`
- `core/session_manager.py:695`
- `core/session_manager.py:764`
- `routes/chat_routes.py:949`
- `routes/chat_routes.py:1341`
- `routes/chat_routes.py:1894`
- `routes/chat_routes.py:3127`
- `routes/chat_routes.py:3230`
- `routes/history/history_routes.py:254`
- `routes/history/history_routes.py:265`
- `routes/history/history_routes.py:348`
- `routes/history/history_routes.py:496`
- `routes/history/history_routes.py:575`
- `routes/history/history_routes.py:641`
- `routes/history/history_routes.py:698`
- `routes/history/history_routes.py:749`
- `routes/history/history_routes.py:876`
- `routes/history/history_routes.py:984`
- `routes/history/history_routes.py:1092`
- `routes/memory/memory_routes.py:127`
- `routes/memory/memory_routes.py:191`
- `routes/memory/memory_routes.py:213`
- `routes/memory/memory_routes.py:223`
- `routes/memory/memory_routes.py:243`
- `routes/memory/memory_routes.py:301`
- `routes/memory/memory_routes.py:357`
- `routes/research/research_routes.py:681`
- `routes/session_routes.py:536`
- `routes/session_routes.py:617`
- `routes/session_routes.py:690`
- `routes/session_routes.py:916`
- `routes/session_routes.py:1030`
- `routes/session_routes.py:1153`
- `routes/session_routes.py:1189`
- `routes/session_routes.py:1570`
- `routes/webhook/webhook_routes.py:260`
- `src/agent_jobs.py:285`
- `src/agent_tools/session_tools.py:59`
- `src/agent_tools/session_tools.py:183`
- `src/agent_tools/session_tools.py:432`
- `src/agent_tools/session_tools.py:450`
- `src/ai_interaction.py:708`
- `src/bg_monitor.py:102`
- `src/chat_helpers.py:446`
- `src/context_compactor.py:783`
- `src/topic_analyzer.py:54`
- `tests/test_draft_promotion_keeps_live_media.py:95`
- `tests/test_draft_promotion_keeps_live_media.py:125`
- `tests/test_history_display_model_hydration.py:260`
- `tests/test_history_display_model_hydration.py:262`
- `tests/test_history_display_model_hydration.py:300`
- `tests/test_history_display_model_hydration.py:303`
- `tests/test_history_display_model_hydration.py:338`
- `tests/test_history_display_model_hydration.py:339`
- `tests/test_history_display_model_hydration.py:380`
- `tests/test_parse_msg_content_jsonlike_string.py:58`
- `tests/test_parse_msg_content_jsonlike_string.py:106`
- `tests/test_replace_messages_multimodal.py:83`
- … +3 more (grep the name in repo)

## `SessionManager.sync_session_metadata` — method, line 919
- **called from:**
- `core/session_manager.py:906`

## `SessionManager._load_session_from_db` — method, line 986
- **called from:**
- `core/session_manager.py:900`
- `core/session_manager.py:912`
- `core/session_manager.py:1163`
- `routes/history/history_routes.py:1079`
- `routes/session_routes.py:965`

## `SessionManager._touch_session` — method, line 1016
- **called from:**
- `core/session_manager.py:915`

## `SessionManager.create_session` — method, line 1030
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

## `SessionManager.delete_session` — method, line 1076
- **called from:**
- `core/session_manager.py:1181`
- `routes/session_routes.py:312`
- `routes/session_routes.py:724`
- `routes/session_routes.py:1335`
- `src/agent_tools/session_tools.py:383`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `SessionManager.trash_session` — method, line 1124
- **called from:**
- `routes/session_routes.py:749`
- `routes/session_routes.py:782`

## `SessionManager.restore_session` — method, line 1151
- **called from:**
- `routes/session_routes.py:887`

## `SessionManager.purge_session` — method, line 1175
- **called from:**
- `routes/session_routes.py:777`
- `routes/session_routes.py:875`
- `routes/session_routes.py:901`

## `SessionManager.list_trashed_sessions` — method, line 1183
- **called from:**
- `routes/session_routes.py:861`
- `routes/session_routes.py:871`

## `SessionManager.update_session_name` — method, line 1215
- **called from:**
- `routes/chat_helpers.py:362`
- `routes/session_routes.py:541`
- `routes/session_routes.py:682`
- `src/agent_tools/session_tools.py:352`

## `SessionManager.archive_session` — method, line 1235
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.mark_important` — method, line 1255
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.get_sessions_for_user` — method, line 1280
- **called from:**
- `routes/session_routes.py:321`
- `routes/session_routes.py:1290`
- `routes/session_routes.py:1379`
- `src/agent_tools/session_tools.py:104`

## `SessionManager.save_sessions` — method, line 1295
- **called from:**
- `routes/chat_helpers.py:1299`
- `routes/chat_helpers.py:1316`
- `routes/chat_routes.py:311`
- `routes/chat_routes.py:320`
- `routes/chat_routes.py:352`
- `routes/chat_routes.py:1098`
- `routes/chat_routes.py:1905`
- `routes/chat_routes.py:2201`
- `routes/chat_routes.py:3130`
- `routes/chat_routes.py:3312`
- `routes/history/history_routes.py:683`
- `routes/history/history_routes.py:734`
- `routes/history/history_routes.py:844`
- `routes/history/history_routes.py:1230`
- `routes/research/research_routes.py:747`
- `routes/research/research_routes.py:775`
- `routes/session_routes.py:718`
- `routes/session_routes.py:1117`
- `routes/session_routes.py:1142`
- `routes/webhook/webhook_routes.py:311`
- `routes/webhook/webhook_routes.py:373`
- `routes/webhook/webhook_routes.py:386`
- `src/agent_jobs.py:335`
- `src/bg_monitor.py:140`
- `src/chat_handler.py:359`

## `SessionManager.ensure_task_session` — method, line 1298
- **called from:**
- `src/task_scheduler.py:1558`
- `src/task_scheduler.py:1736`

## `SessionManager.cleanup_empty_sessions` — method, line 1317
- **called from:**
- `tests/test_session_manager_cleanup.py:29`
