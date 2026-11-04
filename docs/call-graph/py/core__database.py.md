# `core/database.py` — definitions & call sites

105 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `utcnow_naive` — function, line 23
- **called from:**
- `core/database.py:871`
- `core/database.py:2029`
- `core/database.py:2647`
- `core/database.py:2658`
- `core/database.py:2703`
- `core/database.py:2748`
- `core/session_manager.py:1104`
- `core/session_manager.py:1105`
- `routes/chatgpt_subscription_routes.py:58`
- `routes/session_routes.py:228`
- `routes/session_routes.py:297`
- `routes/session_routes.py:550`
- `routes/session_routes.py:597`
- `routes/session_routes.py:856`
- `routes/session_routes.py:890`
- `routes/session_routes.py:1093`
- `routes/session_routes.py:1196`
- `routes/session_routes.py:1256`
- `routes/session_routes.py:1473`
- `src/chatgpt_subscription.py:279`
- `tests/test_database_utcnow.py:13`
- `tests/test_database_utcnow.py:16`
- `tests/test_session_actions_cleanup.py:76`
- `tests/test_session_actions_cleanup.py:79`
- `tests/test_session_actions_cleanup.py:80`
- `tests/test_session_actions_cleanup.py:112`
- `tests/test_session_actions_cleanup.py:115`
- `tests/test_session_actions_cleanup.py:135`
- `tests/test_session_list_owner_scope.py:89`

## `TimestampMixin` — class, line 28
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TimestampMixin.created_at` — method, line 31
- decorator: `declared_attr`
- **called from:**
- `static/js/gallery.js:1396`

## `TimestampMixin.updated_at` — method, line 35
- decorator: `declared_attr`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_default_database_url` — function, line 43
- **called from:**
- `core/database.py:73`

## `_normalize_sqlite_url` — function, line 47
- **called from:**
- `core/database.py:73`
- `tests/test_app_db_permissions.py:59`

## `_sqlite_db_path` — function, line 88
- **called from:**
- `core/database.py:2088`
- `core/database.py:2117`
- `tests/test_app_db_permissions.py:73`
- `tests/test_app_db_permissions.py:74`
- `tests/test_app_db_permissions.py:76`
- `tests/test_app_db_permissions.py:78`
- `tests/test_app_db_permissions.py:79`
- `tests/test_app_db_permissions.py:81`
- `tests/test_app_db_permissions.py:82`
- `tests/test_app_db_permissions.py:83`
- `tests/test_app_db_permissions.py:132`
- `tests/test_app_db_permissions.py:136`
- `tests/test_app_db_permissions.py:142`
- `tests/test_app_db_permissions.py:153`
- `tests/test_app_db_permissions.py:161`
- `tests/test_app_db_permissions.py:165`

## `set_sqlite_pragma` — function, line 143
- decorator: `event.listens_for(Engine, "connect")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EncryptedText` — class, line 164
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EncryptedText.process_bind_param` — method, line 176
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `EncryptedText.process_result_value` — method, line 182
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Session` — class, line 189
- **called from:**
- `core/session_manager.py:188`
- `core/session_manager.py:281`
- `core/session_manager.py:927`
- `tests/test_api_token_tool_authority.py:24`
- `tests/test_api_token_tool_authority.py:97`
- `tests/test_external_context_tool_gate.py:221`
- `tests/test_history_display_model_hydration.py:245`
- `tests/test_history_display_model_hydration.py:326`
- `tests/test_replace_messages_multimodal.py:32`
- `tests/test_replace_messages_upload_reservations.py:46`
- `tests/test_research_query_fallback.py:15`
- `tests/test_session_concurrent.py:24`
- `tests/test_session_concurrent.py:25`
- `tests/test_session_concurrent.py:54`
- `tests/test_session_concurrent.py:55`
- `tests/test_session_concurrent.py:86`
- `tests/test_session_concurrent.py:87`
- `tests/test_session_context_excludes_slash.py:14`
- `tests/test_session_context_excludes_slash.py:41`
- `tests/test_session_image_cleanup.py:29`
- `tests/test_session_manager.py:47`
- `tests/test_session_manager.py:48`
- `tests/test_session_manager.py:62`
- `tests/test_session_manager.py:63`
- `tests/test_session_manager.py:76`
- `tests/test_session_manager.py:91`
- `tests/test_session_manager.py:103`
- `tests/test_session_manager.py:116`
- `tests/test_session_manager.py:117`
- `tests/test_session_manager.py:129`
- `tests/test_session_manager.py:140`
- `tests/test_session_manager.py:156`
- `tests/test_session_manager.py:157`
- `tests/test_session_manager.py:158`
- `tests/test_session_manager.py:173`
- `tests/test_session_manager.py:188`
- `tests/test_sqlite_foreign_keys.py:20`
- `tests/test_tool_approval_task_scope.py:126`
- `tests/test_tool_approval_task_scope.py:145`
- `tests/test_tool_approval_task_scope.py:175`

