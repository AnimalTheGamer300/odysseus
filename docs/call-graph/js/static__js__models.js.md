# `static/js/models.js` — definitions & call sites

16 definitions (regex-based, best-effort).
**Exports:** `default`, `getCachedItems`, `init`, `refreshModels`, `refreshProviders`

## `init` — function, line 27
- **called from:**
- `static/app.js:3723`
- `static/app.js:3724`
- `static/app.js:3725`
- `static/app.js:3726`
- `static/app.js:3727`
- `static/app.js:3728`
- `static/app.js:3730`
- `static/app.js:3733`
- `static/app.js:3735`
- `static/app.js:3738`
- `static/app.js:3747`
- `static/app.js:4369`
- `static/app.js:4370`
- `static/js/a11y.js:121`
- `static/js/a11y.js:163`
- `static/js/censor.js:44`
- `static/js/chat.js:1165`
- `static/js/chat.js:1170`
- `static/js/compare/index.js:55`
- `static/js/cookbookDownload.js:10`
- `static/js/cookbookRunning.js:333`
- `static/js/cookbookServe.js:16`
- `static/js/document.js:154`
- `static/js/emailInbox.js:157`
- `static/js/fileHandler.js:173`
- `static/js/group.js:24`
- `static/js/models.js:27`
- `static/js/presets.js:79`
- `static/js/rag.js:12`
- `static/js/research/jobs.js:35`
- `static/js/research/panel.js:210`
- `static/js/research/panel.js:214`
- `static/js/search-chat.js:198`
- `static/js/search.js:14`
- `static/js/tourAutoplay.js:117`
- `static/js/tourAutoplay.js:129`
- `static/js/tourHints.js:163`
- `static/js/tourHints.js:175`
- `static/js/voiceRecorder.js:268`

## `_loadCollapsed` — function, line 32
- **called from:**
- `static/js/models.js:32`
- `static/js/models.js:228`
- `static/js/models.js:311`
- `static/js/models.js:370`
- `static/js/models.js:417`

## `_saveCollapsed` — function, line 35
- **called from:**
- `static/js/models.js:35`
- `static/js/models.js:313`
- `static/js/models.js:372`
- `static/js/models.js:419`

## `_loadFavorites` — function, line 40
- **called from:**
- `static/js/modelPicker.js:39`
- `static/js/modelPicker.js:41`
- `static/js/modelPicker.js:457`
- `static/js/models.js:40`
- `static/js/models.js:47`
- `static/js/models.js:50`
- `static/js/models.js:268`

## `_saveFavorites` — function, line 43
- **called from:**
- `static/js/models.js:43`
- `static/js/models.js:54`

## `_isFavorite` — function, line 46
- **called from:**
- `static/js/models.js:46`
- `static/js/models.js:107`
- `static/js/models.js:111`

## `_toggleFavorite` — function, line 49
- **called from:**
- `static/js/modelPicker.js:40`
- `static/js/modelPicker.js:519`
- `static/js/models.js:49`
- `static/js/models.js:116`

## `_loadUsage` — function, line 59
- **called from:**
- `static/js/models.js:59`
- `static/js/models.js:63`
- `static/js/models.js:286`
- `static/js/models.js:289`
- `static/js/models.js:444`
- `static/js/models.js:447`

## `_trackUsage` — function, line 62
- **called from:**
- `static/js/models.js:62`
- `static/js/models.js:82`

## `_getSortMode` — function, line 69
- **called from:**
- `static/js/models.js:69`
- `static/js/models.js:282`
- `static/js/models.js:440`

## `_setSortMode` — function, line 72
- **called from:**
- `static/js/models.js:72`

## `_startChat` — function, line 79
- **called from:**
- `static/js/models.js:79`
- `static/js/models.js:145`
- `static/js/models.js:157`

## `_buildModelRow` — function, line 90
- **called from:**
- `static/js/models.js:90`
- `static/js/models.js:323`
- `static/js/models.js:458`
- `static/js/models.js:470`
- `static/js/models.js:564`

## `refreshModels` — function, line 167
- **called from:**
- `static/app.js:1495`
- `static/app.js:4360`
- `static/js/admin.js:434`
- `static/js/admin.js:454`
- `static/js/admin.js:477`
- `static/js/cookbookRunning.js:552`
- `static/js/cookbookRunning.js:3649`
- `static/js/cookbookRunning.js:3680`
- `static/js/cookbookRunning.js:4097`
- `static/js/cookbookRunning.js:4334`
- `static/js/markdown.js:1463`
- `static/js/markdown.js:1492`
- `static/js/modelPicker.js:49`
- `static/js/modelPicker.js:123`
- `static/js/modelPicker.js:362`
- `static/js/modelPicker.js:740`
- `static/js/models.js:119`
- `static/js/models.js:167`
- `static/js/models.js:314`
- `static/js/models.js:373`
- `static/js/models.js:420`
- `static/js/settings.js:397`
- `static/js/settings.js:400`
- `static/js/settings.js:407`
- `static/js/settings.js:410`
- `static/js/settings.js:445`
- `static/js/settings.js:455`
- `static/js/settings.js:481`
- `static/js/settings.js:487`
- `static/js/settings.js:543`
- `static/js/settings.js:586`
- `static/js/settings.js:611`
- `static/js/settings.js:617`
- `static/js/settings.js:1410`
- `static/js/settings.js:1420`
- `static/js/settings.js:1487`
- `static/js/settings.js:1499`
- `static/js/slashCommands.js:705`
- `static/js/slashCommands.js:720`
- `static/js/slashCommands.js:5071`

## `refreshProviders` — function, line 600
- **called from:**
- `static/app.js:4364`
- `static/js/models.js:600`

## `getCachedItems` — function, line 632
- **called from:**
- `static/js/cookbookRunning.js:558`
- `static/js/group.js:42`
- `static/js/group.js:454`
- `static/js/modelPicker.js:91`
- `static/js/modelPicker.js:104`
- `static/js/modelPicker.js:120`
- `static/js/modelPicker.js:276`
- `static/js/modelPicker.js:332`
- `static/js/modelPicker.js:742`
- `static/js/modelPicker.js:923`
- `static/js/models.js:632`
- `static/js/tasks.js:2525`
