# `src/agent_loop.py` — definitions & call sites

647 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_local_media_discovery_call_allowed` — function, line 119
- **called from:**
- `src/agent_loop.py:33967`
- `tests/test_workspace_artifact_tool_floor.py:1695`
- `tests/test_workspace_artifact_tool_floor.py:1696`
- `tests/test_workspace_artifact_tool_floor.py:1697`
- `tests/test_workspace_artifact_tool_floor.py:1698`
- `tests/test_workspace_artifact_tool_floor.py:1701`
- `tests/test_workspace_artifact_tool_floor.py:1702`
- `tests/test_workspace_artifact_tool_floor.py:1705`
- `tests/test_workspace_artifact_tool_floor.py:1706`

## `_resolved_tool_call_id` — function, line 143
- **called from:**
- `src/agent_loop.py:32951`
- `tests/test_tool_event_call_ids.py:5`
- `tests/test_tool_event_call_ids.py:22`
- `tests/test_tool_event_call_ids.py:23`
- `tests/test_tool_event_call_ids.py:30`
- `tests/test_tool_event_call_ids.py:37`

## `_normalize_model_tool_surface` — function, line 179
- **called from:**
- `src/agent_loop.py:345`
- `src/agent_loop.py:393`
- `src/agent_loop.py:25765`
- `src/agent_loop.py:26793`
- `src/agent_loop.py:26822`

## `_route_thinking_policy` — function, line 184
- **called from:**
- `src/agent_loop.py:213`

## `_thinking_mode_for_route` — function, line 189
- **called from:**
- `src/agent_loop.py:22763`
- `src/agent_loop.py:25256`
- `tests/test_model_tool_modes.py:64`
- `tests/test_model_tool_modes.py:69`
- `tests/test_model_tool_modes.py:77`
- `tests/test_model_tool_modes.py:95`

## `_qwen_tool_router_output_budget` — function, line 223
- **called from:**
- `src/agent_loop.py:22060`
- `tests/test_minimal_native_tool_prompt.py:293`
- `tests/test_minimal_native_tool_prompt.py:294`

## `_allow_visual_tool_evidence_for_model` — function, line 233
- **called from:**
- `src/agent_loop.py:26412`
- `src/agent_loop.py:37163`
- `src/agent_loop.py:38372`
- `tests/test_minimal_native_tool_prompt.py:295`
- `tests/test_minimal_native_tool_prompt.py:298`
- `tests/test_minimal_native_tool_prompt.py:299`

## `_malformed_native_tool_recovery_instruction` — function, line 239
- **called from:**
- `tests/test_minimal_native_tool_prompt.py:302`

## `_looks_like_explicit_web_search_request` — function, line 252
- **called from:**
- `src/agent_loop.py:29381`
- `tests/test_minimal_native_tool_prompt.py:27`
- `tests/test_minimal_native_tool_prompt.py:34`

## `_repeated_artifact_mutation_can_finish` — function, line 279
- **called from:**
- `src/agent_loop.py:32884`
- `tests/test_minimal_native_tool_prompt.py:40`
- `tests/test_minimal_native_tool_prompt.py:44`
- `tests/test_minimal_native_tool_prompt.py:48`

## `_malformed_write_needs_body_handoff` — function, line 294
- **called from:**
- `src/agent_loop.py:28481`
- `tests/test_minimal_native_tool_prompt.py:55`
- `tests/test_minimal_native_tool_prompt.py:60`
- `tests/test_minimal_native_tool_prompt.py:65`

## `_post_finish_inspection_should_converge` — function, line 312
- **called from:**
- `src/agent_loop.py:37213`
- `tests/test_minimal_native_tool_prompt.py:81`
- `tests/test_minimal_native_tool_prompt.py:82`
- `tests/test_minimal_native_tool_prompt.py:85`

## `_parse_model_tool_modes` — function, line 333
- **called from:**
- `src/agent_loop.py:8807`
- `tests/test_model_tool_modes.py:28`

## `_model_id_tokens` — function, line 351
- **called from:**
- `src/agent_loop.py:370`
- `src/agent_loop.py:375`

## `_model_tool_mode_for_model` — function, line 356
- **called from:**
- `src/agent_loop.py:8808`

## `_apply_tool_surface_to_schemas` — function, line 389
- **called from:**
- `src/agent_loop.py:25835`
- `src/agent_loop.py:25906`
- `src/agent_loop.py:25940`
- `tests/test_model_tool_modes.py:50`
- `tests/test_model_tool_modes.py:58`

## `_contract_allows_early_completion` — function, line 402
- **called from:**
- `src/agent_loop.py:22065`
- `src/agent_loop.py:22145`
- `src/agent_loop.py:22247`
- `src/agent_loop.py:22355`
- `src/agent_loop.py:22531`
- `src/agent_loop.py:22572`
- `tests/test_contract_prompt_conversation.py:74`

## `_contract_prompt_domains` — function, line 413
- **called from:**
- `src/agent_loop.py:23406`
- `tests/test_contract_prompt_conversation.py:68`

## `_contract_allows_single_action_terminal` — function, line 423
- **called from:**
- `src/agent_loop.py:21778`
- `src/agent_loop.py:36973`
- `src/agent_loop.py:37012`
- `src/agent_loop.py:37023`
- `src/agent_loop.py:37034`
- `tests/test_contract_prompt_conversation.py:78`
- `tests/test_contract_prompt_conversation.py:79`
- `tests/test_contract_prompt_conversation.py:80`

## `_request_has_compound_actions` — function, line 428
- **called from:**
- `src/agent_loop.py:21779`
- `src/agent_loop.py:27327`
- `tests/test_tool_policy.py:1996`
- `tests/test_tool_policy.py:1999`
- `tests/test_tool_policy.py:2004`

## `_request_forbids_execution_retry` — function, line 455
- **called from:**
- `src/agent_loop.py:25621`
- `tests/test_contract_prompt_conversation.py:119`
- `tests/test_contract_prompt_conversation.py:123`

## `_contract_mutation_signature` — function, line 473
- **called from:**
- `src/agent_loop.py:32868`
- `src/agent_loop.py:33855`
- `src/agent_loop.py:34336`
- `tests/test_contract_prompt_conversation.py:86`
- `tests/test_contract_prompt_conversation.py:104`
- `tests/test_contract_prompt_conversation.py:109`

## `_has_accepted_contract_tool_call` — function, line 494
- **called from:**
- `src/agent_loop.py:29501`

## `_required_safe_read_operation` — function, line 501
- **called from:**
- `src/agent_loop.py:27330`
- `src/agent_loop.py:28573`
- `tests/test_required_read_operation.py:37`
- `tests/test_required_read_operation.py:38`
- `tests/test_required_read_operation.py:49`
- `tests/test_required_read_operation.py:64`
- `tests/test_required_read_operation.py:68`
- `tests/test_required_read_operation.py:69`
- `tests/test_required_read_operation.py:70`
- `tests/test_required_read_operation.py:73`
- `tests/test_required_read_operation.py:74`
- `tests/test_required_read_operation.py:84`
- `tests/test_required_read_operation.py:95`
- `tests/test_required_read_operation.py:99`
- `tests/test_required_read_operation.py:118`
- `tests/test_required_read_operation.py:137`
- `tests/test_required_read_operation.py:222`
- `tests/test_required_read_operation.py:224`
- `tests/test_required_read_operation.py:228`

## `field` — function, line 510
- **called from:**
- `routes/chat_helpers.py:456`
- `routes/chat_helpers.py:459`
- `routes/chat_helpers.py:469`
- `scripts/generate_env_reference.py:121`
- `scripts/ref_parity_audit.py:127`
- `services/memory/service.py:21`
- `services/memory/skill_format.py:373`
- `services/memory/skill_format.py:374`
- `services/memory/skill_format.py:375`
- `services/memory/skill_format.py:376`
- `services/memory/skill_format.py:384`
- `services/memory/skill_format.py:385`
- `services/memory/skill_format.py:386`
- `services/research/service.py:29`
- `services/research/service.py:30`
- `src/agent_loop.py:512`
- `src/agent_loop.py:512`
- `src/agent_loop.py:512`
- `src/agent_loop.py:512`
- `src/agent_runtime/context_resolution.py:96`
- `src/agent_runtime/effect_adapters.py:48`
- `src/agent_runtime/journal.py:27`
- `src/agent_runtime/journal.py:31`
- `src/agent_runtime/journal.py:66`
- `src/agent_runtime/journal.py:67`
- `src/agent_runtime/journal.py:72`
- `src/agent_runtime/journal.py:73`
- `src/agent_runtime/process_resources.py:247`
- `src/agent_trace.py:51`
- `src/browser_identity.py:199`
- `src/browser_lifecycle.py:246`
- `src/browser_lifecycle.py:247`
- `src/browser_lifecycle.py:343`
- `src/browser_lifecycle.py:344`
- `src/browser_lifecycle.py:350`
- `src/browser_lifecycle.py:351`
- `src/media_ingress.py:69`
- `src/media_ingress.py:81`
- `src/media_ingress.py:82`
- `src/memory_provider.py:21`
- `src/model_capabilities.py:479`
- `src/model_capability_readers/base.py:43`
- `src/tool_approvals.py:260`
- `src/tool_approvals.py:261`
- `src/tool_capabilities.py:1076`
- `src/tool_capabilities.py:1077`
- `src/tool_capabilities.py:1081`
- `src/tool_execution.py:100`
- `src/tool_policy.py:171`
- `src/turn_contract.py:2180`
- `src/web_recovery.py:8`
- `tests/run_focus.py:137`
- `static/js/document.js:16322`
- `static/js/editor/filters/effects.js:796`
- `static/js/editor/filters/effects.js:1031`
- `static/js/editor/panels/panels.js:177`
- `static/js/settings.js:1973`

## `_required_read_native_id` — function, line 536
- **called from:**
- `src/agent_loop.py:28584`

## `canonical_name` — function, line 539
- **called from:**
- `src/agent_loop.py:543`
- `src/agent_loop.py:543`

## `_required_read_summary` — function, line 555
- **called from:**
- `src/agent_loop.py:595`
- `tests/test_required_read_operation.py:100`
- `tests/test_required_read_operation.py:109`
- `tests/test_required_read_operation.py:112`

## `_dispatch_required_safe_read` — function (async), line 591
- **called from:**
- `src/agent_loop.py:28587`
- `tests/test_required_read_operation.py:119`

## `_tool_rejection_reason` — function, line 599
- **called from:**
- `src/agent_loop.py:34125`
- `tests/test_runtime_behavior_regressions.py:204`

## `_canonical_native_tool_name_for_offered` — function, line 684
- **called from:**
- `src/agent_loop.py:15698`

## `_native_tool_name_was_accepted` — function, line 702
- **called from:**
- `src/agent_loop.py:28442`
- `tests/test_tool_resolution_audit_aliases.py:7`
- `tests/test_tool_resolution_audit_aliases.py:8`
- `tests/test_tool_resolution_audit_aliases.py:9`
- `tests/test_tool_resolution_audit_aliases.py:13`

## `_normalize_native_alias_arguments` — function, line 722
- **called from:**
- `src/agent_loop.py:15702`

## `_redirect_local_html_inspection_call` — function, line 743
- **called from:**
- `src/agent_loop.py:15707`

## `_drop_legacy_email_alias_schemas_when_mcp_available` — function, line 768
- **called from:**
- `src/agent_loop.py:25905`
- `src/agent_loop.py:25939`

## `_is_qwen38_tool_router` — function, line 873
- **called from:**
- `src/agent_loop.py:206`
- `src/agent_loop.py:236`
- `src/agent_loop.py:14740`
- `src/agent_loop.py:22047`
- `src/agent_loop.py:22741`
- `src/agent_loop.py:23634`
- `src/agent_loop.py:23695`
- `src/agent_loop.py:25084`
- `src/agent_loop.py:25252`
- `src/agent_loop.py:38093`
- `src/agent_loop.py:38116`
- `tests/test_minimal_native_tool_prompt.py:277`
- `tests/test_minimal_native_tool_prompt.py:278`
- `tests/test_minimal_native_tool_prompt.py:279`
- `tests/test_minimal_native_tool_prompt.py:280`

## `_explicitly_avoids_web_lookup` — function, line 884
- **called from:**
- `src/agent_loop.py:1181`
- `src/agent_loop.py:9383`
- `src/agent_loop.py:22029`

## `_looks_like_explicit_plan_request` — function, line 894
- **called from:**
- `src/agent_loop.py:22002`
- `src/agent_loop.py:22005`
- `tests/test_agent_rounds_exhausted.py:903`
- `tests/test_agent_rounds_exhausted.py:906`
- `tests/test_tool_policy.py:145`

## `_schema_map` — function, line 916
- **called from:**
- `src/agent_loop.py:8519`

## `_schema_usage_sketch` — function, line 927
- **called from:**
- `src/agent_loop.py:999`

## `_tool_one_liner` — function, line 942
- **called from:**
- `src/agent_loop.py:8518`

## `_schema_one_liner` — function, line 991
- **called from:**
- `src/agent_loop.py:8522`

## `_looks_like_explicit_browser_interaction` — function, line 1014
- **called from:**
- `src/agent_loop.py:1275`
- `src/agent_loop.py:8095`
- `src/agent_loop.py:9109`
- `src/agent_loop.py:9397`
- `src/agent_loop.py:11241`
- `src/agent_loop.py:11323`
- `src/agent_loop.py:23185`
- `src/agent_loop.py:23329`
- `src/agent_loop.py:23476`
- `src/agent_loop.py:23545`
- `src/agent_loop.py:23717`
- `src/agent_loop.py:23733`
- `src/agent_loop.py:23816`
- `src/agent_loop.py:23969`
- `tests/test_private_browser_tool.py:478`
- `tests/test_private_browser_tool.py:481`
- `tests/test_private_browser_tool.py:484`
- `tests/test_private_browser_tool.py:487`
- `tests/test_tool_policy.py:110`
- `tests/test_tool_policy.py:961`

## `_parse_explicit_private_browser_inspection` — function, line 1046
- **called from:**
- `src/agent_loop.py:9396`
- `src/agent_loop.py:29008`
- `tests/test_tool_policy.py:64`
- `tests/test_tool_policy.py:72`
- `tests/test_tool_policy.py:83`
- `tests/test_tool_policy.py:98`
- `tests/test_tool_policy.py:127`

## `_looks_like_map_browser_request` — function, line 1111
- **called from:**
- `src/agent_loop.py:8096`
- `src/agent_loop.py:22026`
- `src/agent_loop.py:23186`
- `tests/test_tool_policy.py:1064`

## `_looks_like_youtube_tool_turn` — function, line 1133
- **called from:**
- `src/agent_loop.py:1273`
- `src/agent_loop.py:7627`
- `src/agent_loop.py:8091`
- `src/agent_loop.py:22025`
- `tests/test_redos_core_parsers.py:435`

## `_explicitly_named_personal_tools` — function, line 1168
- **called from:**
- `src/agent_loop.py:23918`
- `tests/test_explicit_personal_tool_routing.py:6`
- `tests/test_explicit_personal_tool_routing.py:13`
- `tests/test_explicit_personal_tool_routing.py:14`

## `_qwen38_router_tool_names` — function, line 1178
- **called from:**
- `src/agent_loop.py:23696`
- `src/agent_loop.py:23741`
- `src/agent_loop.py:24116`
- `tests/test_agent_runtime_context.py:646`
- `tests/test_minimal_native_tool_prompt.py:557`
- `tests/test_minimal_native_tool_prompt.py:558`
- `tests/test_minimal_native_tool_prompt.py:559`
- `tests/test_minimal_native_tool_prompt.py:560`
- `tests/test_minimal_native_tool_prompt.py:561`
- `tests/test_minimal_native_tool_prompt.py:587`
- `tests/test_minimal_native_tool_prompt.py:588`
- `tests/test_tool_policy.py:1942`
- `tests/test_tool_policy.py:1950`
- `tests/test_tool_policy.py:1958`
- `tests/test_tool_policy.py:1966`
- `tests/test_tool_policy.py:1972`
- `tests/test_tool_policy.py:1980`
- `tests/test_tool_policy.py:2676`
- `tests/test_tool_policy.py:2677`
- `tests/test_tool_policy.py:2678`
- `tests/test_tool_policy.py:2679`
- `tests/test_tool_policy.py:2680`
- `tests/test_tool_policy.py:3183`

## `_parse_explicit_skill_request` — function, line 1284
- **called from:**
- `src/agent_loop.py:28995`
- `src/agent_loop.py:31515`
- `tests/test_minimal_native_tool_prompt.py:1143`
- `tests/test_minimal_native_tool_prompt.py:1154`
- `tests/test_minimal_native_tool_prompt.py:1157`
- `tests/test_minimal_native_tool_prompt.py:1160`
- `tests/test_minimal_native_tool_prompt.py:1163`
- `tests/test_minimal_native_tool_prompt.py:1164`
- `tests/test_tool_policy.py:207`
- `tests/test_tool_policy.py:208`
- `tests/test_tool_policy.py:209`
- `tests/test_tool_policy.py:2329`
- `tests/test_tool_policy.py:2344`

## `_parse_qwen_explicit_create_request` — function, line 1415
- **called from:**
- `src/agent_loop.py:27359`
- `src/agent_loop.py:29142`
- `tests/test_minimal_native_tool_prompt.py:1170`
- `tests/test_minimal_native_tool_prompt.py:1178`
- `tests/test_minimal_native_tool_prompt.py:1186`
- `tests/test_minimal_native_tool_prompt.py:1194`
- `tests/test_minimal_native_tool_prompt.py:1201`
- `tests/test_minimal_native_tool_prompt.py:1207`
- `tests/test_tool_policy.py:2198`
- `tests/test_tool_policy.py:2825`

## `_nth_weekday` — function, line 1595
- **called from:**
- `src/agent_loop.py:1605`
- `src/agent_loop.py:1611`

## `_parse_explicit_open_panel_request` — function, line 1654
- **called from:**
- `src/agent_loop.py:4910`
- `src/agent_loop.py:28992`
- `tests/test_redos_core_parsers.py:332`
- `tests/test_tool_policy.py:2266`
- `tests/test_tool_policy.py:2272`
- `tests/test_tool_policy.py:2273`
- `tests/test_tool_policy.py:2274`
- `tests/test_tool_policy.py:2275`
- `tests/test_tool_policy.py:2276`
- `tests/test_tool_policy.py:2280`
- `tests/test_tool_policy.py:2284`
- `tests/test_tool_policy.py:2288`
- `tests/test_tool_policy.py:2292`
- `tests/test_tool_policy.py:2431`
- `tests/test_tool_policy.py:2437`
- `tests/test_tool_policy.py:2441`
- `tests/test_tool_policy.py:2445`
- `tests/test_tool_policy.py:2449`
- `tests/test_tool_policy.py:2453`
- `tests/test_tool_policy.py:2457`

## `_parse_explicit_theme_change_request` — function, line 1789
- **called from:**
- `src/agent_loop.py:29010`
- `tests/test_tool_policy.py:2305`
- `tests/test_tool_policy.py:2310`

## `_calendar_open_panel_snapshot_command` — function, line 1813
- **called from:**
- `src/agent_loop.py:35881`

## `_inherit_calendar_open_range_from_tool_events` — function, line 1866
- **called from:**
- `src/agent_loop.py:34851`
- `tests/test_minimal_native_tool_prompt.py:938`

## `_fabricated_calendar_event_anchor_without_tool` — function, line 1918
- **called from:**
- `src/agent_loop.py:31686`
- `tests/test_tool_policy.py:2463`
- `tests/test_tool_policy.py:2467`

## `_calendar_anchor_was_already_persisted` — function, line 1929
- **called from:**
- `src/agent_loop.py:31689`
- `tests/test_minimal_native_tool_prompt.py:1061`
- `tests/test_minimal_native_tool_prompt.py:1064`

## `_calendar_expected_mutation_actions` — function, line 1945
- **called from:**
- `src/agent_loop.py:31688`
- `src/agent_loop.py:31693`
- `src/agent_loop.py:32194`
- `tests/test_tool_policy.py:2473`

## `_has_successful_calendar_action_evidence` — function, line 1958
- **called from:**
- `src/agent_loop.py:31691`
- `src/agent_loop.py:32198`
- `tests/test_tool_policy.py:2475`
- `tests/test_tool_policy.py:2485`

## `_has_calendar_mutation_then_verification` — function, line 1986
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_state_manager_expected_action` — function, line 2010
- **called from:**
- `src/agent_loop.py:31417`
- `tests/test_state_manager_intent_boundaries.py:11`
- `tests/test_state_manager_intent_boundaries.py:17`
- `tests/test_state_manager_intent_boundaries.py:23`

## `_actions` — function, line 2040
- **called from:**
- `src/agent_loop.py:2054`
- `src/agent_loop.py:2069`

## `_has_successful_state_manager_evidence` — function, line 2099
- **called from:**
- `src/agent_loop.py:29524`
- `src/agent_loop.py:31523`
- `src/agent_loop.py:31552`

## `_tool_block_action` — function, line 2145
- **called from:**
- `src/agent_loop.py:2165`
- `src/agent_loop.py:29527`
- `src/agent_loop.py:29537`

## `_memory_search_precedes_unrequested_list` — function, line 2158
- **called from:**
- `src/agent_loop.py:30140`
- `tests/test_tui_round_cap.py:425`
- `tests/test_tui_round_cap.py:426`

## `_drop_rejected_round_response` — function, line 2171
- **called from:**
- `src/agent_loop.py:28707`
- `src/agent_loop.py:30591`
- `src/agent_loop.py:30719`
- `src/agent_loop.py:30765`
- `src/agent_loop.py:30786`
- `src/agent_loop.py:30802`
- `src/agent_loop.py:30834`
- `src/agent_loop.py:30963`
- `src/agent_loop.py:31013`
- `src/agent_loop.py:31115`
- `src/agent_loop.py:31386`
- `src/agent_loop.py:31446`
- `src/agent_loop.py:31478`
- `src/agent_loop.py:31538`
- `src/agent_loop.py:31569`
- `src/agent_loop.py:31608`
- `src/agent_loop.py:31642`
- `src/agent_loop.py:31707`
- `src/agent_loop.py:31766`
- `src/agent_loop.py:31894`
- `src/agent_loop.py:32209`
- `tests/test_tool_policy.py:2500`

## `_calendar_lookup_requires_fresh_tool` — function, line 2185
- **called from:**
- `src/agent_loop.py:31588`
- `tests/test_tool_policy.py:2010`
- `tests/test_tool_policy.py:2249`
- `tests/test_tool_policy.py:2254`
- `tests/test_tool_policy.py:2259`
- `tests/test_tui_round_cap.py:407`

## `_looks_like_agent_reasoning_preamble` — function, line 2233
- **called from:**
- `src/agent_loop.py:30664`
- `src/agent_loop.py:30791`
- `src/agent_loop.py:36634`
- `src/agent_loop.py:36981`
- `src/agent_loop.py:38077`
- `src/agent_loop.py:38585`
- `src/agent_loop.py:38680`
- `tests/test_codeql_induced_redos.py:117`
- `tests/test_failed_tool_completion_preamble.py:18`
- `tests/test_failed_tool_completion_preamble.py:105`
- `tests/test_failed_tool_completion_preamble.py:117`
- `tests/test_failed_tool_completion_preamble.py:126`
- `tests/test_failed_tool_completion_preamble.py:138`
- `tests/test_failed_tool_completion_preamble.py:147`
- `tests/test_minimal_native_tool_prompt.py:731`
- `tests/test_redos_core_parsers.py:320`
- `tests/test_tool_policy.py:2017`
- `tests/test_tool_policy.py:2020`
- `tests/test_tool_policy.py:2023`
- `tests/test_tool_policy.py:2027`
- `tests/test_tool_policy.py:2030`
- `tests/test_tool_policy.py:2033`
- `tests/test_tool_policy.py:2036`
- `tests/test_tool_policy.py:2056`

