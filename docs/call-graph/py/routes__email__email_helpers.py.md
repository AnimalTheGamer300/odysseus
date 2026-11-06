# `routes/email/email_helpers.py` — definitions & call sites

73 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmailNotConfiguredError` — class, line 47
- **called from:**
- `routes/email/email_helpers.py:1360`

## `_xoauth2_raw` — function, line 57
- **called from:**
- `routes/email/email_helpers.py:69`
- `routes/email/email_helpers.py:268`
- `routes/email/email_routes.py:7699`
- `tests/test_email_oauth.py:142`

## `_xoauth2_bytes` — function, line 67
- **called from:**
- `routes/email/email_helpers.py:1382`
- `routes/email/email_routes.py:7635`
- `tests/test_email_oauth.py:148`

## `make_oauth_state` — function, line 72
- **called from:**
- `routes/email/email_routes.py:7820`
- `tests/test_email_oauth.py:42`
- `tests/test_email_oauth.py:54`
- `tests/test_email_oauth.py:55`
- `tests/test_email_oauth.py:62`
- `tests/test_email_oauth.py:77`
- `tests/test_email_oauth.py:298`
- `tests/test_email_oauth.py:355`
- `tests/test_email_oauth.py:403`
- `tests/test_email_oauth.py:468`
- `tests/test_email_oauth.py:504`
- `tests/test_email_oauth.py:573`
- `tests/test_email_oauth.py:622`
- `tests/test_email_oauth.py:676`

## `verify_oauth_state` — function, line 87
- **called from:**
- `routes/email/email_routes.py:7846`
- `tests/test_email_oauth.py:43`
- `tests/test_email_oauth.py:54`
- `tests/test_email_oauth.py:55`
- `tests/test_email_oauth.py:71`
- `tests/test_email_oauth.py:82`
- `tests/test_email_oauth.py:89`

## `_refresh_google_token` — function, line 106
- **called from:**
- `routes/email/email_helpers.py:154`
- `tests/test_email_oauth.py:216`
- `tests/test_email_oauth.py:248`
- `tests/test_email_oauth.py:759`
- `tests/test_email_oauth.py:769`

## `_get_valid_google_token` — function, line 143
- **called from:**
- `routes/email/email_helpers.py:264`
- `routes/email/email_helpers.py:1379`
- `routes/email/email_routes.py:7597`
- `tests/test_email_oauth.py:715`
- `tests/test_email_oauth.py:734`

## `_smtp_security_mode` — function, line 157
- **called from:**
- `routes/email/email_helpers.py:272`
- `routes/email/email_helpers.py:1213`
- `routes/email/email_helpers.py:1247`
- `routes/email/email_routes.py:7415`
- `routes/email/email_routes.py:7462`
- `routes/email/email_routes.py:7514`
- `routes/email/email_routes.py:7656`
- `routes/email/email_routes.py:7661`
- `routes/email/email_routes.py:7762`

## `_mail_private_blocked` — function, line 171
- **called from:**
- `routes/email/email_helpers.py:273`
- `routes/email/email_helpers.py:1315`
- `routes/email/email_routes.py:94`
- `routes/email/email_routes.py:7676`
- `routes/email/email_routes.py:7680`
- `tests/test_codeql_python_residual_closure.py:403`
- `tests/test_codeql_python_residual_closure.py:412`

## `_mail_socket_timeout` — function, line 191
- **called from:**
- `routes/email/email_helpers.py:211`

## `_PolicyIMAP4` — class, line 195
- **called from:**
- `routes/email/email_helpers.py:1317`
- `routes/email/email_helpers.py:1335`
- `tests/test_codeql_python_residual_closure.py:202`

## `_PolicyIMAP4.__init__` — method, line 203
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

## `_PolicyIMAP4._create_socket` — method, line 207
- **called from:**
- `routes/email/email_helpers.py:223`
- `tests/test_email_account_host_ssrf.py:387`

## `_PolicyIMAP4_SSL` — class, line 215
- **called from:**
- `routes/email/email_helpers.py:1333`
- `tests/test_codeql_python_residual_closure.py:199`

## `_PolicyIMAP4_SSL.__init__` — method, line 218
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

## `_PolicyIMAP4_SSL._create_socket` — method, line 222
- **called from:**
- `routes/email/email_helpers.py:223`
- `tests/test_email_account_host_ssrf.py:387`

## `_PolicySMTP` — class, line 227
- **called from:**
- `routes/email/email_helpers.py:281`
- `routes/email/email_routes.py:7680`
- `tests/test_codeql_python_residual_closure.py:221`

## `_PolicySMTP.__init__` — method, line 230
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

## `_PolicySMTP._get_socket` — method, line 234
- **called from:**
- `routes/email/email_helpers.py:251`
- `tests/test_email_account_host_ssrf.py:399`

## `_PolicySMTP_SSL` — class, line 243
- **called from:**
- `routes/email/email_helpers.py:276`
- `routes/email/email_routes.py:7672`
- `tests/test_codeql_python_residual_closure.py:218`

## `_PolicySMTP_SSL.__init__` — method, line 246
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

## `_PolicySMTP_SSL._get_socket` — method, line 250
- **called from:**
- `routes/email/email_helpers.py:251`
- `tests/test_email_account_host_ssrf.py:399`

## `_send_smtp_message` — function, line 255
- **called from:**
- `routes/email/email_pollers.py:476`
- `routes/email/email_pollers.py:1424`
- `routes/email/email_pollers.py:1667`
- `routes/email/email_routes.py:3357`
- `routes/email/email_routes.py:5923`
- `routes/email/email_routes.py:6254`
- `routes/note/note_routes.py:392`
- `src/task_scheduler.py:2005`
- `tests/test_codeql_python_residual_followup.py:142`
- `tests/test_email_account_host_ssrf.py:344`
- `tests/test_email_account_host_ssrf.py:370`
- `tests/test_email_smtp_security.py:60`
- `tests/test_email_smtp_security.py:74`
- `tests/test_email_smtp_security.py:89`
- `tests/test_email_smtp_security.py:102`

## `_auth_smtp` — function, line 262
- **called from:**
- `routes/email/email_helpers.py:277`
- `routes/email/email_helpers.py:284`

## `_friendly_email_auth_error` — function, line 288
- **called from:**
- `routes/email/email_helpers.py:350`

## `_mail_connection_test_error` — function, line 324
- **called from:**
- `routes/email/email_routes.py:7643`
- `routes/email/email_routes.py:7704`
- `tests/test_codeql_python_residual_followup.py:163`
- `tests/test_codeql_python_residual_followup.py:171`
- `tests/test_codeql_python_residual_followup.py:174`

## `_strip_think` — function, line 353
- **called from:**
- `routes/email/email_helpers.py:404`
- `routes/email/email_helpers.py:503`
- `routes/email/email_pollers.py:1127`
- `routes/email/email_pollers.py:1337`
- `routes/email/email_pollers.py:1468`
- `routes/email/email_routes.py:6568`
- `routes/note/note_routes.py:236`
- `routes/task/task_routes.py:1215`
- `services/memory/memory_extractor.py:559`
- `services/memory/skill_extractor.py:230`

## `_extract_reply` — function, line 379
- **called from:**
- `mcp_servers/email_server.py:3109`
- `routes/email/email_helpers.py:499`
- `routes/email/email_pollers.py:1036`
- `routes/email/email_routes.py:3883`
- `routes/email/email_routes.py:6806`
- `routes/email/email_routes.py:6905`
- `src/builtin_actions.py:1333`

## `_build_email_summary_messages` — function, line 407
- **called from:**
- `routes/email/email_helpers.py:456`
- `routes/email/email_helpers.py:483`

## `_generate_email_summary` — function (async), line 437
- **called from:**
- `routes/email/email_routes.py:6642`
- `tests/test_email_summary_llm.py:46`
- `tests/test_utility_reasoning_effort.py:430`

## `_generate_scheduled_email_summary` — function (async), line 467
- **called from:**
- `routes/email/email_pollers.py:973`
- `tests/test_email_summary_llm.py:101`
- `tests/test_email_summary_llm.py:164`

## `_normalize_email_summary` — function, line 495
- **called from:**
- `routes/email/email_helpers.py:464`
- `routes/email/email_helpers.py:492`

## `_email_summary_failure_log_detail` — function, line 518
- **called from:**
- `routes/email/email_pollers.py:1008`
- `routes/email/email_routes.py:6656`
- `routes/email/email_routes.py:6694`

## `_apply_email_style_mechanics` — function, line 529
- **called from:**
- `mcp_servers/email_server.py:3109`
- `routes/email/email_pollers.py:1036`
- `routes/email/email_routes.py:3883`
- `routes/email/email_routes.py:6905`
- `routes/email/email_routes.py:7129`
- `routes/email/email_routes.py:7167`

## `_require_auth` — function, line 541
- **called from:**
- `routes/email/email_helpers.py:575`
- `routes/email/email_helpers.py:584`

## `require_owner` — function, line 569
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `require_user` — function, line 581
- **called from:**
- `routes/calendar_routes.py:75`
- `routes/codex_routes.py:97`
- `routes/codex_routes.py:111`
- `routes/history/history_routes.py:1185`
- `routes/memory/memory_routes.py:241`
- `routes/note/note_routes.py:601`
- `routes/note/note_routes.py:861`
- `src/auth_helpers.py:114`
- `src/auth_helpers.py:193`
- `tests/test_api_token_user_route_gate.py:32`
- `tests/test_api_token_user_route_gate.py:51`
- `tests/test_security_regressions.py:545`
- `tests/test_security_regressions.py:599`
- `tests/test_security_regressions.py:632`
- `tests/test_security_regressions.py:664`
- `tests/test_security_regressions.py:696`

## `_assert_owns_account` — function, line 587
- **called from:**
- `routes/codex_routes.py:316`
- `routes/codex_routes.py:343`
- `routes/email/email_helpers.py:577`
- `routes/email/email_routes.py:3299`
- `routes/email/email_routes.py:3323`
- `routes/email/email_routes.py:3415`
- `routes/email/email_routes.py:4456`
- `routes/email/email_routes.py:4544`
- `routes/email/email_routes.py:5349`
- `routes/email/email_routes.py:5466`
- `routes/email/email_routes.py:5939`
- `routes/email/email_routes.py:6159`
- `routes/email/email_routes.py:6397`
- `routes/email/email_routes.py:6483`
- `routes/email/email_routes.py:6597`
- `routes/email/email_routes.py:6887`
- `routes/email/email_routes.py:7218`
- `routes/email/email_routes.py:7230`
- `routes/email/email_routes.py:7245`
- `routes/email/email_routes.py:7294`
- `routes/email/email_routes.py:7491`
- `routes/email/email_routes.py:7746`
- `routes/email/email_routes.py:7812`
- `tests/test_email_ownerless_account_owner_scope.py:61`
- `tests/test_email_ownerless_account_owner_scope.py:70`
- `tests/test_email_ownerless_account_owner_scope.py:80`
- `tests/test_email_ownerless_account_owner_scope.py:89`

## `_account_visible_to_owner` — function, line 617
- **called from:**
- `mcp_servers/email_server.py:146`
- `routes/email/email_helpers.py:603`
- `routes/email/email_helpers.py:1192`
- `routes/email/email_routes.py:265`
- `routes/email/email_routes.py:285`

## `_q` — function, line 636
- **called from:**
- `mcp_servers/email_server.py:750`
- `mcp_servers/email_server.py:864`
- `mcp_servers/email_server.py:1808`
- `mcp_servers/email_server.py:2287`
- `mcp_servers/email_server.py:2416`
- `mcp_servers/email_server.py:2718`
- `mcp_servers/email_server.py:2978`
- `mcp_servers/email_server.py:3145`
- `mcp_servers/email_server.py:3202`
- `mcp_servers/email_server.py:3240`
- `mcp_servers/email_server.py:3285`
- `mcp_servers/email_server.py:3295`
- `mcp_servers/email_server.py:3309`
- `mcp_servers/email_server.py:3319`
- `mcp_servers/email_server.py:3334`
- `mcp_servers/email_server.py:3362`
- `mcp_servers/email_server.py:3374`
- `mcp_servers/email_server.py:3384`
- `mcp_servers/email_server.py:3562`
- `routes/document/document_routes.py:1993`
- `routes/email/email_helpers.py:1576`
- `routes/email/email_helpers.py:1582`
- `routes/email/email_helpers.py:1858`
- `routes/email/email_helpers.py:2035`
- `routes/email/email_pollers.py:682`
- `routes/email/email_pollers.py:690`
- `routes/email/email_pollers.py:820`
- `routes/email/email_pollers.py:1673`
- `routes/email/email_routes.py:1502`
- `routes/email/email_routes.py:1505`
- `routes/email/email_routes.py:1520`
- `routes/email/email_routes.py:2387`
- `routes/email/email_routes.py:2391`
- `routes/email/email_routes.py:2848`
- `routes/email/email_routes.py:3157`
- `routes/email/email_routes.py:3254`
- `routes/email/email_routes.py:3326`
- `routes/email/email_routes.py:3364`
- `routes/email/email_routes.py:3377`
- `routes/email/email_routes.py:3455`
- `routes/email/email_routes.py:3620`
- `routes/email/email_routes.py:3624`
- `routes/email/email_routes.py:3754`
- `routes/email/email_routes.py:3761`
- `routes/email/email_routes.py:3775`
- `routes/email/email_routes.py:3974`
- `routes/email/email_routes.py:4108`
- `routes/email/email_routes.py:4140`
- `routes/email/email_routes.py:4167`
- `routes/email/email_routes.py:4299`
- `routes/email/email_routes.py:4467`
- `routes/email/email_routes.py:4594`
- `routes/email/email_routes.py:4772`
- `routes/email/email_routes.py:4824`
- `routes/email/email_routes.py:5185`
- `routes/email/email_routes.py:5207`
- `routes/email/email_routes.py:5227`
- `routes/email/email_routes.py:5245`
- `routes/email/email_routes.py:5265`
- `routes/email/email_routes.py:5288`
- … +29 more (grep the name in repo)

## `_attach_compose_uploads` — function, line 644
- **called from:**
- `routes/email/email_pollers.py:1660`
- `routes/email/email_routes.py:5919`
- `routes/email/email_routes.py:6220`
- `routes/email/email_routes.py:6415`

## `_cleanup_compose_uploads` — function, line 671
- **called from:**
- `routes/email/email_pollers.py:1677`
- `routes/email/email_routes.py:5925`
- `routes/email/email_routes.py:6369`

## `email_translation_body_hash` — function, line 705
- **called from:**
- `routes/email/email_routes.py:6720`
- `src/builtin_actions.py:1389`

## `_email_cache_owner_clause` — function, line 711
- **called from:**
- `routes/email/email_pollers.py:338`
- `routes/email/email_pollers.py:715`
- `routes/email/email_routes.py:2744`
- `routes/email/email_routes.py:2788`
- `routes/email/email_routes.py:3871`
- `routes/email/email_routes.py:6723`
- `routes/email/email_routes.py:6898`
- `routes/task/task_routes.py:680`
- `src/builtin_actions.py:1254`
- `src/builtin_actions.py:1824`

## `_ensure_owner_scoped_email_cache_table` — function, line 718
- **called from:**
- `routes/email/email_helpers.py:854`
- `routes/email/email_helpers.py:869`
- `routes/email/email_helpers.py:881`
- `routes/email/email_helpers.py:967`
- `routes/email/email_helpers.py:978`

## `_ensure_sender_signatures_table` — function, line 765
- **called from:**
- `routes/email/email_helpers.py:1130`

## `attachment_extract_dir` — function, line 814
- **called from:**
- `routes/email/email_routes.py:4129`
- `routes/email/email_routes.py:4148`
- `routes/email/email_routes.py:4180`
- `routes/email/email_routes.py:4320`
- `routes/email/email_routes.py:4793`
- `routes/email/email_routes.py:4831`
- `routes/email/email_routes.py:5178`
- `routes/email/email_routes.py:5192`
- `routes/email/email_routes.py:5846`
- `tests/test_codeql_python_residual_followup.py:220`
- `tests/test_codeql_python_residual_followup.py:221`
- `tests/test_codeql_python_residual_followup.py:222`
- `tests/test_codeql_python_residual_followup.py:223`

## `_init_scheduled_db` — function, line 831
- **called from:**
- `routes/email/email_helpers.py:1135`
- `src/builtin_actions.py:3128`
- `tests/test_builtin_actions_owner_scope.py:145`
- `tests/test_email_list_stale_while_revalidate.py:155`
- `tests/test_email_list_stale_while_revalidate.py:216`
- `tests/test_email_owner_scope.py:79`
- `tests/test_email_owner_scope.py:151`
- `tests/test_email_owner_scope.py:193`
- `tests/test_email_owner_scope.py:230`
- `tests/test_email_owner_scope.py:276`
- `tests/test_email_owner_scope.py:325`
- `tests/test_email_owner_scope.py:392`
- `tests/test_email_owner_scope.py:459`
- `tests/test_email_owner_scope.py:502`
- `tests/test_email_owner_scope.py:550`
- `tests/test_email_owner_scope.py:598`
- `tests/test_email_read_mark_seen.py:66`
- `tests/test_email_summary_llm.py:248`
- `tests/test_email_summary_llm.py:378`
- `tests/test_schedule_email_offset_normalization.py:33`
- `tests/test_scheduled_poll_race.py:31`

## `_load_settings` — function, line 1138
- **called from:**
- `routes/auth_routes.py:780`
- `routes/auth_routes.py:795`
- `routes/auth_routes.py:986`
- `routes/contacts/contacts_routes.py:52`
- `routes/contacts/contacts_routes.py:1000`
- `routes/email/email_helpers.py:1240`
- `routes/email/email_pollers.py:504`
- `routes/email/email_pollers.py:526`
- `routes/email/email_pollers.py:640`
- `routes/email/email_pollers.py:1576`
- `routes/email/email_routes.py:6573`
- `routes/email/email_routes.py:6930`
- `routes/email/email_routes.py:7219`
- `routes/email/email_routes.py:7231`
- `routes/email/email_routes.py:7257`
- `routes/email/email_routes.py:7304`
- `routes/model_routes.py:184`
- `routes/model_routes.py:2365`
- `routes/model_routes.py:2799`
- `routes/model_routes.py:2967`
- `routes/model_routes.py:2971`
- `routes/model_routes.py:3108`
- `routes/model_routes.py:3128`
- `services/stt/stt_service.py:42`
- `services/stt/stt_service.py:66`
- `services/stt/stt_service.py:157`
- `services/stt/stt_service.py:177`
- `services/tts/tts_service.py:66`
- `services/tts/tts_service.py:200`
- `services/tts/tts_service.py:254`
- `src/agent_loop.py:14918`
- `src/agent_loop.py:15156`
- `src/builtin_actions.py:3583`
- `tests/test_carddav_password_encryption.py:39`
- `tests/test_carddav_password_encryption.py:145`
- `tests/test_carddav_password_encryption.py:158`
- `tests/test_carddav_password_encryption.py:162`

## `_save_settings` — function, line 1144
- **called from:**
- `routes/auth_routes.py:829`
- `routes/contacts/contacts_routes.py:1014`
- `routes/email/email_pollers.py:514`
- `routes/email/email_pollers.py:532`
- `routes/email/email_routes.py:6575`
- `routes/email/email_routes.py:7233`
- `routes/email/email_routes.py:7314`
- `routes/model_routes.py:193`
- `routes/model_routes.py:2387`
- `routes/model_routes.py:2974`
- `routes/model_routes.py:3130`
- `src/builtin_actions.py:3594`
- `tests/test_carddav_password_encryption.py:43`
- `tests/test_carddav_password_encryption.py:143`
- `tests/test_carddav_password_encryption.py:146`
- `tests/test_carddav_password_encryption.py:160`
- `tests/test_carddav_password_encryption.py:164`

## `_get_email_config` — function, line 1149
- **called from:**
- `routes/email/email_helpers.py:1280`
- `routes/email/email_helpers.py:1285`
- `routes/email/email_helpers.py:1354`
- `routes/email/email_pollers.py:433`
- `routes/email/email_pollers.py:755`
- `routes/email/email_pollers.py:1367`
- `routes/email/email_pollers.py:1634`
- `routes/email/email_routes.py:308`
- `routes/email/email_routes.py:1456`
- `routes/email/email_routes.py:1472`
- `routes/email/email_routes.py:5470`
- `routes/email/email_routes.py:6398`
- `routes/email/email_routes.py:7246`
- `routes/note/note_routes.py:316`
- `routes/note/note_routes.py:329`
- `src/task_scheduler.py:2399`
- `tests/test_email_ownerless_account_owner_scope.py:105`
- `tests/test_email_ownerless_account_owner_scope.py:116`

## `_owner_or_matching_legacy_account` — function, line 1171
- **called from:**
- `routes/email/email_helpers.py:1198`
- `routes/email/email_helpers.py:1202`

## `_list_email_accounts` — function, line 1267
- **called from:**
- `src/service_health.py:452`

## `_coerce_imap_timeout_seconds` — function, line 1290
- **called from:**
- `routes/email/email_helpers.py:1298`
- `tests/test_email_imap_timeout.py:53`
- `tests/test_email_imap_timeout.py:54`
- `tests/test_email_imap_timeout.py:55`
- `tests/test_email_imap_timeout.py:56`

## `_open_imap_connection` — function, line 1301
- **called from:**
- `routes/email/email_helpers.py:1370`
- `routes/email/email_routes.py:7627`
- `tests/test_codeql_python_residual_followup.py:140`
- `tests/test_email_imap_timeout.py:66`
- `tests/test_email_imap_timeout.py:81`
- `tests/test_imap_leak_fixes.py:288`

## `_imap_connect` — function, line 1346
- **called from:**
- `mcp_servers/email_server.py:748`
- `mcp_servers/email_server.py:862`
- `mcp_servers/email_server.py:1807`
- `mcp_servers/email_server.py:2282`
- `mcp_servers/email_server.py:2415`
- `mcp_servers/email_server.py:2715`
- `mcp_servers/email_server.py:2977`
- `mcp_servers/email_server.py:3144`
- `mcp_servers/email_server.py:3201`
- `mcp_servers/email_server.py:3237`
- `mcp_servers/email_server.py:3282`
- `mcp_servers/email_server.py:3360`
- `mcp_servers/email_server.py:3373`
- `mcp_servers/email_server.py:3561`
- `routes/email/email_helpers.py:1446`
- `routes/email/email_helpers.py:1575`
- `routes/email/email_helpers.py:1853`
- `routes/email/email_helpers.py:2032`
- `routes/email/email_pollers.py:671`
- `routes/email/email_pollers.py:704`
- `routes/email/email_routes.py:1788`
- `src/builtin_actions.py:1361`
- `src/builtin_actions.py:1772`
- `src/builtin_actions.py:1863`
- `src/builtin_actions.py:2039`
- `src/builtin_actions.py:2806`
- `src/service_health.py:331`
- `tests/test_email_account_host_ssrf.py:330`
- `tests/test_email_oauth.py:795`
- `tests/test_email_oauth.py:823`
- `tests/test_email_send_only_no_inbox.py:52`
- `tests/test_email_send_only_no_inbox.py:73`
- `tests/test_imap_leak_fixes.py:262`
- `tests/test_imap_leak_fixes.py:325`
- `tests/test_imap_leak_fixes.py:346`

## `_imap` — function, line 1408
- decorator: `contextmanager`
- **called from:**
- `routes/document/document_routes.py:1992`
- `routes/email/email_helpers.py:1993`
- `routes/email/email_pollers.py:1671`
- `routes/email/email_routes.py:2847`
- `routes/email/email_routes.py:3156`
- `routes/email/email_routes.py:3253`
- `routes/email/email_routes.py:3325`
- `routes/email/email_routes.py:3363`
- `routes/email/email_routes.py:3376`
- `routes/email/email_routes.py:3454`
- `routes/email/email_routes.py:3599`
- `routes/email/email_routes.py:3747`
- `routes/email/email_routes.py:3973`
- `routes/email/email_routes.py:4107`
- `routes/email/email_routes.py:4139`
- `routes/email/email_routes.py:4166`
- `routes/email/email_routes.py:4298`
- `routes/email/email_routes.py:4466`
- `routes/email/email_routes.py:4593`
- `routes/email/email_routes.py:4771`
- `routes/email/email_routes.py:4823`
- `routes/email/email_routes.py:5184`
- `routes/email/email_routes.py:5206`
- `routes/email/email_routes.py:5226`
- `routes/email/email_routes.py:5244`
- `routes/email/email_routes.py:5264`
- `routes/email/email_routes.py:5287`
- `routes/email/email_routes.py:5330`
- `routes/email/email_routes.py:5363`
- `routes/email/email_routes.py:5485`
- `routes/email/email_routes.py:5540`
- `routes/email/email_routes.py:5581`
- `routes/email/email_routes.py:5626`
- `routes/email/email_routes.py:5642`
- `routes/email/email_routes.py:5839`
- `routes/email/email_routes.py:6108`
- `routes/email/email_routes.py:6287`
- `routes/email/email_routes.py:6434`
- `routes/email/email_routes.py:6487`
- `routes/email/email_routes.py:6612`

## `_decode_header` — function, line 1456
- **called from:**
- `mcp_servers/email_server.py:609`
- `mcp_servers/email_server.py:611`
- `mcp_servers/email_server.py:612`
- `mcp_servers/email_server.py:1862`
- `mcp_servers/email_server.py:1863`
- `mcp_servers/email_server.py:2302`
- `mcp_servers/email_server.py:2303`
- `mcp_servers/email_server.py:2315`
- `mcp_servers/email_server.py:2316`
- `mcp_servers/email_server.py:2361`
- `mcp_servers/email_server.py:2391`
- `mcp_servers/email_server.py:2439`
- `mcp_servers/email_server.py:2440`
- `mcp_servers/email_server.py:2986`
- `mcp_servers/email_server.py:2992`
- `mcp_servers/email_server.py:3156`
- `mcp_servers/email_server.py:3162`
- `routes/document/document_routes.py:1998`
- `routes/document/document_routes.py:2002`
- `routes/email/email_helpers.py:1624`
- `routes/email/email_helpers.py:1684`
- `routes/email/email_helpers.py:1748`
- `routes/email/email_helpers.py:1900`
- `routes/email/email_helpers.py:2019`
- `routes/email/email_helpers.py:2055`
- `routes/email/email_helpers.py:2056`
- `routes/email/email_pollers.py:95`
- `routes/email/email_pollers.py:840`
- `routes/email/email_pollers.py:841`
- `routes/email/email_pollers.py:879`
- `routes/email/email_pollers.py:880`
- `routes/email/email_routes.py:715`
- `routes/email/email_routes.py:717`
- `routes/email/email_routes.py:718`
- `routes/email/email_routes.py:860`
- `routes/email/email_routes.py:861`
- `routes/email/email_routes.py:865`
- `routes/email/email_routes.py:866`
- `routes/email/email_routes.py:2865`
- `routes/email/email_routes.py:2866`
- `routes/email/email_routes.py:3810`
- `routes/email/email_routes.py:3811`
- `routes/email/email_routes.py:3812`
- `routes/email/email_routes.py:3813`
- `routes/email/email_routes.py:4931`
- `routes/email/email_routes.py:4932`
- `routes/email/email_routes.py:4933`
- `routes/email/email_routes.py:4934`
- `routes/email/email_routes.py:6127`
- `src/builtin_actions.py:1382`
- `src/builtin_actions.py:1383`
- `src/builtin_actions.py:2053`
- `src/builtin_actions.py:2054`
- `src/builtin_actions.py:2907`
- `src/builtin_actions.py:2908`
- `tests/test_email_decode_header.py:26`
- `tests/test_email_decode_header.py:32`
- `tests/test_email_decode_header.py:38`
- `tests/test_email_decode_header.py:42`
- `tests/test_email_decode_header.py:46`
- … +11 more (grep the name in repo)

## `_detect_sent_folder` — function, line 1483
- **called from:**
- `mcp_servers/email_server.py:2717`
- `routes/email/email_pollers.py:1672`
- `routes/email/email_routes.py:5486`
- `routes/email/email_routes.py:6288`
- `routes/email/email_routes.py:6488`

## `_detect_drafts_folder` — function, line 1518
- **called from:**
- `routes/email/email_routes.py:6435`

## `_detect_spam_folder` — function, line 1546
- **called from:**
- `routes/email/email_pollers.py:759`

## `_imap_move` — function, line 1571
- **called from:**
- `routes/email/email_pollers.py:1494`
- `tests/test_imap_move_uid.py:49`

## `_extract_attachment_text` — function, line 1599
- **called from:**
- `routes/email/email_helpers.py:1906`
- `routes/email/email_pollers.py:906`
- `routes/email/email_routes.py:6619`

## `_list_attachments_from_msg` — function, line 1667
- **called from:**
- `mcp_servers/email_server.py:2444`
- `routes/email/email_helpers.py:1728`
- `routes/email/email_routes.py:2868`
- `routes/email/email_routes.py:3823`
- `routes/email/email_routes.py:4114`
- `routes/email/email_routes.py:4174`
- `routes/email/email_routes.py:4317`
- `routes/email/email_routes.py:4937`

## `_is_likely_signature_image_attachment` — function, line 1711
- **called from:**
- `routes/email/email_helpers.py:1727`
- `routes/email/email_routes.py:1414`
- `routes/email/email_routes.py:2869`
- `routes/email/email_routes.py:4175`
- `routes/email/email_routes.py:4318`

## `_has_visible_attachments` — function, line 1724
- **called from:**
- `routes/email/email_routes.py:3842`
- `tests/test_email_attachment_search.py:50`
- `tests/test_email_attachment_search.py:72`

## `_extract_attachment_to_disk` — function, line 1732
- **called from:**
- `mcp_servers/email_server.py:3574`
- `routes/email/email_routes.py:4149`
- `routes/email/email_routes.py:4188`
- `routes/email/email_routes.py:4325`
- `routes/email/email_routes.py:4794`
- `routes/email/email_routes.py:4832`
- `routes/email/email_routes.py:5193`
- `routes/email/email_routes.py:5847`

## `_extract_html` — function, line 1773
- **called from:**
- `routes/email/email_routes.py:3819`
- `tests/test_email_mime_body_decoding.py:74`

## `_extract_text` — function, line 1790
- **called from:**
- `mcp_servers/email_server.py:2443`
- `routes/email/email_helpers.py:1902`
- `routes/email/email_helpers.py:2058`
- `routes/email/email_pollers.py:898`
- `routes/email/email_routes.py:3818`
- `routes/email/email_routes.py:4936`
- `src/builtin_actions.py:1384`

## `_fetch_sender_thread_context` — function, line 1823
- **called from:**
- `tests/test_imap_leak_fixes.py:51`
- `tests/test_imap_leak_fixes.py:68`

## `_pre_retrieve_context` — function, line 1934
- **called from:**
- `tests/test_imap_leak_fixes.py:97`

## `SendEmailRequest` — class, line 2129
- **called from:**
- `routes/codex_routes.py:417`
- `routes/codex_routes.py:430`

## `ExtractStyleRequest` — class, line 2158
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
