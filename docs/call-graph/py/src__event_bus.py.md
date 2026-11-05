# `src/event_bus.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_event_automation_enabled_for_owner` — function, line 22
- **called from:**
- `src/event_bus.py:87`
- `tests/test_event_bus_fixture_isolation.py:7`
- `tests/test_event_bus_fixture_isolation.py:8`
- `tests/test_event_bus_fixture_isolation.py:9`
- `tests/test_event_bus_fixture_isolation.py:10`

## `set_task_scheduler` — function, line 27
- **called from:**
- `app.py:870`

## `get_task_scheduler` — function, line 33
- **called from:**
- `src/tools/system.py:686`

## `fire_event` — function, line 38
- **called from:**
- `mcp_servers/email_server.py:2868`
- `mcp_servers/email_server.py:2915`
- `routes/chat_helpers.py:964`
- `routes/document/document_routes.py:212`
- `routes/email/email_routes.py:459`
- `routes/history/history_routes.py:1150`
- `routes/memory/memory_routes.py:143`
- `routes/research/research_routes.py:862`
- `routes/session_routes.py:684`
- `routes/session_routes.py:1290`
- `routes/skills_routes.py:311`
- `services/memory/memory_extractor.py:860`
- `services/memory/skill_extractor.py:286`
- `src/agent_tools/document_tools.py:615`
- `src/agent_tools/session_tools.py:78`
- `src/agent_tools/session_tools.py:478`
- `src/ai_interaction.py:460`
- `src/research_handler.py:789`
- `src/task_scheduler.py:2326`
- `src/tools/system.py:145`

## `_resolve_event_owner` — function, line 56
- **called from:**
- `src/event_bus.py:86`

## `_handle_event` — function (async), line 82
- **called from:**
- `src/event_bus.py:50`
- `src/event_bus.py:53`
- `tests/test_event_bus_fixture_isolation.py:20`
