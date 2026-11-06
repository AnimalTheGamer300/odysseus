# `core/session_manager.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_commit_draft_with_retry` — function, line 44
- **called from:**
- `core/session_manager.py:485`
- `core/session_manager.py:509`

## `_message_timestamp_iso` — function, line 72
- **called from:**
- `core/session_manager.py:251`
- `core/session_manager.py:271`
- `core/session_manager.py:405`
- `core/session_manager.py:469`
- `core/session_manager.py:558`

## `_parse_msg_content` — function, line 81
- **called from:**
- `core/session_manager.py:254`
- `core/session_manager.py:274`

## `SessionManager` — class, line 107
- **called from:**
- `src/app_initializer.py:92`
- `tests/helpers/database.py:51`
- `tests/test_session_concurrent.py:21`
- `tests/test_session_concurrent.py:51`
- `tests/test_session_concurrent.py:83`
- `tests/test_session_discovery_message_count.py:23`
- `tests/test_session_discovery_message_count.py:55`
- `tests/test_session_manager.py:34`
- `tests/test_topic_analyzer.py:85`
- `tests/test_upload_handler_cleanup.py:681`

## `SessionManager.__init__` — method, line 118
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

## `SessionManager.load_sessions` — method, line 128
- **called from:**
- `core/session_manager.py:122`
- `scripts/build_historical_harness_queue.py:324`
- `tests/test_history_display_model_hydration.py:364`
- `tests/test_history_display_model_hydration.py:448`

## `SessionManager._db_to_session_meta` — method, line 179
- **called from:**
- `core/session_manager.py:162`
- `core/session_manager.py:892`
- `tests/test_chatgpt_session_binding.py:53`
- `tests/test_session_cwd_persistence.py:39`
- `tests/test_session_header_persistence.py:35`

## `SessionManager._db_to_session` — method, line 211
- **called from:**
- `core/session_manager.py:886`
- `src/task_scheduler.py:2298`
- `tests/test_chatgpt_session_binding.py:54`

## `SessionManager._draft_ok` — method, line 215
- **called from:**
- `core/session_manager.py:248`
- `core/session_manager.py:268`

## `SessionManager.add_message` — method, line 322
- **called from:**
- `routes/chat_helpers.py:952`
- `routes/chat_helpers.py:1967`
- `routes/chat_routes.py:1515`
- `routes/chat_routes.py:2625`
- `routes/chat_routes.py:4194`
- `routes/chat_routes.py:4495`
- `routes/chat_routes.py:5623`
- `routes/history/history_routes.py:675`
- `routes/history/history_routes.py:1127`
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

## `SessionManager._persist_message` — method, line 361
- **called from:**
- `core/models.py:162`
- `core/session_manager.py:347`
- `core/session_manager.py:541`
- `tests/test_session_manager_persist_guard.py:28`
- `tests/test_session_manager_persist_guard.py:44`
- `tests/test_upload_handler_cleanup.py:683`

## `SessionManager.create_draft` — method, line 455
- **called from:**
- `routes/chat_routes.py:1597`

