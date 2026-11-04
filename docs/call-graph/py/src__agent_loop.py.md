# `src/agent_loop.py` — definitions & call sites

106 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_expand_browser_mcp_tools` — function, line 78
- **called from:**
- `src/agent_loop.py:4529`
- `src/agent_loop.py:4532`

## `_looks_like_notes_list_request` — function, line 102
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_note_list_summary_from_tool_output` — function, line 111
- **called from:**
- `src/agent_loop.py:2289`
- `src/agent_loop.py:6642`
- `src/agent_loop.py:6988`

## `_calendar_list_summary_from_tool_output` — function, line 140
- **called from:**
- `src/agent_loop.py:2291`
- `src/agent_loop.py:6993`

## `_email_list_summary_from_tool_output` — function, line 173
- **called from:**
- `src/agent_loop.py:2293`
- `src/agent_loop.py:7005`

## `_format_email_summary_item` — function, line 224
- **called from:**
- `src/agent_loop.py:186`
- `src/agent_loop.py:210`

## `_email_read_summary_from_tool_output` — function, line 239
- **called from:**
- `src/agent_loop.py:2295`
- `src/agent_loop.py:7010`

## `_load_mcp_disabled_map` — function, line 289
- **called from:**
- `src/agent_loop.py:4175`

## `_domain_rules_for_tools` — function, line 549
- **called from:**
- `src/agent_loop.py:955`
- `src/agent_loop.py:959`
- `tests/test_api_call_integration_routing.py:69`
- `tests/test_tool_rag_contacts_domain.py:63`

## `get_builtin_overrides` — function, line 804
- **called from:**
- `routes/skills_routes.py:1271`
- `routes/skills_routes.py:1303`
- `scripts/dump_agent_prompt.py:500`
- `src/agent_loop.py:820`
- `src/agent_loop.py:2672`
- `src/agent_loop.py:3339`

## `_section_text` — function, line 817
- **called from:**
- `src/agent_loop.py:933`

## `_schema_map` — function, line 828
- **called from:**
- `src/agent_loop.py:934`

## `_schema_usage_sketch` — function, line 839
- **called from:**
- `src/agent_loop.py:911`

## `_tool_one_liner` — function, line 854
- **called from:**
- `src/agent_loop.py:933`

## `_schema_one_liner` — function, line 903
- **called from:**
- `src/agent_loop.py:937`

## `_assemble_prompt` — function, line 917
- **called from:**
- `src/agent_loop.py:964`
- `src/agent_loop.py:3352`
- `src/agent_loop.py:3360`
- `src/agent_loop.py:3364`
- `tests/test_spawn_agent.py:60`
- `tests/test_spawn_agent.py:64`

## `_is_ollama_openai_compat_url` — function, line 992
- **called from:**
- `scripts/dump_agent_prompt.py:90`
- `scripts/dump_agent_prompt.py:329`
- `src/agent_loop.py:1120`
- `src/llm_core.py:2733`
- `src/llm_core.py:3005`
- `tests/test_llm_core_ollama_thinking.py:79`
- `tests/test_llm_core_ollama_thinking.py:82`
- `tests/test_llm_core_ollama_thinking.py:85`
- `tests/test_llm_core_ollama_thinking.py:88`
- `tests/test_llm_core_ollama_thinking.py:92`
- `tests/test_llm_core_ollama_thinking.py:96`
- `tests/test_llm_core_ollama_thinking.py:99`
- `tests/test_llm_core_ollama_thinking.py:102`
- `tests/test_llm_core_ollama_thinking.py:107`
- `tests/test_llm_core_ollama_thinking.py:110`
- `tests/test_llm_core_ollama_thinking.py:114`
- `tests/test_llm_core_ollama_thinking.py:117`
- `tests/test_llm_core_ollama_thinking.py:120`
- `tests/test_llm_core_ollama_thinking.py:123`
- `tests/test_llm_core_ollama_thinking.py:126`
- `tests/test_tool_support_heuristic.py:44`

