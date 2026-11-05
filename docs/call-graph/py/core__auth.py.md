# `core/auth.py` — definitions & call sites

44 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `username_error` — function, line 65
- **called from:**
- `routes/auth_routes.py:158`
- `routes/auth_routes.py:179`
- `routes/auth_routes.py:339`
- `routes/auth_routes.py:391`
- `tests/test_auth_username_policy.py:16`
- `tests/test_auth_username_policy.py:21`
- `tests/test_auth_username_policy.py:25`

## `normalize_known_username` — function, line 83
- **called from:**
- `app.py:363`
- `tests/test_reserved_username_admin_escalation.py:150`
- `tests/test_reserved_username_admin_escalation.py:152`
- `tests/test_reserved_username_admin_escalation.py:153`

## `_hash_password` — function, line 91
- **called from:**
- `core/auth.py:294`
- `core/auth.py:513`
- `core/auth.py:526`

## `_verify_password` — function, line 95
- **called from:**
- `core/auth.py:523`
- `core/auth.py:623`

## `SetAdminResult` — class, line 99
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager` — class, line 108
- **called from:**
- `app.py:296`
- `routes/note/note_routes.py:618`
- `routes/note/note_routes.py:926`
- `src/builtin_actions.py:1999`
- `src/task_action_policy.py:35`
- `src/tool_security.py:281`
- `tests/test_admin_listing_authorization.py:21`
- `tests/test_admin_listing_authorization.py:32`
- `tests/test_auth_config_lock_concurrency.py:60`
- `tests/test_auth_policy.py:39`
- `tests/test_auth_session_persistence.py:12`
- `tests/test_auth_session_persistence.py:18`
- `tests/test_auth_session_persistence.py:25`
- `tests/test_auth_session_persistence.py:30`
- `tests/test_auth_session_revocation.py:39`
- `tests/test_chat_document_owner_context.py:22`
- `tests/test_delete_user_revokes_api_tokens.py:80`
- `tests/test_demote_admin_revokes_api_tokens.py:27`
- `tests/test_rename_user_case_insensitive.py:36`
- `tests/test_rename_user_owner_sync.py:101`
- `tests/test_reserved_username_admin_escalation.py:31`
- `tests/test_security_regressions.py:806`
- `tests/test_set_admin.py:45`
- `tests/test_set_admin.py:203`
- `tests/test_totp_failclosed.py:12`
- `tests/test_totp_failclosed.py:20`

## `AuthManager.__init__` — method, line 111
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

## `AuthManager._load` — method, line 132
- **called from:**
- `core/auth.py:126`
- `routes/prefs_routes.py:32`
- `routes/prefs_routes.py:58`
- `scripts/analyze_odysseus_eval_targets.py:122`
- `scripts/summarize_odysseus_eval_delta.py:147`
- `scripts/summarize_odysseus_eval_delta.py:150`
- `src/agent_runtime/process_resources.py:171`
- `src/bg_jobs.py:175`
- `src/bg_jobs.py:244`
- `src/bg_jobs.py:363`
- `src/bg_jobs.py:375`
- `src/bg_jobs.py:387`
- `src/bg_jobs.py:397`
- `src/bg_jobs.py:413`
- `src/bg_jobs.py:457`
- `src/foreground_model_routing.py:51`
- `src/mcp_oauth.py:140`
- `src/mcp_oauth.py:148`
- `src/tools/research.py:55`
- `src/tools/research.py:82`
- `tests/cli/test_preset_cli_store.py:12`
- `tests/test_auth_config_lock_concurrency.py:83`
- `tests/test_background_resource_identity.py:39`
- `tests/test_background_resource_identity.py:114`
- `tests/test_background_resource_identity.py:259`
- `tests/test_background_resource_identity.py:270`
- `tests/test_bg_job_tools.py:55`
- `tests/test_bg_jobs_store.py:11`
- `tests/test_bg_jobs_store.py:28`
- `tests/test_foreground_model_routing.py:2105`
- `tests/test_foreground_model_routing.py:2186`
- `tests/test_gpu_compose_standalone.py:74`
- `tests/test_gpu_compose_standalone.py:81`
- `tests/test_gpu_compose_standalone.py:82`
- `tests/test_gpu_compose_standalone.py:87`
- `tests/test_gpu_compose_standalone.py:88`
- `tests/test_gpu_compose_standalone.py:97`
- `tests/test_gpu_compose_standalone.py:107`
- `tests/test_gpu_compose_standalone.py:115`
- `tests/test_gpu_compose_standalone.py:142`
- `tests/test_gpu_compose_standalone.py:171`
- `tests/test_gpu_compose_standalone.py:182`
- `tests/test_gpu_compose_standalone.py:183`
- `tests/test_gpu_compose_standalone.py:199`
- `tests/test_gpu_compose_standalone.py:200`
- `tests/test_mcp_oauth.py:116`
- `tests/test_orphan_reaping.py:357`
- `tests/test_orphan_reaping.py:382`
- `tests/test_orphan_reaping.py:392`
- `tests/test_prefs_routes.py:11`
- `tests/test_prefs_routes.py:39`
- `tests/test_runtime_resource_integration.py:272`
- `tests/test_search_query_nonstring.py:26`
- `tests/test_search_query_nonstring.py:37`
- `tests/test_wave3_background_followup.py:35`
- `static/js/workspace.js:109`
- `static/js/workspace.js:152`
- `static/js/workspace.js:212`

## `AuthManager._load_sessions` — method, line 154
- **called from:**
- `core/auth.py:127`

## `AuthManager._save_sessions` — method, line 170
- **called from:**
- `core/auth.py:164`
- `core/auth.py:348`
- `core/auth.py:380`
- `core/auth.py:646`
- `core/auth.py:670`
- `core/auth.py:696`
- `core/auth.py:702`
- `core/auth.py:717`

## `AuthManager._migrate_single_user` — method, line 179
- **called from:**
- `core/auth.py:128`

## `AuthManager._drop_reserved_loaded_users` — method, line 203
- **called from:**
- `core/auth.py:129`

## `AuthManager._migrate_legacy_admin_role` — method, line 228
- **called from:**
- `core/auth.py:130`

## `AuthManager._save` — method, line 239
- **called from:**
- `core/auth.py:200`
- `core/auth.py:221`
- `core/auth.py:237`
- `core/auth.py:254`
- `core/auth.py:299`
- `core/auth.py:336`
- `core/auth.py:370`
- `core/auth.py:428`
- `core/auth.py:502`
- `core/auth.py:514`
- `core/auth.py:527`
- `core/auth.py:547`
- `core/auth.py:573`
- `core/auth.py:595`
- `core/auth.py:611`
- `routes/prefs_routes.py:89`
- `routes/prefs_routes.py:91`
- `routes/prefs_routes.py:100`
- `src/bg_jobs.py:177`
- `src/bg_jobs.py:313`
- `src/bg_jobs.py:369`
- `src/bg_jobs.py:382`
- `src/bg_jobs.py:432`
- `src/bg_jobs.py:481`
- `tests/test_background_containment.py:131`
- `tests/test_background_resource_identity.py:41`
- `tests/test_background_resource_identity.py:116`
- `tests/test_background_resource_identity.py:261`
- `tests/test_background_resource_identity.py:272`
- `tests/test_bg_job_tools.py:57`
- `tests/test_orphan_reaping.py:83`
- `tests/test_prefs_atomic_write.py:19`
- `tests/test_runtime_resource_integration.py:125`
- `tests/test_runtime_resource_integration.py:264`
- `tests/test_runtime_resource_integration.py:279`
- `tests/test_wave3_background_followup.py:38`
- `tests/test_wave3_background_followup.py:66`
- `tests/test_wave3_launch_cost_lifecycle.py:130`
- `tests/test_wave3_launch_cost_lifecycle.py:136`

## `AuthManager.users` — method, line 243
- decorator: `property`
- **called from:**
- `static/js/cookbook.js:87`

## `AuthManager.signup_enabled` — method, line 247
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.signup_enabled` — method, line 251
- decorator: `signup_enabled.setter`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.is_configured` — method, line 257
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.policy` — method, line 260
- **called from:**
- `routes/auth_routes.py:249`
- `tests/test_auth_policy.py:52`
- `tests/test_auth_policy.py:58`
- `tests/test_auth_policy.py:68`
- `tests/test_auth_policy.py:74`
- `tests/test_auth_policy.py:108`

