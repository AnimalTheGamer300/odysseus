# `scripts/dump_agent_prompt.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `classify_endpoint` — function, line 69
- **called from:**
- `scripts/dump_agent_prompt.py:423`

## `pick_finetune_mode` — function, line 123
- **called from:**
- `scripts/dump_agent_prompt.py:147`

## `build` — function, line 133
- **called from:**
- `scripts/dump_agent_prompt.py:424`
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

## `drop_datetime_message` — function, line 265
- **called from:**
- `scripts/dump_agent_prompt.py:448`

## `build_verbatim_payload` — function, line 272
- **called from:**
- `scripts/dump_agent_prompt.py:450`

## `prompt_composition_note` — function, line 339
- **called from:**
- `scripts/dump_agent_prompt.py:498`

## `main` — function, line 350
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

## `_connect_like_app` — function (async), line 402
- **called from:**
- `scripts/dump_agent_prompt.py:415`