## `_is_local_openai_compat_url` — function, line 1007
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_endpoint_lookup_keys` — function, line 1029
- **called from:**
- `scripts/dump_agent_prompt.py:77`
- `src/agent_loop.py:1070`
- `tests/test_tool_support_heuristic.py:165`
- `tests/test_tool_support_heuristic.py:171`

## `add` — function, line 1034
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:517`
- `core/database.py:1972`
- `core/platform_compat.py:205`
- `core/session_manager.py:402`
- `core/session_manager.py:464`
- `core/session_manager.py:698`
- `core/session_manager.py:747`
- `core/session_manager.py:924`
- `mcp_servers/email_server.py:552`
- `mcp_servers/email_server.py:1665`
- `mcp_servers/email_server.py:1706`
- `mcp_servers/email_server.py:1707`
- `mcp_servers/email_server.py:1828`
- `mcp_servers/image_gen_server.py:143`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:190`
- `routes/calendar_routes.py:316`
- `routes/calendar_routes.py:324`
- `routes/calendar_routes.py:1253`
- `routes/calendar_routes.py:1374`
- `routes/calendar_routes.py:1441`
- `routes/calendar_routes.py:1540`
- `routes/chat_helpers.py:86`
- `routes/chat_routes.py:1688`
- `routes/chat_routes.py:1742`
- `routes/chatgpt_subscription_routes.py:54`
- `routes/chatgpt_subscription_routes.py:79`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:476`
- `routes/contacts/contacts_routes.py:604`
- `routes/cookbook_routes.py:1579`
- `routes/cookbook_routes.py:1916`
- `routes/cookbook_routes.py:3006`
- `routes/cookbook_routes.py:3788`
- `routes/cookbook_routes.py:3855`
- `routes/cookbook_routes.py:3971`
- `routes/cookbook_routes.py:4058`
- `routes/copilot_routes.py:77`
- `routes/device_flow.py:154`
- `routes/document/document_routes.py:165`
- `routes/document/document_routes.py:201`
- `routes/document/document_routes.py:202`
- `routes/document/document_routes.py:545`
- `routes/document/document_routes.py:604`
- `routes/document/document_routes.py:683`
- `routes/document/document_routes.py:839`
- `routes/editor_draft_routes.py:126`
- `routes/email_helpers.py:1700`
- `routes/email_helpers.py:1732`
- `routes/email_helpers.py:1868`
- `routes/email_pollers.py:810`
- … +1221 more (grep the name in repo)

## `_agent_route_tool_mode` — function, line 1053
- **called from:**
- `routes/chat_helpers.py:933`
- `src/agent_loop.py:4798`
- `tests/test_tool_support_heuristic.py:218`
- `tests/test_tool_support_heuristic.py:223`

## `_detect_admin_intent` — function, line 1165
- **called from:**
- `src/agent_loop.py:4097`
- `tests/test_agent_loop.py:121`
- `tests/test_agent_loop.py:124`
- `tests/test_agent_loop.py:127`
- `tests/test_agent_loop.py:130`
- `tests/test_agent_loop.py:133`
- `tests/test_agent_loop.py:136`
- `tests/test_agent_loop.py:139`
- `tests/test_agent_loop.py:142`
- `tests/test_agent_loop.py:145`
- `tests/test_agent_loop.py:148`
- `tests/test_agent_loop.py:151`
- `tests/test_agent_loop.py:154`
- `tests/test_agent_loop.py:157`
- `tests/test_agent_loop.py:162`
- `tests/test_agent_loop.py:165`
- `tests/test_agent_loop.py:168`
- `tests/test_agent_loop.py:171`
- `tests/test_agent_loop.py:176`
- `tests/test_agent_loop.py:179`
- `tests/test_agent_loop.py:186`
- `tests/test_agent_loop.py:192`
- `tests/test_agent_loop.py:201`

## `_extract_last_user_message` — function, line 1177
- **called from:**
- `src/agent_loop.py:1860`
- `src/agent_loop.py:1968`
- `src/agent_loop.py:2046`
- `src/agent_loop.py:2153`
- `src/agent_loop.py:2191`
- `src/agent_loop.py:3058`
- `src/agent_loop.py:4098`
- `src/agent_loop.py:4924`
- `src/agent_loop.py:6194`

## `_user_turn_count` — function, line 1188
- **called from:**
- `src/agent_loop.py:4111`

## `_insert_before_latest_user` — function, line 1197
- **called from:**
- `src/agent_loop.py:4094`
- `tests/test_agent_loop.py:85`
- `tests/test_agent_loop.py:104`

