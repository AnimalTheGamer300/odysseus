# `src/llm_core.py` — definitions & call sites

131 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalize_usage_counts` — function, line 28
- **called from:**
- `src/agent_loop.py:4297`
- `src/agent_loop.py:5615`
- `src/llm_core.py:3135`
- `src/llm_core.py:3246`
- `src/llm_core.py:3417`
- `src/llm_core.py:3582`

## `_count` — function, line 31
- **called from:**
- `src/llm_core.py:44`
- `src/llm_core.py:45`

## `_normalize_http_status` — function, line 54
- **called from:**
- `routes/chat_routes.py:95`
- `routes/chat_routes.py:2820`
- `src/agent_loop.py:4354`
- `src/agent_loop.py:5531`
- `src/llm_core.py:2516`
- `src/llm_core.py:3815`
- `src/llm_core.py:3900`

## `_local_model_gate_enabled` — function, line 75
- **called from:**
- `src/llm_core.py:92`

## `_gate_workload` — function, line 79
- **called from:**
- `src/llm_core.py:97`

## `_local_model_slot` — function (async), line 84
- decorator: `asynccontextmanager`
- **called from:**
- `src/llm_core.py:2785`
- `src/llm_core.py:2939`
- `tests/test_email_summary_llm.py:156`
- `tests/test_email_summary_llm.py:177`

## `LLMConfig` — class, line 144
- **called from:**
- `src/config.py:126`

## `_FallbackIneligibleHTTPException` — class, line 162
- **called from:**
- `src/llm_core.py:2542`
- `src/llm_core.py:2849`
- `src/llm_core.py:2882`
- `src/llm_core.py:2893`
- `src/llm_core.py:2904`
- `src/llm_core.py:2917`

## `_call_timeout` — function, line 168
- **called from:**
- `src/llm_core.py:2779`
- `tests/test_llm_core_connect_timeout.py:26`
- `tests/test_llm_core_connect_timeout.py:46`

## `_stream_timeout` — function, line 173
- **called from:**
- `src/llm_core.py:3058`
- `tests/test_llm_core_connect_timeout.py:35`
- `tests/test_llm_core_connect_timeout.py:47`

## `_cache_header_identity` — function, line 179
- **called from:**
- `src/llm_core.py:220`

## `_get_cache_key` — function, line 198
- **called from:**
- `src/llm_core.py:2308`
- `src/llm_core.py:2657`
- `tests/test_llm_core_fallback.py:543`

## `_strip_visible_chat_template_artifacts` — function, line 283
- **called from:**
- `src/llm_core.py:3629`

## `_harmony_suffix_hold_len` — function, line 287
- **called from:**
- `src/llm_core.py:350`

## `_HarmonyStreamRouter` — class, line 297
- **called from:**
- `src/llm_core.py:3191`
- `src/llm_core.py:3469`

## `_HarmonyStreamRouter.__init__` — method, line 300
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

## `_HarmonyStreamRouter.feed` — method, line 306
- **called from:**
- `routes/email_routes.py:1503`
- `src/llm_core.py:3230`
- `src/llm_core.py:3644`
- `src/llm_core.py:3749`
- `src/llm_core.py:3753`
- `tests/test_chat_attachment_picker.py:24`

## `_HarmonyStreamRouter.flush` — method, line 312
- **called from:**
- `core/atomic_io.py:37`
- `core/atomic_io.py:58`
- `core/database.py:525`
- `routes/calendar_routes.py:317`
- `routes/calendar_routes.py:325`
- `routes/email_routes.py:5756`
- `scripts/demo_email/demo_account.py:117`
- `scripts/demo_email/demo_account.py:165`
- `scripts/migrate_searxng_settings.py:133`
- `scripts/pr_blocker_audit.py:125`
- `scripts/pr_blocker_audit.py:138`
- `scripts/pr_blocker_audit.py:144`
- `scripts/pr_blocker_audit.py:151`
- `src/api_key_manager.py:94`
- `src/email_thread_parser.py:328`
- `src/email_thread_parser.py:334`
- `src/email_thread_parser.py:371`
- `src/email_thread_parser.py:385`
- `src/llm_core.py:3241`
- `src/llm_core.py:3259`
- `src/llm_core.py:3518`
- `src/llm_core.py:3760`
- `src/task_scheduler.py:2616`
- `src/upload_handler.py:745`
- `tests/test_atomic_io.py:101`
- `tests/test_launcher.py:24`
- `static/js/chat.js:2840`
- `static/js/emailLibrary.js:6387`
- `static/js/emailLibrary.js:6393`
- `static/js/emailLibrary.js:6398`
- `static/js/liveThinkingThrottle.js:18`
- `static/js/liveThinkingThrottle.js:191`

## `_HarmonyStreamRouter._append_text` — method, line 315
- **called from:**
- `src/llm_core.py:346`
- `src/llm_core.py:353`

## `_HarmonyStreamRouter._handle_marker` — method, line 327
- **called from:**
- `src/llm_core.py:347`

## `_HarmonyStreamRouter._drain` — method, line 340
- **called from:**
- `src/agent_runs.py:201`
- `src/llm_core.py:310`
- `src/llm_core.py:313`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_model_routes.py:1169`
- `tests/test_model_routes.py:1206`

