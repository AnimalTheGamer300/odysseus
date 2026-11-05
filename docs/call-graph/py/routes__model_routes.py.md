# `routes/model_routes.py` — definitions & call sites

114 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_redact_url_for_log` — function, line 28
- **called from:**
- `routes/model_routes.py:1091`
- `routes/model_routes.py:1095`
- `routes/model_routes.py:1097`
- `routes/model_routes.py:1100`
- `routes/model_routes.py:1102`

## `_speech_settings_using_endpoint` — function, line 76
- **called from:**
- `routes/model_routes.py:109`
- `tests/test_model_routes.py:70`

## `_clear_speech_settings_for_endpoint` — function, line 86
- **called from:**
- `routes/model_routes.py:133`
- `tests/test_model_routes.py:81`

## `_endpoint_settings_using_endpoint` — function, line 98
- **called from:**
- `routes/model_routes.py:2967`
- `tests/test_model_routes.py:110`

## `_clear_endpoint_settings_for_endpoint` — function, line 113
- **called from:**
- `routes/model_routes.py:189`
- `routes/model_routes.py:211`
- `routes/model_routes.py:2972`
- `tests/test_model_routes.py:117`

## `_active_cookbook_endpoint_ids` — function, line 142
- **called from:**
- `routes/model_routes.py:172`

## `_disable_stale_cookbook_local_endpoints` — function, line 170
- **called from:**
- `routes/model_routes.py:1606`
- `routes/model_routes.py:1684`
- `routes/model_routes.py:1845`
- `routes/model_routes.py:2087`

## `_clear_user_pref_endpoint_refs` — function, line 198
- **called from:**
- `routes/model_routes.py:2982`
- `tests/test_model_routes.py:160`
- `tests/test_model_routes.py:176`

## `_endpoint_visible_model_ids` — function, line 216
- **called from:**
- `routes/model_routes.py:251`

## `_default_endpoint_needs_assignment` — function, line 227
- **called from:**
- `routes/model_routes.py:2378`
- `tests/test_model_routes.py:186`
- `tests/test_model_routes.py:194`
- `tests/test_model_routes.py:199`

## `_docker_host_gateway_reachable` — function, line 262
- **called from:**
- `routes/model_routes.py:333`
- `routes/model_routes.py:338`
- `tests/test_model_routes.py:849`
- `tests/test_model_routes.py:854`
- `tests/test_model_routes.py:863`

## `_container_loopback_reachable` — function, line 282
- **called from:**
- `routes/model_routes.py:336`

## `_rewrite_loopback_for_docker` — function, line 309
- **called from:**
- `routes/model_routes.py:2175`
- `routes/model_routes.py:2425`
- `tests/test_endpoint_probing.py:292`
- `tests/test_endpoint_probing.py:300`
- `tests/test_endpoint_probing.py:307`
- `tests/test_endpoint_probing.py:314`
- `tests/test_endpoint_probing.py:321`
- `tests/test_model_routes.py:817`
- `tests/test_model_routes.py:819`
- `tests/test_model_routes.py:824`
- `tests/test_model_routes.py:830`
- `tests/test_model_routes.py:832`

## `_match_provider_curated` — function, line 424
- **called from:**
- `routes/model_routes.py:1079`
- `routes/model_routes.py:1084`
- `routes/model_routes.py:1119`
- `routes/model_routes.py:1709`
- `tests/test_model_routes.py:206`
- `tests/test_model_routes.py:209`
- `tests/test_model_routes.py:212`
- `tests/test_model_routes.py:215`
- `tests/test_model_routes.py:218`
- `tests/test_model_routes.py:221`
- `tests/test_model_routes.py:224`
- `tests/test_model_routes.py:227`
- `tests/test_model_routes.py:230`
- `tests/test_model_routes.py:233`
- `tests/test_model_routes.py:236`
- `tests/test_model_routes.py:239`
- `tests/test_model_routes.py:242`
- `tests/test_model_routes.py:248`
- `tests/test_model_routes.py:252`
- `tests/test_model_routes.py:253`
- `tests/test_model_routes.py:259`
- `tests/test_model_routes.py:263`
- `tests/test_model_routes.py:267`

## `_curate_models` — function, line 443
- **called from:**
- `routes/model_routes.py:1710`
- `tests/test_model_routes.py:331`
- `tests/test_model_routes.py:338`
- `tests/test_model_routes.py:344`
- `tests/test_model_routes.py:350`
- `tests/test_model_routes.py:357`
- `tests/test_model_routes.py:363`
- `tests/test_model_routes.py:370`
- `tests/test_model_routes.py:376`
- `tests/test_model_routes.py:387`
- `tests/test_model_routes.py:392`

## `_best_match_idx` — function, line 453
- **called from:**
- `routes/model_routes.py:462`
- `routes/model_routes.py:467`

## `_truthy` — function, line 471
- **called from:**
- `routes/model_routes.py:2175`
- `routes/model_routes.py:2206`
- `routes/model_routes.py:2208`
- `tests/test_model_routes.py:590`
- `tests/test_model_routes.py:594`

## `_normalize_endpoint_kind` — function, line 484
- **called from:**
- `routes/model_routes.py:516`
- `routes/model_routes.py:527`
- `routes/model_routes.py:623`
- `routes/model_routes.py:844`
- `routes/model_routes.py:2198`
- `routes/model_routes.py:2436`
- `routes/model_routes.py:2901`

## `_normalize_model_tool_mode` — function, line 489
- **called from:**
- `routes/model_routes.py:508`
- `routes/model_routes.py:2617`
- `tests/test_model_tool_modes.py:113`
- `tests/test_model_tool_modes.py:114`

## `_model_tool_modes` — function, line 495
- **called from:**
- `routes/model_routes.py:2129`
- `routes/model_routes.py:2549`
- `routes/model_routes.py:2612`
- `routes/model_routes.py:2631`
- `routes/model_routes.py:2956`
- `tests/test_model_tool_modes.py:18`

## `_normalize_refresh_mode` — function, line 514
- **called from:**
- `routes/model_routes.py:931`
- `tests/test_model_routes.py:489`
- `tests/test_model_routes.py:490`
- `tests/test_model_routes.py:491`
- `tests/test_model_routes.py:492`

## `_endpoint_kind` — function, line 526
- **called from:**
- `routes/model_routes.py:533`
- `routes/model_routes.py:860`
- `routes/model_routes.py:2254`
- `routes/model_routes.py:2905`

## `_endpoint_refresh_mode` — function, line 530
- **called from:**
- `routes/model_routes.py:1541`
- `routes/model_routes.py:2132`
- `routes/model_routes.py:2257`
- `tests/test_model_routes.py:512`
- `tests/test_model_routes.py:514`

## `_endpoint_refresh_interval` — function, line 538
- **called from:**
- `routes/model_routes.py:1581`

## `_endpoint_refresh_timeout` — function, line 549
- **called from:**
- `routes/model_routes.py:574`
- `routes/model_routes.py:1554`
- `tests/test_model_picker_refresh_timeout.py:57`
- `tests/test_model_picker_refresh_timeout.py:58`

## `_manual_refresh_timeout` — function, line 563
- **called from:**
- `routes/model_routes.py:2529`

## `_parse_model_list` — function, line 578
- **called from:**
- `routes/model_routes.py:631`
- `routes/model_routes.py:635`
- `tests/test_model_routes.py:517`
- `tests/test_model_routes.py:518`

## `_parse_positive_int` — function, line 608
- **called from:**
- `routes/model_routes.py:569`
- `routes/model_routes.py:572`
- `routes/model_routes.py:620`
- `routes/model_routes.py:2204`
- `routes/model_routes.py:2205`
- `routes/model_routes.py:2440`
- `routes/model_routes.py:2909`
- `routes/model_routes.py:2912`

## `_explicit_model_list_timeout` — function, line 618
- **called from:**
- `routes/model_routes.py:2210`
- `routes/model_routes.py:2284`
- `routes/model_routes.py:2441`

## `_cached_model_ids` — function, line 630
- **called from:**
- `routes/model_routes.py:1428`
- `routes/model_routes.py:1447`
- `routes/model_routes.py:1542`
- `routes/model_routes.py:1919`
- `routes/model_routes.py:2095`
- `routes/model_routes.py:2293`
- `routes/model_routes.py:2523`
- `routes/model_routes.py:2593`

## `_hidden_model_ids` — function, line 634
- **called from:**
- `routes/model_routes.py:1444`
- `routes/model_routes.py:2096`
- `routes/model_routes.py:2522`

## `_is_ollama_base` — function, line 638
- **called from:**
- `routes/model_routes.py:627`
- `routes/model_routes.py:865`

## `_is_chat_model` — function, line 670
- **called from:**
- `routes/model_routes.py:1088`
- `routes/model_routes.py:1115`
- `routes/model_routes.py:2038`
- `routes/model_routes.py:2472`
- `routes/model_routes.py:2851`
- `routes/model_routes.py:2856`
- `tests/test_model_routes.py:408`
- `tests/test_model_routes.py:415`
- `tests/test_model_routes.py:418`
- `tests/test_model_routes.py:422`
- `tests/test_model_routes.py:425`
- `tests/test_model_routes.py:428`
- `tests/test_model_routes.py:434`

## `_delete_orphaned_provider_auth` — function, line 689
- **called from:**
- `routes/model_routes.py:3087`
- `tests/test_chatgpt_subscription_routes.py:286`
- `tests/test_chatgpt_subscription_routes.py:305`
- `tests/test_chatgpt_subscription_routes.py:319`
- `tests/test_chatgpt_subscription_routes.py:331`
- `tests/test_chatgpt_subscription_routes.py:352`
- `tests/test_chatgpt_subscription_routes.py:437`
- `tests/test_chatgpt_subscription_routes.py:444`

## `_safe_detect_provider` — function, line 712
- **called from:**
- `routes/model_routes.py:758`
- `routes/model_routes.py:1020`
- `routes/model_routes.py:1178`
- `routes/model_routes.py:1558`
- `routes/model_routes.py:1700`
- `routes/model_routes.py:1917`
- `routes/model_routes.py:2108`
- `routes/model_routes.py:2190`
- `routes/model_routes.py:2296`
- `routes/model_routes.py:2437`
- `routes/model_routes.py:2656`

## `_safe_build_models_url` — function, line 721
- **called from:**
- `routes/model_routes.py:1041`
- `routes/model_routes.py:1064`
- `routes/model_routes.py:1229`

## `_safe_build_headers` — function, line 732
- **called from:**
- `routes/model_routes.py:779`
- `routes/model_routes.py:784`
- `routes/model_routes.py:1065`
- `routes/model_routes.py:1131`

## `_is_discovery_only_provider` — function, line 741
- **called from:**
- `routes/model_routes.py:759`

## `_resolve_probe_key` — function, line 745
- **called from:**
- `routes/model_routes.py:1615`
- `routes/model_routes.py:1967`
- `routes/model_routes.py:2008`
- `routes/model_routes.py:2466`
- `routes/model_routes.py:2531`
- `routes/model_routes.py:2659`
- `tests/test_endpoint_probing.py:456`
- `tests/test_endpoint_probing.py:467`
- `tests/test_endpoint_probing.py:477`

## `_probe_single_model` — function, line 756
- **called from:**
- `routes/model_routes.py:1980`
- `routes/model_routes.py:2044`
- `routes/model_routes.py:2480`
- `tests/test_chatgpt_zero_native_tools.py:197`
- `tests/test_endpoint_probing.py:338`
- `tests/test_endpoint_probing.py:359`
- `tests/test_endpoint_probing.py:370`
- `tests/test_endpoint_probing.py:381`
- `tests/test_endpoint_probing.py:392`
- `tests/test_endpoint_probing.py:403`
- `tests/test_endpoint_probing.py:416`
- `tests/test_endpoint_probing.py:431`
- `tests/test_endpoint_probing.py:444`

## `_local_ip_literal` — function, line 832
- **called from:**
- `routes/model_routes.py:851`

## `_classify_endpoint` — function, line 840
- **called from:**
- `routes/model_routes.py:624`
- `routes/model_routes.py:1404`
- `routes/model_routes.py:1540`
- `routes/model_routes.py:1705`
- `routes/model_routes.py:1852`
- `routes/model_routes.py:1925`
- `routes/model_routes.py:2131`
- `routes/model_routes.py:2314`
- `routes/model_routes.py:2408`
- `routes/model_routes.py:2454`
- `routes/model_routes.py:2528`
- `tests/test_endpoint_probing.py:489`
- `tests/test_endpoint_probing.py:497`
- `tests/test_model_routes.py:441`
- `tests/test_model_routes.py:444`
- `tests/test_model_routes.py:447`
- `tests/test_model_routes.py:450`
- `tests/test_model_routes.py:458`
- `tests/test_model_routes.py:461`
- `tests/test_model_routes.py:464`
- `tests/test_model_routes.py:467`
- `tests/test_model_routes.py:470`
- `tests/test_model_routes.py:473`
- `tests/test_model_routes.py:476`
- `tests/test_model_routes.py:479`
- `tests/test_model_routes.py:482`

## `_effective_endpoint_kind` — function, line 858
- **called from:**
- `routes/model_routes.py:1539`
- `routes/model_routes.py:1704`
- `routes/model_routes.py:1851`
- `routes/model_routes.py:1918`
- `routes/model_routes.py:2103`
- `routes/model_routes.py:2253`
- `routes/model_routes.py:2295`
- `routes/model_routes.py:2525`
- `routes/model_routes.py:2587`
- `routes/model_routes.py:2602`
- `routes/model_routes.py:2894`
- `tests/test_featherless_provider.py:87`
- `tests/test_model_routes.py:486`

## `_is_loading_model_response` — function, line 875
- **called from:**
- `routes/model_routes.py:1090`
- `routes/model_routes.py:1167`

## `_openai_model_ids` — function, line 886
- **called from:**
- `routes/model_routes.py:1049`
- `routes/model_routes.py:1071`
- `tests/test_endpoint_probing.py:91`

## `_ollama_model_names` — function, line 904
- **called from:**
- `routes/model_routes.py:1074`
- `routes/model_routes.py:1113`
- `tests/test_endpoint_probing.py:103`

## `_is_google_api_base` — function, line 921
- **called from:**
- `routes/model_routes.py:929`
- `routes/model_routes.py:1028`
- `tests/test_model_routes.py:501`
- `tests/test_model_routes.py:502`

## `_normalize_endpoint_refresh_mode` — function, line 928
- **called from:**
- `routes/model_routes.py:531`
- `routes/model_routes.py:2203`
- `routes/model_routes.py:2903`
- `tests/test_model_routes.py:496`
- `tests/test_model_routes.py:497`
- `tests/test_model_routes.py:498`

## `_google_native_root` — function, line 934
- **called from:**
- `routes/model_routes.py:954`

## `_google_native_models_url` — function, line 953
- **called from:**
- `routes/model_routes.py:982`

## `_google_model_id_from_item` — function, line 957
- **called from:**
- `routes/model_routes.py:1004`

## `_google_model_supports_chat` — function, line 964
- **called from:**
- `routes/model_routes.py:1002`

## `_probe_google_models` — function, line 975
- **called from:**
- `routes/model_routes.py:1030`

## `_probe_endpoint` — function, line 1014
- **called from:**
- `routes/cookbook_routes.py:1814`
- `routes/cookbook_routes.py:1855`
- `routes/model_routes.py:1630`
- `routes/model_routes.py:2023`
- `routes/model_routes.py:2281`
- `routes/model_routes.py:2319`
- `routes/model_routes.py:2442`
- `routes/model_routes.py:2471`
- `routes/model_routes.py:2531`
- `src/research_handler.py:1013`
- `tests/test_endpoint_probing.py:116`
- `tests/test_endpoint_probing.py:127`
- `tests/test_endpoint_probing.py:141`
- `tests/test_endpoint_probing.py:151`
- `tests/test_endpoint_probing.py:165`
- `tests/test_endpoint_probing.py:178`
- `tests/test_endpoint_probing.py:188`
- `tests/test_endpoint_probing.py:200`
- `tests/test_endpoint_probing.py:207`
- `tests/test_endpoint_probing.py:208`
- `tests/test_featherless_provider.py:96`
- `tests/test_model_routes.py:289`
- `tests/test_model_routes.py:304`
- `tests/test_model_routes.py:320`
- `tests/test_model_routes.py:607`
- `tests/test_model_routes.py:618`
- `tests/test_model_routes.py:670`
- `tests/test_model_routes.py:695`
- `tests/test_model_routes.py:706`
- `tests/test_model_routes.py:725`
- `tests/test_model_routes.py:745`
- `tests/test_model_routes.py:757`
- `tests/test_research_probe_errors.py:52`

## `_ping_endpoint` — function, line 1127
- **called from:**
- `routes/model_routes.py:1930`
- `routes/model_routes.py:2322`
- `routes/model_routes.py:2443`
- `tests/test_endpoint_probing.py:220`
- `tests/test_endpoint_probing.py:231`
- `tests/test_endpoint_probing.py:242`
- `tests/test_endpoint_probing.py:254`
- `tests/test_endpoint_probing.py:265`
- `tests/test_endpoint_probing.py:280`
- `tests/test_featherless_provider.py:108`
- `tests/test_featherless_provider.py:127`
- `tests/test_featherless_provider.py:141`
- `tests/test_model_routes.py:535`
- `tests/test_model_routes.py:556`
- `tests/test_model_routes.py:577`

## `_is_loading_model_response` — function, line 1142
- **called from:**
- `routes/model_routes.py:1090`
- `routes/model_routes.py:1167`

## `_result_from_response` — function, line 1151
- **called from:**
- `routes/model_routes.py:1183`
- `routes/model_routes.py:1194`
- `routes/model_routes.py:1213`
- `routes/model_routes.py:1224`
- `routes/model_routes.py:1232`

## `_model_endpoint_error_message` — function, line 1247
- **called from:**
- `routes/model_routes.py:2324`
- `tests/test_model_routes.py:760`
- `tests/test_model_routes.py:772`
- `tests/test_model_routes.py:787`
- `tests/test_model_routes.py:804`

## `_normalize_model_ids` — function, line 1308
- **called from:**
- `routes/cookbook_routes.py:1448`
- `routes/cookbook_routes.py:1780`
- `routes/cookbook_routes.py:1789`
- `routes/model_routes.py:1393`
- `routes/model_routes.py:1394`
- `routes/model_routes.py:1399`
- `routes/model_routes.py:1441`
- `routes/model_routes.py:2097`
- `routes/model_routes.py:2245`
- `routes/model_routes.py:2248`
- `routes/model_routes.py:2294`
- `routes/model_routes.py:2334`
- `routes/model_routes.py:2545`
- `routes/model_routes.py:2600`
- `routes/model_routes.py:2892`
- `routes/model_routes.py:2955`
- `tests/test_model_routes.py:871`
- `tests/test_model_routes.py:874`
- `tests/test_model_routes.py:877`
- `tests/test_model_routes.py:880`
- `tests/test_model_routes.py:881`
- `tests/test_model_routes.py:882`
- `tests/test_model_routes.py:885`

## `_merge_model_ids` — function, line 1341
- **called from:**
- `routes/model_routes.py:1392`
- `routes/model_routes.py:2109`
- `routes/model_routes.py:2247`
- `routes/model_routes.py:2402`
- `routes/model_routes.py:2559`

## `_is_mlx_deepseek_v4_repo_id` — function, line 1353
- **called from:**
- `routes/model_routes.py:1374`
- `src/endpoint_resolver.py:137`

## `_is_mlx_deepseek_v4_shim_id` — function, line 1358
- **called from:**
- `routes/model_routes.py:1371`
- `routes/model_routes.py:1378`
- `src/endpoint_resolver.py:134`

## `_filter_mlx_deepseek_v4_repo_when_shimmed` — function, line 1363
- **called from:**
- `routes/model_routes.py:1396`
- `src/endpoint_resolver.py:167`

## `_model_display_name` — function, line 1377
- **called from:**
- `routes/model_routes.py:1727`
- `routes/model_routes.py:1729`

## `_visible_models` — function, line 1383
- **called from:**
- `routes/chat_routes.py:2122`
- `routes/chat_routes.py:2151`
- `routes/model_routes.py:220`
- `routes/model_routes.py:1427`
- `routes/model_routes.py:1446`
- `routes/model_routes.py:2304`
- `routes/model_routes.py:2593`
- `routes/model_routes.py:2855`
- `tests/test_model_routes.py:893`
- `tests/test_model_routes.py:897`
- `tests/test_model_routes.py:901`
- `tests/test_model_routes.py:905`
- `tests/test_model_routes.py:1228`
- `tests/test_model_routes.py:1231`
- `tests/test_model_routes.py:1232`
- `tests/test_review_regressions.py:1663`
- `tests/test_review_regressions.py:1674`
- `tests/test_review_regressions.py:1685`
- `tests/test_review_regressions.py:1696`

## `_picker_requires_pinning` — function, line 1403
- **called from:**
- `routes/model_routes.py:1442`
- `routes/model_routes.py:2105`
- `routes/model_routes.py:2110`
- `routes/model_routes.py:2526`
- `routes/model_routes.py:2588`
- `routes/model_routes.py:2603`
- `routes/model_routes.py:2895`
- `tests/test_featherless_provider.py:172`

## `_has_explicit_pinned_models` — function, line 1407
- **called from:**
- `routes/model_routes.py:1443`
- `routes/model_routes.py:2105`
- `routes/model_routes.py:2546`
- `tests/test_featherless_provider.py:181`

## `_legacy_visible_api_models` — function, line 1418
- **called from:**
- `routes/model_routes.py:1444`
- `routes/model_routes.py:2547`

## `_picker_models_for_endpoint` — function, line 1434
- **called from:**
- `routes/model_routes.py:1706`
- `routes/model_routes.py:2104`
- `tests/test_featherless_provider.py:182`
- `tests/test_featherless_provider.py:198`
- `tests/test_model_routes.py:1341`

## `_chatgpt_endpoint_visible` — function, line 1453
- **called from:**
- `routes/model_routes.py:1966`
- `routes/model_routes.py:2002`
- `routes/model_routes.py:2093`
- `routes/model_routes.py:2464`
- `routes/model_routes.py:2520`
- `routes/model_routes.py:2577`
- `routes/model_routes.py:2653`
- `routes/model_routes.py:2878`
- `routes/model_routes.py:3058`

## `_provider_account_metadata` — function, line 1464
- **called from:**
- `routes/model_routes.py:2135`

## `_api_key_fingerprint` — function, line 1482
- **called from:**
- `routes/model_routes.py:2117`
- `routes/model_routes.py:2303`
- `routes/model_routes.py:2401`
- `tests/test_model_routes.py:1236`
- `tests/test_model_routes.py:1238`
- `tests/test_model_routes.py:1239`
- `tests/test_model_routes.py:1240`
- `tests/test_model_routes.py:1306`
- `tests/test_model_routes.py:1507`
- `tests/test_model_routes.py:1573`

## `setup_model_routes` — function, line 1490
- **called from:**
- `app.py:824`
- `tests/test_chatgpt_subscription_routes.py:376`
- `tests/test_chatgpt_subscription_routes.py:500`
- `tests/test_chatgpt_subscription_routes.py:532`
- `tests/test_cookbook_endpoint_registration.py:354`
- `tests/test_default_chat_model_filter.py:30`
- `tests/test_endpoint_registered_authority.py:110`
- `tests/test_endpoint_registered_authority.py:250`
- `tests/test_endpoint_registered_authority.py:310`
- `tests/test_endpoint_registered_authority.py:359`
- `tests/test_featherless_provider.py:55`
- `tests/test_manage_settings_denylist_hard.py:133`
- `tests/test_model_defaults.py:125`
- `tests/test_model_defaults.py:195`
- `tests/test_model_endpoint_ssrf.py:71`
- `tests/test_model_picker_refresh_timeout.py:63`
- `tests/test_model_picker_refresh_timeout.py:120`
- `tests/test_model_routes.py:978`
- `tests/test_model_routes.py:1707`
- `tests/test_model_routes.py:1742`
- `tests/test_model_routes.py:1783`
- `tests/test_model_routes.py:1816`
- `tests/test_model_routes.py:1841`
- `tests/test_model_routes.py:1866`
- `tests/test_model_routes.py:1891`
- `tests/test_model_routes.py:1920`
- `tests/test_model_routes.py:1943`
- `tests/test_model_routes.py:1968`
- `tests/test_model_routes.py:2001`
- `tests/test_model_routes.py:2035`
- `tests/test_model_routes.py:2096`
- `tests/test_model_routes.py:2141`
- `tests/test_model_routes.py:2177`
- `tests/test_review_regressions.py:75`
- `tests/test_review_regressions.py:156`

## `_invalidate_models_cache` — function, line 1502
- **called from:**
- `routes/chatgpt_subscription_routes.py:216`
- `routes/copilot_routes.py:96`
- `routes/model_routes.py:1658`
- `routes/model_routes.py:1685`
- `routes/model_routes.py:1846`
- `routes/model_routes.py:2088`
- `routes/model_routes.py:2139`
- `routes/model_routes.py:2291`
- `routes/model_routes.py:2388`
- `routes/model_routes.py:2501`
- `routes/model_routes.py:2539`
- `routes/model_routes.py:2624`
- `routes/model_routes.py:2946`
- `routes/model_routes.py:3089`

## `_refresh_key` — function, line 1519
- **called from:**
- `routes/model_routes.py:1543`
- `routes/model_routes.py:1859`

## `_ts` — function, line 1524
- **called from:**
- `routes/model_routes.py:1582`
- `routes/model_routes.py:1582`

## `_failure_delay` — function, line 1530
- **called from:**
- `routes/model_routes.py:1572`

## `_should_refresh_endpoint` — function, line 1537
- **called from:**
- `routes/model_routes.py:1612`
- `tests/test_featherless_provider.py:160`

## `_refresh_caches_bg` — function, line 1587
- **called from:**
- `routes/model_routes.py:1805`
- `tests/test_model_picker_refresh_timeout.py:139`

## `_do` — function, line 1600
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_probe_one` — function, line 1628
- **called from:**
- `routes/model_routes.py:1884`

