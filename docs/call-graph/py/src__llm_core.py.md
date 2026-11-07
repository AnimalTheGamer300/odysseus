# `src/llm_core.py` — definitions & call sites

153 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_managed_stream_endpoint` — function, line 26
- **called from:**
- `src/llm_core.py:232`
- `src/llm_core.py:4337`

## `_normalize_usage_counts` — function, line 49
- **called from:**
- `src/agent_loop.py:22860`
- `src/agent_loop.py:28097`
- `src/llm_core.py:3569`
- `src/llm_core.py:3680`
- `src/llm_core.py:3851`
- `src/llm_core.py:4112`

## `_count` — function, line 52
- **called from:**
- `src/llm_core.py:65`
- `src/llm_core.py:66`
- `tests/test_manage_tasks_admin_action_policy.py:94`
- `tests/test_manage_tasks_admin_action_policy.py:101`

## `_normalize_http_status` — function, line 75
- **called from:**
- `routes/chat_routes.py:1291`
- `routes/chat_routes.py:5211`
- `src/agent_loop.py:22938`
- `src/agent_loop.py:27788`
- `src/llm_core.py:2892`
- `src/llm_core.py:4413`
- `src/llm_core.py:4867`

## `_local_model_gate_enabled` — function, line 96
- **called from:**
- `src/llm_core.py:121`

## `_local_model_gate_key` — function, line 100
- **called from:**
- `src/llm_core.py:125`
- `tests/test_review_model_gate.py:15`

## `_gate_workload` — function, line 108
- **called from:**
- `src/llm_core.py:127`

## `_local_model_slot` — function (async), line 113
- decorator: `asynccontextmanager`
- **called from:**
- `src/llm_core.py:3201`
- `src/llm_core.py:3356`
- `tests/test_email_summary_llm.py:156`
- `tests/test_email_summary_llm.py:177`
- `tests/test_email_summary_llm.py:209`
- `tests/test_email_summary_llm.py:216`
- `tests/test_email_summary_llm.py:222`
- `tests/test_review_model_gate.py:18`
- `tests/test_review_model_gate.py:21`

## `LLMConfig` — class, line 182
- **called from:**
- `src/config.py:126`

## `_FallbackIneligibleHTTPException` — class, line 200
- **called from:**
- `src/llm_core.py:2918`
- `src/llm_core.py:3265`
- `src/llm_core.py:3298`
- `src/llm_core.py:3309`
- `src/llm_core.py:3320`
- `src/llm_core.py:3333`

## `_call_timeout` — function, line 206
- **called from:**
- `src/llm_core.py:3195`
- `tests/test_llm_core_connect_timeout.py:26`
- `tests/test_llm_core_connect_timeout.py:46`

## `_stream_timeout` — function, line 211
- **called from:**
- `src/llm_core.py:3492`
- `tests/test_llm_core_connect_timeout.py:35`
- `tests/test_llm_core_connect_timeout.py:47`

## `_first_token_timeout` — function, line 216
- **called from:**
- `src/llm_core.py:3945`
- `tests/test_llm_core_streaming.py:254`
- `tests/test_llm_core_streaming.py:255`

## `_cache_header_identity` — function, line 238
- **called from:**
- `src/llm_core.py:285`

## `_get_cache_key` — function, line 257
- **called from:**
- `src/llm_core.py:2660`
- `src/llm_core.py:3059`
- `tests/test_llm_core_fallback.py:565`
- `tests/test_prompt_controls_regressions.py:56`
- `tests/test_prompt_controls_regressions.py:56`

## `_strip_visible_chat_template_artifacts` — function, line 353
- **called from:**
- `src/agent_loop.py:22914`
- `src/llm_core.py:4177`

## `_harmony_suffix_hold_len` — function, line 357
- **called from:**
- `src/llm_core.py:420`

## `_HarmonyStreamRouter` — class, line 367
- **called from:**
- `src/llm_core.py:3625`
- `src/llm_core.py:3904`

## `_HarmonyStreamRouter.__init__` — method, line 370
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

## `_HarmonyStreamRouter.feed` — method, line 376
- **called from:**
- `routes/email/email_routes.py:1712`
- `src/agent_tools/document_tools.py:771`
- `src/llm_core.py:3664`
- `src/llm_core.py:4192`
- `src/llm_core.py:4297`
- `src/llm_core.py:4302`
- `src/report_math.py:48`
- `tests/test_chat_attachment_picker.py:24`

## `_HarmonyStreamRouter.flush` — method, line 382
- **called from:**
- `core/atomic_io.py:43`
- `core/atomic_io.py:76`
- `core/atomic_io.py:97`
- `core/database.py:555`
- `routes/calendar_routes.py:331`
- `routes/calendar_routes.py:339`
- `routes/email/email_routes.py:7545`
- `scripts/cook_sft_alex_conversations.py:235`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/eval_exact_file_routing.py:158`
- `scripts/eval_odysseus_tool_use.py:658`
- `scripts/eval_odysseus_tool_use.py:661`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `scripts/run_sft_environment_expansion.py:517`
- `src/agent_tools/filesystem_tools.py:615`
- `src/api_key_manager.py:94`
- `src/browser_identity.py:254`
- `src/containment_worker.py:80`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3675`
- `src/llm_core.py:3693`
- `src/llm_core.py:3977`
- `src/llm_core.py:4314`
- `src/task_scheduler.py:2849`
- `src/upload_handler.py:799`
- `tests/smoke/stub_provider.py:136`
- `tests/test_atomic_io.py:101`
- `tests/test_codeql_python_residual_closure.py:140`
- `tests/test_codeql_python_residual_closure.py:149`
- `tests/test_codeql_python_residual_closure.py:155`
- `tests/test_codeql_python_residual_closure.py:157`
- `tests/test_daily_brief_local_calendar.py:56`
- `tests/test_launcher.py:24`
- `static/js/chat.js:4225`
- `static/js/emailLibrary/bodyRender.js:746`
- `static/js/emailLibrary/bodyRender.js:752`
- `static/js/emailLibrary/bodyRender.js:757`
- `static/js/liveThinkingThrottle.js:18`
- `static/js/liveThinkingThrottle.js:191`

## `_HarmonyStreamRouter._append_text` — method, line 385
- **called from:**
- `src/llm_core.py:416`
- `src/llm_core.py:423`

## `_HarmonyStreamRouter._handle_marker` — method, line 397
- **called from:**
- `src/llm_core.py:417`

## `_HarmonyStreamRouter._drain` — method, line 410
- **called from:**
- `src/agent_runs.py:213`
- `src/containment.py:1109`
- `src/containment.py:1140`
- `src/llm_core.py:380`
- `src/llm_core.py:383`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_model_routes.py:1169`
- `tests/test_model_routes.py:1206`

## `_stream_delta_event` — function, line 427
- **called from:**
- `src/llm_core.py:3661`
- `src/llm_core.py:3665`
- `src/llm_core.py:3676`
- `src/llm_core.py:3694`
- `src/llm_core.py:3923`
- `src/llm_core.py:3931`
- `src/llm_core.py:4175`

## `_is_numeric_token` — function, line 442
- **called from:**
- `src/llm_core.py:507`
- `src/llm_core.py:512`
- `src/llm_core.py:519`
- `src/llm_core.py:557`