## `_uploaded_files_context_message` — function, line 1208
- **called from:**
- `src/agent_loop.py:4092`

## `_looks_like_workspace_coding_request` — function, line 1267
- **called from:**
- `src/agent_loop.py:4494`

## `_looks_like_local_computer_request` — function, line 1282
- **called from:**
- `src/agent_loop.py:4496`

## `_explicitly_references_missing_workspace` — function, line 1287
- **called from:**
- `src/agent_loop.py:4141`

## `_local_computer_rules` — function, line 1296
- **called from:**
- `src/agent_loop.py:3033`

## `_workspace_coding_rules` — function, line 1311
- **called from:**
- `src/agent_loop.py:3027`

## `_looks_like_workspace_coding_request` — function, line 1357
- **called from:**
- `src/agent_loop.py:4494`

## `_looks_like_local_computer_request` — function, line 1372
- **called from:**
- `src/agent_loop.py:4496`

## `_explicitly_references_missing_workspace` — function, line 1377
- **called from:**
- `src/agent_loop.py:4141`

## `_local_computer_rules` — function, line 1386
- **called from:**
- `src/agent_loop.py:3033`

## `_workspace_coding_rules` — function, line 1401
- **called from:**
- `src/agent_loop.py:3027`

## `_strip_think_blocks` — function, line 1420
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

## `_is_explicit_continuation` — function, line 1493
- **called from:**
- `src/agent_loop.py:1571`
- `tests/test_redos_verdict_continuation.py:63`
- `tests/test_redos_verdict_continuation.py:70`

## `_is_casual_low_signal` — function, line 1498
- **called from:**
- `routes/chat_helpers.py:774`
- `src/agent_loop.py:1575`
- `src/agent_loop.py:4110`

## `_is_contextual_retry_continuation` — function, line 1514
- **called from:**
- `src/agent_loop.py:1570`

## `_assistant_requested_followup` — function, line 1529
- **called from:**
- `src/agent_loop.py:1571`

## `_classify_agent_request` — function, line 1561
- **called from:**
- `src/agent_loop.py:4108`
- `tests/test_agent_loop.py:68`
- `tests/test_api_call_integration_routing.py:52`
- `tests/test_api_call_integration_routing.py:58`
- `tests/test_api_call_integration_routing.py:76`
- `tests/test_bg_job_tools.py:160`
- `tests/test_bg_job_tools.py:173`
- `tests/test_tool_rag_contacts_domain.py:26`

## `has` — function, line 1585
- **called from:**
- `src/agent_loop.py:1588`
- `src/agent_loop.py:1590`
- `src/agent_loop.py:1592`
- `src/agent_loop.py:1594`
- `src/agent_loop.py:1596`
- `src/agent_loop.py:1598`
- `src/agent_loop.py:1603`
- `src/agent_loop.py:1605`
- `src/agent_loop.py:1607`
- `src/agent_loop.py:1609`
- `src/agent_loop.py:1615`
- `src/agent_loop.py:1617`
- `src/agent_loop.py:1619`
- `src/agent_loop.py:1621`
- `src/agent_loop.py:1623`
- `src/agent_loop.py:1636`
- `src/agent_loop.py:1637`
- `src/agent_loop.py:1638`
- `src/agent_loop.py:1640`
- `src/agent_loop.py:1642`
- `src/agent_loop.py:1650`
- `static/app.js:3129`
- `static/app.js:3160`
- `static/js/admin.js:271`
- `static/js/admin.js:821`
- `static/js/admin.js:822`
- `static/js/admin.js:1994`
- `static/js/admin.js:2015`
- `static/js/admin.js:2545`
- `static/js/assistant.js:167`
- `static/js/calendar.js:946`
- `static/js/calendar.js:958`
- `static/js/calendar.js:959`
- `static/js/calendar.js:966`
- `static/js/calendar.js:990`
- `static/js/calendar.js:997`
- `static/js/calendar.js:998`
- `static/js/calendar.js:1065`
- `static/js/calendar.js:1672`
- `static/js/calendar.js:1676`
- `static/js/calendar.js:2348`
- `static/js/calendar.js:2350`
- `static/js/calendar.js:2350`
- `static/js/calendar.js:2373`
- `static/js/calendar.js:2375`
- `static/js/calendar.js:2375`
- `static/js/calendar.js:2809`
- `static/js/calendar/reminders.js:65`
- `static/js/censor.js:108`
- `static/js/chat.js:853`
- `static/js/chat.js:993`
- `static/js/chat.js:993`
- `static/js/chat.js:994`
- `static/js/chat.js:1048`
- `static/js/chat.js:1067`
- `static/js/chat.js:1506`
- `static/js/chat.js:2380`
- `static/js/chat.js:3165`
- `static/js/chat.js:4353`
- `static/js/chat.js:4479`
- … +279 more (grep the name in repo)

