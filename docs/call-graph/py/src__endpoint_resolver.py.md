# `src/endpoint_resolver.py` — definitions & call sites

39 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `endpoint_cost_tracked` — function, line 32
- **called from:**
- `src/endpoint_resolver.py:590`
- `src/endpoint_resolver.py:638`
- `src/endpoint_resolver.py:667`
- `src/foreground_model_routing.py:127`
- `src/foreground_model_routing.py:200`
- `tests/test_resolve_endpoint_fallbacks.py:325`
- `tests/test_resolve_endpoint_fallbacks.py:326`
- `tests/test_resolve_endpoint_fallbacks.py:327`
- `tests/test_resolve_endpoint_fallbacks.py:328`
- `tests/test_resolve_endpoint_fallbacks.py:329`
- `tests/test_resolve_endpoint_fallbacks.py:330`
- `tests/test_resolve_endpoint_fallbacks.py:331`
- `tests/test_resolve_endpoint_fallbacks.py:342`

## `_running_in_container` — function, line 69
- **called from:**
- `routes/shell_routes.py:2018`
- `src/endpoint_resolver.py:84`
- `tests/test_shell_routes.py:504`
- `tests/test_shell_routes.py:515`
- `tests/test_shell_routes.py:526`
- `tests/test_shell_routes.py:535`

## `_rewrite_docker_host_for_native_runtime` — function, line 82
- **called from:**
- `src/agent_loop.py:26863`
- `src/endpoint_resolver.py:178`
- `src/endpoint_resolver.py:187`
- `tests/test_provider_endpoints_normalization.py:32`
- `tests/test_provider_endpoints_normalization.py:40`

## `_first_chat_model` — function, line 93
- **called from:**
- `routes/model_routes.py:2386`
- `routes/research/research_routes.py:203`
- `src/editor_agent_model.py:547`
- `src/endpoint_resolver.py:522`
- `src/endpoint_resolver.py:582`
- `tests/test_endpoint_resolver_models.py:21`
- `tests/test_endpoint_resolver_models.py:24`
- `tests/test_endpoint_resolver_models.py:27`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`
- `tests/test_provider_endpoints_models.py:15`
- `tests/test_provider_endpoints_models.py:20`
- `tests/test_provider_endpoints_models.py:25`

## `_endpoint_cached_models` — function, line 101
- **called from:**
- `src/endpoint_resolver.py:162`

## `_endpoint_pinned_models` — function, line 113
- **called from:**
- `src/endpoint_resolver.py:162`

## `_is_mlx_deepseek_v4_repo_id` — function, line 124
- **called from:**
- `routes/model_routes.py:1374`
- `src/endpoint_resolver.py:137`

## `_is_mlx_deepseek_v4_shim_id` — function, line 128
- **called from:**
- `routes/model_routes.py:1371`
- `routes/model_routes.py:1378`
- `src/endpoint_resolver.py:134`

## `_filter_mlx_deepseek_v4_repo_when_shimmed` — function, line 132
- **called from:**
- `routes/model_routes.py:1396`
- `src/endpoint_resolver.py:167`

## `_endpoint_hidden_models` — function, line 140
- **called from:**
- `src/editor_agent_model.py:470`
- `src/editor_agent_model.py:538`
- `src/endpoint_resolver.py:159`
- `src/endpoint_resolver.py:518`
- `src/endpoint_resolver.py:573`
- `src/endpoint_resolver.py:579`
- `tests/test_endpoint_resolver_models.py:63`

## `_endpoint_enabled_models` — function, line 152
- **called from:**
- `routes/chat_routes.py:2127`
- `routes/editor_agent_routes.py:2017`
- `routes/research/research_routes.py:201`
- `routes/task/task_routes.py:300`
- `src/editor_agent_model.py:469`
- `src/editor_agent_model.py:537`
- `src/endpoint_resolver.py:522`
- `src/endpoint_resolver.py:568`
- `tests/test_endpoint_resolver_models.py:42`
- `tests/test_endpoint_resolver_models.py:46`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`