## `_stream_delta_event` — function, line 357
- **called from:**
- `src/llm_core.py:3227`
- `src/llm_core.py:3231`
- `src/llm_core.py:3242`
- `src/llm_core.py:3260`
- `src/llm_core.py:3486`
- `src/llm_core.py:3494`
- `src/llm_core.py:3627`

## `_DegenerateStreamGuard` — class, line 367
- **called from:**
- `src/llm_core.py:3064`
- `tests/test_llm_core_fallback.py:1025`

## `_DegenerateStreamGuard.__init__` — method, line 376
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

## `_DegenerateStreamGuard.check` — method, line 383
- **called from:**
- `routes/auth_routes.py:130`
- `routes/auth_routes.py:148`
- `routes/auth_routes.py:167`
- `src/llm_core.py:3117`
- `src/llm_core.py:3623`
- `src/llm_core.py:3632`
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
- `tests/test_llm_core_fallback.py:1026`
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
- `static/js/skills.js:1352`

## `_model_activity_key` — function, line 432
- **called from:**
- `src/llm_core.py:465`
- `src/llm_core.py:469`

## `_same_model_identity` — function, line 435
- **called from:**
- `src/llm_core.py:446`
- `src/llm_core.py:456`
- `src/llm_core.py:3541`
- `src/llm_core.py:3601`

## `_reported_model_name` — function, line 438
- **called from:**
- `src/llm_core.py:445`
- `src/llm_core.py:453`
- `src/llm_core.py:3104`
- `src/llm_core.py:3216`
- `src/llm_core.py:3343`

## `_model_actual_event` — function, line 443
- **called from:**
- `src/llm_core.py:3110`
- `src/llm_core.py:3220`
- `src/llm_core.py:3351`

## `_annotate_usage_model` — function, line 451
- **called from:**
- `src/llm_core.py:3145`
- `src/llm_core.py:3251`
- `src/llm_core.py:3422`

## `note_model_activity` — function, line 461
- **called from:**
- `src/llm_core.py:2352`
- `src/llm_core.py:2786`
- `src/llm_core.py:3063`

## `seconds_since_model_activity` — function, line 467
- **called from:**
- `src/builtin_actions.py:2068`

## `_host_key` — function, line 474
- **called from:**
- `src/llm_core.py:480`
- `src/llm_core.py:495`
- `src/llm_core.py:505`
- `src/llm_core.py:2777`
- `src/llm_core.py:2859`
- `src/llm_core.py:3061`
- `src/llm_core.py:3172`
- `src/llm_core.py:3266`
- `src/llm_core.py:3443`
- `src/llm_core.py:3771`
- `tests/test_llm_core_concurrency.py:51`

## `_is_host_dead` — function, line 479
- **called from:**
- `src/llm_core.py:2776`
- `src/llm_core.py:3060`

## `_mark_host_dead` — function, line 490
- **called from:**
- `src/llm_core.py:2854`
- `src/llm_core.py:3169`
- `src/llm_core.py:3263`
- `src/llm_core.py:3440`
- `src/llm_core.py:3768`
- `tests/test_llm_core_concurrency.py:68`

## `_clear_host_dead` — function, line 504
- **called from:**
- `src/llm_core.py:2801`
- `src/llm_core.py:3076`
- `src/llm_core.py:3197`
- `src/llm_core.py:3296`
- `src/llm_core.py:3501`

## `_get_http_client` — function, line 517
- **called from:**
- `src/llm_core.py:2787`
- `src/llm_core.py:3074`
- `src/llm_core.py:3195`
- `src/llm_core.py:3294`
- `src/llm_core.py:3498`

## `_get_cached_response` — function, line 527
- **called from:**
- `src/llm_core.py:2312`
- `src/llm_core.py:2661`

## `_get_cached_response_model` — function, line 532
- **called from:**
- `src/llm_core.py:2668`

## `_set_cached_response` — function, line 538
- **called from:**
- `src/llm_core.py:2376`
- `src/llm_core.py:2699`
- `src/llm_core.py:2726`
- `src/llm_core.py:2838`
- `tests/test_llm_core_concurrency.py:38`

## `_is_ollama_native_url` — function, line 568
- **called from:**
- `scripts/dump_agent_prompt.py:89`
- `src/agent_loop.py:1119`
- `src/llm_core.py:1000`
- `src/llm_core.py:1170`
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

## `_is_ollama_openai_compat_url` — function, line 585
- **called from:**
- `scripts/dump_agent_prompt.py:90`
- `scripts/dump_agent_prompt.py:329`
- `src/agent_loop.py:1120`
- `src/llm_core.py:2765`
- `src/llm_core.py:3037`
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

## `_ollama_api_root` — function, line 603
- **called from:**
- `src/endpoint_resolver.py:278`
- `src/endpoint_resolver.py:302`
- `src/llm_core.py:626`
- `src/llm_core.py:2221`
- `tests/test_provider_endpoints_normalization.py:49`