## `_turn_targets_active_document` — function, line 1663
- **called from:**
- `src/agent_loop.py:4112`

## `_is_email_document_obj` — function, line 1731
- **called from:**
- `src/agent_loop.py:4113`

## `_minimal_saved_memory_message` — function, line 1743
- **called from:**
- `src/agent_loop.py:2096`
- `src/agent_loop.py:2164`
- `src/agent_loop.py:2203`

## `_resolved_tool_event_name` — function, line 1789
- **called from:**
- `src/agent_loop.py:1835`
- `src/agent_loop.py:1843`
- `src/agent_loop.py:1943`
- `src/agent_loop.py:1951`
- `src/agent_loop.py:2278`
- `src/agent_loop.py:6777`
- `src/agent_loop.py:6979`

## `_minimal_recent_notes_tool_context_message` — function, line 1801
- **called from:**
- `src/agent_loop.py:2168`
- `src/agent_loop.py:2207`
- `src/agent_loop.py:4598`

## `_resolved_tool_event_name` — function, line 1897
- **called from:**
- `src/agent_loop.py:1835`
- `src/agent_loop.py:1843`
- `src/agent_loop.py:1943`
- `src/agent_loop.py:1951`
- `src/agent_loop.py:2278`
- `src/agent_loop.py:6777`
- `src/agent_loop.py:6979`

## `_minimal_recent_notes_tool_context_message` — function, line 1909
- **called from:**
- `src/agent_loop.py:2168`
- `src/agent_loop.py:2207`
- `src/agent_loop.py:4598`

## `_compact_email_draft_context` — function, line 2005
- **called from:**
- `src/agent_loop.py:2770`

## `_minimal_odysseus_doc_messages` — function, line 2040
- **called from:**
- `src/agent_loop.py:4821`
- `tests/test_external_context_tool_gate.py:472`

## `_looks_like_notes_turn` — function, line 2128
- **called from:**
- `src/agent_loop.py:4595`

## `_looks_like_notes_calendar_followup` — function, line 2139
- **called from:**
- `src/agent_loop.py:4597`

## `_minimal_odysseus_notes_messages` — function, line 2147
- **called from:**
- `src/agent_loop.py:4828`

## `_looks_like_memory_identity_turn` — function, line 2175
- **called from:**
- `src/agent_loop.py:4107`

## `_minimal_odysseus_general_messages` — function, line 2189
- **called from:**
- `src/agent_loop.py:4179`
- `src/agent_loop.py:4202`
- `src/agent_loop.py:4837`

## `_strip_doc_model_artifacts` — function, line 2223
- **called from:**
- `src/agent_loop.py:2508`
- `src/agent_loop.py:5555`
- `src/agent_loop.py:5752`

## `_normalize_ody_qwen_text_artifacts` — function, line 2258
- **called from:**
- `src/agent_loop.py:5757`
- `src/agent_loop.py:6707`
- `src/agent_loop.py:6936`

## `_ody_qwen_terminal_tool_summary` — function, line 2276
- **called from:**
- `src/agent_loop.py:6695`

## `_looks_like_destructive_request` — function, line 2310
- **called from:**
- `src/agent_loop.py:6939`

## `_looks_like_success_claim` — function, line 2314
- **called from:**
- `src/agent_loop.py:6940`

## `_looks_like_effectful_request` — function, line 2359
- **called from:**
- `src/agent_loop.py:2398`

## `_looks_like_tool_claim_narration` — function, line 2364
- **called from:**
- `src/agent_loop.py:6076`
- `src/agent_loop.py:6960`

## `_recent_user_request_is_effectful` — function, line 2373
- **called from:**
- `src/agent_loop.py:6075`
- `src/agent_loop.py:6959`

