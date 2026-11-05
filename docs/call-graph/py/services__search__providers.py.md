# `services/search/providers.py` — definitions & call sites

20 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_get_search_settings` — function, line 33
- **called from:**
- `services/search/core.py:78`
- `services/search/core.py:137`
- `services/search/core.py:844`
- `services/search/core.py:1026`
- `services/search/providers.py:51`
- `services/search/providers.py:60`
- `services/search/providers.py:93`
- `services/search/providers.py:109`
- `services/search/providers.py:120`
- `services/search/providers.py:537`
- `src/research_navigator.py:161`
- `tests/test_search_config_provider_key.py:71`

## `_get_search_instance` — function, line 49
- **called from:**
- `routes/search/search_routes.py:179`
- `scripts/audit_search_pipeline.py:33`
- `services/search/core.py:85`
- `services/search/providers.py:185`
- `services/search/providers.py:315`

## `_get_provider_key` — function, line 58
- **called from:**
- `routes/search/search_routes.py:177`
- `services/search/core.py:81`
- `services/search/providers.py:106`
- `services/search/providers.py:356`
- `services/search/providers.py:538`
- `services/search/providers.py:602`
- `services/search/providers.py:661`
- `tests/test_search_config_provider_key.py:56`
- `tests/test_search_config_provider_key.py:63`

## `_get_result_count` — function, line 91
- **called from:**
- `services/search/core.py:82`
- `services/search/core.py:846`
- `services/search/core.py:992`
- `services/search/core.py:1028`
- `services/search/providers.py:184`
- `services/search/providers.py:355`
- `services/search/providers.py:455`
- `services/search/providers.py:536`
- `services/search/providers.py:601`
- `services/search/providers.py:660`

## `provider_configured` — function, line 100
- **called from:**
- `services/search/core.py:146`
- `tests/test_search_config_provider_key.py:64`

## `_get_safesearch_level` — function, line 118
- **called from:**
- `services/search/providers.py:134`

## `_safesearch_for` — function, line 132
- **called from:**
- `scripts/audit_search_pipeline.py:35`
- `services/search/providers.py:204`
- `services/search/providers.py:324`
- `services/search/providers.py:377`
- `services/search/providers.py:460`
- `services/search/providers.py:507`
- `services/search/providers.py:551`
- `services/search/providers.py:670`
- `tests/test_service_search_provider_guards.py:109`
- `tests/test_service_search_provider_guards.py:110`
- `tests/test_service_search_provider_guards.py:111`
- `tests/test_service_search_provider_guards.py:112`
- `tests/test_service_search_provider_guards.py:113`
- `tests/test_service_search_provider_guards.py:114`
- `tests/test_service_search_provider_guards.py:117`
- `tests/test_service_search_provider_guards.py:118`
- `tests/test_service_search_provider_guards.py:119`
- `tests/test_service_search_provider_guards.py:120`
- `tests/test_service_search_provider_guards.py:121`
- `tests/test_service_search_provider_guards.py:122`

## `searxng_search_api` — function, line 181
- **called from:**
- `services/search/core.py:112`
- `services/search/core.py:114`
- `services/search/core.py:701`
- `tests/test_search_publication_intent.py:65`
- `tests/test_search_publication_intent.py:82`
- `tests/test_service_search_provider_guards.py:57`
- `tests/test_service_search_provider_guards.py:86`
- `tests/test_service_search_provider_guards.py:148`
- `tests/test_service_search_provider_guards.py:186`
- `tests/test_service_search_provider_guards.py:224`

## `_parse_results` — function, line 241
- **called from:**
- `services/search/providers.py:265`

## `_run` — function, line 256
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
- `services/search/providers.py:268`
- `services/search/providers.py:281`
- `services/search/providers.py:290`
- `services/search/providers.py:298`
- `src/research_handler.py:421`
- `tests/test_agent_evidence_loop.py:128`
- `tests/test_agent_evidence_loop.py:140`
- `tests/test_agent_evidence_loop.py:152`
- `tests/test_agent_evidence_loop.py:163`
- `tests/test_agent_evidence_loop.py:189`
- `tests/test_agent_evidence_loop.py:222`
- `tests/test_agent_evidence_loop.py:262`
- `tests/test_agent_evidence_loop.py:304`
- `tests/test_agent_evidence_loop.py:356`
- `tests/test_agent_evidence_loop.py:399`
- `tests/test_agent_evidence_loop.py:439`
- `tests/test_agent_evidence_loop.py:461`
- `tests/test_agent_evidence_loop.py:627`
- `tests/test_agent_evidence_loop.py:649`
- `tests/test_agent_evidence_loop.py:677`
- `tests/test_agent_evidence_loop.py:715`
- `tests/test_agent_rounds_exhausted.py:24`
- `tests/test_agent_runtime_context.py:28`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- … +208 more (grep the name in repo)

## `searxng_search` — function, line 313
- **called from:**
- `services/search/providers.py:307`

## `brave_search` — function, line 353
- **called from:**
- `services/search/core.py:116`
- `tests/test_search_provider_json.py:59`

## `_brave_search_impl` — function, line 360
- **called from:**
- `services/search/providers.py:357`

## `_is_duckduckgo_host` — function, line 427
- **called from:**
- `services/search/providers.py:444`
- `tests/test_ddg_redirect_resolution.py:32`
- `tests/test_ddg_redirect_resolution.py:33`
- `tests/test_ddg_redirect_resolution.py:34`
- `tests/test_ddg_redirect_resolution.py:35`
- `tests/test_ddg_redirect_resolution.py:36`
- `tests/test_ddg_redirect_resolution.py:37`

## `_resolve_ddg_redirect` — function, line 433
- **called from:**
- `services/search/providers.py:475`
- `tests/test_ddg_redirect_resolution.py:15`
- `tests/test_ddg_redirect_resolution.py:19`
- `tests/test_ddg_redirect_resolution.py:28`
- `tests/test_service_search_provider_guards.py:744`
- `tests/test_service_search_provider_guards.py:746`

## `duckduckgo_search` — function, line 453
- **called from:**
- `services/search/core.py:118`
- `tests/test_service_search_provider_guards.py:779`

## `_html_fallback` — function, line 456
- **called from:**
- `services/search/providers.py:494`
- `services/search/providers.py:520`
- `services/search/providers.py:523`

## `google_pse_search` — function, line 528
- **called from:**
- `services/search/core.py:120`
- `tests/test_search_provider_json.py:54`

## `tavily_search` — function, line 599
- **called from:**
- `services/search/core.py:122`
- `tests/test_search_provider_json.py:46`

## `serper_search` — function, line 658
- **called from:**
- `services/search/core.py:124`
- `tests/test_search_provider_json.py:50`
