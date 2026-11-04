# `src/context_compactor.py` — definitions & call sites

19 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_content_as_text` — function, line 21
- **called from:**
- `src/context_compactor.py:139`
- `tests/test_context_compactor.py:127`
- `tests/test_context_compactor.py:132`
- `tests/test_context_compactor.py:139`
- `tests/test_context_compactor.py:142`

## `_strip_think_blocks` — function, line 92
- **called from:**
- `src/agent_loop.py:3860`
- `src/agent_loop.py:5894`
- `src/agent_loop.py:5918`
- `src/agent_loop.py:5999`
- `src/agent_loop.py:6039`
- `src/agent_loop.py:6132`
- `src/context_compactor.py:166`
- `tests/test_context_compactor.py:148`
- `tests/test_context_compactor.py:155`
- `tests/test_context_compactor.py:161`
- `tests/test_context_compactor.py:164`
- `tests/test_context_compactor.py:165`
- `tests/test_redos_think_blocks.py:60`
- `tests/test_redos_think_blocks.py:64`
- `tests/test_redos_think_blocks.py:65`
- `tests/test_redos_think_blocks.py:75`
- `tests/test_redos_think_blocks.py:85`

## `_message_excerpt` — function, line 105
- **called from:**
- `src/context_compactor.py:139`
- `tests/test_context_compactor.py:180`
- `tests/test_context_compactor.py:184`
- `tests/test_context_compactor.py:191`
- `tests/test_context_compactor.py:192`

## `_build_convo_text` — function, line 126
- **called from:**
- `routes/session_routes.py:1236`
- `src/context_compactor.py:480`
- `tests/test_context_compactor.py:201`
- `tests/test_context_compactor.py:209`

## `normalize_compaction_summary` — function, line 157
- **called from:**
- `routes/history/history_routes.py:1143`
- `routes/session_routes.py:1253`
- `src/context_compactor.py:565`
- `src/context_compactor.py:708`
- `tests/test_context_compactor.py:173`

## `_sanitize_tool_messages` — function, line 172
- **called from:**
- `src/context_compactor.py:369`
- `src/context_compactor.py:380`
- `src/context_compactor.py:408`

## `_message_text_token_estimate` — function, line 218
- **called from:**
- `src/context_compactor.py:307`
- `tests/test_context_compactor_nonstring.py:11`
- `tests/test_context_compactor_nonstring.py:12`
- `tests/test_context_compactor_nonstring.py:23`

## `_truncate_text_to_token_budget` — function, line 224
- **called from:**
- `src/context_compactor.py:294`
- `src/context_compactor.py:303`
- `tests/test_context_compactor_nonstring.py:18`
- `tests/test_context_compactor_nonstring.py:19`
- `tests/test_context_compactor_nonstring.py:24`

## `_truncate_tool_call_args` — function, line 249
- **called from:**
- `src/context_compactor.py:311`

## `_truncate_message_to_token_budget` — function, line 289
- **called from:**
- `src/context_compactor.py:406`
- `tests/test_compact_truncate_tool_call_args.py:43`
- `tests/test_compact_truncate_tool_call_args.py:56`
- `tests/test_compact_truncate_tool_call_args.py:61`

## `trim_for_context` — function, line 314
- **called from:**
- `routes/chat_helpers.py:978`
- `routes/chat_routes.py:213`
- `src/agent_loop.py:4750`
- `tests/test_context_compactor.py:90`
- `tests/test_context_compactor.py:103`
- `tests/test_context_compactor.py:118`
- `tests/test_context_compactor.py:608`
- `tests/test_context_compactor.py:613`
- `tests/test_context_compactor.py:621`

## `_is_research_primer` — function, line 351
- **called from:**
- `src/context_compactor.py:353`
- `src/context_compactor.py:354`

## `maybe_compact` — function (async), line 413
- **called from:**
- `routes/chat_helpers.py:972`
- `routes/chat_routes.py:201`
- `src/agent_loop.py:4780`
- `tests/test_compaction_summary_failure.py:55`
- `tests/test_context_compactor.py:245`
- `tests/test_context_compactor.py:337`
- `tests/test_context_compactor.py:431`
- `tests/test_context_compactor.py:554`

## `_summarize` — function (async), line 517
- **called from:**
- `src/context_compactor.py:543`
- `src/context_compactor.py:550`
- `tests/cli/test_research_cli_preview.py:23`

## `_map_convo_split_to_history` — function, line 619
- **called from:**
- `src/context_compactor.py:593`
- `src/context_compactor.py:758`

## `_same_message` — function, line 654
- **called from:**
- `src/context_compactor.py:667`
- `src/context_compactor.py:680`

## `_update_session_history` — function, line 691
- **called from:**
- `src/context_compactor.py:606`
- `src/context_compactor.py:767`

## `apply_compaction_state` — function, line 733
- **called from:**
- `routes/chat_routes.py:1065`
- `routes/chat_routes.py:2216`
- `src/agent_loop.py:5412`
- `src/context_compactor.py:786`
- `tests/test_context_compactor.py:581`
- `tests/test_context_compactor.py:583`

## `apply_compaction_state_for_session` — function, line 772
- **called from:**
- `src/agent_loop.py:5416`