## `_looks_like_conclusion` — function, line 2426
- **called from:**
- `src/agent_loop.py:6079`

## `_tools_ran_in_history_since_last_user` — function, line 2442
- **called from:**
- `src/agent_loop.py:6080`

## `_normalize_truncated_document_tool_fences` — function, line 2472
- **called from:**
- `src/agent_loop.py:2507`

## `_normalize_stream_document_fences` — function, line 2499
- **called from:**
- `src/agent_loop.py:5794`
- `tests/test_odysseus_doc_fence_normalization.py:8`
- `tests/test_odysseus_doc_fence_normalization.py:23`
- `tests/test_odysseus_doc_fence_normalization.py:33`

## `repl` — function, line 2511
- **called from:**
- `src/text_helpers.py:111`

## `_document_stream_events` — function, line 2535
- **called from:**
- `src/agent_loop.py:5134`
- `src/agent_loop.py:6485`
- `tests/test_external_context_tool_gate.py:1426`

## `_recent_context_for_retrieval` — function, line 2568
- **called from:**
- `src/agent_loop.py:1525`
- `src/agent_loop.py:1572`
- `tests/test_tool_output_prompt_injection.py:89`

## `_strip_agent_injected_messages` — function, line 2597
- **called from:**
- `src/agent_loop.py:4805`
- `tests/test_user_time.py:189`

## `_prepend_agent_directive` — function, line 2612
- **called from:**
- `src/agent_loop.py:4840`
- `src/agent_loop.py:4842`
- `src/agent_loop.py:4844`

## `_is_odysseus_qwen_model` — function, line 2627
- **called from:**
- `src/agent_loop.py:4099`
- `src/agent_loop.py:4200`
- `src/agent_loop.py:4577`
- `src/agent_loop.py:5403`

## `_ody_qwen_temperature_cap` — function, line 2631
- **called from:**
- `src/agent_loop.py:4106`
- `src/agent_loop.py:4211`
- `src/agent_loop.py:5402`

## `_build_system_prompt` — function, line 2644
- **called from:**
- `scripts/dump_agent_prompt.py:153`
- `src/agent_loop.py:4804`
- `tests/test_prompt_injection_audit.py:82`
- `tests/test_prompt_injection_audit.py:102`
- `tests/test_prompt_injection_audit.py:123`
- `tests/test_prompt_injection_audit.py:151`
- `tests/test_prompt_injection_audit.py:170`
- `tests/test_prompt_injection_audit.py:189`
- `tests/test_prompt_injection_audit.py:216`
- `tests/test_prompt_injection_audit.py:236`
- `tests/test_prompt_injection_audit.py:255`
- `tests/test_skill_index_prompt_injection.py:125`
- `tests/test_skill_index_prompt_injection.py:154`
- `tests/test_skill_index_prompt_injection.py:188`
- `tests/test_skill_index_prompt_injection.py:192`
- `tests/test_tool_policy.py:435`
- `tests/test_user_time.py:150`
- `tests/test_user_time.py:180`
- `tests/test_workspace_confine.py:416`

## `_build_base_prompt` — function, line 3309
- **called from:**
- `src/agent_loop.py:2681`
- `src/agent_loop.py:2688`

## `_resolve_tool_blocks` — function, line 3411
- **called from:**
- `src/agent_loop.py:5801`
- `tests/test_fenced_example_not_executed_for_native_models.py:183`
- `tests/test_fenced_example_not_executed_for_native_models.py:190`
- `tests/test_fenced_example_not_executed_for_native_models.py:198`
- `tests/test_fenced_example_not_executed_for_native_models.py:310`
- `tests/test_native_tool_result_threading.py:20`

## `_inject_datetime_tool_call` — function, line 3462
- **called from:**
- `src/agent_loop.py:3506`

## `_append_tool_results` — function, line 3476
- **called from:**
- `src/agent_loop.py:5287`
- `src/agent_loop.py:6877`
- `tests/test_agent_loop.py:349`
- `tests/test_agent_loop.py:365`
- `tests/test_agent_loop.py:373`
- `tests/test_agent_loop.py:382`
- `tests/test_agent_loop.py:407`
- `tests/test_agent_loop.py:420`
- `tests/test_approved_replay_message_shape.py:27`
- `tests/test_external_context_tool_gate.py:440`
- `tests/test_external_context_tool_gate.py:725`
- `tests/test_llm_core_sanitize_tool_calls.py:48`
- `tests/test_native_tool_result_threading.py:30`
- `tests/test_temporal_grounding_stamps.py:75`
- `tests/test_temporal_grounding_stamps.py:130`
- `tests/test_temporal_grounding_stamps.py:178`
- `tests/test_tool_output_prompt_injection.py:49`
- `tests/test_tool_output_prompt_injection.py:79`
- `tests/test_tool_output_prompt_injection.py:106`

