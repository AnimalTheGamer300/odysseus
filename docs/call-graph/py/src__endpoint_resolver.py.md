# `src/endpoint_resolver.py` — definitions & call sites

32 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `endpoint_cost_tracked` — function, line 31
- **called from:**
- `src/endpoint_resolver.py:493`
- `src/endpoint_resolver.py:541`
- `src/endpoint_resolver.py:570`
- `src/foreground_model_routing.py:127`
- `tests/test_resolve_endpoint_fallbacks.py:325`
- `tests/test_resolve_endpoint_fallbacks.py:326`
- `tests/test_resolve_endpoint_fallbacks.py:327`
- `tests/test_resolve_endpoint_fallbacks.py:328`
- `tests/test_resolve_endpoint_fallbacks.py:329`
- `tests/test_resolve_endpoint_fallbacks.py:330`
- `tests/test_resolve_endpoint_fallbacks.py:331`
- `tests/test_resolve_endpoint_fallbacks.py:342`

## `_first_chat_model` — function, line 68
- **called from:**
- `routes/model_routes.py:2203`
- `routes/research/research_routes.py:201`
- `routes/research/research_routes.py:719`
- `src/endpoint_resolver.py:425`
- `src/endpoint_resolver.py:485`
- `tests/test_endpoint_resolver_models.py:21`
- `tests/test_endpoint_resolver_models.py:24`
- `tests/test_endpoint_resolver_models.py:27`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`
- `tests/test_provider_endpoints_models.py:15`
- `tests/test_provider_endpoints_models.py:20`
- `tests/test_provider_endpoints_models.py:25`

## `_endpoint_cached_models` — function, line 76
- **called from:**
- `src/endpoint_resolver.py:137`

## `_endpoint_pinned_models` — function, line 88
- **called from:**
- `src/endpoint_resolver.py:137`

## `_is_mlx_deepseek_v4_repo_id` — function, line 99
- **called from:**
- `routes/model_routes.py:1291`
- `src/endpoint_resolver.py:112`

## `_is_mlx_deepseek_v4_shim_id` — function, line 103
- **called from:**
- `routes/model_routes.py:1288`
- `routes/model_routes.py:1295`
- `src/endpoint_resolver.py:109`

## `_filter_mlx_deepseek_v4_repo_when_shimmed` — function, line 107
- **called from:**
- `routes/model_routes.py:1313`
- `src/endpoint_resolver.py:142`

## `_endpoint_hidden_models` — function, line 115
- **called from:**
- `src/endpoint_resolver.py:134`
- `src/endpoint_resolver.py:421`
- `src/endpoint_resolver.py:476`
- `src/endpoint_resolver.py:482`
- `tests/test_endpoint_resolver_models.py:63`

## `_endpoint_enabled_models` — function, line 127
- **called from:**
- `src/endpoint_resolver.py:425`
- `src/endpoint_resolver.py:471`
- `tests/test_endpoint_resolver_models.py:42`
- `tests/test_endpoint_resolver_models.py:46`
- `tests/test_endpoint_resolver_models.py:53`
- `tests/test_endpoint_resolver_models.py:66`

## `resolve_endpoint_runtime` — function, line 146
- **called from:**
- `routes/chat_helpers.py:538`
- `routes/chat_routes.py:762`
- `routes/model_routes.py:695`
- `routes/webhook/webhook_routes.py:334`
- `src/agent_loop.py:1091`
- `src/agent_tools/model_interaction_tools.py:150`
- `src/ai_interaction.py:137`
- `src/endpoint_resolver.py:410`
- `src/endpoint_resolver.py:464`

## `_resolve_tailscale_host` — function, line 169
- **called from:**
- `src/endpoint_resolver.py:215`

## `resolve_url` — function, line 209
- **called from:**
- `routes/model_routes.py:963`
- `routes/model_routes.py:1072`
- `routes/model_routes.py:2016`
- `routes/model_routes.py:2239`
- `src/endpoint_resolver.py:247`
- `tests/test_provider_endpoints_tailscale.py:30`
- `tests/test_provider_endpoints_tailscale.py:46`
- `tests/test_provider_endpoints_tailscale.py:56`
- `tests/test_provider_endpoints_tailscale.py:59`

## `normalize_base` — function, line 225
- **called from:**
- `routes/chat_helpers.py:492`
- `routes/chat_helpers.py:596`
- `routes/chat_helpers.py:612`
- `routes/chat_routes.py:854`
- `routes/compare/compare_routes.py:151`
- `routes/compare/compare_routes.py:173`
- `routes/research/research_routes.py:711`
- `routes/session_routes.py:429`
- `routes/session_routes.py:578`
- `routes/webhook/webhook_routes.py:299`
- `routes/webhook/webhook_routes.py:327`
- `src/agent_loop.py:1047`
- `src/agent_tools/spawn_agent_tools.py:90`
- `src/agent_tools/spawn_agent_tools.py:90`
- `src/agent_tools/spawn_agent_tools.py:91`
- `src/endpoint_resolver.py:153`
- `src/endpoint_resolver.py:160`
- `src/endpoint_resolver.py:246`
- `src/endpoint_resolver.py:247`
- `src/task_scheduler.py:337`
- `src/task_scheduler.py:1880`
- `src/task_scheduler.py:1880`
- `src/task_scheduler.py:1881`
- `src/task_scheduler.py:2056`
- `src/task_scheduler.py:2056`
- `src/task_scheduler.py:2057`
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

## `_validated_endpoint_base` — function, line 237
- **called from:**
- `src/endpoint_resolver.py:246`
- `src/endpoint_resolver.py:247`

## `_prepare_endpoint_base` — function, line 245
- **called from:**
- `src/endpoint_resolver.py:273`
- `src/endpoint_resolver.py:297`

## `_append_endpoint_path` — function, line 250
- **called from:**
- `src/endpoint_resolver.py:276`
- `src/endpoint_resolver.py:278`
- `src/endpoint_resolver.py:280`
- `src/endpoint_resolver.py:282`
- `src/endpoint_resolver.py:283`
- `src/endpoint_resolver.py:300`
- `src/endpoint_resolver.py:302`
- `src/endpoint_resolver.py:314`
- `src/endpoint_resolver.py:315`

## `_pathless_host` — function, line 258
- **called from:**
- `src/endpoint_resolver.py:281`

## `_anthropic_api_root` — function, line 263
- **called from:**
- `src/endpoint_resolver.py:276`
- `src/endpoint_resolver.py:300`
- `tests/test_provider_endpoints_normalization.py:39`

## `build_chat_url` — function, line 271
- **called from:**
- `companion/routes.py:154`
- `routes/chat_helpers.py:496`
- `routes/chat_routes.py:580`
- `routes/chat_routes.py:854`
- `routes/compare/compare_routes.py:173`
- `routes/model_routes.py:724`
- `routes/model_routes.py:729`
- `routes/model_routes.py:1570`
- `routes/model_routes.py:2485`
- `routes/model_routes.py:2618`
- `routes/research/research_routes.py:206`
- `routes/research/research_routes.py:712`
- `routes/session_routes.py:429`
- `routes/session_routes.py:578`
- `routes/webhook/webhook_routes.py:300`
- `routes/webhook/webhook_routes.py:328`
- `routes/webhook/webhook_routes.py:335`
- `src/ai_interaction.py:151`
- `src/ai_interaction.py:189`
- `src/ai_interaction.py:194`
- `src/ai_interaction.py:201`
- `src/endpoint_resolver.py:414`
- `src/endpoint_resolver.py:468`
- `src/task_scheduler.py:337`
- `tests/test_endpoint_owner_scope_followup.py:229`
- `tests/test_endpoint_owner_scope_followup.py:314`
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
- `tests/test_provider_detection_builders.py:79`
- `tests/test_provider_endpoints_url_building.py:71`
- `tests/test_provider_endpoints_url_building.py:84`

## `build_models_url` — function, line 286
- **called from:**
- `routes/model_routes.py:670`
- `routes/model_routes.py:1178`
- `routes/webhook/webhook_routes.py:342`
- `src/agent_tools/model_interaction_tools.py:161`
- `src/ai_interaction.py:156`
- `src/llm_core.py:2225`
- `src/model_context.py:436`
- `src/model_context.py:517`
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

## `build_headers` — function, line 318
- **called from:**
- `routes/chat_helpers.py:545`
- `routes/chat_routes.py:855`
- `routes/compare/compare_routes.py:178`
- `routes/model_routes.py:681`
- `routes/research/research_routes.py:206`
- `routes/research/research_routes.py:713`
- `routes/session_routes.py:442`
- `routes/session_routes.py:510`
- `routes/session_routes.py:586`
- `routes/webhook/webhook_routes.py:310`
- `routes/webhook/webhook_routes.py:343`
- `routes/webhook/webhook_routes.py:372`
- `src/agent_loop.py:1094`
- `src/agent_tools/model_interaction_tools.py:154`
- `src/agent_tools/spawn_agent_tools.py:91`
- `src/ai_interaction.py:141`
- `src/endpoint_resolver.py:415`
- `src/endpoint_resolver.py:469`
- `src/task_scheduler.py:1881`
- `src/task_scheduler.py:2057`
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

## `resolve_endpoint` — function, line 343
- **called from:**
- `mcp_servers/email_server.py:1832`
- `mcp_servers/email_server.py:1836`
- `routes/calendar_routes.py:1657`
- `routes/calendar_routes.py:1659`
- `routes/document/document_routes.py:979`
- `routes/email_routes.py:4841`
- `routes/email_routes.py:4843`
- `routes/email_routes.py:4927`
- `routes/email_routes.py:4929`
- `routes/email_routes.py:5059`
- `routes/email_routes.py:5063`
- `routes/email_routes.py:5243`
- `routes/email_routes.py:5245`
- `routes/email_routes.py:5346`
- `routes/email_routes.py:5352`
- `routes/history/history_routes.py:1126`
- `routes/memory/memory_routes.py:368`
- `routes/note/note_routes.py:214`
- `routes/note/note_routes.py:216`
- `routes/research/research_routes.py:143`
- `routes/research/research_routes.py:530`
- `routes/research/research_routes.py:532`
- `routes/research/research_routes.py:538`
- `routes/research/research_routes.py:540`
- `routes/research/research_routes.py:698`
- `routes/research/research_routes.py:700`
- `routes/research/research_routes.py:702`
- `routes/session_routes.py:252`
- `routes/session_routes.py:264`
- `routes/session_routes.py:642`
- `routes/session_routes.py:1217`
- `routes/skills_routes.py:1112`
- `routes/skills_routes.py:1507`
- `routes/task/task_routes.py:1132`
- `routes/task/task_routes.py:1134`
- `src/context_compactor.py:469`
- `src/task_endpoint.py:18`
- `src/task_endpoint.py:46`
- `src/task_endpoint.py:47`
- `src/task_scheduler.py:2022`
- `src/teacher_escalation.py:419`
- `tests/test_resolve_endpoint_fallbacks.py:95`
- `tests/test_resolve_endpoint_fallbacks.py:117`
- `tests/test_resolve_endpoint_fallbacks.py:135`
- `tests/test_resolve_endpoint_fallbacks.py:154`
- `tests/test_resolve_endpoint_fallbacks.py:174`
- `tests/test_resolve_endpoint_fallbacks.py:201`

## `_stg` — function, line 369
- **called from:**
- `src/endpoint_resolver.py:372`
- `src/endpoint_resolver.py:373`
- `src/endpoint_resolver.py:377`
- `src/endpoint_resolver.py:378`
- `src/endpoint_resolver.py:389`
- `src/endpoint_resolver.py:390`

## `_resolve_endpoint_by_id_with_descriptor` — function, line 437
- **called from:**
- `src/endpoint_resolver.py:515`
- `src/endpoint_resolver.py:551`
- `src/endpoint_resolver.py:589`
- `src/endpoint_resolver.py:659`

## `resolve_endpoint_by_id` — function, line 506
- **called from:**
- `src/endpoint_resolver.py:635`
- `tests/test_resolve_endpoint_fallbacks.py:219`
- `tests/test_resolve_endpoint_fallbacks.py:224`
- `tests/test_resolve_endpoint_fallbacks.py:230`

## `resolve_route_descriptor` — function, line 524
- **called from:**
- `src/foreground_model_routing.py:194`

## `resolve_route_descriptor_by_id` — function, line 574
- **called from:**
- `src/foreground_model_routing.py:186`

## `resolve_utility_fallback_candidates` — function, line 603
- **called from:**
- `mcp_servers/email_server.py:1840`
- `mcp_servers/email_server.py:1842`
- `routes/email_routes.py:5066`
- `routes/email_routes.py:5357`
- `src/task_endpoint.py:48`
- `tests/test_foreground_model_routing.py:2224`

## `resolve_vision_fallback_candidates` — function, line 608
- **called from:**
- `src/document_processor.py:411`

## `_resolve_fallback_candidates` — function, line 613
- **called from:**
- `src/endpoint_resolver.py:605`
- `src/endpoint_resolver.py:610`

## `resolve_fallback_entries` — function, line 623
- **called from:**
- `src/endpoint_resolver.py:620`
- `src/foreground_model_routing.py:98`
- `tests/test_resolve_endpoint_fallbacks.py:254`

## `resolve_fallback_entries_with_descriptors` — function, line 646
- **called from:**
- `src/foreground_model_routing.py:131`
- `tests/test_resolve_endpoint_fallbacks.py:271`
