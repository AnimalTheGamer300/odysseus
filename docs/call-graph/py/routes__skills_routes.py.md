# `routes/skills_routes.py` — definitions & call sites

59 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SkillAddRequest` — class, line 37
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SkillImportUrlRequest` — class, line 67
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SkillUpdateRequest` — class, line 71
- **called from:**
- `tests/test_skills_routes_owner_update.py:90`

## `_skill_test_task` — function, line 94
- **called from:**
- `routes/skills_routes.py:936`
- `routes/skills_routes.py:1503`
- `src/builtin_actions.py:1984`
- `tests/test_skills_routes_nondict.py:22`
- `tests/test_skills_routes_nondict.py:23`

## `_skill_test_messages` — function, line 111
- **called from:**
- `routes/skills_routes.py:464`
- `routes/skills_routes.py:744`
- `routes/skills_routes.py:1636`
- `tests/test_skills_routes_nondict.py:31`

## `_eval_skill_run` — function (async), line 128
- **called from:**
- `routes/skills_routes.py:522`
- `routes/skills_routes.py:802`

## `_clip` — function, line 170
- **called from:**
- `routes/skills_routes.py:179`

## `_parse` — function, line 183
- **called from:**
- `routes/skills_routes.py:272`
- `src/copilot.py:207`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/emailLibrary.js:3637`
- `static/js/emailLibrary.js:3638`

## `_coerce` — function, line 192
- **called from:**
- `routes/skills_routes.py:203`
- `routes/skills_routes.py:216`
- `src/agent_tools/admin_tools.py:671`

## `_eval_skill_necessity` — function (async), line 282
- **called from:**
- `routes/skills_routes.py:888`

## `_should_check_retrieval_precision` — function, line 338
- **called from:**
- `routes/skills_routes.py:917`
- `tests/test_skills_routes_nondict.py:24`
- `tests/test_skills_routes_nondict.py:25`

## `_eval_skill_retrieval_precision` — function (async), line 362
- **called from:**
- `routes/skills_routes.py:918`

## `_run_skill_test_job` — function (async), line 432
- **called from:**
- `routes/skills_routes.py:1558`
- `routes/skills_routes.py:1666`
- `tests/test_skills_routes_nondict.py:96`

## `_flush_say` — function, line 459
- **called from:**
- `routes/skills_routes.py:480`
- `routes/skills_routes.py:485`
- `routes/skills_routes.py:507`
- `routes/skills_routes.py:512`
- `routes/skills_routes.py:514`

## `_audit_auto_publish_policy` — function, line 548
- **called from:**
- `routes/skills_routes.py:690`

## `_skill_duplicate_blocker` — function, line 568
- **called from:**
- `routes/skills_routes.py:702`
- `routes/skills_routes.py:899`

## `_tokens` — function, line 577
- **called from:**
- `routes/skills_routes.py:592`
- `routes/skills_routes.py:592`

## `_sim` — function, line 591
- **called from:**
- `routes/skills_routes.py:619`

## `_base` — function, line 597
- **called from:**
- `routes/skills_routes.py:619`
- `routes/skills_routes.py:619`
- `tests/test_internal_api_base.py:19`
- `tests/test_internal_api_base.py:23`
- `tests/test_internal_api_base.py:28`
- `tests/test_internal_api_base.py:34`

