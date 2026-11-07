# `src/context_compactor.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_content_as_text` — function, line 23
- **called from:**
- `src/context_compactor.py:111`
- `src/context_compactor.py:281`
- `tests/test_context_compactor.py:263`
- `tests/test_context_compactor.py:268`
- `tests/test_context_compactor.py:275`
- `tests/test_context_compactor.py:278`

## `prune_multimodal_images` — function, line 45
- **called from:**
- `src/clean_agent_preview.py:6302`
- `src/llm_core.py:4625`
- `src/llm_core.py:4699`
- `tests/test_context_compactor.py:296`

## `_image_turn_label` — function, line 98
- **called from:**
- `src/context_compactor.py:156`

## `keep_recent_image_turns` — function, line 118
- **called from:**
- `src/clean_agent_preview.py:6303`
- `tests/test_vision_inline.py:130`
- `tests/test_vision_inline.py:150`
- `tests/test_vision_inline.py:158`
- `tests/test_vision_inline.py:168`

## `auto_compact_threshold_percent` — function, line 190
- **called from:**
- `routes/history/history_routes.py:1216`
- `src/context_compactor.py:673`

## `_strip_think_blocks` — function, line 234
- **called from:**
- `src/agent_loop.py:560`
- `src/agent_loop.py:6399`
- `src/agent_loop.py:9142`
- `src/agent_loop.py:14481`
- `src/agent_loop.py:14495`
- `src/agent_loop.py:17238`
- `src/agent_loop.py:17910`
- `src/agent_loop.py:17957`
- `src/agent_loop.py:18177`
- `src/agent_loop.py:19460`
- `src/agent_loop.py:19481`
- `src/agent_loop.py:19499`
- `src/agent_loop.py:19515`
- `src/agent_loop.py:19526`
- `src/agent_loop.py:19916`
- `src/agent_loop.py:19938`
- `src/agent_loop.py:20315`
- `src/agent_loop.py:20718`
- `src/agent_loop.py:20727`
- `src/agent_loop.py:25739`
- `src/agent_loop.py:28701`
- `src/agent_loop.py:30526`
- `src/agent_loop.py:30629`
- `src/agent_loop.py:30638`
- `src/agent_loop.py:31299`
- `src/agent_loop.py:31432`
- `src/agent_loop.py:32310`
- `src/agent_loop.py:37751`
- `src/agent_loop.py:38122`
- `src/agent_loop.py:38202`
- `src/agent_loop.py:38569`
- `src/context_compactor.py:308`
- `tests/test_context_compactor.py:309`
- `tests/test_context_compactor.py:316`
- `tests/test_context_compactor.py:322`
- `tests/test_context_compactor.py:325`
- `tests/test_context_compactor.py:326`
- `tests/test_redos_think_blocks.py:60`
- `tests/test_redos_think_blocks.py:64`
- `tests/test_redos_think_blocks.py:65`
- `tests/test_redos_think_blocks.py:75`
- `tests/test_redos_think_blocks.py:85`

## `_message_excerpt` — function, line 247
- **called from:**
- `src/context_compactor.py:281`
- `tests/test_context_compactor.py:341`
- `tests/test_context_compactor.py:345`
- `tests/test_context_compactor.py:352`
- `tests/test_context_compactor.py:353`

## `_build_convo_text` — function, line 268
- **called from:**
- `routes/session_routes.py:1389`
- `src/context_compactor.py:749`
- `tests/test_context_compactor.py:362`
- `tests/test_context_compactor.py:370`

## `normalize_compaction_summary` — function, line 299
- **called from:**
- `routes/history/history_routes.py:1550`
- `routes/session_routes.py:1407`
- `src/context_compactor.py:839`
- `src/context_compactor.py:982`
- `tests/test_context_compactor.py:334`

## `_sanitize_tool_messages` — function, line 314
- **called from:**
- `src/context_compactor.py:547`
- `src/context_compactor.py:558`
- `src/context_compactor.py:637`

