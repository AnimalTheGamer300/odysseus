# `static/js/editor/panels/studio-panels.js` — definitions & call sites

13 definitions (regex-based, best-effort).
**Exports:** `ADJUSTMENT_TYPES`, `createStudioPanels`

## `adjIcon` — function, line 57
- **called from:**
- `static/js/editor/panels/studio-panels.js:57`
- `static/js/editor/panels/studio-panels.js:224`

## `el` — function, line 63
- **called from:**
- `static/app.js:289`
- `static/app.js:291`
- `static/app.js:295`
- `static/app.js:322`
- `static/app.js:323`
- `static/app.js:341`
- `static/app.js:342`
- `static/app.js:353`
- `static/app.js:358`
- `static/app.js:363`
- `static/app.js:371`
- `static/app.js:383`
- `static/app.js:411`
- `static/app.js:415`
- `static/app.js:472`
- `static/app.js:482`
- `static/app.js:486`
- `static/app.js:491`
- `static/app.js:549`
- `static/app.js:563`
- `static/app.js:599`
- `static/app.js:611`
- `static/app.js:623`
- `static/app.js:667`
- `static/app.js:668`
- `static/app.js:669`
- `static/app.js:673`
- `static/app.js:679`
- `static/app.js:788`
- `static/app.js:888`
- `static/app.js:897`
- `static/app.js:901`
- `static/app.js:909`
- `static/app.js:910`
- `static/app.js:911`
- `static/app.js:912`
- `static/app.js:925`
- `static/app.js:926`
- `static/app.js:941`
- `static/app.js:942`
- `static/app.js:943`
- `static/app.js:954`
- `static/app.js:959`
- `static/app.js:970`
- `static/app.js:972`
- `static/app.js:973`
- `static/app.js:990`
- `static/app.js:1012`
- `static/app.js:1032`
- `static/app.js:1042`
- `static/app.js:1052`
- `static/app.js:1060`
- `static/app.js:1074`
- `static/app.js:1089`
- `static/app.js:1102`
- `static/app.js:1105`
- `static/app.js:1105`
- `static/app.js:1118`
- `static/app.js:1133`
- `static/app.js:1141`
- … +1014 more (grep the name in repo)

## `panel` — function, line 70
- **called from:**
- `static/js/admin.js:102`
- `static/js/admin.js:1540`
- `static/js/calendar.js:946`
- `static/js/cookbook-hwfit.js:1521`
- `static/js/cookbook.js:1198`
- `static/js/cookbook.js:1264`
- `static/js/cookbookRunning.js:2690`
- `static/js/cookbookServe.js:3330`
- `static/js/document.js:8874`
- `static/js/document.js:15129`
- `static/js/editor/actions-panel.js:2`
- `static/js/editor/build/right-panel.js:2`
- `static/js/editor/build/right-panel.js:276`
- `static/js/editor/history-panel.js:111`
- `static/js/editor/history-panel.js:250`
- `static/js/editor/history-panel.js:250`
- `static/js/editor/panel-visibility.js:4`
- `static/js/editor/panels/panels.js:38`
- `static/js/editor/panels/panels.js:305`
- `static/js/editor/panels/panels.js:343`
- `static/js/editor/panels/panels.js:347`
- `static/js/editor/panels/panels.js:387`
- `static/js/editor/panels/panels.js:431`
- `static/js/editor/panels/panels.js:464`
- `static/js/editor/panels/studio-panels.js:70`
- `static/js/editor/panels/studio-panels.js:153`
- `static/js/editor/panels/studio-panels.js:198`
- `static/js/editor/panels/studio-panels.js:202`
- `static/js/editor/panels/studio-panels.js:219`
- `static/js/editor/panels/studio-panels.js:230`
- `static/js/editor/panels/studio-panels.js:241`
- `static/js/editor/tools/transform-session.js:275`
- `static/js/editor/tools/transform-session.js:456`
- `static/js/editor/wire-extra-menus.js:38`
- `static/js/emailLibrary/index.js:3475`
- `static/js/galleryEditor.js:10561`
- `static/js/galleryEditor.js:11215`
- `static/js/memory.js:1015`
- `static/js/settings.js:3762`
- `static/js/ui.js:63`
- `static/js/ui.js:405`

