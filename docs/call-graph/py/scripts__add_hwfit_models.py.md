# `scripts/add_hwfit_models.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_parse_params` — function, line 56
- **called from:**
- `scripts/add_hwfit_models.py:254`
- `scripts/add_hwfit_models.py:257`
- `scripts/add_hwfit_models.py:262`
- `scripts/add_hwfit_models.py:357`

## `_params_from_config` — function, line 76
- **called from:**
- `scripts/add_hwfit_models.py:284`

## `_i` — function, line 102
- **called from:**
- `scripts/add_hwfit_models.py:109`
- `scripts/add_hwfit_models.py:110`
- `scripts/add_hwfit_models.py:114`
- `scripts/add_hwfit_models.py:115`
- `scripts/add_hwfit_models.py:116`
- `scripts/add_hwfit_models.py:117`
- `scripts/add_hwfit_models.py:118`
- `scripts/add_hwfit_models.py:131`
- `scripts/add_hwfit_models.py:131`
- `scripts/add_hwfit_models.py:132`
- `scripts/add_hwfit_models.py:133`
- `scripts/add_hwfit_models.py:134`
- `scripts/add_hwfit_models.py:136`

## `_fetch_config_json` — function, line 170
- **called from:**
- `scripts/add_hwfit_models.py:281`

## `_base_model_tag` — function, line 198
- **called from:**
- `scripts/add_hwfit_models.py:260`
- `scripts/add_hwfit_models.py:277`

## `_quant_from_name` — function, line 206
- **called from:**
- `scripts/add_hwfit_models.py:268`

## `_arch_from_tags` — function, line 242
- **called from:**
- `scripts/add_hwfit_models.py:345`

## `_entry_from_modelinfo` — function, line 251
- **called from:**
- `scripts/add_hwfit_models.py:381`
- `scripts/add_hwfit_models.py:396`

## `main` — function, line 363
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