## `resolve_endpoint_runtime` — function, line 171
- **called from:**
- `routes/chat_helpers.py:666`
- `routes/chat_helpers.py:734`
- `routes/chat_helpers.py:1082`
- `routes/chat_routes.py:2136`
- `routes/model_routes.py:749`
- `routes/skills_routes.py:631`
- `routes/webhook/webhook_routes.py:334`
- `services/skills/model_selection.py:34`
- `src/agent_loop.py:8705`
- `src/agent_loop.py:8797`
- `src/agent_tools/model_interaction_tools.py:206`
- `src/ai_interaction.py:138`
- `src/chat_helpers.py:372`
- `src/chat_helpers.py:392`
- `src/editor_agent_model.py:477`
- `src/editor_agent_model.py:551`
- `src/endpoint_resolver.py:507`
- `src/endpoint_resolver.py:561`
- `src/task_endpoint.py:59`
- `src/task_scheduler.py:2043`
- `src/task_scheduler.py:2248`
- `tests/test_endpoint_registered_authority.py:118`

## `_resolve_tailscale_host` — function, line 198
- **called from:**
- `src/endpoint_resolver.py:244`

## `resolve_url` — function, line 238
- **called from:**
- `routes/model_routes.py:1019`
- `routes/model_routes.py:1130`
- `routes/model_routes.py:2171`
- `routes/model_routes.py:2424`
- `src/agent_runtime/context_resolution.py:265`
- `src/endpoint_resolver.py:344`
- `tests/test_provider_endpoints_tailscale.py:30`
- `tests/test_provider_endpoints_tailscale.py:46`
- `tests/test_provider_endpoints_tailscale.py:56`
- `tests/test_provider_endpoints_tailscale.py:59`

## `normalize_base` — function, line 254
- **called from:**
- `routes/chat_helpers.py:974`
- `routes/chat_helpers.py:1128`
- `routes/chat_helpers.py:1144`
- `routes/chat_routes.py:2237`
- `routes/compare/compare_routes.py:151`
- `routes/compare/compare_routes.py:173`
- `routes/session_routes.py:500`
- `routes/session_routes.py:591`
- `routes/session_routes.py:758`
- `routes/webhook/webhook_routes.py:299`
- `routes/webhook/webhook_routes.py:327`
- `services/skills/model_selection.py:32`
- `src/agent_loop.py:8656`
- `src/agent_tools/spawn_agent_tools.py:90`
- `src/agent_tools/spawn_agent_tools.py:90`
- `src/agent_tools/spawn_agent_tools.py:91`
- `src/chat_helpers.py:373`
- `src/chat_helpers.py:393`
- `src/endpoint_resolver.py:179`
- `src/endpoint_resolver.py:188`
- `src/endpoint_resolver.py:269`
- `src/endpoint_resolver.py:317`
- `src/endpoint_resolver.py:331`
- `src/endpoint_resolver.py:343`
- `src/endpoint_resolver.py:344`
- `src/task_scheduler.py:379`
- `tests/test_endpoint_owner_scope_followup.py:166`
- `tests/test_endpoint_owner_scope_followup.py:229`
- `tests/test_endpoint_owner_scope_followup.py:314`
- `tests/test_endpoint_resolver_urls.py:13`
- `tests/test_endpoint_resolver_urls.py:16`
- `tests/test_endpoint_resolver_urls.py:19`
- `tests/test_endpoint_resolver_urls.py:22`
- `tests/test_endpoint_resolver_urls.py:25`
- `tests/test_endpoint_resolver_urls.py:28`
- `tests/test_endpoint_resolver_urls.py:31`
- `tests/test_endpoint_resolver_urls.py:34`
- `tests/test_endpoint_resolver_urls.py:37`
- `tests/test_provider_endpoints_normalization.py:27`

## `same_endpoint_base` — function, line 266
- **called from:**
- `services/skills/model_selection.py:33`
- `src/utility_effort.py:104`

## `identity` — function, line 268
- **called from:**
- `src/endpoint_resolver.py:278`
- `src/endpoint_resolver.py:279`
- `tests/process_resource_helpers.py:36`
- `tests/process_resource_helpers.py:41`
- `static/js/emailLibrary/index.js:304`
- `static/js/presets.js:746`

## `_registered_endpoint_url_identity` — function, line 284
- **called from:**
- `src/endpoint_resolver.py:312`
- `src/endpoint_resolver.py:318`
- `src/endpoint_resolver.py:323`

## `resolve_owner_registered_endpoint` — function, line 303
- **called from:**
- `routes/chat_helpers.py:665`
- `routes/chat_helpers.py:733`
- `routes/skills_routes.py:630`
- `src/chat_helpers.py:371`
- `src/chat_helpers.py:391`
- `src/endpoint_resolver.py:330`
- `src/task_endpoint.py:58`
- `src/task_scheduler.py:1692`
- `src/task_scheduler.py:2042`
- `src/task_scheduler.py:2213`
- `src/task_scheduler.py:2247`
- `tests/test_endpoint_registered_authority.py:116`
- `tests/test_endpoint_registered_authority.py:150`
- `tests/test_endpoint_registered_authority.py:164`

