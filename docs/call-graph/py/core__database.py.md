# `core/database.py` — definitions & call sites

120 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `utcnow_naive` — function, line 23
- **called from:**
- `core/database.py:930`
- `core/database.py:2326`
- `core/database.py:3002`
- `core/database.py:3013`
- `core/database.py:3058`
- `core/database.py:3103`
- `core/session_manager.py:1135`
- `core/session_manager.py:1136`
- `routes/chatgpt_subscription_routes.py:159`
- `routes/session_routes.py:341`
- `routes/session_routes.py:434`
- `routes/session_routes.py:717`
- `routes/session_routes.py:729`
- `routes/session_routes.py:791`
- `routes/session_routes.py:1069`
- `routes/session_routes.py:1103`
- `routes/session_routes.py:1307`
- `routes/session_routes.py:1418`
- `routes/session_routes.py:1473`
- `routes/session_routes.py:1675`
- `src/background_tool_jobs.py:176`
- `src/chatgpt_subscription.py:433`
- `tests/test_database_utcnow.py:13`
- `tests/test_database_utcnow.py:16`
- `tests/test_session_actions_cleanup.py:76`
- `tests/test_session_actions_cleanup.py:79`
- `tests/test_session_actions_cleanup.py:80`
- `tests/test_session_actions_cleanup.py:112`
- `tests/test_session_actions_cleanup.py:115`
- `tests/test_session_actions_cleanup.py:135`
- `tests/test_session_list_owner_scope.py:244`

