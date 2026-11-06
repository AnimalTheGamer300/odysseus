# `scripts/run_sft_environment_expansion.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `CaseTimeoutError` — class, line 59
- **called from:**
- `scripts/run_sft_environment_expansion.py:64`
- `scripts/run_sft_overnight_fixture_flows.py:58`

## `timeout_handler` — function, line 63
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `atomic_json` — function, line 67
- **called from:**
- `scripts/review_sft_environment_expansion.py:98`
- `scripts/review_sft_environment_expansion.py:143`
- `scripts/review_sft_environment_expansion.py:159`
- `scripts/run_sft_environment_expansion.py:206`
- `scripts/run_sft_environment_expansion.py:545`
- `scripts/run_sft_environment_expansion.py:554`
- `scripts/run_sft_environment_expansion.py:567`
- `scripts/run_sft_environment_expansion.py:575`
- `scripts/run_sft_environment_expansion.py:821`

## `install_fixture_environments` — function, line 74
- **called from:**
- `scripts/run_sft_environment_expansion.py:793`
- `tests/test_sft_environment_expansion_runner.py:106`

## `login` — function, line 211
- **called from:**
- `mcp_servers/email_server.py:435`
- `mcp_servers/email_server.py:2560`
- `routes/email/email_helpers.py:270`
- `routes/email/email_helpers.py:1384`
- `routes/email/email_routes.py:7637`
- `routes/email/email_routes.py:7701`
- `scripts/demo_email/seed_demo_emails.py:60`
- `scripts/diffusion_server.py:365`
- `scripts/run_sft_environment_expansion.py:696`
- `scripts/run_sft_environment_expansion.py:733`
- `scripts/run_sft_overnight_fixture_flows.py:774`
- `scripts/sft_email_overseer.py:651`
- `tests/test_auth_event_loop.py:111`

## `create_session` — function, line 239
- **called from:**
- `core/session_manager.py:1113`
- `routes/compare/compare_routes.py:187`
- `routes/history/history_routes.py:1101`
- `routes/research/research_routes.py:849`
- `routes/session_routes.py:656`
- `routes/session_routes.py:1279`
- `routes/webhook/webhook_routes.py:306`
- `routes/webhook/webhook_routes.py:367`
- `scripts/eval_odysseus_contextual_tool_use.py:880`
- `scripts/odysseus_conversation_qa.py:796`
- `scripts/run_sft_environment_expansion.py:697`
- `scripts/run_sft_overnight_fixture_flows.py:570`
- `scripts/sft_email_overseer.py:653`
- `src/agent_tools/session_tools.py:61`
- `src/agent_tools/session_tools.py:460`
- `src/agent_tools/session_tools.py:501`
- `tests/test_admin_listing_authorization.py:45`
- `tests/test_auth_session_revocation.py:52`
- `tests/test_auth_session_revocation.py:53`
- `tests/test_auth_session_revocation.py:96`
- `tests/test_auth_session_revocation.py:97`
- `tests/test_auth_session_revocation.py:98`
- `tests/test_auth_session_revocation.py:110`
- `tests/test_auth_session_revocation.py:111`
- `tests/test_auth_session_revocation.py:124`
- `tests/test_auth_session_revocation.py:125`
- `tests/test_chat_document_owner_context.py:80`
- `tests/test_chatgpt_session_binding.py:42`
- `tests/test_database_test_isolation.py:43`
- `tests/test_delete_user_revokes_api_tokens.py:120`
- `tests/test_history_add_message_validation.py:41`
- `tests/test_history_add_message_validation.py:57`
- `tests/test_history_truncate_validation.py:21`
- `tests/test_odysseus_conversation_qa.py:103`
- `tests/test_session_cwd_persistence.py:24`
- `tests/test_session_discovery_message_count.py:33`
- `tests/test_session_header_persistence.py:23`
- `tests/test_truncate_message_count_regression.py:28`
- `tests/test_truncate_message_count_regression.py:58`

