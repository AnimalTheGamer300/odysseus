# `services/search/ranking.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow_naive` — function, line 14
- **called from:**
- `services/search/ranking.py:39`
- `src/session_actions.py:34`
- `src/session_actions.py:74`
- `src/session_actions.py:78`
- `src/session_actions.py:79`
- `src/session_actions.py:201`
- `tests/test_search_ranking_recency.py:37`

## `recency_score` — function, line 20
- **called from:**
- `services/search/ranking.py:211`
- `tests/test_search_ranking_recency.py:16`
- `tests/test_search_ranking_recency.py:20`
- `tests/test_search_ranking_recency.py:24`
- `tests/test_search_ranking_recency.py:29`
- `tests/test_search_ranking_recency.py:30`
- `tests/test_search_ranking_recency.py:31`
- `tests/test_search_ranking_recency.py:47`
- `tests/test_search_ranking_recency.py:48`
- `tests/test_search_ranking_recency.py:49`

## `_domain` — function, line 88
- **called from:**
- `services/search/ranking.py:133`
- `services/search/ranking.py:148`
- `services/search/ranking.py:168`

## `_has_word` — function, line 95
- **called from:**
- `services/search/ranking.py:121`
- `services/search/ranking.py:128`
- `services/search/ranking.py:161`
- `services/search/ranking.py:161`
- `services/search/ranking.py:176`
- `services/search/ranking.py:194`
- `tests/test_search_ranking_subject_substring.py:30`
- `tests/test_search_ranking_subject_substring.py:31`
- `tests/test_search_ranking_subject_substring.py:32`
- `tests/test_search_ranking_subject_substring.py:36`
- `tests/test_search_ranking_subject_substring.py:37`

## `rank_search_results` — function, line 108
- **called from:**
- `services/search/core.py:880`
- `services/search/core.py:953`
- `services/search/core.py:1113`
- `tests/test_search_ranking.py:33`
- `tests/test_search_ranking.py:61`
- `tests/test_search_ranking.py:85`
- `tests/test_search_ranking_recency.py:71`
- `tests/test_search_ranking_sports_substring.py:48`
- `tests/test_search_ranking_subject_substring.py:54`
- `tests/test_search_ranking_subject_substring.py:84`

## `title_score` — function, line 117
- **called from:**
- `services/search/ranking.py:208`

## `snippet_score` — function, line 124
- **called from:**
- `services/search/ranking.py:209`

## `domain_score` — function, line 132
- **called from:**
- `services/search/ranking.py:210`

## `news_quality_adjustment` — function, line 144
- **called from:**
- `services/search/ranking.py:212`

## `software_release_adjustment` — function, line 165
- **called from:**
- `services/search/ranking.py:213`

## `product_spec_adjustment` — function, line 182
- **called from:**
- `services/search/ranking.py:214`
