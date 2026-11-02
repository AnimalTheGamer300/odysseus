# `src/prompt_security.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_escape_guard_markers` — function, line 44
- **called from:**
- `src/prompt_security.py:70`
- `src/prompt_security.py:91`
- `tests/test_prompt_security.py:28`
- `tests/test_prompt_security.py:32`
- `tests/test_prompt_security.py:37`
- `tests/test_prompt_security.py:46`

## `_sanitize_label` — function, line 58
- **called from:**
- `src/prompt_security.py:89`
- `tests/test_prompt_security.py:54`
- `tests/test_prompt_security.py:61`
- `tests/test_prompt_security.py:68`
- `tests/test_prompt_security.py:74`
- `tests/test_prompt_security.py:80`
- `tests/test_prompt_security.py:86`

## `untrusted_context_message` — function, line 74
- **called from:**
- `routes/chat_helpers.py:868`
- `routes/chat_helpers.py:872`
- `routes/chat_routes.py:1012`
- `routes/chat_routes.py:3128`
- `routes/skills_routes.py:123`
- `routes/skills_routes.py:1641`
- `src/agent_loop.py:1234`
- `src/agent_loop.py:1777`
- `src/agent_loop.py:1884`
- `src/agent_loop.py:2112`
- `src/agent_loop.py:2871`
- `src/agent_loop.py:2954`
- `src/agent_loop.py:3019`
- `src/agent_loop.py:3153`
- `src/agent_loop.py:3168`
- `src/agent_loop.py:3202`
- `src/agent_loop.py:3644`
- `src/bg_monitor.py:36`
- `src/chat_processor.py:338`
- `src/chat_processor.py:355`
- `src/chat_processor.py:400`
- `src/chat_processor.py:465`
- `src/chat_processor.py:491`
- `src/chat_processor.py:510`
- `src/chat_processor.py:536`
- `src/deep_research.py:639`
- `tests/test_external_context_tool_gate.py:400`
- `tests/test_external_context_tool_gate.py:413`
- `tests/test_external_context_tool_gate.py:414`
- `tests/test_external_context_tool_gate.py:430`
- `tests/test_external_context_tool_gate.py:943`
- `tests/test_external_context_tool_gate.py:1014`
- `tests/test_external_context_tool_gate.py:1063`
- `tests/test_external_context_tool_gate.py:1110`
- `tests/test_external_context_tool_gate.py:1165`
- `tests/test_external_context_tool_gate.py:1224`
- `tests/test_external_context_tool_gate.py:1289`
- `tests/test_external_context_tool_gate.py:1343`
- `tests/test_prompt_security.py:96`
- `tests/test_prompt_security.py:108`
- `tests/test_prompt_security.py:123`
- `tests/test_prompt_security.py:135`
- `tests/test_prompt_security.py:145`
- `tests/test_prompt_security.py:156`
- `tests/test_prompt_security.py:168`
- `tests/test_prompt_security.py:176`
- `tests/test_prompt_security.py:181`
- `tests/test_prompt_security.py:190`
- `tests/test_prompt_security.py:198`
- `tests/test_security_regressions.py:28`