## `_strip_trailing_done` — function, line 2329
- **called from:**
- `src/agent_loop.py:38219`
- `tests/test_redos_core_parsers.py:214`

## `_strip_trailing_answer_promise` — function, line 2336
- **called from:**
- `src/agent_loop.py:30761`
- `tests/test_tool_policy.py:2046`
- `tests/test_tool_policy.py:2053`

## `_parse_qwen_explicit_recurring_task_request` — function, line 2362
- **called from:**
- `src/agent_loop.py:28993`

## `_parse_explicit_task_state_request` — function, line 2444
- **called from:**
- `src/agent_loop.py:28994`
- `src/agent_loop.py:31498`
- `tests/test_tool_policy.py:2315`
- `tests/test_tool_policy.py:2324`

## `_hhmm` — function, line 2461
- **called from:**
- `src/agent_loop.py:2484`

## `_parse_explicit_memory_state_request` — function, line 2507
- **called from:**
- `src/agent_loop.py:28996`
- `src/agent_loop.py:31500`

## `_parse_explicit_memory_lookup_request` — function, line 2538
- **called from:**
- `src/agent_loop.py:22527`
- `src/agent_loop.py:29001`
- `src/agent_loop.py:31506`
- `tests/test_minimal_native_tool_prompt.py:438`
- `tests/test_tool_policy.py:223`
- `tests/test_tool_policy.py:2149`

## `_parse_qwen_explicit_note_delete` — function, line 2577
- **called from:**
- `src/agent_loop.py:25495`
- `src/agent_loop.py:26037`
- `tests/test_minimal_native_tool_prompt.py:1333`
- `tests/test_minimal_native_tool_prompt.py:1336`

## `_space_field_leaders` — function, line 2592
- **called from:**
- `src/agent_loop.py:2674`
- `src/agent_loop.py:2821`

## `_payload_fields` — function, line 2596
- **called from:**
- `src/agent_loop.py:2697`
- `src/agent_loop.py:4885`
- `tests/test_codeql_induced_redos.py:45`

## `tail` — function, line 2604
- **called from:**
- `src/text_scanning.py:232`
- `src/text_scanning.py:250`
- `static/js/galleryEditor.js:8383`
- `static/js/streamingRenderer.js:15`
- `static/js/streamingRenderer.js:34`

## `tail` — function, line 2627
- **called from:**
- `src/text_scanning.py:232`
- `src/text_scanning.py:250`
- `static/js/galleryEditor.js:8383`
- `static/js/streamingRenderer.js:15`
- `static/js/streamingRenderer.js:34`

## `tail` — function, line 2665
- **called from:**
- `src/text_scanning.py:232`
- `src/text_scanning.py:250`
- `static/js/galleryEditor.js:8383`
- `static/js/streamingRenderer.js:15`
- `static/js/streamingRenderer.js:34`

## `_captures_after_first_prefix` — function, line 2677
- **called from:**
- `src/agent_loop.py:2707`
- `src/agent_loop.py:3502`
- `src/agent_loop.py:4940`
- `src/agent_loop.py:5941`
- `src/agent_loop.py:11456`
- `src/agent_loop.py:11462`
- `tests/test_redos_core_parsers.py:630`

## `_parse_qwen_explicit_note_update` — function, line 2700
- **called from:**
- `src/agent_loop.py:25502`
- `src/agent_loop.py:26041`
- `src/agent_loop.py:26099`
- `src/agent_loop.py:26104`

## `_parse_qwen_explicit_note_search` — function, line 2717
- **called from:**
- `src/agent_loop.py:25497`

## `_parse_qwen_explicit_note_view` — function, line 2734
- **called from:**
- `src/agent_loop.py:25498`
- `tests/test_tui_round_cap.py:430`
- `tests/test_tui_round_cap.py:433`

## `_is_qwen_explicit_model_list_request` — function, line 2752
- **called from:**
- `src/agent_loop.py:2944`
- `src/agent_loop.py:29263`
- `tests/test_tool_policy.py:2787`
- `tests/test_tool_policy.py:2790`
- `tests/test_tool_policy.py:2793`
- `tests/test_tui_round_cap.py:934`
- `tests/test_tui_round_cap.py:936`

## `_is_qwen_explicit_endpoint_list_request` — function, line 2781
- **called from:**
- `src/agent_loop.py:2942`
- `src/agent_loop.py:29259`
- `tests/test_config_file_settings_routing.py:27`
- `tests/test_config_file_settings_routing.py:32`

## `_pipeline_request_parts` — function, line 2809
- **called from:**
- `src/agent_loop.py:2827`
- `tests/test_codeql_induced_redos.py:57`
- `tests/test_redos_core_parsers.py:632`

## `tail` — function, line 2818
- **called from:**
- `src/text_scanning.py:232`
- `src/text_scanning.py:250`
- `static/js/galleryEditor.js:8383`
- `static/js/streamingRenderer.js:15`
- `static/js/streamingRenderer.js:34`

## `_parse_explicit_pipeline_request` — function, line 2825
- **called from:**
- `src/agent_loop.py:2868`
- `tests/test_tool_policy.py:3330`

## `_parse_explicit_teacher_request` — function, line 2837
- **called from:**
- `src/agent_loop.py:29009`
- `tests/test_tool_policy.py:132`
- `tests/test_tool_policy.py:140`

## `_parse_qwen_explicit_admin_request` — function, line 2852
- **called from:**
- `src/agent_loop.py:27362`
- `src/agent_loop.py:29003`
- `tests/test_config_file_settings_routing.py:18`
- `tests/test_config_file_settings_routing.py:28`
- `tests/test_config_file_settings_routing.py:50`
- `tests/test_tool_policy.py:122`
- `tests/test_tool_policy.py:2105`
- `tests/test_tool_policy.py:2110`
- `tests/test_tool_policy.py:2117`
- `tests/test_tool_policy.py:2425`
- `tests/test_tool_policy.py:2683`
- `tests/test_tool_policy.py:2687`
- `tests/test_tool_policy.py:2691`
- `tests/test_tool_policy.py:2695`
- `tests/test_tool_policy.py:2729`
- `tests/test_tool_policy.py:2732`
- `tests/test_tool_policy.py:2782`
- `tests/test_tool_policy.py:2817`
- `tests/test_tool_policy.py:3256`
- `tests/test_tool_policy.py:3259`
- `tests/test_tool_policy.py:3264`
- `tests/test_tool_policy.py:3267`
- `tests/test_tool_policy.py:3288`
- `tests/test_tool_policy.py:3291`
- `tests/test_tool_policy.py:3294`
- `tests/test_tool_policy.py:3299`
- `tests/test_tool_policy.py:3304`
- `tests/test_tool_policy.py:3317`
- `tests/test_tool_policy.py:3322`

## `_looks_like_explicit_app_settings_request` — function, line 2961
- **called from:**
- `src/agent_loop.py:2925`
- `src/agent_loop.py:11305`

## `_recent_session_id_for_title` — function, line 2994
- **called from:**
- `src/agent_loop.py:3123`
- `src/agent_loop.py:3181`

## `_recent_cookbook_session_id` — function, line 3018
- **called from:**
- `src/agent_loop.py:3065`

## `_parse_explicit_cookbook_task_action` — function, line 3053
- **called from:**
- `src/agent_loop.py:27344`
- `tests/test_tool_policy.py:2769`
- `tests/test_tool_policy.py:2775`
- `tests/test_tool_policy.py:3283`

## `_parse_qwen_explicit_session_action` — function, line 3082
- **called from:**
- `src/agent_loop.py:27341`
- `src/agent_loop.py:29007`
- `tests/test_tool_policy.py:2708`
- `tests/test_tool_policy.py:2721`
- `tests/test_tool_policy.py:2934`
- `tests/test_tool_policy.py:2945`
- `tests/test_tool_policy.py:2949`

## `_parse_qwen_explicit_session_create` — function, line 3129
- **called from:**
- `src/agent_loop.py:27342`
- `src/agent_loop.py:29004`
- `tests/test_tool_policy.py:2955`

## `_parse_qwen_explicit_session_send` — function, line 3165
- **called from:**
- `src/agent_loop.py:27343`
- `tests/test_tool_policy.py:2744`

## `_session_find_query_capture` — function, line 3200
- **called from:**
- `src/agent_loop.py:3234`
- `tests/test_redos_core_parsers.py:634`

## `_parse_qwen_explicit_session_find` — function, line 3213
- **called from:**
- `src/agent_loop.py:27361`
- `src/agent_loop.py:29006`
- `tests/test_tool_policy.py:2963`
- `tests/test_tool_policy.py:2967`
- `tests/test_tool_policy.py:2973`

## `_parse_qwen_explicit_chat_transcript_search` — function, line 3243
- **called from:**
- `src/agent_loop.py:27137`
- `src/agent_loop.py:27360`
- `src/agent_loop.py:29005`
- `tests/test_tool_policy.py:2978`
- `tests/test_tool_policy.py:2984`

## `_parse_qwen_explicit_resolve_contact` — function, line 3261
- **called from:**
- `src/agent_loop.py:29154`
- `tests/test_tool_policy.py:2992`
- `tests/test_tool_policy.py:2996`

## `_has_successful_tool_evidence` — function, line 3281
- **called from:**
- `src/agent_loop.py:29507`
- `src/agent_loop.py:31141`
- `tests/test_tool_policy.py:3166`

## `_summary_for_preemptive_admin_session_tool` — function, line 3303
- **called from:**
- `src/agent_loop.py:27632`

## `_is_email_account_identity_request` — function, line 3358
- **called from:**
- `src/agent_loop.py:29058`
- `src/agent_loop.py:29193`
- `tests/test_tool_policy.py:2074`
- `tests/test_tool_policy.py:2075`
- `tests/test_tool_policy.py:2076`
- `tests/test_tool_policy.py:2077`
- `tests/test_tool_policy.py:2078`

## `_is_qwen_explicit_latest_email_request` — function, line 3386
- **called from:**
- `src/agent_loop.py:23236`
- `src/agent_loop.py:29252`
- `src/agent_loop.py:35175`
- `tests/test_tui_round_cap.py:941`
- `tests/test_tui_round_cap.py:943`

## `_is_explicit_latest_email_open_request` — function, line 3420
- **called from:**
- `src/agent_loop.py:23235`
- `src/agent_loop.py:29807`
- `src/agent_loop.py:35012`

## `_parse_qwen_explicit_email_search_request` — function, line 3446
- **called from:**
- `src/agent_loop.py:3565`
- `src/agent_loop.py:23238`
- `src/agent_loop.py:29153`
- `src/agent_loop.py:29794`
- `src/agent_loop.py:35011`

## `_parse_qwen_explicit_email_topic_bulk_action_request` — function, line 3482
- **called from:**
- `src/agent_loop.py:27324`
- `src/agent_loop.py:27333`
- `src/agent_loop.py:27489`
- `src/agent_loop.py:29107`
- `src/agent_loop.py:29150`
- `src/agent_loop.py:34974`
- `tests/test_agent_loop.py:110`

## `_parse_explicit_email_uid_action` — function, line 3516
- **called from:**
- `src/agent_loop.py:27345`
- `tests/test_tool_policy.py:2833`
- `tests/test_tool_policy.py:2843`
- `tests/test_tool_policy.py:2853`
- `tests/test_tool_policy.py:2859`
- `tests/test_tool_policy.py:2862`
- `tests/test_tool_policy.py:2868`

## `_parse_explicit_email_search_tool` — function, line 3564
- **called from:**
- `src/agent_loop.py:27358`
- `tests/test_tool_policy.py:2876`
- `tests/test_tool_policy.py:2887`

## `_parse_qwen_explicit_spam_scan_request` — function, line 3573
- **called from:**
- `src/agent_loop.py:23237`
- `src/agent_loop.py:29083`
- `src/agent_loop.py:29147`
- `src/agent_loop.py:29768`
- `tests/test_tool_policy.py:3411`
- `tests/test_tool_policy.py:3416`

## `_parse_qwen_explicit_unsubscribe_scan_request` — function, line 3596
- **called from:**
- `src/agent_loop.py:29077`
- `src/agent_loop.py:29145`
- `tests/test_tool_policy.py:3018`

## `_parse_qwen_explicit_unsubscribe_email_request` — function, line 3609
- **called from:**
- `src/agent_loop.py:29071`
- `src/agent_loop.py:29146`
- `tests/test_tool_policy.py:3025`
- `tests/test_tool_policy.py:3033`

## `_parse_qwen_explicit_download_attachment_request` — function, line 3627
- **called from:**
- `src/agent_loop.py:29065`
- `src/agent_loop.py:29144`
- `tests/test_tool_policy.py:3002`
- `tests/test_tool_policy.py:3009`

## `_parse_qwen_explicit_blocked_sender_list_request` — function, line 3648
- **called from:**
- `src/agent_loop.py:29151`

## `_parse_qwen_explicit_block_sender_request` — function, line 3661
- **called from:**
- `src/agent_loop.py:29095`
- `src/agent_loop.py:29148`
- `tests/test_tool_policy.py:3057`
- `tests/test_tool_policy.py:3065`

## `_parse_qwen_explicit_bulk_email_request` — function, line 3679
- **called from:**
- `src/agent_loop.py:29101`
- `src/agent_loop.py:29149`
- `tests/test_tool_policy.py:3038`
- `tests/test_tool_policy.py:3045`
- `tests/test_tool_policy.py:3052`

## `_parse_qwen_explicit_unblock_sender_request` — function, line 3710
- **called from:**
- `src/agent_loop.py:29152`

## `_email_relative_date_range` — function, line 3720
- **called from:**
- `src/agent_loop.py:3748`

## `_parse_qwen_explicit_email_date_list_request` — function, line 3742
- **called from:**
- `src/agent_loop.py:29246`
- `src/agent_loop.py:29781`

## `_looks_like_effectful_request` — function, line 3795
- **called from:**
- `src/agent_loop.py:3834`

## `_looks_like_tool_claim_narration` — function, line 3800
- **called from:**
- `src/agent_loop.py:31842`
- `src/agent_loop.py:38828`

## `_recent_user_request_is_effectful` — function, line 3809
- **called from:**
- `src/agent_loop.py:31841`
- `src/agent_loop.py:38827`

## `_looks_like_conclusion` — function, line 3862
- **called from:**
- `src/agent_loop.py:31845`

## `_tools_ran_in_history_since_last_user` — function, line 3878
- **called from:**
- `src/agent_loop.py:31846`

## `_qwen_no_tool_boundary_answer` — function, line 3895
- **called from:**
- `src/agent_loop.py:22352`
- `tests/test_tool_policy.py:2089`
- `tests/test_tool_policy.py:2092`
- `tests/test_tool_policy.py:2095`

## `_parse_qwen_explicit_calendar_delete` — function, line 4051
- **called from:**
- `src/agent_loop.py:25506`
- `src/agent_loop.py:33718`
- `tests/test_minimal_native_tool_prompt.py:1343`
- `tests/test_minimal_native_tool_prompt.py:1346`
- `tests/test_minimal_native_tool_prompt.py:1357`

## `_parse_qwen_explicit_calendar_move` — function, line 4085
- **called from:**
- `src/agent_loop.py:29156`
- `src/agent_loop.py:33654`

## `_parse_qwen_explicit_calendar_absence_verify` — function, line 4156
- **called from:**
- `src/agent_loop.py:25507`
- `tests/test_minimal_native_tool_prompt.py:1349`

## `_parse_qwen_explicit_memory_search` — function, line 4187
- **called from:**
- `src/agent_loop.py:25672`
- `tests/test_minimal_native_tool_prompt.py:1363`
- `tests/test_minimal_native_tool_prompt.py:1366`

## `_parse_qwen_explicit_memory_delete` — function, line 4203
- **called from:**
- `src/agent_loop.py:25673`
- `src/agent_loop.py:26048`
- `tests/test_minimal_native_tool_prompt.py:1371`

## `_qwen_memory_id_from_search_output` — function, line 4220
- **called from:**
- `src/agent_loop.py:26178`
- `src/agent_loop.py:36440`

## `_extract_memory_add_text_from_user` — function, line 4238
- **called from:**
- `src/agent_loop.py:29002`
- `src/agent_loop.py:31508`
- `src/agent_loop.py:33359`

## `_parse_qwen_explicit_document_request` — function, line 4257
- **called from:**
- `src/agent_loop.py:29143`
- `tests/test_minimal_native_tool_prompt.py:1377`
- `tests/test_minimal_native_tool_prompt.py:1383`
- `tests/test_tool_policy.py:2333`

## `_parse_qwen_document_absence_verify` — function, line 4289
- **called from:**
- `src/agent_loop.py:33468`

## `_parse_qwen_explicit_contact_request` — function, line 4314
- **called from:**
- `src/agent_loop.py:29155`
- `tests/test_minimal_native_tool_prompt.py:1389`

## `_compact_openai_tool_schema` — function, line 4362
- **called from:**
- `scripts/compare_compact_tool_inventory.py:36`
- `src/agent_loop.py:397`

## `scrub` — function, line 4363
- **called from:**
- `src/agent_loop.py:4369`
- `src/agent_loop.py:4372`
- `src/agent_loop.py:4375`

## `_model_request_capture_enabled` — function, line 4382
- **called from:**
- `src/agent_loop.py:27657`
- `tests/test_model_request_snapshot.py:6`
- `tests/test_model_request_snapshot.py:8`

## `_model_request_snapshot` — function, line 4391
- **called from:**
- `src/agent_loop.py:27669`
- `tests/test_model_request_snapshot.py:14`

## `_safe_runtime_value` — function, line 4418
- **called from:**
- `src/agent_loop.py:4430`
- `src/agent_loop.py:4433`
- `src/agent_loop.py:4437`
- `src/agent_loop.py:4444`
- `src/agent_loop.py:4447`
- `src/agent_loop.py:4461`
- `src/agent_loop.py:4478`
- `src/agent_loop.py:4488`
- `src/agent_loop.py:4490`
- `src/agent_loop.py:4504`
- `src/agent_loop.py:14799`
- `src/agent_loop.py:14801`

## `_client_runtime_context_message` — function, line 4424
- **called from:**
- `src/agent_loop.py:14782`
- `tests/test_agent_runtime_context.py:653`
- `tests/test_native_terminal_context.py:53`

## `_backend_runtime_context_message` — function, line 4500
- **called from:**
- `src/agent_loop.py:14779`

## `_workspace_agents_context_message` — function, line 4523
- **called from:**
- `src/agent_loop.py:14785`

## `_expand_browser_mcp_tools` — function, line 4559
- **called from:**
- `src/agent_loop.py:23358`

## `_should_hide_raw_browser_mcp` — function, line 4592
- **called from:**
- `src/agent_loop.py:4572`
- `src/agent_loop.py:4615`
- `src/agent_loop.py:4632`

## `_with_raw_browser_mcp_hidden` — function, line 4600
- **called from:**
- `src/agent_loop.py:14856`

## `_filter_raw_browser_mcp_schemas` — function, line 4628
- **called from:**
- `src/agent_loop.py:14863`