## `AuthManager.setup` — method, line 273
- **called from:**
- `scripts/demo_email/demo_account.py:178`
- `tests/test_reserved_username_admin_escalation.py:55`
- `tests/test_token_cache_atomic_swap.py:34`

## `AuthManager.create_user` — method, line 280
- **called from:**
- `core/auth.py:278`
- `routes/auth_routes.py:344`
- `tests/test_admin_listing_authorization.py:23`
- `tests/test_admin_listing_authorization.py:156`
- `tests/test_auth_config_lock_concurrency.py:72`
- `tests/test_auth_config_lock_concurrency.py:91`
- `tests/test_auth_config_lock_concurrency.py:108`
- `tests/test_auth_config_lock_concurrency.py:111`
- `tests/test_auth_config_lock_concurrency.py:136`
- `tests/test_auth_config_lock_concurrency.py:139`
- `tests/test_auth_config_lock_concurrency.py:162`
- `tests/test_auth_config_lock_concurrency.py:165`
- `tests/test_auth_config_lock_concurrency.py:169`
- `tests/test_auth_config_lock_concurrency.py:209`
- `tests/test_auth_config_lock_concurrency.py:235`
- `tests/test_auth_policy.py:165`
- `tests/test_auth_policy.py:180`
- `tests/test_auth_policy.py:262`
- `tests/test_auth_policy.py:277`
- `tests/test_auth_policy.py:295`
- `tests/test_auth_session_persistence.py:13`
- `tests/test_auth_session_persistence.py:26`
- `tests/test_auth_session_revocation.py:40`
- `tests/test_auth_session_revocation.py:41`
- `tests/test_auth_session_revocation.py:51`
- `tests/test_auth_session_revocation.py:130`
- `tests/test_auth_username_policy.py:43`
- `tests/test_chat_document_owner_context.py:24`
- `tests/test_delete_user_revokes_api_tokens.py:81`
- `tests/test_delete_user_revokes_api_tokens.py:82`
- `tests/test_demote_admin_revokes_api_tokens.py:28`
- `tests/test_demote_admin_revokes_api_tokens.py:29`
- `tests/test_demote_admin_revokes_api_tokens.py:30`
- `tests/test_rename_user_case_insensitive.py:41`
- `tests/test_rename_user_case_insensitive.py:42`
- `tests/test_rename_user_owner_sync.py:102`
- `tests/test_rename_user_owner_sync.py:103`
- `tests/test_reserved_username_admin_escalation.py:40`
- `tests/test_reserved_username_admin_escalation.py:47`
- `tests/test_reserved_username_admin_escalation.py:62`
- `tests/test_reserved_username_admin_escalation.py:63`
- `tests/test_reserved_username_admin_escalation.py:158`
- `tests/test_set_admin.py:51`
- `tests/test_set_admin.py:52`
- `tests/test_set_admin.py:63`
- `tests/test_set_admin.py:64`
- `tests/test_set_admin.py:75`
- `tests/test_set_admin.py:85`
- `tests/test_set_admin.py:86`
- `tests/test_set_admin.py:97`
- `tests/test_set_admin.py:98`
- `tests/test_set_admin.py:108`
- `tests/test_set_admin.py:109`
- `tests/test_set_admin.py:110`
- `tests/test_set_admin.py:120`
- `tests/test_set_admin.py:129`
- `tests/test_set_admin.py:130`
- `tests/test_set_admin.py:143`
- `tests/test_set_admin.py:144`
- `tests/test_set_admin.py:164`
- … +7 more (grep the name in repo)

