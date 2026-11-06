# `src/chatgpt_subscription.py` — definitions & call sites

48 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_database_handles` — function, line 47
- **called from:**
- `src/chatgpt_subscription.py:410`
- `src/chatgpt_subscription.py:454`
- `src/chatgpt_subscription.py:759`

## `_refresh_lock_for` — function, line 52
- **called from:**
- `src/chatgpt_subscription.py:424`

## `ChatGPTSubscriptionError` — class, line 61
- **called from:**
- `src/chatgpt_subscription.py:309`
- `src/chatgpt_subscription.py:317`
- `src/chatgpt_subscription.py:319`
- `src/chatgpt_subscription.py:332`

## `ChatGPTSubscriptionReauthRequired` — class, line 65
- **called from:**
- `src/chatgpt_subscription.py:308`
- `src/chatgpt_subscription.py:366`
- `src/chatgpt_subscription.py:373`
- `src/chatgpt_subscription.py:386`
- `tests/test_chatgpt_subscription_usage.py:296`

## `ChatGPTSubscriptionRateLimited` — class, line 69
- **called from:**
- `src/chatgpt_subscription.py:304`

## `ChatGPTSubscriptionAuthNotFound` — class, line 73
- **called from:**
- `routes/chatgpt_subscription_routes.py:137`
- `routes/chatgpt_subscription_routes.py:171`
- `src/chatgpt_subscription.py:420`
- `src/chatgpt_subscription.py:757`
- `src/chatgpt_subscription.py:763`
- `tests/test_chatgpt_subscription_usage.py:304`

## `is_chatgpt_subscription_base` — function, line 77
- **called from:**
- `core/session_manager.py:933`
- `routes/chat_helpers.py:1042`
- `routes/chat_routes.py:2075`
- `routes/chat_routes.py:2110`
- `routes/model_routes.py:1455`
- `routes/model_routes.py:1474`
- `routes/model_routes.py:1697`
- `routes/model_routes.py:2332`
- `routes/model_routes.py:2943`
- `routes/session_routes.py:673`
- `src/llm_core.py:1162`
- `src/llm_core.py:1397`

## `chatgpt_headers` — function, line 91
- **called from:**
- `src/chatgpt_subscription.py:249`
- `src/endpoint_resolver.py:429`

## `normalize_account_label` — function, line 108
- **called from:**
- `routes/chatgpt_subscription_routes.py:130`
- `routes/chatgpt_subscription_routes.py:233`

## `endpoint_name_for_label` — function, line 128
- **called from:**
- `routes/chatgpt_subscription_routes.py:151`
- `routes/chatgpt_subscription_routes.py:162`
- `routes/chatgpt_subscription_routes.py:179`
- `routes/chatgpt_subscription_routes.py:187`

## `account_label_from_name` — function, line 136
- **called from:**
- `routes/chatgpt_subscription_routes.py:49`
- `routes/chatgpt_subscription_routes.py:51`
- `routes/model_routes.py:1476`

## `labels_conflict` — function, line 146
- **called from:**
- `routes/chatgpt_subscription_routes.py:68`

## `_extract_reasoning_levels` — function, line 193
- **called from:**
- `src/chatgpt_subscription.py:269`

## `get_chatgpt_model_metadata` — function, line 208
- **called from:**
- `routes/chat_routes.py:2468`
- `routes/model_routes.py:1719`
- `routes/session_routes.py:778`
- `src/chatgpt_subscription.py:234`
- `tests/test_chatgpt_reasoning_and_grouping.py:146`
- `tests/test_chatgpt_reasoning_and_grouping.py:153`
- `tests/test_chatgpt_reasoning_and_grouping.py:163`
- `tests/test_chatgpt_reasoning_and_grouping.py:224`
- `tests/test_chatgpt_reasoning_and_grouping.py:230`

## `validate_reasoning_effort` — function, line 226
- **called from:**
- `routes/chat_routes.py:2471`
- `routes/chat_routes.py:3010`
- `routes/history/history_routes.py:268`
- `src/utility_effort.py:80`
- `src/utility_effort.py:87`
- `src/utility_effort.py:127`
- `tests/test_chatgpt_reasoning_and_grouping.py:137`
- `tests/test_chatgpt_reasoning_and_grouping.py:138`
- `tests/test_chatgpt_reasoning_and_grouping.py:139`
- `tests/test_chatgpt_reasoning_and_grouping.py:140`
- `tests/test_chatgpt_reasoning_and_grouping.py:141`
- `tests/test_chatgpt_reasoning_and_grouping.py:142`
- `tests/test_chatgpt_reasoning_and_grouping.py:143`
- `tests/test_utility_reasoning_effort.py:133`
- `tests/test_utility_reasoning_effort.py:134`
- `tests/test_utility_reasoning_effort.py:135`

## `fetch_available_models` — function, line 243
- **called from:**
- `routes/chat_routes.py:2138`
- `routes/chatgpt_subscription_routes.py:127`
- `routes/model_routes.py:1024`

## `_raise_for_oauth_response` — function, line 289
- **called from:**
- `src/chatgpt_subscription.py:313`
- `tests/test_chatgpt_subscription_usage.py:248`

## `_json_or_error` — function, line 312
- **called from:**
- `src/chatgpt_subscription.py:330`
- `src/chatgpt_subscription.py:348`
- `src/chatgpt_subscription.py:364`
- `src/chatgpt_subscription.py:384`

## `request_device_code` — function, line 323
- **called from:**
- `routes/chatgpt_subscription_routes.py:270`
- `routes/copilot_routes.py:108`
- `tests/test_copilot.py:159`

## `poll_device_auth` — function, line 339
- **called from:**
- `routes/chatgpt_subscription_routes.py:335`

## `exchange_authorization_code` — function, line 351
- **called from:**
- `routes/chatgpt_subscription_routes.py:344`

## `refresh_oauth_tokens` — function, line 370
- **called from:**
- `src/chatgpt_subscription.py:429`

## `_decode_jwt_payload` — function, line 390
- **called from:**
- `src/chatgpt_subscription.py:403`
- `src/chatgpt_subscription.py:468`

## `access_token_is_expiring` — function, line 401
- **called from:**
- `src/chatgpt_subscription.py:423`
- `src/chatgpt_subscription.py:428`

## `resolve_runtime_credentials` — function, line 409
- **called from:**
- `src/chatgpt_subscription.py:774`
- `src/endpoint_resolver.py:186`

## `find_owned_auth_session` — function, line 448
- **called from:**
- `routes/chatgpt_subscription_routes.py:135`
- `routes/chatgpt_subscription_routes.py:246`
- `routes/chatgpt_subscription_routes.py:322`
- `routes/chatgpt_subscription_routes.py:399`
- `src/chatgpt_subscription.py:762`

## `chatgpt_account_id_from_token` — function, line 465
- **called from:**
- `src/chatgpt_subscription.py:485`

## `usage_request_headers` — function, line 479
- **called from:**
- `src/chatgpt_subscription.py:668`

## `ChatGPTUsageUnavailable` — class, line 491
- **called from:**
- `routes/chatgpt_subscription_routes.py:451`
- `src/chatgpt_subscription.py:615`
- `src/chatgpt_subscription.py:666`
- `src/chatgpt_subscription.py:670`
- `src/chatgpt_subscription.py:672`
- `src/chatgpt_subscription.py:675`
- `src/chatgpt_subscription.py:681`
- `src/chatgpt_subscription.py:683`
- `src/chatgpt_subscription.py:685`
- `src/chatgpt_subscription.py:689`
- `src/chatgpt_subscription.py:691`
- `src/chatgpt_subscription.py:778`
- `src/chatgpt_subscription.py:780`
- `src/chatgpt_subscription.py:782`
- `tests/test_chatgpt_subscription_usage.py:334`

## `ChatGPTUsageUnavailable.__init__` — method, line 494
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

## `_coerce_number` — function, line 500
- **called from:**
- `src/chatgpt_subscription.py:513`
- `src/chatgpt_subscription.py:560`

## `_coerce_int` — function, line 512
- **called from:**
- `src/chatgpt_subscription.py:531`
- `src/chatgpt_subscription.py:565`
- `src/chatgpt_subscription.py:568`
- `src/chatgpt_subscription.py:570`
- `src/chatgpt_subscription.py:573`

## `_optional_str` — function, line 522
- **called from:**
- `src/chatgpt_subscription.py:634`
- `src/chatgpt_subscription.py:635`
- `src/chatgpt_subscription.py:641`
- `src/chatgpt_subscription.py:649`
- `src/chatgpt_subscription.py:651`
- `src/chatgpt_subscription.py:655`
- `src/chatgpt_subscription.py:656`

## `window_minutes_from_seconds` — function, line 529
- **called from:**
- `src/chatgpt_subscription.py:563`

## `friendly_window_name` — function, line 537
- **called from:**
- `src/chatgpt_subscription.py:578`
- `tests/test_chatgpt_subscription_usage.py:127`

## `normalize_usage_window` — function, line 551
- **called from:**
- `src/chatgpt_subscription.py:594`
- `tests/test_chatgpt_subscription_usage.py:214`

## `_normalize_rate_limit_details` — function, line 587
- **called from:**
- `src/chatgpt_subscription.py:618`
- `src/chatgpt_subscription.py:633`

## `normalize_usage_payload` — function, line 606
- **called from:**
- `src/chatgpt_subscription.py:784`
- `tests/test_chatgpt_subscription_usage.py:71`
- `tests/test_chatgpt_subscription_usage.py:100`
- `tests/test_chatgpt_subscription_usage.py:109`
- `tests/test_chatgpt_subscription_usage.py:116`
- `tests/test_chatgpt_subscription_usage.py:121`
- `tests/test_chatgpt_subscription_usage.py:222`

## `fetch_usage_payload` — function, line 663
- **called from:**
- `src/chatgpt_subscription.py:783`
- `tests/test_chatgpt_subscription_usage.py:148`
- `tests/test_chatgpt_subscription_usage.py:160`
- `tests/test_chatgpt_subscription_usage.py:168`
- `tests/test_chatgpt_subscription_usage.py:172`
- `tests/test_chatgpt_subscription_usage.py:176`
- `tests/test_chatgpt_subscription_usage.py:180`

## `UsageCache` — class, line 695
- **called from:**
- `src/chatgpt_subscription.py:737`
- `tests/test_chatgpt_subscription_usage.py:186`
- `tests/test_chatgpt_subscription_usage.py:199`
- `tests/test_chatgpt_subscription_usage.py:231`
- `tests/test_chatgpt_subscription_usage.py:254`
- `tests/test_chatgpt_subscription_usage.py:293`

## `UsageCache.__init__` — method, line 698
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

## `UsageCache.get` — method, line 705
- **called from:**
- `app.py:400`
- `app.py:424`
- `app.py:430`
- `app.py:457`
- `app.py:469`
- `app.py:511`
- `app.py:620`
- `app.py:553`
- `app.py:673`
- `app.py:976`
- `app.py:988`
- `app.py:992`
- `app.py:1000`
- `app.py:1004`
- `app.py:1008`
- `app.py:1012`
- `app.py:1016`
- `app.py:1020`
- `app.py:1024`
- `app.py:1029`
- `app.py:1035`
- `app.py:1045`
- `app.py:1054`
- `app.py:1066`
- `app.py:1067`
- `app.py:1068`
- `app.py:1068`
- `app.py:1070`
- `app.py:1070`
- `app.py:1074`
- `app.py:1095`
- `app.py:1086`
- `app.py:1097`
- `app.py:1270`
- `app.py:1273`
- `app.py:1273`
- `app.py:1274`
- `app.py:1275`
- `app.py:1280`
- `app.py:1280`
- `app.py:1301`
- `app.py:1335`
- `app.py:1349`
- `app.py:1390`
- `app.py:1393`
- `app.py:1408`
- `companion/pairing.py:116`
- `companion/pairing.py:126`
- `companion/pairing.py:173`
- `companion/pairing.py:177`
- `companion/routes.py:85`
- `companion/routes.py:97`
- `companion/routes.py:109`
- `companion/routes.py:168`
- `companion/routes.py:222`
- `core/auth.py:161`
- `core/auth.py:182`
- `core/auth.py:205`
- `core/auth.py:232`
- `core/auth.py:244`
- … +16891 more (grep the name in repo)

## `UsageCache.put` — method, line 717
- **called from:**
- `routes/auth_routes.py:349`
- `routes/auth_routes.py:363`
- `routes/auth_routes.py:382`
- `routes/auth_routes.py:660`
- `routes/auth_routes.py:712`
- `routes/auth_routes.py:938`
- `routes/calendar_routes.py:1085`
- `routes/calendar_routes.py:1424`
- `routes/calendar_routes.py:1555`
- `routes/contacts/contacts_routes.py:540`
- `routes/contacts/contacts_routes.py:630`
- `routes/contacts/contacts_routes.py:804`
- `routes/contacts/contacts_routes.py:998`
- `routes/contacts/contacts_routes.py:1037`
- `routes/document/document_routes.py:847`
- `routes/editor_draft_routes.py:192`
- `routes/email/email_routes.py:6860`
- `routes/email/email_routes.py:7222`
- `routes/email/email_routes.py:7280`
- `routes/email/email_routes.py:7487`
- `routes/gallery/gallery_routes.py:3014`
- `routes/memory/memory_routes.py:534`
- `routes/note/note_routes.py:709`
- `routes/prefs_routes.py:117`
- `routes/shell_routes.py:1275`
- `routes/shell_routes.py:1290`
- `routes/shell_routes.py:1292`
- `routes/skills_routes.py:420`
- `routes/skills_routes.py:828`
- `routes/task/task_routes.py:731`
- `routes/upload_routes.py:614`
- `services/shell/service.py:119`
- `services/shell/service.py:121`
- `src/agent_loop.py:25996`
- `src/agent_loop.py:26013`
- `src/agent_loop.py:34262`
- `src/agent_loop.py:34316`
- `src/agent_tools/filesystem_tools.py:128`
- `src/agent_tools/filesystem_tools.py:151`
- `src/agent_tools/filesystem_tools.py:158`
- `src/agent_tools/filesystem_tools.py:160`
- `src/agent_tools/filesystem_tools.py:163`
- `src/agent_tools/filesystem_tools.py:1124`
- `src/chatgpt_subscription.py:787`
- `tests/smoke/test_documents_smoke.py:29`
- `tests/smoke/test_notes_smoke.py:25`
- `tests/smoke/test_settings_smoke.py:17`
- `tests/test_admin_routes_auth_disabled.py:185`
- `tests/test_admin_routes_auth_disabled.py:199`
- `tests/test_admin_routes_auth_disabled.py:210`
- `tests/test_admin_routes_auth_disabled.py:211`
- `tests/test_admin_routes_auth_disabled.py:212`
- `tests/test_admin_routes_auth_disabled.py:213`
- `tests/test_admin_routes_auth_disabled.py:214`
- `tests/test_admin_routes_auth_disabled.py:288`
- `tests/test_admin_routes_auth_disabled.py:305`
- `tests/test_admin_routes_auth_disabled.py:310`
- `tests/test_chatgpt_subscription_usage.py:187`
- `tests/test_chatgpt_subscription_usage.py:201`
- `tests/test_chatgpt_subscription_usage.py:204`
- … +37 more (grep the name in repo)

## `UsageCache.invalidate` — method, line 728
- **called from:**
- `companion/routes.py:78`
- `routes/chatgpt_subscription_routes.py:212`
- `routes/model_routes.py:706`
- `src/agent_tools/web_tools.py:2710`
- `src/browser_identity.py:415`
- `src/browser_identity.py:469`
- `src/browser_identity.py:479`
- `src/browser_identity.py:597`
- `src/browser_identity.py:646`
- `src/chatgpt_subscription.py:772`
- `static/js/editor/render-cancellation.js:13`
- `static/js/galleryEditor.js:4011`
- `static/js/galleryEditor.js:14218`

## `UsageCache.clear` — method, line 732
- **called from:**
- `mcp_servers/email_server.py:117`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email/email_routes.py:1936`
- `routes/email/email_routes.py:1937`
- `routes/gallery/gallery_routes.py:109`
- `routes/gallery/gallery_routes.py:110`
- `routes/model_routes.py:1506`
- `routes/session_routes.py:1045`
- `routes/shell_routes.py:2077`
- `routes/shell_routes.py:2204`
- `scripts/diffusion_server.py:101`
- `scripts/odysseus_related_flow_audit.py:651`
- `services/search/core.py:986`
- `services/skills/agent_runner.py:52`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/agent_runtime/context_resolution.py:235`
- `src/agent_tools/filesystem_tools.py:645`
- `src/agent_tools/web_tools.py:2711`
- `src/chatgpt_subscription.py:734`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:4565`
- `src/llm_core.py:4566`
- `src/llm_core.py:4764`
- `src/llm_core.py:5124`
- `src/shutdown.py:34`
- `src/skill_index.py:116`
- `src/task_scheduler.py:581`
- `src/tool_index.py:881`
- `tests/cli/test_gallery_cli_tag_filters.py:37`
- `tests/conftest.py:400`
- `tests/smoke/stub_provider.py:69`
- `tests/test_admin_routes_auth_disabled.py:330`
- `tests/test_agent_editor_routes.py:606`
- `tests/test_agent_editor_routes.py:620`
- `tests/test_agent_editor_routes.py:1357`
- `tests/test_agent_state_dir_confinement.py:283`
- `tests/test_api_token_routes.py:160`
- `tests/test_background_tool_jobs.py:38`
- `tests/test_background_tool_jobs.py:87`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:109`
- `tests/test_browser_identity_transport.py:120`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:112`
- `tests/test_browser_resource_identity.py:113`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_context_resolution_route.py:90`
- `tests/test_editor_generation_model_routing.py:242`
- … +197 more (grep the name in repo)

## `get_account_usage` — function, line 740
- **called from:**
- `routes/chatgpt_subscription_routes.py:441`
- `tests/test_chatgpt_subscription_usage.py:234`
- `tests/test_chatgpt_subscription_usage.py:236`
- `tests/test_chatgpt_subscription_usage.py:237`
- `tests/test_chatgpt_subscription_usage.py:242`
- `tests/test_chatgpt_subscription_usage.py:270`
- `tests/test_chatgpt_subscription_usage.py:275`
- `tests/test_chatgpt_subscription_usage.py:279`
- `tests/test_chatgpt_subscription_usage.py:283`
- `tests/test_chatgpt_subscription_usage.py:300`
- `tests/test_chatgpt_subscription_usage.py:308`

## `to_http_exception` — function, line 793
- **called from:**
- `routes/chatgpt_subscription_routes.py:272`
- `routes/chatgpt_subscription_routes.py:354`

## `build_responses_input` — function, line 803
- **called from:**
- `src/llm_core.py:1630`
- `tests/test_chatgpt_zero_native_tools.py:225`