## `Session.is_active` — method, line 243
- decorator: `property`
- **called from:**
- `routes/chat_routes.py:3115`
- `routes/session_routes.py:132`
- `src/agent_jobs.py:295`
- `src/bg_monitor.py:115`

## `Session.to_dict` — method, line 247
- **called from:**
- `core/models.py:164`
- `routes/chat_routes.py:3149`
- `services/memory/skills.py:226`
- `services/memory/skills.py:382`
- `services/memory/skills.py:430`
- `src/model_capabilities.py:538`
- `src/model_capability_readers/base.py:66`
- `src/model_capability_readers/base.py:67`
- `src/model_capability_readers/base.py:68`
- `tests/test_history_compact_tool_calls.py:90`
- `tests/test_model_capabilities.py:68`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:83`
- `tests/test_model_capabilities.py:154`

## `ChatMessage` — class, line 268
- **called from:**
- `core/session_manager.py:244`
- `core/session_manager.py:264`
- `routes/chat_helpers.py:470`
- `routes/chat_helpers.py:1309`
- `routes/chat_helpers.py:1312`
- `routes/chat_routes.py:316`
- `routes/chat_routes.py:319`
- `routes/chat_routes.py:1094`
- `routes/chat_routes.py:1904`
- `routes/chat_routes.py:2200`
- `routes/chat_routes.py:3129`
- `routes/history/history_routes.py:256`
- `routes/history/history_routes.py:467`
- `routes/history/history_routes.py:873`
- `routes/history/history_routes.py:1110`
- `routes/history/history_routes.py:1116`
- `routes/research/research_routes.py:770`
- `routes/session_routes.py:713`
- `routes/session_routes.py:1190`
- `routes/webhook/webhook_routes.py:377`
- `routes/webhook/webhook_routes.py:385`
- `src/agent_jobs.py:326`
- `src/agent_tools/session_tools.py:229`
- `src/agent_tools/session_tools.py:230`
- `src/bg_monitor.py:131`
- `src/chat_handler.py:351`
- `src/chat_handler.py:353`
- `src/context_compactor.py:709`
- `src/task_scheduler.py:1773`
- `src/task_scheduler.py:1781`
- `tests/test_api_token_tool_authority.py:45`
- `tests/test_api_token_tool_authority.py:50`
- `tests/test_api_token_tool_authority.py:73`
- `tests/test_api_token_tool_authority.py:74`
- `tests/test_api_token_tool_authority.py:103`
- `tests/test_api_token_tool_authority.py:104`
- `tests/test_api_token_tool_authority.py:135`
- `tests/test_api_token_tool_authority.py:136`
- `tests/test_api_token_tool_authority.py:314`
- `tests/test_api_token_tool_authority.py:315`
- `tests/test_fork_session_metadata.py:63`
- `tests/test_fork_session_metadata.py:64`
- `tests/test_history_compact_tool_calls.py:175`
- `tests/test_history_compact_tool_calls.py:176`
- `tests/test_history_compact_tool_calls.py:177`
- `tests/test_history_compact_tool_calls.py:178`
- `tests/test_history_compact_tool_calls.py:179`
- `tests/test_history_compact_tool_calls.py:180`
- `tests/test_history_compact_tool_calls.py:193`
- `tests/test_history_compact_tool_calls.py:194`
- `tests/test_history_compact_tool_calls.py:195`
- `tests/test_history_compact_tool_calls.py:196`
- `tests/test_history_compact_tool_calls.py:207`
- `tests/test_history_compact_tool_calls.py:208`
- `tests/test_history_compact_tool_calls.py:209`
- `tests/test_history_compact_tool_calls.py:210`
- `tests/test_history_compact_tool_calls.py:211`
- `tests/test_history_compact_tool_calls.py:212`
- `tests/test_history_compact_tool_calls.py:228`
- `tests/test_history_compact_tool_calls.py:229`
- … +63 more (grep the name in repo)

## `Document` — class, line 297
- **called from:**
- `mcp_servers/email_server.py:1684`
- `routes/document/document_routes.py:180`
- `src/agent_tools/document_tools.py:324`
- `src/agent_tools/document_tools.py:440`
- `src/office_doc.py:45`
- `src/pdf_form_doc.py:230`
- `src/pdf_form_doc.py:413`
- `tests/test_auth_disabled_document_access.py:81`
- `tests/test_auth_disabled_document_access.py:266`
- `tests/test_document_close_clears_active_route.py:63`
- `tests/test_document_render_pdf_iframe.py:165`
- `tests/test_document_session_owner_scope.py:68`
- `tests/test_document_session_owner_scope.py:78`
- `tests/test_document_session_owner_scope.py:88`
- `tests/test_document_tidy_null_timestamp.py:37`
- `tests/test_document_tidy_null_timestamp.py:39`
- `tests/test_markitdown_runtime.py:67`
- `tests/test_upload_handler_cleanup.py:495`
- `tests/test_upload_handler_cleanup.py:670`
- `static/js/document.js:9792`

## `DocumentVersion` — class, line 330
- **called from:**
- `mcp_servers/email_server.py:1657`
- `mcp_servers/email_server.py:1698`
- `routes/document/document_routes.py:165`
- `routes/document/document_routes.py:193`
- `routes/document/document_routes.py:545`
- `routes/document/document_routes.py:674`
- `routes/document/document_routes.py:829`
- `src/agent_tools/document_tools.py:334`
- `src/agent_tools/document_tools.py:450`
- `src/agent_tools/document_tools.py:538`
- `src/agent_tools/document_tools.py:622`
- `src/agent_tools/document_tools.py:690`
- `src/office_doc.py:55`
- `src/pdf_form_doc.py:240`
- `src/pdf_form_doc.py:423`
- `tests/test_upload_handler_cleanup.py:502`

## `GalleryAlbum` — class, line 345
- **called from:**
- `routes/gallery/gallery_routes.py:860`
- `tests/test_admin_wipe_gallery.py:18`
- `tests/test_gallery_null_user_routes.py:28`
- `tests/test_gallery_null_user_routes.py:29`

## `GalleryImage` — class, line 358
- **called from:**
- `mcp_servers/image_gen_server.py:143`
- `routes/gallery/gallery_routes.py:408`
- `routes/upload_routes.py:236`
- `src/ai_interaction.py:1115`
- `src/ai_interaction.py:1262`
- `src/ai_interaction.py:1532`
- `src/tools/image.py:73`
- `tests/test_admin_wipe_gallery.py:19`
- `tests/test_gallery_delete_file_ordering.py:34`
- `tests/test_gallery_filename_confinement.py:101`
- `tests/test_gallery_null_user_routes.py:30`
- `tests/test_gallery_null_user_routes.py:42`
- `tests/test_gallery_owner_filter_single_user.py:30`
- `tests/test_session_image_cleanup.py:31`
- `tests/test_session_image_cleanup.py:41`
- `tests/test_upload_handler_cleanup.py:134`
- `tests/test_upload_handler_cleanup.py:508`

## `EmailAccount` — class, line 400
- **called from:**
- `routes/email_routes.py:5547`
- `routes/email_routes.py:5666`
- `scripts/demo_email/demo_account.py:107`
- `tests/test_email_account_default_serialization.py:69`
- `tests/test_email_account_default_serialization.py:498`
- `tests/test_email_account_default_serialization.py:505`
- `tests/test_email_oauth.py:171`
- `tests/test_email_ownerless_account_owner_scope.py:32`
- `tests/test_email_test_connection_oauth.py:34`

## `EmailAccountOwnerLock` — class, line 447
- **called from:**
- `core/database.py:517`

## `lock_email_account_owner_mutations` — function, line 488
- **called from:**
- `core/database.py:2024`
- `routes/auth_routes.py:388`
- `routes/email_routes.py:203`
- `scripts/demo_email/demo_account.py:65`
- `tests/test_email_account_default_serialization.py:358`

## `ModelEndpoint` — class, line 534
- **called from:**
- `routes/chatgpt_subscription_routes.py:71`
- `routes/cookbook_routes.py:1567`
- `routes/cookbook_routes.py:1903`
- `routes/copilot_routes.py:70`
- `routes/model_routes.py:2159`
- `src/agent_tools/admin_tools.py:48`
- `tests/test_chatgpt_subscription_routes.py:98`
- `tests/test_chatgpt_subscription_routes.py:175`
- `tests/test_resolve_session_auth_chatgpt.py:36`
- `tests/test_resolve_session_auth_chatgpt.py:88`
- `tests/test_resolve_session_auth_chatgpt.py:130`

## `ProviderAuthSession` — class, line 570
- **called from:**
- `routes/chatgpt_subscription_routes.py:46`
- `tests/test_chatgpt_subscription_routes.py:92`

## `McpServer` — class, line 584
- **called from:**
- `routes/mcp/mcp_routes.py:240`
- `src/agent_tools/admin_tools.py:266`

## `Comparison` — class, line 601
- **called from:**
- `routes/compare/compare_routes.py:203`
- `routes/compare/compare_routes.py:300`

## `Signature` — class, line 627
- **called from:**
- `routes/signature_routes.py:108`

## `ApiToken` — class, line 648
- **called from:**
- `companion/pairing.py:196`
- `routes/api_token_routes.py:135`
- `src/agent_tools/admin_tools.py:469`

## `Webhook` — class, line 662
- **called from:**
- `routes/webhook/webhook_routes.py:127`
- `src/agent_tools/admin_tools.py:406`
- `static/js/settings.js:2373`
- `static/js/settings.js:2415`

## `UserTool` — class, line 677
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `UserToolData` — class, line 702
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CrewMember` — class, line 720
- **called from:**
- `src/task_scheduler.py:2620`