## `AuthManager.delete_user` — method, line 303
- **called from:**
- `routes/auth_routes.py:736`
- `tests/test_auth_config_lock_concurrency.py:116`
- `tests/test_auth_config_lock_concurrency.py:173`
- `tests/test_delete_user_revokes_api_tokens.py:102`
- `tests/test_delete_user_revokes_api_tokens.py:109`
- `tests/test_delete_user_revokes_api_tokens.py:115`
- `tests/test_delete_user_revokes_api_tokens.py:132`

## `AuthManager.rename_user` — method, line 352
- **called from:**
- `routes/auth_routes.py:405`
- `routes/auth_routes.py:414`
- `tests/test_auth_config_lock_concurrency.py:142`
- `tests/test_auth_config_lock_concurrency.py:177`
- `tests/test_auth_session_revocation.py:133`
- `tests/test_email_account_default_serialization.py:452`
- `tests/test_rename_user_case_insensitive.py:45`
- `tests/test_reserved_username_admin_escalation.py:64`

## `AuthManager.is_admin` — method, line 387
- **called from:**
- `core/auth.py:511`
- `core/auth.py:727`
- `core/middleware.py:81`
- `routes/auth_routes.py:145`
- `routes/auth_routes.py:328`
- `routes/auth_routes.py:335`
- `routes/auth_routes.py:352`
- `routes/auth_routes.py:366`
- `routes/auth_routes.py:385`
- `routes/auth_routes.py:669`
- `routes/auth_routes.py:707`
- `routes/auth_routes.py:716`
- `routes/auth_routes.py:724`
- `routes/auth_routes.py:781`
- `routes/editor_agent_routes.py:1311`
- `routes/gallery/gallery_routes.py:558`
- `routes/model_routes.py:1789`
- `routes/model_routes.py:2804`
- `routes/note/note_routes.py:621`
- `routes/session_routes.py:292`
- `routes/shell_routes.py:81`
- `routes/upload_routes.py:245`
- `src/task_action_policy.py:40`
- `src/tool_security.py:284`
- `src/upload_handler.py:1001`
- `tests/test_demote_admin_revokes_api_tokens.py:53`
- `tests/test_demote_admin_revokes_api_tokens.py:82`
- `tests/test_reserved_username_admin_escalation.py:141`
- `tests/test_security_regressions.py:808`
- `tests/test_set_admin.py:57`
- `tests/test_set_admin.py:69`
- `tests/test_set_admin.py:80`
- `tests/test_set_admin.py:91`
- `tests/test_set_admin.py:92`
- `tests/test_set_admin.py:103`
- `tests/test_set_admin.py:115`

