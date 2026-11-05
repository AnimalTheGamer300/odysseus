# `scripts/agent_migration_manifest.py` — definitions & call sites

30 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `InputWarning` — class, line 41
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/agent_migration_manifest.py:117`
- `scripts/agent_migration_manifest.py:122`
- `scripts/agent_migration_manifest.py:129`
- `scripts/agent_migration_manifest.py:133`
- `scripts/agent_migration_manifest.py:294`
- `scripts/agent_migration_manifest.py:300`
- `scripts/agent_migration_manifest.py:305`
- `scripts/agent_migration_manifest.py:309`
- `scripts/agent_migration_manifest.py:338`
- `scripts/agent_migration_manifest.py:371`
- `scripts/agent_migration_manifest.py:373`
- `scripts/agent_migration_manifest.py:375`
- `scripts/agent_migration_manifest.py:380`
- `scripts/agent_migration_manifest.py:385`
- `scripts/agent_migration_manifest.py:419`
- `scripts/agent_migration_manifest.py:423`
- `scripts/agent_migration_manifest.py:434`
- `scripts/agent_migration_manifest.py:454`
- `scripts/agent_migration_manifest.py:457`
- `scripts/agent_migration_manifest.py:460`
- `scripts/agent_migration_manifest.py:470`
- `scripts/agent_migration_manifest.py:475`
- `scripts/agent_migration_manifest.py:481`
- `scripts/agent_migration_manifest.py:484`

## `utc_now_iso` — function, line 46
- **called from:**
- `scripts/agent_migration_manifest.py:546`

## `sha256_text` — function, line 50
- **called from:**
- `scripts/agent_migration_manifest.py:131`
- `scripts/agent_migration_manifest.py:313`
- `scripts/agent_migration_manifest.py:391`
- `scripts/agent_migration_manifest.py:400`

## `sha256_bytes` — function, line 54
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sha256_path` — function, line 58
- **called from:**
- `scripts/agent_migration_manifest.py:479`

