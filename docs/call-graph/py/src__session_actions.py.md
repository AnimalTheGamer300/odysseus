# `src/session_actions.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow_naive` — function, line 19
- **called from:**
- `services/search/ranking.py:39`
- `src/session_actions.py:34`
- `src/session_actions.py:74`
- `src/session_actions.py:78`
- `src/session_actions.py:79`
- `src/session_actions.py:201`
- `tests/test_search_ranking_recency.py:37`

## `_as_naive_utc` — function, line 24
- **called from:**
- `src/session_actions.py:34`
- `src/session_actions.py:36`
- `src/session_actions.py:78`

## `is_session_recently_active` — function, line 32
- **called from:**
- `routes/session_routes.py:1487`
- `src/session_actions.py:84`

## `run_auto_sort` — function (async), line 46
- **called from:**
- `src/builtin_actions.py:565`
- `tests/test_chat_tidy_content_preservation.py:43`
- `tests/test_chat_tidy_content_preservation.py:140`
- `tests/test_session_actions_cleanup.py:85`
- `tests/test_session_actions_cleanup.py:120`
- `tests/test_session_actions_cleanup.py:159`
