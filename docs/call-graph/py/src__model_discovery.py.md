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

## `ModelDiscovery.__init__` — method, line 94
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

## `ModelDiscovery._get_hosts` — method, line 101
- **called from:**
- `src/model_discovery.py:212`
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
- `src/model_discovery.py:204`
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

## `ModelDiscovery.discover_models` — method, line 210
- **called from:**
- `routes/model_routes.py:1928`
- `src/model_discovery.py:256`
- `src/model_discovery.py:268`
- `tests/test_llamacpp_discovery.py:40`
- `tests/test_lmstudio_discovery.py:35`
- `tests/test_lmstudio_discovery.py:53`

## `ModelDiscovery.warmup_ping_urls` — method, line 247
- **called from:**
- `tests/test_warmup_ping_urls.py:26`
- `tests/test_warmup_ping_urls.py:37`
- `tests/test_warmup_ping_urls.py:47`

## `ModelDiscovery.get_providers` — method, line 266
- **called from:**
- `routes/model_routes.py:1919`
