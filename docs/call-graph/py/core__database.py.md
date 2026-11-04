# `core/database.py` — definitions & call sites

106 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `utcnow_naive` — function, line 23
- **called from:**
- `core/database.py:878`
- `core/database.py:2067`
- `core/database.py:2686`
- `core/database.py:2697`
- `core/database.py:2744`
- `core/database.py:2789`
- `core/session_manager.py:1138`
- `core/session_manager.py:1332`
- `core/session_manager.py:1333`
- `routes/chatgpt_subscription_routes.py:58`
- `routes/session_routes.py:228`
- `routes/session_routes.py:297`
- `routes/session_routes.py:550`
- `routes/session_routes.py:597`
- `routes/session_routes.py:924`
- `routes/session_routes.py:958`
- `routes/session_routes.py:1161`
- `routes/session_routes.py:1264`
- `routes/session_routes.py:1324`
- `routes/session_routes.py:1369`
- `routes/session_routes.py:1543`
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
- `core/database.py:2126`
- `core/database.py:2155`
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
- `core/session_manager.py:189`
- `core/session_manager.py:295`
- `core/session_manager.py:1056`
- `tests/test_api_token_tool_authority.py:24`
- `tests/test_api_token_tool_authority.py:97`
- `tests/test_draft_promotion_keeps_live_media.py:37`
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

## `Session.is_active` — method, line 249
- decorator: `property`
- **called from:**
- `routes/chat_routes.py:3115`
- `routes/session_routes.py:132`
- `src/agent_jobs.py:295`
- `src/bg_monitor.py:115`

## `Session.to_dict` — method, line 253
- **called from:**
- `core/models.py:175`
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

## `ChatMessage` — class, line 275
- **called from:**
- `core/session_manager.py:258`
- `core/session_manager.py:278`
- `routes/chat_helpers.py:470`
- `routes/chat_helpers.py:1309`
- `routes/chat_helpers.py:1312`
- `routes/chat_routes.py:316`
- `routes/chat_routes.py:319`
- `routes/chat_routes.py:1094`
- `routes/chat_routes.py:1904`
- `routes/chat_routes.py:2200`
- `routes/chat_routes.py:3129`
- `routes/history/history_routes.py:258`
- `routes/history/history_routes.py:481`
- `routes/history/history_routes.py:910`
- `routes/history/history_routes.py:1147`
- `routes/history/history_routes.py:1153`
- `routes/research/research_routes.py:770`
- `routes/session_routes.py:713`
- `routes/session_routes.py:1258`
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
- `tests/test_draft_promotion_keeps_live_media.py:47`
- `tests/test_draft_promotion_keeps_live_media.py:83`
- `tests/test_draft_promotion_keeps_live_media.py:120`
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
- … +66 more (grep the name in repo)

## `Document` — class, line 304
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

## `DocumentVersion` — class, line 337
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

## `GalleryAlbum` — class, line 352
- **called from:**
- `routes/gallery/gallery_routes.py:860`
- `tests/test_admin_wipe_gallery.py:18`
- `tests/test_gallery_null_user_routes.py:28`
- `tests/test_gallery_null_user_routes.py:29`

## `GalleryImage` — class, line 365
- **called from:**
- `mcp_servers/image_gen_server.py:143`
- `routes/gallery/gallery_routes.py:408`
- `routes/upload_routes.py:236`
- `src/ai_interaction.py:1115`
- `src/ai_interaction.py:1262`
- `src/ai_interaction.py:1532`
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

## `EmailAccount` — class, line 407
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

## `EmailAccountOwnerLock` — class, line 454
- **called from:**
- `core/database.py:524`

## `lock_email_account_owner_mutations` — function, line 495
- **called from:**
- `core/database.py:2062`
- `routes/auth_routes.py:388`
- `routes/email_routes.py:203`
- `scripts/demo_email/demo_account.py:65`
- `tests/test_email_account_default_serialization.py:358`

## `ModelEndpoint` — class, line 541
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

## `ProviderAuthSession` — class, line 577
- **called from:**
- `routes/chatgpt_subscription_routes.py:46`
- `tests/test_chatgpt_subscription_routes.py:92`

## `McpServer` — class, line 591
- **called from:**
- `routes/mcp/mcp_routes.py:240`
- `src/agent_tools/admin_tools.py:266`

## `Comparison` — class, line 608
- **called from:**
- `routes/compare/compare_routes.py:203`
- `routes/compare/compare_routes.py:300`

## `Signature` — class, line 634
- **called from:**
- `routes/signature_routes.py:108`

## `ApiToken` — class, line 655
- **called from:**
- `companion/pairing.py:196`
- `routes/api_token_routes.py:135`
- `src/agent_tools/admin_tools.py:469`