## `row` — function, line 78
- **called from:**
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:385`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:398`
- `scripts/build_odysseus_web_v53_repair_sft.py:273`
- `scripts/build_odysseus_web_v53_repair_sft.py:286`
- `scripts/build_odysseus_web_v53_repair_sft.py:310`
- `scripts/build_odysseus_web_v53_repair_sft.py:328`
- `tests/test_build_odysseus_sft_repair_manifest.py:38`
- `tests/test_build_odysseus_sft_repair_manifest.py:38`
- `tests/test_build_odysseus_sft_repair_manifest.py:38`
- `tests/test_build_odysseus_sft_repair_manifest.py:39`
- `tests/test_build_odysseus_sft_repair_manifest.py:39`
- `tests/test_build_odysseus_sft_repair_manifest.py:52`
- `tests/test_build_odysseus_sft_repair_manifest.py:65`
- `tests/test_build_odysseus_sft_repair_manifest.py:73`
- `tests/test_build_odysseus_sft_repair_manifest.py:100`
- `tests/test_build_odysseus_sft_repair_manifest.py:101`
- `tests/test_build_odysseus_sft_repair_manifest.py:109`
- `tests/test_build_odysseus_sft_repair_manifest.py:110`
- `tests/test_build_odysseus_sft_repair_manifest.py:122`
- `static/app.js:1252`
- `static/js/a11y.js:142`
- `static/js/calendar.js:2844`
- `static/js/chat.js:3267`
- `static/js/cookbook.js:1092`
- `static/js/cookbook.js:1214`
- `static/js/cookbook.js:3359`
- `static/js/cookbookServe.js:1650`
- `static/js/editor/layer-panel.js:1905`
- `static/js/editor/panels/studio-panels.js:78`
- `static/js/editor/panels/studio-panels.js:152`
- `static/js/editor/panels/studio-panels.js:152`
- `static/js/editor/panels/studio-panels.js:193`
- `static/js/editor/panels/studio-panels.js:193`
- `static/js/editor/panels/studio-panels.js:193`
- `static/js/editor/panels/studio-panels.js:194`
- `static/js/editor/panels/studio-panels.js:194`
- `static/js/editor/panels/studio-panels.js:195`
- `static/js/editor/panels/studio-panels.js:195`
- `static/js/editor/panels/studio-panels.js:196`
- `static/js/editor/panels/studio-panels.js:196`
- `static/js/editor/scroll-affordance.js:3`
- `static/js/editor/selection-mask.js:42`
- `static/js/emailLibrary/index.js:4483`
- `static/js/features/notes/ui/mobileEditor.js:134`
- `static/js/features/notes/ui/mobileEditor.js:154`
- `static/js/galleryEditor.js:11706`
- `static/js/galleryEditor.js:13955`
- `static/js/models.js:149`

## `activeLayerOf` — function, line 85
- **called from:**
- `static/js/editor/panels/studio-panels.js:85`
- `static/js/editor/panels/studio-panels.js:244`

## `patternDataUrl` — function, line 89
- **called from:**
- `static/js/editor/panels/studio-panels.js:89`
- `static/js/editor/panels/studio-panels.js:207`

## `createStudioPanels` — function, line 119
- **called from:**
- `static/js/editor/panels/studio-panels.js:119`
- `static/js/galleryEditor.js:10579`