## `_normalize_ollama_url` — function, line 624
- **called from:**
- `scripts/dump_agent_prompt.py:300`
- `src/llm_core.py:2322`
- `src/llm_core.py:2738`
- `src/llm_core.py:2927`
- `src/llm_core.py:2995`

## `_normalize_openai_chat_url` — function, line 630
- **called from:**
- `scripts/dump_agent_prompt.py:309`
- `src/llm_core.py:2330`
- `src/llm_core.py:2749`
- `src/llm_core.py:2930`
- `src/llm_core.py:3010`

## `_ollama_normalize_messages` — function, line 642
- **called from:**
- `src/llm_core.py:769`

## `_build_ollama_payload` — function, line 738
- **called from:**
- `routes/model_routes.py:727`
- `scripts/dump_agent_prompt.py:301`
- `src/llm_core.py:2324`
- `src/llm_core.py:2743`
- `src/llm_core.py:3000`
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

## `_parse_ollama_response` — function, line 795
- **called from:**
- `src/llm_core.py:2363`
- `src/llm_core.py:2821`

## `_host_match` — function, line 800
- **called from:**
- `routes/model_routes.py:414`
- `routes/model_routes.py:416`
- `routes/model_routes.py:419`
- `routes/model_routes.py:1020`
- `routes/model_routes.py:1025`
- `src/endpoint_resolver.py:266`
- `src/llm_core.py:577`
- `src/llm_core.py:618`
- `src/llm_core.py:837`
- `src/llm_core.py:1002`
- `src/llm_core.py:1004`
- `src/llm_core.py:1006`
- `src/llm_core.py:1008`
- `src/llm_core.py:1010`
- `src/llm_core.py:1012`
- `src/llm_core.py:1014`
- `src/llm_core.py:1014`
- `src/llm_core.py:1022`
- `src/llm_core.py:1024`
- `src/llm_core.py:1046`
- `src/llm_core.py:1144`
- `src/llm_core.py:1145`
- `src/llm_core.py:1146`
- `src/llm_core.py:1147`
- `src/llm_core.py:1148`
- `src/llm_core.py:1149`
- `src/llm_core.py:1150`
- `src/llm_core.py:1151`
- `src/llm_core.py:1156`
- `src/llm_core.py:1158`
- `src/llm_core.py:1159`
- `src/llm_core.py:1160`
- `src/llm_core.py:1161`
- `src/llm_core.py:1162`
- `src/llm_core.py:1163`
- `src/llm_core.py:1164`
- `src/llm_core.py:1193`
- `tests/test_provider_detection_host_match.py:14`
- `tests/test_provider_detection_host_match.py:17`
- `tests/test_provider_detection_host_match.py:20`
- `tests/test_provider_detection_host_match.py:24`
- `tests/test_provider_detection_host_match.py:27`
- `tests/test_provider_detection_host_match.py:30`
- `tests/test_provider_detection_host_match.py:33`
- `tests/test_provider_detection_host_match.py:36`
- `tests/test_provider_detection_host_match.py:37`

## `_is_kimi_code_url` — function, line 836
- **called from:**
- `src/endpoint_resolver.py:338`
- `src/llm_core.py:869`
- `src/llm_core.py:885`
- `src/llm_core.py:916`
- `src/llm_core.py:945`
- `src/llm_core.py:961`
- `src/llm_core.py:977`

## `_kimi_code_base_key` — function, line 845
- **called from:**
- `src/llm_core.py:871`
- `src/llm_core.py:879`
- `src/llm_core.py:887`
- `src/llm_core.py:918`
- `tests/test_kimi_code_user_agent.py:74`
- `tests/test_kimi_code_user_agent.py:131`
- `tests/test_kimi_code_user_agent.py:166`
- `tests/test_kimi_code_user_agent.py:211`

## `_is_kimi_code_access_denied` — function, line 856
- **called from:**
- `src/llm_core.py:901`
- `src/llm_core.py:931`
- `src/llm_core.py:952`
- `src/llm_core.py:968`
- `src/llm_core.py:984`
- `tests/test_kimi_code_user_agent.py:57`
- `tests/test_kimi_code_user_agent.py:60`

## `_kimi_code_ua_candidates` — function, line 868
- **called from:**
- `src/llm_core.py:948`
- `src/llm_core.py:964`
- `src/llm_core.py:980`
- `tests/test_kimi_code_user_agent.py:65`
- `tests/test_kimi_code_user_agent.py:71`

## `_remember_kimi_code_user_agent` — function, line 878
- **called from:**
- `src/llm_core.py:905`
- `src/llm_core.py:935`
- `src/llm_core.py:954`
- `src/llm_core.py:970`
- `src/llm_core.py:986`
- `tests/test_kimi_code_user_agent.py:64`

## `apply_kimi_code_headers` — function, line 882
- **called from:**
- `src/llm_core.py:944`
- `src/llm_core.py:960`

## `apply_kimi_code_headers_async` — function (async), line 913
- **called from:**
- `src/llm_core.py:976`
- `src/llm_core.py:3499`

## `httpx_get_kimi_aware` — function, line 943
- **called from:**
- `routes/model_routes.py:1009`
- `src/llm_core.py:2226`

## `httpx_post_kimi_aware` — function, line 959
- **called from:**
- `src/llm_core.py:2353`
- `tests/test_kimi_code_user_agent.py:90`

