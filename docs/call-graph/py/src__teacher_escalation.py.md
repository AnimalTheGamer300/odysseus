# `src/teacher_escalation.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `is_self_hosted` — function, line 49
- **called from:**
- `tests/test_kimi_code_hosts.py:26`
- `tests/test_kimi_code_hosts.py:29`
- `tests/test_kimi_code_hosts.py:32`
- `tests/test_venice_hosts.py:27`
- `tests/test_venice_hosts.py:30`
- `tests/test_venice_hosts.py:33`

## `evaluate_turn_regex` — function, line 102
- **called from:**
- `src/teacher_escalation.py:499`
- `src/teacher_escalation.py:585`
- `src/teacher_escalation.py:704`
- `tests/test_teacher_eval_nonstring_reply.py:8`
- `tests/test_teacher_eval_nonstring_reply.py:9`
- `tests/test_teacher_eval_nonstring_reply.py:13`

## `_call_teacher` — function (async), line 243
- **called from:**
- `src/teacher_escalation.py:722`
- `tests/test_teacher_audit_owner_scope.py:38`

## `_extract_skill_json` — function, line 342
- **called from:**
- `src/teacher_escalation.py:723`
- `src/teacher_escalation.py:732`
- `tests/test_extract_skill_json_nonstring.py:12`
- `tests/test_extract_skill_json_nonstring.py:13`
- `tests/test_extract_skill_json_nonstring.py:14`
- `tests/test_extract_skill_json_nonstring.py:19`

## `_format_trace` — function, line 364
- **called from:**
- `src/teacher_escalation.py:427`
- `src/teacher_escalation.py:720`

## `evaluate_turn_llm` — function (async), line 407
- **called from:**
- `src/teacher_escalation.py:513`
- `src/teacher_escalation.py:590`
- `tests/test_teacher_eval_tier2.py:25`
- `tests/test_teacher_eval_tier2.py:51`
- `tests/test_teacher_eval_tier2.py:74`
- `tests/test_teacher_eval_tier2.py:98`

## `escalate_and_learn` — function (async), line 452
- **called from:**
- `src/teacher_escalation.py:503`
- `src/teacher_escalation.py:521`
- `tests/test_teacher_eval_tier2.py:195`

## `maybe_escalate` — function, line 467
- **called from:**
- `tests/test_teacher_eval_tier2.py:133`
- `tests/test_teacher_eval_tier2.py:161`

## `evaluate_and_maybe_escalate` — function (async), line 512
- **called from:**
- `src/teacher_escalation.py:524`

## `run_teacher_inline` — function (async), line 531
- **called from:**
- `src/agent_loop.py:7075`
- `tests/test_teacher_eval_tier2.py:258`
- `tests/test_teacher_eval_tier2.py:358`
- `tests/test_teacher_eval_tier2.py:396`