## `Webhook` — class, line 669
- **called from:**
- `routes/webhook/webhook_routes.py:127`
- `src/agent_tools/admin_tools.py:406`
- `static/js/settings.js:2373`
- `static/js/settings.js:2415`

## `UserTool` — class, line 684
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `UserToolData` — class, line 709
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CrewMember` — class, line 727
- **called from:**
- `src/task_scheduler.py:2620`

## `ScheduledTask` — class, line 751
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

## `EditorDraft` — class, line 799
- **called from:**
- `routes/editor_draft_routes.py:116`

## `TaskRun` — class, line 831
- **called from:**
- `src/task_scheduler.py:749`
- `src/task_scheduler.py:882`
- `tests/test_task_cookbook_admin_gate.py:270`

## `Memory` — class, line 854
- **called from:**
- `services/memory/service.py:54`
- `services/memory/service.py:67`
- `static/js/tasks.js:444`

## `_migrate_add_last_message_at_column` — function, line 889
- **called from:**
- `core/database.py:2195`

## `_migrate_add_deleted_at_column` — function, line 934
- **called from:**
- `core/database.py:2199`

## `_migrate_add_document_archived_column` — function, line 965
- **called from:**
- `core/database.py:2194`

## `_migrate_add_owner_column` — function, line 989
- **called from:**
- `core/database.py:2193`

## `_migrate_model_endpoints` — function, line 1013
- **called from:**
- `core/database.py:2146`

## `_migrate_add_hidden_models_column` — function, line 1036
- **called from:**
- `core/database.py:2183`

## `_migrate_add_model_endpoint_owner_column` — function, line 1059
- **called from:**
- `core/database.py:2189`

## `_migrate_add_provider_auth_id_column` — function, line 1091
- **called from:**
- `core/database.py:2190`

## `_migrate_add_model_type_column` — function, line 1116
- **called from:**
- `core/database.py:2187`

## `_migrate_add_model_endpoint_refresh_columns` — function, line 1139
- **called from:**
- `core/database.py:2188`

## `_migrate_add_task_run_model_column` — function, line 1167
- **called from:**
- `core/database.py:2192`

## `_migrate_add_supports_tools_column` — function, line 1190
- **called from:**
- `core/database.py:2191`

## `_migrate_add_cached_models_column` — function, line 1214
- **called from:**
- `core/database.py:2184`

## `_migrate_add_pinned_models_column` — function, line 1236
- **called from:**
- `core/database.py:2185`

## `_migrate_add_notes_sort_order` — function, line 1259
- **called from:**
- `core/database.py:2186`

## `_migrate_add_mode_column` — function, line 1291
- **called from:**
- `core/database.py:2198`

## `_migrate_add_folder_column` — function, line 1314
- **called from:**
- `core/database.py:2196`

## `_migrate_add_token_columns` — function, line 1337
- **called from:**
- `core/database.py:2197`

## `_migrate_add_owner_to_table` — function, line 1361
- **called from:**
- `core/database.py:1387`
- `core/database.py:1388`
- `core/database.py:1389`
- `core/database.py:1390`
- `core/database.py:1391`
- `core/database.py:1394`

## `_migrate_add_multiuser_owner_columns` — function, line 1385
- **called from:**
- `core/database.py:2200`

## `_migrate_add_gallery_caption_column` — function, line 1397
- **called from:**
- `core/database.py:2201`

## `_migrate_add_api_token_scopes_column` — function, line 1420
- **called from:**
- `core/database.py:2202`

## `_migrate_assign_legacy_owner` — function, line 1448
- **called from:**
- `core/database.py:2204`
- `tests/test_foreground_model_routing.py:2063`

## `_migrate_backfill_document_owner_from_session` — function, line 1572
- **called from:**
- `core/database.py:2203`

## `_migrate_add_tidy_verdict` — function, line 1599
- **called from:**
- `core/database.py:2205`

## `_migrate_add_doc_source_email_cols` — function, line 1612
- **called from:**
- `core/database.py:2206`

## `_migrate_add_task_automation_columns` — function, line 1636
- **called from:**
- `core/database.py:2209`

## `_migrate_add_email_oauth_columns` — function, line 1709
- **called from:**
- `core/database.py:2208`

## `_migrate_add_oauth_config` — function, line 1728
- **called from:**
- `core/database.py:2207`

## `_migrate_add_disabled_tools` — function, line 1740
- **called from:**
- `core/database.py:2210`

## `_migrate_add_mcp_oauth_tokens_column` — function, line 1752
- **called from:**
- `core/database.py:2211`

## `_migrate_add_task_v2_columns` — function, line 1769
- **called from:**
- `core/database.py:2212`

## `_migrate_drop_ping_notes_tasks` — function, line 1789
- **called from:**
- `core/database.py:2214`

## `_migrate_add_notifications_enabled` — function, line 1810
- **called from:**
- `core/database.py:2213`

## `_migrate_add_crew_member_id` — function, line 1823
- **called from:**
- `core/database.py:2215`

## `_migrate_add_assistant_columns` — function, line 1840
- **called from:**
- `core/database.py:2216`

## `Note` — class, line 1860
- **called from:**
- `routes/note/note_routes.py:663`
- `src/tools/calendar.py:183`
- `src/tools/notes.py:215`
- `tests/test_notes_fail_closed_auth.py:113`
- `tests/test_notes_fail_closed_auth.py:115`
- `tests/test_notes_fail_closed_auth.py:181`
- `tests/test_upload_handler_cleanup.py:517`
- `static/js/slashCommands.js:1715`

## `CalendarCal` — class, line 1890
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

## `CalendarEvent` — class, line 1908
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

## `CalendarDeletedEvent` — class, line 1942
- **called from:**
- `routes/calendar_routes.py:189`
- `tests/test_caldav_bidirectional_sync.py:120`

## `Integration` — class, line 1956
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_migrate_email_account_default_invariant` — function, line 1971
- **called from:**
- `core/database.py:2218`
- `tests/test_email_account_default_serialization.py:262`
- `tests/test_email_account_default_serialization.py:263`