## `httpx_post_kimi_aware_async` — function (async), line 975
- **called from:**
- `src/llm_core.py:2788`
- `tests/test_kimi_code_user_agent.py:121`
- `tests/test_kimi_code_user_agent.py:157`

## `_detect_provider` — function, line 991
- **called from:**
- `routes/chat_routes.py:3179`
- `routes/gallery/gallery_routes.py:2267`
- `routes/model_routes.py:661`
- `scripts/dump_agent_prompt.py:279`
- `src/agent_tools/model_interaction_tools.py:153`
- `src/ai_interaction.py:140`
- `src/endpoint_resolver.py:274`
- `src/endpoint_resolver.py:298`
- `src/endpoint_resolver.py:320`
- `src/llm_core.py:1046`
- `src/llm_core.py:1631`
- `src/llm_core.py:1677`
- `src/llm_core.py:2213`
- `src/llm_core.py:2275`
- `src/llm_core.py:2287`
- `src/llm_core.py:2307`
- `src/llm_core.py:2641`
- `src/llm_core.py:2923`
- `src/llm_core.py:2969`
- `tests/test_cerebras_cache_affinity.py:12`
- `tests/test_copilot.py:26`
- `tests/test_copilot.py:27`
- `tests/test_copilot.py:29`
- `tests/test_llm_core_ollama.py:8`
- `tests/test_llm_core_ollama.py:9`
- `tests/test_llm_core_ollama.py:13`
- `tests/test_llm_core_ollama.py:14`
- `tests/test_llm_core_ollama.py:15`
- `tests/test_llm_core_temperature_moonshot.py:49`
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

## `_is_self_hosted_openai_compatible` — function, line 1029
- **called from:**
- `routes/chat_routes.py:3187`
- `src/llm_core.py:1070`
- `src/llm_core.py:1648`
- `src/llm_core.py:1691`
- `tests/test_cerebras_cache_affinity.py:18`

## `_apply_local_cache_affinity` — function, line 1052
- **called from:**
- `scripts/dump_agent_prompt.py:332`
- `src/llm_core.py:2773`
- `src/llm_core.py:3044`
- `tests/test_cache_affinity_local_only.py:20`
- `tests/test_cache_affinity_local_only.py:71`
- `tests/test_cerebras_cache_affinity.py:25`

## `_is_local_minimax_mlx_request` — function, line 1076
- **called from:**
- `src/llm_core.py:1096`

## `_apply_local_generation_stability` — function, line 1095
- **called from:**
- `scripts/dump_agent_prompt.py:333`
- `src/llm_core.py:2344`
- `src/llm_core.py:2774`
- `src/llm_core.py:3045`
- `tests/test_llm_core_temperature_reasoning.py:98`

## `_provider_headers` — function, line 1122
- **called from:**
- `src/llm_core.py:2275`
- `src/llm_core.py:2750`
- `src/llm_core.py:3007`
- `src/llm_core.py:3048`

## `_provider_label` — function, line 1140
- **called from:**
- `src/llm_core.py:1346`
- `tests/test_provider_classification.py:94`
- `tests/test_provider_classification.py:108`
- `tests/test_provider_classification.py:111`
- `tests/test_provider_classification.py:115`
- `tests/test_provider_label_js.py:54`

## `_is_openai_hosted_chat_url` — function, line 1187
- **called from:**
- `src/llm_core.py:1256`

## `_model_disallows_reasoning_effort_with_chat_tools` — function, line 1196
- **called from:**
- `src/llm_core.py:1258`
- `src/llm_core.py:1639`

## `_is_harmony_model` — function, line 1226
- **called from:**
- `src/llm_core.py:1233`
- `src/llm_core.py:1248`
- `tests/test_harmony_tool_aliasing.py:69`
- `tests/test_harmony_tool_aliasing.py:70`
- `tests/test_harmony_tool_aliasing.py:71`
- `tests/test_harmony_tool_aliasing.py:72`
- `tests/test_harmony_tool_aliasing.py:73`

## `_alias_harmony_tools` — function, line 1231
- **called from:**
- `src/llm_core.py:791`
- `src/llm_core.py:3025`
- `tests/test_harmony_tool_aliasing.py:37`
- `tests/test_harmony_tool_aliasing.py:44`
- `tests/test_harmony_tool_aliasing.py:51`
- `tests/test_harmony_tool_aliasing.py:77`
- `tests/test_harmony_tool_aliasing.py:78`

## `_unalias_harmony_tool_name` — function, line 1246
- **called from:**
- `src/llm_core.py:3237`
- `src/llm_core.py:3736`
- `tests/test_harmony_tool_aliasing.py:56`
- `tests/test_harmony_tool_aliasing.py:57`
- `tests/test_harmony_tool_aliasing.py:59`
- `tests/test_harmony_tool_aliasing.py:65`