## `_compute_final_metrics` — function, line 3652
- **called from:**
- `src/agent_loop.py:7027`
- `tests/test_agent_loop.py:231`
- `tests/test_agent_loop.py:238`
- `tests/test_agent_loop.py:248`
- `tests/test_agent_loop.py:255`
- `tests/test_agent_loop.py:259`
- `tests/test_agent_loop.py:266`
- `tests/test_agent_loop.py:273`
- `tests/test_agent_loop.py:278`
- `tests/test_agent_loop.py:286`
- `tests/test_agent_loop.py:290`
- `tests/test_agent_loop.py:294`
- `tests/test_agent_loop.py:298`
- `tests/test_agent_loop.py:302`
- `tests/test_agent_loop.py:318`
- `tests/test_agent_loop.py:328`
- `tests/test_chat_metrics.py:198`

## `_usage_bucket` — function, line 3742
- **called from:**
- `src/agent_loop.py:4222`
- `src/agent_loop.py:4398`
- `src/agent_loop.py:5462`
- `src/agent_loop.py:5919`

## `_usage_bucket_summary` — function, line 3774
- **called from:**
- `src/agent_loop.py:4262`
- `src/agent_loop.py:4430`
- `src/agent_loop.py:5576`
- `src/agent_loop.py:7045`

## `_build_actions_snapshot` — function, line 3803
- **called from:**
- `src/agent_loop.py:6012`

## `_run_verifier_subagent` — function (async), line 3821
- **called from:**
- `src/agent_loop.py:6010`

## `_empty_response_fallback` — function, line 3871
- **called from:**
- `src/agent_loop.py:6925`
- `tests/test_llm_core_reasoning_content_fallback.py:201`
- `tests/test_llm_core_reasoning_content_fallback.py:217`

## `build_active_plan_note` — function, line 3917
- **called from:**
- `scripts/dump_agent_prompt.py:197`
- `src/agent_loop.py:4842`
- `tests/test_plan_mode.py:98`
- `tests/test_plan_mode.py:103`
- `tests/test_plan_mode.py:104`

## `_detect_runaway_call` — function, line 3942
- **called from:**
- `src/agent_loop.py:6142`
- `tests/test_loop_breaker_runaway.py:36`
- `tests/test_loop_breaker_runaway.py:41`
- `tests/test_loop_breaker_runaway.py:46`
- `tests/test_loop_breaker_runaway.py:51`
- `tests/test_loop_breaker_runaway.py:56`
- `tests/test_loop_breaker_runaway.py:57`
- `tests/test_loop_breaker_runaway.py:61`