## `_looks_like_notes_list_request` — function, line 4640
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_note_list_summary_from_tool_output` — function, line 4650
- **called from:**
- `src/agent_loop.py:13888`
- `src/agent_loop.py:35339`
- `src/agent_loop.py:38675`
- `src/clean_agent_preview.py:1045`
- `tests/test_minimal_native_tool_prompt.py:844`
- `tests/test_minimal_native_tool_prompt.py:864`
- `tests/test_minimal_native_tool_prompt.py:880`

## `_note_title_id_pairs_from_tool_output` — function, line 4708
- **called from:**
- `src/agent_loop.py:4753`
- `src/agent_loop.py:35274`
- `tests/test_tool_policy.py:2643`

## `add_pair` — function, line 4715
- **called from:**
- `src/agent_loop.py:4727`
- `src/agent_loop.py:4731`
- `src/agent_loop.py:6533`
- `src/agent_loop.py:6537`

## `_linkify_note_titles_from_tool_events` — function, line 4735
- **called from:**
- `src/agent_loop.py:38762`
- `tests/test_minimal_native_tool_prompt.py:852`

## `_notes_expected_actions` — function, line 4782
- **called from:**
- `src/agent_loop.py:5077`
- `src/agent_loop.py:30893`
- `src/agent_loop.py:30949`
- `src/agent_loop.py:31151`
- `src/agent_loop.py:31628`
- `tests/test_tool_policy.py:2523`
- `tests/test_tool_policy.py:2547`

## `_split_note_items` — function, line 4799
- **called from:**
- `src/agent_loop.py:4947`
- `tests/test_redos_core_parsers.py:341`

## `_clean_notes_search_query` — function, line 4807
- **called from:**
- `src/agent_loop.py:4974`
- `src/agent_loop.py:5015`
- `src/agent_loop.py:33236`

## `_notes_general_definition_answer` — function, line 4815
- **called from:**
- `src/agent_loop.py:4917`
- `src/agent_loop.py:30824`

## `_is_personal_tool_definition_turn` — function, line 4850
- **called from:**
- `src/agent_loop.py:2542`
- `src/agent_loop.py:5902`
- `src/agent_loop.py:22518`
- `tests/test_tool_policy.py:2147`

## `_remaining_checklist_name` — function, line 4867
- **called from:**
- `src/agent_loop.py:4972`
- `tests/test_redos_core_parsers.py:636`

## `_inject_datetime_tool_call` — function, line 4889
- **called from:**
- `src/agent_loop.py:16371`

## `_parse_simple_notes_tool_request` — function, line 4903
- **called from:**
- `src/agent_loop.py:30822`
- `tests/test_tool_policy.py:2160`
- `tests/test_tool_policy.py:2570`
- `tests/test_tool_policy.py:2586`
- `tests/test_tool_policy.py:2600`
- `tests/test_tool_policy.py:2607`
- `tests/test_tool_policy.py:2614`
- `tests/test_tool_policy.py:2621`
- `tests/test_tool_policy.py:2628`
- `tests/test_tool_policy.py:3075`
- `tests/test_tool_policy.py:3137`

## `_notes_body_requested` — function, line 5039
- **called from:**
- `src/agent_loop.py:30913`
- `src/agent_loop.py:35271`
- `src/agent_loop.py:35357`

## `_notes_request_requires_fresh_tool` — function, line 5048
- **called from:**
- `src/agent_loop.py:30940`
- `src/agent_loop.py:31148`
- `src/agent_loop.py:31625`
- `tests/test_tool_policy.py:2506`
- `tests/test_tool_policy.py:2511`
- `tests/test_tool_policy.py:2516`
- `tests/test_tool_policy.py:3079`
- `tests/test_tool_policy.py:3138`

## `_has_successful_notes_action_evidence` — function, line 5080
- **called from:**
- `src/agent_loop.py:30947`
- `src/agent_loop.py:31149`
- `src/agent_loop.py:31626`
- `tests/test_tool_policy.py:2525`
- `tests/test_tool_policy.py:2535`
- `tests/test_tool_policy.py:2550`

## `_memory_list_summary_from_tool_output` — function, line 5118
- **called from:**
- `src/agent_loop.py:13896`
- `src/agent_loop.py:26240`
- `src/agent_loop.py:34517`
- `src/agent_loop.py:38693`
- `src/clean_agent_preview.py:1214`
- `tests/test_agent_search_dedupe.py:58`
- `tests/test_agent_search_dedupe.py:70`
- `tests/test_minimal_native_tool_prompt.py:703`
- `tests/test_skill_deeplink_static.py:62`

## `_document_list_summary_from_tool_output` — function, line 5185
- **called from:**
- `src/agent_loop.py:13902`
- `src/agent_loop.py:34558`
- `src/agent_loop.py:38716`
- `src/clean_agent_preview.py:1078`
- `tests/test_minimal_native_tool_prompt.py:632`
- `tests/test_minimal_native_tool_prompt.py:642`
- `tests/test_minimal_native_tool_prompt.py:643`

## `_document_read_summary_from_tool_output` — function, line 5224
- **called from:**
- `src/agent_loop.py:13904`
- `src/agent_loop.py:38723`
- `tests/test_minimal_native_tool_prompt.py:765`

## `_document_detail_requested` — function, line 5232
- **called from:**
- `src/agent_loop.py:34541`
- `tests/test_minimal_native_tool_prompt.py:754`
- `tests/test_minimal_native_tool_prompt.py:757`

## `_single_document_id_from_tool_output` — function, line 5245
- **called from:**
- `src/agent_loop.py:34542`
- `tests/test_minimal_native_tool_prompt.py:763`
- `tests/test_minimal_native_tool_prompt.py:764`

## `_session_link_from_row` — function, line 5256
- **called from:**
- `src/agent_loop.py:5305`
- `tests/test_redos_core_parsers.py:147`

## `_session_list_summary_from_tool_output` — function, line 5288
- **called from:**
- `src/agent_loop.py:3333`
- `src/agent_loop.py:13920`
- `tests/test_agent_search_dedupe.py:77`
- `tests/test_minimal_native_tool_prompt.py:673`
- `tests/test_redos_core_parsers.py:160`

## `_registry_list_summary_from_tool_output` — function, line 5325
- **called from:**
- `src/agent_loop.py:13898`
- `src/agent_loop.py:13924`
- `tests/test_minimal_native_tool_prompt.py:696`

## `_research_listing_row` — function, line 5344
- **called from:**
- `src/agent_loop.py:5378`
- `tests/test_redos_core_parsers.py:532`

## `_research_list_summary_from_tool_output` — function, line 5366
- **called from:**
- `src/agent_loop.py:13922`
- `tests/test_minimal_native_tool_prompt.py:656`

## `_skill_listing_row` — function, line 5398
- **called from:**
- `src/agent_loop.py:5467`
- `tests/test_redos_core_parsers.py:534`

## `_skills_list_summary_from_tool_output` — function, line 5446
- **called from:**
- `src/agent_loop.py:13928`
- `src/agent_loop.py:36501`
- `src/agent_loop.py:38700`
- `tests/test_minimal_native_tool_prompt.py:603`
- `tests/test_skill_deeplink_static.py:43`

## `_calendar_detail_requested` — function, line 5508
- **called from:**
- `src/agent_loop.py:27296`
- `src/agent_loop.py:35467`
- `src/agent_loop.py:38684`
- `tests/test_minimal_native_tool_prompt.py:784`

## `_calendar_listing_row` — function, line 5521
- **called from:**
- `src/agent_loop.py:5613`
- `tests/test_redos_core_parsers.py:536`

## `_calendar_list_summary_from_tool_output` — function, line 5560
- **called from:**
- `src/agent_loop.py:13892`
- `src/agent_loop.py:27294`
- `src/agent_loop.py:35473`
- `src/agent_loop.py:38682`
- `src/clean_agent_preview.py:1032`
- `tests/test_minimal_native_tool_prompt.py:785`
- `tests/test_minimal_native_tool_prompt.py:786`
- `tests/test_minimal_native_tool_prompt.py:806`

## `format_when` — function, line 5578
- **called from:**
- `src/agent_loop.py:5625`

## `time_label` — function, line 5601
- **called from:**
- `src/agent_loop.py:5606`
- `src/agent_loop.py:5606`
- `src/agent_loop.py:5608`
- `src/agent_loop.py:5608`

## `_ordinal_weekday_monthly_rrule_from_text` — function, line 5677
- **called from:**
- `src/agent_loop.py:1586`
- `src/agent_loop.py:5722`

## `_ambiguous_ordinal_weekday_of_week` — function, line 5694
- **called from:**
- `src/agent_loop.py:5732`

## `_normalize_calendar_ordinal_weekday_rrule` — function, line 5709
- **called from:**
- `src/agent_loop.py:33826`
- `tests/test_minimal_native_tool_prompt.py:1075`
- `tests/test_minimal_native_tool_prompt.py:1091`
- `tests/test_minimal_native_tool_prompt.py:1103`

## `_calendar_ordinal_week_ask_user_block` — function, line 5731
- **called from:**
- `src/agent_loop.py:33668`
- `tests/test_minimal_native_tool_prompt.py:1087`

## `_normalize_calendar_list_range_args` — function, line 5750
- **called from:**
- `src/agent_loop.py:33816`
- `tests/test_minimal_native_tool_prompt.py:1000`
- `tests/test_minimal_native_tool_prompt.py:1016`

## `_week_bounds` — function, line 5778
- **called from:**
- `src/agent_loop.py:5796`
- `src/agent_loop.py:5798`

## `_day_bounds` — function, line 5782
- **called from:**
- `src/agent_loop.py:5800`
- `src/agent_loop.py:5802`

## `_calendar_bounds_for_prompt` — function, line 5837
- **called from:**
- `src/agent_loop.py:5817`
- `src/agent_loop.py:5929`
- `tests/test_tool_policy.py:2141`
- `tests/test_tui_round_cap.py:367`

## `_parse_simple_calendar_tool_request` — function, line 5884
- **called from:**
- `src/agent_loop.py:27181`
- `src/agent_loop.py:29157`
- `tests/test_tool_policy.py:2122`
- `tests/test_tool_policy.py:2131`
- `tests/test_tool_policy.py:2140`
- `tests/test_tool_policy.py:2146`
- `tests/test_tool_policy.py:2148`
- `tests/test_tool_policy.py:2152`
- `tests/test_tool_policy.py:2176`
- `tests/test_tool_policy.py:2187`
- `tests/test_tui_round_cap.py:358`
- `tests/test_tui_round_cap.py:413`

## `_parse_ambiguous_calendar_date_ask_user` — function, line 5958
- **called from:**
- `src/agent_loop.py:27139`
- `src/agent_loop.py:29162`
- `tests/test_calendar_ordinal_date_guard.py:10`
- `tests/test_calendar_ordinal_date_guard.py:16`
- `tests/test_tool_policy.py:2210`

## `_normalize_calendar_create_relative_args` — function, line 6009
- **called from:**
- `src/agent_loop.py:33821`
- `tests/test_minimal_native_tool_prompt.py:1038`
- `tests/test_minimal_native_tool_prompt.py:1123`

## `_strip_iso_timezone` — function, line 6045
- **called from:**
- `src/agent_loop.py:6070`
- `src/agent_loop.py:6079`

## `_parse_iso` — function, line 6114
- **called from:**
- `src/agent_loop.py:6125`
- `src/agent_loop.py:6141`

## `_recover_manage_email_tool_block` — function, line 6156
- **called from:**
- `src/agent_loop.py:15739`
- `src/agent_loop.py:15747`
- `src/agent_loop.py:15836`

## `_collapse_repeated_email_singletons` — function, line 6221
- **called from:**
- `src/agent_loop.py:15766`
- `src/agent_loop.py:15851`

## `_email_list_summary_from_tool_output` — function, line 6278
- **called from:**
- `src/agent_loop.py:13938`
- `src/agent_loop.py:13947`
- `src/agent_loop.py:38728`
- `tests/test_native_tool_result_threading.py:21`

## `_single_email_uid_from_tool_output` — function, line 6385
- **called from:**
- `src/agent_loop.py:35002`

## `_visible_response_text` — function, line 6397
- **called from:**
- `src/agent_loop.py:2235`
- `src/agent_loop.py:17265`
- `src/agent_loop.py:17312`
- `src/agent_loop.py:29600`
- `src/agent_loop.py:29652`
- `src/agent_loop.py:29707`
- `src/agent_loop.py:29748`
- `src/agent_loop.py:29766`
- `src/agent_loop.py:29779`
- `src/agent_loop.py:29792`
- `src/agent_loop.py:29805`
- `src/agent_loop.py:30659`
- `src/agent_loop.py:30756`
- `src/agent_loop.py:38059`
- `src/agent_loop.py:38139`
- `src/agent_loop.py:38217`
- `src/agent_loop.py:38424`
- `src/agent_loop.py:38542`
- `src/agent_loop.py:38584`
- `src/agent_loop.py:38639`
- `src/agent_loop.py:38673`
- `src/agent_loop.py:38680`
- `src/agent_loop.py:38691`
- `src/agent_loop.py:38698`
- `src/agent_loop.py:38705`
- `src/agent_loop.py:38714`
- `src/agent_loop.py:38721`
- `src/agent_loop.py:38733`
- `src/agent_loop.py:38739`
- `src/agent_loop.py:38747`
- `src/agent_loop.py:38767`
- `tests/test_minimal_native_tool_prompt.py:432`

## `_format_email_summary_item` — function, line 6411
- **called from:**
- `src/agent_loop.py:6363`
- `src/agent_loop.py:6376`

## `_email_subject_uid_pairs_from_tool_output` — function, line 6432
- **called from:**
- `src/agent_loop.py:6486`

## `flush_current` — function, line 6440
- **called from:**
- `src/agent_loop.py:6452`
- `src/agent_loop.py:6457`
- `src/agent_loop.py:6464`

## `_linkify_email_titles_from_tool_events` — function, line 6468
- **called from:**
- `src/agent_loop.py:38763`

## `_calendar_title_uid_pairs_from_tool_event` — function, line 6516
- **called from:**
- `src/agent_loop.py:6542`
- `src/agent_loop.py:6561`

## `add_pair` — function, line 6520
- **called from:**
- `src/agent_loop.py:4727`
- `src/agent_loop.py:4731`
- `src/agent_loop.py:6533`
- `src/agent_loop.py:6537`

## `_single_calendar_uid_from_tool_event` — function, line 6541
- **called from:**
- `src/agent_loop.py:35861`

## `_linkify_calendar_titles_from_tool_events` — function, line 6550
- **called from:**
- `src/agent_loop.py:38764`
- `tests/test_minimal_native_tool_prompt.py:819`

## `_has_successful_calendar_list_evidence` — function, line 6589
- **called from:**
- `src/agent_loop.py:31135`
- `src/agent_loop.py:31595`

## `_has_successful_calendar_tool_evidence` — function, line 6614
- **called from:**
- `src/agent_loop.py:1965`

## `_friendly_email_date` — function, line 6626
- **called from:**
- `src/agent_loop.py:6690`

## `_strip_terminal_delimited_value` — function, line 6641
- **called from:**
- `src/agent_loop.py:6667`
- `src/agent_loop.py:6668`
- `src/agent_loop.py:6676`

## `_email_sender_name` — function, line 6663
- **called from:**
- `src/agent_loop.py:6687`
- `tests/test_redos_core_parsers.py:350`

## `_email_account_label` — function, line 6672
- **called from:**
- `src/agent_loop.py:6693`
- `tests/test_redos_core_parsers.py:351`

## `_format_email_attachment_summary_item` — function, line 6679
- **called from:**
- `src/agent_loop.py:6369`

## `_email_attachment_list_requested` — function, line 6707
- **called from:**
- `src/agent_loop.py:13940`
- `src/agent_loop.py:13949`
- `src/agent_loop.py:38730`

## `_email_read_summary_from_tool_output` — function, line 6712
- **called from:**
- `src/agent_loop.py:6836`
- `src/agent_loop.py:13954`
- `src/agent_loop.py:35105`
- `src/agent_loop.py:38741`

## `_email_attachment_summary_from_tool_output` — function, line 6782
- **called from:**
- `src/agent_loop.py:6957`
- `src/agent_loop.py:13956`
- `src/agent_loop.py:38746`

## `_email_read_summaries_from_tool_events` — function, line 6829
- **called from:**
- `src/agent_loop.py:38520`

## `_strip_horizontal_space_before_lf` — function, line 6842
- **called from:**
- `src/agent_loop.py:6869`
- `tests/test_redos_core_parsers.py:358`

## `_email_read_evidence_from_tool_output` — function, line 6857
- **called from:**
- `src/agent_loop.py:38466`
- `tests/test_email_fact_lookup_completion.py:72`

## `_is_terse_email_lookup_followup` — function, line 6876
- **called from:**
- `src/agent_loop.py:6889`
- `src/agent_loop.py:6898`
- `tests/test_redos_core_parsers.py:550`

## `_email_lookup_request_from_messages` — function, line 6886
- **called from:**
- `src/agent_loop.py:38452`
- `tests/test_email_fact_lookup_completion.py:37`

## `_email_fact_lookup_requested` — function, line 6903
- **called from:**
- `src/agent_loop.py:6941`
- `tests/test_email_fact_lookup_completion.py:43`
- `tests/test_email_fact_lookup_completion.py:44`
- `tests/test_email_fact_lookup_completion.py:45`
- `tests/test_email_fact_lookup_completion.py:46`

## `_email_lookup_needs_post_synthesis` — function, line 6936
- **called from:**
- `src/agent_loop.py:38459`
- `tests/test_email_fact_lookup_completion.py:55`
- `tests/test_email_fact_lookup_completion.py:58`

## `_email_attachment_summaries_from_tool_events` — function, line 6950
- **called from:**
- `src/agent_loop.py:38521`

## `_email_compact_summary_from_read_summaries` — function, line 6963
- **called from:**
- `src/agent_loop.py:38633`

## `_email_summary_requested` — function, line 7024
- **called from:**
- `src/agent_loop.py:7036`
- `src/agent_loop.py:35574`
- `src/agent_loop.py:38632`

## `_email_count_requested` — function, line 7028
- **called from:**
- `src/agent_loop.py:7036`
- `src/agent_loop.py:13930`
- `src/agent_loop.py:35574`

## `_email_direct_listing_requested` — function, line 7032
- **called from:**
- `src/agent_loop.py:13936`
- `src/agent_loop.py:13945`

## `_email_urgent_summary_from_read_summaries` — function, line 7048
- **called from:**
- `src/agent_loop.py:38629`

## `_email_accounts_summary_from_tool_output` — function, line 7111
- **called from:**
- `src/agent_loop.py:13952`

## `_web_fetch_summary_from_tool_output` — function, line 7147
- **called from:**
- `src/agent_loop.py:13966`

## `_load_mcp_disabled_map` — function, line 7176
- **called from:**
- `routes/chat_routes.py:3837`
- `src/agent_loop.py:21467`
- `src/agent_loop.py:22660`
- `src/agent_loop.py:24853`

## `_mentions_workspace_script` — function, line 7511
- **called from:**
- `src/agent_loop.py:7606`
- `src/agent_loop.py:7949`
- `src/agent_loop.py:24380`
- `tests/test_redos_core_parsers.py:258`

## `_mentions_pdf_url` — function, line 7520
- **called from:**
- `routes/chat_routes.py:358`
- `src/agent_loop.py:7624`
- `tests/test_redos_core_parsers.py:259`
- `tests/test_redos_residual_python.py:121`

## `_blocked_network_recovery_tools` — function, line 7526
- **called from:**
- `src/agent_loop.py:24925`
- `src/agent_loop.py:26738`
- `tests/test_network_guard_recovery_routing.py:17`
- `tests/test_network_guard_recovery_routing.py:40`
- `tests/test_network_guard_recovery_routing.py:57`
- `tests/test_network_guard_recovery_routing.py:93`
- `tests/test_network_guard_recovery_routing.py:99`

## `_compact_native_route_tools` — function, line 7569
- **called from:**
- `src/agent_loop.py:24826`
- `tests/test_multilingual_domain_routing.py:18`
- `tests/test_multilingual_domain_routing.py:35`
- `tests/test_multilingual_domain_routing.py:40`
- `tests/test_multilingual_domain_routing.py:55`
- `tests/test_tool_index_multilingual_literal_hints.py:36`
- `tests/test_tool_policy.py:2808`
- `tests/test_workspace_artifact_tool_floor.py:116`
- `tests/test_workspace_artifact_tool_floor.py:144`
- `tests/test_workspace_artifact_tool_floor.py:167`
- `tests/test_workspace_artifact_tool_floor.py:172`
- `tests/test_workspace_artifact_tool_floor.py:185`
- `tests/test_workspace_artifact_tool_floor.py:196`
- `tests/test_workspace_artifact_tool_floor.py:210`
- `tests/test_workspace_artifact_tool_floor.py:225`
- `tests/test_workspace_artifact_tool_floor.py:578`
- `tests/test_workspace_artifact_tool_floor.py:718`
- `tests/test_workspace_artifact_tool_floor.py:731`
- `tests/test_workspace_artifact_tool_floor.py:749`
- `tests/test_workspace_artifact_tool_floor.py:834`
- `tests/test_workspace_artifact_tool_floor.py:846`
- `tests/test_workspace_artifact_tool_floor.py:923`
- `tests/test_workspace_artifact_tool_floor.py:934`

## `_compact_native_artifact_tools` — function, line 7898
- **called from:**
- `src/agent_loop.py:8022`
- `src/agent_loop.py:24938`
- `src/agent_loop.py:26798`
- `tests/test_tool_routing_audit.py:97`
- `tests/test_workspace_artifact_tool_floor.py:768`
- `tests/test_workspace_artifact_tool_floor.py:792`
- `tests/test_workspace_artifact_tool_floor.py:808`
- `tests/test_workspace_artifact_tool_floor.py:821`

## `_compact_native_media_analysis_tools` — function, line 7968
- **called from:**
- `src/agent_loop.py:24945`
- `tests/test_tool_policy.py:3451`
- `tests/test_tool_policy.py:3464`

## `_compact_native_artifact_schemas` — function, line 8002
- **called from:**
- `src/agent_loop.py:25912`
- `tests/test_tool_policy.py:3499`
- `tests/test_tool_policy.py:3559`

## `_specialize_inspect_media_schema` — function, line 8041
- **called from:**
- `src/agent_loop.py:8033`
- `tests/test_tool_policy.py:3525`

## `_web_only_route_tools` — function, line 8089
- **called from:**
- `src/agent_loop.py:23955`
- `src/agent_loop.py:26665`

## `_workspace_tools_disabled_for_owner` — function, line 8133
- **called from:**
- `routes/chat_routes.py:3828`
- `src/agent_loop.py:8151`
- `src/agent_loop.py:8167`

## `_workspace_tools_disabled_for_request` — function, line 8141
- **called from:**
- `src/agent_loop.py:21809`
- `tests/test_tool_policy.py:190`
- `tests/test_tool_policy.py:193`
- `tests/test_tool_policy.py:197`

## `_strip_workspace_tools_for_sft` — function, line 8154
- **called from:**
- `src/agent_loop.py:23628`
- `src/agent_loop.py:23769`
- `src/agent_loop.py:23890`
- `src/agent_loop.py:23911`
- `tests/test_core_agent_tool_floor.py:44`
- `tests/test_tool_policy.py:182`
- `tests/test_workspace_artifact_tool_floor.py:338`

## `_domain_rules_for_tools` — function, line 8173
- **called from:**
- `src/agent_loop.py:8533`
- `tests/test_api_call_integration_routing.py:69`
- `tests/test_tool_rag_contacts_domain.py:63`

## `get_builtin_overrides` — function, line 8459
- **called from:**
- `routes/skills_routes.py:380`
- `routes/skills_routes.py:412`
- `scripts/dump_agent_prompt.py:500`
- `src/agent_loop.py:8475`
- `src/agent_loop.py:14822`
- `src/agent_loop.py:23066`

## `_section_text` — function, line 8472
- **called from:**
- `src/agent_loop.py:8518`

## `_compact_tool_line` — function, line 8480
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_assemble_prompt` — function, line 8504
- **called from:**
- `src/agent_loop.py:8538`
- `src/agent_loop.py:15600`
- `src/agent_loop.py:15610`
- `src/agent_loop.py:15614`
- `tests/test_spawn_agent.py:60`
- `tests/test_spawn_agent.py:64`
- `tests/test_tool_policy.py:201`

## `_native_tool_route_key` — function, line 8582
- **called from:**
- `src/agent_loop.py:8587`
- `src/agent_loop.py:8598`

## `_native_tools_temporarily_disabled` — function, line 8586
- **called from:**
- `src/agent_loop.py:24801`

## `_disable_native_tools_temporarily` — function, line 8597
- **called from:**
- `src/agent_loop.py:27003`

## `_is_ollama_openai_compat_url` — function, line 8601
- **called from:**
- `scripts/dump_agent_prompt.py:90`
- `scripts/dump_agent_prompt.py:329`
- `src/agent_loop.py:8734`
- `src/llm_core.py:3156`
- `src/llm_core.py:3446`
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