## `_scrub_openai_chat_tool_reasoning` — function, line 1253
- **called from:**
- `scripts/dump_agent_prompt.py:334`
- `src/llm_core.py:3046`
- `tests/test_llm_core_openai_reasoning_tools.py:18`
- `tests/test_llm_core_openai_reasoning_tools.py:31`
- `tests/test_llm_core_openai_reasoning_tools.py:43`
- `tests/test_llm_core_openai_reasoning_tools.py:55`
- `tests/test_llm_core_openai_reasoning_tools.py:67`

## `_normalize_chatgpt_subscription_url` — function, line 1263
- **called from:**
- `scripts/dump_agent_prompt.py:305`
- `src/llm_core.py:2929`
- `src/llm_core.py:3006`

## `_message_content_as_text` — function, line 1270
- **called from:**
- `src/llm_core.py:1291`

## `_chatgpt_subscription_instructions` — function, line 1289
- **called from:**
- `src/llm_core.py:1314`

## `_build_chatgpt_responses_payload` — function, line 1301
- **called from:**
- `scripts/dump_agent_prompt.py:306`
- `src/llm_core.py:3008`
- `tests/test_llm_core_temperature_reasoning.py:115`
- `tests/test_llm_core_temperature_reasoning.py:126`

## `_format_chatgpt_subscription_error` — function, line 1327
- **called from:**
- `src/llm_core.py:3079`

## `_format_upstream_error` — function, line 1335
- **called from:**
- `src/llm_core.py:1332`
- `src/llm_core.py:2791`
- `src/llm_core.py:3200`
- `src/llm_core.py:3299`
- `src/llm_core.py:3504`
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

## `_uses_max_completion_tokens` — function, line 1379
- **called from:**
- `routes/email_pollers.py:1120`
- `routes/gallery/gallery_routes.py:2291`
- `routes/model_routes.py:733`
- `scripts/dump_agent_prompt.py:321`
- `src/llm_core.py:1637`
- `src/llm_core.py:1682`
- `src/llm_core.py:2342`
- `src/llm_core.py:2762`
- `src/llm_core.py:3022`
- `tests/test_provider_classification_token_params.py:26`
- `tests/test_provider_classification_token_params.py:34`

## `_restricts_temperature` — function, line 1395
- **called from:**
- `routes/gallery/gallery_routes.py:2305`
- `routes/model_routes.py:737`
- `src/llm_core.py:1319`
- `src/llm_core.py:1419`
- `tests/test_llm_core_temperature_reasoning.py:20`
- `tests/test_llm_core_temperature_reasoning.py:29`

## `_moonshot_rejects_custom_temperature` — function, line 1409
- **called from:**
- `src/llm_core.py:1419`
- `tests/test_llm_core_temperature_moonshot.py:24`
- `tests/test_llm_core_temperature_moonshot.py:38`

## `_omit_temperature` — function, line 1417
- **called from:**
- `scripts/dump_agent_prompt.py:316`
- `src/llm_core.py:2339`
- `src/llm_core.py:2759`
- `src/llm_core.py:3017`

## `_anthropic_rejects_temperature` — function, line 1429
- **called from:**
- `src/llm_core.py:1836`
- `tests/test_llm_core_anthropic_temp_omit.py:42`
- `tests/test_llm_core_anthropic_temp_omit.py:71`
- `tests/test_llm_core_anthropic_temp_omit.py:78`

## `_disable_deepseek_v4_thinking` — function, line 1470
- **called from:**
- `scripts/dump_agent_prompt.py:331`
- `src/llm_core.py:2347`
- `src/llm_core.py:2769`
- `src/llm_core.py:3039`
- `tests/test_sanitize_promotes_metadata_thinking.py:77`
- `tests/test_sanitize_promotes_metadata_thinking.py:89`
- `tests/test_sanitize_promotes_metadata_thinking.py:99`
- `tests/test_thinking_toggle.py:133`
- `tests/test_thinking_toggle.py:143`

## `_thinking_setting_off` — function, line 1497
- **called from:**
- `src/llm_core.py:2292`
- `src/llm_core.py:2639`
- `src/llm_core.py:2974`
- `tests/test_thinking_toggle.py:46`
- `tests/test_thinking_toggle.py:54`
- `tests/test_thinking_toggle.py:65`

## `normalize_reasoning_override` — function, line 1526
- **called from:**
- `src/llm_core.py:1542`
- `tests/test_nim_reasoning_control.py:59`
- `tests/test_nim_reasoning_control.py:60`
- `tests/test_nim_reasoning_control.py:61`
- `tests/test_nim_reasoning_control.py:62`

## `set_request_reasoning` — function, line 1540
- **called from:**
- `routes/chat_routes.py:942`
- `routes/chat_routes.py:1167`
- `tests/test_nim_reasoning_control.py:66`
- `tests/test_nim_reasoning_control.py:71`

## `_request_reasoning` — function, line 1545
- **called from:**
- `src/llm_core.py:1628`
- `src/llm_core.py:2291`
- `src/llm_core.py:2638`
- `src/llm_core.py:2973`
- `tests/test_nim_reasoning_control.py:68`

## `_nim_model_family` — function, line 1577
- **called from:**
- `src/llm_core.py:1599`

