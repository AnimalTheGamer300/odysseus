# `src/tool_policy.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `tool_toggle_enabled` — function, line 27
- **called from:**
- `src/tool_policy.py:36`
- `src/tool_policy.py:55`
- `src/tool_policy.py:55`

## `tool_toggle_explicitly_denied` — function, line 33
- **called from:**
- `src/tool_policy.py:42`

## `is_web_search_explicitly_denied` — function, line 39
- **called from:**
- `routes/chat_routes.py:3638`
- `src/tool_policy.py:53`
- `src/tool_policy.py:70`
- `tests/test_chat_route_tool_policy.py:494`

## `web_search_enabled_for_turn` — function, line 45
- **called from:**
- `routes/chat_routes.py:2742`
- `tests/test_chat_route_tool_policy.py:493`
- `tests/test_tool_policy.py:172`
- `tests/test_tool_policy.py:173`
- `tests/test_tool_policy.py:174`
- `tests/test_tool_policy.py:175`
- `tests/test_tool_policy.py:176`
- `tests/test_tool_policy.py:177`

## `web_intent_may_enable_for_turn` — function, line 58
- **called from:**
- `routes/chat_routes.py:3630`
- `tests/test_chat_route_tool_policy.py:584`
- `tests/test_chat_route_tool_policy.py:588`
- `tests/test_chat_route_tool_policy.py:589`