## `_message_text_token_estimate` — function, line 360
- **called from:**
- `src/context_compactor.py:466`
- `tests/test_context_compactor_nonstring.py:11`
- `tests/test_context_compactor_nonstring.py:12`
- `tests/test_context_compactor_nonstring.py:23`

## `_truncate_text_to_token_budget` — function, line 366
- **called from:**
- `src/context_compactor.py:453`
- `src/context_compactor.py:462`
- `tests/test_context_compactor_nonstring.py:18`
- `tests/test_context_compactor_nonstring.py:19`
- `tests/test_context_compactor_nonstring.py:24`

## `_truncate_tool_call_args` — function, line 408
- **called from:**
- `src/context_compactor.py:470`

## `_truncate_message_to_token_budget` — function, line 448
- **called from:**
- `src/context_compactor.py:621`
- `src/context_compactor.py:635`
- `tests/test_compact_truncate_tool_call_args.py:43`
- `tests/test_compact_truncate_tool_call_args.py:56`
- `tests/test_compact_truncate_tool_call_args.py:61`

## `trim_for_context` — function, line 473
- **called from:**
- `routes/chat_helpers.py:1578`
- `routes/chat_routes.py:1409`
- `src/agent_loop.py:24659`
- `src/clean_agent_preview.py:5546`
- `src/context_compactor.py:697`
- `src/llm_core.py:4636`
- `src/llm_core.py:4717`
- `tests/test_context_compactor.py:86`
- `tests/test_context_compactor.py:111`
- `tests/test_context_compactor.py:129`
- `tests/test_context_compactor.py:145`
- `tests/test_context_compactor.py:159`
- `tests/test_context_compactor.py:174`
- `tests/test_context_compactor.py:206`
- `tests/test_context_compactor.py:240`
- `tests/test_context_compactor.py:256`
- `tests/test_context_compactor.py:815`
- `tests/test_context_compactor.py:820`
- `tests/test_context_compactor.py:828`

## `_is_research_primer` — function, line 510
- **called from:**
- `src/context_compactor.py:519`
- `src/context_compactor.py:523`

## `_is_compaction_summary` — function, line 513
- **called from:**
- `src/context_compactor.py:520`
- `src/context_compactor.py:523`

## `_is_direct_user_message` — function, line 566
- **called from:**
- `src/context_compactor.py:582`
- `src/context_compactor.py:630`

## `maybe_compact` — function (async), line 642
- **called from:**
- `routes/chat_helpers.py:1571`
- `routes/chat_routes.py:1397`
- `src/agent_loop.py:24777`
- `src/agent_loop.py:26642`
- `tests/test_compaction_summary_failure.py:55`
- `tests/test_context_compactor.py:406`
- `tests/test_context_compactor.py:505`
- `tests/test_context_compactor.py:599`
- `tests/test_context_compactor.py:722`
- `tests/test_context_compactor.py:778`

## `_summarize` — function (async), line 789
- **called from:**
- `src/context_compactor.py:816`
- `src/context_compactor.py:823`
- `tests/cli/test_research_cli_preview.py:23`
- `tests/test_background_tool_jobs.py:188`

## `_map_convo_split_to_history` — function, line 893
- **called from:**
- `src/context_compactor.py:867`
- `src/context_compactor.py:1032`

## `_same_message` — function, line 928
- **called from:**
- `src/context_compactor.py:941`
- `src/context_compactor.py:954`

## `_update_session_history` — function, line 965
- **called from:**
- `src/context_compactor.py:880`
- `src/context_compactor.py:1041`

## `apply_compaction_state` — function, line 1007
- **called from:**
- `routes/chat_routes.py:2596`
- `routes/chat_routes.py:4514`
- `src/agent_loop.py:27083`
- `src/context_compactor.py:1060`
- `tests/test_context_compactor.py:749`
- `tests/test_context_compactor.py:751`

## `apply_compaction_state_for_session` — function, line 1046
- **called from:**
- `src/agent_loop.py:27087`