## `nim_reasoning_off_value` — function, line 1585
- **called from:**
- `routes/chat_routes.py:3184`
- `src/llm_core.py:1689`
- `tests/test_nim_reasoning_control.py:31`
- `tests/test_nim_reasoning_control.py:32`
- `tests/test_nim_reasoning_control.py:33`
- `tests/test_nim_reasoning_control.py:34`
- `tests/test_nim_reasoning_control.py:35`
- `tests/test_nim_reasoning_control.py:36`
- `tests/test_nim_reasoning_control.py:37`

## `nim_reasoning_levels` — function, line 1596
- **called from:**
- `routes/chat_routes.py:3183`
- `src/llm_core.py:1605`
- `tests/test_nim_reasoning_control.py:41`
- `tests/test_nim_reasoning_control.py:42`
- `tests/test_nim_reasoning_control.py:43`
- `tests/test_nim_reasoning_control.py:44`
- `tests/test_nim_reasoning_control.py:45`
- `tests/test_nim_reasoning_control.py:46`

## `_nim_clamp_level` — function, line 1602
- **called from:**
- `src/llm_core.py:1647`
- `tests/test_nim_reasoning_control.py:50`
- `tests/test_nim_reasoning_control.py:51`
- `tests/test_nim_reasoning_control.py:52`
- `tests/test_nim_reasoning_control.py:53`
- `tests/test_nim_reasoning_control.py:54`
- `tests/test_nim_reasoning_control.py:55`

## `_apply_request_reasoning_effort` — function, line 1617
- **called from:**
- `src/llm_core.py:2350`
- `src/llm_core.py:2772`
- `src/llm_core.py:3047`
- `tests/test_nim_reasoning_control.py:70`

## `_apply_thinking_off_openai_compat` — function, line 1654
- **called from:**
- `src/llm_core.py:2349`
- `src/llm_core.py:2771`
- `src/llm_core.py:3043`
- `tests/test_nim_reasoning_control.py:69`
- `tests/test_thinking_toggle.py:77`

## `_supports_thinking` — function, line 1701
- **called from:**
- `scripts/dump_agent_prompt.py:327`
- `scripts/dump_agent_prompt.py:329`
- `src/llm_core.py:2345`
- `src/llm_core.py:2765`
- `src/llm_core.py:2767`
- `src/llm_core.py:3032`
- `src/llm_core.py:3037`
- `src/llm_core.py:3465`
- `tests/test_llm_core_thinking_models.py:22`
- `tests/test_llm_core_thinking_models.py:27`

## `_normalize_mistral_content` — function, line 1708
- **called from:**
- `src/llm_core.py:2369`
- `src/llm_core.py:2831`
- `src/llm_core.py:3618`
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

## `_convert_openai_content_to_anthropic` — function, line 1740
- **called from:**
- `src/llm_core.py:1821`

## `_build_anthropic_payload` — function, line 1783
- **called from:**
- `routes/model_routes.py:719`
- `scripts/dump_agent_prompt.py:297`
- `src/llm_core.py:2320`
- `src/llm_core.py:2736`
- `src/llm_core.py:2993`
- `tests/test_approved_replay_message_shape.py:60`
- `tests/test_llm_core_anthropic_cache.py:7`
- `tests/test_llm_core_anthropic_temp_clamp.py:17`
- `tests/test_llm_core_anthropic_temp_omit.py:82`
- `tests/test_llm_core_sanitize_tool_calls.py:162`
- `tests/test_llm_core_system_msg_missing_content.py:27`
- `tests/test_llm_core_system_msg_missing_content.py:38`
- `tests/test_llm_core_system_msg_missing_content.py:49`
- `tests/test_llm_core_system_msg_missing_content.py:67`
- `tests/test_llm_core_temperature_anthropic.py:11`

## `_build_anthropic_headers` — function, line 1870
- **called from:**
- `routes/model_routes.py:718`
- `src/llm_core.py:2319`
- `src/llm_core.py:2735`
- `src/llm_core.py:2992`

## `_parse_anthropic_response` — function, line 1881
- **called from:**
- `src/llm_core.py:2361`
- `src/llm_core.py:2819`
- `tests/test_anthropic_response_parse.py:13`
- `tests/test_anthropic_response_parse.py:21`
- `tests/test_anthropic_response_parse.py:25`
- `tests/test_anthropic_response_parse.py:26`
- `tests/test_anthropic_response_parse.py:27`

## `_as_content_blocks` — function, line 1896
- **called from:**
- `src/llm_core.py:2098`
- `src/llm_core.py:2098`

## `_is_untrusted_context_content` — function, line 1910
- **called from:**
- `src/llm_core.py:1920`
- `src/llm_core.py:2087`

## `_sanitize_llm_messages` — function, line 1934
- **called from:**
- `scripts/dump_agent_prompt.py:280`
- `src/llm_core.py:2288`
- `src/llm_core.py:2642`
- `src/llm_core.py:2970`
- `tests/test_approved_replay_message_shape.py:59`
- `tests/test_approved_replay_message_shape.py:72`
- `tests/test_llm_core_sanitize_tool_calls.py:53`
- `tests/test_llm_core_sanitize_tool_calls.py:82`
- `tests/test_llm_core_sanitize_tool_calls.py:106`
- `tests/test_llm_core_sanitize_tool_calls.py:137`
- `tests/test_llm_core_sanitize_tool_calls.py:157`
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

