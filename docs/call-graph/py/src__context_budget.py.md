# `src/context_budget.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_int_or_zero` — function, line 21
- **called from:**
- `src/context_budget.py:58`
- `src/context_budget.py:59`
- `src/context_budget.py:79`
- `src/context_budget.py:80`
- `src/context_budget.py:97`
- `src/context_budget.py:98`

## `compute_input_token_budget` — function, line 28
- **called from:**
- `src/agent_loop.py:24635`
- `tests/test_budget_auto_sentinel.py:53`
- `tests/test_budget_auto_sentinel.py:57`
- `tests/test_budget_auto_sentinel.py:63`
- `tests/test_budget_auto_sentinel.py:67`
- `tests/test_budget_auto_sentinel.py:68`
- `tests/test_budget_auto_sentinel.py:111`
- `tests/test_context_budget.py:40`
- `tests/test_context_budget.py:44`
- `tests/test_context_budget.py:49`
- `tests/test_context_budget.py:51`
- `tests/test_context_budget.py:55`
- `tests/test_context_budget.py:59`
- `tests/test_context_budget.py:60`
- `tests/test_context_budget.py:64`
- `tests/test_context_budget.py:65`
- `tests/test_context_budget.py:92`
- `tests/test_context_budget.py:94`
- `tests/test_context_budget.py:100`
- `tests/test_context_budget.py:102`
- `tests/test_context_budget.py:108`

## `bound_trim_reserve` — function, line 71
- **called from:**
- `src/context_budget.py:100`
- `tests/test_context_budget.py:17`
- `tests/test_context_budget.py:18`
- `tests/test_context_budget.py:19`

## `compute_trim_context_window` — function, line 84
- **called from:**
- `src/agent_loop.py:24654`
- `tests/test_context_budget.py:23`
- `tests/test_context_budget.py:31`

## `budget_is_explicit` — function, line 107
- **called from:**
- `tests/test_budget_auto_sentinel.py:51`
- `tests/test_budget_auto_sentinel.py:53`