## `resolve_owner_registered_endpoint_url` — function, line 328
- **called from:**
- `routes/assistant_routes.py:184`
- `routes/task/task_routes.py:523`
- `routes/task/task_routes.py:765`
- `tests/test_endpoint_registered_authority.py:115`
- `tests/test_endpoint_registered_authority.py:124`
- `tests/test_endpoint_registered_authority.py:181`
- `tests/test_endpoint_registered_authority.py:187`
- `tests/test_endpoint_registered_authority.py:197`

## `_validated_endpoint_base` — function, line 334
- **called from:**
- `src/endpoint_resolver.py:343`
- `src/endpoint_resolver.py:344`

## `_prepare_endpoint_base` — function, line 342
- **called from:**
- `src/endpoint_resolver.py:370`
- `src/endpoint_resolver.py:394`

## `_append_endpoint_path` — function, line 347
- **called from:**
- `src/endpoint_resolver.py:373`
- `src/endpoint_resolver.py:375`
- `src/endpoint_resolver.py:377`
- `src/endpoint_resolver.py:379`
- `src/endpoint_resolver.py:380`
- `src/endpoint_resolver.py:397`
- `src/endpoint_resolver.py:399`
- `src/endpoint_resolver.py:411`
- `src/endpoint_resolver.py:412`

## `_pathless_host` — function, line 355
- **called from:**
- `src/endpoint_resolver.py:378`

## `_anthropic_api_root` — function, line 360
- **called from:**
- `src/endpoint_resolver.py:373`
- `src/endpoint_resolver.py:397`
- `tests/test_provider_endpoints_normalization.py:52`

## `build_chat_url` — function, line 368
- **called from:**
- `companion/routes.py:154`
- `routes/chat_helpers.py:667`
- `routes/chat_helpers.py:735`
- `routes/chat_helpers.py:978`
- `routes/chat_routes.py:1923`
- `routes/chat_routes.py:2237`
- `routes/compare/compare_routes.py:173`
- `routes/model_routes.py:778`
- `routes/model_routes.py:783`
- `routes/model_routes.py:1703`
- `routes/model_routes.py:2850`
- `routes/model_routes.py:2998`
- `routes/research/research_routes.py:208`
- `routes/session_routes.py:500`
- `routes/session_routes.py:591`
- `routes/session_routes.py:758`
- `routes/skills_routes.py:632`
- `routes/webhook/webhook_routes.py:300`
- `routes/webhook/webhook_routes.py:328`
- `routes/webhook/webhook_routes.py:335`
- `src/ai_interaction.py:152`
- `src/ai_interaction.py:195`
- `src/ai_interaction.py:200`
- `src/ai_interaction.py:207`
- `src/editor_agent_model.py:479`
- `src/editor_agent_model.py:553`
- `src/endpoint_resolver.py:323`
- `src/endpoint_resolver.py:511`
- `src/endpoint_resolver.py:565`
- `src/task_endpoint.py:60`
- `src/task_scheduler.py:379`
- `src/task_scheduler.py:2044`
- `src/task_scheduler.py:2249`
- `tests/test_endpoint_owner_scope_followup.py:229`
- `tests/test_endpoint_owner_scope_followup.py:314`
- `tests/test_endpoint_registered_authority.py:112`
- `tests/test_endpoint_registered_authority.py:179`
- `tests/test_endpoint_resolver_urls.py:42`
- `tests/test_endpoint_resolver_urls.py:45`
- `tests/test_endpoint_resolver_urls.py:48`
- `tests/test_endpoint_resolver_urls.py:51`
- `tests/test_endpoint_resolver_urls.py:54`
- `tests/test_endpoint_resolver_urls.py:57`
- `tests/test_endpoint_resolver_urls.py:60`
- `tests/test_endpoint_resolver_urls.py:63`
- `tests/test_endpoint_resolver_urls.py:66`
- `tests/test_endpoint_resolver_urls.py:75`
- `tests/test_ollama_port_detection.py:83`
- `tests/test_ollama_port_detection.py:86`
- `tests/test_ollama_port_detection.py:89`
- `tests/test_ollama_port_detection.py:98`
- `tests/test_ollama_port_detection.py:101`
- `tests/test_ollama_port_detection.py:104`
- `tests/test_provider_detection_builders.py:32`
- `tests/test_provider_detection_builders.py:35`
- `tests/test_provider_detection_builders.py:41`
- `tests/test_provider_detection_builders.py:48`
- `tests/test_provider_detection_builders.py:51`
- `tests/test_provider_detection_builders.py:54`
- `tests/test_provider_detection_builders.py:73`
- … +4 more (grep the name in repo)

