# `routes/chat_routes.py` — definitions & call sites

101 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_append_internal_chat_context` — function, line 112
- **called from:**
- `routes/chat_routes.py:2509`
- `routes/chat_routes.py:3336`
- `tests/test_request_authority.py:474`

## `_clean_v3_route_for_model` — function, line 131
- **called from:**
- `routes/chat_routes.py:2825`
- `routes/chat_routes.py:3148`
- `tests/test_clean_v3_route_ownership.py:10`
- `tests/test_clean_v3_route_ownership.py:14`
- `tests/test_clean_v3_route_ownership.py:18`
- `tests/test_clean_v3_route_ownership.py:19`
- `tests/test_clean_v3_route_ownership.py:23`
- `tests/test_clean_v3_route_ownership.py:24`
- `tests/test_clean_v3_route_ownership.py:25`
- `tests/test_clean_v3_route_ownership.py:29`
- `tests/test_clean_v3_route_ownership.py:30`
- `tests/test_clean_v3_route_ownership.py:34`
- `tests/test_clean_v3_route_ownership.py:35`
- `tests/test_clean_v3_route_ownership.py:36`
- `tests/test_clean_v3_route_ownership.py:37`
- `tests/test_clean_v3_route_ownership.py:41`
- `tests/test_clean_v3_route_ownership.py:42`
- `tests/test_compact_core_contract_path.py:16`

## `_turn_contract_enabled` — function, line 142
- **called from:**
- `routes/chat_routes.py:3273`
- `routes/chat_routes.py:3479`
- `tests/test_clean_v3_route_ownership.py:46`
- `tests/test_clean_v3_route_ownership.py:55`
- `tests/test_clean_v3_route_ownership.py:64`
- `tests/test_clean_v3_route_ownership.py:96`
- `tests/test_clean_v3_route_ownership.py:116`
- `tests/test_context_resolution_route.py:504`

## `_request_privileges` — function, line 160
- **called from:**
- `routes/chat_routes.py:3281`
- `routes/chat_routes.py:3682`
- `tests/test_context_resolution_route.py:522`

## `_native_runtime_requires_local_browser` — function, line 173
- **called from:**
- `routes/chat_routes.py:2800`
- `tests/test_clean_v3_route_ownership.py:113`
- `tests/test_clean_v3_route_ownership.py:115`

## `_AgentRenderState` — class, line 189
- **called from:**
- `routes/chat_routes.py:4268`
- `tests/test_foreground_model_routing.py:48`
- `tests/test_runtime_evidence_contract.py:205`

## `_AgentRenderState.__init__` — method, line 192
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `_AgentRenderState.consume` — method, line 197
- **called from:**
- `routes/chat_routes.py:3055`
- `routes/chat_routes.py:5084`
- `routes/skills_routes.py:700`
- `services/skills/agent_runner.py:146`
- `services/skills/agent_runner.py:277`
- `services/skills/audit_workflow.py:119`
- `services/skills/audit_workflow.py:153`
- `services/skills/job_coordinator.py:24`
- `src/task_scheduler.py:2134`
- `tests/test_agent_render_ownership.py:23`
- `tests/test_agent_render_ownership.py:24`
- `tests/test_agent_render_ownership.py:31`
- `tests/test_agent_render_ownership.py:32`
- `tests/test_agent_render_ownership.py:44`
- `tests/test_agent_render_ownership.py:45`
- `tests/test_agent_render_ownership.py:46`
- `tests/test_agent_render_ownership.py:47`
- `tests/test_agent_render_ownership.py:58`
- `tests/test_agent_render_ownership.py:59`
- `tests/test_agent_render_ownership.py:60`
- `tests/test_agent_render_ownership.py:74`
- `tests/test_agent_render_ownership.py:80`
- `tests/test_agent_render_ownership.py:81`
- `tests/test_agent_rounds_exhausted.py:3779`
- `tests/test_exact_approval_ungranted_process.py:33`
- `tests/test_external_context_tool_gate.py:1345`
- `tests/test_foreground_model_routing.py:49`
- `tests/test_local_mcp_capabilities.py:531`
- `tests/test_owned_resource_identity.py:49`
- `tests/test_remote_resource_identity.py:39`
- `tests/test_request_authority.py:271`
- `tests/test_request_authority.py:303`
- `tests/test_resource_identity.py:549`
- `tests/test_runtime_evidence_contract.py:207`
- `tests/test_runtime_resource_integration.py:45`
- `tests/test_skills_audit_services.py:357`
- `tests/test_teacher_eval_tier2.py:299`
- `tests/test_tool_approval_single_action_scope.py:41`
- `tests/test_tool_approval_single_action_scope.py:65`
- `tests/test_tool_approval_single_action_scope.py:81`
- `tests/test_tool_approval_task_scope.py:79`
- `tests/test_tool_approval_task_scope.py:108`
- `tests/test_tool_approval_task_scope.py:174`
- `tests/test_tool_approvals.py:50`
- `tests/test_tool_approvals.py:85`
- `tests/test_tool_approvals.py:94`
- `tests/test_tool_approvals.py:108`
- `tests/test_tool_approvals.py:180`
- `tests/test_tool_approvals.py:238`
- `tests/test_tool_approvals.py:290`
- `tests/test_tool_approvals.py:403`
- `tests/test_tool_approvals.py:439`
- `tests/test_tool_approvals.py:473`
- `tests/test_turn_contract_integration.py:225`
- `static/js/cookbookRunning.js:4167`

## `_AgentRenderState.metadata` — method, line 222
- **called from:**
- `routes/chat_routes.py:230`
- `routes/chat_routes.py:5183`
- `routes/chat_routes.py:5227`
- `routes/chat_routes.py:5313`
- `tests/test_agent_render_ownership.py:26`
- `tests/test_agent_render_ownership.py:36`
- `tests/test_agent_render_ownership.py:52`
- `tests/test_agent_render_ownership.py:76`
- `tests/test_agent_render_ownership.py:84`
- `tests/test_media_ingress.py:46`
- `tests/test_media_ingress.py:157`
- `tests/test_nested_invocation_ownership.py:85`
- `tests/test_nested_invocation_ownership.py:86`
- `tests/test_nested_invocation_ownership.py:130`
- `tests/test_nested_invocation_ownership.py:130`
- `tests/test_nested_invocation_ownership.py:292`
- `tests/test_nested_invocation_ownership.py:302`
- `tests/test_nested_invocation_ownership.py:303`
- `tests/test_nested_invocation_ownership.py:304`
- `tests/test_nested_invocation_ownership.py:306`
- `tests/test_nested_invocation_ownership.py:544`
- `static/js/chatRenderer.js:3632`
- `static/js/fileHandler.js:461`

## `_AgentRenderState.message_saved` — method, line 229
- **called from:**
- `routes/chat_routes.py:5224`
- `routes/chat_routes.py:5284`
- `routes/chat_routes.py:5347`
- `tests/test_agent_render_ownership.py:27`
- `tests/test_agent_render_ownership.py:39`
- `tests/test_agent_render_ownership.py:40`
- `tests/test_agent_render_ownership.py:53`
- `tests/test_agent_render_ownership.py:54`
- `tests/test_agent_render_ownership.py:63`

## `_visible_response_text_for_save` — function, line 233
- **called from:**
- `routes/chat_routes.py:4797`
- `routes/chat_routes.py:4799`
- `routes/chat_routes.py:4806`
- `routes/chat_routes.py:5250`
- `routes/chat_routes.py:5252`
- `routes/chat_routes.py:5257`
- `routes/chat_routes.py:5317`
- `routes/chat_routes.py:5319`
- `routes/chat_routes.py:5323`
- `routes/chat_routes.py:5331`
- `tests/test_foreground_model_routing.py:38`
- `tests/test_foreground_model_routing.py:39`
- `tests/test_foreground_model_routing.py:40`
- `tests/test_foreground_model_routing.py:42`

## `_is_personal_data_search_without_web_target` — function, line 244
- **called from:**
- `routes/chat_routes.py:2756`
- `tests/test_chat_route_tool_policy.py:45`
- `tests/test_chat_route_tool_policy.py:48`
- `tests/test_chat_route_tool_policy.py:51`
- `tests/test_chat_route_tool_policy.py:54`
- `tests/test_chat_route_tool_policy.py:57`

## `_explicitly_denies_web_lookup` — function, line 264
- **called from:**
- `routes/chat_routes.py:303`
- `routes/chat_routes.py:3620`
- `routes/chat_routes.py:3625`
- `routes/chat_routes.py:3633`
- `tests/test_chat_route_tool_policy.py:652`

## `_explicitly_denies_tool_use` — function, line 275
- **called from:**
- `routes/chat_routes.py:3838`

## `_contains_explicit_url_target` — function, line 289
- **called from:**
- `routes/chat_routes.py:2755`
- `tests/test_chat_route_tool_policy.py:63`
- `tests/test_chat_route_tool_policy.py:64`
- `tests/test_chat_route_tool_policy.py:65`
- `tests/test_chat_route_tool_policy.py:66`
- `tests/test_chat_route_tool_policy.py:72`

## `_authorizes_exact_url_fetch` — function, line 294
- **called from:**
- `routes/chat_routes.py:2775`
- `tests/test_chat_route_tool_policy.py:91`
- `tests/test_chat_route_tool_policy.py:94`
- `tests/test_chat_route_tool_policy.py:97`
- `tests/test_chat_route_tool_policy.py:100`

## `_is_explicit_browser_automation_request` — function, line 312
- **called from:**
- `routes/chat_routes.py:303`
- `routes/chat_routes.py:2769`
- `tests/test_chat_route_tool_policy.py:73`
- `tests/test_chat_route_tool_policy.py:74`
- `tests/test_chat_route_tool_policy.py:77`

## `_is_external_discovery_request` — function, line 323
- **called from:**
- `routes/chat_routes.py:2772`
- `tests/test_chat_route_tool_policy.py:83`
- `tests/test_chat_route_tool_policy.py:86`
- `tests/test_chat_route_tool_policy.py:87`

## `_mentions_pdf_url` — function, line 338
- **called from:**
- `routes/chat_routes.py:358`
- `src/agent_loop.py:7624`
- `tests/test_redos_core_parsers.py:259`
- `tests/test_redos_residual_python.py:121`

## `_prefers_structured_document_tools` — function, line 352
- **called from:**
- `routes/chat_routes.py:3961`
- `tests/test_chat_route_tool_policy.py:111`
- `tests/test_chat_route_tool_policy.py:114`
- `tests/test_chat_route_tool_policy.py:117`

## `_is_contextual_web_link_followup` — function, line 368
- **called from:**
- `routes/chat_routes.py:3612`

## `_parse_client_tools` — function, line 397
- **called from:**
- `routes/chat_routes.py:616`

## `_parse_legacy_client_runtime_context` — function, line 417
- **called from:**
- `routes/chat_routes.py:725`

## `clean_skill_name` — function, line 419
- **called from:**
- `routes/chat_routes.py:671`
- `routes/chat_routes.py:683`

## `clean_contract_atom` — function, line 423
- **called from:**
- `routes/chat_routes.py:479`
- `routes/chat_routes.py:515`
- `routes/chat_routes.py:551`
- `routes/chat_routes.py:653`

## `clean_short_text` — function, line 427
- **called from:**
- `routes/chat_routes.py:446`
- `routes/chat_routes.py:447`
- `routes/chat_routes.py:500`
- `routes/chat_routes.py:527`
- `routes/chat_routes.py:632`
- `routes/chat_routes.py:651`
- `routes/chat_routes.py:652`
- `routes/chat_routes.py:655`
- `routes/chat_routes.py:657`
- `routes/chat_routes.py:687`
- `routes/chat_routes.py:688`
- `routes/chat_routes.py:698`

## `clean_multiline_text` — function, line 431
- **called from:**
- `routes/chat_routes.py:451`
- `routes/chat_routes.py:702`

## `clean_local_agents_md` — function, line 437
- **called from:**
- `routes/chat_routes.py:640`

## `clean_bool_map` — function, line 461
- **called from:**
- `routes/chat_routes.py:518`
- `routes/chat_routes.py:521`

## `clean_host_shell_request` — function, line 475
- **called from:**
- `routes/chat_routes.py:524`

## `clean_runtime_contract` — function, line 505
- **called from:**
- `routes/chat_routes.py:637`

## `_native_context_has_workspace_inputs` — function, line 713
- **called from:**
- `routes/chat_routes.py:2837`
- `tests/test_chat_route_tool_policy.py:451`
- `tests/test_chat_route_tool_policy.py:456`

## `_parse_client_runtime_context` — function, line 723
- **called from:**
- `routes/chat_routes.py:2702`
- `tests/test_client_tool_contract.py:30`
- `tests/test_client_tool_contract.py:43`
- `tests/test_client_tool_routing.py:913`
- `tests/test_client_tool_routing.py:932`
- `tests/test_client_tool_routing.py:982`
- `tests/test_client_tool_routing.py:1025`
- `tests/test_client_tool_routing.py:1026`
- `tests/test_client_tool_routing.py:1034`
- `tests/test_client_tool_routing.py:1071`
- `tests/test_client_tool_routing.py:1089`
- `tests/test_client_tool_routing.py:1169`
- `tests/test_native_terminal_context.py:13`
- `tests/test_tui_round_cap.py:164`
- `tests/test_tui_round_cap.py:171`

## `_external_execution_bridge` — function, line 811
- **called from:**
- `routes/chat_routes.py:5033`
- `tests/test_remote_resource_identity.py:282`

## `route_tool` — function (async), line 826
- **called from:**
- `src/tool_execution.py:2215`

## `_stream_agent_with_execution_bridge` — function (async), line 857
- **called from:**
- `routes/chat_routes.py:5032`
- `tests/test_turn_contract_integration.py:120`
- `tests/test_turn_contract_integration.py:161`

## `_should_detach_chat_stream` — function, line 868
- **called from:**
- `routes/chat_routes.py:5513`
- `tests/test_compare_stop_disconnect_poll.py:485`

## `_post_response_extraction_allowed` — function, line 894
- **called from:**
- `routes/chat_routes.py:4831`
- `routes/chat_routes.py:5298`
- `routes/chat_routes.py:5363`
- `tests/test_compare_stop_disconnect_poll.py:518`

## `_client_runtime_context_system_message` — function, line 920
- **called from:**
- `routes/chat_routes.py:4049`
- `tests/test_client_tool_routing.py:1007`
- `tests/test_client_tool_routing.py:1059`
- `tests/test_client_tool_routing.py:1149`

## `_client_runtime_context_requests_workspace_profile` — function, line 1122
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_client_runtime_context_cwd` — function, line 1130
- **called from:**
- `routes/chat_routes.py:960`
- `routes/chat_routes.py:1154`
- `tests/test_client_tool_routing.py:1177`
- `tests/test_client_tool_routing.py:1178`