## `stream_agent_loop` — function (async), line 3957
- **called from:**
- `routes/chat_routes.py:2696`
- `routes/skills_routes.py:466`
- `routes/skills_routes.py:750`
- `src/agent_tools/spawn_agent_tools.py:195`
- `src/bg_monitor.py:47`
- `src/task_scheduler.py:1909`
- `src/teacher_escalation.py:646`
- `tests/test_agent_rounds_exhausted.py:50`
- `tests/test_agent_rounds_exhausted.py:125`
- `tests/test_ask_user_persistence.py:67`
- `tests/test_external_context_tool_gate.py:809`
- `tests/test_external_context_tool_gate.py:846`
- `tests/test_external_context_tool_gate.py:880`
- `tests/test_external_context_tool_gate.py:913`
- `tests/test_external_context_tool_gate.py:947`
- `tests/test_external_context_tool_gate.py:1018`
- `tests/test_external_context_tool_gate.py:1067`
- `tests/test_external_context_tool_gate.py:1105`
- `tests/test_external_context_tool_gate.py:1160`
- `tests/test_external_context_tool_gate.py:1219`
- `tests/test_external_context_tool_gate.py:1284`
- `tests/test_external_context_tool_gate.py:1338`
- `tests/test_external_context_tool_gate.py:1470`
- `tests/test_fenced_example_not_executed_for_native_models.py:86`
- `tests/test_foreground_model_routing.py:2258`
- `tests/test_foreground_model_routing.py:2315`
- `tests/test_foreground_model_routing.py:2385`
- `tests/test_foreground_model_routing.py:2429`
- `tests/test_foreground_model_routing.py:2493`
- `tests/test_foreground_model_routing.py:2562`
- `tests/test_foreground_model_routing.py:2668`
- `tests/test_foreground_model_routing.py:2735`
- `tests/test_foreground_model_routing.py:2777`
- `tests/test_foreground_model_routing.py:2806`
- `tests/test_foreground_model_routing.py:2847`
- `tests/test_foreground_model_routing.py:2913`
- `tests/test_foreground_model_routing.py:2988`
- `tests/test_foreground_model_routing.py:3096`
- `tests/test_foreground_model_routing.py:3184`
- `tests/test_foreground_model_routing.py:3260`
- `tests/test_foreground_model_routing.py:3383`
- `tests/test_foreground_model_routing.py:3462`
- `tests/test_foreground_model_routing.py:3507`
- `tests/test_foreground_model_routing.py:3616`
- `tests/test_partial_tool_events.py:113`
- `tests/test_pr6020_rebase_regressions.py:78`
- `tests/test_pr6020_rebase_regressions.py:270`
- `tests/test_pr6020_rebase_regressions.py:320`
- `tests/test_tool_policy.py:112`
- `tests/test_tool_policy.py:138`
- `tests/test_tool_policy.py:174`
- `tests/test_tool_policy.py:226`
- `tests/test_tool_policy.py:257`
- `tests/test_tool_policy.py:291`
- `tests/test_tool_policy.py:314`
- `tests/test_tool_policy.py:345`
- `tests/test_tool_policy.py:370`
- `tests/test_tool_policy.py:402`
- `tests/test_tool_policy.py:469`
- `tests/test_tool_policy.py:520`
- … +4 more (grep the name in repo)

## `_direct_candidate_request` — function, line 4199
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_direct_terminal_event` — function, line 4218
- **called from:**
- `src/agent_loop.py:4364`
- `src/agent_loop.py:4377`
- `src/agent_loop.py:4388`

## `_route_finetune_modes` — function, line 4576
- **called from:**
- `src/agent_loop.py:4627`
- `src/agent_loop.py:4651`
- `src/agent_loop.py:4796`

## `_route_relevant_tools` — function, line 4619
- **called from:**
- `src/agent_loop.py:4652`
- `src/agent_loop.py:4797`

## `_trim_route_request_messages` — function, line 4705
- **called from:**
- `src/agent_loop.py:4878`
- `src/agent_loop.py:5380`
- `src/agent_loop.py:5675`

## `_without_protection` — function, line 4708
- **called from:**
- `src/agent_loop.py:4731`
- `src/agent_loop.py:4766`
- `src/agent_loop.py:4773`

## `_build_route_request_state` — function (async), line 4775
- **called from:**
- `src/agent_loop.py:4861`
- `src/agent_loop.py:5372`
- `src/agent_loop.py:5669`

## `_filter_route_tool_schemas` — function, line 5000
- **called from:**
- `src/agent_loop.py:5047`
- `src/agent_loop.py:5051`

## `_tool_schemas_for_route` — function, line 5007
- **called from:**
- `src/agent_loop.py:5332`
- `src/agent_loop.py:5393`

## `_push_approved_progress` — function (async), line 5082
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_approved_tool` — function (async), line 5085
- **called from:**
- `src/agent_loop.py:5102`

## `_candidate_request` — function (async), line 5364
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apply_candidate_compaction` — function, line 5409
- **called from:**
- `src/agent_loop.py:5601`
- `src/agent_loop.py:5703`
- `src/agent_loop.py:5713`
- `src/agent_loop.py:5727`

## `_finalize_round_usage` — function, line 5438
- **called from:**
- `src/agent_loop.py:5545`
- `src/agent_loop.py:5792`

## `_push_progress` — function (async), line 6355
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_tool` — function (async), line 6358
- **called from:**
- `src/agent_loop.py:6380`
