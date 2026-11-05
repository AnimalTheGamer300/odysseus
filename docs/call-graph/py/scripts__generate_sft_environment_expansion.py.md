# `scripts/generate_sft_environment_expansion.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `compact_tool_catalog` — function, line 34
- **called from:**
- `scripts/cook_sft_alex_conversations.py:218`
- `scripts/generate_sft_environment_expansion.py:170`
- `scripts/judge_seeded_harness_replay.py:92`
- `scripts/odysseus_conversation_qa.py:412`
- `scripts/odysseus_conversation_qa.py:902`
- `tests/test_odysseus_conversation_qa.py:818`
- `tests/test_odysseus_conversation_qa.py:1119`

## `normalize` — function, line 83
- **called from:**
- `scripts/generate_sft_environment_expansion.py:267`
- `src/agent_loop.py:34856`
- `src/agent_runtime/authority.py:504`
- `src/agent_runtime/authority.py:619`
- `src/agent_runtime/authority.py:621`
- `src/agent_runtime/journal.py:232`
- `src/agent_runtime/journal.py:253`
- `src/agent_runtime/local_model_control.py:50`
- `src/agent_tools/bg_job_tools.py:90`
- `src/agent_tools/document_tools.py:388`
- `src/agent_tools/document_tools.py:389`
- `src/agent_tools/web_tools.py:867`
- `src/agent_tools/web_tools.py:868`
- `src/agent_tools/web_tools.py:1153`
- `src/agent_tools/web_tools.py:1155`
- `src/agent_tools/web_tools.py:1303`
- `src/agent_tools/web_tools.py:1548`
- `src/agent_tools/web_tools.py:1570`
- `src/agent_tools/web_tools_prewave3.py:871`
- `src/agent_tools/web_tools_prewave3.py:872`
- `src/agent_tools/web_tools_prewave3.py:1157`
- `src/agent_tools/web_tools_prewave3.py:1159`
- `src/agent_tools/web_tools_prewave3.py:1307`
- `src/agent_tools/web_tools_prewave3.py:1552`
- `src/agent_tools/web_tools_prewave3.py:1574`
- `src/browser_identity.py:85`
- `src/builtin_actions.py:892`
- `src/tool_approvals.py:410`
- `src/tool_approvals.py:467`
- `src/tool_capabilities.py:1028`
- `src/tool_execution.py:1766`
- `src/upload_handler.py:23`
- `tests/process_resource_helpers.py:17`
- `tests/process_resource_helpers.py:50`
- `tests/test_agent_state_dir_confinement.py:182`
- `tests/test_agent_state_dir_confinement.py:186`
- `tests/test_background_resource_identity.py:119`
- `tests/test_background_resource_identity.py:133`
- `tests/test_background_resource_identity.py:152`
- `tests/test_bg_job_tools.py:68`
- `tests/test_browser_identity_transport.py:148`
- `tests/test_browser_resource_identity.py:295`
- `tests/test_browser_resource_identity.py:304`
- `tests/test_effect_verification_adapters.py:63`
- `tests/test_effect_verification_adapters.py:75`
- `tests/test_effect_verification_adapters.py:225`
- `tests/test_effect_verification_adapters.py:297`
- `tests/test_effect_verification_adapters.py:316`
- `tests/test_effects_foundation.py:149`
- `tests/test_grep_followup_integrity.py:27`
- `tests/test_local_mcp_capabilities.py:890`
- `tests/test_local_mcp_capabilities.py:893`
- `tests/test_local_mcp_capabilities.py:958`
- `tests/test_local_mcp_capabilities.py:959`
- `tests/test_local_mcp_capabilities.py:981`
- `tests/test_local_mcp_capabilities.py:982`
- `tests/test_local_mcp_capabilities.py:988`
- `tests/test_local_mcp_capabilities.py:989`
- `tests/test_local_mcp_capabilities.py:1001`
- `tests/test_local_mcp_capabilities.py:1002`
- … +76 more (grep the name in repo)

## `compact_seed` — function, line 88
- **called from:**
- `scripts/generate_sft_environment_expansion.py:167`

## `compact_environment` — function, line 105
- **called from:**
- `scripts/generate_sft_environment_expansion.py:171`

## `target_owners` — function, line 121
- **called from:**
- `scripts/generate_sft_environment_expansion.py:336`

## `request_variants` — function, line 127
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `validate_case` — function, line 203
- **called from:**
- `scripts/generate_sft_environment_expansion.py:328`
- `scripts/generate_sft_environment_expansion.py:367`
- `tests/test_sft_environment_expansion_runner.py:133`
- `tests/test_sft_environment_expansion_runner.py:149`
- `tests/test_sft_environment_expansion_runner.py:171`
- `tests/test_sft_environment_expansion_runner.py:188`
- `tests/test_sft_environment_expansion_runner.py:205`
- `tests/tools/organizer_smoke.py:301`
- `tests/tools/organizer_smoke.py:357`
- `tests/tools/organizer_smoke.py:382`

## `main` — function, line 294
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