## `AuthManager.list_users` — method, line 390
- **called from:**
- `routes/auth_routes.py:330`

## `AuthManager.get_privileges` — method, line 396
- **called from:**
- `core/auth.py:392`
- `core/auth.py:414`
- `core/auth.py:730`
- `routes/auth_routes.py:241`
- `routes/auth_routes.py:380`
- `routes/chat_helpers.py:495`
- `routes/chat_helpers.py:518`
- `routes/chat_routes.py:170`
- `routes/research/research_routes.py:556`
- `src/auth_helpers.py:200`
- `tests/test_set_admin.py:151`
- `tests/test_set_admin.py:157`
- `tests/test_set_admin.py:158`
- `tests/test_set_admin.py:159`
- `tests/test_set_admin.py:167`
- `tests/test_set_admin.py:173`
- `tests/test_set_admin.py:183`
- `tests/test_set_admin.py:191`
- `tests/test_set_admin.py:192`
- `tests/test_set_admin.py:205`
- `tests/test_set_privileges_validation.py:19`
- `tests/test_set_privileges_validation.py:24`
- `tests/test_set_privileges_validation.py:38`

## `AuthManager.set_privileges` — method, line 405
- **called from:**
- `routes/auth_routes.py:375`
- `tests/test_set_admin.py:132`
- `tests/test_set_admin.py:146`
- `tests/test_set_admin.py:166`
- `tests/test_set_admin.py:182`
- `tests/test_set_admin.py:199`
- `tests/test_set_privileges_validation.py:22`
- `tests/test_set_privileges_validation.py:31`

## `AuthManager.set_admin` — method, line 432
- **called from:**
- `routes/auth_routes.py:672`
- `tests/test_demote_admin_revokes_api_tokens.py:50`
- `tests/test_demote_admin_revokes_api_tokens.py:58`
- `tests/test_demote_admin_revokes_api_tokens.py:64`
- `tests/test_demote_admin_revokes_api_tokens.py:80`
- `tests/test_set_admin.py:54`
- `tests/test_set_admin.py:66`
- `tests/test_set_admin.py:77`
- `tests/test_set_admin.py:88`
- `tests/test_set_admin.py:100`
- `tests/test_set_admin.py:102`
- `tests/test_set_admin.py:112`
- `tests/test_set_admin.py:122`
- `tests/test_set_admin.py:134`
- `tests/test_set_admin.py:153`
- `tests/test_set_admin.py:154`
- `tests/test_set_admin.py:170`
- `tests/test_set_admin.py:171`
- `tests/test_set_admin.py:185`
- `tests/test_set_admin.py:187`
- `tests/test_set_admin.py:188`
- `tests/test_set_admin.py:200`
- `tests/test_set_admin.py:204`

