# `src/context_budget.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_int_or_zero` — function, line 21
- **called from:**
- `src/context_budget.py:58`
- `src/context_budget.py:59`

## `compute_input_token_budget` — function, line 28
- **called from:**
- `src/agent_loop.py:4744`
- `tests/test_budget_auto_sentinel.py:53`
- `tests/test_budget_auto_sentinel.py:57`
- `tests/test_budget_auto_sentinel.py:63`
- `tests/test_budget_auto_sentinel.py:67`
- `tests/test_budget_auto_sentinel.py:68`
- `tests/test_budget_auto_sentinel.py:111`
- `tests/test_context_budget.py:13`
- `tests/test_context_budget.py:17`
- `tests/test_context_budget.py:22`
- `tests/test_context_budget.py:24`
- `tests/test_context_budget.py:28`
- `tests/test_context_budget.py:32`
- `tests/test_context_budget.py:33`
- `tests/test_context_budget.py:37`
- `tests/test_context_budget.py:38`
- `tests/test_context_budget.py:65`
- `tests/test_context_budget.py:67`
- `tests/test_context_budget.py:73`
- `tests/test_context_budget.py:75`
- `tests/test_context_budget.py:81`

## `budget_is_explicit` — function, line 71
- **called from:**
- `tests/test_budget_auto_sentinel.py:51`
- `tests/test_budget_auto_sentinel.py:53`