## `TimestampMixin` — class, line 28
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TimestampMixin.created_at` — method, line 31
- decorator: `declared_attr`
- **called from:**
- `static/js/gallery.js:1591`

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
- `core/database.py:2394`
- `core/database.py:2423`
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
- `core/session_manager.py:289`
- `core/session_manager.py:953`
- `tests/test_api_token_tool_authority.py:387`
- `tests/test_api_token_tool_authority.py:460`
- `tests/test_background_tool_jobs.py:18`
- `tests/test_background_tool_jobs.py:93`
- `tests/test_caldav_redirect_hardening.py:103`
- `tests/test_chat_document_owner_context.py:60`
- `tests/test_chat_document_owner_context.py:62`
- `tests/test_chat_image_preservation.py:21`
- `tests/test_chat_image_preservation.py:49`
- `tests/test_chat_image_preservation.py:50`
- `tests/test_chat_tidy_content_preservation.py:61`
- `tests/test_chat_tidy_content_preservation.py:91`
- `tests/test_chat_tidy_content_preservation.py:121`
- `tests/test_clean_v3_route_ownership.py:90`
- `tests/test_cleanup_transcript_preservation.py:38`
- `tests/test_cleanup_transcript_preservation.py:43`
- `tests/test_cleanup_transcript_preservation.py:168`
- `tests/test_cleanup_transcript_preservation.py:173`
- `tests/test_cleanup_transcript_preservation.py:179`
- `tests/test_cleanup_transcript_preservation.py:235`
- `tests/test_cleanup_transcript_preservation.py:320`
- `tests/test_cleanup_transcript_preservation.py:325`
- `tests/test_cleanup_transcript_preservation.py:331`
- `tests/test_external_context_tool_gate.py:290`
- `tests/test_history_display_model_hydration.py:249`
- `tests/test_history_display_model_hydration.py:330`
- `tests/test_interrupted_thinking_context.py:5`
- `tests/test_minimal_native_tool_prompt.py:1402`
- `tests/test_owned_resource_identity.py:67`
- `tests/test_pinned_model_route_selection.py:42`
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
- … +5 more (grep the name in repo)

## `Session.is_active` — method, line 257
- decorator: `property`
- **called from:**
- `app.py:1225`
- `routes/chat_routes.py:5604`
- `routes/session_routes.py:242`
- `src/agent_jobs.py:295`
- `src/bg_monitor.py:161`

## `Session.to_dict` — method, line 261
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5643`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31336`
- `src/agent_loop.py:31809`
- `src/agent_loop.py:32074`
- `src/agent_loop.py:32114`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32198`
- `src/agent_loop.py:32326`
- `src/agent_loop.py:32658`
- `src/agent_loop.py:34878`
- `src/agent_loop.py:36887`
- `src/agent_loop.py:37210`
- `src/agent_loop.py:37423`
- `src/agent_loop.py:37478`
- `src/agent_loop.py:37535`
- `src/agent_loop.py:37869`
- `src/agent_loop.py:37881`
- `src/agent_loop.py:37987`
- `src/agent_loop.py:38909`
- `src/agent_loop.py:38910`
- `src/agent_loop.py:38915`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:681`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `src/agent_runtime/completion.py:392`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:154`
- `src/agent_runtime/context_resolution.py:155`
- `src/agent_runtime/context_resolution.py:502`
- `src/agent_runtime/context_resolution.py:518`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_log.py:263`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- … +146 more (grep the name in repo)

## `ChatMessage` — class, line 289
- **called from:**
- `core/session_manager.py:252`
- `core/session_manager.py:272`
- `routes/chat_helpers.py:952`
- `routes/chat_helpers.py:1964`
- `routes/chat_helpers.py:1967`
- `routes/chat_routes.py:1512`
- `routes/chat_routes.py:1515`
- `routes/chat_routes.py:2625`
- `routes/chat_routes.py:4194`
- `routes/chat_routes.py:4495`
- `routes/chat_routes.py:5623`
- `routes/history/history_routes.py:403`
- `routes/history/history_routes.py:674`
- `routes/history/history_routes.py:1127`
- `routes/history/history_routes.py:1554`
- `routes/history/history_routes.py:1560`
- `routes/research/research_routes.py:882`
- `routes/session_routes.py:907`
- `routes/session_routes.py:1412`
- `routes/webhook/webhook_routes.py:377`
- `routes/webhook/webhook_routes.py:385`
- `src/agent_jobs.py:326`
- `src/agent_tools/session_tools.py:250`
- `src/agent_tools/session_tools.py:251`
- `src/background_tool_jobs.py:179`
- `src/bg_monitor.py:199`
- `src/chat_handler.py:367`
- `src/chat_handler.py:369`
- `src/context_compactor.py:983`
- `src/task_scheduler.py:1935`
- `src/task_scheduler.py:1943`
- `tests/test_api_token_tool_authority.py:408`
- `tests/test_api_token_tool_authority.py:413`
- `tests/test_api_token_tool_authority.py:436`
- `tests/test_api_token_tool_authority.py:437`
- `tests/test_api_token_tool_authority.py:466`
- `tests/test_api_token_tool_authority.py:467`
- `tests/test_api_token_tool_authority.py:498`
- `tests/test_api_token_tool_authority.py:499`
- `tests/test_api_token_tool_authority.py:677`
- `tests/test_api_token_tool_authority.py:678`
- `tests/test_background_tool_jobs.py:94`
- `tests/test_background_tool_jobs.py:94`
- `tests/test_chat_image_preservation.py:22`
- `tests/test_chat_image_preservation.py:53`
- `tests/test_chat_tidy_content_preservation.py:68`
- `tests/test_chat_tidy_content_preservation.py:70`
- `tests/test_chat_tidy_content_preservation.py:101`
- `tests/test_chat_tidy_content_preservation.py:125`
- `tests/test_chatgpt_session_binding.py:50`
- `tests/test_cleanup_transcript_preservation.py:50`
- `tests/test_cleanup_transcript_preservation.py:186`
- `tests/test_cleanup_transcript_preservation.py:190`
- `tests/test_cleanup_transcript_preservation.py:241`
- `tests/test_cleanup_transcript_preservation.py:338`
- `tests/test_cleanup_transcript_preservation.py:342`
- `tests/test_database_test_isolation.py:45`
- `tests/test_database_test_isolation.py:46`
- `tests/test_fork_session_metadata.py:65`
- `tests/test_fork_session_metadata.py:66`
- … +95 more (grep the name in repo)

## `BackgroundToolJob` — class, line 318
- **called from:**
- `src/background_tool_jobs.py:50`

## `Document` — class, line 334
- **called from:**
- `mcp_servers/email_server.py:2883`
- `routes/document/document_routes.py:185`
- `scripts/eval_odysseus_everyday_live_hard.py:229`
- `scripts/eval_odysseus_live_hard_examples.py:237`
- `scripts/eval_odysseus_tool_use.py:296`
- `scripts/odysseus_domain_audit.py:324`
- `scripts/run_sft_environment_expansion.py:132`
- `scripts/run_sft_environment_expansion.py:602`
- `src/agent_tools/document_tools.py:474`
- `src/agent_tools/document_tools.py:590`
- `src/email_attachment_text.py:30`
- `src/office_doc.py:50`
- `src/pdf_form_doc.py:233`
- `src/pdf_form_doc.py:416`
- `tests/cli/test_docs_cli_search.py:34`
- `tests/cli/test_docs_cli_search.py:39`
- `tests/cli/test_docs_cli_search.py:44`
- `tests/cli/test_docs_cli_search.py:49`
- `tests/test_auth_disabled_document_access.py:81`
- `tests/test_auth_disabled_document_access.py:266`
- `tests/test_chat_document_owner_context.py:98`
- `tests/test_document_close_clears_active_route.py:63`
- `tests/test_document_export_zip_filenames.py:33`
- `tests/test_document_followup_integrity.py:25`
- `tests/test_document_followup_integrity.py:27`
- `tests/test_document_library_literal_search.py:41`
- `tests/test_document_library_literal_search.py:65`
- `tests/test_document_read_pagination.py:24`
- `tests/test_document_render_pdf_iframe.py:165`
- `tests/test_document_session_owner_scope.py:63`
- `tests/test_document_session_owner_scope.py:73`
- `tests/test_document_session_owner_scope.py:83`
- `tests/test_document_tidy_null_timestamp.py:37`
- `tests/test_document_tidy_null_timestamp.py:39`
- `tests/test_markitdown_runtime.py:67`
- `tests/test_owned_resource_identity.py:69`
- `tests/test_owned_resource_identity.py:92`
- `tests/test_owned_resource_identity.py:348`
- `tests/test_upload_handler_cleanup.py:495`
- `tests/test_upload_handler_cleanup.py:670`
- `tests/tools/editor_writing_smoke.py:87`
- `static/js/document.js:15977`

## `DocumentVersion` — class, line 367
- **called from:**
- `mcp_servers/email_server.py:2851`
- `mcp_servers/email_server.py:2897`
- `routes/document/document_routes.py:170`
- `routes/document/document_routes.py:198`
- `routes/document/document_routes.py:761`
- `routes/document/document_routes.py:898`
- `routes/document/document_routes.py:1053`
- `scripts/eval_odysseus_tool_use.py:308`
- `scripts/odysseus_domain_audit.py:327`
- `scripts/run_sft_environment_expansion.py:137`
- `scripts/run_sft_environment_expansion.py:613`
- `src/agent_tools/document_tools.py:484`
- `src/agent_tools/document_tools.py:600`
- `src/agent_tools/document_tools.py:696`
- `src/agent_tools/document_tools.py:850`
- `src/agent_tools/document_tools.py:954`
- `src/office_doc.py:60`
- `src/pdf_form_doc.py:243`
- `src/pdf_form_doc.py:426`
- `tests/test_upload_handler_cleanup.py:502`

## `GalleryAlbum` — class, line 382
- **called from:**
- `routes/gallery/gallery_routes.py:1370`
- `tests/cli/test_gallery_cli_tag_filters.py:18`
- `tests/test_admin_wipe_gallery.py:18`
- `tests/test_gallery_null_user_routes.py:28`
- `tests/test_gallery_null_user_routes.py:29`

## `GalleryImage` — class, line 395
- **called from:**
- `mcp_servers/image_gen_server.py:144`
- `routes/gallery/gallery_routes.py:914`
- `routes/upload_routes.py:317`
- `src/agent_tools/editor_tools.py:161`
- `src/ai_interaction.py:1477`
- `src/ai_interaction.py:1648`
- `src/ai_interaction.py:1980`
- `src/tools/image.py:75`
- `src/tools/image.py:209`
- `tests/cli/test_gallery_cli_tag_filters.py:27`
- `tests/test_admin_wipe_gallery.py:19`
- `tests/test_chat_image_preservation.py:23`
- `tests/test_chat_image_preservation.py:52`
- `tests/test_gallery_delete_file_ordering.py:34`
- `tests/test_gallery_filename_confinement.py:101`
- `tests/test_gallery_null_user_routes.py:30`
- `tests/test_gallery_null_user_routes.py:42`
- `tests/test_gallery_owner_filter_single_user.py:30`
- `tests/test_gallery_search_multiword.py:35`
- `tests/test_gallery_search_multiword.py:45`
- `tests/test_gallery_search_multiword.py:55`
- `tests/test_gallery_search_multiword.py:65`
- `tests/test_session_image_cleanup.py:31`
- `tests/test_session_image_cleanup.py:41`
- `tests/test_upload_handler_cleanup.py:134`
- `tests/test_upload_handler_cleanup.py:508`

## `EmailAccount` — class, line 437
- **called from:**
- `routes/email/email_routes.py:7326`
- `routes/email/email_routes.py:7450`
- `scripts/demo_email/demo_account.py:107`
- `tests/test_email_account_default_serialization.py:69`
- `tests/test_email_account_default_serialization.py:498`
- `tests/test_email_account_default_serialization.py:505`
- `tests/test_email_account_host_ssrf.py:238`
- `tests/test_email_account_host_ssrf.py:324`
- `tests/test_email_oauth.py:171`
- `tests/test_email_ownerless_account_owner_scope.py:32`
- `tests/test_email_test_connection_oauth.py:34`

## `EmailAccountOwnerLock` — class, line 484
- **called from:**
- `core/database.py:554`

## `lock_email_account_owner_mutations` — function, line 525
- **called from:**
- `core/database.py:2321`
- `routes/auth_routes.py:438`
- `routes/email/email_routes.py:245`
- `scripts/demo_email/demo_account.py:65`
- `tests/test_email_account_default_serialization.py:358`

## `ModelEndpoint` — class, line 571
- **called from:**
- `routes/chatgpt_subscription_routes.py:177`
- `routes/cookbook_routes.py:1466`
- `routes/cookbook_routes.py:1823`
- `routes/copilot_routes.py:70`
- `routes/model_routes.py:2342`
- `src/agent_tools/admin_tools.py:62`
- `tests/test_chat_document_owner_context.py:64`
- `tests/test_chat_helpers.py:512`
- `tests/test_chat_helpers.py:566`
- `tests/test_chat_helpers.py:603`
- `tests/test_chatgpt_session_binding.py:28`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:41`
- `tests/test_chatgpt_subscription_routes.py:221`
- `tests/test_chatgpt_subscription_routes.py:266`
- `tests/test_chatgpt_subscription_routes.py:343`
- `tests/test_chatgpt_subscription_usage.py:327`
- `tests/test_cookbook_endpoint_registration.py:121`
- `tests/test_cookbook_endpoint_registration.py:505`
- `tests/test_cookbook_serve_lifecycle.py:124`
- `tests/test_default_chat_model_filter.py:37`
- `tests/test_editor_planner_ssrf_authorization.py:135`
- `tests/test_editor_planner_ssrf_authorization.py:159`
- `tests/test_editor_planner_ssrf_authorization.py:188`
- `tests/test_editor_planner_ssrf_authorization.py:217`
- `tests/test_editor_planner_ssrf_authorization.py:225`
- `tests/test_editor_planner_ssrf_authorization.py:256`
- `tests/test_editor_planner_ssrf_authorization.py:281`
- `tests/test_editor_planner_ssrf_authorization.py:345`
- `tests/test_editor_planner_ssrf_authorization.py:403`
- `tests/test_editor_planner_ssrf_authorization.py:411`
- `tests/test_endpoint_registered_authority.py:90`
- `tests/test_endpoint_registered_authority.py:176`
- `tests/test_gallery_endpoint_enforcement.py:72`
- `tests/test_gallery_endpoint_enforcement.py:113`
- `tests/test_gallery_endpoint_enforcement.py:154`
- `tests/test_gallery_endpoint_enforcement.py:196`
- `tests/test_gallery_endpoint_enforcement.py:242`
- `tests/test_gallery_endpoint_enforcement.py:315`
- `tests/test_gallery_endpoint_enforcement.py:358`
- `tests/test_gallery_endpoint_enforcement.py:399`
- `tests/test_gallery_endpoint_enforcement.py:430`
- `tests/test_headless_completion_consumers.py:25`
- `tests/test_pinned_model_route_selection.py:28`
- `tests/test_request_authority.py:550`
- `tests/test_resolve_session_auth_chatgpt.py:36`
- `tests/test_resolve_session_auth_chatgpt.py:88`
- `tests/test_resolve_session_auth_chatgpt.py:130`
- `tests/test_resolve_session_auth_chatgpt.py:176`
- `tests/test_resolve_session_auth_chatgpt.py:180`
- `tests/test_resolve_session_auth_chatgpt.py:269`
- `tests/test_review_endpoint_credentials.py:63`
- `tests/test_task_scheduler_endpoint_authority.py:89`
- `tests/test_task_scheduler_endpoint_authority.py:101`
- `tests/test_task_scheduler_endpoint_authority.py:118`
- `tests/test_task_scheduler_endpoint_authority.py:135`
- `tests/test_task_scheduler_endpoint_authority.py:156`
- `tests/test_task_scheduler_endpoint_authority.py:181`
- `tests/test_task_scheduler_endpoint_authority.py:230`
- `tests/test_task_scheduler_endpoint_authority.py:242`
- `tests/test_utility_reasoning_effort.py:328`
- … +5 more (grep the name in repo)

