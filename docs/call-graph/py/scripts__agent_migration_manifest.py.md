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

## `read_json` — function, line 71
- **called from:**
- `scripts/agent_migration_manifest.py:115`
- `scripts/agent_migration_manifest.py:292`

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

## `parse_args` — function, line 561
- **called from:**
- `scripts/_lib/cli.py:112`
- `scripts/agent_migration_manifest.py:617`
- `scripts/agent_migration_manifest.py:621`
- `scripts/backfill_model_release_dates.py:60`
- `scripts/demo_email/seed_demo_emails.py:360`
- `scripts/diffusion_server.py:1492`
- `scripts/dump_agent_prompt.py:382`
- `scripts/hf_download.py:148`
- `scripts/import_from_vllm_recipes.py:252`
- `scripts/mlx_image_server.py:465`
- `scripts/pr_blocker_audit.py:1026`
- `tests/cli/test_research_cli_status.py:33`
- `tests/run_focus.py:300`
- `tests/run_order_report.py:137`

## `main` — function, line 620
- **called from:**
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:218`
- `integrations/codex/scripts/odysseus_api.py:218`
- `scripts/add_hwfit_models.py:422`
- `scripts/agent_migration_manifest.py:635`
- `scripts/backfill_model_release_dates.py:133`
- `scripts/claim_ownerless.py:106`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:341`
- `scripts/index_documents.py:117`
- `scripts/migrate_searxng_settings.py:166`
- `scripts/mlx_image_server.py:470`
- `scripts/pr_blocker_audit.py:1051`
- `tests/run_focus.py:325`
- `tests/run_order_report.py:156`
- `tests/test_agent_migration_manifest.py:302`
- `tests/test_agent_migration_manifest.py:325`
- `tests/test_app.py:98`
- `tests/test_backup_import_skills_dedup.py:112`
- `tests/test_pr_blocker_audit.py:219`
- `tests/test_pr_blocker_audit.py:230`
- `tests/test_pr_blocker_audit.py:255`
- `tests/test_pr_blocker_audit.py:270`
- `tests/test_pr_blocker_audit.py:289`
- `tests/test_pr_blocker_audit.py:307`
- `tests/test_pr_blocker_audit.py:324`
- `tests/test_pr_blocker_audit.py:342`
- `tests/test_pr_blocker_audit.py:362`
- `tests/test_pr_blocker_audit.py:383`
- `tests/test_pr_blocker_audit.py:704`
- `tests/test_pr_blocker_audit.py:716`
- `tests/test_pr_blocker_audit.py:753`
- `tests/test_pr_blocker_audit.py:763`
- `tests/test_pr_blocker_audit.py:802`
- `tests/test_pr_blocker_audit.py:815`
- `tests/test_pr_blocker_audit.py:835`
- `tests/test_pr_blocker_audit.py:853`
- `tests/test_pr_blocker_audit.py:870`
- `tests/test_pr_blocker_audit.py:892`
- `tests/test_pr_blocker_audit.py:919`
- `tests/test_pr_blocker_audit.py:947`
- `tests/test_rag_search_signature.py:22`
- `tests/test_research_session_id_validation.py:55`
- `tests/test_setup_admin_user.py:61`
- `tests/tools/build_oversized_test_split_plan.py:574`