## `_DegenerateStreamGuard` — class, line 448
- **called from:**
- `src/llm_core.py:3498`
- `tests/test_llm_core_fallback.py:1047`
- `tests/test_llm_core_fallback.py:1055`
- `tests/test_llm_core_fallback.py:1065`
- `tests/test_llm_core_fallback.py:1074`
- `tests/test_llm_core_fallback.py:1085`
- `tests/test_llm_core_fallback.py:1120`
- `tests/test_llm_core_fallback.py:1128`
- `tests/test_llm_core_fallback.py:1140`
- `tests/test_llm_core_fallback.py:1158`
- `tests/test_llm_core_fallback.py:1176`
- `tests/test_llm_core_fallback.py:1196`

## `_DegenerateStreamGuard.__init__` — method, line 459
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

## `_DegenerateStreamGuard.check` — method, line 469
- **called from:**
- `routes/auth_routes.py:152`
- `routes/auth_routes.py:171`
- `routes/auth_routes.py:191`
- `src/llm_core.py:3551`
- `src/llm_core.py:4171`
- `src/llm_core.py:4180`
- `tests/markdown_browser_check.py:80`
- `tests/markdown_browser_check.py:82`
- `tests/markdown_browser_check.py:84`
- `tests/markdown_browser_check.py:86`
- `tests/markdown_browser_check.py:88`
- `tests/markdown_browser_check.py:90`
- `tests/markdown_browser_check.py:92`
- `tests/markdown_browser_check.py:95`
- `tests/markdown_browser_check.py:100`
- `tests/markdown_browser_check.py:101`
- `tests/markdown_browser_check.py:104`
- `tests/markdown_browser_check.py:117`
- `tests/markdown_browser_check.py:118`
- `tests/markdown_browser_check.py:126`
- `tests/test_draft_contact_evidence.py:17`
- `tests/test_draft_contact_evidence.py:21`
- `tests/test_draft_contact_evidence.py:25`
- `tests/test_draft_contact_evidence.py:33`
- `tests/test_llm_core_fallback.py:1048`
- `tests/test_llm_core_fallback.py:1061`
- `tests/test_llm_core_fallback.py:1067`
- `tests/test_llm_core_fallback.py:1077`
- `tests/test_llm_core_fallback.py:1078`
- `tests/test_llm_core_fallback.py:1091`
- `tests/test_llm_core_fallback.py:1122`
- `tests/test_llm_core_fallback.py:1130`
- `tests/test_llm_core_fallback.py:1144`
- `tests/test_llm_core_fallback.py:1162`
- `tests/test_llm_core_fallback.py:1180`
- `tests/test_llm_core_fallback.py:1201`
- `tests/test_rate_limiter.py:11`
- `tests/test_rate_limiter.py:12`
- `tests/test_rate_limiter.py:13`
- `tests/test_rate_limiter.py:18`
- `tests/test_rate_limiter.py:19`
- `tests/test_rate_limiter.py:23`
- `tests/test_rate_limiter.py:24`
- `tests/test_rate_limiter.py:25`
- `tests/test_rate_limiter.py:26`
- `tests/test_rate_limiter.py:32`
- `tests/test_rate_limiter.py:33`
- `tests/test_rate_limiter.py:35`
- `tests/test_rate_limiter.py:42`
- `tests/test_rate_limiter.py:45`
- `static/js/editor/text-layer.js:55`
- `static/js/skills.js:1632`

## `_model_activity_key` — function, line 575
- **called from:**
- `src/llm_core.py:608`
- `src/llm_core.py:612`

## `_same_model_identity` — function, line 578
- **called from:**
- `src/llm_core.py:589`
- `src/llm_core.py:599`
- `src/llm_core.py:4071`
- `src/llm_core.py:4141`

## `_reported_model_name` — function, line 581
- **called from:**
- `src/llm_core.py:588`
- `src/llm_core.py:596`
- `src/llm_core.py:3538`
- `src/llm_core.py:3650`
- `src/llm_core.py:3777`

## `_model_actual_event` — function, line 586
- **called from:**
- `src/llm_core.py:3544`
- `src/llm_core.py:3654`
- `src/llm_core.py:3785`

## `_annotate_usage_model` — function, line 594
- **called from:**
- `src/llm_core.py:3579`
- `src/llm_core.py:3685`
- `src/llm_core.py:3856`

## `note_model_activity` — function, line 604
- **called from:**
- `src/llm_core.py:2712`
- `src/llm_core.py:3202`
- `src/llm_core.py:3497`

## `seconds_since_model_activity` — function, line 610
- **called from:**
- `src/builtin_actions.py:2293`

## `_host_key` — function, line 617
- **called from:**
- `src/llm_core.py:623`
- `src/llm_core.py:638`
- `src/llm_core.py:648`
- `src/llm_core.py:3193`
- `src/llm_core.py:3275`
- `src/llm_core.py:3495`
- `src/llm_core.py:3606`
- `src/llm_core.py:3700`
- `src/llm_core.py:3877`
- `src/llm_core.py:4325`
- `src/llm_core.py:4341`
- `src/llm_core.py:4498`
- `tests/test_llm_core_concurrency.py:51`

## `_is_host_dead` — function, line 622
- **called from:**
- `src/llm_core.py:3192`
- `src/llm_core.py:3494`

## `_mark_host_dead` — function, line 633
- **called from:**
- `src/llm_core.py:3270`
- `src/llm_core.py:3603`
- `src/llm_core.py:3697`
- `src/llm_core.py:3874`
- `src/llm_core.py:4322`
- `tests/test_llm_core_concurrency.py:68`

## `_clear_host_dead` — function, line 647
- **called from:**
- `src/llm_core.py:3217`
- `src/llm_core.py:3510`
- `src/llm_core.py:3631`
- `src/llm_core.py:3730`
- `src/llm_core.py:3938`

## `_get_http_client` — function, line 660
- **called from:**
- `src/llm_core.py:3203`
- `src/llm_core.py:3508`
- `src/llm_core.py:3629`
- `src/llm_core.py:3728`
- `src/llm_core.py:3935`

## `_get_cached_response` — function, line 670
- **called from:**
- `src/llm_core.py:2666`
- `src/llm_core.py:3065`

## `_get_cached_response_model` — function, line 675
- **called from:**
- `src/llm_core.py:3072`

## `_set_cached_response` — function, line 681
- **called from:**
- `src/llm_core.py:2736`
- `src/llm_core.py:3105`
- `src/llm_core.py:3132`
- `src/llm_core.py:3254`
- `tests/test_llm_core_concurrency.py:38`

## `_is_ollama_native_url` — function, line 711
- **called from:**
- `scripts/dump_agent_prompt.py:89`
- `src/agent_loop.py:8733`
- `src/llm_core.py:1143`
- `src/llm_core.py:1415`
- `tests/test_ollama_port_detection.py:32`
- `tests/test_ollama_port_detection.py:35`
- `tests/test_ollama_port_detection.py:38`
- `tests/test_ollama_port_detection.py:41`
- `tests/test_ollama_port_detection.py:44`
- `tests/test_ollama_port_detection.py:47`
- `tests/test_ollama_port_detection.py:50`
- `tests/test_ollama_port_detection.py:59`
- `tests/test_ollama_port_detection.py:62`
- `tests/test_ollama_port_detection.py:65`
- `tests/test_ollama_port_detection.py:68`
- `tests/test_ollama_port_detection.py:71`
- `tests/test_ollama_port_detection.py:74`
- `tests/test_tool_support_heuristic.py:43`