## `_agent_turn_cwd` — function, line 1139
- **called from:**
- `routes/chat_routes.py:5065`
- `tests/test_client_tool_routing.py:605`
- `tests/test_client_tool_routing.py:611`
- `tests/test_client_tool_routing.py:612`

## `_effective_agent_rounds` — function, line 1159
- **called from:**
- `routes/chat_routes.py:4969`
- `tests/test_client_tool_routing.py:1017`
- `tests/test_client_tool_routing.py:1018`
- `tests/test_client_tool_routing.py:1019`
- `tests/test_tui_round_cap.py:62`
- `tests/test_tui_round_cap.py:63`
- `tests/test_tui_round_cap.py:70`
- `tests/test_tui_round_cap.py:79`
- `tests/test_tui_round_cap.py:103`
- `tests/test_tui_round_cap.py:107`
- `tests/test_tui_round_cap.py:120`
- `tests/test_tui_round_cap.py:132`
- `tests/test_tui_round_cap.py:180`

## `_effective_native_output_tokens` — function, line 1222
- **called from:**
- `routes/chat_routes.py:4976`
- `tests/test_tui_round_cap.py:151`
- `tests/test_tui_round_cap.py:152`
- `tests/test_tui_round_cap.py:155`
- `tests/test_tui_round_cap.py:158`