## `ProviderAuthSession` — class, line 611
- **called from:**
- `routes/chatgpt_subscription_routes.py:147`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:37`
- `tests/test_chatgpt_subscription_routes.py:216`
- `tests/test_chatgpt_subscription_routes.py:260`
- `tests/test_chatgpt_subscription_usage.py:28`
- `tests/test_chatgpt_subscription_usage.py:325`

## `McpServer` — class, line 625
- **called from:**
- `routes/mcp/mcp_routes.py:260`
- `src/agent_tools/admin_tools.py:280`
- `tests/test_admin_listing_authorization.py:64`
- `tests/test_mcp_oauth.py:363`
- `tests/test_mcp_oauth.py:414`

## `Comparison` — class, line 642
- **called from:**
- `routes/compare/compare_routes.py:203`
- `routes/compare/compare_routes.py:300`

## `Signature` — class, line 668
- **called from:**
- `routes/signature_routes.py:108`

## `ApiToken` — class, line 689
- **called from:**
- `companion/pairing.py:196`
- `routes/api_token_routes.py:135`
- `src/agent_tools/admin_tools.py:483`

## `Webhook` — class, line 703
- **called from:**
- `routes/webhook/webhook_routes.py:127`
- `src/agent_tools/admin_tools.py:420`
- `static/js/settings.js:2086`
- `static/js/settings.js:2128`

## `UserTool` — class, line 718
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `UserToolData` — class, line 743
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CrewMember` — class, line 761
- **called from:**
- `src/task_scheduler.py:2853`
- `tests/test_endpoint_registered_authority.py:100`