## `ScheduledTask` — class, line 744
- **called from:**
- `routes/task/task_routes.py:528`
- `src/task_scheduler.py:2476`
- `src/tools/system.py:355`
- `tests/test_manage_tasks_owner_scope.py:46`
- `tests/test_scheduler_restart_doublefire.py:128`
- `tests/test_scheduler_restart_doublefire.py:159`
- `tests/test_scheduler_restart_doublefire.py:182`
- `tests/test_task_chain_owner_scope.py:48`
- `tests/test_task_cookbook_admin_gate.py:124`
- `tests/test_task_scheduler_cancel.py:47`
- `static/js/cookbookServe.js:1815`

## `EditorDraft` — class, line 792
- **called from:**
- `routes/editor_draft_routes.py:116`

## `TaskRun` — class, line 824
- **called from:**
- `src/task_scheduler.py:749`
- `src/task_scheduler.py:882`
- `tests/test_task_cookbook_admin_gate.py:270`

## `Memory` — class, line 847
- **called from:**
- `services/memory/service.py:54`
- `services/memory/service.py:67`
- `static/js/tasks.js:444`

## `_migrate_add_last_message_at_column` — function, line 882
- **called from:**
- `core/database.py:2157`

## `_migrate_add_document_archived_column` — function, line 927
- **called from:**
- `core/database.py:2156`

