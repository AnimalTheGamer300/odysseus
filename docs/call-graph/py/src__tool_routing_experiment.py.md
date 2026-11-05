# `src/tool_routing_experiment.py` — definitions & call sites

4 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `has_research_hint` — function, line 28
- **called from:**
- `src/tool_routing_experiment.py:71`

## `experiment_mode` — function, line 37
- **called from:**
- `routes/chat_routes.py:4008`
- `tests/test_tool_routing_experiment.py:66`
- `tests/test_tool_routing_experiment.py:67`
- `tests/test_tool_routing_experiment.py:70`
- `tests/test_tool_routing_experiment.py:71`
- `tests/test_tool_routing_experiment.py:72`
- `tests/test_tool_routing_experiment.py:73`
- `tests/test_tool_routing_experiment.py:331`
- `tests/test_tool_routing_experiment.py:332`
- `tests/test_tool_routing_experiment.py:342`
- `tests/test_tool_routing_experiment.py:343`
- `tests/test_tool_routing_experiment.py:364`
- `tests/test_tool_routing_experiment.py:391`
- `tests/test_tool_routing_experiment.py:392`

## `select_experiment_inventory` — function, line 56
- **called from:**
- `routes/chat_routes.py:4013`
- `scripts/eval_followup_domain_continuity.py:111`
- `tests/test_research_chat_runtime.py:17`
- `tests/test_result_reference_followup.py:43`
- `tests/test_result_reference_followup.py:115`
- `tests/test_tool_routing_experiment.py:18`
- `tests/test_tool_routing_experiment.py:47`
- `tests/test_tool_routing_experiment.py:92`
- `tests/test_tool_routing_experiment.py:98`
- `tests/test_tool_routing_experiment.py:117`
- `tests/test_tool_routing_experiment.py:129`
- `tests/test_tool_routing_experiment.py:147`
- `tests/test_tool_routing_experiment.py:166`
- `tests/test_tool_routing_experiment.py:188`
- `tests/test_tool_routing_experiment.py:209`
- `tests/test_tool_routing_experiment.py:228`
- `tests/test_tool_routing_experiment.py:258`
- `tests/test_tool_routing_experiment.py:273`
- `tests/test_tool_routing_experiment.py:281`
- `tests/test_tool_routing_experiment.py:302`
- `tests/test_tool_routing_experiment.py:340`
- `tests/test_tool_routing_experiment.py:344`
- `tests/test_tool_routing_experiment.py:374`
- `tests/test_tool_routing_experiment.py:387`
- `tests/test_tool_routing_experiment.py:390`
- `tests/test_tool_routing_experiment.py:402`
- `tests/test_tool_routing_experiment.py:405`
- `tests/test_tool_routing_experiment.py:417`
- `tests/test_tool_routing_experiment.py:423`
- `tests/test_tool_routing_experiment.py:426`
- `tests/test_tool_routing_experiment.py:428`
- `tests/test_tool_routing_experiment.py:429`
- `tests/test_tool_routing_experiment.py:461`

## `model_choice_private_tools` — function, line 205
- **called from:**
- `src/clean_agent_preview.py:5787`
- `tests/test_tool_routing_experiment.py:303`
- `tests/test_tool_routing_experiment.py:306`
- `tests/test_tool_routing_experiment.py:307`
