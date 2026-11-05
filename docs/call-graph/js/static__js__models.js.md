# `static/js/models.js` — definitions & call sites

16 definitions (regex-based, best-effort).
**Exports:** `default`, `getCachedItems`, `init`, `refreshModels`, `refreshProviders`

## `init` — function, line 27
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

## `_loadCollapsed` — function, line 32
- **called from:**
- `static/js/models.js:32`
- `static/js/models.js:230`
- `static/js/models.js:313`
- `static/js/models.js:372`
- `static/js/models.js:419`

## `_saveCollapsed` — function, line 35
- **called from:**
- `static/js/models.js:35`
- `static/js/models.js:315`
- `static/js/models.js:374`
- `static/js/models.js:421`

## `_loadFavorites` — function, line 40
- **called from:**
- `static/js/modelPicker.js:39`
- `static/js/modelPicker.js:41`
- `static/js/modelPicker.js:467`
- `static/js/models.js:40`
- `static/js/models.js:47`
- `static/js/models.js:50`
- `static/js/models.js:270`

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
- `static/js/modelPicker.js:530`
- `static/js/models.js:49`
- `static/js/models.js:116`

## `_loadUsage` — function, line 59
- **called from:**
- `static/js/models.js:59`
- `static/js/models.js:63`
- `static/js/models.js:288`
- `static/js/models.js:291`
- `static/js/models.js:446`
- `static/js/models.js:449`

## `_trackUsage` — function, line 62
- **called from:**
- `static/js/models.js:62`
- `static/js/models.js:82`

## `_getSortMode` — function, line 69
- **called from:**
- `static/js/models.js:69`
- `static/js/models.js:284`
- `static/js/models.js:442`

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
- `static/js/models.js:325`
- `static/js/models.js:460`
- `static/js/models.js:472`
- `static/js/models.js:566`

## `refreshModels` — function, line 167
- **called from:**
- `static/app.js:1536`
- `static/app.js:4477`
- `static/js/admin.js:491`
- `static/js/admin.js:511`
- `static/js/admin.js:1012`
- `static/js/cookbookRunning.js:556`
- `static/js/cookbookRunning.js:3705`
- `static/js/cookbookRunning.js:3736`
- `static/js/cookbookRunning.js:4174`
- `static/js/cookbookRunning.js:4411`
- `static/js/markdown.js:1870`
- `static/js/markdown.js:1899`
- `static/js/modelPicker.js:49`
- `static/js/modelPicker.js:123`
- `static/js/modelPicker.js:361`
- `static/js/modelPicker.js:761`
- `static/js/models.js:119`
- `static/js/models.js:167`
- `static/js/models.js:316`
- `static/js/models.js:375`
- `static/js/models.js:422`
- `static/js/settings.js:387`
- `static/js/settings.js:390`
- `static/js/settings.js:400`
- `static/js/settings.js:403`
- `static/js/settings.js:516`
- `static/js/settings.js:528`
- `static/js/settings.js:569`
- `static/js/settings.js:580`
- `static/js/settings.js:607`
- `static/js/settings.js:650`
- `static/js/settings.js:675`
- `static/js/settings.js:681`
- `static/js/settings.js:1165`
- `static/js/settings.js:1175`
- `static/js/settings.js:1242`
- `static/js/settings.js:1254`
- `static/js/slashCommands.js:705`
- `static/js/slashCommands.js:720`
- `static/js/slashCommands.js:5082`

## `refreshProviders` — function, line 608
- **called from:**
- `static/app.js:4481`
- `static/js/models.js:608`

## `getCachedItems` — function, line 640
- **called from:**
- `static/js/cookbookRunning.js:562`
- `static/js/group.js:42`
- `static/js/group.js:454`
- `static/js/modelPicker.js:91`
- `static/js/modelPicker.js:104`
- `static/js/modelPicker.js:120`
- `static/js/modelPicker.js:276`
- `static/js/modelPicker.js:331`
- `static/js/modelPicker.js:763`
- `static/js/modelPicker.js:942`
- `static/js/models.js:640`
- `static/js/tasks.js:2661`