## `_normalize_anthropic_url` — function, line 2118
- **called from:**
- `routes/model_routes.py:716`
- `scripts/dump_agent_prompt.py:296`
- `src/llm_core.py:2318`
- `src/llm_core.py:2734`
- `src/llm_core.py:2925`
- `src/llm_core.py:2991`

## `_model_list_base` — function, line 2128
- **called from:**
- `src/llm_core.py:2167`
- `src/llm_core.py:2184`

## `_parse_model_cache` — function, line 2140
- **called from:**
- `src/llm_core.py:2186`
- `src/llm_core.py:2189`

## `_configured_cached_model_ids` — function, line 2160
- **called from:**
- `src/llm_core.py:2210`

## `list_model_ids` — function, line 2201
- **called from:**
- `routes/email_routes.py:5258`
- `routes/session_routes.py:452`
- `routes/session_routes.py:472`
- `routes/skills_routes.py:1118`
- `routes/skills_routes.py:1519`
- `src/builtin_actions.py:1950`
- `src/llm_core.py:2259`
- `tests/test_llama_server_models_url.py:33`
- `tests/test_llm_core_ollama.py:124`
- `tests/test_lmstudio_models_url.py:133`
- `tests/test_lmstudio_models_url.py:156`
- `tests/test_lmstudio_models_url.py:174`
- `tests/test_model_routes.py:1978`

## `normalize_model_id` — function, line 2250
- **called from:**
- `routes/chat_helpers.py:876`

## `llm_call` — function, line 2271
- **called from:**
- `routes/session_routes.py:1461`
- `src/chat_processor.py:420`
- `src/document_processor.py:418`
- `src/llm_core.py:2463`
- `tests/test_llm_core_fallback.py:518`
- `tests/test_llm_core_fallback.py:524`
- `tests/test_llm_core_fallback.py:530`
- `tests/test_llm_core_ollama.py:35`
- `tests/test_llm_core_ollama.py:67`
- `tests/test_llm_core_ollama.py:101`
- `tests/test_llm_core_ollama.py:274`
- `tests/test_llm_core_reasoning_content_fallback.py:44`
- `tests/test_llm_core_reasoning_content_fallback.py:165`
- `tests/test_llm_core_temperature_moonshot.py:72`
- `tests/test_llm_core_temperature_reasoning.py:52`

## `_candidate_is_configured` — function, line 2382
- **called from:**
- `src/llm_core.py:2421`
- `src/llm_core.py:2541`
- `src/llm_core.py:3956`

## `_safe_route_descriptor` — function, line 2393
- **called from:**
- `src/llm_core.py:2429`

## `_dedupe_model_candidates_with_descriptors` — function, line 2413
- **called from:**
- `src/llm_core.py:2445`
- `src/llm_core.py:3959`

## `dedupe_model_candidates` — function, line 2433
- **called from:**
- `src/agent_loop.py:5346`
- `src/llm_core.py:2457`
- `src/llm_core.py:2496`
- `src/llm_core.py:2544`
- `tests/test_llm_core_fallback.py:1272`
- `tests/test_llm_core_fallback.py:1277`
- `tests/test_llm_core_fallback.py:1278`

