# `routes/model_routes.py` — definitions & call sites

108 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_speech_settings_using_endpoint` — function, line 57
- **called from:**
- `routes/model_routes.py:90`
- `tests/test_model_routes.py:70`

## `_clear_speech_settings_for_endpoint` — function, line 67
- **called from:**
- `routes/model_routes.py:114`
- `tests/test_model_routes.py:81`

## `_endpoint_settings_using_endpoint` — function, line 79
- **called from:**
- `routes/model_routes.py:2587`
- `tests/test_model_routes.py:110`

## `_clear_endpoint_settings_for_endpoint` — function, line 94
- **called from:**
- `routes/model_routes.py:170`
- `routes/model_routes.py:192`
- `routes/model_routes.py:2592`
- `tests/test_model_routes.py:117`

## `_active_cookbook_endpoint_ids` — function, line 123
- **called from:**
- `routes/model_routes.py:153`

## `_disable_stale_cookbook_local_endpoints` — function, line 151
- **called from:**
- `routes/model_routes.py:1479`
- `routes/model_routes.py:1554`
- `routes/model_routes.py:1697`
- `routes/model_routes.py:1937`

## `_clear_user_pref_endpoint_refs` — function, line 179
- **called from:**
- `routes/model_routes.py:2602`
- `tests/test_model_routes.py:160`
- `tests/test_model_routes.py:176`

## `_endpoint_visible_model_ids` — function, line 197
- **called from:**
- `routes/model_routes.py:232`

## `_default_endpoint_needs_assignment` — function, line 208
- **called from:**
- `routes/model_routes.py:2195`
- `tests/test_model_routes.py:186`
- `tests/test_model_routes.py:194`
- `tests/test_model_routes.py:199`

## `_docker_host_gateway_reachable` — function, line 243
- **called from:**
- `routes/model_routes.py:314`
- `routes/model_routes.py:319`
- `tests/test_model_routes.py:849`
- `tests/test_model_routes.py:854`
- `tests/test_model_routes.py:863`

## `_container_loopback_reachable` — function, line 263
- **called from:**
- `routes/model_routes.py:317`

## `_rewrite_loopback_for_docker` — function, line 290
- **called from:**
- `routes/model_routes.py:2020`
- `routes/model_routes.py:2240`
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

## `_match_provider_curated` — function, line 405
- **called from:**
- `routes/model_routes.py:1021`
- `routes/model_routes.py:1026`
- `routes/model_routes.py:1061`
- `routes/model_routes.py:1576`
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

## `_curate_models` — function, line 424
- **called from:**
- `routes/model_routes.py:1577`
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

## `_best_match_idx` — function, line 434
- **called from:**
- `routes/model_routes.py:443`
- `routes/model_routes.py:448`

## `_truthy` — function, line 452
- **called from:**
- `routes/model_routes.py:2020`
- `routes/model_routes.py:2030`
- `routes/model_routes.py:2032`
- `tests/test_model_routes.py:590`
- `tests/test_model_routes.py:594`

## `_normalize_endpoint_kind` — function, line 460
- **called from:**
- `routes/model_routes.py:467`
- `routes/model_routes.py:478`
- `routes/model_routes.py:574`
- `routes/model_routes.py:790`
- `routes/model_routes.py:2026`
- `routes/model_routes.py:2241`
- `routes/model_routes.py:2535`

## `_normalize_refresh_mode` — function, line 465
- **called from:**
- `routes/model_routes.py:875`
- `tests/test_model_routes.py:489`
- `tests/test_model_routes.py:490`
- `tests/test_model_routes.py:491`
- `tests/test_model_routes.py:492`

## `_endpoint_kind` — function, line 477
- **called from:**
- `routes/model_routes.py:484`
- `routes/model_routes.py:806`
- `routes/model_routes.py:2076`
- `routes/model_routes.py:2539`

## `_endpoint_refresh_mode` — function, line 481
- **called from:**
- `routes/model_routes.py:1424`
- `routes/model_routes.py:1978`
- `routes/model_routes.py:2079`
- `tests/test_model_routes.py:512`
- `tests/test_model_routes.py:514`

## `_endpoint_refresh_interval` — function, line 489
- **called from:**
- `routes/model_routes.py:1456`

## `_endpoint_refresh_timeout` — function, line 500
- **called from:**
- `routes/model_routes.py:525`
- `routes/model_routes.py:1437`

## `_manual_refresh_timeout` — function, line 514
- **called from:**
- `routes/model_routes.py:2329`

## `_parse_model_list` — function, line 529
- **called from:**
- `routes/model_routes.py:582`
- `routes/model_routes.py:586`
- `tests/test_model_routes.py:517`
- `tests/test_model_routes.py:518`

## `_parse_positive_int` — function, line 559
- **called from:**
- `routes/model_routes.py:520`
- `routes/model_routes.py:523`
- `routes/model_routes.py:571`
- `routes/model_routes.py:2028`
- `routes/model_routes.py:2029`
- `routes/model_routes.py:2242`
- `routes/model_routes.py:2543`
- `routes/model_routes.py:2546`

## `_explicit_model_list_timeout` — function, line 569
- **called from:**
- `routes/model_routes.py:2034`
- `routes/model_routes.py:2106`
- `routes/model_routes.py:2243`

## `_cached_model_ids` — function, line 581
- **called from:**
- `routes/model_routes.py:1345`
- `routes/model_routes.py:1364`
- `routes/model_routes.py:1425`
- `routes/model_routes.py:1771`
- `routes/model_routes.py:1943`
- `routes/model_routes.py:2115`
- `routes/model_routes.py:2323`
- `routes/model_routes.py:2391`

## `_hidden_model_ids` — function, line 585
- **called from:**
- `routes/model_routes.py:1361`
- `routes/model_routes.py:1944`
- `routes/model_routes.py:2322`

## `_is_ollama_base` — function, line 589
- **called from:**
- `routes/model_routes.py:578`
- `routes/model_routes.py:809`

## `_is_chat_model` — function, line 621
- **called from:**
- `routes/model_routes.py:1030`
- `routes/model_routes.py:1057`
- `routes/model_routes.py:1888`
- `routes/model_routes.py:2272`
- `tests/test_model_routes.py:408`
- `tests/test_model_routes.py:415`
- `tests/test_model_routes.py:418`
- `tests/test_model_routes.py:422`
- `tests/test_model_routes.py:425`
- `tests/test_model_routes.py:428`
- `tests/test_model_routes.py:434`

## `_delete_orphaned_provider_auth` — function, line 640
- **called from:**
- `routes/model_routes.py:2679`
- `tests/test_chatgpt_subscription_routes.py:118`
- `tests/test_chatgpt_subscription_routes.py:137`
- `tests/test_chatgpt_subscription_routes.py:151`
- `tests/test_chatgpt_subscription_routes.py:163`
- `tests/test_chatgpt_subscription_routes.py:184`
- `tests/test_chatgpt_subscription_routes.py:269`
- `tests/test_chatgpt_subscription_routes.py:276`

## `_safe_detect_provider` — function, line 658
- **called from:**
- `routes/model_routes.py:704`
- `routes/model_routes.py:964`
- `routes/model_routes.py:1567`
- `routes/model_routes.py:1769`

## `_safe_build_models_url` — function, line 667
- **called from:**
- `routes/model_routes.py:983`
- `routes/model_routes.py:1006`
- `routes/model_routes.py:1146`

## `_safe_build_headers` — function, line 678
- **called from:**
- `routes/model_routes.py:725`
- `routes/model_routes.py:730`
- `routes/model_routes.py:1007`
- `routes/model_routes.py:1073`

## `_is_discovery_only_provider` — function, line 687
- **called from:**
- `routes/model_routes.py:705`

## `_resolve_probe_key` — function, line 691
- **called from:**
- `tests/test_endpoint_probing.py:456`
- `tests/test_endpoint_probing.py:467`
- `tests/test_endpoint_probing.py:477`

## `_probe_single_model` — function, line 702
- **called from:**
- `routes/model_routes.py:1832`
- `routes/model_routes.py:1894`
- `routes/model_routes.py:2280`
- `tests/test_endpoint_probing.py:338`
- `tests/test_endpoint_probing.py:359`
- `tests/test_endpoint_probing.py:370`
- `tests/test_endpoint_probing.py:381`
- `tests/test_endpoint_probing.py:392`
- `tests/test_endpoint_probing.py:403`
- `tests/test_endpoint_probing.py:416`
- `tests/test_endpoint_probing.py:431`
- `tests/test_endpoint_probing.py:444`

## `_local_ip_literal` — function, line 778
- **called from:**
- `routes/model_routes.py:797`

## `_classify_endpoint` — function, line 786
- **called from:**
- `routes/model_routes.py:575`
- `routes/model_routes.py:1321`
- `routes/model_routes.py:1423`
- `routes/model_routes.py:1572`
- `routes/model_routes.py:1704`
- `routes/model_routes.py:1777`
- `routes/model_routes.py:1977`
- `routes/model_routes.py:2134`
- `routes/model_routes.py:2223`
- `routes/model_routes.py:2254`
- `routes/model_routes.py:2328`
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

## `_effective_endpoint_kind` — function, line 804
- **called from:**
- `routes/model_routes.py:1422`
- `routes/model_routes.py:1571`
- `routes/model_routes.py:1703`
- `routes/model_routes.py:1770`
- `routes/model_routes.py:1951`
- `routes/model_routes.py:2075`
- `routes/model_routes.py:2117`
- `routes/model_routes.py:2325`
- `routes/model_routes.py:2385`
- `routes/model_routes.py:2400`
- `routes/model_routes.py:2528`
- `tests/test_model_routes.py:486`

## `_is_loading_model_response` — function, line 819
- **called from:**
- `routes/model_routes.py:1032`
- `routes/model_routes.py:1109`

## `_openai_model_ids` — function, line 830
- **called from:**
- `routes/model_routes.py:991`
- `routes/model_routes.py:1013`
- `tests/test_endpoint_probing.py:91`

## `_ollama_model_names` — function, line 848
- **called from:**
- `routes/model_routes.py:1016`
- `routes/model_routes.py:1055`
- `tests/test_endpoint_probing.py:103`

## `_is_google_api_base` — function, line 865
- **called from:**
- `routes/model_routes.py:873`
- `routes/model_routes.py:970`
- `tests/test_model_routes.py:501`
- `tests/test_model_routes.py:502`

## `_normalize_endpoint_refresh_mode` — function, line 872
- **called from:**
- `routes/model_routes.py:482`
- `routes/model_routes.py:2027`
- `routes/model_routes.py:2537`
- `tests/test_model_routes.py:496`
- `tests/test_model_routes.py:497`
- `tests/test_model_routes.py:498`

## `_google_native_root` — function, line 878
- **called from:**
- `routes/model_routes.py:898`

## `_google_native_models_url` — function, line 897
- **called from:**
- `routes/model_routes.py:926`

## `_google_model_id_from_item` — function, line 901
- **called from:**
- `routes/model_routes.py:948`

## `_google_model_supports_chat` — function, line 908
- **called from:**
- `routes/model_routes.py:946`

## `_probe_google_models` — function, line 919
- **called from:**
- `routes/model_routes.py:972`

## `_probe_endpoint` — function, line 958
- **called from:**
- `routes/cookbook_routes.py:1878`
- `routes/cookbook_routes.py:1946`
- `routes/model_routes.py:1502`
- `routes/model_routes.py:1873`
- `routes/model_routes.py:2103`
- `routes/model_routes.py:2139`
- `routes/model_routes.py:2244`
- `routes/model_routes.py:2271`
- `routes/model_routes.py:2331`
- `src/research_handler.py:785`
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

## `_ping_endpoint` — function, line 1069
- **called from:**
- `routes/model_routes.py:1782`
- `routes/model_routes.py:2142`
- `routes/model_routes.py:2245`
- `tests/test_endpoint_probing.py:220`
- `tests/test_endpoint_probing.py:231`
- `tests/test_endpoint_probing.py:242`
- `tests/test_endpoint_probing.py:254`
- `tests/test_endpoint_probing.py:265`
- `tests/test_endpoint_probing.py:280`
- `tests/test_model_routes.py:535`
- `tests/test_model_routes.py:556`
- `tests/test_model_routes.py:577`

## `_is_loading_model_response` — function, line 1084
- **called from:**
- `routes/model_routes.py:1032`
- `routes/model_routes.py:1109`

## `_result_from_response` — function, line 1093
- **called from:**
- `routes/model_routes.py:1130`
- `routes/model_routes.py:1141`
- `routes/model_routes.py:1149`

## `_model_endpoint_error_message` — function, line 1164
- **called from:**
- `routes/model_routes.py:2144`
- `tests/test_model_routes.py:760`
- `tests/test_model_routes.py:772`
- `tests/test_model_routes.py:787`
- `tests/test_model_routes.py:804`

## `_normalize_model_ids` — function, line 1225
- **called from:**
- `routes/model_routes.py:1310`
- `routes/model_routes.py:1311`
- `routes/model_routes.py:1316`
- `routes/model_routes.py:1358`
- `routes/model_routes.py:1945`
- `routes/model_routes.py:2067`
- `routes/model_routes.py:2070`
- `routes/model_routes.py:2116`
- `routes/model_routes.py:2151`
- `routes/model_routes.py:2345`
- `routes/model_routes.py:2398`
- `routes/model_routes.py:2526`
- `routes/model_routes.py:2576`
- `tests/test_model_routes.py:871`
- `tests/test_model_routes.py:874`
- `tests/test_model_routes.py:877`
- `tests/test_model_routes.py:880`
- `tests/test_model_routes.py:881`
- `tests/test_model_routes.py:882`
- `tests/test_model_routes.py:885`

## `_merge_model_ids` — function, line 1258
- **called from:**
- `routes/model_routes.py:1309`
- `routes/model_routes.py:1956`
- `routes/model_routes.py:2069`
- `routes/model_routes.py:2217`
- `routes/model_routes.py:2357`

## `_is_mlx_deepseek_v4_repo_id` — function, line 1270
- **called from:**
- `routes/model_routes.py:1291`
- `src/endpoint_resolver.py:112`

## `_is_mlx_deepseek_v4_shim_id` — function, line 1275
- **called from:**
- `routes/model_routes.py:1288`
- `routes/model_routes.py:1295`
- `src/endpoint_resolver.py:109`

## `_filter_mlx_deepseek_v4_repo_when_shimmed` — function, line 1280
- **called from:**
- `routes/model_routes.py:1313`
- `src/endpoint_resolver.py:142`

## `_model_display_name` — function, line 1294
- **called from:**
- `routes/model_routes.py:1589`
- `routes/model_routes.py:1591`

## `_visible_models` — function, line 1300
- **called from:**
- `routes/chat_routes.py:751`
- `routes/chat_routes.py:777`
- `routes/model_routes.py:201`
- `routes/model_routes.py:1344`
- `routes/model_routes.py:1363`
- `routes/model_routes.py:2124`
- `routes/model_routes.py:2391`
- `routes/model_routes.py:2488`
- `tests/test_model_routes.py:893`
- `tests/test_model_routes.py:897`
- `tests/test_model_routes.py:901`
- `tests/test_model_routes.py:905`
- `tests/test_model_routes.py:1228`
- `tests/test_model_routes.py:1231`
- `tests/test_model_routes.py:1232`
- `tests/test_review_regressions.py:1418`
- `tests/test_review_regressions.py:1429`
- `tests/test_review_regressions.py:1440`
- `tests/test_review_regressions.py:1451`

## `_picker_requires_pinning` — function, line 1320
- **called from:**
- `routes/model_routes.py:1359`
- `routes/model_routes.py:1953`
- `routes/model_routes.py:1957`
- `routes/model_routes.py:2326`
- `routes/model_routes.py:2386`
- `routes/model_routes.py:2401`
- `routes/model_routes.py:2529`

## `_has_explicit_pinned_models` — function, line 1324
- **called from:**
- `routes/model_routes.py:1360`
- `routes/model_routes.py:1953`
- `routes/model_routes.py:2346`

## `_legacy_visible_api_models` — function, line 1335
- **called from:**
- `routes/model_routes.py:1361`
- `routes/model_routes.py:2347`

## `_picker_models_for_endpoint` — function, line 1351
- **called from:**
- `routes/model_routes.py:1573`
- `routes/model_routes.py:1952`
- `tests/test_model_routes.py:1340`

## `_api_key_fingerprint` — function, line 1370
- **called from:**
- `routes/model_routes.py:1964`
- `routes/model_routes.py:2123`
- `routes/model_routes.py:2216`
- `tests/test_model_routes.py:1236`
- `tests/test_model_routes.py:1238`
- `tests/test_model_routes.py:1239`
- `tests/test_model_routes.py:1240`
- `tests/test_model_routes.py:1305`
- `tests/test_model_routes.py:1506`
- `tests/test_model_routes.py:1572`

## `setup_model_routes` — function, line 1378
- **called from:**
- `app.py:744`
- `tests/test_chatgpt_subscription_routes.py:208`
- `tests/test_model_defaults.py:125`
- `tests/test_model_defaults.py:195`
- `tests/test_model_routes.py:978`
- `tests/test_model_routes.py:1706`
- `tests/test_model_routes.py:1741`
- `tests/test_model_routes.py:1782`
- `tests/test_model_routes.py:1815`
- `tests/test_model_routes.py:1840`
- `tests/test_model_routes.py:1865`
- `tests/test_model_routes.py:1890`
- `tests/test_model_routes.py:1924`
- `tests/test_model_routes.py:1949`
- `tests/test_model_routes.py:1982`
- `tests/test_model_routes.py:2015`
- `tests/test_model_routes.py:2075`
- `tests/test_model_routes.py:2120`
- `tests/test_model_routes.py:2156`
- `tests/test_review_regressions.py:73`
- `tests/test_review_regressions.py:154`

## `_invalidate_models_cache` — function, line 1390
- **called from:**
- `routes/chatgpt_subscription_routes.py:103`
- `routes/copilot_routes.py:96`
- `routes/model_routes.py:1530`
- `routes/model_routes.py:1555`
- `routes/model_routes.py:1698`
- `routes/model_routes.py:1938`
- `routes/model_routes.py:1984`
- `routes/model_routes.py:2113`
- `routes/model_routes.py:2205`
- `routes/model_routes.py:2301`
- `routes/model_routes.py:2339`
- `routes/model_routes.py:2407`
- `routes/model_routes.py:2567`
- `routes/model_routes.py:2681`

## `_refresh_key` — function, line 1404
- **called from:**
- `routes/model_routes.py:1426`
- `routes/model_routes.py:1711`

## `_ts` — function, line 1407
- **called from:**
- `routes/model_routes.py:1457`
- `routes/model_routes.py:1457`

## `_failure_delay` — function, line 1413
- **called from:**
- `routes/model_routes.py:1453`

## `_should_refresh_endpoint` — function, line 1420
- **called from:**
- `routes/model_routes.py:1485`

## `_refresh_caches_bg` — function, line 1462
- **called from:**
- `routes/model_routes.py:1665`

## `_do` — function, line 1473
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_probe_one` — function, line 1500
- **called from:**
- `routes/model_routes.py:1736`