## `_is_local_openai_compat_url` — function, line 8616
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_endpoint_lookup_keys` — function, line 8638
- **called from:**
- `scripts/dump_agent_prompt.py:77`
- `src/agent_loop.py:8684`
- `src/agent_loop.py:8776`
- `tests/test_tool_support_heuristic.py:171`
- `tests/test_tool_support_heuristic.py:177`

## `add` — function, line 8643
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3587`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3924`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2017 more (grep the name in repo)

## `_agent_route_tool_mode` — function, line 8662
- **called from:**
- `routes/chat_helpers.py:1525`
- `src/agent_loop.py:24776`
- `tests/test_model_tool_modes.py:118`
- `tests/test_model_tool_modes.py:121`
- `tests/test_tool_support_heuristic.py:224`
- `tests/test_tool_support_heuristic.py:229`

## `_configured_model_tool_surface_raw` — function, line 8749
- **called from:**
- `routes/chat_routes.py:3785`
- `src/agent_loop.py:8848`
- `src/agent_loop.py:21574`
- `src/agent_loop.py:21601`
- `src/agent_loop.py:21704`
- `src/agent_loop.py:21723`
- `src/agent_loop.py:24792`
- `src/clean_agent_preview.py:1458`
- `src/clean_agent_preview.py:1479`
- `src/clean_agent_preview.py:1526`
- `src/clean_agent_preview.py:1565`

## `_configured_model_tool_surface` — function, line 8839
- **called from:**
- `routes/chat_routes.py:3143`
- `src/agent_loop.py:24782`
- `tests/test_model_tool_modes.py:92`

## `_detect_admin_intent` — function, line 8851
- **called from:**
- `src/agent_loop.py:21993`
- `tests/test_agent_loop.py:399`
- `tests/test_agent_loop.py:402`
- `tests/test_agent_loop.py:405`
- `tests/test_agent_loop.py:408`
- `tests/test_agent_loop.py:411`
- `tests/test_agent_loop.py:414`
- `tests/test_agent_loop.py:417`
- `tests/test_agent_loop.py:420`
- `tests/test_agent_loop.py:423`
- `tests/test_agent_loop.py:426`
- `tests/test_agent_loop.py:429`
- `tests/test_agent_loop.py:432`
- `tests/test_agent_loop.py:435`
- `tests/test_agent_loop.py:440`
- `tests/test_agent_loop.py:443`
- `tests/test_agent_loop.py:446`
- `tests/test_agent_loop.py:449`
- `tests/test_agent_loop.py:454`
- `tests/test_agent_loop.py:457`
- `tests/test_agent_loop.py:464`
- `tests/test_agent_loop.py:470`
- `tests/test_agent_loop.py:479`

## `_extract_last_user_message` — function, line 8863
- **called from:**
- `src/agent_loop.py:8892`
- `src/agent_loop.py:10426`
- `src/agent_loop.py:11848`
- `src/agent_loop.py:13497`
- `src/agent_loop.py:13649`
- `src/agent_loop.py:13706`
- `src/agent_loop.py:14741`
- `src/agent_loop.py:15204`
- `src/agent_loop.py:15246`
- `src/agent_loop.py:21581`
- `src/agent_loop.py:21608`
- `src/agent_loop.py:21779`
- `src/agent_loop.py:21994`
- `src/agent_loop.py:32946`

## `_completion_verifier_request` — function, line 8877
- **called from:**
- `src/agent_loop.py:25375`
- `tests/test_completion_verifier_request.py:10`
- `tests/test_completion_verifier_request.py:19`

## `_message_content_text` — function, line 8895
- **called from:**
- `src/agent_loop.py:17744`
- `src/agent_loop.py:17772`
- `src/agent_loop.py:17910`
- `src/agent_loop.py:17934`
- `src/agent_loop.py:17957`
- `src/agent_loop.py:17993`
- `src/agent_loop.py:18092`
- `src/agent_loop.py:18177`
- `src/agent_loop.py:24650`
- `src/agent_loop.py:24730`
- `src/agent_loop.py:25048`

## `_user_turn_count` — function, line 8906
- **called from:**
- `src/agent_loop.py:22478`
- `tests/test_minimal_native_tool_prompt.py:425`

## `_insert_before_latest_user` — function, line 8923
- **called from:**
- `src/agent_loop.py:21990`
- `tests/test_agent_loop.py:169`
- `tests/test_agent_loop.py:188`

## `_uploaded_files_context_message` — function, line 8934
- **called from:**
- `src/agent_loop.py:21988`
- `tests/test_uploaded_file_read_routing.py:54`

## `_uploaded_file_read_only_turn` — function, line 8986
- **called from:**
- `src/agent_loop.py:21995`
- `tests/test_uploaded_file_read_routing.py:26`
- `tests/test_uploaded_file_read_routing.py:30`
- `tests/test_uploaded_file_read_routing.py:37`
- `tests/test_uploaded_file_read_routing.py:43`
- `tests/test_uploaded_file_read_routing.py:47`

## `_looks_like_workspace_coding_request` — function, line 9092
- **called from:**
- `routes/chat_routes.py:1208`
- `src/agent_loop.py:9248`
- `src/agent_loop.py:9297`
- `src/agent_loop.py:9435`
- `src/agent_loop.py:9606`
- `src/agent_loop.py:9744`
- `src/agent_loop.py:9853`
- `src/agent_loop.py:9856`
- `src/agent_loop.py:9879`
- `src/agent_loop.py:9881`
- `src/agent_loop.py:10113`
- `src/agent_loop.py:11206`
- `src/agent_loop.py:16771`
- `src/agent_loop.py:23206`
- `src/agent_loop.py:25653`
- `src/agent_loop.py:31167`
- `tests/test_tui_round_cap.py:519`

## `_looks_like_actionable_user_request` — function, line 9128
- **called from:**
- `src/agent_loop.py:31667`
- `tests/test_agent_rounds_exhausted.py:890`
- `tests/test_agent_rounds_exhausted.py:893`
- `tests/test_agent_rounds_exhausted.py:896`

## `_looks_like_unattended_clarification` — function, line 9139
- **called from:**
- `src/agent_loop.py:31373`
- `tests/test_failed_tool_completion_preamble.py:180`
- `tests/test_failed_tool_completion_preamble.py:181`
- `tests/test_failed_tool_completion_preamble.py:193`
- `tests/test_runtime_behavior_regressions.py:181`
- `tests/test_runtime_behavior_regressions.py:193`

## `_tui_read_only_inspection_turn` — function, line 9159
- **called from:**
- `src/agent_loop.py:24023`
- `tests/test_agent_rounds_exhausted.py:1492`
- `tests/test_agent_rounds_exhausted.py:1495`
- `tests/test_agent_rounds_exhausted.py:1498`

## `_looks_like_local_computer_request` — function, line 9186
- **called from:**
- `src/agent_loop.py:9285`
- `src/agent_loop.py:9581`
- `src/agent_loop.py:9663`
- `src/agent_loop.py:9704`
- `src/agent_loop.py:23209`
- `tests/test_tui_round_cap.py:196`

## `_is_explicit_local_network_request` — function, line 9197
- **called from:**
- `src/agent_loop.py:9407`
- `src/agent_loop.py:9564`
- `src/agent_loop.py:9577`
- `src/agent_loop.py:29282`
- `tests/test_client_tool_routing.py:60`
- `tests/test_client_tool_routing.py:63`
- `tests/test_client_tool_routing.py:66`

## `_looks_like_explicit_tui_personal_domain_request` — function, line 9241
- **called from:**
- `src/agent_loop.py:9561`
- `src/agent_loop.py:9574`
- `src/agent_loop.py:9740`
- `src/agent_loop.py:11212`
- `tests/test_tui_round_cap.py:852`
- `tests/test_tui_round_cap.py:868`
- `tests/test_tui_round_cap.py:878`
- `tests/test_tui_round_cap.py:897`
- `tests/test_tui_round_cap.py:907`
- `tests/test_tui_round_cap.py:958`

## `_looks_like_explicit_tui_app_or_external_request` — function, line 9251
- **called from:**
- `src/agent_loop.py:9563`
- `src/agent_loop.py:9576`
- `src/agent_loop.py:23210`
- `tests/test_tui_round_cap.py:788`
- `tests/test_tui_round_cap.py:920`
- `tests/test_tui_round_cap.py:948`

## `_is_host_bridge_failure_result` — function, line 9300
- **called from:**
- `src/agent_loop.py:26280`
- `src/agent_loop.py:34647`
- `tests/test_host_shell_polling.py:73`
- `tests/test_host_shell_polling.py:76`
- `tests/test_tui_round_cap.py:58`

## `_normalize_incomplete_shell_artifact_result` — function, line 9327
- **called from:**
- `src/agent_loop.py:34329`
- `tests/test_core_agent_tool_floor.py:69`
- `tests/test_core_agent_tool_floor.py:85`
- `tests/test_core_agent_tool_floor.py:88`

## `_host_bridge_failure_response` — function, line 9354
- **called from:**
- `src/agent_loop.py:26285`
- `src/agent_loop.py:26644`
- `src/agent_loop.py:30631`
- `tests/test_host_shell_polling.py:82`

## `_web_search_unavailable_for_turn` — function, line 9362
- **called from:**
- `src/agent_loop.py:23534`
- `tests/test_tool_policy.py:104`
- `tests/test_tool_policy.py:111`
- `tests/test_tool_policy.py:116`
- `tests/test_tui_round_cap.py:813`
- `tests/test_tui_round_cap.py:820`
- `tests/test_tui_round_cap.py:830`

## `_streamed_tool_markup_complete` — function, line 9438
- **called from:**
- `src/agent_loop.py:28290`
- `tests/test_streamed_tool_markup.py:11`
- `tests/test_streamed_tool_markup.py:12`

## `_streamed_tool_markup_starts` — function, line 9450
- **called from:**
- `src/agent_loop.py:9471`
- `src/agent_loop.py:28288`
- `src/agent_loop.py:28291`
- `tests/test_streamed_tool_markup.py:28`
- `tests/test_streamed_tool_markup.py:34`
- `tests/test_streamed_tool_markup.py:35`
- `tests/test_streamed_tool_markup.py:36`
- `tests/test_streamed_tool_markup.py:37`
- `tests/test_streamed_tool_markup.py:40`
- `tests/test_streamed_tool_markup.py:41`
- `tests/test_streamed_tool_markup.py:42`
- `tests/test_streamed_tool_markup.py:43`
- `tests/test_streamed_tool_markup.py:44`
- `tests/test_streamed_tool_markup.py:45`

## `_strip_incomplete_tool_markup_tail` — function, line 9466
- **called from:**
- `src/agent_loop.py:6407`
- `tests/test_streamed_tool_markup.py:29`

## `_tui_runtime_prefers_host_workspace` — function, line 9476
- **called from:**
- `src/agent_loop.py:9407`
- `src/agent_loop.py:9632`
- `src/agent_loop.py:14534`

## `_tui_host_bridge_is_usable` — function, line 9530
- **called from:**
- `src/agent_loop.py:9645`
- `src/agent_loop.py:15196`
- `src/agent_loop.py:21853`

## `_tui_turn_targets_local_workspace` — function, line 9547
- **called from:**
- `src/agent_loop.py:9409`
- `src/agent_loop.py:9632`
- `src/agent_loop.py:9712`
- `tests/test_agent_runtime_context.py:589`

## `_tui_local_workspace_turn` — function, line 9625
- **called from:**
- `src/agent_loop.py:9762`
- `src/agent_loop.py:24011`
- `src/agent_loop.py:24018`
- `src/agent_loop.py:25208`
- `src/agent_loop.py:25218`
- `src/agent_loop.py:25766`
- `src/agent_loop.py:29264`
- `src/agent_loop.py:29376`
- `tests/test_agent_runtime_context.py:502`
- `tests/test_tui_round_cap.py:656`
- `tests/test_tui_round_cap.py:789`
- `tests/test_tui_round_cap.py:797`
- `tests/test_tui_round_cap.py:853`
- `tests/test_tui_round_cap.py:869`
- `tests/test_tui_round_cap.py:879`
- `tests/test_tui_round_cap.py:888`
- `tests/test_tui_round_cap.py:898`
- `tests/test_tui_round_cap.py:908`
- `tests/test_tui_round_cap.py:921`
- `tests/test_tui_round_cap.py:949`
- `tests/test_tui_round_cap.py:959`

## `_tui_local_no_web_recovery_turn` — function, line 9639
- **called from:**
- `src/agent_loop.py:28384`
- `src/agent_loop.py:29824`

## `_tui_local_no_web_request_turn` — function, line 9667
- **called from:**
- `src/agent_loop.py:9766`

## `_tui_prebridge_local_workspace_request_turn` — function, line 9720
- **called from:**
- `src/agent_loop.py:9770`

## `_tui_local_tool_constrained_turn` — function, line 9756
- **called from:**
- `src/agent_loop.py:9801`
- `src/agent_loop.py:14743`
- `src/agent_loop.py:23999`
- `src/agent_loop.py:24026`

## `_should_use_workspace_toolset` — function, line 9777
- **called from:**
- `tests/test_workspace_domain_precedence.py:5`
- `tests/test_workspace_domain_precedence.py:13`
- `tests/test_workspace_domain_precedence.py:21`
- `tests/test_workspace_domain_precedence.py:29`

## `_route_tui_local_workspace_tools` — function, line 9794
- **called from:**
- `src/agent_loop.py:23622`
- `src/agent_loop.py:23763`
- `src/agent_loop.py:23800`
- `src/agent_loop.py:24005`
- `tests/test_agent_rounds_exhausted.py:1122`
- `tests/test_agent_runtime_context.py:473`
- `tests/test_agent_runtime_context.py:507`
- `tests/test_agent_runtime_context.py:530`
- `tests/test_agent_runtime_context.py:549`
- `tests/test_agent_runtime_context.py:566`
- `tests/test_tui_round_cap.py:615`
- `tests/test_tui_round_cap.py:634`
- `tests/test_tui_round_cap.py:661`
- `tests/test_tui_round_cap.py:670`
- `tests/test_tui_round_cap.py:680`
- `tests/test_tui_round_cap.py:691`
- `tests/test_tui_round_cap.py:703`
- `tests/test_tui_round_cap.py:714`
- `tests/test_tui_round_cap.py:734`
- `tests/test_tui_round_cap.py:751`
- `tests/test_tui_round_cap.py:768`
- `tests/test_tui_round_cap.py:858`
- `tests/test_tui_round_cap.py:964`

## `_tui_local_execution_allowlist` — function, line 9868
- **called from:**
- `src/agent_loop.py:9811`
- `src/agent_loop.py:10108`
- `src/agent_loop.py:28388`
- `src/agent_loop.py:29829`
- `tests/test_agent_runtime_context.py:597`

## `_failed_tool_round_limit` — function, line 9888
- **called from:**
- `src/agent_loop.py:37778`
- `tests/test_agent_runtime_context.py:11`
- `tests/test_agent_runtime_context.py:12`
- `tests/test_agent_runtime_context.py:13`
- `tests/test_agent_runtime_context.py:14`
- `tests/test_agent_runtime_context.py:18`

## `_tui_python_runner_setup` — function, line 9910
- **called from:**
- `src/agent_loop.py:9935`
- `src/agent_loop.py:10004`
- `tests/test_runtime_evidence_contract.py:538`

## `_tui_local_test_runner_command` — function, line 9916
- **called from:**
- `src/agent_loop.py:9963`
- `src/agent_loop.py:9979`
- `src/agent_loop.py:10033`
- `tests/test_runtime_evidence_contract.py:543`
- `tests/test_tui_round_cap.py:457`

## `_tui_explicit_full_test_request` — function, line 9943
- **called from:**
- `src/agent_loop.py:9980`
- `src/agent_loop.py:10032`
- `tests/test_tui_round_cap.py:489`
- `tests/test_tui_round_cap.py:490`

## `_tui_local_smoke_test_runner_command` — function, line 9961
- **called from:**
- `src/agent_loop.py:10034`
- `tests/test_tui_round_cap.py:477`

## `_tui_smoke_test_request` — function, line 9966
- **called from:**
- `tests/test_tui_round_cap.py:471`
- `tests/test_tui_round_cap.py:472`
- `tests/test_tui_round_cap.py:473`
- `tests/test_tui_round_cap.py:474`
- `tests/test_tui_round_cap.py:475`

## `_tui_local_test_runner_host_shell_content` — function, line 9977
- **called from:**
- `src/agent_loop.py:33600`
- `tests/test_tui_round_cap.py:485`
- `tests/test_tui_round_cap.py:486`
- `tests/test_tui_round_cap.py:487`

## `_tui_normalize_pytest_command` — function, line 9986
- **called from:**
- `src/agent_loop.py:33605`
- `tests/test_tui_round_cap.py:504`
- `tests/test_tui_round_cap.py:511`

## `_tui_local_fallback_shell_command` — function, line 10007
- **called from:**
- `src/agent_loop.py:10112`
- `src/agent_loop.py:10122`
- `src/agent_loop.py:25627`
- `src/agent_loop.py:29296`
- `src/agent_loop.py:29893`
- `src/agent_loop.py:29918`
- `src/agent_loop.py:29946`
- `src/agent_loop.py:29973`
- `src/agent_loop.py:30025`
- `src/agent_loop.py:30053`
- `src/agent_loop.py:33566`
- `src/agent_loop.py:33595`
- `src/agent_loop.py:33622`
- `tests/test_agent_runtime_context.py:607`
- `tests/test_agent_runtime_context.py:612`
- `tests/test_agent_runtime_context.py:618`
- `tests/test_tui_round_cap.py:220`
- `tests/test_tui_round_cap.py:226`
- `tests/test_tui_round_cap.py:445`
- `tests/test_tui_round_cap.py:514`
- `tests/test_tui_round_cap.py:525`
- `tests/test_tui_round_cap.py:571`

## `_tui_recover_invalid_local_tools` — function, line 10099
- **called from:**
- `src/agent_loop.py:29839`
- `tests/test_tui_round_cap.py:232`
- `tests/test_tui_round_cap.py:246`
- `tests/test_tui_round_cap.py:535`

## `_native_unattended_workspace_read_floor` — function, line 10131
- **called from:**
- `src/agent_loop.py:26688`
- `tests/test_native_unattended_workspace_floor.py:11`
- `tests/test_native_unattended_workspace_floor.py:22`
- `tests/test_native_unattended_workspace_floor.py:25`
- `tests/test_native_unattended_workspace_floor.py:35`
- `tests/test_native_unattended_workspace_floor.py:38`

## `_looks_like_malformed_tui_tool_call` — function, line 10162
- **called from:**
- `src/agent_loop.py:29913`
- `tests/test_tui_round_cap.py:268`
- `tests/test_tui_round_cap.py:271`
- `tests/test_tui_round_cap.py:274`

## `_tui_project_discovery_summary` — function, line 10176
- **called from:**
- `src/agent_loop.py:34474`
- `tests/test_tui_round_cap.py:582`

## `_tui_network_target_from_text` — function, line 10199
- **called from:**
- `src/agent_loop.py:10079`
- `src/agent_loop.py:34455`

## `_tui_network_summary` — function, line 10214
- **called from:**
- `src/agent_loop.py:34453`
- `tests/test_tui_round_cap.py:559`

## `_tui_normalize_network_host_command` — function, line 10238
- **called from:**
- `src/agent_loop.py:33544`
- `tests/test_tui_round_cap.py:200`
- `tests/test_tui_round_cap.py:213`

## `_tui_normalize_workspace_host_command` — function, line 10291
- **called from:**
- `src/agent_loop.py:33639`
- `tests/test_tui_round_cap.py:256`

## `_explicitly_references_missing_workspace` — function, line 10317
- **called from:**
- `src/agent_loop.py:9608`
- `src/agent_loop.py:22536`
- `tests/test_workspace_confine.py:443`

## `_local_computer_rules` — function, line 10345
- **called from:**
- `src/agent_loop.py:15218`

## `_workspace_coding_rules` — function, line 10360
- **called from:**
- `src/agent_loop.py:15209`
- `tests/test_tool_policy.py:3483`
- `tests/test_tui_round_cap.py:546`

## `_native_artifact_workspace_rules` — function, line 10389
- **called from:**
- `src/agent_loop.py:15199`
- `tests/test_tool_policy.py:3431`

## `_native_media_workspace_rules` — function, line 10401
- **called from:**
- `src/agent_loop.py:15207`
- `tests/test_tool_policy.py:3438`

## `_is_native_artifact_workspace_turn` — function, line 10415
- **called from:**
- `src/agent_loop.py:15198`
- `tests/test_tool_policy.py:3430`
- `tests/test_tool_policy.py:3482`

## `_strip_think_blocks` — function, line 10450
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
- `src/agent_loop.py:25719`
- `src/agent_loop.py:28681`
- `src/agent_loop.py:30506`
- `src/agent_loop.py:30609`
- `src/agent_loop.py:30618`
- `src/agent_loop.py:31237`
- `src/agent_loop.py:31370`
- `src/agent_loop.py:32248`
- `src/agent_loop.py:37689`
- `src/agent_loop.py:38060`
- `src/agent_loop.py:38140`
- `src/agent_loop.py:38507`
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

## `_is_explicit_continuation` — function, line 10531
- **called from:**
- `src/agent_loop.py:11125`
- `tests/test_redos_verdict_continuation.py:63`
- `tests/test_redos_verdict_continuation.py:70`

## `_is_action_continuation` — function, line 10536
- **called from:**
- `src/agent_loop.py:11010`
- `src/agent_loop.py:11128`
- `tests/test_agent_continuation_routing.py:20`

## `_is_self_contained_workspace_sequence` — function, line 10541
- **called from:**
- `src/agent_loop.py:11123`

## `_is_casual_low_signal` — function, line 10558
- **called from:**
- `routes/chat_helpers.py:1326`
- `src/agent_loop.py:10971`
- `src/agent_loop.py:11147`
- `src/agent_loop.py:12757`
- `src/agent_loop.py:17857`
- `src/agent_loop.py:22453`

## `_is_ambiguous_short_low_signal` — function, line 10574
- **called from:**
- `src/agent_loop.py:22452`
- `tests/test_boundary_tool_routing.py:66`
- `tests/test_boundary_tool_routing.py:67`
- `tests/test_boundary_tool_routing.py:68`
- `tests/test_minimal_native_tool_prompt.py:192`

## `_has_matching_skill_for_turn` — function, line 10599
- **called from:**
- `src/agent_loop.py:22468`

## `_extract_oversized_svg` — function, line 10649
- **called from:**
- `src/agent_loop.py:30710`
- `tests/test_builtin_skills.py:114`
- `tests/test_builtin_skills.py:115`

## `_boundary` — function, line 10660
- **called from:**
- `src/agent_loop.py:10665`
- `src/agent_loop.py:10674`
- `src/agent_loop.py:10683`

## `_should_use_direct_low_signal_path` — function, line 10703
- **called from:**
- `src/agent_loop.py:22496`
- `tests/test_minimal_native_tool_prompt.py:154`
- `tests/test_minimal_native_tool_prompt.py:155`
- `tests/test_minimal_native_tool_prompt.py:170`
- `tests/test_minimal_native_tool_prompt.py:186`

## `_is_contextual_retry_continuation` — function, line 10762
- **called from:**
- `src/agent_loop.py:11121`

## `_is_contextual_link_followup` — function, line 10777
- **called from:**
- `src/agent_loop.py:10843`
- `src/agent_loop.py:11122`
- `src/agent_loop.py:22457`
- `src/agent_loop.py:25130`
- `tests/test_minimal_native_tool_prompt.py:228`
- `tests/test_minimal_native_tool_prompt.py:248`
- `tests/test_minimal_native_tool_prompt.py:249`

## `_is_terse_link_request` — function, line 10827
- **called from:**
- `src/agent_loop.py:22456`
- `tests/test_minimal_native_tool_prompt.py:227`
- `tests/test_minimal_native_tool_prompt.py:247`
- `tests/test_redos_core_parsers.py:437`

## `_contextual_link_followup_topic` — function, line 10841
- **called from:**
- `src/agent_loop.py:25133`
- `tests/test_minimal_native_tool_prompt.py:229`

## `_assistant_requested_followup` — function, line 10870
- **called from:**
- `src/agent_loop.py:11131`

## `_domain_tools_from_previous_assistant_turn` — function, line 10956
- **called from:**
- `src/agent_loop.py:22389`
- `tests/test_tool_policy.py:1770`
- `tests/test_tool_policy.py:1802`
- `tests/test_tool_policy.py:1841`

## `_record` — function, line 10973
- **called from:**
- `src/agent_loop.py:10999`
- `src/agent_loop.py:11001`
- `src/agent_runtime/owned_resources.py:236`
- `src/agent_runtime/owned_resources.py:312`
- `src/agent_runtime/owned_resources.py:342`
- `src/agent_runtime/owned_resources.py:371`
- `src/model_capability_readers/llamacpp.py:306`
- `src/model_capability_readers/llamacpp.py:328`

## `_plain_content` — function, line 10986
- **called from:**
- `src/agent_loop.py:11006`

## `_has_explicit_local_path` — function, line 11104
- **called from:**
- `src/agent_loop.py:11146`
- `src/agent_loop.py:11223`

## `_classify_agent_request` — function, line 11112
- **called from:**
- `src/agent_loop.py:22388`
- `tests/test_agent_continuation_routing.py:18`
- `tests/test_agent_continuation_routing.py:33`
- `tests/test_agent_continuation_routing.py:42`
- `tests/test_agent_continuation_routing.py:50`
- `tests/test_agent_loop.py:152`
- `tests/test_api_call_integration_routing.py:52`
- `tests/test_api_call_integration_routing.py:58`
- `tests/test_api_call_integration_routing.py:76`
- `tests/test_bg_job_tools.py:183`
- `tests/test_bg_job_tools.py:196`
- `tests/test_boundary_tool_routing.py:7`
- `tests/test_boundary_tool_routing.py:58`
- `tests/test_config_file_settings_routing.py:38`
- `tests/test_config_file_settings_routing.py:54`
- `tests/test_config_file_settings_routing.py:62`
- `tests/test_implicit_notes_routing.py:11`
- `tests/test_implicit_notes_routing.py:17`
- `tests/test_local_fixture_domain_isolation.py:5`
- `tests/test_minimal_native_tool_prompt.py:200`
- `tests/test_minimal_native_tool_prompt.py:1246`
- `tests/test_minimal_native_tool_prompt.py:1290`
- `tests/test_multilingual_domain_routing.py:9`
- `tests/test_tool_policy.py:959`
- `tests/test_tool_policy.py:1957`
- `tests/test_tool_policy.py:2163`
- `tests/test_tool_policy.py:2313`
- `tests/test_tool_policy.py:2319`
- `tests/test_tool_policy.py:2341`
- `tests/test_tool_policy.py:2422`
- `tests/test_tool_policy.py:2562`
- `tests/test_tool_policy.py:3179`
- `tests/test_tool_rag_contacts_domain.py:26`

## `has` — function, line 11157
- **called from:**
- `src/agent_loop.py:11160`
- `src/agent_loop.py:11169`
- `src/agent_loop.py:11174`
- `src/agent_loop.py:11179`
- `src/agent_loop.py:11185`
- `src/agent_loop.py:11187`
- `src/agent_loop.py:11189`
- `src/agent_loop.py:11195`
- `src/agent_loop.py:11197`
- `src/agent_loop.py:11202`
- `src/agent_loop.py:11204`
- `src/agent_loop.py:11226`
- `src/agent_loop.py:11236`
- `src/agent_loop.py:11247`
- `src/agent_loop.py:11253`
- `src/agent_loop.py:11255`
- `src/agent_loop.py:11257`
- `src/agent_loop.py:11259`
- `src/agent_loop.py:11272`
- `src/agent_loop.py:11286`
- `src/agent_loop.py:11299`
- `src/agent_loop.py:11300`
- `src/agent_loop.py:11301`
- `src/agent_loop.py:11304`
- `src/agent_loop.py:11310`
- `src/agent_loop.py:11318`
- `src/agent_loop.py:11326`
- `static/app.js:3206`
- `static/app.js:3238`
- `static/js/admin.js:328`
- `static/js/admin.js:596`
- `static/js/admin.js:753`
- `static/js/admin.js:833`
- `static/js/admin.js:984`
- `static/js/admin.js:985`
- `static/js/admin.js:1073`
- `static/js/admin.js:1129`
- `static/js/admin.js:1631`
- `static/js/admin.js:1691`
- `static/js/admin.js:1692`
- `static/js/admin.js:2863`
- `static/js/admin.js:2884`
- `static/js/admin.js:3419`
- `static/js/assistant.js:167`
- `static/js/backgroundToolJobs.js:16`
- `static/js/backgroundToolJobs.js:60`
- `static/js/backgroundToolJobs.js:92`
- `static/js/calendar.js:1079`
- `static/js/calendar.js:1091`
- `static/js/calendar.js:1092`
- `static/js/calendar.js:1099`
- `static/js/calendar.js:1124`
- `static/js/calendar.js:1131`
- `static/js/calendar.js:1132`
- `static/js/calendar.js:1195`
- `static/js/calendar.js:2186`
- `static/js/calendar.js:2190`
- `static/js/calendar.js:2939`
- `static/js/calendar.js:2941`
- `static/js/calendar.js:2941`
- … +453 more (grep the name in repo)

## `_looks_like_explicit_notes_only_turn` — function, line 11339
- **called from:**
- `src/agent_loop.py:22443`
- `tests/test_implicit_notes_routing.py:12`
- `tests/test_implicit_notes_routing.py:18`
- `tests/test_minimal_native_tool_prompt.py:117`
- `tests/test_minimal_native_tool_prompt.py:123`
- `tests/test_minimal_native_tool_prompt.py:126`

## `_looks_like_implicit_notes_turn` — function, line 11353
- **called from:**
- `src/agent_loop.py:5066`
- `src/agent_loop.py:11177`
- `src/agent_loop.py:13587`
- `tests/test_implicit_notes_routing.py:10`
- `tests/test_implicit_notes_routing.py:23`

## `_clean_file_edit_value` — function, line 11370
- **called from:**
- `src/agent_loop.py:11400`
- `src/agent_loop.py:11401`
- `src/agent_loop.py:11402`
- `src/agent_loop.py:11433`
- `src/agent_loop.py:11469`
- `src/agent_loop.py:11470`
- `src/agent_loop.py:16828`
- `src/agent_loop.py:16840`
- `src/agent_loop.py:16873`

## `_parse_exact_file_replacement` — function, line 11378
- **called from:**
- `src/agent_loop.py:11411`
- `src/agent_loop.py:22560`

## `_looks_like_exact_file_replacement` — function, line 11410
- **called from:**
- `scripts/eval_exact_file_routing.py:113`
- `src/agent_loop.py:11308`
- `tests/test_exact_file_edit_routing.py:23`
- `tests/test_exact_file_edit_routing.py:46`

## `_parse_inspection_file_replacement` — function, line 11414
- **called from:**
- `src/agent_loop.py:22561`
- `tests/test_exact_file_edit_routing.py:75`
- `tests/test_exact_file_edit_routing.py:79`
- `tests/test_exact_file_edit_routing.py:85`

## `_reconcile_inspection_edit_with_read` — function, line 11476
- **called from:**
- `src/agent_loop.py:37662`
- `tests/test_exact_file_edit_routing.py:102`
- `tests/test_exact_file_edit_routing.py:121`

## `_minimal_native_tool_prompt` — function, line 11509
- **called from:**
- `tests/test_boundary_tool_routing.py:72`
- `tests/test_boundary_tool_routing.py:78`
- `tests/test_minimal_native_tool_prompt.py:91`
- `tests/test_minimal_native_tool_prompt.py:101`
- `tests/test_minimal_native_tool_prompt.py:108`

## `_turn_targets_active_document` — function, line 11556
- **called from:**
- `src/agent_loop.py:22479`
- `tests/test_agent_loop.py:68`
- `tests/test_agent_loop.py:82`
- `tests/test_agent_loop.py:88`

## `_active_document_mutation_requires_tool` — function, line 11637
- **called from:**
- `src/agent_loop.py:22481`

## `_has_successful_active_document_mutation` — function, line 11659
- **called from:**
- `src/agent_loop.py:31433`

## `_is_email_document_obj` — function, line 11671
- **called from:**
- `src/agent_loop.py:6207`
- `src/agent_loop.py:11650`
- `src/agent_loop.py:22139`
- `src/agent_loop.py:22230`
- `src/agent_loop.py:22249`
- `src/agent_loop.py:22486`
- `src/agent_loop.py:29165`
- `src/agent_loop.py:35210`

## `_minimal_saved_memory_message` — function, line 11683
- **called from:**
- `src/agent_loop.py:13547`
- `src/agent_loop.py:13660`
- `src/agent_loop.py:13718`

## `_resolved_tool_event_name` — function, line 11729
- **called from:**
- `src/agent_loop.py:1884`
- `src/agent_loop.py:1969`
- `src/agent_loop.py:1994`
- `src/agent_loop.py:2110`
- `src/agent_loop.py:2164`
- `src/agent_loop.py:4742`
- `src/agent_loop.py:5099`
- `src/agent_loop.py:6475`
- `src/agent_loop.py:6557`
- `src/agent_loop.py:6594`
- `src/agent_loop.py:6619`
- `src/agent_loop.py:6832`
- `src/agent_loop.py:6944`
- `src/agent_loop.py:6953`
- `src/agent_loop.py:11040`
- `src/agent_loop.py:11786`
- `src/agent_loop.py:11793`
- `src/agent_loop.py:11828`
- `src/agent_loop.py:11938`
- `src/agent_loop.py:11962`
- `src/agent_loop.py:12119`
- `src/agent_loop.py:12197`
- `src/agent_loop.py:12223`
- `src/agent_loop.py:12227`
- `src/agent_loop.py:12229`
- `src/agent_loop.py:12243`
- `src/agent_loop.py:12367`
- `src/agent_loop.py:12466`
- `src/agent_loop.py:12551`
- `src/agent_loop.py:12665`
- `src/agent_loop.py:12693`
- `src/agent_loop.py:12980`
- `src/agent_loop.py:13029`
- `src/agent_loop.py:13860`
- `src/agent_loop.py:14093`
- `src/agent_loop.py:17741`
- `src/agent_loop.py:17770`
- `src/agent_loop.py:19405`
- `src/agent_loop.py:28026`
- `src/agent_loop.py:29430`
- `src/agent_loop.py:31913`
- `src/agent_loop.py:32525`
- `src/agent_loop.py:35143`
- `src/agent_loop.py:35512`
- `src/agent_loop.py:35717`
- `src/agent_loop.py:35798`
- `src/agent_loop.py:36917`
- `src/agent_loop.py:36935`
- `src/agent_loop.py:38175`
- `src/agent_loop.py:38184`
- `src/agent_loop.py:38456`
- `src/agent_loop.py:38529`
- `src/agent_loop.py:38645`

## `_minimal_recent_notes_tool_context_message` — function, line 11741
- **called from:**
- `src/agent_loop.py:13664`
- `src/agent_loop.py:13722`
- `src/agent_loop.py:15223`
- `src/agent_loop.py:23658`
- `tests/test_minimal_native_tool_prompt.py:918`
- `tests/test_minimal_native_tool_prompt.py:1322`

## `_calendar_event_context_lines` — function, line 11792
- **called from:**
- `src/agent_loop.py:11841`

## `_has_recent_email_tool_context` — function, line 11917
- **called from:**
- `src/agent_loop.py:12754`
- `src/agent_loop.py:15222`

## `_latest_email_reference_from_recent_tool_context` — function, line 11948
- **called from:**
- `src/agent_loop.py:12084`
- `src/agent_loop.py:29574`
- `src/agent_loop.py:29656`
- `src/agent_loop.py:29751`

## `_recent_mentioned_email_reference` — function, line 11987
- **called from:**
- `src/agent_loop.py:29710`

## `_split_before_assistant_prompt` — function, line 12038
- **called from:**
- `src/agent_loop.py:12064`
- `tests/test_redos_core_parsers.py:355`

## `_suggested_reply_from_recent_assistant` — function, line 12051
- **called from:**
- `src/agent_loop.py:12081`

## `_reply_draft_confirmation_block_from_recent_context` — function, line 12077
- **called from:**
- `src/agent_loop.py:29415`

## `_email_account_selector_from_label` — function, line 12097
- **called from:**
- `src/agent_loop.py:12154`

## `_recent_spam_candidates_from_tool_context` — function, line 12105
- **called from:**
- `src/agent_loop.py:12281`
- `src/agent_loop.py:29087`

## `_contextual_spam_confirmation_action` — function, line 12165
- **called from:**
- `src/agent_loop.py:12276`
- `src/agent_loop.py:29451`
- `tests/test_tool_policy.py:3375`

## `_email_bulk_or_block_tool_succeeded` — function, line 12191
- **called from:**
- `src/agent_loop.py:12279`
- `src/agent_loop.py:29452`

## `_email_bulk_or_block_tool_attempted` — function, line 12214
- **called from:**
- `src/agent_loop.py:12279`

## `_tool_block_matches_event_args` — function, line 12226
- **called from:**
- `src/agent_loop.py:29437`
- `tests/test_tool_policy.py:3579`

## `_spam_action_success_summary` — function, line 12240
- **called from:**
- `src/agent_loop.py:29472`

## `_contextual_spam_confirmation_blocks` — function, line 12270
- **called from:**
- `src/agent_loop.py:29394`
- `tests/test_tool_policy.py:3376`
- `tests/test_tool_policy.py:3395`
- `tests/test_tool_policy.py:3404`

## `_looks_like_other_email_attachment_followup` — function, line 12346
- **called from:**
- `src/agent_loop.py:29550`

## `_recent_downloaded_attachment_uids` — function, line 12356
- **called from:**
- `src/agent_loop.py:12537`

## `_email_rows_from_list_output` — function, line 12378
- **called from:**
- `src/agent_loop.py:12413`
- `src/agent_loop.py:12468`
- `src/agent_loop.py:12553`

## `_email_bulk_blocks_from_search_output` — function, line 12406
- **called from:**
- `src/agent_loop.py:27506`
- `src/agent_loop.py:34982`
- `tests/test_agent_loop.py:138`

## `_named_email_row_from_recent_list_context` — function, line 12437
- **called from:**
- `src/agent_loop.py:12489`
- `src/agent_loop.py:29604`
- `src/agent_loop.py:29727`

## `_named_email_reference_from_recent_list_context` — function, line 12488
- **called from:**
- `src/agent_loop.py:29734`

## `_attachment_content_requested` — function, line 12498
- **called from:**
- `src/agent_loop.py:29731`

## `_email_read_and_attachment_blocks_from_row` — function, line 12508
- **called from:**
- `src/agent_loop.py:29732`

## `_alternate_email_attachment_blocks_from_recent_context` — function, line 12535
- **called from:**
- `src/agent_loop.py:29551`

## `_looks_like_email_body_followup` — function, line 12590
- **called from:**
- `src/agent_loop.py:29709`
- `src/agent_loop.py:29750`

## `_contextual_email_action_request` — function, line 12604
- **called from:**
- `src/agent_loop.py:12636`
- `src/agent_loop.py:12645`
- `src/agent_loop.py:29654`

## `_inherited_contextual_email_action_request` — function, line 12631
- **called from:**
- `src/agent_loop.py:29602`

## `_email_action_tool_succeeded` — function, line 12651
- **called from:**
- `src/agent_loop.py:29603`
- `src/agent_loop.py:29655`

## `_email_state_bulk_terminal_summary` — function, line 12689
- **called from:**
- `src/agent_loop.py:38522`

## `_looks_like_contextual_email_followup` — function, line 12753
- **called from:**
- `src/agent_loop.py:22429`

## `_recent_odysseus_anchor_refs` — function, line 12778
- **called from:**
- `src/agent_loop.py:2215`
- `src/agent_loop.py:2517`
- `src/agent_loop.py:5909`
- `src/agent_loop.py:13624`
- `src/agent_loop.py:29481`
- `src/agent_loop.py:33268`
- `src/agent_loop.py:33303`
- `src/agent_loop.py:33371`
- `src/agent_loop.py:33425`
- `src/agent_loop.py:33530`
- `src/agent_loop.py:33770`
- `src/agent_loop.py:33796`
- `tests/test_minimal_native_tool_prompt.py:1427`

## `_numbered_row_parenthesized_ids` — function, line 12855
- **called from:**
- `src/agent_loop.py:12994`
- `tests/test_redos_core_parsers.py:413`

## `_ordinal_collection_mutation_target` — function, line 12927
- **called from:**
- `src/agent_loop.py:33401`
- `src/agent_loop.py:33690`
- `tests/test_native_tool_result_threading.py:76`
- `tests/test_native_tool_result_threading.py:92`

## `_recent_odysseus_note_title` — function, line 13002
- **called from:**
- `src/agent_loop.py:33270`

## `_looks_like_recent_reference` — function, line 13047
- **called from:**
- `src/agent_loop.py:33250`
- `src/agent_loop.py:33300`
- `src/agent_loop.py:33368`
- `src/agent_loop.py:33422`
- `src/agent_loop.py:33527`
- `src/agent_loop.py:33766`
- `src/agent_loop.py:33793`

## `_user_named_explicit_title` — function, line 13062
- **called from:**
- `src/agent_loop.py:33252`
- `src/agent_loop.py:33301`
- `src/agent_loop.py:33423`
- `src/agent_loop.py:33768`
- `src/agent_loop.py:33794`

## `_extract_followup_content_update` — function, line 13066
- **called from:**
- `src/agent_loop.py:2522`
- `src/agent_loop.py:6210`
- `src/agent_loop.py:13118`
- `src/agent_loop.py:13278`
- `src/agent_loop.py:22138`
- `src/agent_loop.py:22228`
- `src/agent_loop.py:29164`
- `src/agent_loop.py:33271`
- `src/agent_loop.py:33309`
- `src/agent_loop.py:33376`
- `tests/test_tool_policy.py:216`

## `_active_email_reader_reply_body` — function, line 13098
- **called from:**
- `src/agent_loop.py:22061`
- `src/agent_loop.py:29183`

## `_email_reply_draft_requested` — function, line 13132
- **called from:**
- `src/agent_loop.py:11650`
- `src/agent_loop.py:13158`
- `src/agent_loop.py:29573`
- `src/agent_loop.py:35083`
- `src/agent_loop.py:35488`

## `_email_reply_suggestion_requested` — function, line 13148
- **called from:**
- `src/agent_loop.py:35488`
- `src/agent_loop.py:35493`

## `_email_send_requested` — function, line 13156
- **called from:**
- `src/agent_loop.py:35013`
- `src/agent_loop.py:35035`
- `src/agent_loop.py:35120`

## `_email_immediate_send_requested` — function, line 13170
- **called from:**
- `src/agent_loop.py:3529`
- `src/agent_loop.py:33127`
- `src/agent_loop.py:33142`
- `src/agent_loop.py:33155`
- `src/agent_loop.py:33172`
- `src/agent_loop.py:35038`
- `src/agent_loop.py:35043`
- `src/agent_loop.py:35066`
- `tests/test_tool_policy.py:2892`
- `tests/test_tool_policy.py:2893`
- `tests/test_tool_policy.py:2894`
- `tests/test_tool_policy.py:2895`
- `tests/test_tool_policy.py:2900`

## `_email_draft_review_requested` — function, line 13182
- **called from:**
- `src/agent_loop.py:33143`
- `src/agent_loop.py:33173`
- `tests/test_tool_policy.py:2901`

## `_email_mutation_forbidden` — function, line 13204
- **called from:**
- `src/agent_loop.py:32825`
- `src/agent_loop.py:33895`
- `tests/test_tool_policy.py:2915`
- `tests/test_tool_policy.py:2917`
- `tests/test_tool_policy.py:2918`
- `tests/test_tool_policy.py:2919`
- `tests/test_tool_policy.py:2923`
- `tests/test_tool_policy.py:2927`

## `_send_recipient_name_from_request` — function, line 13248
- **called from:**
- `src/agent_loop.py:35121`

## `_contact_lookup_did_not_resolve_email` — function, line 13264
- **called from:**
- `src/agent_loop.py:35122`

## `_email_reply_body_from_request` — function, line 13277
- **called from:**
- `src/agent_loop.py:29580`
- `src/agent_loop.py:35074`
- `src/agent_loop.py:35097`

## `_is_generic_email_reply_body` — function, line 13286
- **called from:**
- `src/agent_loop.py:33577`

## `_contextual_summary_fragment` — function, line 13299
- **called from:**
- `src/agent_loop.py:13374`
- `tests/test_redos_core_parsers.py:446`
- `tests/test_redos_core_parsers.py:486`

## `_contextual_email_subject` — function, line 13316
- **called from:**
- `src/agent_loop.py:13371`
- `tests/test_codeql_induced_redos.py:82`

## `_contextual_reply_body_from_recent_email_context` — function, line 13348
- **called from:**
- `src/agent_loop.py:33578`

## `_clean_fragment` — function, line 13362
- **called from:**
- `src/agent_loop.py:13369`
- `src/agent_loop.py:13373`
- `src/agent_loop.py:13376`

## `_email_uid_from_read_context` — function, line 13393
- **called from:**
- `src/agent_loop.py:35049`
- `src/agent_loop.py:35084`

## `_email_folder_from_read_context` — function, line 13407
- **called from:**
- `src/agent_loop.py:35073`
- `src/agent_loop.py:35095`

## `_build_active_email_draft_reply_content` — function, line 13417
- **called from:**
- `src/agent_loop.py:6213`
- `src/agent_loop.py:22154`
- `src/agent_loop.py:29176`

## `_extract_followup_location_update` — function, line 13436
- **called from:**
- `src/agent_loop.py:33772`
- `src/agent_loop.py:33801`

## `_extract_followup_prompt_update` — function, line 13443
- **called from:**
- `src/agent_loop.py:33377`
- `src/agent_loop.py:33436`

## `_compact_email_draft_context` — function, line 13456
- **called from:**
- `src/agent_loop.py:14929`

## `_minimal_odysseus_doc_messages` — function, line 13491
- **called from:**
- `src/agent_loop.py:25086`
- `tests/test_external_context_tool_gate.py:557`

## `_looks_like_notes_turn` — function, line 13579
- **called from:**
- `src/agent_loop.py:23655`

## `_looks_like_notes_calendar_followup` — function, line 13590
- **called from:**
- `src/agent_loop.py:23657`

## `_contextual_calendar_action_request` — function, line 13599
- **called from:**
- `src/agent_loop.py:29480`
- `src/agent_loop.py:35860`
- `tests/test_minimal_native_tool_prompt.py:1135`
- `tests/test_minimal_native_tool_prompt.py:1136`
- `tests/test_minimal_native_tool_prompt.py:1137`

## `_calendar_context_owns_ambiguous_mutation` — function, line 13610
- **called from:**
- `src/agent_loop.py:31424`
- `tests/test_tui_round_cap.py:380`
- `tests/test_tui_round_cap.py:393`

## `_looks_like_explicit_email_action_turn` — function, line 13633
- **called from:**
- `src/agent_loop.py:12759`
- `src/agent_loop.py:22428`

## `_minimal_odysseus_notes_messages` — function, line 13643
- **called from:**
- `src/agent_loop.py:25093`

## `_minimal_datetime_context_message` — function, line 13674
- **called from:**
- `src/agent_loop.py:13667`
- `src/agent_loop.py:13725`

## `_looks_like_memory_identity_turn` — function, line 13690
- **called from:**
- `src/agent_loop.py:22387`
- `src/agent_loop.py:22714`
- `src/agent_loop.py:22749`
- `src/agent_loop.py:25124`

## `_minimal_odysseus_general_messages` — function, line 13704
- **called from:**
- `src/agent_loop.py:22712`
- `src/agent_loop.py:22747`
- `src/agent_loop.py:25122`

## `_strip_doc_model_artifacts` — function, line 13741
- **called from:**
- `src/agent_loop.py:14269`
- `src/agent_loop.py:27988`
- `src/agent_loop.py:28273`

## `_normalize_ody_qwen_text_artifacts` — function, line 13780
- **called from:**
- `src/agent_loop.py:30757`
- `src/agent_loop.py:35510`
- `src/agent_loop.py:38223`
- `tests/test_minimal_native_tool_prompt.py:535`
- `tests/test_tool_policy.py:232`
- `tests/test_tool_policy.py:233`
- `tests/test_tui_round_cap.py:553`

## `_looks_like_ody_qwen_leaked_tool_text` — function, line 13828
- **called from:**
- `src/agent_loop.py:30665`
- `src/agent_loop.py:36982`
- `tests/test_redos_core_parsers.py:310`
- `tests/test_tool_policy.py:236`

## `_contains_email_draft_headers` — function, line 13846
- **called from:**
- `src/agent_loop.py:13915`
- `tests/test_redos_core_parsers.py:537`

## `_ody_qwen_terminal_tool_summary` — function, line 13858
- **called from:**
- `src/agent_loop.py:577`
- `src/agent_loop.py:17302`
- `src/agent_loop.py:17308`
- `src/agent_loop.py:26444`
- `src/agent_loop.py:27610`
- `src/agent_loop.py:35456`
- `src/agent_loop.py:36514`
- `src/agent_loop.py:36539`
- `src/agent_loop.py:37096`
- `src/agent_loop.py:38617`
- `tests/test_minimal_native_tool_prompt.py:447`
- `tests/test_minimal_native_tool_prompt.py:685`
- `tests/test_minimal_native_tool_prompt.py:728`
- `tests/test_minimal_native_tool_prompt.py:739`
- `tests/test_minimal_native_tool_prompt.py:990`
- `tests/test_tool_policy.py:2071`
- `tests/test_tool_policy.py:2402`
- `tests/test_tool_policy.py:3145`
- `tests/test_tui_round_cap.py:437`
- `tests/test_tui_round_cap.py:596`
- `tests/test_tui_round_cap.py:605`

## `_tui_verified_coding_summary` — function, line 14088
- **called from:**
- `src/agent_loop.py:14129`
- `src/agent_loop.py:36911`
- `tests/test_minimal_native_tool_prompt.py:492`

## `_tui_coding_failure_summary` — function, line 14126
- **called from:**
- `src/agent_loop.py:28031`
- `tests/test_minimal_native_tool_prompt.py:518`

## `_looks_like_destructive_request` — function, line 14148
- **called from:**
- `src/agent_loop.py:38232`
- `tests/test_redos_core_parsers.py:436`

## `_looks_like_success_claim` — function, line 14170
- **called from:**
- `src/agent_loop.py:38233`

## `_latest_email_action_needs_followup` — function, line 14174
- **called from:**
- `src/agent_loop.py:37059`

## `_parse_qwen_task_mutation_request` — function, line 14194
- **called from:**
- `src/agent_loop.py:35395`
- `tests/test_minimal_native_tool_prompt.py:570`
- `tests/test_minimal_native_tool_prompt.py:571`
- `tests/test_minimal_native_tool_prompt.py:572`
- `tests/test_minimal_native_tool_prompt.py:573`

## `_single_task_id_from_manage_tasks_list` — function, line 14206
- **called from:**
- `src/agent_loop.py:35396`
- `tests/test_minimal_native_tool_prompt.py:575`
- `tests/test_minimal_native_tool_prompt.py:579`

## `_normalize_truncated_document_tool_fences` — function, line 14233
- **called from:**
- `src/agent_loop.py:14268`

## `_normalize_stream_document_fences` — function, line 14260
- **called from:**
- `src/agent_loop.py:28376`
- `tests/test_odysseus_doc_fence_normalization.py:8`
- `tests/test_odysseus_doc_fence_normalization.py:23`
- `tests/test_odysseus_doc_fence_normalization.py:33`

## `repl` — function, line 14272
- **called from:**
- `src/text_helpers.py:111`

## `_document_stream_events` — function, line 14296
- **called from:**
- `src/agent_loop.py:26186`
- `src/agent_loop.py:34733`
- `tests/test_external_context_tool_gate.py:1533`

## `_recent_context_for_retrieval` — function, line 14329
- **called from:**
- `src/agent_loop.py:10773`
- `src/agent_loop.py:11135`
- `src/agent_loop.py:22404`
- `src/agent_loop.py:22423`
- `src/agent_loop.py:22437`
- `tests/test_tool_output_prompt_injection.py:89`

## `_strip_agent_injected_messages` — function, line 14358
- **called from:**
- `src/agent_loop.py:24951`
- `tests/test_user_time.py:239`

## `_prepend_agent_directive` — function, line 14373
- **called from:**
- `src/agent_loop.py:25083`
- `src/agent_loop.py:25134`
- `src/agent_loop.py:25139`
- `src/agent_loop.py:25144`
- `src/agent_loop.py:25160`
- `src/agent_loop.py:25169`
- `src/agent_loop.py:25181`
- `src/agent_loop.py:25190`
- `src/agent_loop.py:25217`
- `src/agent_loop.py:25223`
- `src/agent_loop.py:25225`
- `src/agent_loop.py:25227`
- `src/agent_loop.py:25229`
- `src/agent_loop.py:25231`
- `src/agent_loop.py:25233`

## `_tui_runtime_directive` — function, line 14388
- **called from:**
- `src/agent_loop.py:25215`
- `tests/test_agent_runtime_context.py:320`
- `tests/test_agent_runtime_context.py:330`

## `_tui_read_only_inspection_directive` — function, line 14418
- **called from:**
- `src/agent_loop.py:25225`
- `tests/test_agent_rounds_exhausted.py:1503`

## `_tui_local_network_directive` — function, line 14430
- **called from:**
- `src/agent_loop.py:25227`
- `tests/test_agent_rounds_exhausted.py:1506`

## `_tui_local_workspace_directive` — function, line 14444
- **called from:**
- `src/agent_loop.py:25223`
- `tests/test_agent_rounds_exhausted.py:1510`

## `_substantive_answer_after_failed_tools` — function, line 14469
- **called from:**
- `src/agent_loop.py:36832`
- `tests/test_agent_rounds_exhausted.py:1584`
- `tests/test_agent_rounds_exhausted.py:1590`
- `tests/test_agent_rounds_exhausted.py:1591`
- `tests/test_failed_tool_completion_preamble.py:17`
- `tests/test_failed_tool_completion_preamble.py:38`
- `tests/test_failed_tool_completion_preamble.py:48`
- `tests/test_failed_tool_completion_preamble.py:62`
- `tests/test_failed_tool_completion_preamble.py:74`
- `tests/test_failed_tool_completion_preamble.py:86`
- `tests/test_failed_tool_completion_preamble.py:104`

## `_is_tool_preamble` — function, line 14493
- **called from:**
- `src/agent_loop.py:14485`
- `src/agent_loop.py:17958`
- `src/agent_loop.py:18178`
- `src/agent_loop.py:19511`
- `src/agent_loop.py:19518`
- `src/agent_loop.py:30790`
- `src/agent_loop.py:38382`
- `tests/test_agent_search_dedupe.py:42`
- `tests/test_agent_search_dedupe.py:43`
- `tests/test_agent_search_dedupe.py:44`
- `tests/test_failed_tool_completion_preamble.py:14`
- `tests/test_failed_tool_completion_preamble.py:22`
- `tests/test_failed_tool_completion_preamble.py:34`
- `tests/test_failed_tool_completion_preamble.py:47`
- `tests/test_failed_tool_completion_preamble.py:58`
- `tests/test_failed_tool_completion_preamble.py:71`
- `tests/test_failed_tool_completion_preamble.py:83`
- `tests/test_failed_tool_completion_preamble.py:92`
- `tests/test_failed_tool_completion_preamble.py:101`
- `tests/test_failed_tool_completion_preamble.py:114`
- `tests/test_failed_tool_completion_preamble.py:137`
- `tests/test_tool_policy.py:2081`
- `tests/test_tool_policy.py:2084`

## `_tui_broad_host_read_reason` — function, line 14527
- **called from:**
- `src/agent_loop.py:33908`
- `tests/test_agent_rounds_exhausted.py:1532`
- `tests/test_agent_rounds_exhausted.py:1546`
- `tests/test_agent_rounds_exhausted.py:1551`
- `tests/test_agent_rounds_exhausted.py:1556`
- `tests/test_agent_rounds_exhausted.py:1561`

## `_tui_host_command_text` — function, line 14557
- **called from:**
- `src/agent_loop.py:10257`
- `src/agent_loop.py:14049`
- `src/agent_loop.py:14539`
- `src/agent_loop.py:14583`
- `src/agent_loop.py:15874`
- `src/agent_loop.py:20093`
- `src/agent_loop.py:33047`
- `src/agent_loop.py:33560`
- `src/agent_loop.py:33588`
- `src/agent_loop.py:36315`

## `_tui_bounded_host_read_command` — function, line 14575
- **called from:**
- `src/agent_loop.py:33915`
- `tests/test_agent_rounds_exhausted.py:1526`
- `tests/test_agent_rounds_exhausted.py:1569`
- `tests/test_agent_rounds_exhausted.py:1572`
- `tests/test_agent_rounds_exhausted.py:1578`
- `tests/test_agent_rounds_exhausted.py:1579`

## `_is_odysseus_qwen_model` — function, line 14623
- **called from:**
- `src/agent_loop.py:22046`
- `src/agent_loop.py:22519`
- `src/agent_loop.py:22740`
- `src/agent_loop.py:23636`
- `src/agent_loop.py:24973`
- `src/agent_loop.py:26983`
- `src/agent_loop.py:37148`

## `_is_odysseus_qwen_native` — function, line 14630
- **called from:**
- `tests/test_qwen_native_model_family.py:20`
- `tests/test_qwen_native_model_family.py:37`

## `_is_deepseek_flash_vision_model` — function, line 14636
- **called from:**
- `src/agent_loop.py:26919`
- `tests/test_agent_evidence_loop.py:52`
- `tests/test_agent_evidence_loop.py:53`
- `tests/test_agent_evidence_loop.py:54`
- `tests/test_agent_evidence_loop.py:55`

## `_deepseek_flash_visual_continuation` — function, line 14642
- **called from:**
- `src/agent_loop.py:26920`
- `tests/test_agent_evidence_loop.py:41`
- `tests/test_agent_evidence_loop.py:46`

## `_ody_qwen_temperature_cap` — function, line 14706
- **called from:**
- `src/agent_loop.py:22054`
- `src/agent_loop.py:22759`
- `src/agent_loop.py:26982`

## `_build_system_prompt` — function, line 14719
- **called from:**
- `scripts/dump_agent_prompt.py:153`
- `src/agent_loop.py:25014`
- `tests/test_agent_runtime_context.py:679`
- `tests/test_agent_runtime_context.py:1250`
- `tests/test_contract_prompt_conversation.py:33`
- `tests/test_contract_prompt_conversation.py:48`
- `tests/test_contract_prompt_conversation.py:61`
- `tests/test_minimal_native_tool_prompt.py:471`
- `tests/test_private_browser_tool.py:450`
- `tests/test_prompt_injection_audit.py:82`
- `tests/test_prompt_injection_audit.py:102`
- `tests/test_prompt_injection_audit.py:123`
- `tests/test_prompt_injection_audit.py:151`
- `tests/test_prompt_injection_audit.py:170`
- `tests/test_prompt_injection_audit.py:189`
- `tests/test_prompt_injection_audit.py:216`
- `tests/test_prompt_injection_audit.py:236`
- `tests/test_prompt_injection_audit.py:255`
- `tests/test_skill_index_prompt_injection.py:123`
- `tests/test_skill_index_prompt_injection.py:152`
- `tests/test_skill_index_prompt_injection.py:186`
- `tests/test_skill_index_prompt_injection.py:190`
- `tests/test_tool_policy.py:1694`
- `tests/test_user_time.py:200`
- `tests/test_user_time.py:230`
- `tests/test_workspace_confine.py:469`

## `_active_skill_is_eligible` — function, line 15308
- **called from:**
- `src/agent_loop.py:15323`

## `_build_base_prompt` — function, line 15556
- **called from:**
- `src/agent_loop.py:14831`
- `src/agent_loop.py:14839`

## `_resolve_tool_blocks` — function, line 15668
- **called from:**
- `src/agent_loop.py:28395`
- `tests/test_agent_rounds_exhausted.py:912`
- `tests/test_agent_rounds_exhausted.py:926`
- `tests/test_fenced_example_not_executed_for_native_models.py:194`
- `tests/test_fenced_example_not_executed_for_native_models.py:201`
- `tests/test_fenced_example_not_executed_for_native_models.py:212`
- `tests/test_fenced_example_not_executed_for_native_models.py:259`
- `tests/test_fenced_example_not_executed_for_native_models.py:300`
- `tests/test_fenced_example_not_executed_for_native_models.py:315`
- `tests/test_fenced_example_not_executed_for_native_models.py:333`
- `tests/test_fenced_example_not_executed_for_native_models.py:340`
- `tests/test_fenced_example_not_executed_for_native_models.py:355`
- `tests/test_fenced_example_not_executed_for_native_models.py:484`
- `tests/test_fenced_example_not_executed_for_native_models.py:497`
- `tests/test_fenced_example_not_executed_for_native_models.py:516`
- `tests/test_fenced_example_not_executed_for_native_models.py:531`
- `tests/test_fenced_example_not_executed_for_native_models.py:555`
- `tests/test_fenced_example_not_executed_for_native_models.py:575`
- `tests/test_fenced_example_not_executed_for_native_models.py:592`
- `tests/test_fenced_example_not_executed_for_native_models.py:605`
- `tests/test_fenced_example_not_executed_for_native_models.py:628`
- `tests/test_native_tool_result_threading.py:102`

## `_tool_block_content_key` — function, line 15685
- **called from:**
- `src/agent_loop.py:15752`

## `_recover_shell_wrapped_file_tool` — function, line 15869
- **called from:**
- `src/agent_loop.py:28797`
- `tests/test_agent_evidence_loop.py:744`
- `tests/test_agent_evidence_loop.py:753`
- `tests/test_agent_evidence_loop.py:762`
- `tests/test_agent_evidence_loop.py:782`

## `_recover_adjacent_fenced_write_file` — function, line 15939
- **called from:**
- `src/agent_loop.py:28634`
- `tests/test_agent_evidence_loop.py:786`
- `tests/test_agent_evidence_loop.py:806`
- `tests/test_agent_evidence_loop.py:824`

## `_recover_fenced_media_shell_command` — function, line 15983
- **called from:**
- `src/agent_loop.py:28639`
- `tests/test_agent_evidence_loop.py:838`
- `tests/test_agent_evidence_loop.py:853`
- `tests/test_agent_evidence_loop.py:862`

## `_normalize_required_artifact_write_paths` — function, line 16022
- **called from:**
- `src/agent_loop.py:28809`
- `tests/test_agent_rounds_exhausted.py:3594`

## `_artifact_lock_key` — function, line 16079
- **called from:**
- `src/agent_loop.py:16084`
- `src/agent_loop.py:16085`
- `src/agent_loop.py:16128`
- `src/agent_loop.py:16143`
- `src/agent_loop.py:16196`

## `_metric_lock_matches` — function, line 16083
- **called from:**
- `src/agent_loop.py:16190`
- `src/agent_loop.py:16208`

## `_resolved_value_locks_from_tool_events` — function, line 16095
- **called from:**
- `src/agent_loop.py:16177`
- `src/agent_loop.py:37352`

## `_normalize_csv_write_body_from_resolved_tool_evidence` — function, line 16171
- **called from:**
- `src/agent_loop.py:16062`
- `src/agent_loop.py:16068`

## `_append_tool_results` — function, line 16225
- **called from:**
- `src/agent_loop.py:26396`
- `src/agent_loop.py:37138`
- `src/agent_loop.py:38363`
- `tests/test_agent_external_tool_schemas.py:287`
- `tests/test_agent_external_tool_schemas.py:305`
- `tests/test_agent_loop.py:627`
- `tests/test_agent_loop.py:643`
- `tests/test_agent_loop.py:651`
- `tests/test_agent_loop.py:660`
- `tests/test_agent_loop.py:685`
- `tests/test_agent_loop.py:698`
- `tests/test_approved_replay_message_shape.py:27`
- `tests/test_external_context_tool_gate.py:525`
- `tests/test_external_context_tool_gate.py:822`
- `tests/test_inspect_media_tool.py:1986`
- `tests/test_inspect_media_tool.py:2015`
- `tests/test_inspect_media_tool.py:2062`
- `tests/test_inspect_media_tool.py:2080`
- `tests/test_inspect_media_tool.py:2089`
- `tests/test_inspect_media_tool.py:2098`
- `tests/test_inspect_media_tool.py:2122`
- `tests/test_llm_core_sanitize_tool_calls.py:48`
- `tests/test_native_tool_result_threading.py:112`
- `tests/test_temporal_grounding_stamps.py:75`
- `tests/test_temporal_grounding_stamps.py:130`
- `tests/test_temporal_grounding_stamps.py:178`
- `tests/test_tool_output_prompt_injection.py:49`
- `tests/test_tool_output_prompt_injection.py:79`
- `tests/test_tool_output_prompt_injection.py:106`

## `_compact_web_search_tool_text_for_model` — function, line 16542
- **called from:**
- `src/agent_loop.py:36413`
- `src/agent_loop.py:38343`

## `_compute_final_metrics` — function, line 16580
- **called from:**
- `src/agent_loop.py:28616`
- `src/agent_loop.py:38798`
- `tests/test_agent_loop.py:509`
- `tests/test_agent_loop.py:516`
- `tests/test_agent_loop.py:526`
- `tests/test_agent_loop.py:533`
- `tests/test_agent_loop.py:537`
- `tests/test_agent_loop.py:544`
- `tests/test_agent_loop.py:551`
- `tests/test_agent_loop.py:556`
- `tests/test_agent_loop.py:564`
- `tests/test_agent_loop.py:568`
- `tests/test_agent_loop.py:572`
- `tests/test_agent_loop.py:576`
- `tests/test_agent_loop.py:580`
- `tests/test_agent_loop.py:596`
- `tests/test_agent_loop.py:606`
- `tests/test_chat_metrics.py:198`
- `tests/test_cost_tracking.py:98`

## `_usage_bucket` — function, line 16690
- **called from:**
- `src/agent_loop.py:22688`
- `src/agent_loop.py:22776`
- `src/agent_loop.py:22990`
- `src/agent_loop.py:27118`
- `src/agent_loop.py:28530`
- `src/agent_loop.py:30669`
- `src/agent_loop.py:32711`

## `_usage_bucket_summary` — function, line 16722
- **called from:**
- `src/agent_loop.py:22687`
- `src/agent_loop.py:22816`
- `src/agent_loop.py:23022`
- `src/agent_loop.py:28009`
- `src/agent_loop.py:38852`

## `_request_authorizes_workspace_mutation_completion` — function, line 16751
- **called from:**
- `src/agent_loop.py:25605`
- `tests/test_failed_tool_completion_preamble.py:156`
- `tests/test_failed_tool_completion_preamble.py:165`

## `_requested_post_edit_verification` — function, line 16775
- **called from:**
- `src/agent_loop.py:25623`
- `tests/test_agent_evidence_loop.py:879`
- `tests/test_agent_evidence_loop.py:896`

## `_requested_artifact_readback` — function, line 16797
- **called from:**
- `src/agent_loop.py:25624`
- `tests/test_agent_evidence_loop.py:897`

## `_parse_explicit_file_creation` — function, line 16811
- **called from:**
- `src/agent_loop.py:25603`
- `tests/test_agent_runtime_context.py:624`

## `_first_explicit_workspace_file` — function, line 16835
- **called from:**
- `src/agent_loop.py:33324`
- `src/agent_loop.py:36689`
- `tests/test_agent_runtime_context.py:630`

## `_read_file_block_path` — function, line 16843
- **called from:**
- `src/agent_loop.py:16863`
- `tests/test_review_20260919_fixes.py:91`
- `tests/test_review_20260919_fixes.py:94`
- `tests/test_review_20260919_fixes.py:97`

## `_read_file_targets_artifact` — function, line 16855
- **called from:**
- `src/agent_loop.py:36389`
- `tests/test_review_20260919_fixes.py:103`
- `tests/test_review_20260919_fixes.py:104`
- `tests/test_review_20260919_fixes.py:105`
- `tests/test_review_20260919_fixes.py:108`

## `_explicit_workspace_files` — function, line 16869
- **called from:**
- `src/agent_loop.py:7593`
- `src/agent_loop.py:7602`
- `src/agent_loop.py:7662`
- `src/agent_loop.py:7697`
- `src/agent_loop.py:7717`
- `src/agent_loop.py:7864`
- `src/agent_loop.py:7877`
- `src/agent_loop.py:10428`
- `src/agent_loop.py:17166`
- `src/agent_loop.py:24336`
- `src/agent_loop.py:25390`
- `src/agent_loop.py:25657`
- `tests/test_workspace_artifact_tool_floor.py:1068`

## `_explicit_local_media_files` — function, line 16892
- **called from:**
- `src/agent_loop.py:16913`
- `tests/test_workspace_artifact_tool_floor.py:513`
- `tests/test_workspace_artifact_tool_floor.py:516`
- `tests/test_workspace_artifact_tool_floor.py:519`

## `_explicit_local_media_inputs` — function, line 16906
- **called from:**
- `src/agent_loop.py:7649`
- `src/agent_loop.py:7652`
- `src/agent_loop.py:7854`
- `src/agent_loop.py:7857`
- `src/agent_loop.py:16963`
- `src/agent_loop.py:20365`
- `tests/test_workspace_artifact_tool_floor.py:520`
- `tests/test_workspace_artifact_tool_floor.py:523`

## `_runtime_local_media_inputs` — function, line 16930
- **called from:**
- `src/agent_loop.py:16964`
- `tests/test_workspace_artifact_tool_floor.py:533`
- `tests/test_workspace_artifact_tool_floor.py:539`

## `_native_local_media_inputs` — function, line 16958
- **called from:**
- `src/agent_loop.py:15203`
- `src/agent_loop.py:23604`
- `src/agent_loop.py:23840`
- `src/agent_loop.py:23845`
- `src/agent_loop.py:23943`
- `src/agent_loop.py:24451`
- `src/agent_loop.py:24886`
- `src/agent_loop.py:24891`
- `src/agent_loop.py:24934`
- `src/agent_loop.py:26534`
- `src/agent_loop.py:31268`
- `src/agent_loop.py:31946`
- `src/agent_loop.py:32548`
- `tests/test_workspace_artifact_tool_floor.py:536`

## `_direct_source_media_extraction_requested` — function, line 16970
- **called from:**
- `src/agent_loop.py:20305`
- `src/agent_loop.py:24456`
- `tests/test_workspace_artifact_tool_floor.py:1007`
- `tests/test_workspace_artifact_tool_floor.py:1011`
- `tests/test_workspace_artifact_tool_floor.py:1015`
- `tests/test_workspace_artifact_tool_floor.py:1019`
- `tests/test_workspace_artifact_tool_floor.py:1023`

## `_visible_media_caption_requested` — function, line 17019
- **called from:**
- `src/agent_loop.py:24464`
- `tests/test_workspace_artifact_tool_floor.py:1027`
- `tests/test_workspace_artifact_tool_floor.py:1030`
- `tests/test_workspace_artifact_tool_floor.py:1033`

## `_visual_text_extraction_requested` — function, line 17035
- **called from:**
- `src/agent_loop.py:7987`
- `src/agent_loop.py:23849`
- `src/agent_loop.py:24471`
- `src/agent_loop.py:24895`
- `tests/test_workspace_artifact_tool_floor.py:1039`
- `tests/test_workspace_artifact_tool_floor.py:1042`
- `tests/test_workspace_artifact_tool_floor.py:1045`
- `tests/test_workspace_artifact_tool_floor.py:1046`
- `tests/test_workspace_artifact_tool_floor.py:1049`

## `_local_media_needs_web_lookup` — function, line 17054
- **called from:**
- `src/agent_loop.py:7680`
- `src/agent_loop.py:7945`
- `src/agent_loop.py:7995`
- `src/agent_loop.py:20541`
- `src/agent_loop.py:20688`
- `src/agent_loop.py:23875`
- `src/agent_loop.py:24509`
- `src/agent_loop.py:24908`
- `tests/test_workspace_artifact_tool_floor.py:548`
- `tests/test_workspace_artifact_tool_floor.py:549`
- `tests/test_workspace_artifact_tool_floor.py:550`
- `tests/test_workspace_artifact_tool_floor.py:554`
- `tests/test_workspace_artifact_tool_floor.py:557`
- `tests/test_workspace_artifact_tool_floor.py:560`
- `tests/test_workspace_artifact_tool_floor.py:563`
- `tests/test_workspace_artifact_tool_floor.py:564`
- `tests/test_workspace_artifact_tool_floor.py:567`
- `tests/test_workspace_artifact_tool_floor.py:570`

## `_local_media_needs_browser_render` — function, line 17104
- **called from:**
- `routes/chat_routes.py:2799`
- `src/agent_loop.py:7672`
- `src/agent_loop.py:7929`
- `src/agent_loop.py:7997`
- `src/agent_loop.py:20393`
- `src/agent_loop.py:20950`
- `src/agent_loop.py:21118`
- `src/agent_loop.py:23865`
- `src/agent_loop.py:24484`
- `src/agent_loop.py:24916`
- `tests/test_workspace_artifact_tool_floor.py:595`
- `tests/test_workspace_artifact_tool_floor.py:599`
- `tests/test_workspace_artifact_tool_floor.py:602`

## `_existing_workspace_files` — function, line 17125
- **called from:**
- `src/agent_loop.py:25656`
- `tests/test_agent_runtime_context.py:639`
- `tests/test_existing_workspace_files_confinement.py:10`
- `tests/test_existing_workspace_files_confinement.py:22`
- `tests/test_existing_workspace_files_confinement.py:34`
- `tests/test_existing_workspace_files_confinement.py:46`
- `tests/test_existing_workspace_files_confinement.py:61`
- `tests/test_existing_workspace_files_confinement.py:73`

## `_requested_verification_command` — function, line 17147
- **called from:**
- `src/agent_loop.py:16780`
- `src/agent_loop.py:25625`
- `tests/test_agent_evidence_loop.py:876`
- `tests/test_agent_evidence_loop.py:887`

## `_build_actions_snapshot` — function, line 17181
- **called from:**
- `src/agent_loop.py:31335`

## `_run_verifier_subagent` — function (async), line 17199
- **called from:**
- `src/agent_loop.py:31333`

## `_empty_response_fallback` — function, line 17249
- **called from:**
- `src/agent_loop.py:38208`
- `tests/test_llm_core_reasoning_content_fallback.py:201`
- `tests/test_llm_core_reasoning_content_fallback.py:217`
- `tests/test_tui_round_cap.py:280`
- `tests/test_tui_round_cap.py:296`
- `tests/test_tui_round_cap.py:308`
- `tests/test_tui_round_cap.py:329`

## `build_active_plan_note` — function, line 17340
- **called from:**
- `scripts/dump_agent_prompt.py:197`
- `src/agent_loop.py:25231`
- `tests/test_plan_mode.py:98`
- `tests/test_plan_mode.py:103`
- `tests/test_plan_mode.py:104`

## `_detect_runaway_call` — function, line 17365
- **called from:**
- `src/agent_loop.py:32266`
- `tests/test_loop_breaker_runaway.py:36`
- `tests/test_loop_breaker_runaway.py:41`
- `tests/test_loop_breaker_runaway.py:46`
- `tests/test_loop_breaker_runaway.py:51`
- `tests/test_loop_breaker_runaway.py:56`
- `tests/test_loop_breaker_runaway.py:57`
- `tests/test_loop_breaker_runaway.py:61`

## `_tool_approval_gate_bypassed` — function, line 17376
- **called from:**
- `src/agent_loop.py:21850`
- `tests/test_tool_approvals.py:515`
- `tests/test_tool_approvals.py:527`
- `tests/test_tool_approvals.py:536`

## `_tool_result_signature` — function, line 17391
- **called from:**
- `src/agent_loop.py:37685`
- `tests/test_loop_breaker_runaway.py:65`
- `tests/test_loop_breaker_runaway.py:68`
- `tests/test_loop_breaker_runaway.py:75`
- `tests/test_loop_breaker_runaway.py:78`
- `tests/test_loop_breaker_runaway.py:85`
- `tests/test_loop_breaker_runaway.py:88`

## `_tool_call_signature` — function, line 17423
- **called from:**
- `src/agent_loop.py:32573`
- `src/agent_loop.py:32959`
- `src/agent_loop.py:33848`

## `_web_fetch_pagination_signature` — function, line 17459
- **called from:**
- `src/agent_loop.py:37698`
- `tests/test_agent_rounds_exhausted.py:3697`
- `tests/test_agent_rounds_exhausted.py:3704`

## `_web_search_meaningful_words` — function, line 17543
- **called from:**
- `src/agent_loop.py:17623`
- `src/agent_loop.py:17624`
- `src/agent_loop.py:17650`
- `src/agent_loop.py:17666`
- `src/agent_loop.py:18041`
- `src/agent_loop.py:18200`
- `src/agent_loop.py:18201`
- `src/agent_loop.py:18245`
- `src/agent_loop.py:18246`
- `src/agent_loop.py:18265`
- `src/agent_loop.py:18266`
- `src/agent_loop.py:18305`
- `src/agent_loop.py:18306`
- `src/agent_loop.py:18770`
- `src/agent_loop.py:18771`
- `src/agent_loop.py:18996`
- `src/agent_loop.py:19153`
- `src/agent_loop.py:19183`
- `src/agent_loop.py:19588`

## `_strip_web_search_conversation_prefix` — function, line 17553
- **called from:**
- `src/agent_loop.py:18728`

## `_web_search_query_from_user_text` — function, line 17563
- **called from:**
- `src/agent_loop.py:17622`
- `src/agent_loop.py:18167`
- `src/agent_loop.py:18786`
- `src/agent_loop.py:18807`
- `src/agent_loop.py:18811`
- `src/agent_loop.py:18815`
- `src/agent_loop.py:18819`
- `src/agent_loop.py:18823`
- `src/agent_loop.py:18833`
- `src/agent_loop.py:18934`
- `src/agent_loop.py:19090`
- `src/agent_loop.py:38269`
- `tests/test_tool_policy.py:432`

## `_web_search_query_drops_user_terms` — function, line 17619
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_web_search_query_has_topic` — function, line 17649
- **called from:**
- `src/agent_loop.py:17785`
- `src/agent_loop.py:17975`

