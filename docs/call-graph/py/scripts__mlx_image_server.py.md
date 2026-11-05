# `scripts/mlx_image_server.py` — definitions & call sites

27 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ImageRequest` — class, line 30
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `HarmonizeRequest` — class, line 39
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_steps` — function, line 52
- **called from:**
- `scripts/mlx_image_server.py:343`
- `scripts/mlx_image_server.py:345`
- `scripts/mlx_image_server.py:363`

## `_size` — function, line 58
- **called from:**
- `scripts/mlx_image_server.py:336`

## `_cli_for_model` — function, line 66
- **called from:**
- `scripts/mlx_image_server.py:349`

## `_resolve_cli` — function, line 75
- **called from:**
- `scripts/mlx_image_server.py:139`
- `scripts/mlx_image_server.py:350`

## `_valid_numbers` — function, line 88
- **called from:**
- `scripts/mlx_image_server.py:373`

## `_is_hidream` — function, line 102
- **called from:**
- `scripts/mlx_image_server.py:342`

## `_is_boogu` — function, line 106
- **called from:**
- `scripts/mlx_image_server.py:344`

## `_is_lama_inpaint` — function, line 110
- **called from:**
- `scripts/mlx_image_server.py:346`
- `scripts/mlx_image_server.py:402`
- `scripts/mlx_image_server.py:428`

## `_is_ddcolor` — function, line 115
- **called from:**
- `scripts/mlx_image_server.py:120`
- `scripts/mlx_image_server.py:346`
- `scripts/mlx_image_server.py:402`
- `scripts/mlx_image_server.py:410`
- `scripts/mlx_image_server.py:428`
- `scripts/mlx_image_server.py:437`

## `_unsupported_swift_mlx_runtime` — function, line 119
- **called from:**
- `scripts/mlx_image_server.py:217`
- `scripts/mlx_image_server.py:240`
- `scripts/mlx_image_server.py:347`

## `_resolve_bridge` — function, line 137
- **called from:**
- `scripts/mlx_image_server.py:215`
- `scripts/mlx_image_server.py:238`

## `_snapshot_path` — function, line 145
- **called from:**
- `scripts/mlx_image_server.py:164`
- `scripts/mlx_image_server.py:259`
- `scripts/mlx_image_server.py:298`

## `_weights_path` — function, line 160
- **called from:**
- `scripts/mlx_image_server.py:221`
- `scripts/mlx_image_server.py:246`

## `_write_bridge_input_image` — function, line 173
- **called from:**
- `scripts/mlx_image_server.py:220`
- `scripts/mlx_image_server.py:244`

## `_write_bridge_mask` — function, line 186
- **called from:**
- `scripts/mlx_image_server.py:245`

## `_run_bridge` — function, line 205
- **called from:**
- `scripts/mlx_image_server.py:223`
- `scripts/mlx_image_server.py:248`

## `_run_ddcolor_bridge` — function, line 214
- **called from:**
- `scripts/mlx_image_server.py:411`
- `scripts/mlx_image_server.py:438`

## `_run_inpaint_bridge` — function, line 232
- **called from:**
- `scripts/mlx_image_server.py:413`
- `scripts/mlx_image_server.py:440`

## `_generate_hidream` — function, line 258
- **called from:**
- `scripts/mlx_image_server.py:343`

## `_generate_boogu` — function, line 287
- **called from:**
- `scripts/mlx_image_server.py:345`

## `list_models` — function, line 324
- **route:** `GET /v1/models`
- decorator: `app.get("/v1/models")`
- **called from:**
- `scripts/add_hwfit_models.py:457`
- `src/agent_tools/model_interaction_tools.py:271`
- `tests/test_chatgpt_subscription_routes.py:509`
- `tests/test_list_models_hardware_fit.py:32`

## `generate` — function, line 329
- **route:** `POST /v1/images/generations`
- decorator: `app.post("/v1/images/generations")`
- **called from:**
- `routes/shell_routes.py:1344`
- `scripts/mlx_image_server.py:311`

## `edit_image` — function (async), line 392
- **route:** `POST /v1/images/edits`
- decorator: `app.post("/v1/images/edits")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `harmonize_image` — function, line 426
- **route:** `POST /v1/images/harmonize`
- decorator: `app.post("/v1/images/harmonize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `main` — function, line 451
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
