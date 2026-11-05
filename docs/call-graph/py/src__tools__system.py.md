# `src/tools/system.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `do_manage_skills` — function (async), line 24
- **called from:**
- `src/tool_execution.py:2403`
- `tests/test_builtin_skills.py:132`
- `tests/test_manage_skills_action_required.py:19`
- `tests/test_manage_skills_action_required.py:30`
- `tests/test_manage_skills_action_required.py:36`
- `tests/test_skill_tool_followup_contract.py:12`

## `_skill_dump` — function, line 255
- **called from:**
- `src/tools/system.py:183`
- `src/tools/system.py:209`

## `_task_date_utc` — function, line 283
- **called from:**
- `src/tools/system.py:497`
- `src/tools/system.py:617`

## `_task_structured_schedule` — function, line 296
- **called from:**
- `src/tools/system.py:477`
- `src/tools/system.py:565`

## `_admin_task_action_denied` — function, line 328
- **called from:**
- `src/tools/system.py:485`
- `src/tools/system.py:555`
- `src/tools/system.py:658`
- `src/tools/system.py:681`
- `tests/test_manage_tasks_admin_action_policy.py:229`
- `tests/test_manage_tasks_admin_action_policy.py:230`
- `tests/test_manage_tasks_admin_action_policy.py:231`
- `tests/test_manage_tasks_admin_action_policy.py:232`

## `do_manage_tasks` — function (async), line 348
- **called from:**
- `src/tool_execution.py:2400`
- `tests/test_manage_tasks_admin_action_policy.py:95`
- `tests/test_manage_tasks_admin_action_policy.py:106`
- `tests/test_manage_tasks_admin_action_policy.py:116`
- `tests/test_manage_tasks_admin_action_policy.py:125`
- `tests/test_manage_tasks_admin_action_policy.py:135`
- `tests/test_manage_tasks_admin_action_policy.py:148`
- `tests/test_manage_tasks_admin_action_policy.py:160`
- `tests/test_manage_tasks_admin_action_policy.py:170`
- `tests/test_manage_tasks_admin_action_policy.py:181`
- `tests/test_manage_tasks_admin_action_policy.py:200`
- `tests/test_manage_tasks_admin_action_policy.py:219`
- `tests/test_manage_tasks_admin_action_policy.py:247`
- `tests/test_manage_tasks_admin_action_policy.py:257`
- `tests/test_manage_tasks_cron.py:24`
- `tests/test_manage_tasks_owner_scope.py:76`
- `tests/test_manage_tasks_owner_scope.py:87`
- `tests/test_manage_tasks_owner_scope.py:98`
- `tests/test_manage_tasks_owner_scope.py:109`
- `tests/test_manage_tasks_owner_scope.py:119`
- `tests/test_manage_tasks_owner_scope.py:130`
- `tests/test_manage_tasks_owner_scope.py:143`
- `tests/test_manage_tasks_owner_scope.py:155`
- `tests/test_manage_tasks_owner_scope.py:170`
- `tests/test_manage_tasks_owner_scope.py:188`
- `tests/test_manage_tasks_owner_scope.py:207`
- `tests/test_manage_tasks_owner_scope.py:226`
- `tests/test_manage_tasks_owner_scope.py:242`
- `tests/test_manage_tasks_owner_scope.py:257`
- `tests/test_manage_tasks_owner_scope.py:263`
- `tests/test_manage_tasks_owner_scope.py:270`
- `tests/test_manage_tasks_owner_scope.py:274`
- `tests/test_manage_tasks_owner_scope.py:287`
- `tests/test_manage_tasks_owner_scope.py:302`
- `tests/test_manage_tasks_owner_scope.py:306`
- `tests/test_manage_tasks_owner_scope.py:320`
- `tests/tools/organizer_smoke.py:124`
- `tests/tools/organizer_smoke.py:130`
- `tests/tools/organizer_smoke.py:136`
- `tests/tools/organizer_smoke.py:150`
- `tests/tools/organizer_smoke.py:240`

## `_task_by_id_or_exact_name` — function, line 385
- **called from:**
- `src/tools/system.py:541`
- `src/tools/system.py:638`
- `src/tools/system.py:649`
- `src/tools/system.py:676`

## `do_api_call` — function (async), line 709
- **called from:**
- `src/tool_execution.py:2407`

## `do_app_api` — function (async), line 810
- **called from:**
- `src/agent_tools/model_interaction_tools.py:146`
- `src/tool_execution.py:2448`
- `tests/test_manage_settings_denylist_hard.py:115`
- `tests/test_manage_settings_denylist_hard.py:180`
- `tests/test_review_regressions.py:724`
- `tests/test_review_regressions.py:771`
- `tests/test_review_regressions.py:798`
- `tests/test_review_regressions.py:846`
- `tests/test_review_regressions.py:890`