## `stream_turn` — function, line 256
- **called from:**
- `scripts/run_sft_environment_expansion.py:702`
- `scripts/run_sft_overnight_fixture_flows.py:571`
- `scripts/sft_email_overseer.py:668`

## `normalized_tool` — function, line 304
- **called from:**
- `scripts/run_sft_environment_expansion.py:315`
- `scripts/run_sft_environment_expansion.py:329`
- `scripts/run_sft_environment_expansion.py:366`
- `scripts/run_sft_environment_expansion.py:387`
- `scripts/run_sft_environment_expansion.py:408`

## `tool_names` — function, line 311
- **called from:**
- `scripts/run_sft_environment_expansion.py:407`
- `scripts/run_sft_environment_expansion.py:711`
- `scripts/run_sft_overnight_fixture_flows.py:269`
- `scripts/run_sft_overnight_fixture_flows.py:594`
- `scripts/sft_email_overseer.py:685`

## `tool_outputs` — function, line 319
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:270`

## `has_unrecovered_tool_failure` — function, line 323
- **called from:**
- `scripts/run_sft_environment_expansion.py:427`
- `tests/test_sft_environment_expansion_runner.py:77`
- `tests/test_sft_environment_expansion_runner.py:78`

## `compact_evidence` — function, line 343
- **called from:**
- `scripts/judge_seeded_harness_replay.py:94`
- `scripts/run_sft_environment_expansion.py:714`

## `tool_actions` — function, line 363
- **called from:**
- `scripts/run_sft_environment_expansion.py:417`

## `inferred_expected_actions` — function, line 383
- **called from:**
- `scripts/run_sft_environment_expansion.py:416`

## `score_turn` — function, line 405
- **called from:**
- `scripts/run_sft_environment_expansion.py:706`
- `tests/test_sft_environment_expansion_runner.py:22`
- `tests/test_sft_environment_expansion_runner.py:31`
- `tests/test_sft_environment_expansion_runner.py:40`
- `tests/test_sft_environment_expansion_runner.py:51`
- `tests/test_sft_environment_expansion_runner.py:57`
- `tests/test_sft_environment_expansion_runner.py:67`

## `row_dict` — function, line 436
- **called from:**
- `scripts/run_sft_environment_expansion.py:469`
- `scripts/run_sft_environment_expansion.py:472`
- `scripts/run_sft_environment_expansion.py:474`
- `scripts/run_sft_environment_expansion.py:477`

## `OwnerSnapshot` — class, line 440
- **called from:**
- `scripts/run_sft_environment_expansion.py:689`

## `OwnerSnapshot.__init__` — method, line 443
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

## `OwnerSnapshot.capture` — method, line 452
- **called from:**
- `routes/shell_routes.py:739`
- `scripts/css_snapshot.py:258`
- `scripts/run_sft_environment_expansion.py:695`
- `scripts/verify_notes_browser_runtime.py:74`
- `src/agent_tools/web_tools.py:115`
- `src/agent_tools/web_tools_prewave3.py:119`
- `src/bg_jobs.py:162`
- `src/containment.py:475`
- `src/containment.py:1096`
- `src/containment.py:1127`
- `src/containment.py:1254`
- `src/process_lifecycle.py:122`
- `tests/test_ai_interaction_owner_scope.py:52`
- `tests/test_ai_interaction_owner_scope.py:57`
- `tests/test_css_computed_style_snapshot.py:94`
- `tests/test_css_computed_style_snapshot.py:103`
- `tests/test_css_computed_style_snapshot.py:152`
- `tests/test_css_computed_style_snapshot.py:153`
- `tests/test_css_computed_style_snapshot.py:166`
- `tests/test_css_computed_style_snapshot.py:183`
- `tests/test_css_computed_style_snapshot.py:186`
- `tests/test_notes_native_cleanup.py:24`
- `tests/test_notes_native_cleanup.py:28`
- `tests/test_process_lifecycle.py:185`
- `tests/test_process_lifecycle.py:242`
- `tests/test_process_ownership.py:103`
- `tests/test_process_ownership.py:152`
- `static/js/signature.js:4`
- `static/js/signature.js:379`
- `static/js/signature.js:517`

## `OwnerSnapshot.restore` — method, line 498
- **called from:**
- `scripts/run_sft_environment_expansion.py:726`
- `tests/test_context_compactor.py:436`
- `tests/test_context_compactor.py:450`
- `tests/test_context_compactor.py:466`
- `tests/test_context_compactor.py:631`
- `tests/test_context_compactor.py:640`
- `tests/test_context_compactor.py:651`
- `tests/test_context_compactor.py:663`
- `tests/test_context_compactor.py:678`
- `tests/test_context_compactor.py:689`
- `static/js/admin.js:1237`
- `static/js/admin.js:1259`
- `static/js/admin.js:1268`
- `static/js/calendar.js:4253`
- `static/js/cookbook.js:3533`
- `static/js/editor/document-geometry.js:88`
- `static/js/editor/layer-panel.js:2170`
- `static/js/editor/mask-ops.js:58`
- `static/js/editor/mask-utils.js:117`
- `static/js/editor/precision-guides.js:122`
- `static/js/editor/precision-guides.js:186`
- `static/js/editor/select-and-mask.js:149`
- `static/js/editor/selection-mask.js:265`
- `static/js/editor/stroke-pipeline.js:66`
- `static/js/editor/stroke-pipeline.js:80`
- `static/js/editor/stroke-pipeline.js:116`
- `static/js/editor/stroke-pipeline.js:200`
- `static/js/editor/stroke-pipeline.js:279`
- `static/js/editor/text-layer.js:370`
- `static/js/editor/tools/crop.js:188`
- `static/js/editor/tools/pen-selection.js:139`
- `static/js/editor/tools/transform-handles.js:275`
- `static/js/editor/tools/transform-session.js:573`
- `static/js/editor/tools/transform-session.js:580`
- `static/js/editor/tools/transform-session.js:586`
- `static/js/features/notes/ui/drawing.js:181`
- `static/js/features/notes/ui/drawing.js:292`
- `static/js/features/notes/ui/drawing.js:312`
- `static/js/gallery.js:2270`
- `static/js/galleryEditor.js:3857`
- `static/js/galleryEditor.js:3941`
- `static/js/galleryEditor.js:4111`
- `static/js/galleryEditor.js:4130`
- `static/js/galleryEditor.js:6830`
- `static/js/galleryEditor.js:7684`
- `static/js/galleryEditor.js:8194`
- `static/js/galleryEditor.js:8437`
- `static/js/galleryEditor.js:11177`
- `static/js/galleryEditor.js:12290`
- `static/js/galleryEditor.js:12438`
- `static/js/galleryEditor.js:12455`
- `static/js/galleryEditor.js:12472`
- `static/js/galleryEditor.js:12609`
- `static/js/galleryEditor.js:12609`
- `static/js/galleryEditor.js:12626`
- `static/js/galleryEditor.js:12688`
- `static/js/galleryEditor.js:12688`
- `static/js/galleryEditor.js:13365`
- `static/js/modalManager.js:387`
- `static/js/modalManager.js:944`
- … +7 more (grep the name in repo)

## `marker_fields` — function, line 578
- **called from:**
- `scripts/run_sft_environment_expansion.py:582`
- `scripts/run_sft_environment_expansion.py:584`
- `scripts/run_sft_environment_expansion.py:598`

## `apply_fixture_plan` — function, line 588
- **called from:**
- `scripts/run_sft_environment_expansion.py:698`

## `delete_session` — function, line 644
- **called from:**
- `routes/session_routes.py:449`
- `routes/session_routes.py:918`
- `routes/session_routes.py:943`
- `routes/session_routes.py:980`
- `routes/session_routes.py:981`
- `routes/session_routes.py:1483`
- `routes/session_routes.py:1496`
- `scripts/run_sft_environment_expansion.py:740`
- `scripts/run_sft_overnight_fixture_flows.py:580`
- `src/agent_tools/session_tools.py:404`
- `tests/test_chat_image_preservation.py:28`
- `tests/test_chat_image_preservation.py:31`
- `tests/test_session_ghost_delete.py:123`
- `tests/test_session_ghost_delete.py:133`
- `tests/test_session_manager.py:106`

## `annotate_trace` — function, line 649
- **called from:**
- `scripts/run_sft_environment_expansion.py:735`

## `run_case` — function, line 681
- **called from:**
- `scripts/eval_followup_domain_continuity.py:183`
- `scripts/eval_odysseus_everyday_live_hard.py:554`
- `scripts/eval_odysseus_live_hard_direct.py:242`
- `scripts/eval_odysseus_tool_use.py:1434`
- `scripts/eval_qwen35_document_shape_direct.py:271`
- `scripts/eval_qwen35_implicit_memory.py:223`
- `scripts/eval_qwen35_tool_router_extended.py:503`
- `scripts/run_sft_environment_expansion.py:819`
- `scripts/run_sft_overnight_fixture_flows.py:782`
- `tests/test_eval_script_contract.py:204`
- `tests/test_eval_script_contract.py:266`

## `main` — function, line 753
- **called from:**
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:218`
- `integrations/codex/scripts/odysseus_api.py:218`
- `scripts/add_hwfit_models.py:512`
- `scripts/agent_migration_manifest.py:635`
- `scripts/analyze_odysseus_eval_targets.py:180`
- `scripts/assemble_sft_clean_corpus.py:74`
- `scripts/audit_c5_benchmark_evidence.py:1637`
- `scripts/audit_email_sft_with_deepseek.py:323`
- `scripts/audit_historical_tool_routing.py:121`
- `scripts/audit_sft_corpus_with_deepseek.py:344`
- `scripts/audit_typo_tool_routing.py:99`
- `scripts/backfill_model_release_dates.py:136`
- `scripts/build_frontend.py:148`
- `scripts/build_historical_harness_queue.py:333`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:274`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:353`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:361`
- `scripts/build_odysseus_search_teacher_edited_rows.py:267`
- `scripts/build_odysseus_sft_repair_manifest.py:230`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:447`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:557`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:519`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:551`
- `scripts/build_odysseus_v61_app_route_web_rows.py:394`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:288`
- `scripts/build_odysseus_web_teacher_sft.py:500`
- `scripts/build_odysseus_web_v53_repair_sft.py:483`
- `scripts/build_sft_environment_inventories.py:97`
- `scripts/build_sft_expansion_manifest.py:161`
- `scripts/build_sft_expansion_splits.py:110`
- `scripts/build_v66_calendar_heldout_cases.py:113`
- `scripts/check_brotli.py:122`
- `scripts/check_ca_trust.py:180`
- `scripts/claim_ownerless.py:106`
- `scripts/cook_sft_alex_conversations.py:298`
- `scripts/css_snapshot.py:295`
- `scripts/curate_public_search_seed_cases.py:324`
- `scripts/curate_sft_trace_run.py:178`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/eval_ajax_basic_tools.py:71`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:400`
- `scripts/eval_odysseus_contextual_tool_use.py:944`
- `scripts/eval_odysseus_crud.py:925`
- `scripts/eval_odysseus_everyday_live_hard.py:590`
- `scripts/eval_odysseus_live_hard_direct.py:261`
- `scripts/eval_odysseus_live_hard_examples.py:468`
- `scripts/eval_odysseus_tool_use.py:1490`
- `scripts/eval_qwen35_document_shape_direct.py:303`
- `scripts/eval_qwen35_implicit_memory.py:279`
- `scripts/eval_qwen35_tool_router_extended.py:571`
- `scripts/filter_sft_seed_hygiene.py:90`
- `scripts/generate_env_reference.py:1270`
- `scripts/generate_sft_environment_expansion.py:399`
- `scripts/generate_sft_flow_variants_with_kimi.py:211`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:348`
- `scripts/index_documents.py:117`
- … +139 more (grep the name in repo)
