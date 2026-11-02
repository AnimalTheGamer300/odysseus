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
- `scripts/add_hwfit_models.py:375`
- `src/agent_tools/model_interaction_tools.py:215`

## `generate` — function, line 329
- **route:** `POST /v1/images/generations`
- decorator: `app.post("/v1/images/generations")`
- **called from:**
- `routes/shell_routes.py:1110`
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
