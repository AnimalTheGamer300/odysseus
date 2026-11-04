# `src/session_actions.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow_naive` — function, line 29
- **called from:**
- `services/search/ranking.py:39`
- `src/session_actions.py:44`
- `src/session_actions.py:83`
- `src/session_actions.py:87`
- `src/session_actions.py:88`
- `src/session_actions.py:242`
- `tests/test_search_ranking_recency.py:37`

## `_as_naive_utc` — function, line 34
- **called from:**
- `src/session_actions.py:44`
- `src/session_actions.py:46`
- `src/session_actions.py:87`

## `is_session_recently_active` — function, line 42
- **called from:**
- `routes/session_routes.py:1337`
- `src/session_actions.py:93`

## `run_auto_sort` — function (async), line 56
- **called from:**
- `src/builtin_actions.py:441`
- `tests/test_session_actions_cleanup.py:85`
- `tests/test_session_actions_cleanup.py:120`
- `tests/test_session_actions_cleanup.py:159`
