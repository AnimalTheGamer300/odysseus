# `services/search/core.py` — definitions & call sites

33 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_secret_key` — function, line 65
- **called from:**
- `services/search/core.py:90`
- `services/search/core.py:105`
- `tests/test_search_config_no_key_leak.py:50`
- `tests/test_search_config_no_key_leak.py:51`
- `tests/test_search_config_no_key_leak.py:52`
- `tests/test_search_config_no_key_leak.py:53`

## `get_search_config` — function, line 70
- **called from:**
- `routes/search/search_routes.py:145`
- `services/search/service.py:102`
- `tests/test_search_config_no_key_leak.py:37`
- `tests/test_search_config_provider_key.py:17`
- `tests/test_search_config_provider_key.py:55`

## `update_search_config` — function, line 94
- **called from:**
- `src/app_initializer.py:148`
- `tests/test_search_config_no_key_leak.py:21`

## `_call_provider` — function, line 109
- **called from:**
- `routes/search/search_routes.py:204`
- `services/search/core.py:912`
- `services/search/core.py:936`
- `services/search/core.py:1047`
- `services/search/core.py:1074`

## `_build_provider_chain` — function, line 134
- **called from:**
- `services/search/core.py:905`
- `services/search/core.py:1038`
- `src/research_navigator.py:169`
- `tests/test_search_empty_query_relaxation.py:114`
- `tests/test_service_search_provider_guards.py:95`
- `tests/test_service_search_provider_guards.py:102`

## `_relaxed_query_after_empty` — function, line 183
- **called from:**
- `services/search/core.py:200`

## `_empty_result_query_relaxations` — function, line 198
- **called from:**
- `services/search/core.py:929`
- `services/search/core.py:1067`
- `tests/test_search_empty_query_relaxation.py:77`
- `tests/test_search_empty_query_relaxation.py:120`

## `_meaningful_query_terms` — function, line 227
- **called from:**
- `services/search/core.py:253`
- `tests/test_service_search_provider_guards.py:308`

## `_result_has_query_overlap` — function, line 252
- **called from:**
- `services/search/core.py:329`
- `tests/test_review_20260919_fixes.py:77`
- `tests/test_review_20260919_fixes.py:87`
- `tests/test_search_empty_query_relaxation.py:9`
- `tests/test_search_empty_query_relaxation.py:14`
- `tests/test_search_empty_query_relaxation.py:15`
- `tests/test_search_empty_query_relaxation.py:16`
- `tests/test_search_empty_query_relaxation.py:130`
- `tests/test_search_empty_query_relaxation.py:135`

## `lexical_root` — function, line 306
- **called from:**
- `services/search/core.py:312`
- `services/search/core.py:315`

## `_filter_low_relevance_results` — function, line 325
- **called from:**
- `services/search/core.py:878`
- `services/search/core.py:913`
- `services/search/core.py:937`
- `services/search/core.py:1048`
- `services/search/core.py:1077`
- `tests/test_search_empty_query_relaxation.py:57`
- `tests/test_service_search_provider_guards.py:235`
- `tests/test_service_search_provider_guards.py:255`
- `tests/test_service_search_provider_guards.py:277`
- `tests/test_service_search_provider_guards.py:314`
- `tests/test_service_search_provider_guards.py:334`
- `tests/test_service_search_provider_guards.py:791`
- `tests/test_service_search_provider_guards.py:801`

## `_result_matches_site_scope` — function, line 337
- **called from:**
- `services/search/core.py:328`
- `services/search/core.py:857`
- `tests/test_search_empty_query_relaxation.py:64`
- `tests/test_search_empty_query_relaxation.py:65`
- `tests/test_search_empty_query_relaxation.py:66`
- `tests/test_search_empty_query_relaxation.py:67`

## `_exact_arxiv_identifier_results` — function, line 382
- **called from:**
- `services/search/core.py:733`

## `_title_before_explicit_arxiv_identifier` — function, line 404
- **called from:**
- `services/search/core.py:735`

## `_normalized_title_terms` — function, line 428
- **called from:**
- `services/search/core.py:425`
- `services/search/core.py:439`
- `services/search/core.py:459`
- `services/search/core.py:463`
- `services/search/core.py:474`
- `services/search/core.py:492`
- `services/search/core.py:493`

## `_is_distinctive_short_scholarly_title` — function, line 436
- **called from:**
- `services/search/core.py:460`
- `services/search/core.py:475`
- `services/search/core.py:486`

## `_scholarly_title_from_query` — function, line 449
- **called from:**
- `services/search/core.py:753`
- `services/search/core.py:854`
- `tests/test_clawmm_r44_short_title.py:49`
- `tests/test_clawmm_r44_short_title.py:52`
- `tests/test_service_search_provider_guards.py:373`
- `tests/test_service_search_provider_guards.py:376`
- `tests/test_service_search_provider_guards.py:379`

## `_result_strongly_matches_title` — function, line 491
- **called from:**
- `services/search/core.py:611`
- `services/search/core.py:656`
- `services/search/core.py:707`
- `services/search/core.py:758`

## `_scholarly_user_agent` — function, line 500
- **called from:**
- `services/search/core.py:559`
- `tests/test_review_20260923_fixes.py:71`

## `_scholarly_budget` — function, line 513
- decorator: `contextmanager`
- **called from:**
- `services/search/core.py:695`
- `services/search/core.py:722`
- `tests/test_review_20260923_fixes.py:338`

## `_scholarly_api_get` — function, line 527
- **called from:**
- `services/search/core.py:590`
- `services/search/core.py:636`
- `tests/test_review_20260923_fixes.py:87`
- `tests/test_review_20260923_fixes.py:114`
- `tests/test_review_20260923_fixes.py:144`
- `tests/test_review_20260923_fixes.py:165`
- `tests/test_review_20260923_fixes.py:184`
- `tests/test_review_20260923_fixes.py:212`
- `tests/test_review_20260923_fixes.py:243`
- `tests/test_review_20260923_fixes.py:275`
- `tests/test_review_20260923_fixes.py:300`

## `_arxiv_title_results` — function, line 586
- **called from:**
- `services/search/core.py:714`
- `services/search/core.py:726`
- `tests/test_review_20260923_fixes.py:62`
- `tests/test_review_20260923_fixes.py:259`

## `_openalex_title_results` — function, line 629
- **called from:**
- `services/search/core.py:711`
- `services/search/core.py:723`
- `services/search/core.py:740`
- `tests/test_review_20260923_fixes.py:63`
- `tests/test_review_20260923_fixes.py:260`
- `tests/test_service_search_provider_guards.py:576`
- `tests/test_service_search_provider_guards.py:618`

## `_scholarly_title_results` — function, line 689
- **called from:**
- `services/search/core.py:763`

## `_scholarly_title_results_inner` — function, line 699
- **called from:**
- `services/search/core.py:696`

## `_direct_scholarly_title_results` — function, line 717
- **called from:**
- `services/search/core.py:856`
- `tests/test_review_20260923_fixes.py:328`

## `_augment_scholarly_results` — function, line 729
- **called from:**
- `services/search/core.py:881`
- `services/search/core.py:947`
- `services/search/core.py:954`
- `services/search/core.py:1093`
- `services/search/core.py:1114`
- `tests/test_service_search_provider_guards.py:419`
- `tests/test_service_search_provider_guards.py:439`
- `tests/test_service_search_provider_guards.py:458`
- `tests/test_service_search_provider_guards.py:505`
- `tests/test_service_search_provider_guards.py:536`
- `tests/test_service_search_provider_guards.py:734`

## `_subject_first_weather_query` — function, line 770
- **called from:**
- `services/search/core.py:809`
- `tests/test_service_search_provider_guards.py:367`

## `_provider_friendly_query` — function, line 807
- **called from:**
- `services/search/core.py:843`
- `services/search/core.py:1021`
- `tests/test_service_search_provider_guards.py:299`
- `tests/test_service_search_provider_guards.py:305`

## `searxng_search_results` — function, line 841
- **called from:**
- `src/agent_tools/web_tools.py:341`
- `src/agent_tools/web_tools.py:370`
- `src/agent_tools/web_tools_prewave3.py:345`
- `src/agent_tools/web_tools_prewave3.py:374`
- `tests/test_clawmm_r44_short_title.py:34`
- `tests/test_clawmm_r44_short_title.py:38`
- `tests/test_search_empty_query_relaxation.py:42`
- `tests/test_search_empty_query_relaxation.py:101`
- `tests/test_search_empty_query_relaxation.py:170`
- `tests/test_service_search_provider_guards.py:668`
- `tests/test_service_search_provider_guards.py:708`

## `invalidate_search_cache` — function, line 978
- **called from:**
- `tests/test_search_cache_invalidation.py:37`

## `comprehensive_web_search` — function, line 1008
- **called from:**
- `routes/search/search_routes.py:161`
- `services/research/research_handler.py:445`
- `src/agent_tools/web_tools.py:350`
- `src/agent_tools/web_tools.py:404`
- `src/agent_tools/web_tools_prewave3.py:354`
- `src/agent_tools/web_tools_prewave3.py:408`
- `src/chat_processor.py:480`
- `src/research_handler.py:1181`
- `tests/test_search_content_block_source_index.py:44`
- `tests/test_search_content_block_source_index.py:61`
- `tests/test_search_empty_query_relaxation.py:37`
- `tests/test_search_empty_query_relaxation.py:99`

## `url_passes_filters` — function, line 1121
- **called from:**
- `services/search/core.py:1147`