## `_web_search_query_is_actionable` — function, line 17653
- **called from:**
- `src/agent_loop.py:18792`
- `src/agent_loop.py:18814`
- `src/agent_loop.py:38252`

## `_web_fetch_failure_needs_private_browser` — function, line 17669
- **called from:**
- `src/agent_loop.py:34405`

## `_private_browser_blocked_by_bot_check` — function, line 17687
- **called from:**
- `src/agent_loop.py:34417`
- `src/agent_loop.py:34607`

## `_should_retry_empty_search_in_browser` — function, line 17704
- **called from:**
- `src/agent_loop.py:34577`
- `tests/test_weather_search_recovery.py:153`
- `tests/test_weather_search_recovery.py:154`
- `tests/test_weather_search_recovery.py:155`
- `tests/test_weather_search_recovery.py:156`
- `tests/test_weather_search_recovery.py:159`

## `_has_recent_web_tool_context` — function, line 17718
- **called from:**
- `src/agent_loop.py:17854`

## `_has_recent_private_browser_context` — function, line 17750
- **called from:**
- `src/agent_loop.py:22018`

## `_is_generic_web_search_followup` — function, line 17777
- **called from:**
- `src/agent_loop.py:17664`
- `src/agent_loop.py:17844`
- `src/agent_loop.py:17976`
- `src/agent_loop.py:17997`
- `src/agent_loop.py:18000`
- `src/agent_loop.py:18117`
- `src/agent_loop.py:18806`

