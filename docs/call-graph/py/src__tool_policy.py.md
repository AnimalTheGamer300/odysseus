# `src/tool_policy.py` — definitions & call sites

11 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `tool_toggle_enabled` — function, line 22
- **called from:**
- `src/tool_policy.py:31`
- `src/tool_policy.py:50`
- `src/tool_policy.py:50`

## `tool_toggle_explicitly_denied` — function, line 28
- **called from:**
- `src/tool_policy.py:37`

## `is_web_search_explicitly_denied` — function, line 34
- **called from:**
- `routes/chat_routes.py:1690`
- `src/tool_policy.py:48`
- `tests/test_chat_route_tool_policy.py:152`

## `web_search_enabled_for_turn` — function, line 40
- **called from:**
- `routes/chat_routes.py:1200`
- `tests/test_chat_route_tool_policy.py:151`
- `tests/test_tool_policy.py:85`
- `tests/test_tool_policy.py:86`
- `tests/test_tool_policy.py:87`
- `tests/test_tool_policy.py:88`
- `tests/test_tool_policy.py:89`
- `tests/test_tool_policy.py:90`

## `ToolPolicy` — class, line 141
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/tool_policy.py:230`
- `src/tool_policy.py:239`
- `tests/test_review_regressions.py:785`

## `ToolPolicy.all_disabled_names` — method, line 151
- **called from:**
- `routes/chat_routes.py:1797`
- `src/agent_loop.py:4069`
- `tests/test_tool_policy.py:180`

## `ToolPolicy.blocks` — method, line 154
- **called from:**
- `routes/chat_routes.py:977`
- `routes/chat_routes.py:1003`
- `routes/chat_routes.py:1004`
- `routes/chat_routes.py:1799`
- `routes/chat_routes.py:1800`
- `routes/chat_routes.py:2110`
- `src/agent_loop.py:6226`
- `src/agent_loop.py:6237`
- `src/tool_execution.py:1082`
- `tests/test_tool_policy.py:71`
- `tests/test_tool_policy.py:80`
- `tests/test_tool_policy.py:81`
- `static/js/documentLibrary.js:1988`
- `static/js/markdown.js:181`
- `static/js/markdown.js:535`
- `static/js/markdown.js:541`
- `static/js/streamingRenderer.js:105`
- `static/js/streamingRenderer.js:145`
- `static/js/tasks.js:2696`
- `static/js/tts-ai.js:72`

## `ToolPolicy.reason_for` — method, line 159
- **called from:**
- `routes/chat_routes.py:2111`
- `src/agent_loop.py:6239`

## `detect_guide_only_turn` — function, line 167
- **called from:**
- `src/tool_policy.py:224`
- `tests/test_tool_policy.py:46`
- `tests/test_tool_policy.py:47`
- `tests/test_tool_policy.py:48`
- `tests/test_tool_policy.py:49`
- `tests/test_tool_policy.py:53`
- `tests/test_tool_policy.py:54`
- `tests/test_tool_policy.py:55`
- `tests/test_tool_policy.py:56`
- `tests/test_tool_policy.py:57`

## `known_tool_names` — function, line 179
- **called from:**
- `scripts/dump_agent_prompt.py:184`
- `src/agent_loop.py:4560`
- `src/agent_loop.py:4663`
- `src/tool_policy.py:226`
- `tests/test_pr6020_rebase_regressions.py:118`

## `build_effective_tool_policy` — function, line 208
- **called from:**
- `routes/chat_routes.py:972`
- `routes/chat_routes.py:1540`
- `routes/chat_routes.py:1793`
- `tests/test_tool_policy.py:61`
- `tests/test_tool_policy.py:75`
- `tests/test_tool_policy.py:169`
- `tests/test_tool_policy.py:195`
- `tests/test_tool_policy.py:224`
- `tests/test_tool_policy.py:254`
- `tests/test_tool_policy.py:288`
- `tests/test_tool_policy.py:312`
- `tests/test_tool_policy.py:343`
- `tests/test_tool_policy.py:368`
- `tests/test_tool_policy.py:393`
- `tests/test_tool_policy.py:466`