## `stable_id` — function, line 66
- **called from:**
- `scripts/agent_migration_manifest.py:140`
- `scripts/agent_migration_manifest.py:329`
- `scripts/agent_migration_manifest.py:391`
- `scripts/agent_migration_manifest.py:486`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:272`
- `scripts/build_odysseus_search_teacher_edited_rows.py:199`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:157`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:248`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:290`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:346`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:391`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:359`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:358`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:364`
- `scripts/build_odysseus_v61_app_route_web_rows.py:183`
- `scripts/build_odysseus_v61_app_route_web_rows.py:231`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:117`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:189`
- `scripts/build_odysseus_web_teacher_sft.py:319`
- `scripts/build_odysseus_web_v53_repair_sft.py:345`
- `scripts/curate_public_search_seed_cases.py:82`
- `scripts/curate_public_search_seed_cases.py:148`
- `scripts/run_odysseus_search_teacher_pipeline.py:556`

## `read_json` — function, line 71
- **called from:**
- `scripts/agent_migration_manifest.py:115`
- `scripts/agent_migration_manifest.py:292`
- `scripts/sft_email_overseer.py:145`
- `scripts/sft_email_overseer.py:637`

## `normalize_category` — function, line 76
- **called from:**
- `scripts/agent_migration_manifest.py:136`

## `normalize_memory_text` — function, line 81
- **called from:**
- `scripts/agent_migration_manifest.py:127`

## `memory_metadata` — function, line 92
- **called from:**
- `scripts/agent_migration_manifest.py:145`

## `payload_items` — function, line 104
- **called from:**
- `scripts/agent_migration_manifest.py:119`
- `scripts/agent_migration_manifest.py:296`

## `collect_memory_json` — function, line 112
- **called from:**
- `scripts/agent_migration_manifest.py:511`
- `tests/test_agent_migration_manifest.py:33`
- `tests/test_agent_migration_manifest.py:47`

## `normalize_timestamp` — function, line 151
- **called from:**
- `scripts/agent_migration_manifest.py:228`
- `scripts/agent_migration_manifest.py:325`

## `normalize_role` — function, line 167
- **called from:**
- `scripts/agent_migration_manifest.py:225`

## `content_part_text` — function, line 178
- **called from:**
- `scripts/agent_migration_manifest.py:196`
- `scripts/agent_migration_manifest.py:200`

## `normalize_message_text` — function, line 191
- **called from:**
- `scripts/agent_migration_manifest.py:221`

## `normalize_message` — function, line 212
- **called from:**
- `scripts/agent_migration_manifest.py:251`
- `scripts/agent_migration_manifest.py:268`

## `chatgpt_mapping_messages` — function, line 237
- **called from:**
- `scripts/agent_migration_manifest.py:258`

## `conversation_messages` — function, line 257
- **called from:**
- `scripts/agent_migration_manifest.py:307`

## `conversation_title` — function, line 275
- **called from:**
- `scripts/agent_migration_manifest.py:311`

## `collect_conversation_json` — function, line 283
- **called from:**
- `scripts/agent_migration_manifest.py:521`
- `tests/test_agent_migration_manifest.py:170`
- `tests/test_agent_migration_manifest.py:200`
- `tests/test_agent_migration_manifest.py:243`
- `tests/test_agent_migration_manifest.py:271`

## `parse_skill_frontmatter` — function, line 350
- **called from:**
- `scripts/agent_migration_manifest.py:387`

## `collect_skill_dir` — function, line 368
- **called from:**
- `scripts/agent_migration_manifest.py:516`
- `tests/test_agent_migration_manifest.py:69`
- `tests/test_agent_migration_manifest.py:88`
- `tests/test_agent_migration_manifest.py:101`

## `looks_textual` — function, line 408
- **called from:**
- `scripts/agent_migration_manifest.py:469`

## `iter_archive_dir` — function, line 415
- **called from:**
- `scripts/agent_migration_manifest.py:428`
- `scripts/agent_migration_manifest.py:439`

## `iter_archive_files` — function, line 431
- **called from:**
- `scripts/agent_migration_manifest.py:464`

## `collect_archive_paths` — function, line 442
- **called from:**
- `scripts/agent_migration_manifest.py:531`
- `tests/test_agent_migration_manifest.py:112`
- `tests/test_agent_migration_manifest.py:113`
- `tests/test_agent_migration_manifest.py:129`
- `tests/test_agent_migration_manifest.py:142`
- `tests/test_agent_migration_manifest.py:287`

## `build_manifest` — function, line 506
- **called from:**
- `scripts/agent_migration_manifest.py:622`
- `scripts/build_odysseus_sft_repair_manifest.py:213`
- `tests/test_build_odysseus_sft_repair_manifest.py:41`
- `tests/test_build_odysseus_sft_repair_manifest.py:54`
- `tests/test_build_odysseus_sft_repair_manifest.py:66`
- `tests/test_build_odysseus_sft_repair_manifest.py:74`
- `tests/test_build_odysseus_sft_repair_manifest.py:102`
- `tests/test_build_odysseus_sft_repair_manifest.py:112`
- `tests/test_build_odysseus_sft_repair_manifest.py:126`

## `parse_args` — function, line 561
- **called from:**
- `scripts/_lib/cli.py:112`
- `scripts/agent_migration_manifest.py:617`
- `scripts/agent_migration_manifest.py:621`
- `scripts/analyze_odysseus_eval_targets.py:120`
- `scripts/assemble_sft_clean_corpus.py:24`
- `scripts/audit_c5_benchmark_evidence.py:1558`
- `scripts/audit_email_sft_with_deepseek.py:246`
- `scripts/audit_historical_tool_routing.py:60`
- `scripts/audit_sft_corpus_with_deepseek.py:216`
- `scripts/audit_typo_tool_routing.py:60`
- `scripts/backfill_model_release_dates.py:63`
- `scripts/build_frontend.py:134`
- `scripts/build_historical_harness_queue.py:323`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:238`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:309`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:285`
- `scripts/build_odysseus_search_teacher_edited_rows.py:211`
- `scripts/build_odysseus_sft_repair_manifest.py:208`
- `scripts/build_odysseus_sft_repair_manifest.py:212`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:416`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:427`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:454`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:476`
- `scripts/build_odysseus_v61_app_route_web_rows.py:252`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:208`
- `scripts/build_odysseus_web_teacher_sft.py:378`
- `scripts/build_odysseus_web_v53_repair_sft.py:415`
- `scripts/build_sft_environment_inventories.py:54`
- `scripts/build_sft_expansion_manifest.py:74`
- `scripts/build_sft_expansion_splits.py:25`
- `scripts/build_v66_calendar_heldout_cases.py:49`
- `scripts/check_brotli.py:104`
- `scripts/check_ca_trust.py:139`
- `scripts/cook_sft_alex_conversations.py:248`
- `scripts/cook_sft_alex_conversations.py:252`
- `scripts/css_snapshot.py:247`
- `scripts/curate_public_search_seed_cases.py:262`
- `scripts/curate_sft_trace_run.py:157`
- `scripts/demo_email/seed_demo_emails.py:360`
- `scripts/diffusion_server.py:1492`
- `scripts/dump_agent_prompt.py:382`
- `scripts/eval_ajax_basic_tools.py:32`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:360`
- `scripts/eval_odysseus_contextual_tool_use.py:861`
- `scripts/eval_odysseus_crud.py:800`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_direct.py:67`
- `scripts/eval_odysseus_live_hard_direct.py:232`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_odysseus_tool_use.py:1377`
- `scripts/eval_qwen35_document_shape_direct.py:142`
- `scripts/eval_qwen35_document_shape_direct.py:262`
- `scripts/eval_qwen35_implicit_memory.py:206`
- `scripts/eval_qwen35_tool_router_extended.py:450`
- `scripts/eval_qwen_tool_groups_stream.py:226`
- `scripts/filter_sft_seed_hygiene.py:46`
- `scripts/generate_env_reference.py:1230`
- `scripts/generate_sft_environment_expansion.py:307`
- … +30 more (grep the name in repo)

## `main` — function, line 620
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
