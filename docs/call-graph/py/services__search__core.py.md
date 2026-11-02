# `services/search/core.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_secret_key` — function, line 52
- **called from:**
- `services/search/core.py:77`
- `services/search/core.py:92`
- `tests/test_search_config_no_key_leak.py:50`
- `tests/test_search_config_no_key_leak.py:51`
- `tests/test_search_config_no_key_leak.py:52`
- `tests/test_search_config_no_key_leak.py:53`

## `get_search_config` — function, line 57
- **called from:**
- `routes/search/search_routes.py:44`
- `services/search/service.py:102`
- `tests/test_search_config_no_key_leak.py:37`
- `tests/test_search_config_provider_key.py:16`
- `tests/test_search_config_provider_key.py:54`

## `update_search_config` — function, line 81
- **called from:**
- `src/app_initializer.py:148`
- `tests/test_search_config_no_key_leak.py:21`

## `_call_provider` — function, line 96
- **called from:**
- `routes/search/search_routes.py:103`
- `services/search/core.py:181`
- `services/search/core.py:288`

## `_build_provider_chain` — function, line 119
- **called from:**
- `services/search/core.py:174`
- `services/search/core.py:279`
- `src/deep_research.py:578`

## `searxng_search_results` — function, line 136
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `invalidate_search_cache` — function, line 220
- **called from:**
- `tests/test_search_cache_invalidation.py:37`

## `comprehensive_web_search` — function, line 250
- **called from:**
- `routes/search/search_routes.py:60`
- `services/research/research_handler.py:445`
- `src/agent_tools/web_tools.py:51`
- `src/chat_processor.py:462`
- `src/research_handler.py:949`
- `tests/test_search_content_block_source_index.py:43`
- `tests/test_search_content_block_source_index.py:60`

## `url_passes_filters` — function, line 321
- **called from:**
- `services/search/core.py:347`
