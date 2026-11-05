# `services/skills/publication.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `auto_publish_policy` — function, line 11
- **called from:**
- `services/skills/publication.py:113`
- `services/skills/publication.py:298`

## `duplicate_blocker` — function, line 31
- **called from:**
- `services/skills/audit_workflow.py:40`
- `services/skills/publication.py:316`

## `_tokens` — function, line 40
- **called from:**
- `services/skills/publication.py:55`
- `services/skills/publication.py:55`
- `src/agent_loop.py:20540`
- `src/agent_loop.py:20558`
- `tests/test_process_lifecycle.py:319`
- `tests/test_process_lifecycle.py:325`
- `tests/test_process_lifecycle.py:330`
- `tests/test_process_lifecycle.py:339`

## `_sim` — function, line 54
- **called from:**
- `services/skills/publication.py:82`

## `_base` — function, line 60
- **called from:**
- `services/skills/publication.py:82`
- `services/skills/publication.py:82`
- `tests/test_internal_api_base.py:19`
- `tests/test_internal_api_base.py:23`
- `tests/test_internal_api_base.py:28`
- `tests/test_internal_api_base.py:34`

## `_score` — function, line 63
- **called from:**
- `src/agent_tools/web_tools.py:2242`
- `src/agent_tools/web_tools_prewave3.py:2246`

## `finalize_batch` — function, line 103
- **called from:**
- `routes/skills_routes.py:187`
- `services/skills/audit_workflow.py:389`
- `tests/test_skills_audit_services.py:308`

## `tokens` — function, line 125
- **called from:**
- `services/skills/publication.py:138`
- `services/skills/publication.py:138`
- `static/js/censor.js:38`
- `static/js/chat.js:9238`

## `similar` — function, line 137
- **called from:**
- `services/skills/publication.py:193`

## `base` — function, line 141
- **called from:**
- `services/skills/publication.py:193`
- `services/skills/publication.py:193`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:269`

## `score` — function, line 144
- **called from:**
- `scripts/run_sft_overnight_fixture_flows.py:573`
- `scripts/select_sft_expansion_seeds.py:115`
- `scripts/select_sft_expansion_seeds.py:127`
- `tests/test_sft_overnight_fixture_flows.py:115`

## `find` — function, line 180
- **called from:**
- `mcp_servers/email_server.py:2783`
- `routes/calendar_routes.py:154`
- `routes/contacts/contacts_routes.py:388`
- `routes/contacts/contacts_routes.py:389`
- `routes/contacts/contacts_routes.py:610`
- `routes/editor_agent_routes.py:1206`
- `routes/email/email_routes.py:1581`
- `routes/email/email_routes.py:1584`
- `routes/session_routes.py:1622`
- `routes/shell_routes.py:549`
- `routes/shell_routes.py:550`
- `scripts/agent_migration_manifest.py:353`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:141`
- `scripts/build_odysseus_v61_app_route_web_rows.py:65`
- `scripts/migrate_searxng_settings.py:47`
- `services/memory/memory_extractor.py:568`
- `services/memory/memory_extractor.py:1069`
- `services/memory/skill_extractor.py:89`
- `services/memory/skill_extractor.py:98`
- `services/memory/skill_format.py:166`
- `services/search/content.py:120`
- `services/search/content.py:123`
- `services/search/content.py:136`
- `services/search/content.py:139`
- `services/search/content.py:142`
- `services/search/content.py:189`
- `services/search/content.py:190`
- `services/search/content.py:192`
- `services/search/content.py:262`
- `services/search/content.py:262`
- `services/search/content.py:466`
- `services/search/content.py:470`
- `services/search/content.py:485`
- `services/search/content.py:485`
- `services/search/content.py:515`
- `services/skills/evaluation.py:77`
- `services/skills/evaluation.py:300`
- `services/skills/evaluation.py:395`
- `services/skills/publication.py:187`
- `services/skills/publication.py:187`
- `services/skills/publication.py:197`
- `src/agent_loop.py:2286`
- `src/agent_loop.py:2626`
- `src/agent_loop.py:2637`
- `src/agent_loop.py:2642`
- `src/agent_loop.py:4872`
- `src/agent_loop.py:5265`
- `src/agent_loop.py:5266`
- `src/agent_loop.py:5273`
- `src/agent_loop.py:5281`
- `src/agent_loop.py:5284`
- `src/agent_loop.py:5356`
- `src/agent_loop.py:5359`
- `src/agent_loop.py:5362`
- `src/agent_loop.py:5410`
- `src/agent_loop.py:5423`
- `src/agent_loop.py:5435`
- `src/agent_loop.py:5442`
- `src/agent_loop.py:5534`
- `src/agent_loop.py:5543`
- … +618 more (grep the name in repo)

## `unite` — function, line 186
- **called from:**
- `services/skills/publication.py:194`
- `static/js/skills.js:401`

## `audit_flag_text` — function, line 234
- **called from:**
- `services/skills/publication.py:279`

## `utility_blocker` — function, line 246
- **called from:**
- `services/skills/publication.py:303`

## `finalize_status` — function, line 288
- **called from:**
- `routes/skills_routes.py:201`
- `services/skills/audit_workflow.py:220`
- `services/skills/audit_workflow.py:232`
- `services/skills/audit_workflow.py:260`
- `services/skills/audit_workflow.py:297`
- `tests/test_skills_audit_services.py:290`

## `apply_markdown` — function, line 328
- **called from:**
- `services/skills/audit_workflow.py:97`
- `services/skills/audit_workflow.py:209`
- `services/skills/audit_workflow.py:242`
- `services/skills/audit_workflow.py:277`
