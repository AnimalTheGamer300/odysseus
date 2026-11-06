# `src/teacher_escalation.py` — definitions & call sites

13 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `request_teacher_takeover` — function, line 42
- **called from:**
- `src/agent_loop.py:38926`
- `tests/test_nested_invocation_ownership.py:273`
- `tests/test_nested_invocation_ownership.py:383`

## `with_teacher_takeover` — function, line 51
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `wrapped` — function (async), line 54
- decorator: `wraps(func)`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `is_self_hosted` — function, line 105
- **called from:**
- `tests/test_kimi_code_hosts.py:26`
- `tests/test_kimi_code_hosts.py:29`
- `tests/test_kimi_code_hosts.py:32`
- `tests/test_venice_hosts.py:27`
- `tests/test_venice_hosts.py:30`
- `tests/test_venice_hosts.py:33`

## `evaluate_turn_regex` — function, line 158
- **called from:**
- `src/teacher_escalation.py:555`
- `src/teacher_escalation.py:646`
- `src/teacher_escalation.py:778`
- `tests/test_teacher_eval_nonstring_reply.py:8`
- `tests/test_teacher_eval_nonstring_reply.py:9`
- `tests/test_teacher_eval_nonstring_reply.py:13`

## `_call_teacher` — function (async), line 299
- **called from:**
- `src/teacher_escalation.py:796`
- `tests/test_teacher_audit_owner_scope.py:38`

## `_extract_skill_json` — function, line 398
- **called from:**
- `src/teacher_escalation.py:797`
- `src/teacher_escalation.py:806`
- `tests/test_extract_skill_json_nonstring.py:12`
- `tests/test_extract_skill_json_nonstring.py:13`
- `tests/test_extract_skill_json_nonstring.py:14`
- `tests/test_extract_skill_json_nonstring.py:19`

## `_format_trace` — function, line 420
- **called from:**
- `src/teacher_escalation.py:483`
- `src/teacher_escalation.py:794`

## `evaluate_turn_llm` — function (async), line 463
- **called from:**
- `src/teacher_escalation.py:569`
- `src/teacher_escalation.py:651`
- `tests/test_teacher_eval_tier2.py:31`
- `tests/test_teacher_eval_tier2.py:57`
- `tests/test_teacher_eval_tier2.py:80`
- `tests/test_teacher_eval_tier2.py:104`

## `escalate_and_learn` — function (async), line 508
- **called from:**
- `src/teacher_escalation.py:559`
- `src/teacher_escalation.py:577`
- `tests/test_teacher_eval_tier2.py:201`

## `maybe_escalate` — function, line 523
- **called from:**
- `tests/test_teacher_eval_tier2.py:139`
- `tests/test_teacher_eval_tier2.py:167`

## `evaluate_and_maybe_escalate` — function (async), line 568
- **called from:**
- `src/teacher_escalation.py:580`

## `run_teacher_inline` — function (async), line 587
- **called from:**
- `src/teacher_escalation.py:71`
- `tests/test_nested_invocation_ownership.py:334`
- `tests/test_nested_invocation_ownership.py:359`
- `tests/test_request_authority.py:332`
- `tests/test_teacher_eval_tier2.py:264`
- `tests/test_teacher_eval_tier2.py:364`
- `tests/test_teacher_eval_tier2.py:402`
