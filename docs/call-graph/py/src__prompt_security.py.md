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
- `routes/chat_helpers.py:1438`
- `routes/chat_helpers.py:1451`
- `routes/chat_helpers.py:1459`
- `routes/chat_routes.py:113`
- `routes/chat_routes.py:2522`
- `routes/chat_routes.py:5603`
- `services/skills/job_coordinator.py:85`
- `services/skills/prompts.py:36`
- `src/agent_loop.py:4497`
- `src/agent_loop.py:4520`
- `src/agent_loop.py:4556`
- `src/agent_loop.py:8963`
- `src/agent_loop.py:11717`
- `src/agent_loop.py:11872`
- `src/agent_loop.py:13563`
- `src/agent_loop.py:15030`
- `src/agent_loop.py:15113`
- `src/agent_loop.py:15183`
- `src/agent_loop.py:15388`
- `src/agent_loop.py:15403`
- `src/agent_loop.py:15442`
- `src/agent_loop.py:16489`
- `src/agent_loop.py:16529`
- `src/agent_loop.py:20322`
- `src/agent_loop.py:20345`
- `src/agent_loop.py:20682`
- `src/background_tool_jobs.py:25`
- `src/bg_monitor.py:43`
- `src/chat_processor.py:334`
- `src/chat_processor.py:356`
- `src/chat_processor.py:373`
- `src/chat_processor.py:418`
- `src/chat_processor.py:483`
- `src/chat_processor.py:509`
- `src/chat_processor.py:539`
- `src/chat_processor.py:565`
- `src/clean_agent_preview.py:4133`
- `src/clean_agent_preview.py:4316`
- `src/clean_agent_preview.py:4368`
- `src/clean_agent_preview.py:8740`
- `src/deep_research.py:1346`
- `src/email_task_intent.py:91`
- `tests/test_compact_memory_context.py:8`
- `tests/test_compact_memory_context.py:28`
- `tests/test_email_task_intent.py:104`
- `tests/test_external_context_tool_gate.py:485`
- `tests/test_external_context_tool_gate.py:498`
- `tests/test_external_context_tool_gate.py:499`
- `tests/test_external_context_tool_gate.py:515`
- `tests/test_external_context_tool_gate.py:1040`
- `tests/test_external_context_tool_gate.py:1113`
- `tests/test_external_context_tool_gate.py:1164`
- `tests/test_external_context_tool_gate.py:1211`
- `tests/test_external_context_tool_gate.py:1266`
- `tests/test_external_context_tool_gate.py:1325`
- `tests/test_external_context_tool_gate.py:1390`
- `tests/test_external_context_tool_gate.py:1444`
- `tests/test_minimal_native_tool_prompt.py:421`
- `tests/test_prompt_security.py:96`
- `tests/test_prompt_security.py:108`
- … +10 more (grep the name in repo)
