# `static/js/editor/panels/panels.js` — definitions & call sites

28 definitions (regex-based, best-effort).
**Exports:** `createColorPanels`

## `el` — function, line 31
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

## `panel` — function, line 38
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

## `activeLayer` — function, line 46
- **called from:**
- `static/js/editor/layer-geometry.js:133`
- `static/js/editor/layer-geometry.js:153`
- `static/js/editor/layer-geometry.js:186`
- `static/js/editor/layer-geometry.js:224`
- `static/js/editor/panels/panels.js:46`
- `static/js/editor/panels/panels.js:435`
- `static/js/editor/stroke-pipeline.js:293`
- `static/js/editor/tools/bucket.js:134`
- `static/js/editor/tools/clone.js:26`
- `static/js/editor/tools/eyedropper.js:37`
- `static/js/editor/tools/gradient.js:33`
- `static/js/editor/tools/gradient.js:59`
- `static/js/editor/tools/gradient.js:84`
- `static/js/editor/tools/gradient.js:108`
- `static/js/editor/tools/liquify.js:142`
- `static/js/editor/tools/liquify.js:157`
- `static/js/editor/tools/marquee.js:52`
- `static/js/editor/tools/marquee.js:177`
- `static/js/editor/tools/move.js:48`
- `static/js/editor/tools/move.js:87`
- `static/js/editor/tools/object-select.js:43`
- `static/js/editor/tools/patch.js:22`
- `static/js/editor/tools/pen-selection.js:7`
- `static/js/editor/tools/pen-selection.js:52`
- `static/js/editor/tools/pen-selection.js:59`
- `static/js/editor/tools/quick-select.js:33`
- `static/js/editor/tools/transform-session.js:114`
- `static/js/editor/tools/wand.js:27`
- `static/js/editor/wire-topbar.js:160`
- `static/js/galleryEditor.js:2123`
- `static/js/galleryEditor.js:3371`
- `static/js/galleryEditor.js:5443`
- `static/js/galleryEditor.js:5454`
- `static/js/galleryEditor.js:5475`
- `static/js/galleryEditor.js:5544`
- `static/js/galleryEditor.js:5724`
- `static/js/galleryEditor.js:5727`
- `static/js/galleryEditor.js:6009`
- `static/js/galleryEditor.js:6014`
- `static/js/galleryEditor.js:6931`
- `static/js/galleryEditor.js:7124`
- `static/js/galleryEditor.js:7332`
- `static/js/galleryEditor.js:7377`
- `static/js/galleryEditor.js:7456`
- `static/js/galleryEditor.js:7502`
- `static/js/galleryEditor.js:7536`
- `static/js/galleryEditor.js:7837`
- `static/js/galleryEditor.js:8107`
- `static/js/galleryEditor.js:8121`
- `static/js/galleryEditor.js:8135`
- `static/js/galleryEditor.js:8493`
- `static/js/galleryEditor.js:8545`
- `static/js/galleryEditor.js:10603`
- `static/js/galleryEditor.js:11828`
- `static/js/galleryEditor.js:12190`
- `static/js/galleryEditor.js:12311`
- `static/js/galleryEditor.js:12475`
- `static/js/galleryEditor.js:12489`
- `static/js/galleryEditor.js:12496`
- `static/js/galleryEditor.js:12600`
- … +48 more (grep the name in repo)

## `hexToHsv` — function, line 55
- **called from:**
- `static/js/colorPicker.js:71`
- `static/js/colorPicker.js:111`
- `static/js/colorPicker.js:197`
- `static/js/editor/panels/panels.js:55`
- `static/js/editor/panels/panels.js:250`

## `hsvToHex` — function, line 76
- **called from:**
- `static/js/colorPicker.js:69`
- `static/js/colorPicker.js:96`
- `static/js/colorPicker.js:97`
- `static/js/colorPicker.js:98`
- `static/js/colorPicker.js:99`
- `static/js/colorPicker.js:100`
- `static/js/colorPicker.js:161`
- `static/js/colorPicker.js:169`
- `static/js/colorPicker.js:190`
- `static/js/colorPicker.js:299`
- `static/js/editor/panels/panels.js:76`
- `static/js/editor/panels/panels.js:244`
- `static/js/editor/panels/panels.js:255`

