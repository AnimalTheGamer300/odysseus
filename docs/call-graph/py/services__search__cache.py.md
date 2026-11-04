# `services/search/cache.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `generate_cache_key` — function, line 35
- **called from:**
- `services/search/content.py:358`
- `services/search/core.py:145`
- `services/search/core.py:234`
- `tests/test_search_cache_invalidation.py:31`

## `cleanup_cache` — function, line 40
- **called from:**
- `services/search/content.py:607`
- `services/search/core.py:207`
