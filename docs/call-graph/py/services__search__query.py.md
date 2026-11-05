# `services/search/query.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_detect_question_type` — function, line 14
- **called from:**
- `services/search/query.py:33`
- `services/search/query.py:95`
- `tests/test_question_type_detection.py:7`
- `tests/test_question_type_detection.py:8`
- `tests/test_question_type_detection.py:9`
- `tests/test_question_type_detection.py:15`
- `tests/test_question_type_detection.py:16`
- `tests/test_question_type_detection.py:17`
- `tests/test_question_type_detection.py:18`
- `tests/test_search_query_nonstring.py:27`
- `tests/test_search_query_nonstring.py:38`
- `tests/test_src_search_query_nonstring.py:10`
- `tests/test_src_search_query_nonstring.py:19`

## `_extract_entities` — function, line 28
- **called from:**
- `services/search/query.py:107`
- `tests/test_search_query.py:9`
- `tests/test_search_query.py:15`
- `tests/test_search_query.py:20`
- `tests/test_search_query_entities_nonstring.py:8`
- `tests/test_search_query_entities_nonstring.py:9`
- `tests/test_search_query_entities_nonstring.py:13`
- `tests/test_search_query_unicode_names.py:14`

## `_split_multi_part` — function, line 56
- **called from:**
- `services/search/query.py:91`
- `tests/test_search_query_nonstring.py:28`
- `tests/test_src_search_query_nonstring.py:11`

## `_extract_site_filter` — function, line 64
- **called from:**
- `services/search/query.py:90`
- `tests/test_search_query_nonstring.py:29`
- `tests/test_search_query_nonstring.py:40`
- `tests/test_src_search_query_nonstring.py:12`
- `tests/test_src_search_query_nonstring.py:21`

## `_boost_entities_in_query` — function, line 76
- **called from:**
- `services/search/query.py:108`

## `enhance_query` — function, line 86
- **called from:**
- `services/search/query.py:121`
- `tests/test_search_query_nonstring.py:32`
- `tests/test_src_search_query_nonstring.py:14`

## `build_enhanced_query` — function, line 119
- **called from:**
- `services/search/providers.py:362`
- `tests/test_search_query_nonstring.py:33`
- `tests/test_src_search_query_nonstring.py:15`

## `_is_news_query` — function, line 136
- **called from:**
- `services/search/query.py:147`
- `tests/test_search_query_nonstring.py:30`
- `tests/test_search_query_nonstring.py:39`
- `tests/test_src_search_query_nonstring.py:13`
- `tests/test_src_search_query_nonstring.py:20`

## `_cache_duration_for_query` — function, line 145
- **called from:**
- `services/search/core.py:956`
