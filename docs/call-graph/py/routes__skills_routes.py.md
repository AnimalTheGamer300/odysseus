# `routes/skills_routes.py` — definitions & call sites

45 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `SkillAddRequest` — class, line 42
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SkillImportUrlRequest` — class, line 72
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `SkillUpdateRequest` — class, line 76
- **called from:**
- `tests/test_skill_rename_collision.py:80`
- `tests/test_skills_routes_owner_update.py:90`

## `_skill_baseline_task` — function, line 102
- **called from:**
- `tests/test_skill_audit_utility.py:16`
- `tests/test_skills_audit_services.py:153`

## `_eval_skill_run` — function (async), line 113
- **called from:**
- `tests/test_skills_audit_characterization.py:340`
- `tests/test_skills_audit_characterization.py:363`
- `tests/test_skills_audit_characterization.py:375`

## `_eval_skill_necessity` — function (async), line 125
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_eval_skill_retrieval_precision` — function (async), line 137
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_skill_test_job` — function (async), line 153
- **called from:**
- `tests/test_skill_test_stream_closed.py:42`
- `tests/test_skills_routes_nondict.py:96`
- `tests/test_skills_routes_nondict.py:162`

## `_finalize_audit_batch` — function, line 186
- **called from:**
- `tests/test_skill_audit_utility.py:98`
- `tests/test_skills_audit_characterization.py:483`

## `_audit_finalize_status` — function, line 198
- **called from:**
- `tests/test_skill_audit_utility.py:62`

## `_run_skill_audit_arm` — function (async), line 213
- **called from:**
- `tests/test_skill_audit_unavailable.py:18`
- `tests/test_skill_test_stream_closed.py:57`
- `tests/test_skills_audit_characterization.py:425`

## `_run_skill_test_once` — function (async), line 218
- **called from:**
- `src/builtin_actions.py:2201`
- `tests/test_skills_routes_nondict.py:59`

## `_improve_skill_md` — function (async), line 225
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_audit_one_skill` — function (async), line 233
- **called from:**
- `tests/test_skill_audit_utility.py:262`
- `tests/test_skill_audit_utility.py:350`
- `tests/test_skill_audit_utility.py:461`
- `tests/test_skills_audit_services.py:89`
- `tests/test_skills_audit_services.py:116`

## `_run_audit_all_job` — function (async), line 241
- **called from:**
- `src/builtin_actions.py:2313`
- `tests/test_skill_audit_unavailable.py:38`
- `tests/test_skills_audit_characterization.py:447`

## `_resolve_audit_models` — function, line 249
- **called from:**
- `routes/skills_routes.py:753`
- `src/builtin_actions.py:2281`
- `tests/test_review_endpoint_credentials.py:83`
- `tests/test_teacher_audit_owner_scope.py:67`

## `run_scheduled_skill_audit` — function (async), line 253
- **called from:**
- `routes/skills_routes.py:256`
- `tests/test_skill_audit_utility.py:392`
- `tests/test_skills_audit_services.py:93`

## `_audit_dependencies` — function, line 261
- **called from:**
- `routes/skills_routes.py:172`
- `routes/skills_routes.py:188`
- `routes/skills_routes.py:203`
- `routes/skills_routes.py:221`
- `routes/skills_routes.py:237`
- `routes/skills_routes.py:245`
- `routes/skills_routes.py:257`
- `routes/skills_routes.py:656`
- `routes/skills_routes.py:714`
- `routes/skills_routes.py:724`
- `routes/skills_routes.py:762`
- `routes/skills_routes.py:768`
- `routes/skills_routes.py:773`
- `tests/test_skills_audit_services.py:235`
- `tests/test_skills_audit_services.py:262`
- `tests/test_skills_audit_services.py:287`
- `tests/test_skills_audit_services.py:306`

## `setup_skills_routes` — function, line 290
- **called from:**
- `app.py:777`
- `tests/test_endpoint_registered_authority.py:330`
- `tests/test_request_authority.py:489`
- `tests/test_request_authority.py:518`
- `tests/test_skill_rename_collision.py:77`
- `tests/test_skill_save_no_rename.py:103`
- `tests/test_skills_audit_characterization.py:134`
- `tests/test_skills_audit_characterization.py:149`
- `tests/test_skills_delete_owner.py:81`
- `tests/test_skills_routes_owner_update.py:84`
- `tests/test_skills_routes_owner_update.py:108`
- `tests/test_skills_routes_owner_update.py:151`