## `_annotate_chat_cost` — function, line 1255
- **called from:**
- `routes/chat_routes.py:4641`
- `routes/chat_routes.py:4789`

## `_stream_failure_status` — function, line 1283
- **called from:**
- `routes/chat_routes.py:4651`
- `tests/test_foreground_model_routing.py:136`

## `_reject_delegated_tool_approval` — function, line 1297
- **called from:**
- `routes/chat_routes.py:3027`
- `tests/test_api_token_tool_authority.py:525`
- `tests/test_api_token_tool_authority.py:533`

## `_mark_tool_approval_resolved` — function, line 1314
- **called from:**
- `routes/chat_routes.py:3070`
- `tests/test_tool_approval_task_scope.py:290`

## `_tool_approval_resolution_stream` — function (async), line 1373
- **called from:**
- `routes/chat_routes.py:3081`
- `tests/test_tool_approval_task_scope.py:308`

## `_chat_candidate_request_factory` — function, line 1378
- **called from:**
- `routes/chat_routes.py:2557`
- `routes/chat_routes.py:4357`

## `factory` — function (async), line 1395
- **called from:**
- `tests/test_admin_listing_authorization.py:63`
- `tests/test_background_tool_jobs.py:16`
- `tests/test_calendar_default_transaction.py:79`
- `tests/test_calendar_default_transaction.py:180`
- `tests/test_calendar_default_transaction.py:225`
- `tests/test_calendar_default_transaction.py:251`
- `tests/test_calendar_default_transaction.py:295`
- `tests/test_calendar_default_transaction.py:499`
- `tests/test_calendar_default_transaction.py:511`
- `tests/test_calendar_default_transaction.py:526`
- `tests/test_chat_document_owner_context.py:58`
- `tests/test_chat_document_owner_context.py:94`
- `tests/test_chat_document_owner_context.py:115`
- `tests/test_chat_helpers.py:511`
- `tests/test_chat_helpers.py:565`
- `tests/test_chat_helpers.py:602`
- `tests/test_chat_image_preservation.py:20`
- `tests/test_chat_image_preservation.py:32`
- `tests/test_chat_image_preservation.py:48`
- `tests/test_chat_tidy_content_preservation.py:60`
- `tests/test_chat_tidy_content_preservation.py:75`
- `tests/test_chat_tidy_content_preservation.py:79`
- `tests/test_chat_tidy_content_preservation.py:90`
- `tests/test_chat_tidy_content_preservation.py:107`
- `tests/test_chat_tidy_content_preservation.py:120`
- `tests/test_chat_tidy_content_preservation.py:146`
- `tests/test_chatgpt_session_binding.py:26`
- `tests/test_chatgpt_session_binding.py:49`
- `tests/test_chatgpt_session_binding.py:65`
- `tests/test_chatgpt_session_binding.py:79`
- `tests/test_chatgpt_session_binding.py:92`
- `tests/test_chatgpt_session_binding.py:103`
- `tests/test_chatgpt_session_binding.py:130`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:174`
- `tests/test_chatgpt_subscription_usage.py:26`
- `tests/test_cleanup_transcript_preservation.py:36`
- `tests/test_cleanup_transcript_preservation.py:67`
- `tests/test_cleanup_transcript_preservation.py:79`
- `tests/test_cleanup_transcript_preservation.py:91`
- `tests/test_cleanup_transcript_preservation.py:107`
- `tests/test_cleanup_transcript_preservation.py:115`
- `tests/test_cleanup_transcript_preservation.py:128`
- `tests/test_cleanup_transcript_preservation.py:157`
- `tests/test_cleanup_transcript_preservation.py:166`
- `tests/test_cleanup_transcript_preservation.py:206`
- `tests/test_cleanup_transcript_preservation.py:224`
- `tests/test_cleanup_transcript_preservation.py:233`
- `tests/test_cleanup_transcript_preservation.py:260`
- `tests/test_cleanup_transcript_preservation.py:276`
- `tests/test_cleanup_transcript_preservation.py:306`
- `tests/test_cleanup_transcript_preservation.py:318`
- `tests/test_cleanup_transcript_preservation.py:358`
- `tests/test_cleanup_transcript_preservation.py:375`
- `tests/test_cookbook_endpoint_registration.py:75`
- `tests/test_cookbook_endpoint_registration.py:474`
- `tests/test_cost_tracking.py:142`
- `tests/test_cost_tracking.py:158`
- `tests/test_cost_tracking.py:176`
- `tests/test_cost_tracking.py:187`
- `tests/test_default_chat_model_filter.py:36`
- … +50 more (grep the name in repo)

## `_candidate_index` — function, line 1425
- **called from:**
- `routes/chat_routes.py:2576`

## `_stream_set` — function, line 1432
- **called from:**
- `routes/chat_routes.py:4246`
- `routes/chat_routes.py:4544`
- `routes/chat_routes.py:4734`
- `routes/chat_routes.py:4741`
- `routes/chat_routes.py:4875`
- `routes/chat_routes.py:4884`
- `routes/chat_routes.py:5105`
- `routes/chat_routes.py:5115`
- `routes/chat_routes.py:5222`
- `routes/chat_routes.py:5405`
- `routes/chat_routes.py:5414`

## `_persist_stream_partial` — function, line 1445
- **called from:**
- `routes/chat_routes.py:4895`
- `routes/chat_routes.py:4913`
- `routes/chat_routes.py:4930`
- `routes/chat_routes.py:5425`
- `routes/chat_routes.py:5450`
- `routes/chat_routes.py:5471`
- `tests/test_partial_tool_events.py:59`
- `tests/test_partial_tool_events.py:73`

## `_persist_continue_separator` — function, line 1520
- **called from:**
- `routes/chat_routes.py:3008`

## `_sink_tool_state` — function, line 1556
- **called from:**
- `routes/chat_routes.py:4320`
- `routes/chat_routes.py:5423`
- `routes/chat_routes.py:5444`
- `routes/chat_routes.py:5466`
- `tests/test_partial_tool_events.py:34`
- `tests/test_partial_tool_events.py:35`
- `tests/test_partial_tool_events.py:44`
- `tests/test_partial_tool_events.py:54`

## `_checkpoint_draft` — function, line 1574
- **called from:**
- `routes/chat_routes.py:4325`

## `_message_plain_text` — function, line 1601
- **called from:**
- `routes/chat_routes.py:1618`
- `routes/chat_routes.py:1695`

## `_last_user_plain_text` — function, line 1615
- **called from:**
- `routes/chat_routes.py:1627`

## `_ensure_current_request_is_latest_user` — function, line 1622
- **called from:**
- `routes/chat_routes.py:4258`

## `_recent_session_text` — function, line 1688
- **called from:**
- `routes/chat_routes.py:1705`
- `routes/chat_routes.py:1822`

## `_is_contextual_web_followup` — function, line 1701
- **called from:**
- `routes/chat_routes.py:3170`
- `routes/chat_routes.py:3618`
- `tests/test_chat_route_tool_policy.py:395`

## `_has_recent_web_tool_event` — function, line 1708
- **called from:**
- `routes/chat_routes.py:3619`

## `_successful_session_tool_names` — function, line 1713
- **called from:**
- `routes/chat_routes.py:3846`
- `tests/test_clean_v3_route_ownership.py:90`

## `_most_recent_successful_web_tool` — function, line 1748
- **called from:**
- `routes/chat_routes.py:1710`
- `routes/chat_routes.py:3898`
- `routes/chat_routes.py:3916`
- `tests/test_chat_route_tool_policy.py:405`
- `tests/test_chat_route_tool_policy.py:414`

## `_has_recent_private_browser_success` — function, line 1771
- **called from:**
- `routes/chat_routes.py:3153`
- `tests/test_chat_route_tool_policy.py:259`
- `tests/test_chat_route_tool_policy.py:260`
- `tests/test_chat_route_tool_policy.py:261`

## `has_success` — function, line 1773
- **called from:**
- `routes/chat_routes.py:1792`
- `routes/chat_routes.py:1810`

## `_is_contextual_browser_followup` — function, line 1815
- **called from:**
- `routes/chat_routes.py:3183`
- `routes/chat_routes.py:3544`
- `tests/test_chat_route_tool_policy.py:270`
- `tests/test_chat_route_tool_policy.py:281`
- `tests/test_chat_route_tool_policy.py:285`

## `_resolve_request_workspace` — function, line 1825
- **called from:**
- `routes/chat_routes.py:1872`
- `routes/chat_routes.py:2724`
- `tests/test_workspace_confine.py:588`
- `tests/test_workspace_confine.py:589`
- `tests/test_workspace_confine.py:593`
- `tests/test_workspace_confine.py:594`
- `tests/test_workspace_confine.py:612`

## `_resolve_persisted_session_workspace` — function, line 1865
- **called from:**
- `routes/chat_routes.py:2997`
- `tests/test_workspace_confine.py:627`
- `tests/test_workspace_confine.py:649`
- `tests/test_workspace_confine.py:655`

## `_resolve_workspace_from_message_path` — function, line 1884
- **called from:**
- `routes/chat_routes.py:3193`

## `_session_url_matches_endpoint` — function, line 1915
- **called from:**
- `routes/chat_helpers.py:1004`
- `routes/chat_routes.py:1943`
- `routes/chat_routes.py:2019`
- `routes/chat_routes.py:2097`
- `routes/chat_routes.py:2102`
- `routes/chat_routes.py:2220`
- `routes/chat_routes.py:2232`

## `_clear_orphaned_session_endpoint` — function, line 1928
- **called from:**
- `routes/chat_routes.py:2458`
- `routes/chat_routes.py:3116`
- `tests/test_chatgpt_session_binding.py:77`

## `_endpoint_cache_contains_model` — function, line 1972
- **called from:**
- `routes/chat_routes.py:2021`

## `_is_image_generation_session` — function, line 1992
- **called from:**
- `routes/chat_routes.py:3245`
- `tests/test_chat_image_routing.py:68`
- `tests/test_chat_image_routing.py:77`
- `tests/test_chat_image_routing.py:86`
- `tests/test_chat_image_routing.py:96`
- `tests/test_chat_image_routing.py:105`

## `_first_image_attachment` — function, line 2030
- **called from:**
- `routes/chat_routes.py:4382`

## `_ts_or_zero` — function, line 2053
- **called from:**
- `routes/chat_routes.py:2101`

## `_recover_empty_session_model` — function, line 2060
- **called from:**
- `routes/chat_routes.py:2464`
- `routes/chat_routes.py:3124`
- `tests/test_chatgpt_session_binding.py:78`
- `tests/test_pinned_model_route_selection.py:46`
- `tests/test_pinned_model_route_selection.py:55`
- `tests/test_pinned_model_route_selection.py:64`

## `_reconcile_selected_route_from_request` — function, line 2185
- **called from:**
- `routes/chat_routes.py:2454`
- `routes/chat_routes.py:3115`
- `tests/test_chatgpt_session_binding.py:99`
- `tests/test_chatgpt_session_binding.py:105`
- `tests/test_chatgpt_session_binding.py:114`
- `tests/test_selected_endpoint_header_hydration.py:62`

## `_set_user_time_from_request` — function, line 2293
- **called from:**
- `routes/chat_routes.py:2417`
- `routes/chat_routes.py:2649`
- `tests/test_user_time.py:115`
- `tests/test_user_time.py:131`

## `_parse_selected_note_ids` — function, line 2319
- **called from:**
- `routes/chat_routes.py:2654`
- `tests/test_selected_notes_context.py:15`
- `tests/test_selected_notes_context.py:27`

## `_format_selected_notes_context` — function, line 2343
- **called from:**
- `routes/chat_routes.py:3024`

## `_resolve_prompt_thinking_mode` — function, line 2382
- **called from:**
- `tests/test_prompt_controls_regressions.py:61`
- `tests/test_prompt_controls_regressions.py:62`

## `setup_chat_routes` — function, line 2395
- **called from:**
- `app.py:781`
- `tests/test_api_token_tool_authority.py:563`
- `tests/test_chat_document_owner_context.py:76`
- `tests/test_foreground_model_routing.py:288`
- `tests/test_foreground_model_routing.py:1211`
- `tests/test_history_display_model_hydration.py:513`
- `tests/test_session_load_404s.py:68`

## `chat_endpoint` — function (async), line 2415
- **route:** `POST /api/chat`
- decorator: `router.post("/api/chat", response_model=Dict[str, Any])`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stream` — function (async), line 2635
- **route:** `POST /api/chat_stream`
- decorator: `router.post("/api/chat_stream")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `stream_with_save` — function (async), line 4068
- **called from:**
- `routes/chat_routes.py:5490`

## `_on_research_done` — function, line 4160
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_checkpoint` — function, line 4290
- **called from:**
- `routes/chat_routes.py:4881`
- `routes/chat_routes.py:5411`