## `build_models_url` — function, line 383
- **called from:**
- `routes/model_routes.py:724`
- `routes/model_routes.py:1261`
- `routes/webhook/webhook_routes.py:342`
- `src/agent_runtime/context_resolution.py:265`
- `src/agent_tools/model_interaction_tools.py:217`
- `src/ai_interaction.py:157`
- `src/llm_core.py:2551`
- `src/model_context.py:438`
- `src/model_context.py:533`
- `tests/test_endpoint_resolver_urls.py:80`
- `tests/test_endpoint_resolver_urls.py:83`
- `tests/test_endpoint_resolver_urls.py:86`
- `tests/test_endpoint_resolver_urls.py:95`
- `tests/test_llama_server_models_url.py:12`
- `tests/test_llama_server_models_url.py:16`
- `tests/test_lmstudio_models_url.py:43`
- `tests/test_lmstudio_models_url.py:54`
- `tests/test_lmstudio_models_url.py:65`
- `tests/test_lmstudio_models_url.py:76`
- `tests/test_lmstudio_models_url.py:89`
- `tests/test_lmstudio_models_url.py:104`
- `tests/test_provider_detection_builders.py:38`
- `tests/test_provider_detection_builders.py:45`
- `tests/test_provider_detection_builders.py:58`
- `tests/test_provider_detection_builders.py:76`
- `tests/test_provider_detection_builders.py:82`
- `tests/test_provider_endpoints_url_building.py:79`

## `build_headers` — function, line 415
- **called from:**
- `routes/chat_helpers.py:668`
- `routes/chat_helpers.py:736`
- `routes/chat_helpers.py:1089`
- `routes/chat_routes.py:2238`
- `routes/compare/compare_routes.py:178`
- `routes/model_routes.py:735`
- `routes/research/research_routes.py:208`
- `routes/session_routes.py:604`
- `routes/session_routes.py:675`
- `routes/session_routes.py:772`
- `routes/skills_routes.py:633`
- `routes/webhook/webhook_routes.py:310`
- `routes/webhook/webhook_routes.py:343`
- `routes/webhook/webhook_routes.py:372`
- `services/skills/model_selection.py:35`
- `src/agent_loop.py:8708`
- `src/agent_loop.py:8800`
- `src/agent_tools/model_interaction_tools.py:210`
- `src/agent_tools/spawn_agent_tools.py:91`
- `src/ai_interaction.py:142`
- `src/editor_agent_model.py:481`
- `src/editor_agent_model.py:555`
- `src/endpoint_resolver.py:512`
- `src/endpoint_resolver.py:566`
- `src/task_endpoint.py:60`
- `src/task_scheduler.py:2045`
- `src/task_scheduler.py:2250`
- `tests/test_copilot.py:64`
- `tests/test_copilot.py:68`
- `tests/test_endpoint_owner_scope_followup.py:315`
- `tests/test_endpoint_resolver_headers.py:7`
- `tests/test_endpoint_resolver_headers.py:10`
- `tests/test_endpoint_resolver_headers.py:13`
- `tests/test_endpoint_resolver_headers.py:16`
- `tests/test_provider_endpoints_headers.py:13`
- `tests/test_provider_endpoints_headers.py:20`
- `tests/test_provider_endpoints_headers.py:34`
- `tests/test_provider_endpoints_headers.py:41`
- `tests/test_provider_endpoints_headers.py:49`
- `tests/test_task_scheduler_endpoint_authority.py:93`
- `tests/test_task_scheduler_endpoint_authority.py:109`
- `tests/test_task_scheduler_endpoint_authority.py:164`