## `SessionManager._create` — method, line 463
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.update_draft` — method, line 490
- **called from:**
- `routes/chat_routes.py:1595`

## `SessionManager._update` — method, line 497
- **called from:**
- `src/mcp_oauth.py:144`
- `src/mcp_oauth.py:152`
- `tests/test_mcp_oauth.py:131`

## `SessionManager.promote_draft` — method, line 514
- **called from:**
- `routes/chat_helpers.py:1963`
- `routes/chat_routes.py:1511`

## `SessionManager.finalize_orphan_draft` — method, line 586
- **called from:**
- `core/session_manager.py:234`
- `routes/history/history_routes.py:363`
- `routes/history/history_routes.py:380`

## `SessionManager.truncate_messages` — method, line 621
- **called from:**
- `routes/history/history_routes.py:641`
- `src/agent_tools/session_tools.py:438`
- `tests/test_database_test_isolation.py:47`
- `tests/test_truncate_message_count_regression.py:34`
- `tests/test_truncate_message_count_regression.py:63`

## `SessionManager.replace_messages` — method, line 669
- **called from:**
- `routes/session_routes.py:1422`
- `src/context_compactor.py:1002`
- `tests/test_parse_msg_content_jsonlike_string.py:55`
- `tests/test_parse_msg_content_jsonlike_string.py:84`
- `tests/test_replace_messages_multimodal.py:62`
- `tests/test_replace_messages_multimodal.py:100`
- `tests/test_replace_messages_multimodal.py:111`
- `tests/test_replace_messages_upload_reservations.py:128`
- `tests/test_replace_messages_upload_reservations.py:170`

## `SessionManager.get_session` — method, line 793
- **called from:**
- `core/session_manager.py:341`
- `core/session_manager.py:524`
- `core/session_manager.py:623`
- `core/session_manager.py:671`
- `routes/chat_helpers.py:827`
- `routes/chat_routes.py:2436`
- `routes/chat_routes.py:2994`
- `routes/chat_routes.py:4184`
- `routes/chat_routes.py:5621`
- `routes/chat_routes.py:5724`
- `routes/history/history_routes.py:399`
- `routes/history/history_routes.py:410`
- `routes/history/history_routes.py:494`
- `routes/history/history_routes.py:689`
- `routes/history/history_routes.py:781`
- `routes/history/history_routes.py:828`
- `routes/history/history_routes.py:885`
- `routes/history/history_routes.py:936`
- `routes/history/history_routes.py:1092`
- `routes/history/history_routes.py:1201`
- `routes/history/history_routes.py:1258`
- `routes/history/history_routes.py:1294`
- `routes/history/history_routes.py:1333`
- `routes/history/history_routes.py:1369`
- `routes/history/history_routes.py:1491`
- `routes/memory/memory_routes.py:127`
- `routes/memory/memory_routes.py:191`
- `routes/memory/memory_routes.py:213`
- `routes/memory/memory_routes.py:223`
- `routes/memory/memory_routes.py:243`
- `routes/memory/memory_routes.py:304`
- `routes/memory/memory_routes.py:361`
- `routes/research/research_routes.py:803`
- `routes/session_routes.py:703`
- `routes/session_routes.py:811`
- `routes/session_routes.py:884`
- `routes/session_routes.py:1061`
- `routes/session_routes.py:1176`
- `routes/session_routes.py:1299`
- `routes/session_routes.py:1335`
- `routes/session_routes.py:1707`
- `routes/webhook/webhook_routes.py:260`
- `src/agent_jobs.py:285`
- `src/agent_tools/session_tools.py:43`
- `src/agent_tools/session_tools.py:73`
- `src/agent_tools/session_tools.py:199`
- `src/agent_tools/session_tools.py:455`
- `src/agent_tools/session_tools.py:473`
- `src/ai_interaction.py:804`
- `src/background_tool_jobs.py:100`
- `src/bg_monitor.py:138`
- `src/chat_helpers.py:758`
- `src/context_compactor.py:1057`
- `src/topic_analyzer.py:54`
- `tests/test_database_test_isolation.py:69`
- `tests/test_history_add_message_validation.py:47`
- `tests/test_history_add_message_validation.py:61`
- `tests/test_history_display_model_hydration.py:264`
- `tests/test_history_display_model_hydration.py:266`
- `tests/test_history_display_model_hydration.py:304`
- … +11 more (grep the name in repo)

## `SessionManager.sync_session_metadata` — method, line 826
- **called from:**
- `core/session_manager.py:813`
- `tests/test_chatgpt_session_binding.py:57`

## `SessionManager._load_session_from_db` — method, line 878
- **called from:**
- `core/session_manager.py:807`
- `core/session_manager.py:819`
- `routes/history/history_routes.py:1478`
- `routes/session_routes.py:1110`

## `SessionManager._touch_session` — method, line 905
- **called from:**
- `core/session_manager.py:822`

## `SessionManager.create_session` — method, line 919
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

## `SessionManager.delete_session` — method, line 975
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

## `SessionManager.update_session_name` — method, line 1026
- **called from:**
- `routes/chat_helpers.py:637`
- `routes/chat_helpers.py:692`
- `routes/chat_helpers.py:701`
- `routes/chat_helpers.py:709`
- `routes/chat_helpers.py:753`
- `routes/chat_helpers.py:800`
- `routes/chat_helpers.py:808`
- `routes/session_routes.py:708`
- `routes/session_routes.py:876`
- `src/agent_tools/session_tools.py:373`

## `SessionManager.archive_session` — method, line 1046
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.mark_important` — method, line 1066
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SessionManager.get_sessions_for_user` — method, line 1091
- **called from:**
- `routes/session_routes.py:458`
- `routes/session_routes.py:1453`
- `routes/session_routes.py:1507`
- `src/agent_tools/session_tools.py:118`

## `SessionManager.save_sessions` — method, line 1100
- **called from:**
- `routes/chat_helpers.py:1954`
- `routes/chat_helpers.py:1971`
- `routes/chat_routes.py:1507`
- `routes/chat_routes.py:1516`
- `routes/chat_routes.py:1548`
- `routes/chat_routes.py:2629`
- `routes/chat_routes.py:4195`
- `routes/chat_routes.py:4496`
- `routes/chat_routes.py:5624`
- `routes/chat_routes.py:5808`
- `routes/history/history_routes.py:870`
- `routes/history/history_routes.py:921`
- `routes/history/history_routes.py:1042`
- `routes/history/history_routes.py:1313`
- `routes/history/history_routes.py:1350`
- `routes/history/history_routes.py:1637`
- `routes/research/research_routes.py:859`
- `routes/research/research_routes.py:887`
- `routes/session_routes.py:912`
- `routes/session_routes.py:1263`
- `routes/session_routes.py:1288`
- `routes/webhook/webhook_routes.py:311`
- `routes/webhook/webhook_routes.py:373`
- `routes/webhook/webhook_routes.py:386`
- `src/agent_jobs.py:335`
- `src/bg_monitor.py:208`
- `src/chat_handler.py:375`

## `SessionManager.ensure_task_session` — method, line 1103
- **called from:**
- `src/task_scheduler.py:1718`
- `src/task_scheduler.py:1898`

## `SessionManager.cleanup_empty_sessions` — method, line 1122
- **called from:**
- `tests/test_session_manager_cleanup.py:29`
