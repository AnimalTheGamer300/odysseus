# `scripts/css_snapshot.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `load_inventory` — function, line 61
- **called from:**
- `scripts/css_snapshot.py:115`
- `tests/test_css_computed_style_snapshot.py:54`
- `tests/test_css_computed_style_snapshot.py:88`
- `tests/test_css_computed_style_snapshot.py:143`

## `load_baseline` — function, line 66
- **called from:**
- `scripts/css_snapshot.py:284`
- `tests/test_css_computed_style_snapshot.py:55`
- `tests/test_css_computed_style_snapshot.py:111`

## `_canonical` — function, line 71
- **called from:**
- `scripts/css_snapshot.py:76`

## `_hash` — function, line 75
- **called from:**
- `scripts/css_snapshot.py:157`
- `scripts/css_snapshot.py:160`
- `scripts/css_snapshot.py:162`

## `node_available` — function, line 79
- **called from:**
- `scripts/css_snapshot.py:90`

## `playwright_available` — function, line 84
- **called from:**
- `scripts/css_snapshot.py:249`
- `tests/test_css_computed_style_snapshot.py:21`

## `capture` — function, line 99
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

## `summarize` — function, line 141
- **called from:**
- `scripts/css_snapshot.py:268`
- `src/background_tool_jobs.py:155`
- `tests/test_css_computed_style_snapshot.py:110`
- `tests/test_css_computed_style_snapshot.py:168`
- `tests/test_css_computed_style_snapshot.py:168`
- `tests/test_css_computed_style_snapshot.py:182`
- `tests/test_css_computed_style_snapshot.py:185`
- `tests/test_email_summary_llm.py:274`
- `tests/test_email_summary_llm.py:344`

## `compare` — function, line 168
- **called from:**
- `scripts/css_snapshot.py:285`
- `tests/test_css_computed_style_snapshot.py:111`
- `tests/test_css_computed_style_snapshot.py:191`

## `serve_repository` — function, line 184
- **called from:**
- `scripts/css_snapshot.py:256`
- `tests/test_css_computed_style_snapshot.py:92`
- `tests/test_css_computed_style_snapshot.py:150`

## `Handler` — class, line 192
- **called from:**
- `tests/test_edit_image_tool.py:161`

## `Handler.__init__` — method, line 193
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

## `Handler.log_message` — method, line 196
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Handler.guess_type` — method, line 199
- **called from:**
- `routes/email/email_helpers.py:657`
- `routes/upload_routes.py:484`
- `routes/upload_routes.py:588`
- `scripts/agent_migration_manifest.py:411`
- `scripts/css_snapshot.py:204`
- `src/agent_tools/media_tools.py:1855`
- `src/ai_interaction.py:1629`
- `src/ai_interaction.py:1961`
- `src/document_processor.py:379`
- `src/document_processor.py:822`
- `src/media_ingress.py:199`
- `src/tools/image.py:53`
- `src/upload_handler.py:353`
- `src/upload_handler.py:1076`
- `tests/conftest.py:209`

## `Server` — class, line 206
- **called from:**
- `app.py:1517`
- `mcp_servers/email_server.py:37`
- `mcp_servers/image_gen_server.py:21`
- `mcp_servers/memory_server.py:22`
- `mcp_servers/rag_server.py:18`
- `scripts/css_snapshot.py:209`
- `tests/test_codeql_python_residual_closure.py:559`

## `shutdown` — function, line 213
- **called from:**
- `mcp_servers/email_server.py:428`
- `mcp_servers/email_server.py:440`
- `routes/email/email_helpers.py:1327`
- `routes/email/email_helpers.py:1392`
- `scripts/css_snapshot.py:214`
- `scripts/css_snapshot.py:261`
- `src/service_health.py:194`
- `tests/conftest.py:241`
- `tests/smoke/stub_provider.py:164`
- `tests/test_caldav_redirect_hardening.py:118`
- `tests/test_caldav_redirect_hardening.py:119`
- `tests/test_css_computed_style_snapshot.py:98`
- `tests/test_css_computed_style_snapshot.py:170`
- `tests/test_editor_planner_ssrf_authorization.py:45`
- `tests/test_gallery_endpoint_enforcement.py:45`
- `tests/test_webhook_dns_rebinding_pin.py:107`
- `tests/test_webhook_dns_rebinding_pin.py:156`

## `_describe` — function, line 220
- **called from:**
- `scripts/css_snapshot.py:290`
- `tests/test_vision_description_provenance.py:79`
- `tests/test_vision_description_provenance.py:113`
- `tests/test_vision_description_provenance.py:119`

## `main` — function, line 232
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