## `_is_ollama_openai_compat_url` — function, line 728
- **called from:**
- `scripts/dump_agent_prompt.py:90`
- `scripts/dump_agent_prompt.py:329`
- `src/agent_loop.py:8734`
- `src/llm_core.py:3172`
- `src/llm_core.py:3462`
- `tests/test_llm_core_ollama_thinking.py:79`
- `tests/test_llm_core_ollama_thinking.py:82`
- `tests/test_llm_core_ollama_thinking.py:85`
- `tests/test_llm_core_ollama_thinking.py:88`
- `tests/test_llm_core_ollama_thinking.py:92`
- `tests/test_llm_core_ollama_thinking.py:96`
- `tests/test_llm_core_ollama_thinking.py:99`
- `tests/test_llm_core_ollama_thinking.py:102`
- `tests/test_llm_core_ollama_thinking.py:107`
- `tests/test_llm_core_ollama_thinking.py:110`
- `tests/test_llm_core_ollama_thinking.py:114`
- `tests/test_llm_core_ollama_thinking.py:117`
- `tests/test_llm_core_ollama_thinking.py:120`
- `tests/test_llm_core_ollama_thinking.py:123`
- `tests/test_llm_core_ollama_thinking.py:126`
- `tests/test_tool_support_heuristic.py:44`

## `_ollama_api_root` — function, line 746
- **called from:**
- `src/endpoint_resolver.py:375`
- `src/endpoint_resolver.py:399`
- `src/llm_core.py:769`
- `src/llm_core.py:2557`
- `tests/test_provider_endpoints_normalization.py:62`

## `_normalize_ollama_url` — function, line 767
- **called from:**
- `scripts/dump_agent_prompt.py:300`
- `src/llm_core.py:2676`
- `src/llm_core.py:3144`
- `src/llm_core.py:3343`
- `src/llm_core.py:3416`

## `_normalize_openai_chat_url` — function, line 773
- **called from:**
- `scripts/dump_agent_prompt.py:309`
- `src/llm_core.py:2684`
- `src/llm_core.py:3155`
- `src/llm_core.py:3346`
- `src/llm_core.py:3434`

## `_ollama_normalize_messages` — function, line 785
- **called from:**
- `src/llm_core.py:912`

## `_build_ollama_payload` — function, line 881
- **called from:**
- `routes/model_routes.py:781`
- `scripts/dump_agent_prompt.py:301`
- `src/llm_core.py:2678`
- `src/llm_core.py:3149`
- `src/llm_core.py:3421`
- `tests/test_llm_core_ollama.py:159`
- `tests/test_llm_core_ollama.py:176`
- `tests/test_llm_core_ollama.py:186`
- `tests/test_llm_core_ollama.py:195`
- `tests/test_llm_core_ollama.py:214`
- `tests/test_llm_core_ollama.py:224`
- `tests/test_llm_core_ollama.py:235`
- `tests/test_llm_core_ollama.py:249`
- `tests/test_ollama_multimodal.py:32`
- `tests/test_ollama_multimodal.py:53`
- `tests/test_ollama_multimodal.py:67`
- `tests/test_ollama_multimodal.py:85`
- `tests/test_ollama_multimodal.py:93`
- `tests/test_ollama_multimodal.py:106`

## `_parse_ollama_response` — function, line 938
- **called from:**
- `src/llm_core.py:2723`
- `src/llm_core.py:3237`

## `_host_match` — function, line 943
- **called from:**
- `routes/model_routes.py:433`
- `routes/model_routes.py:435`
- `routes/model_routes.py:438`
- `routes/model_routes.py:863`
- `routes/model_routes.py:1026`
- `routes/model_routes.py:1078`
- `routes/model_routes.py:1083`
- `routes/model_routes.py:1178`
- `routes/model_routes.py:1558`
- `routes/model_routes.py:2108`
- `routes/model_routes.py:2190`
- `routes/model_routes.py:2296`
- `routes/model_routes.py:2437`
- `routes/model_routes.py:2656`
- `src/endpoint_resolver.py:363`
- `src/llm_core.py:720`
- `src/llm_core.py:761`
- `src/llm_core.py:980`
- `src/llm_core.py:1145`
- `src/llm_core.py:1147`
- `src/llm_core.py:1149`
- `src/llm_core.py:1151`
- `src/llm_core.py:1153`
- `src/llm_core.py:1155`
- `src/llm_core.py:1159`
- `src/llm_core.py:1159`
- `src/llm_core.py:1167`
- `src/llm_core.py:1169`
- `src/llm_core.py:1171`
- `src/llm_core.py:1193`
- `src/llm_core.py:1388`
- `src/llm_core.py:1389`
- `src/llm_core.py:1390`
- `src/llm_core.py:1391`
- `src/llm_core.py:1392`
- `src/llm_core.py:1393`
- `src/llm_core.py:1394`
- `src/llm_core.py:1395`
- `src/llm_core.py:1400`
- `src/llm_core.py:1401`
- `src/llm_core.py:1403`
- `src/llm_core.py:1404`
- `src/llm_core.py:1405`
- `src/llm_core.py:1406`
- `src/llm_core.py:1407`
- `src/llm_core.py:1408`
- `src/llm_core.py:1409`
- `src/llm_core.py:1438`
- `src/llm_core.py:1533`
- `tests/test_provider_detection_host_match.py:14`
- `tests/test_provider_detection_host_match.py:17`
- `tests/test_provider_detection_host_match.py:20`
- `tests/test_provider_detection_host_match.py:24`
- `tests/test_provider_detection_host_match.py:27`
- `tests/test_provider_detection_host_match.py:30`
- `tests/test_provider_detection_host_match.py:33`
- `tests/test_provider_detection_host_match.py:36`
- `tests/test_provider_detection_host_match.py:37`

## `_is_kimi_code_url` — function, line 979
- **called from:**
- `src/endpoint_resolver.py:435`
- `src/llm_core.py:1012`
- `src/llm_core.py:1028`
- `src/llm_core.py:1059`
- `src/llm_core.py:1088`
- `src/llm_core.py:1104`
- `src/llm_core.py:1120`
- `src/llm_core.py:1157`

## `_kimi_code_base_key` — function, line 988
- **called from:**
- `src/llm_core.py:1014`
- `src/llm_core.py:1022`
- `src/llm_core.py:1030`
- `src/llm_core.py:1061`
- `tests/test_kimi_code_user_agent.py:74`
- `tests/test_kimi_code_user_agent.py:131`
- `tests/test_kimi_code_user_agent.py:166`
- `tests/test_kimi_code_user_agent.py:211`

## `_is_kimi_code_access_denied` — function, line 999
- **called from:**
- `src/llm_core.py:1044`
- `src/llm_core.py:1074`
- `src/llm_core.py:1095`
- `src/llm_core.py:1111`
- `src/llm_core.py:1127`
- `tests/test_kimi_code_user_agent.py:57`
- `tests/test_kimi_code_user_agent.py:60`

## `_kimi_code_ua_candidates` — function, line 1011
- **called from:**
- `src/llm_core.py:1091`
- `src/llm_core.py:1107`
- `src/llm_core.py:1123`
- `tests/test_kimi_code_user_agent.py:65`
- `tests/test_kimi_code_user_agent.py:71`