## `llm_call_with_fallback` — function, line 2449
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_extract_finish_reason` — function, line 2472
- **called from:**
- `src/llm_core.py:2844`
- `tests/test_llm_core_reasoning_content_fallback.py:131`
- `tests/test_llm_core_reasoning_content_fallback.py:137`
- `tests/test_llm_core_reasoning_content_fallback.py:143`
- `tests/test_llm_core_reasoning_content_fallback.py:149`
- `tests/test_llm_core_reasoning_content_fallback.py:150`
- `tests/test_llm_core_reasoning_content_fallback.py:151`

## `llm_call_async_with_fallback` — function (async), line 2494
- **called from:**
- `mcp_servers/email_server.py:1849`
- `routes/email_routes.py:5071`
- `routes/email_routes.py:5364`
- `src/builtin_actions.py:599`
- `src/builtin_actions.py:1456`
- `src/builtin_actions.py:1731`
- `src/builtin_actions.py:2729`
- `src/task_endpoint.py:73`

## `_nonstream_error_status` — function, line 2511
- **called from:**
- `src/llm_core.py:2584`
- `src/llm_core.py:3983`

## `llm_call_async_with_route_fallback` — function (async), line 2524
- **called from:**
- `routes/chat_routes.py:1054`
- `tests/test_llm_core_fallback.py:735`
- `tests/test_llm_core_fallback.py:764`
- `tests/test_llm_core_fallback.py:1078`
- `tests/test_llm_core_fallback.py:1107`
- `tests/test_llm_core_fallback.py:1152`
- `tests/test_llm_core_fallback.py:1166`
- `tests/test_llm_core_fallback.py:1379`
- `tests/test_llm_core_fallback.py:1404`
- `tests/test_llm_core_fallback.py:1430`

## `llm_call_async` — function (async), line 2598
- **called from:**
- `routes/calendar_routes.py:1690`
- `routes/chat_helpers.py:330`
- `routes/document/document_routes.py:1014`
- `routes/document/document_routes.py:1326`
- `routes/email_helpers.py:325`
- `routes/email_routes.py:4866`
- `routes/email_routes.py:5396`
- `routes/history/history_routes.py:1134`
- `routes/memory/memory_routes.py:265`
- `routes/memory/memory_routes.py:457`
- `routes/note/note_routes.py:220`
- `routes/preset_routes.py:107`
- `routes/session_routes.py:650`
- `routes/session_routes.py:1238`
- `routes/skills_routes.py:259`
- `routes/skills_routes.py:309`
- `routes/skills_routes.py:397`
- `routes/skills_routes.py:832`
- `routes/task/task_routes.py:325`
- `routes/task/task_routes.py:1137`
- `routes/webhook/webhook_routes.py:381`
- `services/memory/memory_extractor.py:522`
- `services/memory/memory_extractor.py:733`
- `services/memory/skill_extractor.py:194`
- `src/agent_loop.py:3852`
- `src/agent_loop.py:5913`
- `src/agent_tools/model_interaction_tools.py:55`
- `src/agent_tools/model_interaction_tools.py:102`
- `src/agent_tools/session_tools.py:222`
- `src/ai_interaction.py:299`
- `src/context_compactor.py:518`
- `src/deep_research.py:385`
- `src/llm_core.py:2502`
- `src/llm_core.py:2563`
- `src/research_handler.py:150`
- `src/research_handler.py:182`
- `src/research_handler.py:725`
- `src/session_actions.py:186`
- `src/teacher_escalation.py:261`
- `src/teacher_escalation.py:435`
- `tests/test_llm_core_async_mistral_content.py:37`
- `tests/test_llm_core_fallback.py:817`
- `tests/test_llm_core_fallback.py:818`
- `tests/test_llm_core_reasoning_content_fallback.py:65`
- `tests/test_llm_core_reasoning_content_fallback.py:91`
- `tests/test_llm_core_reasoning_content_fallback.py:116`

## `_stream_target_url` — function, line 2922
- **called from:**
- `src/llm_core.py:2938`

## `stream_llm` — function (async), line 2933
- **called from:**
- `routes/chat_routes.py:3249`
- `src/llm_core.py:2677`
- `src/llm_core.py:4014`
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
- `tests/test_llm_core_streaming.py:57`
- `tests/test_llm_core_usage_finish_delta.py:58`

## `_stream_llm_inner` — function (async), line 2956
- **called from:**
- `src/llm_core.py:2940`
- `tests/test_llm_core_fallback.py:80`
- `tests/test_llm_core_fallback.py:1051`

## `_emit_tool_calls` — function, line 3474
- **called from:**
- `src/llm_core.py:3520`
- `src/llm_core.py:3762`

## `_format_routed_content` — function, line 3481
- **called from:**
- `src/llm_core.py:3518`
- `src/llm_core.py:3644`
- `src/llm_core.py:3749`
- `src/llm_core.py:3753`
- `src/llm_core.py:3760`

## `_summarize_stream_error` — function, line 3787
- **called from:**
- `src/llm_core.py:4001`
- `src/llm_core.py:4043`
- `src/llm_core.py:4089`
- `src/llm_core.py:4145`
- `tests/test_llm_core_fallback.py:1491`
- `tests/test_llm_core_fallback.py:1492`
- `tests/test_llm_core_fallback.py:1493`

## `_stream_error_status` — function, line 3805
- **called from:**
- `src/llm_core.py:4024`

## `_stream_error_fallback_override` — function, line 3821
- **called from:**
- `src/llm_core.py:4025`

## `_request_factory_error_chunk` — function, line 3837
- **called from:**
- `src/llm_core.py:3994`

## `_provider_stream_error_status` — function, line 3865
- **called from:**
- `src/llm_core.py:2805`
- `src/llm_core.py:3164`
- `src/llm_core.py:3212`
- `src/llm_core.py:3433`
- `src/llm_core.py:3532`
- `tests/test_llm_core_fallback.py:596`
- `tests/test_llm_core_fallback.py:607`
- `tests/test_llm_core_fallback.py:614`
- `tests/test_llm_core_fallback.py:623`
- `tests/test_llm_core_fallback.py:632`
- `tests/test_llm_core_fallback.py:778`

## `stream_llm_with_fallback` — function (async), line 3933
- **called from:**
- `routes/chat_routes.py:2223`
- `src/agent_loop.py:4273`
- `src/agent_loop.py:5483`
- `tests/test_llm_core_fallback.py:60`
- `tests/test_llm_core_fallback.py:224`
- `tests/test_llm_core_fallback.py:261`
- `tests/test_llm_core_fallback.py:410`
- `tests/test_llm_core_fallback.py:447`
- `tests/test_llm_core_fallback.py:483`
- `tests/test_llm_core_fallback.py:681`
- `tests/test_llm_core_fallback.py:708`
- `tests/test_llm_core_fallback.py:1219`
- `tests/test_llm_core_fallback.py:1295`
- `tests/test_llm_core_fallback.py:1320`
- `tests/test_llm_core_fallback.py:1357`
- `tests/test_llm_core_fallback.py:1458`