## `_is_contextual_web_search_followup` — function, line 17835
- **called from:**
- `src/agent_loop.py:17870`
- `src/agent_loop.py:17984`
- `src/agent_loop.py:18012`
- `src/agent_loop.py:18080`

## `_looks_like_contextual_web_resource_followup` — function, line 17849
- **called from:**
- `src/agent_loop.py:22016`

## `_looks_like_contextual_web_tool_followup` — function, line 17853
- **called from:**
- `src/agent_loop.py:22017`

## `_looks_like_contextual_weather_status_followup` — function, line 17883
- **called from:**
- `src/agent_loop.py:17942`
- `src/agent_loop.py:22015`
- `tests/test_tool_policy.py:653`
- `tests/test_weather_search_recovery.py:118`

## `_weather_tool_relevant` — function, line 17924
- **called from:**
- `src/agent_loop.py:23901`
- `tests/test_weather_search_recovery.py:98`
- `tests/test_weather_search_recovery.py:99`
- `tests/test_weather_search_recovery.py:100`
- `tests/test_weather_search_recovery.py:103`
- `tests/test_weather_search_recovery.py:104`
- `tests/test_weather_search_recovery.py:105`
- `tests/test_weather_search_recovery.py:106`
- `tests/test_weather_search_recovery.py:107`
- `tests/test_weather_search_recovery.py:119`
- `tests/test_weather_search_recovery.py:120`

