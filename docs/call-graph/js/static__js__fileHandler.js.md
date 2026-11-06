# `static/js/fileHandler.js` — definitions & call sites

27 definitions (regex-based, best-effort).
**Exports:** `addFiles`, `cancelUpload`, `clearPending`, `cropForMobileUpload`, `default`, `getLastUploadedMeta`, `getPendingCount`, `getPendingInfo`, `getPendingRaw`, `init`, `isUploading`, `openPicker`, `removePending`, `renderAttachStrip`, `uploadPending`, `wasLastUploadCancelled`

## `_isMobileViewport` — function, line 27
- **called from:**
- `static/js/fileHandler.js:27`
- `static/js/fileHandler.js:271`
- `static/js/fileHandler.js:273`
- `static/js/fileHandler.js:408`
- `static/js/fileHandler.js:422`

## `_isCroppableImage` — function, line 31
- **called from:**
- `static/js/fileHandler.js:31`
- `static/js/fileHandler.js:271`
- `static/js/fileHandler.js:273`
- `static/js/fileHandler.js:408`
- `static/js/fileHandler.js:422`

## `_loadImage` — function, line 38
- **called from:**
- `static/js/fileHandler.js:38`
- `static/js/fileHandler.js:53`
- `static/js/fileHandler.js:154`

## `_canvasToBlob` — function, line 47
- **called from:**
- `static/js/fileHandler.js:47`
- `static/js/fileHandler.js:145`
- `static/js/fileHandler.js:171`

## `_openMobileCropper` — function, line 51
- **called from:**
- `static/js/fileHandler.js:51`
- `static/js/fileHandler.js:276`
- `static/js/fileHandler.js:410`
- `static/js/fileHandler.js:424`

## `applyCrop` — function, line 82
- **called from:**
- `static/js/fileHandler.js:82`
- `static/js/fileHandler.js:129`

## `clampCrop` — function, line 90
- **called from:**
- `static/js/fileHandler.js:90`
- `static/js/fileHandler.js:128`
- `static/js/fileHandler.js:160`

## `finish` — function, line 96
- **called from:**
- `src/agent_loop.py:32996`
- `src/agent_loop.py:33009`
- `src/agent_loop.py:33017`
- `src/agent_loop.py:34877`
- `src/agent_runtime/journal.py:267`
- `src/agent_runtime/journal.py:269`
- `src/containment.py:1512`
- `src/containment.py:1518`
- `src/containment.py:1527`
- `src/containment.py:1542`
- `src/containment.py:1545`
- `src/pdf_forms.py:338`
- `tests/test_effect_verification_adapters.py:55`
- `tests/test_effect_verification_adapters.py:121`
- `tests/test_effect_verification_adapters.py:215`
- `tests/test_effect_verification_adapters.py:431`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:2122`
- `static/js/colorPicker.js:237`
- `static/js/colorPicker.js:243`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:211`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/ai-inpaint.js:280`
- `static/js/editor/ai-operation.js:19`
- `static/js/editor/ai-tool-runner.js:164`
- `static/js/editor/ai-tools-misc.js:157`
- `static/js/editor/ai-tools-misc.js:206`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:372`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-panel.js:1424`
- `static/js/editor/layer-panel.js:1426`
- `static/js/editor/layer-panel.js:1431`
- `static/js/editor/precision-guides.js:210`
- `static/js/editor/precision-guides.js:229`
- `static/js/editor/tools/pen-path.js:39`
- `static/js/editor/tools/pen-path.js:46`
- `static/js/features/notes/ui/cardInteractions.js:234`
- `static/js/features/notes/ui/cardInteractions.js:238`
- `static/js/features/notes/ui/colors.js:63`
- `static/js/features/notes/ui/colors.js:71`
- `static/js/features/notes/ui/colors.js:72`
- `static/js/features/notes/ui/colors.js:75`
- `static/js/fileHandler.js:96`
- `static/js/fileHandler.js:134`
- `static/js/fileHandler.js:135`
- `static/js/fileHandler.js:172`
- `static/js/fileHandler.js:175`
- `static/js/gallery.js:2484`
- `static/js/gallery.js:2487`
- `static/js/galleryEditor.js:430`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4573`
- `static/js/galleryEditor.js:4575`
- `static/js/galleryEditor.js:4655`
- `static/js/galleryEditor.js:4659`
- … +4 more (grep the name in repo)

## `_getPreviewUrl` — function, line 180
- **called from:**
- `static/js/fileHandler.js:52`
- `static/js/fileHandler.js:180`
- `static/js/fileHandler.js:269`
- `static/js/fileHandler.js:470`

## `_revokePreviewUrl` — function, line 190
- **called from:**
- `static/js/fileHandler.js:190`
- `static/js/fileHandler.js:278`
- `static/js/fileHandler.js:304`

