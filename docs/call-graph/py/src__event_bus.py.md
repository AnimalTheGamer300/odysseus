# `src/event_bus.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_task_scheduler` — function, line 22
- **called from:**
- `app.py:786`

## `get_task_scheduler` — function, line 28
- **called from:**
- `src/tools/system.py:473`

## `fire_event` — function, line 33
- **called from:**
- `mcp_servers/email_server.py:1669`
- `mcp_servers/email_server.py:1711`
- `routes/chat_helpers.py:482`
- `routes/document/document_routes.py:207`
- `routes/email_routes.py:415`
- `routes/history/history_routes.py:912`
- `routes/memory/memory_routes.py:143`
- `routes/research/research_routes.py:750`
- `routes/session_routes.py:519`
- `routes/session_routes.py:1076`
- `routes/skills_routes.py:1202`
- `services/memory/memory_extractor.py:656`
- `services/memory/skill_extractor.py:290`
- `src/agent_tools/document_tools.py:465`
- `src/agent_tools/session_tools.py:64`
- `src/agent_tools/session_tools.py:455`
- `src/ai_interaction.py:411`
- `src/research_handler.py:635`
- `src/task_scheduler.py:2132`
- `src/tools/system.py:149`

## `_resolve_event_owner` — function, line 46
- **called from:**
- `src/event_bus.py:76`

## `_handle_event` — function (async), line 72
- **called from:**
- `src/event_bus.py:40`
- `src/event_bus.py:43`