## `_owner` — function, line 293
- **called from:**
- `routes/assistant_routes.py:127`
- `routes/assistant_routes.py:140`
- `routes/assistant_routes.py:161`
- `routes/assistant_routes.py:279`
- `routes/assistant_routes.py:303`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:274`
- `routes/memory/memory_routes.py:299`
- `routes/memory/memory_routes.py:357`
- `routes/memory/memory_routes.py:398`
- `routes/memory/memory_routes.py:512`
- `routes/memory/memory_routes.py:526`
- `routes/memory/memory_routes.py:537`
- `routes/memory/memory_routes.py:559`
- `routes/note/note_routes.py:632`
- `routes/note/note_routes.py:656`
- `routes/note/note_routes.py:694`
- `routes/note/note_routes.py:711`
- `routes/note/note_routes.py:771`
- `routes/note/note_routes.py:790`
- `routes/note/note_routes.py:809`
- `routes/note/note_routes.py:828`
- `routes/note/note_routes.py:867`
- `routes/note/note_routes.py:913`
- `routes/skills_routes.py:317`
- `routes/skills_routes.py:326`
- `routes/skills_routes.py:337`
- `routes/skills_routes.py:463`
- `routes/skills_routes.py:491`
- `routes/skills_routes.py:529`
- `routes/skills_routes.py:565`
- `routes/skills_routes.py:576`
- `routes/skills_routes.py:605`
- `routes/skills_routes.py:666`
- `routes/skills_routes.py:720`
- `routes/skills_routes.py:736`
- `routes/skills_routes.py:767`
- `routes/skills_routes.py:772`
- `routes/skills_routes.py:779`
- `routes/skills_routes.py:830`
- `routes/skills_routes.py:853`
- `routes/skills_routes.py:870`
- `routes/task/task_routes.py:353`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:393`
- `routes/task/task_routes.py:462`
- `routes/task/task_routes.py:580`
- `routes/task/task_routes.py:589`
- `routes/task/task_routes.py:617`
- `routes/task/task_routes.py:640`
- `routes/task/task_routes.py:719`
- `routes/task/task_routes.py:733`
- `routes/task/task_routes.py:830`
- … +16 more (grep the name in repo)

## `_verify_owner` — function, line 296
- **called from:**
- `routes/skills_routes.py:581`
- `routes/skills_routes.py:616`
- `routes/skills_routes.py:674`
- `routes/skills_routes.py:788`
- `routes/skills_routes.py:835`
- `routes/skills_routes.py:858`

## `_fire_skill_added` — function, line 308
- **called from:**
- `routes/skills_routes.py:486`
- `routes/skills_routes.py:519`
- `routes/skills_routes.py:825`
- `routes/skills_routes.py:848`