## `_remember_kimi_code_user_agent` — function, line 1021
- **called from:**
- `src/llm_core.py:1048`
- `src/llm_core.py:1078`
- `src/llm_core.py:1097`
- `src/llm_core.py:1113`
- `src/llm_core.py:1129`
- `tests/test_kimi_code_user_agent.py:64`

## `apply_kimi_code_headers` — function, line 1025
- **called from:**
- `src/llm_core.py:1087`
- `src/llm_core.py:1103`

## `apply_kimi_code_headers_async` — function (async), line 1056
- **called from:**
- `src/llm_core.py:1119`
- `src/llm_core.py:3936`

## `httpx_get_kimi_aware` — function, line 1086
- **called from:**
- `routes/model_routes.py:1067`
- `src/llm_core.py:2562`

## `httpx_post_kimi_aware` — function, line 1102
- **called from:**
- `src/llm_core.py:2713`
- `tests/test_kimi_code_user_agent.py:90`

## `httpx_post_kimi_aware_async` — function (async), line 1118
- **called from:**
- `src/llm_core.py:3204`
- `tests/test_kimi_code_user_agent.py:121`
- `tests/test_kimi_code_user_agent.py:157`

## `_detect_provider` — function, line 1134
- **called from:**
- `routes/chat_routes.py:5676`
- `routes/gallery/gallery_routes.py:3147`
- `routes/model_routes.py:715`
- `scripts/dump_agent_prompt.py:279`
- `src/agent_tools/model_interaction_tools.py:209`
- `src/ai_interaction.py:141`
- `src/endpoint_resolver.py:371`
- `src/endpoint_resolver.py:395`
- `src/endpoint_resolver.py:417`
- `src/llm_core.py:1193`
- `src/llm_core.py:1978`
- `src/llm_core.py:2024`
- `src/llm_core.py:2549`
- `src/llm_core.py:2627`
- `src/llm_core.py:2639`
- `src/llm_core.py:2659`
- `src/llm_core.py:3025`
- `src/llm_core.py:3339`
- `src/llm_core.py:3390`
- `tests/test_cerebras_cache_affinity.py:12`
- `tests/test_copilot.py:26`
- `tests/test_copilot.py:27`
- `tests/test_copilot.py:29`
- `tests/test_featherless_provider.py:73`
- `tests/test_featherless_provider.py:78`
- `tests/test_llm_core_ollama.py:8`
- `tests/test_llm_core_ollama.py:9`
- `tests/test_llm_core_ollama.py:13`
- `tests/test_llm_core_ollama.py:14`
- `tests/test_llm_core_ollama.py:15`
- `tests/test_llm_core_temperature_moonshot.py:49`
- `tests/test_prompt_controls_regressions.py:8`
- `tests/test_provider_classification.py:53`
- `tests/test_provider_classification.py:58`
- `tests/test_provider_classification.py:62`
- `tests/test_provider_classification.py:66`
- `tests/test_provider_classification.py:70`
- `tests/test_provider_detection_builders.py:44`
- `tests/test_provider_detection_builders.py:57`
- `tests/test_provider_detection_detect.py:14`
- `tests/test_provider_detection_detect.py:15`
- `tests/test_provider_detection_detect.py:18`
- `tests/test_provider_detection_detect.py:21`
- `tests/test_provider_detection_detect.py:25`
- `tests/test_provider_detection_detect.py:28`
- `tests/test_provider_detection_detect.py:31`
- `tests/test_provider_detection_detect.py:38`
- `tests/test_provider_detection_detect.py:41`
- `tests/test_provider_detection_detect.py:44`
- `tests/test_provider_detection_detect.py:47`

## `_is_self_hosted_openai_compatible` — function, line 1176
- **called from:**
- `routes/chat_routes.py:5684`
- `src/llm_core.py:1217`
- `src/llm_core.py:1995`
- `src/llm_core.py:2038`
- `tests/test_cerebras_cache_affinity.py:18`
- `tests/test_featherless_provider.py:75`
- `tests/test_featherless_provider.py:80`

## `_apply_local_cache_affinity` — function, line 1199
- **called from:**
- `scripts/dump_agent_prompt.py:332`
- `src/llm_core.py:3183`
- `src/llm_core.py:3472`
- `tests/test_cache_affinity_local_only.py:20`
- `tests/test_cache_affinity_local_only.py:71`
- `tests/test_cerebras_cache_affinity.py:25`

## `_is_local_minimax_mlx_request` — function, line 1223
- **called from:**
- `src/llm_core.py:1340`

## `_is_odysseus_qwen_native_model` — function, line 1242
- **called from:**
- `src/llm_core.py:1334`
- `tests/test_qwen_native_model_family.py:21`
- `tests/test_qwen_native_model_family.py:38`

## `_is_odysseus_qwen_tool_router_model` — function, line 1248
- **called from:**
- `src/llm_core.py:1287`
- `src/llm_core.py:1323`
- `src/llm_core.py:3174`
- `src/llm_core.py:3464`

## `_normalize_thinking_mode` — function, line 1264
- **called from:**
- `src/llm_core.py:275`
- `src/llm_core.py:1282`
- `src/llm_core.py:1303`
- `src/llm_core.py:1528`
- `src/llm_core.py:3660`
- `src/llm_core.py:3900`
- `src/llm_core.py:4168`

## `_apply_local_qwen_thinking_mode` — function, line 1269
- **called from:**
- `src/llm_core.py:2699`
- `src/llm_core.py:3185`
- `src/llm_core.py:3474`
- `tests/test_model_tool_modes.py:103`

## `_apply_hosted_thinking_mode` — function, line 1296
- **called from:**
- `src/llm_core.py:2700`
- `src/llm_core.py:3186`
- `src/llm_core.py:3475`
- `tests/test_kimi_thinking_toggle.py:12`
- `tests/test_prompt_controls_regressions.py:10`
- `tests/test_prompt_controls_regressions.py:18`
- `tests/test_prompt_controls_regressions.py:26`
- `tests/test_prompt_controls_regressions.py:34`

## `_openrouter_requires_reasoning` — function, line 1316
- **called from:**
- `src/llm_core.py:1308`

## `_apply_local_generation_stability` — function, line 1322
- **called from:**
- `scripts/dump_agent_prompt.py:333`
- `src/llm_core.py:2698`
- `src/llm_core.py:3184`
- `src/llm_core.py:3473`
- `tests/test_llm_core_temperature_reasoning.py:92`
- `tests/test_llm_core_temperature_reasoning.py:105`
- `tests/test_llm_core_temperature_reasoning.py:123`
- `tests/test_qwen_native_model_family.py:45`

## `_provider_headers` — function, line 1366
- **called from:**
- `src/llm_core.py:2627`
- `src/llm_core.py:3156`
- `src/llm_core.py:3428`
- `src/llm_core.py:3481`

## `_provider_label` — function, line 1384
- **called from:**
- `src/llm_core.py:1684`
- `tests/test_featherless_provider.py:74`
- `tests/test_featherless_provider.py:79`
- `tests/test_provider_classification.py:94`
- `tests/test_provider_classification.py:108`
- `tests/test_provider_classification.py:111`
- `tests/test_provider_classification.py:115`
- `tests/test_provider_label_js.py:54`