## `ScheduledTask` — class, line 785
- **called from:**
- `routes/task/task_routes.py:540`
- `scripts/eval_odysseus_tool_use.py:318`
- `scripts/odysseus_domain_audit.py:330`
- `scripts/run_sft_environment_expansion.py:143`
- `src/task_scheduler.py:2708`
- `src/tools/system.py:514`
- `tests/test_endpoint_registered_authority.py:95`
- `tests/test_manage_tasks_admin_action_policy.py:65`
- `tests/test_manage_tasks_owner_scope.py:44`
- `tests/test_request_authority.py:402`
- `tests/test_scheduler_restart_doublefire.py:148`
- `tests/test_scheduler_restart_doublefire.py:179`
- `tests/test_scheduler_restart_doublefire.py:202`
- `tests/test_task_chain_owner_scope.py:48`
- `tests/test_task_cookbook_admin_gate.py:124`
- `tests/test_task_scheduler_cancel.py:61`
- `tests/test_task_scheduler_cancel.py:128`
- `tests/test_task_scheduler_cancel.py:193`
- `static/js/cookbookServe.js:1859`

## `EditorDraft` — class, line 834
- **called from:**
- `routes/editor_draft_routes.py:169`

## `TaskRun` — class, line 866
- **called from:**
- `src/task_scheduler.py:893`
- `src/task_scheduler.py:1028`
- `tests/test_task_cookbook_admin_gate.py:270`
- `tests/test_task_scheduler_cancel.py:132`

