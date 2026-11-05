# `services/skills/audit_workflow.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `audit_one_skill` — function (async), line 16
- **called from:**
- `routes/skills_routes.py:235`

## `_set_conf` — function, line 26
- **called from:**
- `services/skills/audit_workflow.py:210`
- `services/skills/audit_workflow.py:250`
- `services/skills/audit_workflow.py:286`

## `run_audit_batch` — function (async), line 317
- **called from:**
- `routes/skills_routes.py:243`
- `tests/test_skills_audit_services.py:265`

## `log` — function, line 327
- **called from:**
- `scripts/diffusion_server.py:1221`
- `services/skills/audit_workflow.py:34`
- `services/skills/audit_workflow.py:49`
- `services/skills/audit_workflow.py:75`
- `services/skills/audit_workflow.py:77`
- `services/skills/audit_workflow.py:89`
- `services/skills/audit_workflow.py:103`
- `services/skills/audit_workflow.py:106`
- `services/skills/audit_workflow.py:141`
- `services/skills/audit_workflow.py:175`
- `services/skills/audit_workflow.py:190`
- `services/skills/audit_workflow.py:203`
- `services/skills/audit_workflow.py:221`
- `services/skills/audit_workflow.py:233`
- `services/skills/audit_workflow.py:237`
- `services/skills/audit_workflow.py:248`
- `services/skills/audit_workflow.py:261`
- `services/skills/audit_workflow.py:272`
- `services/skills/audit_workflow.py:284`
- `services/skills/audit_workflow.py:298`
- `services/skills/audit_workflow.py:313`
- `services/skills/audit_workflow.py:337`
- `services/skills/audit_workflow.py:352`
- `services/skills/audit_workflow.py:356`
- `services/skills/audit_workflow.py:359`
- `services/skills/publication.py:173`
- `services/skills/publication.py:220`
- `services/skills/publication.py:229`
- `src/chat_processor.py:221`
- `src/image_model_ids.py:37`
- `src/image_model_ids.py:48`
- `static/app.js:3987`
- `static/app.js:3990`
- `static/app.js:3991`
- `static/app.js:4709`
- `static/js/cookbookRunning.js:4103`
- `static/js/cookbookSchedule.js:65`
- `static/js/editor/build/controls.js:13`
- `static/js/editor/build/controls.js:13`
- `static/js/editor/canvas-context-menu.js:38`
- `static/js/editor/canvas-context-menu.js:38`
- `static/js/editor/fx/adj-popup.js:1144`
- `static/js/editor/fx/adj-popup.js:1144`
- `static/js/editor/fx/pixel-pass.js:351`
- `static/js/editor/fx/pixel-pass.js:351`
- `static/js/editor/retouch.js:125`
- `static/js/editor/retouch.js:125`
- `static/js/emailLibrary/index.js:5348`
- `static/js/galleryEditor.js:10141`
- `static/js/galleryEditor.js:10141`
- `static/js/galleryEditor.js:11086`
- `static/js/galleryEditor.js:11086`

## `run_scheduled_skill_audit` — function (async), line 398
- **called from:**
- `routes/skills_routes.py:256`
- `tests/test_skill_audit_utility.py:392`
- `tests/test_skills_audit_services.py:93`