## `_is_openai_hosted_chat_url` — function, line 1432
- **called from:**
- `src/llm_core.py:1501`

## `_model_disallows_reasoning_effort_with_chat_tools` — function, line 1441
- **called from:**
- `src/llm_core.py:1503`
- `src/llm_core.py:1986`

## `_is_harmony_model` — function, line 1471
- **called from:**
- `src/llm_core.py:1478`
- `src/llm_core.py:1493`
- `tests/test_harmony_tool_aliasing.py:69`
- `tests/test_harmony_tool_aliasing.py:70`
- `tests/test_harmony_tool_aliasing.py:71`
- `tests/test_harmony_tool_aliasing.py:72`
- `tests/test_harmony_tool_aliasing.py:73`

## `_alias_harmony_tools` — function, line 1476
- **called from:**
- `src/llm_core.py:934`
- `src/llm_core.py:3449`
- `tests/test_harmony_tool_aliasing.py:37`
- `tests/test_harmony_tool_aliasing.py:44`
- `tests/test_harmony_tool_aliasing.py:51`
- `tests/test_harmony_tool_aliasing.py:77`
- `tests/test_harmony_tool_aliasing.py:78`

## `_unalias_harmony_tool_name` — function, line 1491
- **called from:**
- `src/llm_core.py:3671`
- `src/llm_core.py:4284`
- `tests/test_harmony_tool_aliasing.py:56`
- `tests/test_harmony_tool_aliasing.py:57`
- `tests/test_harmony_tool_aliasing.py:59`
- `tests/test_harmony_tool_aliasing.py:65`

## `_scrub_openai_chat_tool_reasoning` — function, line 1498
- **called from:**
- `scripts/dump_agent_prompt.py:334`
- `src/llm_core.py:3479`
- `tests/test_llm_core_openai_reasoning_tools.py:18`
- `tests/test_llm_core_openai_reasoning_tools.py:31`
- `tests/test_llm_core_openai_reasoning_tools.py:43`
- `tests/test_llm_core_openai_reasoning_tools.py:55`
- `tests/test_llm_core_openai_reasoning_tools.py:67`

## `_apply_deepseek_v4_reasoning_defaults` — function, line 1508
- **called from:**
- `src/llm_core.py:2701`
- `src/llm_core.py:3187`
- `src/llm_core.py:3476`
- `tests/test_llm_core_openai_reasoning_tools.py:79`
- `tests/test_llm_core_openai_reasoning_tools.py:92`
- `tests/test_llm_core_openai_reasoning_tools.py:104`

## `_normalize_chatgpt_subscription_url` — function, line 1541
- **called from:**
- `scripts/dump_agent_prompt.py:305`
- `src/llm_core.py:3345`
- `src/llm_core.py:3427`

## `_message_content_as_text` — function, line 1548
- **called from:**
- `src/llm_core.py:1569`

## `_chatgpt_subscription_instructions` — function, line 1567
- **called from:**
- `src/llm_core.py:1629`

## `_build_chatgpt_responses_payload` — function, line 1606
- **called from:**
- `scripts/dump_agent_prompt.py:306`
- `src/llm_core.py:3429`
- `tests/test_chatgpt_reasoning_and_grouping.py:205`
- `tests/test_chatgpt_zero_native_tools.py:37`
- `tests/test_chatgpt_zero_native_tools.py:54`
- `tests/test_chatgpt_zero_native_tools.py:74`
- `tests/test_chatgpt_zero_native_tools.py:87`
- `tests/test_llm_core_temperature_reasoning.py:140`
- `tests/test_llm_core_temperature_reasoning.py:151`
- `tests/test_llm_core_temperature_reasoning.py:163`
- `tests/test_utility_reasoning_effort.py:139`
- `tests/test_utility_reasoning_effort.py:143`

## `_strip_chatgpt_native_tool_surfaces` — function, line 1650
- **called from:**
- `src/llm_core.py:1642`
- `tests/test_chatgpt_zero_native_tools.py:69`

## `_chatgpt_safe_error` — function, line 1655
- **called from:**
- `src/llm_core.py:3513`
- `src/llm_core.py:3599`

## `_format_chatgpt_subscription_error` — function, line 1665
- **called from:**
- `src/llm_core.py:3513`

## `_format_upstream_error` — function, line 1673
- **called from:**
- `src/llm_core.py:1670`
- `src/llm_core.py:3207`
- `src/llm_core.py:3634`
- `src/llm_core.py:3733`
- `src/llm_core.py:3941`
- `tests/test_provider_classification_errors.py:21`
- `tests/test_provider_classification_errors.py:29`
- `tests/test_provider_classification_errors.py:36`
- `tests/test_provider_classification_errors.py:40`
- `tests/test_provider_classification_errors.py:47`
- `tests/test_provider_classification_errors.py:51`
- `tests/test_provider_classification_errors.py:55`
- `tests/test_provider_classification_errors.py:59`
- `tests/test_provider_classification_errors.py:64`
- `tests/test_provider_classification_errors.py:70`

## `_uses_max_completion_tokens` — function, line 1717
- **called from:**
- `routes/email/email_pollers.py:1318`
- `routes/gallery/gallery_routes.py:3171`
- `routes/model_routes.py:787`
- `scripts/dump_agent_prompt.py:321`
- `src/llm_core.py:1984`
- `src/llm_core.py:2029`
- `src/llm_core.py:2696`
- `src/llm_core.py:3168`
- `src/llm_core.py:3446`
- `tests/test_provider_classification_token_params.py:26`
- `tests/test_provider_classification_token_params.py:34`

## `_restricts_temperature` — function, line 1733
- **called from:**
- `routes/gallery/gallery_routes.py:3185`
- `routes/model_routes.py:791`
- `src/llm_core.py:1757`
- `tests/test_llm_core_temperature_reasoning.py:20`
- `tests/test_llm_core_temperature_reasoning.py:29`

## `_moonshot_rejects_custom_temperature` — function, line 1747
- **called from:**
- `src/llm_core.py:1757`
- `tests/test_llm_core_temperature_moonshot.py:24`
- `tests/test_llm_core_temperature_moonshot.py:38`

## `_omit_temperature` — function, line 1755
- **called from:**
- `scripts/dump_agent_prompt.py:316`
- `src/llm_core.py:2693`
- `src/llm_core.py:3165`
- `src/llm_core.py:3441`

## `_anthropic_rejects_temperature` — function, line 1767
- **called from:**
- `src/llm_core.py:2183`
- `tests/test_llm_core_anthropic_temp_omit.py:42`
- `tests/test_llm_core_anthropic_temp_omit.py:71`
- `tests/test_llm_core_anthropic_temp_omit.py:78`

## `_disable_deepseek_v4_thinking` — function, line 1818
- **called from:**
- `scripts/dump_agent_prompt.py:331`
- `src/llm_core.py:2706`
- `src/llm_core.py:3179`
- `src/llm_core.py:3467`
- `tests/test_sanitize_promotes_metadata_thinking.py:75`
- `tests/test_sanitize_promotes_metadata_thinking.py:85`
- `tests/test_sanitize_promotes_metadata_thinking.py:94`
- `tests/test_thinking_toggle.py:132`
- `tests/test_thinking_toggle.py:142`