## `NotificationLog` — class, line 889
- **called from:**
- `routes/task/task_routes.py:624`
- `src/task_scheduler.py:550`

## `Memory` — class, line 906
- **called from:**
- `scripts/run_sft_environment_expansion.py:123`
- `services/memory/service.py:54`
- `services/memory/service.py:67`
- `static/js/tasks.js:451`

## `_migrate_add_last_message_at_column` — function, line 941
- **called from:**
- `core/database.py:2465`

## `_migrate_add_memory_extraction_enabled_column` — function, line 986
- **called from:**
- `core/database.py:2466`

## `_migrate_add_skill_injection_enabled_column` — function, line 1008
- **called from:**
- `core/database.py:2468`

## `_migrate_add_memory_injection_enabled_column` — function, line 1030
- **called from:**
- `core/database.py:2467`

## `_migrate_add_session_generation_settings_columns` — function, line 1052
- **called from:**
- `core/database.py:2469`

## `_migrate_add_document_archived_column` — function, line 1076
- **called from:**
- `core/database.py:2464`

## `_migrate_add_owner_column` — function, line 1100
- **called from:**
- `core/database.py:2463`

## `_migrate_model_endpoints` — function, line 1124
- **called from:**
- `core/database.py:2414`

## `_migrate_add_hidden_models_column` — function, line 1147
- **called from:**
- `core/database.py:2451`

