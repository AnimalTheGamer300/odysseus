# `static/js/panels.js` — definitions & call sites

3 definitions (regex-based, best-effort).
**Exports:** `createPanelLoader`, `loadPanel`, `panelNames`

## `createPanelLoader` — function, line 25
- **called from:**
- `static/js/panels.js:25`
- `static/js/panels.js:48`

## `load` — function, line 27
- **called from:**
- `app.py:1151`
- `app.py:1198`
- `companion/pairing.py:168`
- `core/auth.py:118`
- `core/auth.py:141`
- `core/database.py:1468`
- `core/database.py:1526`
- `core/database.py:1544`
- `routes/backup_routes.py:26`
- `routes/backup_routes.py:32`
- `routes/mcp/mcp_routes.py:446`
- `routes/mcp/mcp_routes.py:540`
- `routes/memory/memory_routes.py:89`
- `routes/memory/memory_routes.py:121`
- `routes/memory/memory_routes.py:152`
- `routes/memory/memory_routes.py:158`
- `routes/memory/memory_routes.py:174`
- `routes/memory/memory_routes.py:217`
- `routes/memory/memory_routes.py:520`
- `routes/prefs_routes.py:20`
- `routes/skills_routes.py:609`
- `routes/skills_routes.py:692`
- `routes/skills_routes.py:884`
- `routes/skills_routes.py:930`
- `routes/skills_routes.py:973`
- `routes/skills_routes.py:994`
- `routes/skills_routes.py:1020`
- `routes/skills_routes.py:1062`
- `routes/skills_routes.py:1077`
- `routes/skills_routes.py:1161`
- `routes/skills_routes.py:1209`
- `routes/skills_routes.py:1229`
- `routes/skills_routes.py:1457`
- `routes/skills_routes.py:1468`
- `routes/skills_routes.py:1494`
- `routes/skills_routes.py:1568`
- `routes/skills_routes.py:1686`
- `routes/skills_routes.py:1733`
- `routes/skills_routes.py:1812`
- `routes/skills_routes.py:1859`
- `routes/skills_routes.py:1878`
- `routes/skills_routes.py:1895`
- `scripts/add_hwfit_models.py:190`
- `scripts/add_hwfit_models.py:365`
- `scripts/agent_migration_manifest.py:73`
- `scripts/backfill_model_release_dates.py:67`
- `scripts/claim_ownerless.py:53`
- `scripts/dump_agent_prompt.py:388`
- `scripts/dump_agent_prompt.py:421`
- `scripts/import_from_vllm_recipes.py:257`
- `scripts/migrate_faiss_to_chroma.py:32`
- `scripts/pr_blocker_audit.py:157`
- `services/hwfit/hf_discovery.py:286`
- `services/hwfit/hf_discovery.py:308`
- `services/hwfit/models.py:273`
- `services/memory/memory_extractor.py:57`
- `services/memory/memory_extractor.py:95`
- `services/memory/memory_extractor.py:699`
- `services/memory/skill_extractor.py:257`
- `services/memory/skills.py:93`
- … +80 more (grep the name in repo)

## `panelNames` — function, line 51
- **called from:**
- `static/js/panels.js:51`
