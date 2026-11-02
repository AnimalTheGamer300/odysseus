# `src/tools/system.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_skills` — function (async), line 24
- **called from:**
- `src/tool_execution.py:1221`
- `tests/test_manage_skills_action_required.py:19`

## `_skill_dump` — function, line 246
- **called from:**
- `src/tools/system.py:177`
- `src/tools/system.py:201`

## `do_manage_tasks` — function (async), line 274
- **called from:**
- `src/tool_execution.py:1218`
- `tests/test_manage_tasks_owner_scope.py:67`
- `tests/test_manage_tasks_owner_scope.py:78`
- `tests/test_manage_tasks_owner_scope.py:89`
- `tests/test_manage_tasks_owner_scope.py:100`
- `tests/test_manage_tasks_owner_scope.py:110`
- `tests/test_manage_tasks_owner_scope.py:121`
- `tests/test_manage_tasks_owner_scope.py:134`

## `do_api_call` — function (async), line 496
- **called from:**
- `src/tool_execution.py:1225`

## `do_app_api` — function (async), line 588
- **called from:**
- `src/tool_execution.py:1266`
- `tests/test_review_regressions.py:530`
- `tests/test_review_regressions.py:577`
- `tests/test_review_regressions.py:604`
- `tests/test_review_regressions.py:652`
- `tests/test_review_regressions.py:696`