## `_migrate_add_model_endpoint_owner_column` — function, line 1170
- **called from:**
- `core/database.py:2458`

## `_migrate_add_provider_auth_id_column` — function, line 1202
- **called from:**
- `core/database.py:2459`

## `_migrate_add_model_type_column` — function, line 1227
- **called from:**
- `core/database.py:2456`

## `_migrate_add_model_endpoint_refresh_columns` — function, line 1250
- **called from:**
- `core/database.py:2457`

## `_migrate_add_task_run_model_column` — function, line 1278
- **called from:**
- `core/database.py:2462`

## `_migrate_add_supports_tools_column` — function, line 1301
- **called from:**
- `core/database.py:2460`

## `_migrate_add_model_tool_modes_column` — function, line 1325
- **called from:**
- `core/database.py:2461`

## `_migrate_add_cached_models_column` — function, line 1349
- **called from:**
- `core/database.py:2452`

## `_migrate_add_pinned_models_column` — function, line 1371
- **called from:**
- `core/database.py:2453`

## `_migrate_add_cookbook_serve_session_id_column` — function, line 1395
- **called from:**
- `core/database.py:2454`
- `tests/test_cookbook_endpoint_registration.py:313`
- `tests/test_cookbook_endpoint_registration.py:314`

## `_migrate_add_notes_sort_order` — function, line 1414
- **called from:**
- `core/database.py:2455`

## `_migrate_add_mode_column` — function, line 1446
- **called from:**
- `core/database.py:2475`

## `_migrate_add_folder_column` — function, line 1469
- **called from:**
- `core/database.py:2470`

## `_migrate_add_session_cwd_column` — function, line 1492
- **called from:**
- `core/database.py:2471`

## `_migrate_add_session_endpoint_id_column` — function, line 1515
- **called from:**
- `core/database.py:2472`
- `tests/test_chatgpt_session_binding.py:155`
- `tests/test_chatgpt_session_binding.py:156`
- `tests/test_chatgpt_session_binding.py:160`

## `_migrate_add_token_columns` — function, line 1528
- **called from:**
- `core/database.py:2473`

## `_migrate_add_total_cost_usd` — function, line 1552
- **called from:**
- `core/database.py:2474`
- `tests/test_cost_tracking.py:207`
- `tests/test_cost_tracking.py:208`

## `_migrate_add_owner_to_table` — function, line 1575
- **called from:**
- `core/database.py:1601`
- `core/database.py:1602`
- `core/database.py:1603`
- `core/database.py:1604`
- `core/database.py:1605`
- `core/database.py:1608`

## `_migrate_add_multiuser_owner_columns` — function, line 1599
- **called from:**
- `core/database.py:2476`

## `_migrate_add_gallery_caption_column` — function, line 1611
- **called from:**
- `core/database.py:2477`

## `_migrate_add_api_token_scopes_column` — function, line 1634
- **called from:**
- `core/database.py:2478`

## `_migrate_assign_legacy_owner` — function, line 1662
- **called from:**
- `core/database.py:2480`
- `tests/test_foreground_model_routing.py:2147`

## `_migrate_backfill_document_owner_from_session` — function, line 1786
- **called from:**
- `core/database.py:2479`

## `_migrate_add_tidy_verdict` — function, line 1813
- **called from:**
- `core/database.py:2481`

## `_migrate_add_doc_source_email_cols` — function, line 1826
- **called from:**
- `core/database.py:2482`

## `_migrate_add_calendar_source_email_cols` — function, line 1851
- **called from:**
- `core/database.py:2483`

## `_migrate_add_task_automation_columns` — function, line 1873
- **called from:**
- `core/database.py:2486`

## `_migrate_add_email_oauth_columns` — function, line 1946
- **called from:**
- `core/database.py:2485`

## `_migrate_add_oauth_config` — function, line 1965
- **called from:**
- `core/database.py:2484`

## `_migrate_add_disabled_tools` — function, line 1977
- **called from:**
- `core/database.py:2488`

## `_migrate_add_mcp_oauth_tokens_column` — function, line 1989
- **called from:**
- `core/database.py:2489`

## `_migrate_add_task_v2_columns` — function, line 2006
- **called from:**
- `core/database.py:2490`