## `_image_progress_callback` — function (async), line 4405
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_commit_chat_compaction` — function, line 4491
- **called from:**
- `routes/chat_routes.py:4523`
- `routes/chat_routes.py:4556`
- `routes/chat_routes.py:4565`
- `routes/chat_routes.py:4579`
- `routes/chat_routes.py:4721`
- `routes/chat_routes.py:4792`

## `_safe_stream` — function (async), line 5486
- **called from:**
- `routes/chat_routes.py:5517`
- `routes/chat_routes.py:5522`

## `chat_resume` — function (async), line 5538
- **route:** `GET /api/chat/resume/{session_id}`
- decorator: `router.get("/api/chat/resume/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stop` — function (async), line 5558
- **route:** `POST /api/chat/stop/{session_id}`
- decorator: `router.post("/api/chat/stop/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_finish` — function (async), line 5565
- **route:** `POST /api/chat/finish/{session_id}`
- decorator: `router.post("/api/chat/finish/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `chat_stream_status` — function (async), line 5576
- **route:** `GET /api/chat/stream_status/{session_id}`
- decorator: `router.get("/api/chat/stream_status/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inject_context` — function (async), line 5599
- **route:** `POST /api/inject_context/{session_id}`
- decorator: `router.post("/api/inject_context/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_messages` — function (async), line 5614
- **route:** `GET /api/search`
- decorator: `router.get("/api/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reasoning_control` — function (async), line 5638
- **route:** `GET /api/chat/reasoning-control`
- decorator: `router.get("/api/chat/reasoning-control")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `rewrite_message` — function (async), line 5684
- **route:** `POST /api/rewrite`
- decorator: `router.post("/api/rewrite")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `stream_rewrite` — function (async), line 5721
- **called from:**
- `routes/chat_routes.py:5795`