## `_thinking_setting_off` — function, line 1844
- **called from:**
- `src/llm_core.py:2644`
- `src/llm_core.py:3023`
- `src/llm_core.py:3395`
- `tests/test_thinking_toggle.py:46`
- `tests/test_thinking_toggle.py:54`
- `tests/test_thinking_toggle.py:65`

## `normalize_reasoning_override` — function, line 1873
- **called from:**
- `src/llm_core.py:1889`
- `tests/test_nim_reasoning_control.py:59`
- `tests/test_nim_reasoning_control.py:60`
- `tests/test_nim_reasoning_control.py:61`
- `tests/test_nim_reasoning_control.py:62`

## `set_request_reasoning` — function, line 1887
- **called from:**
- `routes/chat_routes.py:2429`
- `routes/chat_routes.py:2728`
- `tests/test_nim_reasoning_control.py:66`
- `tests/test_nim_reasoning_control.py:71`

## `_request_reasoning` — function, line 1892
- **called from:**
- `src/llm_core.py:1975`
- `src/llm_core.py:2643`
- `src/llm_core.py:3022`
- `src/llm_core.py:3394`
- `tests/test_nim_reasoning_control.py:68`

## `_nim_model_family` — function, line 1924
- **called from:**
- `src/llm_core.py:1946`

## `nim_reasoning_off_value` — function, line 1932
- **called from:**
- `routes/chat_routes.py:5681`
- `src/llm_core.py:2036`
- `tests/test_nim_reasoning_control.py:31`
- `tests/test_nim_reasoning_control.py:32`
- `tests/test_nim_reasoning_control.py:33`
- `tests/test_nim_reasoning_control.py:34`
- `tests/test_nim_reasoning_control.py:35`
- `tests/test_nim_reasoning_control.py:36`
- `tests/test_nim_reasoning_control.py:37`

## `nim_reasoning_levels` — function, line 1943
- **called from:**
- `routes/chat_routes.py:5680`
- `src/llm_core.py:1952`
- `tests/test_nim_reasoning_control.py:41`
- `tests/test_nim_reasoning_control.py:42`
- `tests/test_nim_reasoning_control.py:43`
- `tests/test_nim_reasoning_control.py:44`
- `tests/test_nim_reasoning_control.py:45`
- `tests/test_nim_reasoning_control.py:46`

## `_nim_clamp_level` — function, line 1949
- **called from:**
- `src/llm_core.py:1994`
- `tests/test_nim_reasoning_control.py:50`
- `tests/test_nim_reasoning_control.py:51`
- `tests/test_nim_reasoning_control.py:52`
- `tests/test_nim_reasoning_control.py:53`
- `tests/test_nim_reasoning_control.py:54`
- `tests/test_nim_reasoning_control.py:55`

## `_apply_request_reasoning_effort` — function, line 1964
- **called from:**
- `src/llm_core.py:2709`
- `src/llm_core.py:3182`
- `src/llm_core.py:3480`
- `tests/test_nim_reasoning_control.py:70`

## `_apply_thinking_off_openai_compat` — function, line 2001
- **called from:**
- `src/llm_core.py:2708`
- `src/llm_core.py:3181`
- `src/llm_core.py:3471`
- `tests/test_nim_reasoning_control.py:69`
- `tests/test_thinking_toggle.py:77`

## `_supports_thinking` — function, line 2048
- **called from:**
- `scripts/dump_agent_prompt.py:327`
- `scripts/dump_agent_prompt.py:329`
- `src/llm_core.py:1287`
- `src/llm_core.py:2704`
- `src/llm_core.py:3173`
- `src/llm_core.py:3177`
- `src/llm_core.py:3456`
- `src/llm_core.py:3463`
- `src/llm_core.py:3899`
- `tests/test_llm_core_thinking_models.py:22`
- `tests/test_llm_core_thinking_models.py:27`

## `_normalize_mistral_content` — function, line 2055
- **called from:**
- `src/llm_core.py:2729`
- `src/llm_core.py:3247`
- `src/llm_core.py:4158`
- `tests/test_llm_core_mistral_content.py:26`
- `tests/test_llm_core_mistral_content.py:32`
- `tests/test_llm_core_mistral_content.py:47`
- `tests/test_llm_core_mistral_content.py:61`
- `tests/test_llm_core_mistral_content.py:69`
- `tests/test_llm_core_mistral_content.py:80`
- `tests/test_llm_core_mistral_content.py:96`
- `tests/test_llm_core_mistral_content.py:102`
- `tests/test_llm_core_mistral_content.py:117`
- `tests/test_llm_core_mistral_content.py:124`
- `tests/test_llm_core_mistral_content.py:131`
- `tests/test_llm_core_mistral_content.py:143`
- `tests/test_llm_core_mistral_content.py:154`

## `_convert_openai_content_to_anthropic` — function, line 2087
- **called from:**
- `src/llm_core.py:2168`

## `_build_anthropic_payload` — function, line 2130
- **called from:**
- `routes/model_routes.py:773`
- `scripts/dump_agent_prompt.py:297`
- `src/llm_core.py:2674`
- `src/llm_core.py:3142`
- `src/llm_core.py:3414`
- `tests/test_approved_replay_message_shape.py:60`
- `tests/test_llm_core_anthropic_cache.py:7`
- `tests/test_llm_core_anthropic_temp_clamp.py:17`
- `tests/test_llm_core_anthropic_temp_omit.py:82`
- `tests/test_llm_core_sanitize_tool_calls.py:198`
- `tests/test_llm_core_system_msg_missing_content.py:27`
- `tests/test_llm_core_system_msg_missing_content.py:38`
- `tests/test_llm_core_system_msg_missing_content.py:49`
- `tests/test_llm_core_system_msg_missing_content.py:67`
- `tests/test_llm_core_temperature_anthropic.py:11`

## `_build_anthropic_headers` — function, line 2217
- **called from:**
- `routes/model_routes.py:772`
- `src/llm_core.py:2673`
- `src/llm_core.py:3141`
- `src/llm_core.py:3413`

## `_parse_anthropic_response` — function, line 2228
- **called from:**
- `src/llm_core.py:2721`
- `src/llm_core.py:3235`
- `tests/test_anthropic_response_parse.py:13`
- `tests/test_anthropic_response_parse.py:21`
- `tests/test_anthropic_response_parse.py:25`
- `tests/test_anthropic_response_parse.py:26`
- `tests/test_anthropic_response_parse.py:27`

## `_as_content_blocks` — function, line 2243
- **called from:**
- `src/llm_core.py:2434`
- `src/llm_core.py:2434`

## `_is_untrusted_context_content` — function, line 2257
- **called from:**
- `src/llm_core.py:2267`
- `src/llm_core.py:2423`

