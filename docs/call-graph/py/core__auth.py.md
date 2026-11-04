# `core/auth.py` — definitions & call sites

42 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `normalize_known_username` — function, line 65
- **called from:**
- `app.py:322`
- `tests/test_reserved_username_admin_escalation.py:150`
- `tests/test_reserved_username_admin_escalation.py:152`
- `tests/test_reserved_username_admin_escalation.py:153`

## `_hash_password` — function, line 73
- **called from:**
- `core/auth.py:276`
- `core/auth.py:475`

## `_verify_password` — function, line 77
- **called from:**
- `core/auth.py:472`
- `core/auth.py:572`

## `SetAdminResult` — class, line 81
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager` — class, line 90
- **called from:**
- `app.py:256`
- `routes/note/note_routes.py:615`
- `routes/note/note_routes.py:917`
- `src/builtin_actions.py:1800`
- `src/task_action_policy.py:35`
- `src/tool_security.py:258`
- `tests/test_auth_config_lock_concurrency.py:60`
- `tests/test_auth_policy.py:39`
- `tests/test_auth_session_revocation.py:39`
- `tests/test_delete_user_revokes_api_tokens.py:80`
- `tests/test_rename_user_case_insensitive.py:36`
- `tests/test_rename_user_owner_sync.py:101`
- `tests/test_reserved_username_admin_escalation.py:31`
- `tests/test_security_regressions.py:805`
- `tests/test_set_admin.py:45`
- `tests/test_set_admin.py:203`
- `tests/test_totp_failclosed.py:12`
- `tests/test_totp_failclosed.py:20`

## `AuthManager.__init__` — method, line 93
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

## `AuthManager._load` — method, line 114
- **called from:**
- `core/auth.py:108`
- `routes/prefs_routes.py:32`
- `routes/prefs_routes.py:58`
- `src/bg_jobs.py:156`
- `src/bg_jobs.py:194`
- `src/bg_jobs.py:247`
- `src/bg_jobs.py:255`
- `src/bg_jobs.py:271`
- `src/foreground_model_routing.py:51`
- `src/mcp_oauth.py:140`
- `src/mcp_oauth.py:148`
- `src/tools/research.py:54`
- `src/tools/research.py:81`
- `tests/cli/test_preset_cli_store.py:12`
- `tests/test_auth_config_lock_concurrency.py:83`
- `tests/test_bg_job_tools.py:42`
- `tests/test_bg_jobs_store.py:11`
- `tests/test_bg_jobs_store.py:28`
- `tests/test_foreground_model_routing.py:2021`
- `tests/test_foreground_model_routing.py:2102`
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
- `tests/test_prefs_routes.py:11`
- `tests/test_prefs_routes.py:39`
- `tests/test_search_query_nonstring.py:26`
- `tests/test_search_query_nonstring.py:37`
- `static/js/workspace.js:92`
- `static/js/workspace.js:135`
- `static/js/workspace.js:189`

## `AuthManager._load_sessions` — method, line 136
- **called from:**
- `core/auth.py:109`

## `AuthManager._save_sessions` — method, line 152
- **called from:**
- `core/auth.py:146`
- `core/auth.py:330`
- `core/auth.py:362`
- `core/auth.py:595`
- `core/auth.py:619`
- `core/auth.py:645`
- `core/auth.py:651`
- `core/auth.py:666`

## `AuthManager._migrate_single_user` — method, line 161
- **called from:**
- `core/auth.py:110`

## `AuthManager._drop_reserved_loaded_users` — method, line 185
- **called from:**
- `core/auth.py:111`

## `AuthManager._migrate_legacy_admin_role` — method, line 210
- **called from:**
- `core/auth.py:112`

## `AuthManager._save` — method, line 221
- **called from:**
- `core/auth.py:182`
- `core/auth.py:203`
- `core/auth.py:219`
- `core/auth.py:236`
- `core/auth.py:281`
- `core/auth.py:318`
- `core/auth.py:352`
- `core/auth.py:401`
- `core/auth.py:464`
- `core/auth.py:476`
- `core/auth.py:496`
- `core/auth.py:522`
- `core/auth.py:544`
- `core/auth.py:560`
- `routes/prefs_routes.py:89`
- `routes/prefs_routes.py:91`
- `routes/prefs_routes.py:100`
- `src/bg_jobs.py:158`
- `src/bg_jobs.py:229`
- `src/bg_jobs.py:250`
- `src/bg_jobs.py:282`
- `tests/test_bg_job_tools.py:44`
- `tests/test_prefs_atomic_write.py:19`

## `AuthManager.users` — method, line 225
- decorator: `property`
- **called from:**
- `static/js/cookbook.js:93`

## `AuthManager.signup_enabled` — method, line 229
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.signup_enabled` — method, line 233
- decorator: `signup_enabled.setter`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.is_configured` — method, line 239
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `AuthManager.policy` — method, line 242
- **called from:**
- `routes/auth_routes.py:225`
- `tests/test_auth_policy.py:52`
- `tests/test_auth_policy.py:58`
- `tests/test_auth_policy.py:68`
- `tests/test_auth_policy.py:74`
- `tests/test_auth_policy.py:108`

## `AuthManager.setup` — method, line 255
- **called from:**
- `scripts/demo_email/demo_account.py:178`
- `tests/test_reserved_username_admin_escalation.py:55`

## `AuthManager.create_user` — method, line 262
- **called from:**
- `core/auth.py:260`
- `routes/auth_routes.py:319`
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
- `tests/test_auth_config_lock_concurrency.py:229`
- `tests/test_auth_policy.py:165`
- `tests/test_auth_policy.py:180`
- `tests/test_auth_policy.py:262`
- `tests/test_auth_policy.py:277`
- `tests/test_auth_policy.py:295`
- `tests/test_auth_session_revocation.py:40`
- `tests/test_auth_session_revocation.py:41`
- `tests/test_auth_session_revocation.py:85`
- `tests/test_delete_user_revokes_api_tokens.py:81`
- `tests/test_delete_user_revokes_api_tokens.py:82`
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
- `tests/test_set_admin.py:165`
- `tests/test_set_admin.py:180`
- `tests/test_set_admin.py:181`
- `tests/test_set_admin.py:197`
- `tests/test_set_admin.py:198`

## `AuthManager.delete_user` — method, line 285
- **called from:**
- `routes/auth_routes.py:675`
- `tests/test_auth_config_lock_concurrency.py:116`
- `tests/test_auth_config_lock_concurrency.py:173`
- `tests/test_delete_user_revokes_api_tokens.py:102`
- `tests/test_delete_user_revokes_api_tokens.py:109`
- `tests/test_delete_user_revokes_api_tokens.py:115`
- `tests/test_delete_user_revokes_api_tokens.py:132`

## `AuthManager.rename_user` — method, line 334
- **called from:**
- `routes/auth_routes.py:355`
- `routes/auth_routes.py:364`
- `tests/test_auth_config_lock_concurrency.py:142`
- `tests/test_auth_config_lock_concurrency.py:177`
- `tests/test_auth_session_revocation.py:88`
- `tests/test_email_account_default_serialization.py:452`
- `tests/test_rename_user_case_insensitive.py:45`
- `tests/test_reserved_username_admin_escalation.py:64`

## `AuthManager.is_admin` — method, line 369
- **called from:**
- `core/auth.py:676`
- `core/middleware.py:81`
- `routes/auth_routes.py:304`
- `routes/auth_routes.py:311`
- `routes/auth_routes.py:327`
- `routes/auth_routes.py:338`
- `routes/auth_routes.py:619`
- `routes/auth_routes.py:646`
- `routes/auth_routes.py:655`
- `routes/auth_routes.py:663`
- `routes/auth_routes.py:703`
- `routes/auth_routes.py:722`
- `routes/auth_routes.py:730`
- `routes/auth_routes.py:766`
- `routes/auth_routes.py:782`
- `routes/auth_routes.py:792`
- `routes/auth_routes.py:804`
- `routes/auth_routes.py:815`
- `routes/gallery/gallery_routes.py:216`
- `routes/model_routes.py:1649`
- `routes/model_routes.py:2439`
- `routes/note/note_routes.py:618`
- `routes/session_routes.py:182`
- `routes/shell_routes.py:68`
- `routes/upload_routes.py:377`
- `routes/upload_routes.py:466`
- `routes/upload_routes.py:512`
- `src/task_action_policy.py:40`
- `src/tool_security.py:261`
- `src/upload_handler.py:947`
- `tests/test_reserved_username_admin_escalation.py:141`
- `tests/test_security_regressions.py:807`
- `tests/test_set_admin.py:57`
- `tests/test_set_admin.py:69`
- `tests/test_set_admin.py:80`
- `tests/test_set_admin.py:91`
- `tests/test_set_admin.py:92`
- `tests/test_set_admin.py:103`
- `tests/test_set_admin.py:115`

## `AuthManager.list_users` — method, line 372
- **called from:**
- `routes/auth_routes.py:306`

## `AuthManager.get_privileges` — method, line 378
- **called from:**
- `core/auth.py:374`
- `core/auth.py:396`
- `core/auth.py:679`
- `routes/auth_routes.py:217`
- `routes/auth_routes.py:333`
- `routes/chat_helpers.py:208`
- `routes/chat_helpers.py:231`
- `routes/chat_routes.py:1733`
- `routes/research/research_routes.py:503`
- `src/auth_helpers.py:179`
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

## `AuthManager.set_privileges` — method, line 387
- **called from:**
- `routes/auth_routes.py:330`
- `tests/test_set_admin.py:132`
- `tests/test_set_admin.py:146`
- `tests/test_set_admin.py:166`
- `tests/test_set_admin.py:182`
- `tests/test_set_admin.py:199`

## `AuthManager.set_admin` — method, line 405
- **called from:**
- `routes/auth_routes.py:621`
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

## `AuthManager.change_password` — method, line 468
- **called from:**
- `tests/test_auth_session_revocation.py:68`
- `tests/test_auth_session_revocation.py:77`

## `AuthManager.totp_enabled` — method, line 483
- **called from:**
- `routes/auth_routes.py:174`
- `routes/auth_routes.py:251`
- `routes/auth_routes.py:298`

## `AuthManager.totp_generate_secret` — method, line 488
- **called from:**
- `routes/auth_routes.py:253`

## `AuthManager.totp_get_provisioning_uri` — method, line 499
- **called from:**
- `routes/auth_routes.py:256`

## `AuthManager.totp_confirm_enable` — method, line 504
- **called from:**
- `routes/auth_routes.py:274`

## `AuthManager.totp_verify` — method, line 526
- **called from:**
- `routes/auth_routes.py:178`
- `tests/test_totp_failclosed.py:14`
- `tests/test_totp_failclosed.py:21`

## `AuthManager.totp_disable` — method, line 550
- **called from:**
- `routes/auth_routes.py:288`

## `AuthManager.verify_password` — method, line 568
- **called from:**
- `core/auth.py:553`
- `core/auth.py:577`
- `tests/test_auth_session_revocation.py:87`

## `AuthManager.create_session` — method, line 574
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

## `AuthManager.create_session_trusted` — method, line 581
- **called from:**
- `core/auth.py:579`
- `tests/test_auth_session_revocation.py:90`
- `tests/test_rename_user_owner_sync.py:652`
- `tests/test_rename_user_owner_sync.py:653`
- `tests/test_rename_user_owner_sync.py:681`

## `AuthManager.validate_token` — method, line 598
- **called from:**
- `app.py:471`
- `tests/test_auth_session_revocation.py:58`
- `tests/test_auth_session_revocation.py:59`
- `tests/test_auth_session_revocation.py:60`
- `tests/test_auth_session_revocation.py:70`
- `tests/test_auth_session_revocation.py:71`
- `tests/test_delete_user_revokes_api_tokens.py:134`
- `tests/test_reserved_username_admin_escalation.py:97`

## `AuthManager.get_username_for_token` — method, line 623
- **called from:**
- `app.py:480`
- `core/auth.py:670`
- `routes/auth_routes.py:125`
- `tests/test_rename_user_owner_sync.py:670`
- `tests/test_rename_user_owner_sync.py:698`
- `tests/test_reserved_username_admin_escalation.py:98`
- `tests/test_reserved_username_admin_escalation.py:119`

## `AuthManager.revoke_token` — method, line 648
- **called from:**
- `routes/auth_routes.py:201`

## `AuthManager.revoke_user_sessions` — method, line 653
- **called from:**
- `tests/test_auth_session_revocation.py:55`

## `AuthManager.status` — method, line 669
- **called from:**
- `routes/auth_routes.py:208`
- `static/js/skills.js:1305`
- `static/js/tasks.js:2656`