## `_score` — function, line 600
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_audit_flag_text` — function, line 640
- **called from:**
- `routes/skills_routes.py:666`
- `routes/skills_routes.py:671`

## `_audit_generic_blocker` — function, line 652
- **called from:**
- `routes/skills_routes.py:693`
- `routes/skills_routes.py:898`

## `_audit_finalize_status` — function, line 680
- **called from:**
- `routes/skills_routes.py:974`
- `routes/skills_routes.py:979`
- `routes/skills_routes.py:995`
- `routes/skills_routes.py:1021`

## `_apply_skill_md` — function, line 714
- **called from:**
- `routes/skills_routes.py:928`
- `routes/skills_routes.py:970`
- `routes/skills_routes.py:986`
- `routes/skills_routes.py:1009`

## `_run_skill_test_once` — function (async), line 738
- **called from:**
- `routes/skills_routes.py:938`
- `routes/skills_routes.py:988`
- `routes/skills_routes.py:1012`
- `src/builtin_actions.py:1986`
- `tests/test_skills_routes_nondict.py:59`

## `_improve_skill_md` — function (async), line 806
- **called from:**
- `routes/skills_routes.py:922`
- `routes/skills_routes.py:968`
- `routes/skills_routes.py:985`
- `routes/skills_routes.py:1008`

## `_audit_one_skill` — function (async), line 853
- **called from:**
- `routes/skills_routes.py:1067`

## `_set_conf` — function, line 863
- **called from:**
- `routes/skills_routes.py:971`
- `routes/skills_routes.py:992`
- `routes/skills_routes.py:1016`

## `_run_audit_all_job` — function (async), line 1040
- **called from:**
- `routes/skills_routes.py:1178`
- `routes/skills_routes.py:1772`
- `src/builtin_actions.py:2088`

## `log` — function, line 1049
- **called from:**
- `routes/skills_routes.py:871`
- `routes/skills_routes.py:894`
- `routes/skills_routes.py:896`
- `routes/skills_routes.py:911`
- `routes/skills_routes.py:921`
- `routes/skills_routes.py:934`
- `routes/skills_routes.py:937`
- `routes/skills_routes.py:940`
- `routes/skills_routes.py:954`
- `routes/skills_routes.py:967`
- `routes/skills_routes.py:975`
- `routes/skills_routes.py:980`
- `routes/skills_routes.py:984`
- `routes/skills_routes.py:990`
- `routes/skills_routes.py:996`
- `routes/skills_routes.py:1007`
- `routes/skills_routes.py:1014`
- `routes/skills_routes.py:1022`
- `routes/skills_routes.py:1036`
- `routes/skills_routes.py:1059`
- `routes/skills_routes.py:1071`
- `routes/skills_routes.py:1074`
- `scripts/diffusion_server.py:1221`
- `src/chat_processor.py:215`
- `static/app.js:3884`
- `static/app.js:3887`
- `static/app.js:3888`
- `static/app.js:4593`
- `static/js/cookbookRunning.js:4036`
- `static/js/cookbookSchedule.js:50`
- `static/js/editor/build/controls.js:13`
- `static/js/editor/build/controls.js:13`
- `static/js/editor/fx/adj-popup.js:605`
- `static/js/editor/fx/adj-popup.js:605`
- `static/js/emailLibrary.js:4960`
- `static/js/galleryEditor.js:3002`
- `static/js/galleryEditor.js:3002`
- `static/js/galleryEditor.js:3187`
- `static/js/galleryEditor.js:3187`

## `_resolve_audit_models` — function, line 1103
- **called from:**
- `routes/skills_routes.py:1156`
- `routes/skills_routes.py:1729`
- `src/builtin_actions.py:2065`
- `tests/test_teacher_audit_owner_scope.py:67`

## `run_scheduled_skill_audit` — function (async), line 1140
- **called from:**
- `app.py:1263`

## `setup_skills_routes` — function, line 1183
- **called from:**
- `app.py:698`
- `tests/test_skill_save_no_rename.py:103`
- `tests/test_skills_delete_owner.py:81`
- `tests/test_skills_routes_owner_update.py:84`
- `tests/test_skills_routes_owner_update.py:108`
- `tests/test_skills_routes_owner_update.py:151`

## `_owner` — function, line 1186
- **called from:**
- `routes/assistant_routes.py:126`
- `routes/assistant_routes.py:139`
- `routes/assistant_routes.py:160`
- `routes/assistant_routes.py:272`
- `routes/assistant_routes.py:296`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:296`
- `routes/memory/memory_routes.py:353`
- `routes/memory/memory_routes.py:394`
- `routes/memory/memory_routes.py:505`
- `routes/memory/memory_routes.py:519`
- `routes/memory/memory_routes.py:530`
- `routes/memory/memory_routes.py:552`
- `routes/note/note_routes.py:629`
- `routes/note/note_routes.py:653`
- `routes/note/note_routes.py:690`
- `routes/note/note_routes.py:707`
- `routes/note/note_routes.py:762`
- `routes/note/note_routes.py:781`
- `routes/note/note_routes.py:800`
- `routes/note/note_routes.py:819`
- `routes/note/note_routes.py:858`
- `routes/note/note_routes.py:904`
- `routes/skills_routes.py:1208`
- `routes/skills_routes.py:1217`
- `routes/skills_routes.py:1228`
- `routes/skills_routes.py:1354`
- `routes/skills_routes.py:1382`
- `routes/skills_routes.py:1420`
- `routes/skills_routes.py:1456`
- `routes/skills_routes.py:1467`
- `routes/skills_routes.py:1490`
- `routes/skills_routes.py:1567`
- `routes/skills_routes.py:1685`
- `routes/skills_routes.py:1713`
- `routes/skills_routes.py:1778`
- `routes/skills_routes.py:1792`
- `routes/skills_routes.py:1807`
- `routes/skills_routes.py:1858`
- `routes/skills_routes.py:1877`
- `routes/skills_routes.py:1894`
- `routes/task/task_routes.py:344`
- `routes/task/task_routes.py:375`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:453`
- `routes/task/task_routes.py:566`
- `routes/task/task_routes.py:575`
- `routes/task/task_routes.py:654`
- `routes/task/task_routes.py:668`
- `routes/task/task_routes.py:758`
- `routes/task/task_routes.py:780`
- `routes/task/task_routes.py:796`
- `routes/task/task_routes.py:820`
- … +9 more (grep the name in repo)

## `_verify_owner` — function, line 1189
- **called from:**
- `routes/skills_routes.py:1472`
- `routes/skills_routes.py:1498`
- `routes/skills_routes.py:1575`
- `routes/skills_routes.py:1816`
- `routes/skills_routes.py:1863`
- `routes/skills_routes.py:1882`

## `_fire_skill_added` — function, line 1199
- **called from:**
- `routes/skills_routes.py:1377`
- `routes/skills_routes.py:1410`
- `routes/skills_routes.py:1853`
- `routes/skills_routes.py:1872`

## `list_skills` — function (async), line 1207
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_index` — function (async), line 1213
- **route:** `GET /index`
- decorator: `router.get("/index")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_slash_catalog` — function (async), line 1222
- **route:** `GET /slash-catalog`
- decorator: `router.get("/slash-catalog")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_builtin_skills` — function (async), line 1251
- **route:** `GET /builtin`
- decorator: `router.get("/builtin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_clean` — function, line 1259
- **called from:**
- `routes/skills_routes.py:1281`