## `to` — arrow, line 90
- **called from:**
- `routes/gallery/gallery_routes.py:426`
- `routes/gallery/gallery_routes.py:462`
- `routes/gallery/gallery_routes.py:480`
- `routes/gallery/gallery_routes.py:481`
- `scripts/diffusion_server.py:332`
- `scripts/diffusion_server.py:462`
- `scripts/diffusion_server.py:628`
- `scripts/diffusion_server.py:951`
- `scripts/diffusion_server.py:964`
- `services/tts/tts_service.py:306`
- `static/js/actionMenuOrder.js:10`
- `static/js/calendar.js:1242`
- `static/js/calendar.js:2883`
- `static/js/chat.js:9375`
- `static/js/editor/panels/panels.js:91`
- `static/js/editor/panels/panels.js:91`
- `static/js/editor/panels/panels.js:91`
- `static/js/sessions.js:2200`

## `createColorPanels` — function, line 94
- **called from:**
- `static/js/editor/panels/panels.js:94`
- `static/js/galleryEditor.js:10563`

## `getFavoriteColors` — arrow, line 130
- **called from:**
- `static/js/editor/panels/panels.js:139`
- `static/js/editor/panels/panels.js:159`
- `static/js/editor/panels/panels.js:219`

## `setFavoriteColors` — arrow, line 136
- **called from:**
- `static/js/editor/panels/panels.js:222`

## `isFavorite` — arrow, line 139
- **called from:**
- `static/js/editor/panels/panels.js:163`

## `_syncForeground` — arrow, line 141
- **called from:**
- `static/js/editor/panels/panels.js:235`
- `static/js/editor/panels/panels.js:256`
- `static/js/editor/panels/panels.js:293`
- `static/js/editor/panels/panels.js:300`

## `renderInlineSwatches` — arrow, line 148
- **called from:**
- `static/js/editor/panels/panels.js:223`
- `static/js/editor/panels/panels.js:238`
- `static/js/editor/panels/panels.js:259`
- `static/js/editor/panels/panels.js:297`
- `static/js/editor/panels/panels.js:303`
- `static/js/editor/panels/panels.js:306`
- `static/js/editor/panels/panels.js:312`

## `_setHex` — arrow, line 227
- **called from:**
- `static/js/editor/panels/panels.js:258`
- `static/js/editor/panels/panels.js:295`
- `static/js/editor/panels/panels.js:301`
- `static/js/editor/panels/panels.js:310`

## `paintPicker` — arrow, line 243
- **called from:**
- `static/js/editor/panels/panels.js:252`
- `static/js/editor/panels/panels.js:266`
- `static/js/editor/panels/panels.js:271`

## `setPickerFromColor` — arrow, line 249
- **called from:**
- `static/js/editor/panels/panels.js:237`
- `static/js/editor/panels/panels.js:286`
- `static/js/editor/panels/panels.js:296`
- `static/js/editor/panels/panels.js:302`
- `static/js/editor/panels/panels.js:311`

## `commitPicker` — arrow, line 254
- **called from:**
- `static/js/editor/panels/panels.js:267`
- `static/js/editor/panels/panels.js:272`

## `pickFromEvent` — arrow, line 261
- **called from:**
- `static/js/editor/panels/panels.js:279`
- `static/js/editor/panels/panels.js:283`

## `startDrag` — arrow, line 275
- **called from:**
- `static/js/dragSort.js:65`
- `static/js/dragSort.js:189`
- `static/js/dragSort.js:200`
- `static/js/dragSort.js:239`
- `static/js/dragSort.js:298`
- `static/js/editor/panels/panels.js:281`
- `static/js/editor/panels/panels.js:282`
- `static/js/emailLibrary/reader.js:251`

## `refreshSwatches` — arrow, line 307
- **called from:**
- `static/js/editor/panels/panels.js:520`

## `renderChannels` — arrow, line 348
- **called from:**
- `static/js/editor/panels/panels.js:366`
- `static/js/editor/panels/panels.js:375`
- `static/js/editor/panels/panels.js:521`

## `histogramLayer` — arrow, line 392
- **called from:**
- `static/js/editor/panels/panels.js:403`

## `redrawHistogram` — arrow, line 402
- **called from:**
- `static/js/editor/panels/panels.js:522`

## `refreshInfo` — arrow, line 432
- **called from:**
- `static/js/editor/panels/panels.js:523`

## `sampleAt` — arrow, line 438
- **called from:**
- `static/js/editor/panels/panels.js:455`

## `navScale` — arrow, line 465
- **called from:**
- `static/js/editor/panels/panels.js:479`
- `static/js/editor/panels/panels.js:502`

## `drawNavigator` — arrow, line 470
- **called from:**
- `static/js/editor/panels/panels.js:511`
- `static/js/editor/panels/panels.js:524`

## `panFromNavigator` — arrow, line 497
- **called from:**
- `static/js/editor/panels/panels.js:514`
- `static/js/editor/panels/panels.js:515`

## `refresh` — arrow, line 519
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