## `list_skills` — function (async), line 316
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_index` — function (async), line 322
- **route:** `GET /index`
- decorator: `router.get("/index")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_slash_catalog` — function (async), line 331
- **route:** `GET /slash-catalog`
- decorator: `router.get("/slash-catalog")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_builtin_skills` — function (async), line 360
- **route:** `GET /builtin`
- decorator: `router.get("/builtin")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_clean` — function, line 368
- **called from:**
- `routes/skills_routes.py:390`

## `get_builtin_skill` — function (async), line 397
- **route:** `GET /builtin/{name}`
- decorator: `router.get("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_builtin_override` — function (async), line 421
- **route:** `PUT /builtin/{name}`
- decorator: `router.put("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reset_builtin_override` — function (async), line 447
- **route:** `DELETE /builtin/{name}`
- decorator: `router.delete("/builtin/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_skill_from_url` — function (async), line 460
- **route:** `POST /import-from-url`
- decorator: `router.post("/import-from-url")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_skill` — function (async), line 490
- **route:** `POST /add`
- decorator: `router.post("/add")`
- **called from:**
- `routes/backup_routes.py:150`
- `routes/skills_routes.py:492`
- `scripts/odysseus_domain_audit.py:348`
- `services/memory/skill_extractor.py:272`
- `src/tools/system.py:114`
- `tests/test_skill_frontmatter_escape_roundtrip.py:202`
- `tests/test_skill_rename_collision.py:20`
- `tests/test_skill_rename_collision.py:22`
- `tests/test_skill_tool_followup_contract.py:18`
- `tests/test_skill_tool_followup_contract.py:30`
- `tests/test_skill_tool_followup_contract.py:41`
- `tests/test_skill_tool_followup_contract.py:52`
- `tests/test_skill_tool_followup_contract.py:67`
- `tests/test_skill_tool_followup_contract.py:86`
- `tests/test_skill_version_preservation.py:52`
- `tests/test_skills_manager_owner_isolation.py:227`
- `tests/test_skills_manager_owner_isolation.py:236`

## `invoke_skill` — function (async), line 523
- **route:** `POST /{skill_id}/invoke`
- decorator: `router.post("/{skill_id}/invoke")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_skill` — function (async), line 564
- **route:** `GET /{skill_id}`
- decorator: `router.get("/{skill_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_skill_markdown` — function (async), line 573
- **route:** `GET /{skill_id}/markdown`
- decorator: `router.get("/{skill_id}/markdown")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_skill` — function (async), line 592
- **route:** `POST /{skill_id}/test`
- decorator: `router.post("/{skill_id}/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `approve_skill_test_action` — function (async), line 660
- **route:** `POST /{skill_id}/test-approval`
- decorator: `router.post("/{skill_id}/test-approval")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_skill_status` — function (async), line 718
- **route:** `GET /{skill_id}/test-status`
- decorator: `router.get("/{skill_id}/test-status")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `audit_all_skills` — function (async), line 727
- **route:** `POST /audit-all`
- decorator: `router.post("/audit-all")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `audit_status` — function (async), line 766
- **route:** `GET /audit-all/status`
- decorator: `router.get("/audit-all/status")`
- **called from:**
- `routes/skills_routes.py:768`

## `audit_cancel` — function (async), line 771
- **route:** `POST /audit-all/cancel`
- decorator: `router.post("/audit-all/cancel")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `save_skill_markdown` — function (async), line 776
- **route:** `POST /{skill_id}/markdown`
- decorator: `router.post("/{skill_id}/markdown")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_skill` — function (async), line 829
- **route:** `PUT /{skill_id}`
- decorator: `router.put("/{skill_id}")`
- **called from:**
- `routes/skills_routes.py:799`
- `routes/skills_routes.py:844`
- `services/skills/agent_runner.py:188`
- `services/skills/audit_workflow.py:28`
- `services/skills/audit_workflow.py:44`
- `services/skills/audit_workflow.py:303`
- `services/skills/publication.py:172`
- `services/skills/publication.py:219`
- `services/skills/publication.py:228`
- `services/skills/publication.py:322`
- `services/skills/publication.py:338`
- `src/tools/system.py:170`
- `src/tools/system.py:183`
- `src/tools/system.py:209`
- `src/tools/system.py:222`
- `tests/test_skill_frontmatter_escape_roundtrip.py:205`
- `tests/test_skill_rename_collision.py:34`
- `tests/test_skill_rename_collision.py:40`
- `tests/test_skill_rename_collision.py:49`
- `tests/test_skill_rename_collision.py:59`
- `tests/test_skill_rename_collision.py:67`
- `tests/test_skill_version_preservation.py:54`
- `tests/test_skills_manager_owner_isolation.py:90`
- `tests/test_skills_manager_owner_isolation.py:211`

## `delete_skill` — function (async), line 852
- **route:** `DELETE /{skill_id}`
- decorator: `router.delete("/{skill_id}")`
- **called from:**
- `routes/skills_routes.py:859`
- `scripts/odysseus_domain_audit.py:374`
- `src/tools/system.py:229`
- `tests/test_skill_rename_collision.py:42`
- `tests/test_skills_delete_owner.py:58`
- `tests/test_skills_delete_owner.py:62`

## `search_skills` — function (async), line 865
- **route:** `POST /search`
- decorator: `router.post("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