## `ToolPolicy` — class, line 166
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/editor_agent_routes.py:1680`
- `scripts/eval_followup_domain_continuity.py:103`
- `scripts/probe_browser_budget.py:31`
- `scripts/probe_browser_budget.py:65`
- `scripts/probe_empty_search_recovery.py:46`
- `scripts/probe_empty_search_recovery.py:54`
- `scripts/probe_fixed_search_evidence.py:51`
- `scripts/probe_fixed_search_evidence.py:66`
- `src/agent_loop.py:21418`
- `src/agent_runtime/authority.py:226`
- `src/tool_policy.py:255`
- `src/tool_policy.py:264`
- `tests/test_agent_rounds_exhausted.py:1669`
- `tests/test_ajax_email_live.py:43`
- `tests/test_ajax_email_live.py:114`
- `tests/test_ajax_email_live.py:194`
- `tests/test_api_token_tool_authority.py:330`
- `tests/test_api_token_tool_authority.py:336`
- `tests/test_browser_target_correction.py:41`
- `tests/test_browser_transport_recovery.py:96`
- `tests/test_buffered_terminal_answer.py:31`
- `tests/test_calendar_stream_links.py:58`
- `tests/test_clawmm_r47_malformed_write_body.py:71`
- `tests/test_clawmm_r47_malformed_write_body.py:80`
- `tests/test_clean_agent_preview.py:606`
- `tests/test_clean_agent_preview.py:611`
- `tests/test_clean_agent_preview.py:868`
- `tests/test_clean_agent_preview.py:873`
- `tests/test_clean_agent_preview.py:961`
- `tests/test_clean_agent_preview.py:966`
- `tests/test_clean_agent_preview.py:1050`
- `tests/test_clean_agent_preview.py:1055`
- `tests/test_clean_agent_preview.py:1198`
- `tests/test_clean_agent_preview.py:1203`
- `tests/test_clean_agent_preview.py:1277`
- `tests/test_clean_agent_preview.py:1282`
- `tests/test_clean_agent_preview.py:1363`
- `tests/test_clean_agent_preview.py:1368`
- `tests/test_clean_agent_preview.py:1649`
- `tests/test_clean_agent_preview.py:1672`
- `tests/test_clean_agent_preview.py:1687`
- `tests/test_clean_agent_preview.py:2194`
- `tests/test_clean_agent_preview.py:2199`
- `tests/test_clean_agent_preview.py:2306`
- `tests/test_clean_agent_preview.py:2311`
- `tests/test_clean_agent_preview.py:3608`
- `tests/test_clean_agent_preview.py:3705`
- `tests/test_clean_agent_preview.py:3720`
- `tests/test_clean_agent_preview.py:4144`
- `tests/test_clean_agent_preview.py:4151`
- `tests/test_clean_agent_preview.py:4182`
- `tests/test_clean_agent_preview.py:4195`
- `tests/test_clean_agent_preview.py:4205`
- `tests/test_clean_agent_preview.py:4283`
- `tests/test_clean_agent_preview.py:4293`
- `tests/test_clean_agent_preview.py:4476`
- `tests/test_clean_agent_preview.py:4487`
- `tests/test_clean_agent_preview.py:4499`
- `tests/test_clean_agent_preview.py:4521`
- `tests/test_clean_agent_preview.py:4541`
- … +245 more (grep the name in repo)

## `ToolPolicy.all_disabled_names` — method, line 176
- **called from:**
- `routes/chat_routes.py:3759`
- `src/agent_loop.py:21698`
- `src/agent_loop.py:21893`
- `src/agent_loop.py:21930`
- `src/agent_runtime/authority.py:228`
- `src/clean_agent_preview.py:5673`
- `src/turn_contract.py:6365`
- `src/turn_contract.py:6408`
- `tests/test_tool_policy.py:857`

## `ToolPolicy.blocks` — method, line 179
- **called from:**
- `routes/chat_routes.py:2484`
- `routes/chat_routes.py:2513`
- `routes/chat_routes.py:2514`
- `routes/chat_routes.py:4041`
- `routes/chat_routes.py:4042`
- `routes/chat_routes.py:4386`
- `src/agent_loop.py:616`
- `src/agent_loop.py:17714`
- `src/agent_loop.py:21493`
- `src/agent_loop.py:22067`
- `src/agent_loop.py:22151`
- `src/agent_loop.py:22255`
- `src/agent_loop.py:33890`
- `src/agent_tools/web_tools.py:420`
- `src/agent_tools/web_tools_prewave3.py:424`
- `src/tool_execution.py:1786`
- `src/tool_execution.py:2140`
- `src/turn_contract.py:6368`
- `src/turn_contract.py:6410`
- `tests/test_core_agent_tool_floor.py:31`
- `tests/test_product_turn_contract_route.py:97`
- `tests/test_product_turn_contract_route.py:110`
- `tests/test_tool_policy.py:160`
- `tests/test_tool_policy.py:168`
- `tests/test_tool_policy.py:169`
- `tests/test_turn_contract.py:1691`
- `static/js/documentLibrary.js:2209`
- `static/js/markdown.js:365`
- `static/js/markdown.js:671`
- `static/js/markdown.js:677`
- `static/js/streamingRenderer.js:134`
- `static/js/streamingRenderer.js:209`
- `static/js/tasks.js:2832`
- `static/js/tts-ai.js:72`

## `ToolPolicy.reason_for` — method, line 184
- **called from:**
- `routes/chat_routes.py:4389`
- `src/agent_loop.py:618`

## `detect_guide_only_turn` — function, line 192
- **called from:**
- `src/tool_policy.py:249`
- `tests/test_tool_policy.py:51`
- `tests/test_tool_policy.py:52`
- `tests/test_tool_policy.py:53`
- `tests/test_tool_policy.py:54`
- `tests/test_tool_policy.py:57`
- `tests/test_tool_policy.py:58`
- `tests/test_tool_policy.py:59`
- `tests/test_tool_policy.py:60`
- `tests/test_tool_policy.py:61`

## `known_tool_names` — function, line 204
- **called from:**
- `scripts/dump_agent_prompt.py:184`
- `src/agent_loop.py:21917`
- `src/agent_loop.py:21969`
- `src/agent_loop.py:23392`
- `src/agent_loop.py:24038`
- `src/agent_loop.py:24178`
- `src/tool_policy.py:251`
- `tests/runtime_evidence_helpers.py:29`
- `tests/test_client_tool_contract.py:23`
- `tests/test_pr6020_rebase_regressions.py:136`

## `build_effective_tool_policy` — function, line 233
- **called from:**
- `routes/chat_routes.py:2479`
- `routes/chat_routes.py:3257`
- `routes/chat_routes.py:3744`
- `routes/chat_routes.py:3842`
- `routes/chat_routes.py:3886`
- `routes/chat_routes.py:4037`
- `src/agent_runtime/authority.py:512`
- `tests/test_chat_image_routing.py:145`
- `tests/test_review_fixture_policy.py:39`
- `tests/test_review_fixture_policy.py:45`
- `tests/test_tool_policy.py:150`
- `tests/test_tool_policy.py:163`
- `tests/test_tool_policy.py:846`
- `tests/test_tool_policy.py:1462`
- `tests/test_tool_policy.py:1490`
- `tests/test_tool_policy.py:1519`
- `tests/test_tool_policy.py:1552`
- `tests/test_tool_policy.py:1575`
- `tests/test_tool_policy.py:1605`
- `tests/test_tool_policy.py:1629`
- `tests/test_tool_policy.py:1653`
- `tests/test_tool_policy.py:1724`
