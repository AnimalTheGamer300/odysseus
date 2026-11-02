# `services/search/providers.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_get_search_settings` — function, line 32
- **called from:**
- `services/search/core.py:65`
- `services/search/core.py:122`
- `services/search/core.py:138`
- `services/search/core.py:267`
- `services/search/providers.py:43`
- `services/search/providers.py:52`
- `services/search/providers.py:80`
- `services/search/providers.py:94`
- `services/search/providers.py:464`
- `src/deep_research.py:566`

## `_get_search_instance` — function, line 41
- **called from:**
- `routes/search/search_routes.py:78`
- `services/search/core.py:72`
- `services/search/providers.py:139`
- `services/search/providers.py:251`

## `_get_provider_key` — function, line 50
- **called from:**
- `routes/search/search_routes.py:76`
- `services/search/core.py:68`
- `services/search/providers.py:287`
- `services/search/providers.py:465`
- `services/search/providers.py:529`
- `services/search/providers.py:588`
- `tests/test_search_config_provider_key.py:55`

## `_get_result_count` — function, line 78
- **called from:**
- `services/search/core.py:69`
- `services/search/core.py:140`
- `services/search/core.py:234`
- `services/search/core.py:269`
- `services/search/providers.py:138`
- `services/search/providers.py:286`
- `services/search/providers.py:386`
- `services/search/providers.py:463`
- `services/search/providers.py:528`
- `services/search/providers.py:587`

## `_get_safesearch_level` — function, line 92
- **called from:**
- `services/search/providers.py:108`

## `_safesearch_for` — function, line 106
- **called from:**
- `services/search/providers.py:158`
- `services/search/providers.py:208`
- `services/search/providers.py:259`
- `services/search/providers.py:308`
- `services/search/providers.py:391`
- `services/search/providers.py:434`
- `services/search/providers.py:478`
- `services/search/providers.py:597`
- `tests/test_service_search_provider_guards.py:14`
- `tests/test_service_search_provider_guards.py:15`
- `tests/test_service_search_provider_guards.py:16`
- `tests/test_service_search_provider_guards.py:17`
- `tests/test_service_search_provider_guards.py:18`
- `tests/test_service_search_provider_guards.py:19`
- `tests/test_service_search_provider_guards.py:22`
- `tests/test_service_search_provider_guards.py:23`
- `tests/test_service_search_provider_guards.py:24`
- `tests/test_service_search_provider_guards.py:25`
- `tests/test_service_search_provider_guards.py:26`
- `tests/test_service_search_provider_guards.py:27`

## `searxng_search_api` — function, line 135
- **called from:**
- `services/search/core.py:99`
- `tests/test_service_search_provider_guards.py:53`

## `_parse_results` — function, line 175
- **called from:**
- `services/search/providers.py:195`

## `_run` — function, line 186
- **called from:**
- `services/hwfit/hardware.py:87`
- `services/hwfit/hardware.py:94`
- `services/hwfit/hardware.py:108`
- `services/hwfit/hardware.py:110`
- `services/hwfit/hardware.py:211`
- `services/hwfit/hardware.py:221`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:294`
- `services/hwfit/hardware.py:323`
- `services/hwfit/hardware.py:325`
- `services/hwfit/hardware.py:338`
- `services/hwfit/hardware.py:341`
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`
- `services/hwfit/hardware.py:393`
- `services/hwfit/hardware.py:422`
- `services/hwfit/hardware.py:466`
- `services/hwfit/hardware.py:491`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:549`
- `services/hwfit/hardware.py:554`
- `services/hwfit/hardware.py:557`
- `services/hwfit/hardware.py:562`
- `services/hwfit/hardware.py:635`
- `services/research/research_handler.py:102`
- `services/search/providers.py:198`
- `services/search/providers.py:217`
- `services/search/providers.py:226`
- `services/search/providers.py:234`
- `src/research_handler.py:403`
- `tests/test_agent_rounds_exhausted.py:18`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- `tests/test_app_config_shared_fetch_js.py:322`
- `tests/test_ask_user_persistence.py:22`
- `tests/test_ask_user_tool.py:31`
- `tests/test_ask_user_tool.py:48`
- `tests/test_ask_user_tool.py:55`
- `tests/test_ask_user_tool.py:65`
- `tests/test_ask_user_tool.py:71`
- `tests/test_ask_user_tool.py:78`
- `tests/test_bg_job_tools.py:90`
- `tests/test_bg_job_tools.py:96`
- `tests/test_bg_job_tools.py:102`
- `tests/test_bg_job_tools.py:108`
- `tests/test_bg_job_tools.py:114`
- `tests/test_bg_job_tools.py:122`
- `tests/test_bg_job_tools.py:128`
- `tests/test_bg_job_tools.py:132`
- `tests/test_bg_job_tools.py:138`
- … +122 more (grep the name in repo)

## `searxng_search` — function, line 249
- **called from:**
- `services/search/providers.py:243`

## `brave_search` — function, line 284
- **called from:**
- `services/search/core.py:101`
- `tests/test_search_provider_json.py:59`

## `_brave_search_impl` — function, line 291
- **called from:**
- `services/search/providers.py:288`

## `_is_duckduckgo_host` — function, line 358
- **called from:**
- `services/search/providers.py:375`
- `tests/test_ddg_redirect_resolution.py:32`
- `tests/test_ddg_redirect_resolution.py:33`
- `tests/test_ddg_redirect_resolution.py:34`
- `tests/test_ddg_redirect_resolution.py:35`
- `tests/test_ddg_redirect_resolution.py:36`
- `tests/test_ddg_redirect_resolution.py:37`

## `_resolve_ddg_redirect` — function, line 364
- **called from:**
- `services/search/providers.py:402`
- `tests/test_ddg_redirect_resolution.py:15`
- `tests/test_ddg_redirect_resolution.py:19`
- `tests/test_ddg_redirect_resolution.py:28`
- `tests/test_service_search_provider_guards.py:63`
- `tests/test_service_search_provider_guards.py:65`

## `duckduckgo_search` — function, line 384
- **called from:**
- `services/search/core.py:103`
- `tests/test_service_search_provider_guards.py:97`

## `_html_fallback` — function, line 387
- **called from:**
- `services/search/providers.py:421`
- `services/search/providers.py:447`
- `services/search/providers.py:450`

## `google_pse_search` — function, line 455
- **called from:**
- `services/search/core.py:105`
- `tests/test_search_provider_json.py:54`

## `tavily_search` — function, line 526
- **called from:**
- `services/search/core.py:107`
- `tests/test_search_provider_json.py:46`

## `serper_search` — function, line 585
- **called from:**
- `services/search/core.py:109`
- `tests/test_search_provider_json.py:50`