## `_migrate_add_owner_column` — function, line 951
- **called from:**
- `core/database.py:2155`

## `_migrate_model_endpoints` — function, line 975
- **called from:**
- `core/database.py:2108`

## `_migrate_add_hidden_models_column` — function, line 998
- **called from:**
- `core/database.py:2145`

## `_migrate_add_model_endpoint_owner_column` — function, line 1021
- **called from:**
- `core/database.py:2151`

## `_migrate_add_provider_auth_id_column` — function, line 1053
- **called from:**
- `core/database.py:2152`

## `_migrate_add_model_type_column` — function, line 1078
- **called from:**
- `core/database.py:2149`

## `_migrate_add_model_endpoint_refresh_columns` — function, line 1101
- **called from:**
- `core/database.py:2150`

## `_migrate_add_task_run_model_column` — function, line 1129
- **called from:**
- `core/database.py:2154`

## `_migrate_add_supports_tools_column` — function, line 1152
- **called from:**
- `core/database.py:2153`

## `_migrate_add_cached_models_column` — function, line 1176
- **called from:**
- `core/database.py:2146`

## `_migrate_add_pinned_models_column` — function, line 1198
- **called from:**
- `core/database.py:2147`

## `_migrate_add_notes_sort_order` — function, line 1221
- **called from:**
- `core/database.py:2148`

## `_migrate_add_mode_column` — function, line 1253
- **called from:**
- `core/database.py:2160`

## `_migrate_add_folder_column` — function, line 1276
- **called from:**
- `core/database.py:2158`

