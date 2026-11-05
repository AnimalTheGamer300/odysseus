# `src/model_profiles.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `model_id_leaf` — function, line 17
- **called from:**
- `src/ai_interaction.py:1210`
- `src/ai_interaction.py:1380`
- `src/clean_agent_preview.py:304`
- `src/clean_agent_preview.py:2668`
- `src/image_model_ids.py:32`
- `src/image_model_ids.py:60`
- `src/model_profiles.py:27`
- `src/model_profiles.py:52`

## `is_odysseus_tool_profile_model` — function, line 24
- **called from:**
- `src/model_profiles.py:33`
- `src/model_profiles.py:41`
- `src/model_profiles.py:47`

## `tool_schema_profile` — function, line 30
- **called from:**
- `routes/chat_routes.py:139`
- `src/agent_loop.py:8674`
- `src/agent_loop.py:8817`
- `tests/test_model_tool_modes.py:135`
- `tests/test_model_tool_modes.py:136`
- `tests/test_model_tool_modes.py:138`
- `tests/test_model_tool_modes.py:142`

## `is_odysseus_merged_tools_model` — function, line 38
- **called from:**
- `src/agent_loop.py:211`
- `src/agent_loop.py:236`
- `src/agent_loop.py:880`
- `src/agent_loop.py:14626`
- `src/agent_loop.py:22736`
- `src/agent_loop.py:22742`
- `src/clean_agent_preview.py:5646`
- `src/clean_agent_preview.py:6062`
- `src/llm_core.py:1256`

## `uses_odysseus_progressive_thinking` — function, line 44
- **called from:**
- `routes/chat_helpers.py:650`
- `src/clean_agent_preview.py:1445`
- `src/model_profiles.py:53`

## `supports_user_thinking_toggle` — function, line 50
- **called from:**
- `routes/chat_routes.py:2443`
- `routes/chat_routes.py:2986`
- `routes/chat_routes.py:3138`
- `routes/history/history_routes.py:1197`
- `routes/history/history_routes.py:1368`
- `tests/test_kimi_thinking_toggle.py:10`
- `tests/test_kimi_thinking_toggle.py:17`