## `init` — function, line 201
- **called from:**
- `static/app.js:3824`
- `static/app.js:3825`
- `static/app.js:3826`
- `static/app.js:3827`
- `static/app.js:3828`
- `static/app.js:3829`
- `static/app.js:3833`
- `static/app.js:3836`
- `static/app.js:3838`
- `static/app.js:3841`
- `static/app.js:3850`
- `static/app.js:4486`
- `static/app.js:4487`
- `static/js/a11y.js:174`
- `static/js/a11y.js:223`
- `static/js/censor.js:44`
- `static/js/chat.js:2061`
- `static/js/chat.js:2066`
- `static/js/compare/index.js:57`
- `static/js/cookbookDownload.js:10`
- `static/js/cookbookRunning.js:337`
- `static/js/cookbookServe.js:21`
- `static/js/document.js:1065`
- `static/js/emailInbox.js:159`
- `static/js/fileHandler.js:201`
- `static/js/group.js:24`
- `static/js/models.js:27`
- `static/js/presets.js:79`
- `static/js/rag.js:12`
- `static/js/research/jobs.js:66`
- `static/js/research/panel.js:206`
- `static/js/research/panel.js:210`
- `static/js/search-chat.js:204`
- `static/js/search.js:14`
- `static/js/tourAutoplay.js:117`
- `static/js/tourAutoplay.js:129`
- `static/js/tourHints.js:158`
- `static/js/tourHints.js:170`
- `static/js/voiceRecorder.js:268`

## `openPicker` — function, line 208
- **called from:**
- `static/js/fileHandler.js:208`

## `renderAttachStrip` — function, line 217
- **called from:**
- `static/app.js:315`
- `static/js/fileHandler.js:217`
- `static/js/fileHandler.js:243`
- `static/js/fileHandler.js:280`
- `static/js/fileHandler.js:306`
- `static/js/fileHandler.js:394`
- `static/js/fileHandler.js:418`
- `static/js/fileHandler.js:482`

## `_createChip` — function, line 261
- **called from:**
- `static/js/fileHandler.js:255`
- `static/js/fileHandler.js:261`

## `removePending` — function, line 302
- **called from:**
- `static/js/fileHandler.js:294`
- `static/js/fileHandler.js:302`

## `uploadPending` — function, line 312
- **called from:**
- `static/js/chat.js:3108`
- `static/js/chat.js:3129`
- `static/js/chatRenderer.js:624`
- `static/js/fileHandler.js:13`
- `static/js/fileHandler.js:14`
- `static/js/fileHandler.js:312`
- `static/js/fileHandler.js:485`

## `addFiles` — function, line 401
- **called from:**
- `static/app.js:292`
- `static/app.js:310`
- `static/app.js:4187`
- `static/app.js:4318`
- `static/app.js:4341`
- `static/app.js:4415`
- `static/js/chatRenderer.js:2110`
- `static/js/fileHandler.js:401`
- `static/js/gallery.js:1755`
- `static/js/gallery.js:1798`

## `cropForMobileUpload` — function, line 421
- **called from:**
- `static/js/fileHandler.js:421`
- `static/js/gallery.js:1375`

## `_showToast` — function, line 430
- **called from:**
- `static/js/fileHandler.js:282`
- `static/js/fileHandler.js:362`
- `static/js/fileHandler.js:380`
- `static/js/fileHandler.js:383`
- `static/js/fileHandler.js:404`
- `static/js/fileHandler.js:430`

## `getPendingCount` — function, line 449
- **called from:**
- `static/app.js:4028`
- `static/js/chat.js:2464`
- `static/js/chat.js:2717`
- `static/js/chat.js:3038`
- `static/js/fileHandler.js:449`

## `getPendingRaw` — function, line 456
- **called from:**
- `static/js/chat.js:3045`
- `static/js/fileHandler.js:456`

## `getPendingInfo` — function, line 463
- **called from:**
- `static/js/chat.js:3039`
- `static/js/fileHandler.js:463`

## `clearPending` — function, line 478
- **called from:**
- `static/js/fileHandler.js:249`
- `static/js/fileHandler.js:478`

## `getLastUploadedMeta` — function, line 486
- **called from:**
- `static/js/fileHandler.js:373`
- `static/js/fileHandler.js:486`

## `isUploading` — function, line 490
- **called from:**
- `static/js/chat.js:2523`
- `static/js/fileHandler.js:490`

## `wasLastUploadCancelled` — function, line 494
- **called from:**
- `static/js/chat.js:3117`
- `static/js/fileHandler.js:494`

## `cancelUpload` — function, line 498
- **called from:**
- `static/js/chat.js:2524`
- `static/js/fileHandler.js:303`
- `static/js/fileHandler.js:479`
- `static/js/fileHandler.js:498`
