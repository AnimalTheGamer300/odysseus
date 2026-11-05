# `src/task_endpoint.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `resolve_task_endpoint` — function, line 12
- **called from:**
- `routes/chat_helpers.py:714`
- `routes/chat_helpers.py:2099`
- `routes/chat_helpers.py:2119`
- `routes/chat_helpers.py:2162`
- `routes/document/document_routes.py:1200`
- `routes/memory/memory_routes.py:260`
- `routes/memory/memory_routes.py:312`
- `routes/memory/memory_routes.py:374`
- `routes/memory/memory_routes.py:378`
- `routes/session_routes.py:394`
- `routes/session_routes.py:1564`
- `src/session_actions.py:123`
- `src/task_endpoint.py:67`

## `resolve_task_candidates` — function, line 22
- **called from:**
- `routes/email/email_pollers.py:774`
- `routes/session_routes.py:1590`
- `src/builtin_actions.py:693`
- `src/builtin_actions.py:1541`
- `src/builtin_actions.py:1848`
- `src/builtin_actions.py:2145`
- `src/builtin_actions.py:2645`
- `src/task_endpoint.py:100`
- `src/task_scheduler.py:2065`
- `tests/test_review_endpoint_credentials.py:33`
- `tests/test_review_endpoint_credentials.py:76`

## `_append` — function, line 41
- **called from:**
- `src/agent_evidence.py:842`
- `src/agent_evidence.py:872`
- `src/agent_evidence.py:894`
- `src/agent_evidence.py:911`
- `src/agent_evidence.py:922`
- `src/agent_evidence.py:986`
- `src/agent_runtime/effect_log.py:345`
- `src/agent_runtime/effect_log.py:350`
- `src/agent_runtime/effect_log.py:353`
- `src/agent_runtime/effect_log.py:509`
- `src/task_endpoint.py:60`
- `src/task_endpoint.py:67`
- `src/task_endpoint.py:68`
- `src/task_endpoint.py:69`
- `src/task_endpoint.py:71`

## `task_llm_call_async` — function (async), line 75
- **called from:**
- `routes/document/document_routes.py:1238`
- `routes/email/email_helpers.py:482`
- `routes/email/email_pollers.py:1026`
- `routes/email/email_pollers.py:1071`
- `routes/email/email_pollers.py:1331`
- `routes/email/email_pollers.py:1459`
- `src/builtin_actions.py:1291`
- `src/session_actions.py:141`
- `src/task_scheduler.py:1811`
- `src/task_scheduler.py:2169`
- `tests/test_utility_reasoning_effort.py:62`