## `_migrate_drop_ping_notes_tasks` — function, line 2026
- **called from:**
- `core/database.py:2492`

## `_migrate_add_notifications_enabled` — function, line 2047
- **called from:**
- `core/database.py:2491`

## `_migrate_add_crew_member_id` — function, line 2060
- **called from:**
- `core/database.py:2493`

## `_migrate_add_assistant_columns` — function, line 2077
- **called from:**
- `core/database.py:2494`

## `Note` — class, line 2097
- **called from:**
- `routes/calendar_routes.py:750`
- `routes/note/note_routes.py:666`
- `scripts/run_sft_environment_expansion.py:115`
- `scripts/run_sft_environment_expansion.py:623`
- `scripts/run_sft_overnight_fixture_flows.py:118`
- `src/tools/calendar.py:324`
- `src/tools/notes.py:389`
- `tests/test_calendar_rrule.py:79`
- `tests/test_calendar_rrule.py:121`
- `tests/test_failed_call_correction.py:26`
- `tests/test_note_ping_delivery_retry.py:45`
- `tests/test_note_ping_delivery_retry.py:116`
- `tests/test_notes_checklist_state.py:20`
- `tests/test_notes_fail_closed_auth.py:113`
- `tests/test_notes_fail_closed_auth.py:115`
- `tests/test_notes_fail_closed_auth.py:181`
- `tests/test_owned_resource_identity.py:72`
- `tests/test_owned_resource_identity.py:73`
- `tests/test_owned_resource_identity.py:74`
- `tests/test_upload_handler_cleanup.py:517`
- `static/js/slashCommands.js:1719`

## `CalendarCal` — class, line 2128
- **called from:**
- `routes/calendar_routes.py:321`
- `routes/calendar_routes.py:1538`
- `routes/calendar_routes.py:1605`
- `scripts/eval_odysseus_app_route_smoke.py:56`
- `scripts/eval_odysseus_everyday_live_hard.py:188`
- `scripts/eval_odysseus_tool_use.py:334`
- `scripts/run_sft_environment_expansion.py:154`
- `scripts/run_sft_environment_expansion.py:163`
- `scripts/run_sft_overnight_fixture_flows.py:78`
- `scripts/run_sft_overnight_fixture_flows.py:133`
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
- `tests/test_calendar_rrule.py:70`
- `tests/test_calendar_rrule.py:109`
- `tests/test_checkin_digest_owner_scope.py:31`
- `tests/test_checkin_digest_owner_scope.py:32`
- `tests/test_checkin_digest_owner_scope.py:78`
- `tests/test_checkin_digest_owner_scope.py:96`
- `tests/test_daily_brief_local_calendar.py:55`
- `tests/test_upload_handler_cleanup.py:524`

## `CalendarEvent` — class, line 2146
- **called from:**
- `routes/calendar_routes.py:1376`
- `routes/calendar_routes.py:1701`
- `scripts/eval_odysseus_app_route_smoke.py:66`
- `scripts/eval_odysseus_everyday_live_hard.py:198`
- `scripts/eval_odysseus_tool_use.py:343`
- `scripts/run_sft_environment_expansion.py:168`
- `scripts/run_sft_overnight_fixture_flows.py:144`
- `src/caldav_sync.py:437`
- `src/tools/calendar.py:614`
- `tests/test_caldav_bidirectional_sync.py:108`
- `tests/test_caldav_sync_prune_local_events.py:61`
- `tests/test_caldav_sync_prune_local_events.py:67`
- `tests/test_caldav_sync_uid_scope.py:35`
- `tests/test_calendar_default_transaction.py:257`
- `tests/test_calendar_default_transaction.py:515`
- `tests/test_calendar_import_zero_duration.py:134`
- `tests/test_calendar_rrule.py:71`
- `tests/test_calendar_rrule.py:110`
- `tests/test_checkin_digest_owner_scope.py:33`
- `tests/test_checkin_digest_owner_scope.py:36`
- `tests/test_checkin_digest_owner_scope.py:62`
- `tests/test_checkin_digest_owner_scope.py:79`
- `tests/test_checkin_digest_owner_scope.py:103`
- `tests/test_daily_brief_local_calendar.py:58`
- `tests/test_upload_handler_cleanup.py:530`

## `EmailCalendarInvitation` — class, line 2186
- **called from:**
- `src/email_calendar_import.py:114`

