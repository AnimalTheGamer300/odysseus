# `src/web_recovery.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `WebRecoveryBudget` — class, line 7
- decorator: `dataclass`
- **called from:**
- `src/agent_loop.py:25434`
- `tests/test_web_recovery_budget.py:5`
- `tests/test_web_recovery_budget.py:21`

## `WebRecoveryBudget.admit` — method, line 12
- **called from:**
- `src/agent_loop.py:34261`
- `tests/test_web_recovery_budget.py:6`
- `tests/test_web_recovery_budget.py:7`
- `tests/test_web_recovery_budget.py:8`
- `tests/test_web_recovery_budget.py:9`
- `tests/test_web_recovery_budget.py:10`
- `tests/test_web_recovery_budget.py:11`
- `tests/test_web_recovery_budget.py:12`
- `tests/test_web_recovery_budget.py:13`
- `tests/test_web_recovery_budget.py:14`
- `tests/test_web_recovery_budget.py:15`
- `tests/test_web_recovery_budget.py:16`
- `tests/test_web_recovery_budget.py:22`

## `WebRecoveryBudget.instruction` — method, line 30
- **called from:**
- `src/agent_loop.py:31897`
- `src/agent_loop.py:34269`
- `src/agent_loop.py:34642`
- `tests/test_web_recovery_budget.py:17`