## `_fetch_models` — function, line 1539
- **called from:**
- `routes/model_routes.py:1659`

## `api_models` — function, line 1619
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_local_endpoints` — function (async), line 1677
- **route:** `GET /model-endpoints/probe-local`
- decorator: `router.get("/model-endpoints/probe-local")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_compute_local_probe` — function (async), line 1694
- **called from:**
- `routes/model_routes.py:1748`

## `_probe_one` — function (async), line 1714
- **called from:**
- `routes/model_routes.py:1736`

## `ping_endpoints` — function, line 1757
- **route:** `GET /ping`
- decorator: `router.get("/ping")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_selected` — function, line 1797
- **route:** `POST /probe-selected`
- decorator: `router.post("/probe-selected")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_models` — function, line 1842
- **route:** `GET /probe`
- decorator: `router.get("/probe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_empty` — function, line 1864
- **called from:**
- `routes/model_routes.py:1866`

## `_stream` — function, line 1868
- **called from:**
- `routes/model_routes.py:1904`
- `routes/model_routes.py:2305`

## `providers` — function, line 1913
- **route:** `GET /providers`
- decorator: `router.get("/providers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `discover_local` — function, line 1925
- **route:** `GET /discover`
- decorator: `router.get("/discover")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_model_endpoints` — function, line 1933
- **route:** `GET /model-endpoints`
- decorator: `router.get("/model-endpoints")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_model_endpoint` — function, line 1990
- **route:** `POST /model-endpoints`
- decorator: `router.post("/model-endpoints")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_model_endpoint` — function, line 2227
- **route:** `POST /model-endpoints/test`
- decorator: `router.post("/model-endpoints/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe_endpoint_models` — function, line 2258
- **route:** `GET /model-endpoints/{ep_id}/probe`
- decorator: `router.get("/model-endpoints/{ep_id}/probe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_stream` — function, line 2275
- **called from:**
- `routes/model_routes.py:1904`
- `routes/model_routes.py:2305`

## `list_endpoint_models` — function, line 2308
- **route:** `GET /model-endpoints/{ep_id}/models`
- decorator: `router.get("/model-endpoints/{ep_id}/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_hidden_models` — function (async), line 2363
- **route:** `PATCH /model-endpoints/{ep_id}/models`
- decorator: `router.patch("/model-endpoints/{ep_id}/models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_default_chat` — function, line 2415
- **route:** `GET /default-chat`
- decorator: `router.get("/default-chat")`
- **called from:**
- `tests/test_model_defaults.py:129`
- `tests/test_model_defaults.py:199`

## `toggle_model_endpoint` — function (async), line 2498
- **route:** `PATCH /model-endpoints/{ep_id}`
- decorator: `router.patch("/model-endpoints/{ep_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_settings_using_endpoint` — function, line 2585
- **called from:**
- `routes/model_routes.py:2662`

## `_clear_settings_for_endpoint` — function, line 2589
- **called from:**
- `routes/model_routes.py:2673`

## `_clear_user_prefs_for_endpoint` — function, line 2597
- **called from:**
- `routes/model_routes.py:2674`

## `_session_uses_endpoint_url` — function, line 2610
- **called from:**
- `routes/model_routes.py:2634`
- `routes/model_routes.py:2651`

## `_clear_sessions_for_endpoint` — function, line 2622
- **called from:**
- `routes/model_routes.py:2675`

## `_clear_loaded_sessions_for_endpoint` — function, line 2640
- **called from:**
- `routes/model_routes.py:2676`

## `get_endpoint_dependents` — function, line 2659
- **route:** `GET /model-endpoints/{ep_id}/dependents`
- decorator: `router.get("/model-endpoints/{ep_id}/dependents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_model_endpoint` — function, line 2665
- **route:** `DELETE /model-endpoints/{ep_id}`
- decorator: `router.delete("/model-endpoints/{ep_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_tools` — function, line 2697
- **route:** `GET /tools`
- decorator: `router.get("/tools")`
- **called from:**
- `mcp_servers/email_server.py:2088`
- `mcp_servers/image_gen_server.py:24`
- `mcp_servers/memory_server.py:115`
- `mcp_servers/rag_server.py:46`
- `src/mcp_manager.py:205`
- `src/mcp_manager.py:274`
- `src/mcp_manager.py:362`

## `ToolsUpdate` — class, line 2707
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_tools` — function, line 2711
- **route:** `POST /tools`
- decorator: `router.post("/tools")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