## `_sanitize_llm_messages` — function, line 2283
- **called from:**
- `scripts/dump_agent_prompt.py:280`
- `src/llm_core.py:2640`
- `src/llm_core.py:3026`
- `src/llm_core.py:3391`
- `tests/test_approved_replay_message_shape.py:59`
- `tests/test_approved_replay_message_shape.py:72`
- `tests/test_llm_core_sanitize_tool_calls.py:53`
- `tests/test_llm_core_sanitize_tool_calls.py:82`
- `tests/test_llm_core_sanitize_tool_calls.py:106`
- `tests/test_llm_core_sanitize_tool_calls.py:137`
- `tests/test_llm_core_sanitize_tool_calls.py:165`
- `tests/test_llm_core_sanitize_tool_calls.py:193`
- `tests/test_media_ingress.py:134`
- `tests/test_sanitize_multimodal_merge.py:12`
- `tests/test_sanitize_multimodal_merge.py:26`
- `tests/test_sanitize_preserves_reasoning.py:49`
- `tests/test_sanitize_preserves_reasoning.py:70`
- `tests/test_sanitize_preserves_reasoning.py:87`
- `tests/test_sanitize_promotes_metadata_thinking.py:33`
- `tests/test_sanitize_promotes_metadata_thinking.py:47`
- `tests/test_sanitize_promotes_metadata_thinking.py:56`
- `tests/test_sanitize_promotes_metadata_thinking.py:64`
- `tests/test_temporal_grounding_stamps.py:29`
- `tests/test_temporal_grounding_stamps.py:49`
- `tests/test_temporal_grounding_stamps.py:58`
- `tests/test_temporal_grounding_stamps.py:65`
- `tests/test_temporal_grounding_stamps.py:66`
- `tests/test_temporal_grounding_stamps.py:85`
- `tests/test_temporal_grounding_stamps.py:106`
- `tests/test_temporal_grounding_stamps.py:165`

## `_normalize_anthropic_url` — function, line 2454
- **called from:**
- `routes/model_routes.py:770`
- `scripts/dump_agent_prompt.py:296`
- `src/llm_core.py:2672`
- `src/llm_core.py:3140`
- `src/llm_core.py:3341`
- `src/llm_core.py:3412`

## `_model_list_base` — function, line 2464
- **called from:**
- `src/llm_core.py:2503`
- `src/llm_core.py:2520`

## `_parse_model_cache` — function, line 2476
- **called from:**
- `src/llm_core.py:2522`
- `src/llm_core.py:2525`

## `_configured_cached_model_ids` — function, line 2496
- **called from:**
- `src/llm_core.py:2546`

## `list_model_ids` — function, line 2537
- **called from:**
- `routes/session_routes.py:614`
- `routes/session_routes.py:634`
- `routes/skills_routes.py:645`
- `services/skills/model_selection.py:56`
- `src/builtin_actions.py:2165`
- `src/llm_core.py:2595`
- `tests/test_llama_server_models_url.py:33`
- `tests/test_llm_core_ollama.py:124`
- `tests/test_lmstudio_models_url.py:133`
- `tests/test_lmstudio_models_url.py:156`
- `tests/test_lmstudio_models_url.py:174`
- `tests/test_model_routes.py:1997`

## `normalize_model_id` — function, line 2586
- **called from:**
- `routes/chat_helpers.py:1468`

## `_apply_explicit_nonstream_reasoning_effort` — function, line 2608
- **called from:**
- `src/llm_core.py:2710`
- `src/llm_core.py:3190`

## `llm_call` — function, line 2621
- **called from:**
- `src/chat_processor.py:438`
- `src/document_processor.py:524`
- `src/llm_core.py:2823`
- `tests/test_llm_core_fallback.py:540`
- `tests/test_llm_core_fallback.py:546`
- `tests/test_llm_core_fallback.py:552`
- `tests/test_llm_core_ollama.py:35`
- `tests/test_llm_core_ollama.py:67`
- `tests/test_llm_core_ollama.py:101`
- `tests/test_llm_core_ollama.py:274`
- `tests/test_llm_core_reasoning_content_fallback.py:44`
- `tests/test_llm_core_reasoning_content_fallback.py:165`
- `tests/test_llm_core_temperature_moonshot.py:72`
- `tests/test_llm_core_temperature_reasoning.py:52`
- `tests/test_utility_reasoning_effort.py:158`
- `tests/test_utility_reasoning_effort.py:159`
- `tests/test_utility_reasoning_effort.py:160`
- `tests/test_utility_reasoning_effort.py:279`
- `tests/test_utility_reasoning_effort.py:491`
- `tests/test_utility_reasoning_effort.py:495`

## `_candidate_is_configured` — function, line 2742
- **called from:**
- `src/llm_core.py:2781`
- `src/llm_core.py:2917`
- `src/llm_core.py:4930`

## `_safe_route_descriptor` — function, line 2753
- **called from:**
- `src/llm_core.py:2789`

## `_dedupe_model_candidates_with_descriptors` — function, line 2773
- **called from:**
- `src/llm_core.py:2805`
- `src/llm_core.py:4933`

## `dedupe_model_candidates` — function, line 2793
- **called from:**
- `src/agent_loop.py:26896`
- `src/llm_core.py:2817`
- `src/llm_core.py:2862`
- `src/llm_core.py:2920`
- `tests/test_llm_core_fallback.py:1528`
- `tests/test_llm_core_fallback.py:1533`
- `tests/test_llm_core_fallback.py:1534`

## `llm_call_with_fallback` — function, line 2809
- **called from:**
- `routes/session_routes.py:1589`

## `_extract_finish_reason` — function, line 2832
- **called from:**
- `src/llm_core.py:3260`
- `tests/test_llm_core_reasoning_content_fallback.py:131`
- `tests/test_llm_core_reasoning_content_fallback.py:137`
- `tests/test_llm_core_reasoning_content_fallback.py:143`
- `tests/test_llm_core_reasoning_content_fallback.py:149`
- `tests/test_llm_core_reasoning_content_fallback.py:150`
- `tests/test_llm_core_reasoning_content_fallback.py:151`

## `llm_call_async_with_fallback` — function (async), line 2854
- **called from:**
- `mcp_servers/email_server.py:3096`
- `routes/email/email_routes.py:6775`
- `routes/email/email_routes.py:7115`
- `src/builtin_actions.py:727`
- `src/builtin_actions.py:1623`
- `src/builtin_actions.py:1910`
- `src/builtin_actions.py:3012`
- `src/task_endpoint.py:114`
- `tests/test_utility_reasoning_effort.py:122`

## `_nonstream_error_status` — function, line 2887
- **called from:**
- `src/llm_core.py:2960`
- `src/llm_core.py:4957`

## `llm_call_async_with_route_fallback` — function (async), line 2900
- **called from:**
- `routes/chat_routes.py:2583`
- `tests/test_llm_core_fallback.py:757`
- `tests/test_llm_core_fallback.py:786`
- `tests/test_llm_core_fallback.py:1334`
- `tests/test_llm_core_fallback.py:1363`
- `tests/test_llm_core_fallback.py:1408`
- `tests/test_llm_core_fallback.py:1422`
- `tests/test_llm_core_fallback.py:1635`
- `tests/test_llm_core_fallback.py:1660`
- `tests/test_llm_core_fallback.py:1686`