## `get_builtin_skill` — function (async), line 1288
- **route:** `GET /builtin/{name}`
- decorator: `router.get("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_builtin_override` — function (async), line 1312
- **route:** `PUT /builtin/{name}`
- decorator: `router.put("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reset_builtin_override` — function (async), line 1338
- **route:** `DELETE /builtin/{name}`
- decorator: `router.delete("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_skill_from_url` — function (async), line 1351
- **route:** `POST /import-from-url`
- decorator: `router.post("/import-from-url")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_skill` — function (async), line 1381
- **route:** `POST /add`
- decorator: `router.post("/add")`
- **called from:**
- `routes/backup_routes.py:150`
- `routes/skills_routes.py:1383`
- `services/memory/skill_extractor.py:276`
- `src/tools/system.py:118`
- `tests/test_skill_frontmatter_escape_roundtrip.py:202`
- `tests/test_skills_manager_owner_isolation.py:253`
- `tests/test_skills_manager_owner_isolation.py:262`

## `invoke_skill` — function (async), line 1414
- **route:** `POST /{skill_id}/invoke`
- decorator: `router.post("/{skill_id}/invoke")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_skill` — function (async), line 1455
- **route:** `GET /{skill_id}`
- decorator: `router.get("/{skill_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_skill_markdown` — function (async), line 1464
- **route:** `GET /{skill_id}/markdown`
- decorator: `router.get("/{skill_id}/markdown")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_skill` — function (async), line 1479
- **route:** `POST /{skill_id}/test`
- decorator: `router.post("/{skill_id}/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `approve_skill_test_action` — function (async), line 1562
- **route:** `POST /{skill_id}/test-approval`
- decorator: `router.post("/{skill_id}/test-approval")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_skill_status` — function (async), line 1683
- **route:** `GET /{skill_id}/test-status`
- decorator: `router.get("/{skill_id}/test-status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `audit_all_skills` — function (async), line 1702
- **route:** `POST /audit-all`
- decorator: `router.post("/audit-all")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `audit_status` — function (async), line 1777
- **route:** `GET /audit-all/status`
- decorator: `router.get("/audit-all/status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `audit_cancel` — function (async), line 1791
- **route:** `POST /audit-all/cancel`
- decorator: `router.post("/audit-all/cancel")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `save_skill_markdown` — function (async), line 1804
- **route:** `POST /{skill_id}/markdown`
- decorator: `router.post("/{skill_id}/markdown")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_skill` — function (async), line 1857
- **route:** `PUT /{skill_id}`
- decorator: `router.put("/{skill_id}")`
- **called from:**
- `routes/skills_routes.py:538`
- `routes/skills_routes.py:708`
- `routes/skills_routes.py:724`
- `routes/skills_routes.py:865`
- `routes/skills_routes.py:903`
- `routes/skills_routes.py:1027`
- `routes/skills_routes.py:1827`
- `routes/skills_routes.py:1868`
- `src/tools/system.py:177`
- `src/tools/system.py:201`
- `src/tools/system.py:214`
- `tests/test_skill_frontmatter_escape_roundtrip.py:205`
- `tests/test_skills_manager_owner_isolation.py:110`
- `tests/test_skills_manager_owner_isolation.py:237`

## `delete_skill` — function (async), line 1876
- **route:** `DELETE /{skill_id}`
- decorator: `router.delete("/{skill_id}")`
- **called from:**
- `routes/skills_routes.py:1883`
- `src/tools/system.py:220`
- `tests/test_skills_delete_owner.py:58`
- `tests/test_skills_delete_owner.py:62`

## `search_skills` — function (async), line 1889
- **route:** `POST /search`
- decorator: `router.post("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
