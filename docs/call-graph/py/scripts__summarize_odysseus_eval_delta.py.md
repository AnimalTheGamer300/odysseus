# `scripts/summarize_odysseus_eval_delta.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_infra_failure_error` — function, line 22
- **called from:**
- `scripts/analyze_odysseus_eval_targets.py:66`
- `scripts/eval_odysseus_tool_use.py:1121`
- `scripts/summarize_odysseus_eval_delta.py:52`

## `_record_has_infra_error` — function, line 45
- **called from:**
- `scripts/analyze_odysseus_eval_targets.py:70`
- `scripts/analyze_odysseus_eval_targets.py:124`
- `scripts/analyze_odysseus_eval_targets.py:125`
- `scripts/summarize_odysseus_eval_delta.py:86`

## `_load` — function, line 55
- **called from:**
- `core/auth.py:126`
- `routes/prefs_routes.py:32`
- `routes/prefs_routes.py:58`
- `scripts/analyze_odysseus_eval_targets.py:122`
- `scripts/summarize_odysseus_eval_delta.py:147`
- `scripts/summarize_odysseus_eval_delta.py:150`
- `src/agent_runtime/process_resources.py:171`
- `src/bg_jobs.py:175`
- `src/bg_jobs.py:244`
- `src/bg_jobs.py:363`
- `src/bg_jobs.py:375`
- `src/bg_jobs.py:387`
- `src/bg_jobs.py:397`
- `src/bg_jobs.py:413`
- `src/bg_jobs.py:457`
- `src/foreground_model_routing.py:51`
- `src/mcp_oauth.py:140`
- `src/mcp_oauth.py:148`
- `src/tools/research.py:55`
- `src/tools/research.py:82`
- `tests/cli/test_preset_cli_store.py:12`
- `tests/test_auth_config_lock_concurrency.py:83`
- `tests/test_background_resource_identity.py:39`
- `tests/test_background_resource_identity.py:114`
- `tests/test_background_resource_identity.py:259`
- `tests/test_background_resource_identity.py:270`
- `tests/test_bg_job_tools.py:55`
- `tests/test_bg_jobs_store.py:11`
- `tests/test_bg_jobs_store.py:28`
- `tests/test_foreground_model_routing.py:2105`
- `tests/test_foreground_model_routing.py:2186`
- `tests/test_gpu_compose_standalone.py:74`
- `tests/test_gpu_compose_standalone.py:81`
- `tests/test_gpu_compose_standalone.py:82`
- `tests/test_gpu_compose_standalone.py:87`
- `tests/test_gpu_compose_standalone.py:88`
- `tests/test_gpu_compose_standalone.py:97`
- `tests/test_gpu_compose_standalone.py:107`
- `tests/test_gpu_compose_standalone.py:115`
- `tests/test_gpu_compose_standalone.py:142`
- `tests/test_gpu_compose_standalone.py:171`
- `tests/test_gpu_compose_standalone.py:182`
- `tests/test_gpu_compose_standalone.py:183`
- `tests/test_gpu_compose_standalone.py:199`
- `tests/test_gpu_compose_standalone.py:200`
- `tests/test_mcp_oauth.py:116`
- `tests/test_orphan_reaping.py:357`
- `tests/test_orphan_reaping.py:382`
- `tests/test_orphan_reaping.py:392`
- `tests/test_prefs_routes.py:11`
- `tests/test_prefs_routes.py:39`
- `tests/test_runtime_resource_integration.py:272`
- `tests/test_search_query_nonstring.py:26`
- `tests/test_search_query_nonstring.py:37`
- `tests/test_wave3_background_followup.py:35`
- `static/js/workspace.js:109`
- `static/js/workspace.js:152`
- `static/js/workspace.js:212`

## `_records_by_case` — function, line 60
- **called from:**
- `scripts/summarize_odysseus_eval_delta.py:109`
- `scripts/summarize_odysseus_eval_delta.py:110`

## `_metric` — function, line 68
- **called from:**
- `scripts/analyze_odysseus_eval_targets.py:100`
- `scripts/analyze_odysseus_eval_targets.py:101`
- `scripts/analyze_odysseus_eval_targets.py:128`
- `scripts/analyze_odysseus_eval_targets.py:129`
- `scripts/analyze_odysseus_eval_targets.py:133`
- `scripts/analyze_odysseus_eval_targets.py:134`
- `scripts/analyze_odysseus_eval_targets.py:139`
- `scripts/summarize_odysseus_eval_delta.py:119`
- `scripts/summarize_odysseus_eval_delta.py:120`
- `scripts/summarize_odysseus_eval_delta.py:121`
- `scripts/summarize_odysseus_eval_delta.py:122`

## `_fmt_num` — function, line 73
- **called from:**
- `scripts/summarize_odysseus_eval_delta.py:129`
- `scripts/summarize_odysseus_eval_delta.py:129`
- `scripts/summarize_odysseus_eval_delta.py:131`
- `scripts/summarize_odysseus_eval_delta.py:131`
- `scripts/summarize_odysseus_eval_delta.py:133`
- `scripts/summarize_odysseus_eval_delta.py:133`

## `_print_summary` — function, line 81
- **called from:**
- `scripts/summarize_odysseus_eval_delta.py:148`
- `scripts/summarize_odysseus_eval_delta.py:152`

## `_print_delta` — function, line 108
- **called from:**
- `scripts/summarize_odysseus_eval_delta.py:154`

## `main` — function, line 141
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
