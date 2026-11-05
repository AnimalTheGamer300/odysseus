# `src/email_task_intent.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmailTaskIntent` — class, line 10
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/email_task_intent.py:114`
- `tests/test_editor_writing_action_routing.py:141`
- `tests/test_editor_writing_action_routing.py:211`
- `tests/test_email_scope_routing.py:75`
- `tests/test_email_search_recovery.py:68`
- `tests/test_preview_drafting_recovery.py:109`
- `tests/test_source_question_routing.py:40`
- `tests/test_source_question_routing.py:78`

## `email_composition_schemas` — function, line 58
- **called from:**
- `src/clean_agent_preview.py:5811`
- `tests/test_email_task_intent.py:32`

## `email_style_context` — function, line 83
- **called from:**
- `src/clean_agent_preview.py:5816`
- `tests/test_email_task_intent.py:10`
- `tests/test_email_task_intent.py:14`
- `tests/test_email_task_intent.py:15`

## `parse_email_task_intent` — function, line 94
- **called from:**
- `src/email_task_intent.py:319`
- `tests/test_email_task_intent.py:44`
- `tests/test_email_task_intent.py:52`
- `tests/test_email_task_intent.py:62`
- `tests/test_email_task_intent.py:73`
- `tests/test_email_task_intent.py:85`
- `tests/test_email_task_intent.py:92`

## `scope_email_tools` — function, line 118
- **called from:**
- `src/clean_agent_preview.py:6082`
- `tests/test_email_task_intent.py:47`
- `tests/test_email_task_intent.py:48`
- `tests/test_email_task_intent.py:54`
- `tests/test_email_task_intent.py:55`
- `tests/test_email_task_intent.py:68`
- `tests/test_email_task_intent.py:79`
- `tests/test_email_task_intent.py:86`
- `tests/test_source_question_routing.py:42`
- `tests/test_source_question_routing.py:43`

## `classify_email_task` — function (async), line 210
- **called from:**
- `src/clean_agent_preview.py:6065`
- `tests/test_ajax_email_live.py:67`
- `tests/test_email_task_intent.py:120`
- `tests/test_email_task_intent.py:142`
- `tests/test_email_task_intent.py:156`
- `tests/test_email_task_intent.py:174`
