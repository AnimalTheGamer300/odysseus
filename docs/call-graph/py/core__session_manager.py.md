# `core/session_manager.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_commit_draft_with_retry` — function, line 44
- **called from:**
- `core/session_manager.py:469`
- `core/session_manager.py:493`

## `_message_timestamp_iso` — function, line 72
- **called from:**
- `core/session_manager.py:243`
- `core/session_manager.py:263`
- `core/session_manager.py:389`
- `core/session_manager.py:453`
- `core/session_manager.py:542`

## `_parse_msg_content` — function, line 81
- **called from:**
- `core/session_manager.py:246`
- `core/session_manager.py:266`

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

## `SessionManager._db_to_session_meta` — method, line 179
- **called from:**
- `core/session_manager.py:162`
- `core/session_manager.py:874`

## `SessionManager._db_to_session` — method, line 203
- **called from:**
- `core/session_manager.py:868`
- `src/task_scheduler.py:2104`

## `SessionManager._draft_ok` — method, line 207
- **called from:**
- `core/session_manager.py:240`
- `core/session_manager.py:260`

## `SessionManager.add_message` — method, line 306
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

## `SessionManager._persist_message` — method, line 345
- **called from:**
- `core/models.py:151`
- `core/session_manager.py:331`
- `core/session_manager.py:525`
- `tests/test_session_manager_persist_guard.py:28`
- `tests/test_session_manager_persist_guard.py:44`
- `tests/test_upload_handler_cleanup.py:683`

## `SessionManager.create_draft` — method, line 439
- **called from:**
- `routes/chat_routes.py:401`

## `SessionManager._create` — method, line 447
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.update_draft` — method, line 474
- **called from:**
- `routes/chat_routes.py:399`

## `SessionManager._update` — method, line 481
- **called from:**
- `src/mcp_oauth.py:144`
- `src/mcp_oauth.py:152`
- `tests/test_mcp_oauth.py:131`

## `SessionManager.promote_draft` — method, line 498
- **called from:**
- `routes/chat_helpers.py:1308`
- `routes/chat_routes.py:315`

## `SessionManager.finalize_orphan_draft` — method, line 570
- **called from:**
- `core/session_manager.py:226`
- `routes/history/history_routes.py:216`
- `routes/history/history_routes.py:233`

## `SessionManager.truncate_messages` — method, line 605
- **called from:**
- `routes/history/history_routes.py:447`
- `src/agent_tools/session_tools.py:415`
- `tests/test_truncate_message_count_regression.py:43`
- `tests/test_truncate_message_count_regression.py:72`

## `SessionManager.replace_messages` — method, line 653
- **called from:**
- `routes/session_routes.py:1200`
- `src/context_compactor.py:728`
- `tests/test_parse_msg_content_jsonlike_string.py:55`
- `tests/test_parse_msg_content_jsonlike_string.py:84`
- `tests/test_replace_messages_multimodal.py:62`
- `tests/test_replace_messages_multimodal.py:100`
- `tests/test_replace_messages_multimodal.py:111`
- `tests/test_replace_messages_upload_reservations.py:128`
- `tests/test_replace_messages_upload_reservations.py:170`

## `SessionManager.get_session` — method, line 777
- **called from:**
- `core/session_manager.py:325`
- `core/session_manager.py:508`
- `core/session_manager.py:607`
- `core/session_manager.py:655`
- `routes/chat_routes.py:949`
- `routes/chat_routes.py:1341`
- `routes/chat_routes.py:1894`
- `routes/chat_routes.py:3127`
- `routes/chat_routes.py:3230`
- `routes/history/history_routes.py:252`
- `routes/history/history_routes.py:263`
- `routes/history/history_routes.py:346`
- `routes/history/history_routes.py:482`
- `routes/history/history_routes.py:557`
- `routes/history/history_routes.py:604`
- `routes/history/history_routes.py:661`
- `routes/history/history_routes.py:712`
- `routes/history/history_routes.py:839`
- `routes/history/history_routes.py:947`
- `routes/history/history_routes.py:1055`
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
- `routes/session_routes.py:848`
- `routes/session_routes.py:962`
- `routes/session_routes.py:1085`
- `routes/session_routes.py:1121`
- `routes/session_routes.py:1500`
- `routes/webhook/webhook_routes.py:260`
- `src/agent_jobs.py:285`
- `src/agent_tools/session_tools.py:59`
- `src/agent_tools/session_tools.py:183`
- `src/agent_tools/session_tools.py:432`
- `src/agent_tools/session_tools.py:450`
- `src/ai_interaction.py:708`
- `src/bg_monitor.py:102`
- `src/chat_helpers.py:444`
- `src/context_compactor.py:783`
- `src/topic_analyzer.py:54`
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
- `tests/test_replace_messages_multimodal.py:102`
- `tests/test_session_discovery_message_count.py:61`
- `tests/test_session_manager.py:192`

## `SessionManager.sync_session_metadata` — method, line 810
- **called from:**
- `core/session_manager.py:797`

## `SessionManager._load_session_from_db` — method, line 860
- **called from:**
- `core/session_manager.py:791`
- `core/session_manager.py:803`
- `routes/history/history_routes.py:1042`
- `routes/session_routes.py:897`

## `SessionManager._touch_session` — method, line 887
- **called from:**
- `core/session_manager.py:806`

## `SessionManager.create_session` — method, line 901
- **called from:**
- `core/session_manager.py:1082`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:848`
- `routes/research/research_routes.py:737`
- `routes/session_routes.py:494`
- `routes/session_routes.py:1065`
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

## `SessionManager.delete_session` — method, line 947
- **called from:**
- `routes/session_routes.py:312`
- `routes/session_routes.py:724`
- `routes/session_routes.py:749`
- `routes/session_routes.py:773`
- `routes/session_routes.py:1267`
- `routes/session_routes.py:1300`
- `src/agent_tools/session_tools.py:383`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `SessionManager.update_session_name` — method, line 995
- **called from:**
- `routes/chat_helpers.py:362`
- `routes/session_routes.py:541`
- `routes/session_routes.py:682`
- `src/agent_tools/session_tools.py:352`

## `SessionManager.archive_session` — method, line 1015
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.mark_important` — method, line 1035
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.get_sessions_for_user` — method, line 1060
- **called from:**
- `routes/session_routes.py:321`
- `routes/session_routes.py:1222`
- `routes/session_routes.py:1309`
- `src/agent_tools/session_tools.py:104`

## `SessionManager.save_sessions` — method, line 1069
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
- `routes/history/history_routes.py:646`
- `routes/history/history_routes.py:697`
- `routes/history/history_routes.py:807`
- `routes/history/history_routes.py:1193`
- `routes/research/research_routes.py:747`
- `routes/research/research_routes.py:775`
- `routes/session_routes.py:718`
- `routes/session_routes.py:1049`
- `routes/session_routes.py:1074`
- `routes/webhook/webhook_routes.py:311`
- `routes/webhook/webhook_routes.py:373`
- `routes/webhook/webhook_routes.py:386`
- `src/agent_jobs.py:335`
- `src/bg_monitor.py:140`
- `src/chat_handler.py:359`

## `SessionManager.ensure_task_session` — method, line 1072
- **called from:**
- `src/task_scheduler.py:1558`
- `src/task_scheduler.py:1736`

## `SessionManager.cleanup_empty_sessions` — method, line 1091
- **called from:**
- `tests/test_session_manager_cleanup.py:29`
