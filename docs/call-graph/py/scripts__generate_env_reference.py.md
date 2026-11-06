# `scripts/generate_env_reference.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `Read` — class, line 105
- decorator: `dataclass`
- **called from:**
- `scripts/generate_env_reference.py:310`
- `scripts/generate_env_reference.py:319`

## `Read.location` — method, line 114
- decorator: `property`
- **called from:**
- `static/js/compare/index.js:1336`

## `Variable` — class, line 119
- decorator: `dataclass`
- **called from:**
- `scripts/generate_env_reference.py:327`

## `Variable.primary` — method, line 124
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `Variable.defaults` — method, line 129
- decorator: `property`
- **called from:**
- `static/app.js:2767`
- `static/js/galleryEditor.js:2275`

## `Variable.test_only` — method, line 138
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_read_rank` — function, line 142
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `iter_source_files` — function, line 160
- **called from:**
- `scripts/generate_env_reference.py:325`
- `scripts/generate_env_reference.py:1078`

## `_fold` — function, line 177
- **called from:**
- `scripts/generate_env_reference.py:309`

## `_collect_constants` — function, line 194
- **called from:**
- `scripts/generate_env_reference.py:270`

## `_env_name` — function, line 219
- **called from:**
- `scripts/generate_env_reference.py:285`
- `scripts/generate_env_reference.py:289`
- `scripts/generate_env_reference.py:295`
- `scripts/generate_env_reference.py:300`
- `scripts/generate_env_reference.py:304`

## `find_env_reader_helpers` — function, line 230
- **called from:**
- `scripts/generate_env_reference.py:271`

## `scan_file` — function, line 259
- **called from:**
- `scripts/generate_env_reference.py:326`

## `collect` — function, line 323
- **called from:**
- `routes/gallery/gallery_routes.py:118`
- `scripts/diffusion_server.py:404`
- `scripts/generate_env_reference.py:1213`
- `tests/test_agent_evidence_loop.py:107`
- `tests/test_chat_image_routing.py:161`
- `tests/test_completion_boundary.py:316`
- `tests/test_effect_verification_adapters.py:153`
- `tests/test_env_reference.py:93`
- `tests/test_env_reference.py:110`
- `tests/test_env_reference.py:124`
- `tests/test_env_reference.py:139`
- `tests/test_env_reference.py:144`
- `tests/test_env_reference.py:166`
- `tests/test_env_reference.py:180`
- `tests/test_env_reference.py:198`
- `tests/test_llm_core_ollama.py:320`
- `tests/test_nested_invocation_ownership.py:445`
- `tests/test_nested_invocation_ownership.py:456`
- `tests/test_required_read_operation.py:158`
- `tests/test_tool_approval_task_scope.py:310`
- `static/js/features/notes/application/drafts.js:17`

## `naive_line_scan` — function, line 1067
- **called from:**
- `scripts/generate_env_reference.py:1219`
- `tests/test_env_reference.py:109`
- `tests/test_env_reference.py:168`
- `tests/test_env_reference.py:180`

## `check_notes` — function, line 1085
- **called from:**
- `scripts/generate_env_reference.py:1214`
- `tests/test_env_reference.py:144`
- `tests/test_env_reference.py:154`

## `_cell` — function, line 1112
- **called from:**
- `scripts/generate_env_reference.py:1130`
- `scripts/generate_env_reference.py:1139`

## `_read_cell` — function, line 1116
- **called from:**
- `scripts/generate_env_reference.py:1139`

## `_default_cell` — function, line 1128
- **called from:**
- `scripts/generate_env_reference.py:1138`

## `_table` — function, line 1133
- **called from:**
- `scripts/generate_env_reference.py:1156`
- `scripts/pr_blocker_audit.py:735`
- `scripts/pr_blocker_audit.py:737`

## `_sections` — function, line 1144
- **called from:**
- `scripts/generate_env_reference.py:1186`
- `scripts/generate_env_reference.py:1190`

## `render` — function, line 1160
- **called from:**
- `scripts/generate_env_reference.py:1219`
- `src/agent_tools/media_tools.py:493`
- `src/agent_tools/media_tools.py:1002`
- `tests/test_audit_c5_benchmark_evidence.py:2875`
- `tests/test_audit_c5_benchmark_evidence.py:2882`
- `tests/test_audit_c5_benchmark_evidence.py:2892`
- `tests/test_audit_c5_benchmark_evidence.py:2906`
- `tests/test_audit_c5_benchmark_evidence.py:2925`
- `tests/test_audit_c5_benchmark_evidence.py:2933`
- `tests/test_audit_c5_benchmark_evidence.py:2935`
- `tests/test_audit_c5_benchmark_evidence.py:2978`
- `tests/test_audit_c5_benchmark_evidence.py:3001`
- `tests/test_audit_c5_benchmark_evidence.py:3006`
- `tests/test_env_reference.py:168`
- `tests/test_env_reference.py:179`
- `static/js/calendar.js:1664`
- `static/js/calendar.js:2653`
- `static/js/chat.js:3712`
- `static/js/chat.js:4812`
- `static/js/chat.js:5173`
- `static/js/chat.js:6073`
- `static/js/chat.js:6217`
- `static/js/chat.js:7371`
- `static/js/documentLibrary.js:108`
- `static/js/documentLibrary.js:124`
- `static/js/editor/adjustments-worker.js:5`
- `static/js/editor/adjustments-worker.js:20`
- `static/js/editor/build/command-palette.js:22`
- `static/js/editor/build/command-palette.js:56`
- `static/js/editor/build/command-palette.js:64`
- `static/js/editor/build/command-palette.js:67`
- `static/js/editor/build/command-palette.js:68`
- `static/js/editor/layer-panel.js:186`
- `static/js/editor/layer-panel.js:302`
- `static/js/editor/layer-panel.js:440`
- `static/js/editor/layer-panel.js:490`
- `static/js/editor/layer-panel.js:581`
- `static/js/editor/layer-panel.js:613`
- `static/js/editor/layer-panel.js:672`
- `static/js/editor/layer-panel.js:711`
- `static/js/editor/layer-panel.js:725`
- `static/js/editor/layer-panel.js:739`
- `static/js/editor/layer-panel.js:751`
- `static/js/editor/layer-panel.js:795`
- `static/js/editor/layer-panel.js:807`
- `static/js/editor/layer-panel.js:839`
- `static/js/editor/layer-panel.js:918`
- `static/js/editor/layer-panel.js:929`
- `static/js/editor/layer-panel.js:942`
- `static/js/editor/layer-panel.js:962`
- `static/js/editor/layer-panel.js:992`
- `static/js/editor/layer-panel.js:1042`
- `static/js/editor/layer-panel.js:1056`
- `static/js/editor/layer-panel.js:1079`
- `static/js/editor/layer-panel.js:1101`
- `static/js/editor/layer-panel.js:1118`
- `static/js/editor/layer-panel.js:1132`
- `static/js/editor/layer-panel.js:1139`
- `static/js/editor/layer-panel.js:1315`
- `static/js/editor/layer-panel.js:1342`
- … +104 more (grep the name in repo)

## `build` — function, line 1211
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `scripts/generate_env_reference.py:1232`
- `src/agent_runtime/effect_log.py:303`
- `src/agent_runtime/effect_log.py:330`
- `src/agent_trace.py:468`
- `src/agent_trace.py:578`
- `src/agent_trace.py:655`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_env_reference.py:37`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `main` — function, line 1222
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