## `_web_search_assistant_context_text` — function, line 17946
- **called from:**
- `src/agent_loop.py:18003`
- `src/agent_loop.py:18120`
- `tests/test_tool_policy.py:395`

## `_web_search_topic_text` — function, line 17982
- **called from:**
- `src/agent_loop.py:22024`
- `tests/test_agent_loop.py:199`
- `tests/test_agent_loop.py:216`

## `_looks_like_contextual_public_web_followup` — function, line 18009
- **called from:**
- `src/agent_loop.py:22036`
- `tests/test_tool_policy.py:426`

## `_web_search_context_anchor_words` — function, line 18025
- **called from:**
- `src/agent_loop.py:18047`
- `src/agent_loop.py:18131`
- `src/agent_loop.py:18769`
- `src/agent_loop.py:18995`

## `_web_search_context_candidate_score` — function, line 18046
- **called from:**
- `src/agent_loop.py:18110`

## `_contextual_public_web_topic_text` — function, line 18074
- **called from:**
- `src/agent_loop.py:22019`
- `tests/test_tool_policy.py:363`
- `tests/test_tool_policy.py:381`
- `tests/test_tool_policy.py:418`

## `_web_search_contextual_query_prefix` — function, line 18126
- **called from:**
- `src/agent_loop.py:18780`
- `src/agent_loop.py:18785`

## `_web_followup_context_directive` — function, line 18156
- **called from:**
- `src/agent_loop.py:25162`
- `tests/test_tool_policy.py:364`

## `_web_search_query_low_relevance` — function, line 18199
- **called from:**
- `src/agent_loop.py:18818`

## `_web_search_query_supplies_visual_entity` — function, line 18229
- **called from:**
- `src/agent_loop.py:18269`
- `src/agent_loop.py:18778`

## `_web_search_query_missing_context_anchor` — function, line 18256
- **called from:**
- `src/agent_loop.py:18783`
- `src/agent_loop.py:38267`

## `_web_search_query_has_unasked_source_terms` — function, line 18295
- **called from:**
- `src/agent_loop.py:18822`

## `_private_browser_product_query` — function, line 18314
- **called from:**
- `src/agent_loop.py:36121`
- `tests/test_native_tool_result_threading.py:28`
- `tests/test_native_tool_result_threading.py:31`
- `tests/test_native_tool_result_threading.py:34`
- `tests/test_redos_core_parsers.py:462`

## `_private_browser_uses_unrequested_placeholder` — function, line 18347
- **called from:**
- `src/agent_loop.py:34246`
- `tests/test_native_tool_result_threading.py:42`
- `tests/test_native_tool_result_threading.py:45`
- `tests/test_native_tool_result_threading.py:60`

## `_should_emit_buffered_qwen_round` — function, line 18386
- **called from:**
- `src/agent_loop.py:30809`
- `tests/test_minimal_native_tool_prompt.py:310`
- `tests/test_minimal_native_tool_prompt.py:316`
- `tests/test_minimal_native_tool_prompt.py:322`

## `_incremental_qwen_visible_text` — function, line 18422
- **called from:**
- `src/agent_loop.py:28323`
- `tests/test_minimal_native_tool_prompt.py:334`
- `tests/test_minimal_native_tool_prompt.py:335`
- `tests/test_minimal_native_tool_prompt.py:338`
- `tests/test_minimal_native_tool_prompt.py:346`
- `tests/test_minimal_native_tool_prompt.py:347`

## `_private_browser_product_catalog_ready` — function, line 18452
- **called from:**
- `src/agent_loop.py:36078`
- `tests/test_minimal_native_tool_prompt.py:360`
- `tests/test_minimal_native_tool_prompt.py:361`

## `_private_browser_open_needs_snapshot` — function, line 18473
- **called from:**
- `src/agent_loop.py:36019`
- `tests/test_minimal_native_tool_prompt.py:395`
- `tests/test_minimal_native_tool_prompt.py:396`
- `tests/test_minimal_native_tool_prompt.py:399`

## `_private_browser_product_submit_needs_snapshot` — function, line 18481
- **called from:**
- `src/agent_loop.py:36045`
- `tests/test_minimal_native_tool_prompt.py:405`
- `tests/test_minimal_native_tool_prompt.py:408`
- `tests/test_minimal_native_tool_prompt.py:411`

## `_web_search_needs_official_product_evidence` — function, line 18497
- **called from:**
- `src/agent_loop.py:18826`

## `_web_search_query_from_block` — function, line 18521
- **called from:**
- `src/agent_loop.py:18724`
- `src/agent_loop.py:27837`
- `src/agent_loop.py:30359`
- `src/agent_loop.py:34263`
- `src/agent_loop.py:34582`
- `src/agent_loop.py:34614`
- `src/agent_loop.py:38251`
- `src/agent_loop.py:38263`
- `tests/test_agent_loop.py:229`
- `tests/test_agent_loop.py:240`
- `tests/test_agent_loop.py:273`
- `tests/test_agent_loop.py:285`
- `tests/test_agent_loop.py:331`
- `tests/test_agent_loop.py:382`
- `tests/test_agent_search_dedupe.py:33`
- `tests/test_agent_search_dedupe.py:36`
- `tests/test_tool_policy.py:1180`

## `_normalize_native_tool_shell_wrapper` — function, line 18534
- **called from:**
- `src/agent_loop.py:33005`
- `tests/test_workspace_artifact_tool_floor.py:2322`
- `tests/test_workspace_artifact_tool_floor.py:2328`

## `_normalize_pdf_extract_source_url` — function, line 18565
- **called from:**
- `src/agent_loop.py:33013`
- `tests/test_workspace_artifact_tool_floor.py:368`
- `tests/test_workspace_artifact_tool_floor.py:391`
- `tests/test_workspace_artifact_tool_floor.py:410`

## `_normalize_pdf_extract_query_entities` — function, line 18624
- **called from:**
- `src/agent_loop.py:33021`
- `tests/test_workspace_artifact_tool_floor.py:430`

## `_normalize_local_pdf_inspection_query` — function, line 18684
- **called from:**
- `src/agent_loop.py:33029`
- `tests/test_workspace_artifact_tool_floor.py:450`
- `tests/test_workspace_artifact_tool_floor.py:471`

## `_normalize_web_search_block_query` — function, line 18708
- **called from:**
- `src/agent_loop.py:18999`
- `src/agent_loop.py:27833`
- `src/agent_loop.py:30355`
- `src/agent_loop.py:33080`
- `src/agent_loop.py:33100`
- `src/agent_loop.py:33117`
- `src/agent_loop.py:38258`
- `tests/test_agent_loop.py:224`
- `tests/test_agent_loop.py:235`
- `tests/test_agent_loop.py:249`
- `tests/test_agent_loop.py:267`
- `tests/test_agent_loop.py:279`
- `tests/test_agent_loop.py:294`
- `tests/test_agent_loop.py:323`
- `tests/test_agent_loop.py:340`
- `tests/test_agent_loop.py:358`
- `tests/test_agent_loop.py:376`
- `tests/test_tool_policy.py:241`
- `tests/test_tool_policy.py:249`
- `tests/test_tool_policy.py:340`
- `tests/test_tool_policy.py:439`

## `_browser_search_navigation_to_web_search` — function, line 18878
- **called from:**
- `src/agent_loop.py:15772`
- `src/agent_loop.py:15856`

## `_contextual_browser_opens_to_web_search` — function, line 18945
- **called from:**
- `src/agent_loop.py:33057`
- `tests/test_tool_policy.py:259`
- `tests/test_tool_policy.py:289`
- `tests/test_tool_policy.py:304`

## `_web_search_queries_overlap` — function, line 19006
- **called from:**
- `src/agent_loop.py:30360`
- `src/agent_loop.py:38273`
- `tests/test_agent_search_dedupe.py:12`
- `tests/test_agent_search_dedupe.py:19`
- `tests/test_agent_search_dedupe.py:26`

## `words` — function, line 19013
- **called from:**
- `scripts/pr_blocker_audit.py:362`
- `scripts/pr_blocker_audit.py:381`
- `scripts/pr_blocker_audit.py:584`
- `src/agent_loop.py:19019`
- `src/agent_loop.py:19020`
- `static/js/editor/look-recipes.js:30`

## `_web_search_is_coordinate_query` — function, line 19076
- **called from:**
- `src/agent_loop.py:18829`
- `src/agent_loop.py:19085`
- `src/agent_loop.py:19145`

## `_web_search_coordinate_answer_from_text` — function, line 19084
- **called from:**
- `src/agent_loop.py:19146`
- `src/agent_loop.py:19582`
- `src/agent_loop.py:19829`

## `_web_search_output_has_answer_evidence` — function, line 19115
- **called from:**
- `src/agent_loop.py:19279`
- `src/agent_loop.py:37536`
- `tests/test_tool_policy.py:2350`
- `tests/test_tool_policy.py:2356`
- `tests/test_tool_policy.py:2365`
- `tests/test_tool_policy.py:2375`

## `_web_search_fuel_euro_conversion_answer` — function, line 19169
- **called from:**
- `src/agent_loop.py:19268`
- `src/agent_loop.py:27894`

## `_web_search_answer_from_evidence` — function, line 19266
- **called from:**
- `src/agent_loop.py:27819`
- `src/agent_loop.py:27966`
- `src/agent_loop.py:28035`
- `src/agent_loop.py:38438`

## `_official_website_answer_from_search` — function, line 19287
- **called from:**
- `src/agent_loop.py:34620`
- `tests/test_agent_loop.py:312`
- `tests/test_agent_loop.py:315`

## `_tool_routing_audit_payload` — function, line 19334
- **called from:**
- `src/agent_loop.py:26807`
- `tests/test_tool_routing_audit.py:8`
- `tests/test_tool_routing_audit.py:32`
- `tests/test_tool_routing_audit.py:49`
- `tests/test_tool_routing_audit.py:61`
- `tests/test_tool_routing_audit.py:77`
- `tests/test_tool_routing_audit.py:106`

## `_names` — function, line 19350
- **called from:**
- `src/agent_loop.py:19355`
- `src/agent_loop.py:19356`
- `src/agent_loop.py:19357`
- `src/agent_loop.py:19358`
- `src/agent_loop.py:19359`
- `tests/test_harmony_tool_aliasing.py:38`
- `tests/test_harmony_tool_aliasing.py:45`
- `tests/test_harmony_tool_aliasing.py:52`
- `tests/test_search_query_unicode_names.py:18`
- `tests/test_search_query_unicode_names.py:19`
- `tests/test_search_query_unicode_names.py:20`
- `tests/test_search_query_unicode_names.py:24`
- `tests/test_search_query_unicode_names.py:25`
- `tests/test_search_query_unicode_names.py:29`
- `tests/test_search_query_unicode_names.py:30`
- `tests/test_search_query_unicode_names.py:31`
- `tests/test_skill_index_local_model_gating.py:65`
- `tests/test_skill_index_local_model_gating.py:75`
- `tests/test_skill_index_local_model_gating.py:77`
- `tests/test_skill_index_local_model_gating.py:78`
- `tests/test_skill_index_local_model_gating.py:87`
- `tests/test_skill_index_local_model_gating.py:88`
- `tests/test_skill_index_local_model_gating.py:98`
- `tests/test_skill_index_toolset_gating.py:73`
- `tests/test_skill_index_toolset_gating.py:74`
- `tests/test_skill_index_toolset_gating.py:84`
- `tests/test_skill_index_toolset_gating.py:85`
- `tests/test_skill_index_toolset_gating.py:87`
- `tests/test_skill_index_toolset_gating.py:99`
- `tests/test_skill_index_toolset_gating.py:100`
- `tests/test_skill_index_toolset_gating.py:101`
- `tests/test_skill_index_toolset_gating.py:111`
- `tests/test_skill_index_toolset_gating.py:120`
- `tests/test_skill_index_toolset_gating.py:132`
- `tests/test_skill_index_toolset_gating.py:150`
- `tests/test_skill_rename_collision.py:35`
- `tests/test_skill_rename_collision.py:43`
- `tests/test_skill_rename_collision.py:50`
- `tests/test_skill_rename_collision.py:83`

## `_unoffered_web_search_should_synthesize` — function, line 19395
- **called from:**
- `src/agent_loop.py:28453`
- `tests/test_tool_routing_audit.py:127`
- `tests/test_tool_routing_audit.py:132`
- `tests/test_tool_routing_audit.py:137`

## `_web_search_safety_touch_hygiene_postprocess` — function, line 19411
- **called from:**
- `src/agent_loop.py:27817`
- `src/agent_loop.py:27964`
- `src/agent_loop.py:28033`
- `src/agent_loop.py:38752`

## `_web_search_requested_unit_postprocess` — function, line 19432
- **called from:**
- `src/agent_loop.py:27971`
- `src/agent_loop.py:38756`

## `_looks_like_web_source_dump` — function, line 19447
- **called from:**
- `src/agent_loop.py:17958`
- `src/agent_loop.py:18178`
- `src/agent_loop.py:19518`
- `src/agent_loop.py:19529`
- `src/agent_loop.py:38380`

## `_looks_like_web_retry_preamble` — function, line 19458
- **called from:**
- `src/agent_loop.py:19511`
- `src/agent_loop.py:28842`
- `src/agent_loop.py:38237`
- `tests/test_tool_policy.py:447`
- `tests/test_tool_policy.py:448`
- `tests/test_tool_policy.py:449`

## `_web_model_reports_insufficient_evidence` — function, line 19479
- **called from:**
- `src/agent_loop.py:31881`
- `tests/test_tool_policy.py:2391`
- `tests/test_tool_policy.py:2394`
- `tests/test_tool_policy.py:2397`

## `_looks_like_web_preamble_only_response` — function, line 19497
- **called from:**
- `src/agent_loop.py:38383`

## `_substantive_web_model_answer` — function, line 19514
- **called from:**
- `src/agent_loop.py:19502`
- `src/agent_loop.py:19531`
- `src/agent_loop.py:19535`

## `_web_search_terminal_summary_should_replace` — function, line 19525
- **called from:**
- `src/agent_loop.py:35518`
- `src/agent_loop.py:38621`

## `_web_search_result_snippets` — function, line 19539
- **called from:**
- `src/agent_loop.py:19133`
- `src/agent_loop.py:19839`

## `_web_search_snippets_are_low_signal` — function, line 19559
- **called from:**
- `src/agent_loop.py:19840`

## `_web_search_snippet_synthesis` — function, line 19579
- **called from:**
- `src/agent_loop.py:19841`