## `emitText` — arrow, line 178
- **called from:**
- `static/js/editor/panels/studio-panels.js:179`
- `static/js/editor/panels/studio-panels.js:181`
- `static/js/editor/panels/studio-panels.js:183`
- `static/js/editor/panels/studio-panels.js:184`
- `static/js/editor/panels/studio-panels.js:185`
- `static/js/editor/panels/studio-panels.js:186`
- `static/js/editor/panels/studio-panels.js:187`
- `static/js/editor/panels/studio-panels.js:189`

## `refreshProperties` — function, line 243
- **called from:**
- `static/js/editor/panels/studio-panels.js:243`
- `static/js/editor/panels/studio-panels.js:295`

## `refreshCharacter` — function, line 253
- **called from:**
- `static/js/editor/panels/studio-panels.js:190`
- `static/js/editor/panels/studio-panels.js:253`
- `static/js/editor/panels/studio-panels.js:296`

## `renderPaths` — function, line 269
- **called from:**
- `static/js/editor/panels/studio-panels.js:269`
- `static/js/editor/panels/studio-panels.js:283`
- `static/js/editor/panels/studio-panels.js:297`

## `renderPatterns` — function, line 288
- **called from:**
- `static/js/editor/panels/studio-panels.js:214`
- `static/js/editor/panels/studio-panels.js:288`

## `refresh` — function, line 294
- **called from:**
- `routes/calendar_routes.py:1395`
- `routes/calendar_routes.py:1470`
- `routes/calendar_routes.py:1614`
- `routes/document/document_routes.py:179`
- `routes/document/document_routes.py:209`
- `routes/document/document_routes.py:322`
- `routes/document/document_routes.py:396`
- `routes/document/document_routes.py:911`
- `routes/document/document_routes.py:950`
- `routes/document/document_routes.py:1065`
- `routes/editor_draft_routes.py:181`
- `routes/editor_draft_routes.py:217`
- `routes/gallery/gallery_routes.py:1488`
- `routes/note/note_routes.py:686`
- `routes/note/note_routes.py:763`
- `routes/signature_routes.py:121`
- `routes/task/task_routes.py:570`
- `routes/task/task_routes.py:823`
- `routes/task/task_routes.py:924`
- `scripts/eval_odysseus_app_route_smoke.py:59`
- `scripts/eval_odysseus_everyday_live_hard.py:191`
- `scripts/eval_odysseus_everyday_live_hard.py:241`
- `scripts/eval_odysseus_live_hard_examples.py:249`
- `scripts/eval_odysseus_live_hard_examples.py:322`
- `scripts/run_sft_overnight_fixture_flows.py:86`
- `scripts/run_sft_overnight_fixture_flows.py:141`
- `src/agent_runtime/effect_log.py:378`
- `src/bg_jobs.py:350`
- `src/bg_jobs.py:395`
- `src/chatgpt_subscription.py:425`
- `src/chatgpt_subscription.py:435`
- `src/tools/image.py:85`
- `tests/test_background_resource_identity.py:106`
- `tests/test_background_resource_identity.py:245`
- `tests/test_runtime_resource_integration.py:251`
- `static/js/chatRenderer.js:3852`
- `static/js/chatStream.js:172`
- `static/js/cookbookDownload.js:181`
- `static/js/document.js:6424`
- `static/js/document.js:6448`
- `static/js/editor/panels/panels.js:526`
- `static/js/editor/panels/studio-panels.js:294`
- `static/js/editor/panels/studio-panels.js:300`
- `static/js/editor/preflight.js:239`
- `static/js/editor/tools/transform-session.js:384`
- `static/js/editor/tools/transform-session.js:397`
- `static/js/galleryEditor.js:10578`
- `static/js/research/panel.js:1465`
- `static/js/research/panel.js:1469`
- `static/js/research/panel.js:1528`
- `static/js/research/panel.js:1576`
- `static/js/search.js:42`
- `static/js/settings.js:583`
- `static/js/settings.js:779`
- `static/js/settings.js:933`
- `static/js/slashAutocomplete.js:253`
- `static/js/slashAutocomplete.js:266`