## `resolve_endpoint` — function, line 440
- **called from:**
- `mcp_servers/email_server.py:3079`
- `mcp_servers/email_server.py:3083`
- `routes/auth_routes.py:866`
- `routes/auth_routes.py:868`
- `routes/calendar_routes.py:1832`
- `routes/calendar_routes.py:1834`
- `routes/chat_helpers.py:742`
- `routes/document/document_routes.py:1203`
- `routes/email/email_routes.py:6537`
- `routes/email/email_routes.py:6539`
- `routes/email/email_routes.py:6628`
- `routes/email/email_routes.py:6630`
- `routes/email/email_routes.py:6761`
- `routes/email/email_routes.py:6765`
- `routes/email/email_routes.py:6980`
- `routes/email/email_routes.py:6982`
- `routes/email/email_routes.py:7093`
- `routes/email/email_routes.py:7099`
- `routes/history/history_routes.py:1510`
- `routes/memory/memory_routes.py:372`
- `routes/note/note_routes.py:217`
- `routes/note/note_routes.py:219`
- `routes/research/research_routes.py:144`
- `routes/research/research_routes.py:592`
- `routes/research/research_routes.py:594`
- `routes/research/research_routes.py:600`
- `routes/research/research_routes.py:602`
- `routes/research/research_routes.py:820`
- `routes/research/research_routes.py:822`
- `routes/research/research_routes.py:824`
- `routes/session_routes.py:388`
- `routes/session_routes.py:400`
- `routes/session_routes.py:836`
- `routes/session_routes.py:1364`
- `routes/skills_routes.py:625`
- `routes/task/task_routes.py:1204`
- `routes/task/task_routes.py:1206`
- `services/skills/model_selection.py:43`
- `src/context_compactor.py:732`
- `src/editor_agent_model.py:390`
- `src/editor_agent_model.py:434`
- `src/editor_agent_model.py:574`
- `src/editor_agent_model.py:669`
- `src/task_endpoint.py:19`
- `src/task_endpoint.py:68`
- `src/task_endpoint.py:69`
- `src/task_scheduler.py:2218`
- `src/teacher_escalation.py:475`
- `src/utility_effort.py:25`
- `tests/test_resolve_endpoint_fallbacks.py:95`
- `tests/test_resolve_endpoint_fallbacks.py:117`
- `tests/test_resolve_endpoint_fallbacks.py:135`
- `tests/test_resolve_endpoint_fallbacks.py:154`
- `tests/test_resolve_endpoint_fallbacks.py:174`
- `tests/test_resolve_endpoint_fallbacks.py:201`

## `_stg` — function, line 466
- **called from:**
- `src/endpoint_resolver.py:469`
- `src/endpoint_resolver.py:470`
- `src/endpoint_resolver.py:474`
- `src/endpoint_resolver.py:475`
- `src/endpoint_resolver.py:486`
- `src/endpoint_resolver.py:487`

## `_resolve_endpoint_by_id_with_descriptor` — function, line 534
- **called from:**
- `src/endpoint_resolver.py:612`
- `src/endpoint_resolver.py:648`
- `src/endpoint_resolver.py:686`
- `src/endpoint_resolver.py:756`

## `resolve_endpoint_by_id` — function, line 603
- **called from:**
- `src/endpoint_resolver.py:732`
- `src/utility_effort.py:59`
- `tests/test_resolve_endpoint_fallbacks.py:219`
- `tests/test_resolve_endpoint_fallbacks.py:224`
- `tests/test_resolve_endpoint_fallbacks.py:230`
- `tests/test_resolve_session_auth_chatgpt.py:321`
- `tests/test_resolve_session_auth_chatgpt.py:322`

## `resolve_route_descriptor` — function, line 621
- **called from:**
- `src/foreground_model_routing.py:203`

## `resolve_route_descriptor_by_id` — function, line 671
- **called from:**
- `src/foreground_model_routing.py:186`
- `tests/test_resolve_session_auth_chatgpt.py:328`
- `tests/test_resolve_session_auth_chatgpt.py:329`
- `tests/test_resolve_session_auth_chatgpt.py:333`

## `resolve_utility_fallback_candidates` — function, line 700
- **called from:**
- `mcp_servers/email_server.py:3087`
- `mcp_servers/email_server.py:3089`
- `routes/email/email_routes.py:6768`
- `routes/email/email_routes.py:7104`
- `services/skills/model_selection.py:48`
- `src/task_endpoint.py:70`
- `src/utility_effort.py:26`
- `tests/test_foreground_model_routing.py:2308`

## `resolve_vision_fallback_candidates` — function, line 705
- **called from:**
- `src/document_processor.py:517`

## `_resolve_fallback_candidates` — function, line 710
- **called from:**
- `src/endpoint_resolver.py:702`
- `src/endpoint_resolver.py:707`

## `resolve_fallback_entries` — function, line 720
- **called from:**
- `src/endpoint_resolver.py:717`
- `src/foreground_model_routing.py:98`
- `tests/test_resolve_endpoint_fallbacks.py:254`

## `resolve_fallback_entries_with_descriptors` — function, line 743
- **called from:**
- `src/foreground_model_routing.py:131`
- `tests/test_resolve_endpoint_fallbacks.py:271`
