# `src/model_discovery.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_parse_tailscale_status` — function, line 19
- **called from:**
- `src/model_discovery.py:55`
- `tests/test_model_discovery_status.py:5`
- `tests/test_model_discovery_status.py:6`
- `tests/test_model_discovery_status.py:7`

## `_first_tailscale_ipv4` — function, line 27
- **called from:**
- `src/model_discovery.py:61`
- `src/model_discovery.py:78`

## `discover_tailscale_hosts` — function, line 36
- **called from:**
- `src/model_discovery.py:137`
- `tests/test_model_discovery_status.py:19`
- `tests/test_model_discovery_status.py:37`
- `tests/test_tailscale_discovery_cache.py:42`
- `tests/test_tailscale_discovery_cache.py:43`
- `tests/test_tailscale_discovery_cache.py:50`
- `tests/test_tailscale_discovery_cache.py:51`
- `tests/test_tailscale_discovery_cache.py:67`
- `tests/test_tailscale_discovery_cache.py:68`

## `ModelDiscovery` — class, line 93
- **called from:**
- `src/app_initializer.py:143`
- `tests/test_llamacpp_discovery.py:28`
- `tests/test_llamacpp_discovery.py:61`
- `tests/test_llamacpp_discovery.py:77`
- `tests/test_llamacpp_discovery.py:95`
- `tests/test_llamacpp_discovery.py:109`
- `tests/test_llamacpp_discovery.py:121`
- `tests/test_llamacpp_discovery.py:152`
- `tests/test_lmstudio_discovery.py:22`
- `tests/test_lmstudio_discovery.py:45`
- `tests/test_lmstudio_discovery.py:70`
- `tests/test_lmstudio_discovery.py:78`
- `tests/test_lmstudio_discovery.py:86`
- `tests/test_lmstudio_discovery.py:94`
- `tests/test_lmstudio_discovery.py:103`
- `tests/test_lmstudio_discovery.py:110`
- `tests/test_lmstudio_discovery.py:137`
- `tests/test_lmstudio_discovery.py:149`
- `tests/test_lmstudio_discovery.py:157`
- `tests/test_lmstudio_discovery.py:169`
- `tests/test_lmstudio_discovery.py:181`
- `tests/test_model_discovery_model_ids.py:10`
- `tests/test_model_discovery_model_ids.py:33`

## `ModelDiscovery.__init__` — method, line 94
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

## `ModelDiscovery._get_hosts` — method, line 101
- **called from:**
- `src/model_discovery.py:215`
- `tests/test_llamacpp_discovery.py:153`
- `tests/test_lmstudio_discovery.py:138`
- `tests/test_lmstudio_discovery.py:150`
- `tests/test_lmstudio_discovery.py:158`
- `tests/test_lmstudio_discovery.py:170`
- `tests/test_lmstudio_discovery.py:182`

## `ModelDiscovery._append_host` — method, line 105
- **called from:**
- `src/model_discovery.py:119`
- `src/model_discovery.py:132`
- `src/model_discovery.py:142`
- `src/model_discovery.py:149`

## `ModelDiscovery._append_env_hosts` — method, line 111
- **called from:**
- `src/model_discovery.py:133`
- `src/model_discovery.py:143`
- `src/model_discovery.py:150`

## `ModelDiscovery._fingerprint_provider` — method, line 153
- **called from:**
- `src/model_discovery.py:207`
- `tests/test_llamacpp_discovery.py:72`
- `tests/test_llamacpp_discovery.py:91`
- `tests/test_llamacpp_discovery.py:105`
- `tests/test_llamacpp_discovery.py:117`
- `tests/test_lmstudio_discovery.py:75`
- `tests/test_lmstudio_discovery.py:83`
- `tests/test_lmstudio_discovery.py:91`
- `tests/test_lmstudio_discovery.py:100`
- `tests/test_lmstudio_discovery.py:107`

## `ModelDiscovery._check_port` — method, line 186
- **called from:**
- `tests/test_llamacpp_discovery.py:133`
- `tests/test_llamacpp_discovery.py:175`
- `tests/test_lmstudio_discovery.py:118`
- `tests/test_model_discovery_model_ids.py:20`
- `tests/test_model_discovery_model_ids.py:33`

## `ModelDiscovery.discover_models` — method, line 213
- **called from:**
- `routes/model_routes.py:2078`
- `src/model_discovery.py:259`
- `src/model_discovery.py:271`
- `tests/test_llamacpp_discovery.py:40`
- `tests/test_lmstudio_discovery.py:35`
- `tests/test_lmstudio_discovery.py:53`

## `ModelDiscovery.warmup_ping_urls` — method, line 250
- **called from:**
- `tests/test_warmup_ping_urls.py:26`
- `tests/test_warmup_ping_urls.py:37`
- `tests/test_warmup_ping_urls.py:47`

## `ModelDiscovery.get_providers` — method, line 269
- **called from:**
- `routes/model_routes.py:2069`
