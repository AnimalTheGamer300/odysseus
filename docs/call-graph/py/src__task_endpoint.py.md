# `src/task_endpoint.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `resolve_task_endpoint` — function, line 11
- **called from:**
- `routes/chat_helpers.py:318`
- `routes/chat_helpers.py:1425`
- `routes/chat_helpers.py:1463`
- `routes/document/document_routes.py:976`
- `routes/memory/memory_routes.py:260`
- `routes/memory/memory_routes.py:309`
- `routes/memory/memory_routes.py:370`
- `routes/memory/memory_routes.py:374`
- `routes/session_routes.py:258`
- `routes/session_routes.py:1366`
- `src/session_actions.py:166`
- `src/task_endpoint.py:45`

## `resolve_task_candidates` — function, line 21
- **called from:**
- `routes/email_pollers.py:638`
- `src/builtin_actions.py:569`
- `src/builtin_actions.py:1378`
- `src/builtin_actions.py:1673`
- `src/builtin_actions.py:1934`
- `src/builtin_actions.py:2303`
- `src/task_endpoint.py:63`
- `src/task_scheduler.py:1901`

## `_append` — function, line 37
- **called from:**
- `src/task_endpoint.py:45`
- `src/task_endpoint.py:46`
- `src/task_endpoint.py:47`
- `src/task_endpoint.py:49`

## `task_llm_call_async` — function (async), line 53
- **called from:**
- `routes/email_helpers.py:353`
- `routes/email_pollers.py:843`
- `routes/email_pollers.py:887`
- `routes/email_pollers.py:1133`
- `routes/email_pollers.py:1261`
- `src/builtin_actions.py:1145`
- `src/task_scheduler.py:1649`
- `src/task_scheduler.py:1986`
