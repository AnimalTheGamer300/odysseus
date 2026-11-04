# `services/search/ranking.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow_naive` — function, line 14
- **called from:**
- `services/search/ranking.py:39`
- `src/session_actions.py:44`
- `src/session_actions.py:83`
- `src/session_actions.py:87`
- `src/session_actions.py:88`
- `src/session_actions.py:242`
- `tests/test_search_ranking_recency.py:37`

## `recency_score` — function, line 20
- **called from:**
- `services/search/ranking.py:158`
- `tests/test_search_ranking_recency.py:16`
- `tests/test_search_ranking_recency.py:20`
- `tests/test_search_ranking_recency.py:24`
- `tests/test_search_ranking_recency.py:29`
- `tests/test_search_ranking_recency.py:30`
- `tests/test_search_ranking_recency.py:31`
- `tests/test_search_ranking_recency.py:47`
- `tests/test_search_ranking_recency.py:48`
- `tests/test_search_ranking_recency.py:49`

## `_domain` — function, line 72
- **called from:**
- `services/search/ranking.py:115`
- `services/search/ranking.py:130`

## `_has_word` — function, line 79
- **called from:**
- `services/search/ranking.py:103`
- `services/search/ranking.py:110`
- `services/search/ranking.py:143`
- `services/search/ranking.py:143`
- `tests/test_search_ranking_subject_substring.py:30`
- `tests/test_search_ranking_subject_substring.py:31`
- `tests/test_search_ranking_subject_substring.py:32`
- `tests/test_search_ranking_subject_substring.py:36`
- `tests/test_search_ranking_subject_substring.py:37`

## `rank_search_results` — function, line 92
- **called from:**
- `services/search/core.py:196`
- `services/search/core.py:318`
- `tests/test_search_ranking.py:33`
- `tests/test_search_ranking_recency.py:71`
- `tests/test_search_ranking_sports_substring.py:48`
- `tests/test_search_ranking_subject_substring.py:54`
- `tests/test_search_ranking_subject_substring.py:84`

## `title_score` — function, line 99
- **called from:**
- `services/search/ranking.py:155`

## `snippet_score` — function, line 106
- **called from:**
- `services/search/ranking.py:156`

## `domain_score` — function, line 114
- **called from:**
- `services/search/ranking.py:157`

## `news_quality_adjustment` — function, line 126
- **called from:**
- `services/search/ranking.py:159`