## `AuthManager.reset_user_password` — method, line 506
- **called from:**
- `tests/test_auth_session_revocation.py:54`
- `tests/test_auth_session_revocation.py:55`
- `tests/test_auth_session_revocation.py:56`
- `tests/test_auth_session_revocation.py:58`

## `AuthManager.change_password` — method, line 519
- **called from:**
- `tests/test_auth_session_revocation.py:113`
- `tests/test_auth_session_revocation.py:122`

## `AuthManager.totp_enabled` — method, line 534
- **called from:**
- `routes/auth_routes.py:198`
- `routes/auth_routes.py:275`
- `routes/auth_routes.py:322`

## `AuthManager.totp_generate_secret` — method, line 539
- **called from:**
- `routes/auth_routes.py:277`

## `AuthManager.totp_get_provisioning_uri` — method, line 550
- **called from:**
- `routes/auth_routes.py:280`

## `AuthManager.totp_confirm_enable` — method, line 555
- **called from:**
- `routes/auth_routes.py:298`

## `AuthManager.totp_verify` — method, line 577
- **called from:**
- `routes/auth_routes.py:202`
- `tests/test_totp_failclosed.py:14`
- `tests/test_totp_failclosed.py:21`

## `AuthManager.totp_disable` — method, line 601
- **called from:**
- `routes/auth_routes.py:312`

## `AuthManager.verify_password` — method, line 619
- **called from:**
- `core/auth.py:604`
- `core/auth.py:628`
- `tests/test_auth_session_revocation.py:61`
- `tests/test_auth_session_revocation.py:62`
- `tests/test_auth_session_revocation.py:132`

## `AuthManager.create_session` — method, line 625
- **called from:**
- `core/session_manager.py:1113`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:1085`
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

## `AuthManager.create_session_trusted` — method, line 632
- **called from:**
- `core/auth.py:630`
- `tests/test_auth_session_persistence.py:14`
- `tests/test_auth_session_persistence.py:27`
- `tests/test_auth_session_revocation.py:135`
- `tests/test_rename_user_owner_sync.py:652`
- `tests/test_rename_user_owner_sync.py:653`
- `tests/test_rename_user_owner_sync.py:681`

## `AuthManager.validate_token` — method, line 649
- **called from:**
- `app.py:512`
- `tests/test_auth_session_persistence.py:15`
- `tests/test_auth_session_persistence.py:19`
- `tests/test_auth_session_persistence.py:31`
- `tests/test_auth_session_revocation.py:57`
- `tests/test_auth_session_revocation.py:59`
- `tests/test_auth_session_revocation.py:60`
- `tests/test_auth_session_revocation.py:103`
- `tests/test_auth_session_revocation.py:104`
- `tests/test_auth_session_revocation.py:105`
- `tests/test_auth_session_revocation.py:115`
- `tests/test_auth_session_revocation.py:116`
- `tests/test_delete_user_revokes_api_tokens.py:134`
- `tests/test_reserved_username_admin_escalation.py:97`

## `AuthManager.get_username_for_token` — method, line 674
- **called from:**
- `app.py:521`
- `core/auth.py:721`
- `routes/auth_routes.py:132`
- `tests/test_admin_listing_authorization.py:39`
- `tests/test_admin_listing_authorization.py:155`
- `tests/test_auth_session_persistence.py:20`
- `tests/test_chat_document_owner_context.py:73`
- `tests/test_rename_user_owner_sync.py:670`
- `tests/test_rename_user_owner_sync.py:698`
- `tests/test_reserved_username_admin_escalation.py:98`
- `tests/test_reserved_username_admin_escalation.py:119`

## `AuthManager.revoke_token` — method, line 699
- **called from:**
- `routes/auth_routes.py:225`
- `tests/test_auth_session_persistence.py:28`

## `AuthManager.revoke_user_sessions` — method, line 704
- **called from:**
- `core/auth.py:515`
- `tests/test_auth_session_revocation.py:100`

## `AuthManager.status` — method, line 720
- **called from:**
- `routes/auth_routes.py:232`
- `scripts/sft_email_overseer.py:783`
- `static/js/skills.js:1585`
- `static/js/tasks.js:2792`