## `CalendarDeletedEvent` — class, line 2201
- **called from:**
- `routes/calendar_routes.py:201`
- `tests/test_caldav_bidirectional_sync.py:120`

## `Integration` — class, line 2215
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_migrate_email_account_default_invariant` — function, line 2230
- **called from:**
- `core/database.py:2496`
- `tests/test_email_account_default_serialization.py:262`
- `tests/test_email_account_default_serialization.py:263`

## `_migrate_seed_email_account` — function, line 2293
- **called from:**
- `core/database.py:2497`

## `_migrate_add_task_authority_column` — function, line 2372
- **called from:**
- `core/database.py:2487`
- `tests/test_request_authority.py:379`
- `tests/test_request_authority.py:380`

## `_enable_sqlite_wal` — function, line 2381
- **called from:**
- `core/database.py:2413`

## `init_db` — function, line 2408
- **called from:**
- `core/database.py:3134`

## `_migrate_backfill_task_folders` — function, line 2512
- **called from:**
- `core/database.py:2509`

## `_migrate_chat_messages_fts` — function, line 2538
- **called from:**
- `core/database.py:2505`
- `tests/test_session_search.py:292`
- `tests/test_session_search.py:334`
- `tests/test_session_search.py:335`

## `_scrub_legacy_chat_message_fts_media` — function, line 2640
- **called from:**
- `core/database.py:2629`

## `_migrate_add_email_smtp_security` — function, line 2671
- **called from:**
- `core/database.py:2495`

## `_migrate_encrypt_endpoint_keys` — function, line 2702
- **called from:**
- `core/database.py:2508`

## `_migrate_encrypt_signatures` — function, line 2726
- **called from:**
- `core/database.py:2507`

## `_migrate_encrypt_email_passwords` — function, line 2758
- **called from:**
- `core/database.py:2506`

## `_migrate_add_calendar_is_utc` — function, line 2792
- **called from:**
- `core/database.py:2499`

## `_migrate_add_calendar_origin` — function, line 2818
- **called from:**
- `core/database.py:2500`

## `_migrate_add_calendar_account_id` — function, line 2845
- **called from:**
- `core/database.py:2501`

## `_migrate_add_caldav_sync_columns` — function, line 2871
- **called from:**
- `core/database.py:2502`

## `_migrate_add_calendar_metadata` — function, line 2896
- **called from:**
- `core/database.py:2498`

## `_migrate_add_calendar_recurrence_exdates` — function, line 2923
- **called from:**
- `core/database.py:2503`

## `_migrate_add_note_gallery_id` — function, line 2944
- **called from:**
- `core/database.py:2504`

## `get_db` — function, line 2965
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_db_session` — function, line 2980
- decorator: `contextmanager`
- **called from:**
- `companion/pairing.py:195`
- `core/auth.py:326`
- `core/auth.py:471`
- `core/database.py:2994`
- `core/database.py:3012`
- `core/database.py:3025`
- `core/database.py:3055`
- `core/database.py:3070`
- `core/database.py:3083`
- `core/database.py:3092`
- `core/database.py:3104`
- `core/database.py:3123`
- `routes/api_token_routes.py:82`
- `routes/api_token_routes.py:134`
- `routes/api_token_routes.py:165`
- `routes/api_token_routes.py:199`

## `bulk_insert_messages` — function, line 2992
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_old_sessions` — function, line 3008
- **called from:**
- `src/cleanup_service.py:350`

## `get_session_stats` — function, line 3023
- **called from:**
- `core/database.py:3037`

## `get_detailed_stats` — function, line 3035
- **called from:**
- `routes/diagnostics_routes.py:61`

## `update_session_last_accessed` — function, line 3053
- **called from:**
- `routes/chat_helpers.py:1953`
- `routes/chat_helpers.py:1970`
- `routes/chat_routes.py:2628`
- `src/chat_handler.py:374`

## `get_session_mode` — function, line 3063
- **called from:**
- `routes/chat_routes.py:3247`
- `tests/test_session_mode_helpers.py:74`
- `tests/test_session_mode_helpers.py:81`

## `set_session_mode` — function, line 3076
- **called from:**
- `routes/chat_routes.py:4085`
- `routes/chat_routes.py:4164`
- `tests/test_session_mode_helpers.py:55`
- `tests/test_session_mode_helpers.py:65`

## `get_session_by_id` — function, line 3090
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_upcoming_events` — function, line 3095
- **called from:**
- `routes/email/email_pollers.py:1068`

## `archive_session` — function, line 3121
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