## `llm_call_async` — function (async), line 2974
- **called from:**
- `routes/auth_routes.py:885`
- `routes/calendar_routes.py:1865`
- `routes/chat_helpers.py:671`
- `routes/chat_helpers.py:763`
- `routes/document/document_routes.py:1550`
- `routes/email/email_helpers.py:453`
- `routes/email/email_routes.py:6564`
- `routes/email/email_routes.py:7156`
- `routes/history/history_routes.py:1540`
- `routes/memory/memory_routes.py:267`
- `routes/memory/memory_routes.py:463`
- `routes/note/note_routes.py:223`
- `routes/preset_routes.py:113`
- `routes/session_routes.py:844`
- `routes/session_routes.py:1391`
- `routes/task/task_routes.py:334`
- `routes/task/task_routes.py:1209`
- `routes/webhook/webhook_routes.py:381`
- `services/memory/memory_extractor.py:680`
- `services/memory/memory_extractor.py:935`
- `services/memory/memory_extractor.py:1026`
- `services/memory/skill_extractor.py:199`
- `src/agent_loop.py:17230`
- `src/agent_loop.py:28531`
- `src/agent_loop.py:30666`
- `src/agent_loop.py:32748`
- `src/agent_loop.py:38190`
- `src/agent_loop.py:38477`
- `src/agent_loop.py:38541`
- `src/agent_tools/model_interaction_tools.py:55`
- `src/agent_tools/model_interaction_tools.py:102`
- `src/agent_tools/session_tools.py:243`
- `src/ai_interaction.py:305`
- `src/background_tool_jobs.py:115`
- `src/context_compactor.py:790`
- `src/deep_research.py:631`
- `src/llm_core.py:2876`
- `src/llm_core.py:2939`
- `src/research_handler.py:166`
- `src/research_handler.py:198`
- `src/research_handler.py:946`
- `src/teacher_escalation.py:317`
- `src/teacher_escalation.py:491`
- `tests/test_llm_core_async_mistral_content.py:37`
- `tests/test_llm_core_async_mistral_content.py:85`
- `tests/test_llm_core_fallback.py:839`
- `tests/test_llm_core_fallback.py:840`
- `tests/test_llm_core_reasoning_content_fallback.py:65`
- `tests/test_llm_core_reasoning_content_fallback.py:91`
- `tests/test_llm_core_reasoning_content_fallback.py:116`
- `tests/test_utility_reasoning_effort.py:278`
- `tests/test_utility_reasoning_effort.py:280`
- `tests/test_utility_reasoning_effort.py:530`
- `tests/test_utility_reasoning_effort.py:534`

## `_stream_target_url` — function, line 3338
- **called from:**
- `src/llm_core.py:3355`

## `stream_llm` — function (async), line 3349
- **called from:**
- `routes/chat_routes.py:5746`
- `scripts/eval_qwen_tool_groups_stream.py:167`
- `src/email_reply_stream.py:28`
- `src/llm_core.py:3081`
- `src/llm_core.py:4555`
- `tests/test_chat_metrics.py:66`
- `tests/test_chat_metrics.py:94`
- `tests/test_kimi_code_user_agent.py:200`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_llm_core_ollama.py:312`
- `tests/test_llm_core_ollama_thinking.py:62`
- `tests/test_llm_core_reasoning.py:50`
- `tests/test_llm_core_sse_no_space.py:56`
- `tests/test_llm_core_streaming.py:105`
- `tests/test_llm_core_streaming.py:171`
- `tests/test_llm_core_streaming.py:204`
- `tests/test_llm_core_streaming.py:234`
- `tests/test_llm_core_usage_finish_delta.py:58`

## `_stream_llm_inner` — function (async), line 3375
- **called from:**
- `src/llm_core.py:3357`
- `src/llm_core.py:4343`
- `tests/test_chatgpt_zero_native_tools.py:138`
- `tests/test_llm_core_fallback.py:80`
- `tests/test_llm_core_fallback.py:1307`

## `_emit_tool_calls` — function, line 3910
- **called from:**
- `src/llm_core.py:3979`
- `src/llm_core.py:4316`

## `_format_routed_content` — function, line 3917
- **called from:**
- `src/llm_core.py:3977`
- `src/llm_core.py:4192`
- `src/llm_core.py:4297`
- `src/llm_core.py:4302`
- `src/llm_core.py:4314`

## `_choice_has_meaningful_output` — function, line 3994
- **called from:**
- `src/llm_core.py:4034`

## `_meaningful` — function, line 4000
- **called from:**
- `src/llm_core.py:4018`

## `_stream_failure_message` — function, line 4375
- **called from:**
- `src/llm_core.py:3713`
- `src/llm_core.py:3890`
- `src/llm_core.py:4372`
- `tests/test_codeql_python_residual_security.py:121`

## `_summarize_stream_error` — function, line 4385
- **called from:**
- `src/llm_core.py:4975`
- `src/llm_core.py:5057`
- `src/llm_core.py:5103`
- `src/llm_core.py:5159`
- `tests/test_llm_core_fallback.py:1747`
- `tests/test_llm_core_fallback.py:1748`
- `tests/test_llm_core_fallback.py:1749`

## `_stream_error_status` — function, line 4403
- **called from:**
- `src/llm_core.py:4609`
- `src/llm_core.py:4658`
- `src/llm_core.py:4665`
- `src/llm_core.py:5038`

## `_stream_error_fallback_override` — function, line 4419
- **called from:**
- `src/llm_core.py:4659`
- `src/llm_core.py:5039`

## `_stream_error_text` — function, line 4435
- **called from:**
- `src/llm_core.py:4460`
- `src/llm_core.py:4506`
- `src/llm_core.py:4678`

## `_is_degenerate_stream_error` — function, line 4459
- **called from:**
- `src/llm_core.py:4567`

## `_debug_llm_request_shape` — function, line 4464
- **called from:**
- `src/llm_core.py:3491`

## `_native_tool_transport_rejected` — function, line 4503
- **called from:**
- `src/llm_core.py:4744`

## `_stream_candidate_with_context_recovery` — function (async), line 4522
- **called from:**
- `src/llm_core.py:5012`
- `tests/test_llm_core_fallback.py:1232`

## `_request_factory_error_chunk` — function, line 4804
- **called from:**
- `src/llm_core.py:4968`

## `_provider_stream_error_status` — function, line 4832
- **called from:**
- `src/llm_core.py:3221`
- `src/llm_core.py:3598`
- `src/llm_core.py:3646`
- `src/llm_core.py:3867`
- `src/llm_core.py:4054`
- `tests/test_llm_core_fallback.py:618`
- `tests/test_llm_core_fallback.py:629`
- `tests/test_llm_core_fallback.py:636`
- `tests/test_llm_core_fallback.py:645`
- `tests/test_llm_core_fallback.py:654`
- `tests/test_llm_core_fallback.py:800`

## `stream_llm_with_fallback` — function (async), line 4900
- **called from:**
- `routes/chat_routes.py:4521`
- `src/agent_loop.py:22827`
- `src/agent_loop.py:27705`
- `tests/test_generation_budget.py:182`
- `tests/test_generation_budget.py:211`
- `tests/test_generation_budget.py:262`
- `tests/test_generation_budget.py:319`
- `tests/test_llm_core_fallback.py:60`
- `tests/test_llm_core_fallback.py:246`
- `tests/test_llm_core_fallback.py:283`
- `tests/test_llm_core_fallback.py:432`
- `tests/test_llm_core_fallback.py:469`
- `tests/test_llm_core_fallback.py:505`
- `tests/test_llm_core_fallback.py:703`
- `tests/test_llm_core_fallback.py:730`
- `tests/test_llm_core_fallback.py:1273`
- `tests/test_llm_core_fallback.py:1475`
- `tests/test_llm_core_fallback.py:1551`
- `tests/test_llm_core_fallback.py:1576`
- `tests/test_llm_core_fallback.py:1613`
- `tests/test_llm_core_fallback.py:1714`
- `tests/test_llm_core_fallback.py:1780`