## `_fetch_models` — function, line 1669
- **called from:**
- `routes/model_routes.py:1799`
- `routes/model_routes.py:1812`

## `api_models` — function, line 1758
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_local_endpoints` — function (async), line 1825
- **route:** `GET /model-endpoints/probe-local`
- decorator: `router.get("/model-endpoints/probe-local")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_compute_local_probe` — function (async), line 1842
- **called from:**
- `routes/model_routes.py:1896`

## `_probe_one` — function (async), line 1862
- **called from:**
- `routes/model_routes.py:1884`

## `ping_endpoints` — function, line 1905
- **route:** `GET /ping`
- decorator: `router.get("/ping")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_selected` — function, line 1945
- **route:** `POST /probe-selected`
- decorator: `router.post("/probe-selected")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_models` — function, line 1990
- **route:** `GET /probe`
- decorator: `router.get("/probe")`
- **called from:**
- `src/editor_agent_model.py:714`
- `src/editor_agent_model.py:719`

## `_empty` — function, line 2014
- **called from:**
- `routes/model_routes.py:2016`

## `_stream` — function, line 2018
- **called from:**
- `routes/model_routes.py:2054`
- `routes/model_routes.py:2505`

## `providers` — function, line 2063
- **route:** `GET /providers`
- decorator: `router.get("/providers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `discover_local` — function, line 2075
- **route:** `GET /discover`
- decorator: `router.get("/discover")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_model_endpoints` — function, line 2083
- **route:** `GET /model-endpoints`
- decorator: `router.get("/model-endpoints")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_model_endpoint` — function, line 2145
- **route:** `POST /model-endpoints`
- decorator: `router.post("/model-endpoints")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_model_endpoint` — function, line 2412
- **route:** `POST /model-endpoints/test`
- decorator: `router.post("/model-endpoints/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_endpoint_models` — function, line 2458
- **route:** `GET /model-endpoints/{ep_id}/probe`
- decorator: `router.get("/model-endpoints/{ep_id}/probe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_stream` — function, line 2475
- **called from:**
- `routes/model_routes.py:2054`
- `routes/model_routes.py:2505`

## `list_endpoint_models` — function, line 2508
- **route:** `GET /model-endpoints/{ep_id}/models`
- decorator: `router.get("/model-endpoints/{ep_id}/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_hidden_models` — function (async), line 2565
- **route:** `PATCH /model-endpoints/{ep_id}/models`
- decorator: `router.patch("/model-endpoints/{ep_id}/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_endpoint_catalog` — function (async), line 2637
- **route:** `GET /model-endpoints/{ep_id}/catalog-search`
- decorator: `router.get("/model-endpoints/{ep_id}/catalog-search")`
- **called from:**
- `tests/test_featherless_provider.py:212`
- `tests/test_featherless_provider.py:358`
- `tests/test_featherless_provider.py:402`
- `tests/test_featherless_provider.py:421`
- `tests/test_featherless_provider.py:449`
- `tests/test_featherless_provider.py:463`
- `tests/test_featherless_provider.py:468`
- `tests/test_featherless_provider.py:500`
- `tests/test_featherless_provider.py:510`
- `tests/test_featherless_provider.py:519`
- `tests/test_featherless_provider.py:527`
- `tests/test_featherless_provider.py:536`
- `tests/test_featherless_provider.py:545`
- `tests/test_featherless_provider.py:569`
- `tests/test_featherless_provider.py:578`
- `tests/test_featherless_provider.py:585`

## `get_default_chat` — function, line 2780
- **route:** `GET /default-chat`
- decorator: `router.get("/default-chat")`
- **called from:**
- `tests/test_model_defaults.py:129`
- `tests/test_model_defaults.py:199`

## `toggle_model_endpoint` — function (async), line 2864
- **route:** `PATCH /model-endpoints/{ep_id}`
- decorator: `router.patch("/model-endpoints/{ep_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_settings_using_endpoint` — function, line 2965
- **called from:**
- `routes/model_routes.py:3046`

## `_clear_settings_for_endpoint` — function, line 2969
- **called from:**
- `routes/model_routes.py:3080`

## `_clear_user_prefs_for_endpoint` — function, line 2977
- **called from:**
- `routes/model_routes.py:3081`

## `_session_uses_endpoint_url` — function, line 2990
- **called from:**
- `routes/model_routes.py:3016`
- `routes/model_routes.py:3035`

## `_clear_sessions_for_endpoint` — function, line 3002
- **called from:**
- `routes/model_routes.py:3082`

## `_clear_loaded_sessions_for_endpoint` — function, line 3022
- **called from:**
- `routes/model_routes.py:3083`

## `get_endpoint_dependents` — function, line 3043
- **route:** `GET /model-endpoints/{ep_id}/dependents`
- decorator: `router.get("/model-endpoints/{ep_id}/dependents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_model_endpoint` — function, line 3049
- **route:** `DELETE /model-endpoints/{ep_id}`
- decorator: `router.delete("/model-endpoints/{ep_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_tools` — function, line 3105
- **route:** `GET /tools`
- decorator: `router.get("/tools")`
- **called from:**
- `mcp_servers/email_server.py:3586`
- `mcp_servers/image_gen_server.py:24`
- `mcp_servers/memory_server.py:115`
- `mcp_servers/rag_server.py:46`
- `src/mcp_manager.py:233`
- `src/mcp_manager.py:303`
- `src/mcp_manager.py:393`
- `tests/test_clean_agent_preview.py:4319`
- `tests/test_generate_image_native_schema.py:56`

## `ToolsUpdate` — class, line 3115
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_tools` — function, line 3119
- **route:** `POST /tools`
- decorator: `router.post("/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
