# `services/search/analytics.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SearchEngineError` — class, line 37
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `NetworkError` — class, line 41
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ParseError` — class, line 45
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `RateLimitError` — class, line 49
- **called from:**
- `services/search/content.py:393`
- `services/search/providers.py:324`
- `services/search/providers.py:494`
- `services/search/providers.py:552`
- `services/search/providers.py:613`

## `_default_analytics` — function, line 56
- **called from:**
- `services/search/analytics.py:70`
- `services/search/analytics.py:79`
- `services/search/analytics.py:85`

## `_load_analytics` — function, line 67
- **called from:**
- `services/search/analytics.py:99`
- `services/search/analytics.py:125`
- `tests/test_search_analytics_defaults.py:18`
- `tests/test_search_analytics_defaults.py:35`
- `tests/test_services_search_analytics_defaults.py:22`
- `tests/test_services_search_analytics_defaults.py:38`

## `_save_analytics` — function, line 88
- **called from:**
- `services/search/analytics.py:71`
- `services/search/analytics.py:120`

## `_record_query` — function, line 97
- **called from:**
- `services/search/core.py:158`
- `services/search/core.py:193`
- `tests/test_search_analytics_defaults.py:33`
- `tests/test_services_search_analytics_defaults.py:36`

## `get_search_stats` — function, line 123
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