## `_migrate_add_token_columns` — function, line 1299
- **called from:**
- `core/database.py:2159`

## `_migrate_add_owner_to_table` — function, line 1323
- **called from:**
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1351`
- `core/database.py:1352`
- `core/database.py:1353`
- `core/database.py:1356`

## `_migrate_add_multiuser_owner_columns` — function, line 1347
- **called from:**
- `core/database.py:2161`

## `_migrate_add_gallery_caption_column` — function, line 1359
- **called from:**
- `core/database.py:2162`

## `_migrate_add_api_token_scopes_column` — function, line 1382
- **called from:**
- `core/database.py:2163`

## `_migrate_assign_legacy_owner` — function, line 1410
- **called from:**
- `core/database.py:2165`
- `tests/test_foreground_model_routing.py:2063`

## `_migrate_backfill_document_owner_from_session` — function, line 1534
- **called from:**
- `core/database.py:2164`

## `_migrate_add_tidy_verdict` — function, line 1561
- **called from:**
- `core/database.py:2166`

## `_migrate_add_doc_source_email_cols` — function, line 1574
- **called from:**
- `core/database.py:2167`

## `_migrate_add_task_automation_columns` — function, line 1598
- **called from:**
- `core/database.py:2170`

## `_migrate_add_email_oauth_columns` — function, line 1671
- **called from:**
- `core/database.py:2169`

## `_migrate_add_oauth_config` — function, line 1690
- **called from:**
- `core/database.py:2168`

## `_migrate_add_disabled_tools` — function, line 1702
- **called from:**
- `core/database.py:2171`

## `_migrate_add_mcp_oauth_tokens_column` — function, line 1714
- **called from:**
- `core/database.py:2172`

## `_migrate_add_task_v2_columns` — function, line 1731
- **called from:**
- `core/database.py:2173`

## `_migrate_drop_ping_notes_tasks` — function, line 1751
- **called from:**
- `core/database.py:2175`

## `_migrate_add_notifications_enabled` — function, line 1772
- **called from:**
- `core/database.py:2174`

## `_migrate_add_crew_member_id` — function, line 1785
- **called from:**
- `core/database.py:2176`

## `_migrate_add_assistant_columns` — function, line 1802
- **called from:**
- `core/database.py:2177`

## `Note` — class, line 1822
- **called from:**
- `routes/note/note_routes.py:663`
- `src/tools/calendar.py:183`
- `src/tools/notes.py:215`
- `tests/test_notes_fail_closed_auth.py:113`
- `tests/test_notes_fail_closed_auth.py:115`
- `tests/test_notes_fail_closed_auth.py:181`
- `tests/test_upload_handler_cleanup.py:517`
- `static/js/slashCommands.js:1715`

## `CalendarCal` — class, line 1852
- **called from:**
- `routes/calendar_routes.py:307`
- `routes/calendar_routes.py:1367`
- `routes/calendar_routes.py:1434`
- `src/caldav_sync.py:325`
- `tests/test_caldav_bidirectional_sync.py:101`
- `tests/test_caldav_sync_prune_local_events.py:59`
- `tests/test_caldav_sync_uid_scope.py:32`
- `tests/test_caldav_sync_uid_scope.py:33`
- `tests/test_caldav_writeback_route.py:71`
- `tests/test_calendar_default_transaction.py:227`
- `tests/test_calendar_default_transaction.py:345`
- `tests/test_calendar_default_transaction.py:405`
- `tests/test_calendar_default_transaction.py:458`
- `tests/test_calendar_default_transaction.py:501`
- `tests/test_calendar_import_zero_duration.py:132`
- `tests/test_checkin_digest_owner_scope.py:31`
- `tests/test_checkin_digest_owner_scope.py:32`
- `tests/test_upload_handler_cleanup.py:524`

## `CalendarEvent` — class, line 1870
- **called from:**
- `routes/calendar_routes.py:1239`
- `routes/calendar_routes.py:1528`
- `src/caldav_sync.py:437`
- `src/tools/calendar.py:431`
- `tests/test_caldav_bidirectional_sync.py:108`
- `tests/test_caldav_sync_prune_local_events.py:61`
- `tests/test_caldav_sync_prune_local_events.py:67`
- `tests/test_caldav_sync_uid_scope.py:35`
- `tests/test_calendar_default_transaction.py:257`
- `tests/test_calendar_default_transaction.py:515`
- `tests/test_calendar_import_zero_duration.py:134`
- `tests/test_checkin_digest_owner_scope.py:33`
- `tests/test_checkin_digest_owner_scope.py:36`
- `tests/test_checkin_digest_owner_scope.py:62`
- `tests/test_upload_handler_cleanup.py:530`

## `CalendarDeletedEvent` — class, line 1904
- **called from:**
- `routes/calendar_routes.py:189`
- `tests/test_caldav_bidirectional_sync.py:120`

## `Integration` — class, line 1918
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_migrate_email_account_default_invariant` — function, line 1933
- **called from:**
- `core/database.py:2179`
- `tests/test_email_account_default_serialization.py:262`
- `tests/test_email_account_default_serialization.py:263`