## `_migrate_seed_email_account` — function, line 2034
- **called from:**
- `core/database.py:2219`

## `_enable_sqlite_wal` — function, line 2113
- **called from:**
- `core/database.py:2145`

## `init_db` — function, line 2140
- **called from:**
- `core/database.py:2820`

## `_migrate_backfill_task_folders` — function, line 2233
- **called from:**
- `core/database.py:2230`

## `_migrate_chat_messages_fts` — function, line 2259
- **called from:**
- `core/database.py:2226`
- `tests/test_session_search.py:251`

## `_scrub_legacy_chat_message_fts_media` — function, line 2345
- **called from:**
- `core/database.py:2334`

## `_migrate_add_email_smtp_security` — function, line 2376
- **called from:**
- `core/database.py:2217`

## `_migrate_encrypt_endpoint_keys` — function, line 2407
- **called from:**
- `core/database.py:2229`

## `_migrate_encrypt_signatures` — function, line 2431
- **called from:**
- `core/database.py:2228`

## `_migrate_encrypt_email_passwords` — function, line 2463
- **called from:**
- `core/database.py:2227`

## `_migrate_add_calendar_is_utc` — function, line 2497
- **called from:**
- `core/database.py:2221`

## `_migrate_add_calendar_origin` — function, line 2523
- **called from:**
- `core/database.py:2222`

## `_migrate_add_calendar_account_id` — function, line 2550
- **called from:**
- `core/database.py:2223`

## `_migrate_add_caldav_sync_columns` — function, line 2576
- **called from:**
- `core/database.py:2224`

## `_migrate_add_calendar_metadata` — function, line 2601
- **called from:**
- `core/database.py:2220`

## `_migrate_add_calendar_recurrence_exdates` — function, line 2628
- **called from:**
- `core/database.py:2225`

## `get_db` — function, line 2649
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_db_session` — function, line 2664
- decorator: `contextmanager`
- **called from:**
- `companion/pairing.py:195`
- `core/auth.py:308`
- `core/database.py:2678`
- `core/database.py:2696`
- `core/database.py:2711`
- `core/database.py:2741`
- `core/database.py:2756`
- `core/database.py:2769`
- `core/database.py:2778`
- `core/database.py:2790`
- `core/database.py:2809`
- `routes/api_token_routes.py:82`
- `routes/api_token_routes.py:134`
- `routes/api_token_routes.py:165`
- `routes/api_token_routes.py:199`

## `bulk_insert_messages` — function, line 2676
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_old_sessions` — function, line 2692
- **called from:**
- `src/cleanup_service.py:289`

## `get_session_stats` — function, line 2709
- **called from:**
- `core/database.py:2723`

## `get_detailed_stats` — function, line 2721
- **called from:**
- `routes/diagnostics_routes.py:61`

## `update_session_last_accessed` — function, line 2739
- **called from:**
- `routes/chat_helpers.py:1298`
- `routes/chat_helpers.py:1315`
- `routes/chat_routes.py:1097`
- `src/chat_handler.py:358`

## `get_session_mode` — function, line 2749
- **called from:**
- `routes/chat_routes.py:1511`
- `tests/test_session_mode_helpers.py:74`
- `tests/test_session_mode_helpers.py:81`

## `set_session_mode` — function, line 2762
- **called from:**
- `routes/chat_routes.py:1810`
- `routes/chat_routes.py:1874`
- `tests/test_session_mode_helpers.py:55`
- `tests/test_session_mode_helpers.py:65`

## `get_session_by_id` — function, line 2776
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_upcoming_events` — function, line 2781
- **called from:**
- `routes/email_pollers.py:884`

## `archive_session` — function, line 2807
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