## `score_hit` — function, line 19591
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_web_search_fetched_content_chunks` — function, line 19708
- **called from:**
- `src/agent_loop.py:19835`
- `src/agent_loop.py:19844`

## `_web_search_fetched_content_synthesis` — function, line 19773
- **called from:**
- `src/agent_loop.py:19833`
- `src/agent_loop.py:19842`

## `_public_question_misrouted_to_memory` — function, line 19810
- **called from:**
- `src/agent_loop.py:33112`

## `_compact_web_search_terminal_summary` — function, line 19825
- **called from:**
- `src/agent_loop.py:19271`

## `_status_only_shell_command` — function, line 19889
- **called from:**
- `src/agent_loop.py:19929`
- `tests/test_agent_rounds_exhausted.py:876`
- `tests/test_agent_rounds_exhausted.py:877`
- `tests/test_agent_rounds_exhausted.py:878`
- `tests/test_agent_rounds_exhausted.py:879`

## `_blocked_status_tool_round` — function, line 19914
- **called from:**
- `src/agent_loop.py:32249`
- `tests/test_agent_rounds_exhausted.py:1075`
- `tests/test_agent_rounds_exhausted.py:1076`

## `_false_unavailable_tool_claim` — function, line 19934
- **called from:**
- `src/agent_loop.py:31416`
- `tests/test_tool_policy.py:2662`
- `tests/test_tool_policy.py:2670`

## `_read_only_shell_command` — function, line 19972
- **called from:**
- `src/agent_loop.py:14048`
- `src/agent_loop.py:20011`
- `src/agent_loop.py:35956`
- `tests/test_agent_rounds_exhausted.py:883`
- `tests/test_agent_rounds_exhausted.py:884`
- `tests/test_agent_rounds_exhausted.py:885`
- `tests/test_agent_rounds_exhausted.py:886`
- `tests/test_redos_core_parsers.py:370`

## `_read_only_inspection_tool_round` — function, line 19999
- **called from:**
- `src/agent_loop.py:32253`
- `tests/test_agent_rounds_exhausted.py:1059`
- `tests/test_agent_rounds_exhausted.py:1062`
- `tests/test_agent_rounds_exhausted.py:1065`

## `_workspace_mutation_tool_block` — function, line 20018
- **called from:**
- `src/agent_loop.py:20082`
- `src/agent_loop.py:20099`
- `src/agent_loop.py:20271`
- `src/agent_loop.py:20932`
- `src/agent_loop.py:21078`
- `src/agent_loop.py:31918`
- `src/agent_loop.py:31982`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32186`
- `src/agent_loop.py:32445`
- `src/agent_loop.py:34340`
- `src/agent_loop.py:36163`
- `src/agent_loop.py:36199`
- `src/agent_loop.py:36239`
- `src/agent_loop.py:37417`
- `src/agent_loop.py:37728`
- `src/agent_loop.py:37738`
- `tests/test_media_export_mutation_classification.py:18`
- `tests/test_media_export_mutation_classification.py:27`

## `_failed_workspace_mutation_attempts` — function, line 20074
- **called from:**
- `src/agent_loop.py:37717`
- `tests/test_agent_evidence_loop.py:122`

## `_workspace_pre_mutation_verification_block` — function, line 20087
- **called from:**
- `src/agent_loop.py:32385`
- `tests/test_tui_round_cap.py:88`
- `tests/test_tui_round_cap.py:91`
- `tests/test_tui_round_cap.py:94`
- `tests/test_tui_round_cap.py:97`

## `_workspace_mutation_signature` — function, line 20096
- **called from:**
- `src/agent_loop.py:20122`
- `src/agent_loop.py:32867`
- `tests/test_tool_policy.py:3548`

## `_record_successful_workspace_mutation` — function, line 20113
- **called from:**
- `src/agent_loop.py:34342`
- `tests/test_tool_policy.py:3545`
- `tests/test_tool_policy.py:3549`

## `_workspace_file_mutation_paths` — function, line 20129
- **called from:**
- `src/agent_loop.py:36168`
- `src/agent_loop.py:36204`
- `tests/test_workspace_artifact_tool_floor.py:255`
- `tests/test_workspace_artifact_tool_floor.py:256`
- `tests/test_workspace_artifact_tool_floor.py:275`
- `tests/test_workspace_artifact_tool_floor.py:313`

## `_evidenced_workspace_mutation_paths` — function, line 20159
- **called from:**
- `src/agent_loop.py:36169`
- `src/agent_loop.py:36205`
- `tests/test_workspace_artifact_tool_floor.py:293`
- `tests/test_workspace_artifact_tool_floor.py:298`

## `_workspace_inspection_tool_block` — function, line 20179
- **called from:**
- `src/agent_loop.py:20241`
- `src/agent_loop.py:32144`
- `src/agent_loop.py:32201`
- `src/agent_loop.py:32448`
- `src/agent_loop.py:34363`
- `tests/test_workspace_artifact_tool_floor.py:667`
- `tests/test_workspace_artifact_tool_floor.py:671`
- `tests/test_workspace_artifact_tool_floor.py:688`
- `tests/test_workspace_artifact_tool_floor.py:689`
- `tests/test_workspace_artifact_tool_floor.py:690`
- `tests/test_workspace_artifact_tool_floor.py:1295`

## `_personal_read_only_tool_block` — function, line 20217
- **called from:**
- `src/agent_loop.py:32202`

## `_read_only_repeat_limit` — function, line 20238
- **called from:**
- `src/agent_loop.py:20264`
- `tests/test_workspace_artifact_tool_floor.py:691`
- `tests/test_workspace_artifact_tool_floor.py:692`
- `tests/test_workspace_artifact_tool_floor.py:693`

## `_redundant_read_should_block` — function, line 20256
- **called from:**
- `src/agent_loop.py:32967`
- `tests/test_workspace_artifact_tool_floor.py:702`
- `tests/test_workspace_artifact_tool_floor.py:703`
- `tests/test_workspace_artifact_tool_floor.py:704`

## `_artifact_recovery_messages` — function, line 20275
- **called from:**
- `src/agent_loop.py:28488`
- `src/agent_loop.py:28737`
- `src/agent_loop.py:31770`
- `src/agent_loop.py:32036`
- `src/agent_loop.py:32106`
- `src/agent_loop.py:32160`
- `src/agent_loop.py:32285`
- `src/agent_loop.py:32596`
- `src/agent_loop.py:32642`
- `src/agent_loop.py:36848`
- `src/agent_loop.py:37381`
- `src/agent_loop.py:37439`
- `src/agent_loop.py:37497`
- `src/agent_loop.py:37868`
- `tests/test_workspace_artifact_tool_floor.py:623`
- `tests/test_workspace_artifact_tool_floor.py:1087`
- `tests/test_workspace_artifact_tool_floor.py:1156`
- `tests/test_workspace_artifact_tool_floor.py:1404`
- `tests/test_workspace_artifact_tool_floor.py:1551`
- `tests/test_workspace_artifact_tool_floor.py:1564`

## `_artifact_unoffered_recovery_exhausted` — function, line 20486
- **called from:**
- `src/agent_loop.py:28743`
- `src/agent_loop.py:32588`
- `tests/test_workspace_artifact_tool_floor.py:22`
- `tests/test_workspace_artifact_tool_floor.py:23`
- `tests/test_workspace_artifact_tool_floor.py:24`
- `tests/test_workspace_artifact_tool_floor.py:25`

## `_artifact_source_evidence_ready` — function, line 20492
- **called from:**
- `src/agent_loop.py:32004`
- `src/agent_loop.py:36275`
- `tests/test_workspace_artifact_tool_floor.py:1301`
- `tests/test_workspace_artifact_tool_floor.py:1305`
- `tests/test_workspace_artifact_tool_floor.py:1327`
- `tests/test_workspace_artifact_tool_floor.py:1598`
- `tests/test_workspace_artifact_tool_floor.py:1616`

## `_tokens` — function, line 20533
- **called from:**
- `services/skills/publication.py:55`
- `services/skills/publication.py:55`
- `src/agent_loop.py:20540`
- `src/agent_loop.py:20558`
- `tests/test_process_lifecycle.py:319`
- `tests/test_process_lifecycle.py:325`
- `tests/test_process_lifecycle.py:330`
- `tests/test_process_lifecycle.py:339`

## `_artifact_has_current_inspection` — function, line 20578
- **called from:**
- `src/agent_loop.py:27786`
- `src/agent_loop.py:37218`
- `src/agent_loop.py:37253`
- `src/agent_loop.py:37294`
- `tests/test_agent_evidence_loop.py:496`
- `tests/test_agent_evidence_loop.py:499`
- `tests/test_agent_evidence_loop.py:502`

## `_artifact_acquisition_recovery_messages` — function, line 20636
- **called from:**
- `src/agent_loop.py:32076`
- `src/agent_loop.py:37371`
- `tests/test_workspace_artifact_tool_floor.py:1328`

## `_artifact_body_from_synthesis` — function, line 20715
- **called from:**
- `src/agent_loop.py:28527`
- `src/agent_loop.py:28686`
- `src/agent_loop.py:32708`
- `tests/test_agent_rounds_exhausted.py:2486`
- `tests/test_agent_rounds_exhausted.py:2487`
- `tests/test_agent_rounds_exhausted.py:2499`

## `_artifact_body_matches_target` — function, line 20742
- **called from:**
- `src/agent_loop.py:28545`
- `src/agent_loop.py:28694`
- `src/agent_loop.py:32727`
- `tests/test_agent_rounds_exhausted.py:2500`
- `tests/test_agent_rounds_exhausted.py:2501`
- `tests/test_agent_rounds_exhausted.py:2508`
- `tests/test_agent_rounds_exhausted.py:2509`

## `_binary_artifact_path` — function, line 20776
- **called from:**
- `src/agent_loop.py:308`
- `src/agent_loop.py:20352`
- `src/agent_loop.py:20356`
- `src/agent_loop.py:20392`
- `src/agent_loop.py:20806`
- `src/agent_loop.py:20817`
- `src/agent_loop.py:20828`
- `src/agent_loop.py:21043`
- `src/agent_loop.py:28648`
- `src/agent_loop.py:28691`
- `src/agent_loop.py:31272`
- `src/agent_loop.py:32671`
- `tests/test_workspace_artifact_tool_floor.py:477`
- `tests/test_workspace_artifact_tool_floor.py:478`
- `tests/test_workspace_artifact_tool_floor.py:479`
- `tests/test_workspace_artifact_tool_floor.py:480`

## `_artifact_mutation_surface_for_missing` — function, line 20781
- **called from:**
- `src/agent_loop.py:26536`
- `tests/test_workspace_artifact_tool_floor.py:614`
- `tests/test_workspace_artifact_tool_floor.py:619`
- `tests/test_workspace_artifact_tool_floor.py:996`
- `tests/test_workspace_artifact_tool_floor.py:1080`
- `tests/test_workspace_artifact_tool_floor.py:1110`
- `tests/test_workspace_artifact_tool_floor.py:1205`
- `tests/test_workspace_artifact_tool_floor.py:1214`
- `tests/test_workspace_artifact_tool_floor.py:1226`
- `tests/test_workspace_artifact_tool_floor.py:1235`

## `_artifact_recovery_capability_floor` — function, line 20864
- **called from:**
- `src/agent_loop.py:26554`
- `tests/test_workspace_artifact_tool_floor.py:1247`
- `tests/test_workspace_artifact_tool_floor.py:1256`

## `_force_answer_keeps_artifact_tools` — function, line 20886
- **called from:**
- `src/agent_loop.py:25779`
- `src/agent_loop.py:30476`
- `tests/test_workspace_artifact_tool_floor.py:2351`
- `tests/test_workspace_artifact_tool_floor.py:2357`
- `tests/test_workspace_artifact_tool_floor.py:2363`
- `tests/test_workspace_artifact_tool_floor.py:2369`
- `tests/test_workspace_artifact_tool_floor.py:2377`

## `_artifact_calls_are_verification_only` — function, line 20922
- **called from:**
- `src/agent_loop.py:30537`
- `src/agent_loop.py:37217`
- `tests/test_workspace_artifact_tool_floor.py:38`
- `tests/test_workspace_artifact_tool_floor.py:39`
- `tests/test_workspace_artifact_tool_floor.py:40`
- `tests/test_workspace_artifact_tool_floor.py:41`

## `_post_correction_verification_available` — function, line 20936
- **called from:**
- `src/agent_loop.py:25789`
- `src/agent_loop.py:30486`
- `tests/test_workspace_artifact_tool_floor.py:54`
- `tests/test_workspace_artifact_tool_floor.py:57`
- `tests/test_workspace_artifact_tool_floor.py:60`
- `tests/test_workspace_artifact_tool_floor.py:63`

## `_artifact_browser_render_required` — function, line 20944
- **called from:**
- `src/agent_loop.py:26539`
- `src/agent_loop.py:26556`
- `src/agent_loop.py:36259`
- `tests/test_workspace_artifact_tool_floor.py:137`
- `tests/test_workspace_artifact_tool_floor.py:138`

## `_completed_artifact_acquisition_tools_to_remove` — function, line 20953
- **called from:**
- `src/agent_loop.py:36258`
- `tests/test_workspace_artifact_tool_floor.py:130`
- `tests/test_workspace_artifact_tool_floor.py:131`

## `_artifact_mutation_route_surface` — function, line 20970
- **called from:**
- `src/agent_loop.py:26560`
- `tests/test_agent_rounds_exhausted.py:1878`
- `tests/test_agent_rounds_exhausted.py:1888`

## `_request_scoped_allowed_tool_names` — function, line 20993
- **called from:**
- `src/agent_loop.py:32777`
- `tests/test_agent_rounds_exhausted.py:1905`
- `tests/test_agent_rounds_exhausted.py:1908`
- `tests/test_runtime_behavior_regressions.py:226`
- `tests/test_runtime_behavior_regressions.py:239`

## `_empty_action_tool_hint` — function, line 21015
- **called from:**
- `src/agent_loop.py:31181`
- `tests/test_agent_rounds_exhausted.py:973`

## `_source_media_text_companion_recovery_tools` — function, line 21034
- **called from:**
- `src/agent_loop.py:26719`
- `src/agent_loop.py:26725`
- `tests/test_workspace_artifact_tool_floor.py:1117`
- `tests/test_workspace_artifact_tool_floor.py:1121`
- `tests/test_workspace_artifact_tool_floor.py:1125`

## `_bounded_local_media_inspection_blocks` — function, line 21048
- **called from:**
- `src/agent_loop.py:21095`
- `src/agent_loop.py:32544`

## `_bounded_local_pdf_inspection_blocks` — function, line 21086
- **called from:**
- `tests/test_workspace_artifact_tool_floor.py:1267`
- `tests/test_workspace_artifact_tool_floor.py:1274`
- `tests/test_workspace_artifact_tool_floor.py:1281`

## `_browser_render_recovery_blocks` — function, line 21103
- **called from:**
- `src/agent_loop.py:32466`
- `tests/test_workspace_artifact_tool_floor.py:642`

## `_svg_render_recovery_blocks` — function, line 21175
- **called from:**
- `src/agent_loop.py:32486`
- `tests/test_workspace_artifact_tool_floor.py:319`

## `_artifact_synthesis_messages` — function, line 21245
- **called from:**
- `src/agent_loop.py:28493`
- `src/agent_loop.py:32678`
- `tests/test_agent_rounds_exhausted.py:2513`

## `_artifact_generator_execution_block` — function, line 21274
- **called from:**
- `src/agent_loop.py:32649`
- `tests/test_workspace_artifact_tool_floor.py:1430`
- `tests/test_workspace_artifact_tool_floor.py:1470`
- `tests/test_workspace_artifact_tool_floor.py:1473`
- `tests/test_workspace_artifact_tool_floor.py:1476`
- `tests/test_workspace_artifact_tool_floor.py:1504`
- `tests/test_workspace_artifact_tool_floor.py:1518`

## `_mutated_script` — function, line 21294
- **called from:**
- `src/agent_loop.py:21324`
- `src/agent_loop.py:21337`

## `_failed_artifact_generator_repair_reads` — function, line 21358
- **called from:**
- `src/agent_loop.py:32452`
- `tests/test_workspace_artifact_tool_floor.py:1535`
- `tests/test_workspace_artifact_tool_floor.py:1543`

## `_enforce_caller_disabled_tool_policy` — function, line 21400
- **called from:**
- `src/agent_loop.py:24216`
- `tests/test_core_agent_tool_floor.py:19`

## `_blocks_before_inference` — function, line 21432
- **called from:**
- `src/agent_loop.py:21728`
- `src/agent_loop.py:21763`
- `tests/test_turn_contract_integration.py:93`
- `tests/test_turn_contract_integration.py:94`

## `_spec_unavailable_reply` — function, line 21442
- **called from:**
- `src/agent_loop.py:21716`
- `tests/test_spec_route_policy_conflict.py:66`
- `tests/test_spec_route_policy_conflict.py:67`

## `_apply_spec_decision_to_contract` — function, line 21457
- **called from:**
- `src/agent_loop.py:21582`
- `src/agent_loop.py:21609`

## `_denied` — function, line 21490
- **called from:**
- `src/agent_loop.py:21496`
- `src/agent_loop.py:21498`

## `_spec_router_contract` — function, line 21554
- **called from:**
- `tests/test_spec_contract_security.py:34`
- `tests/test_spec_route_policy_conflict.py:53`
- `tests/test_spec_route_policy_conflict.py:155`
- `tests/test_spec_route_policy_conflict.py:178`

## `_spec_router_contract_async` — function (async), line 21588
- **called from:**
- `src/agent_loop.py:21709`

## `stream_agent_loop` — function (async), line 21626
- decorator: `with_request_authority`
- decorator: `with_turn_contract`
- decorator: `with_teacher_takeover`
- **called from:**
- `routes/chat_routes.py:860`
- `routes/chat_routes.py:864`
- `scripts/eval_exact_file_routing.py:90`
- `scripts/eval_odysseus_everyday_live_hard.py:259`
- `scripts/eval_odysseus_live_hard_examples.py:271`
- `services/skills/agent_runner.py:59`
- `services/skills/agent_runner.py:209`
- `src/agent_tools/spawn_agent_tools.py:195`
- `src/bg_monitor.py:72`
- `src/task_scheduler.py:2079`
- `src/teacher_escalation.py:708`
- `tests/test_agent_evidence_loop.py:96`
- `tests/test_agent_external_tool_schemas.py:35`
- `tests/test_agent_external_tool_schemas.py:95`
- `tests/test_agent_external_tool_schemas.py:149`
- `tests/test_agent_external_tool_schemas.py:365`
- `tests/test_agent_external_tool_schemas.py:442`
- `tests/test_agent_rounds_exhausted.py:76`
- `tests/test_agent_rounds_exhausted.py:135`
- `tests/test_agent_rounds_exhausted.py:176`
- `tests/test_agent_rounds_exhausted.py:252`
- `tests/test_agent_rounds_exhausted.py:331`
- `tests/test_agent_rounds_exhausted.py:394`
- `tests/test_agent_rounds_exhausted.py:449`
- `tests/test_agent_rounds_exhausted.py:510`
- `tests/test_agent_rounds_exhausted.py:568`
- `tests/test_agent_rounds_exhausted.py:624`
- `tests/test_agent_rounds_exhausted.py:671`
- `tests/test_agent_rounds_exhausted.py:731`
- `tests/test_agent_rounds_exhausted.py:783`
- `tests/test_agent_rounds_exhausted.py:826`
- `tests/test_agent_rounds_exhausted.py:960`
- `tests/test_agent_rounds_exhausted.py:1029`
- `tests/test_agent_rounds_exhausted.py:1138`
- `tests/test_agent_rounds_exhausted.py:1210`
- `tests/test_agent_rounds_exhausted.py:1282`
- `tests/test_agent_rounds_exhausted.py:1384`
- `tests/test_agent_rounds_exhausted.py:1469`
- `tests/test_agent_rounds_exhausted.py:1620`
- `tests/test_agent_rounds_exhausted.py:1664`
- `tests/test_agent_rounds_exhausted.py:1707`
- `tests/test_agent_rounds_exhausted.py:1781`
- `tests/test_agent_rounds_exhausted.py:1852`
- `tests/test_agent_rounds_exhausted.py:1931`
- `tests/test_agent_rounds_exhausted.py:1999`
- `tests/test_agent_rounds_exhausted.py:2103`
- `tests/test_agent_rounds_exhausted.py:2162`
- `tests/test_agent_rounds_exhausted.py:2202`
- `tests/test_agent_rounds_exhausted.py:2249`
- `tests/test_agent_rounds_exhausted.py:2300`
- `tests/test_agent_rounds_exhausted.py:2340`
- `tests/test_agent_rounds_exhausted.py:2386`
- `tests/test_agent_rounds_exhausted.py:2438`
- `tests/test_agent_rounds_exhausted.py:2559`
- `tests/test_agent_rounds_exhausted.py:2609`
- `tests/test_agent_rounds_exhausted.py:2669`
- `tests/test_agent_rounds_exhausted.py:2782`
- `tests/test_agent_rounds_exhausted.py:2879`
- `tests/test_agent_rounds_exhausted.py:2972`
- `tests/test_agent_rounds_exhausted.py:3092`
- … +131 more (grep the name in repo)

## `_direct_candidate_request` — function, line 22739
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_direct_terminal_event` — function, line 22772
- **called from:**
- `src/agent_loop.py:22948`
- `src/agent_loop.py:22964`
- `src/agent_loop.py:22977`

## `_route_finetune_modes` — function, line 23633
- **called from:**
- `src/agent_loop.py:23778`
- `src/agent_loop.py:23900`
- `src/agent_loop.py:24774`

## `_route_relevant_tools` — function, line 23689
- **called from:**
- `src/agent_loop.py:23910`
- `src/agent_loop.py:24775`

## `_trim_route_request_messages` — function, line 24559
- **called from:**
- `src/agent_loop.py:25336`
- `src/agent_loop.py:26913`
- `src/agent_loop.py:27017`
- `src/agent_loop.py:27660`
- `src/agent_loop.py:28144`

## `_without_protection` — function, line 24562
- **called from:**
- `src/agent_loop.py:24602`
- `src/agent_loop.py:24704`
- `src/agent_loop.py:24711`

## `_build_route_request_state` — function (async), line 24713
- **called from:**
- `src/agent_loop.py:25318`
- `src/agent_loop.py:26902`
- `src/agent_loop.py:27007`
- `src/agent_loop.py:28137`

## `_is_direct_conversation_message` — function, line 25280
- **called from:**
- `src/agent_loop.py:25292`
- `src/agent_loop.py:25296`
- `src/agent_loop.py:25302`

## `_looks_like_unfinished_action_promise` — function, line 25709
- **called from:**
- `src/agent_loop.py:30505`
- `src/agent_loop.py:30612`
- `src/agent_loop.py:30663`
- `src/agent_loop.py:31238`

## `_filter_route_tool_schemas` — function, line 25750
- **called from:**
- `src/agent_loop.py:25820`
- `src/agent_loop.py:25843`
- `src/agent_loop.py:25933`
- `src/agent_loop.py:25941`

## `_tool_schemas_for_route` — function, line 25761
- **called from:**
- `src/agent_loop.py:26773`
- `src/agent_loop.py:26938`

## `_push_approved_progress` — function (async), line 25975
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_approved_tool` — function (async), line 25978
- **called from:**
- `src/agent_loop.py:25995`

## `_runtime_candidate` — function, line 26858
- **called from:**
- `src/agent_loop.py:26869`
- `src/agent_loop.py:26873`
- `src/agent_loop.py:26874`

## `_candidate_request` — function (async), line 26894
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_candidate_capability_recovery` — function (async), line 26991
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apply_candidate_compaction` — function, line 27060
- **called from:**
- `src/agent_loop.py:28069`
- `src/agent_loop.py:28190`
- `src/agent_loop.py:28200`
- `src/agent_loop.py:28223`

## `_finalize_round_usage` — function, line 27094
- **called from:**
- `src/agent_loop.py:27178`
- `src/agent_loop.py:27307`
- `src/agent_loop.py:27626`
- `src/agent_loop.py:27643`
- `src/agent_loop.py:27800`
- `src/agent_loop.py:27816`
- `src/agent_loop.py:27832`
- `src/agent_loop.py:27978`
- `src/agent_loop.py:28374`

## `_push_progress` — function (async), line 34241
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_tool` — function (async), line 34244
- **called from:**
- `src/agent_loop.py:34298`

## `_calendar_time_label` — function, line 35729
- **called from:**
- `src/agent_loop.py:35762`
- `src/agent_loop.py:35769`