## `_migrate_seed_email_account` — function, line 1996
- **called from:**
- `core/database.py:2180`

## `_enable_sqlite_wal` — function, line 2075
- **called from:**
- `core/database.py:2107`

## `init_db` — function, line 2102
- **called from:**
- `core/database.py:2779`

## `_migrate_backfill_task_folders` — function, line 2194
- **called from:**
- `core/database.py:2191`

## `_migrate_chat_messages_fts` — function, line 2220
- **called from:**
- `core/database.py:2187`
- `tests/test_session_search.py:251`

## `_scrub_legacy_chat_message_fts_media` — function, line 2306
- **called from:**
- `core/database.py:2295`

## `_migrate_add_email_smtp_security` — function, line 2337
- **called from:**
- `core/database.py:2178`

## `_migrate_encrypt_endpoint_keys` — function, line 2368
- **called from:**
- `core/database.py:2190`

## `_migrate_encrypt_signatures` — function, line 2392
- **called from:**
- `core/database.py:2189`

## `_migrate_encrypt_email_passwords` — function, line 2424
- **called from:**
- `core/database.py:2188`

## `_migrate_add_calendar_is_utc` — function, line 2458
- **called from:**
- `core/database.py:2182`

## `_migrate_add_calendar_origin` — function, line 2484
- **called from:**
- `core/database.py:2183`

## `_migrate_add_calendar_account_id` — function, line 2511
- **called from:**
- `core/database.py:2184`

## `_migrate_add_caldav_sync_columns` — function, line 2537
- **called from:**
- `core/database.py:2185`

## `_migrate_add_calendar_metadata` — function, line 2562
- **called from:**
- `core/database.py:2181`

## `_migrate_add_calendar_recurrence_exdates` — function, line 2589
- **called from:**
- `core/database.py:2186`

## `get_db` — function, line 2610
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_db_session` — function, line 2625
- decorator: `contextmanager`
- **called from:**
- `companion/pairing.py:195`
- `core/auth.py:308`
- `core/database.py:2639`
- `core/database.py:2657`
- `core/database.py:2670`
- `core/database.py:2700`
- `core/database.py:2715`
- `core/database.py:2728`
- `core/database.py:2737`
- `core/database.py:2749`
- `core/database.py:2768`
- `routes/api_token_routes.py:82`
- `routes/api_token_routes.py:134`
- `routes/api_token_routes.py:165`
- `routes/api_token_routes.py:199`

## `bulk_insert_messages` — function, line 2637
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_old_sessions` — function, line 2653
- **called from:**
- `src/cleanup_service.py:289`

## `get_session_stats` — function, line 2668
- **called from:**
- `core/database.py:2682`

## `get_detailed_stats` — function, line 2680
- **called from:**
- `routes/diagnostics_routes.py:61`

## `update_session_last_accessed` — function, line 2698
- **called from:**
- `routes/chat_helpers.py:1298`
- `routes/chat_helpers.py:1315`
- `routes/chat_routes.py:1097`
- `src/chat_handler.py:358`

## `get_session_mode` — function, line 2708
- **called from:**
- `routes/chat_routes.py:1511`
- `tests/test_session_mode_helpers.py:74`
- `tests/test_session_mode_helpers.py:81`

## `set_session_mode` — function, line 2721
- **called from:**
- `routes/chat_routes.py:1810`
- `routes/chat_routes.py:1874`
- `tests/test_session_mode_helpers.py:55`
- `tests/test_session_mode_helpers.py:65`

## `get_session_by_id` — function, line 2735
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_upcoming_events` — function, line 2740
- **called from:**
- `routes/email_pollers.py:884`

## `archive_session` — function, line 2766
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
