# `static/js/research/jobs.js` — definitions & call sites

35 definitions (regex-based, best-effort).
**Exports:** `addToQueue`, `adoptSession`, `cancelJob`, `clearAll`, `formatElapsed`, `formatPhase`, `getJobs`, `init`, `onComplete`, `refreshLibrary`, `removeJob`, `retryJob`, `setRenderCallback`, `startAllQueued`, `startAllQueuedSequential`, `startJob`, `startQueued`

## `_loadDismissed` — function, line 14
- **called from:**
- `static/js/research/jobs.js:14`
- `static/js/research/jobs.js:23`
- `static/js/research/jobs.js:25`
- `static/js/research/jobs.js:147`

## `_saveDismissed` — function, line 20
- **called from:**
- `static/js/research/jobs.js:20`
- `static/js/research/jobs.js:27`

## `_isDismissed` — function, line 23
- **called from:**
- `static/js/research/jobs.js:23`

## `_markDismissed` — function, line 24
- **called from:**
- `static/js/research/jobs.js:24`
- `static/js/research/jobs.js:272`
- `static/js/research/jobs.js:282`

## `_loadSavedErrors` — function, line 30
- **called from:**
- `static/js/research/jobs.js:30`
- `static/js/research/jobs.js:41`
- `static/js/research/jobs.js:57`
- `static/js/research/jobs.js:70`

## `_saveErrors` — function, line 37
- **called from:**
- `static/js/research/jobs.js:37`
- `static/js/research/jobs.js:54`
- `static/js/research/jobs.js:57`
- `static/js/research/jobs.js:283`

## `_rememberError` — function, line 40
- **called from:**
- `static/js/research/jobs.js:40`
- `static/js/research/jobs.js:340`
- `static/js/research/jobs.js:348`
- `static/js/research/jobs.js:423`

## `_forgetError` — function, line 56
- **called from:**
- `static/js/research/jobs.js:56`
- `static/js/research/jobs.js:246`
- `static/js/research/jobs.js:273`

## `init` — function, line 66
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

## `adoptSession` — function, line 91
- **called from:**
- `static/js/research/jobs.js:91`

## `refreshLibrary` — function, line 96
- **called from:**
- `static/js/research/jobs.js:96`

## `_reconnectActive` — function, line 100
- **called from:**
- `static/js/research/jobs.js:77`
- `static/js/research/jobs.js:85`
- `static/js/research/jobs.js:93`
- `static/js/research/jobs.js:100`

## `_syncLibrary` — function, line 138
- **called from:**
- `static/js/research/jobs.js:97`
- `static/js/research/jobs.js:130`
- `static/js/research/jobs.js:138`

## `_parseDuration` — function, line 196
- **called from:**
- `static/js/research/jobs.js:151`
- `static/js/research/jobs.js:196`

## `setRenderCallback` — function, line 201
- **called from:**
- `static/js/research/jobs.js:201`
- `static/js/research/panel.js:211`

## `getJobs` — function, line 202
- **called from:**
- `static/js/research/jobs.js:202`
- `static/js/research/panel.js:98`
- `static/js/research/panel.js:693`
- `static/js/research/panel.js:697`
- `static/js/research/panel.js:957`
- `static/js/research/panel.js:984`
- `static/js/research/panel.js:997`

## `addToQueue` — function, line 204
- **called from:**
- `static/js/research/jobs.js:204`
- `static/js/research/jobs.js:212`
- `static/js/research/panel.js:648`

## `startJob` — function, line 211
- **called from:**
- `static/js/research/jobs.js:211`
- `static/js/research/panel.js:746`

## `startQueued` — function, line 217
- **called from:**
- `static/js/research/jobs.js:217`
- `static/js/research/panel.js:1158`

## `startAllQueued` — function, line 223
- **called from:**
- `static/js/research/jobs.js:223`
- `static/js/research/panel.js:734`
- `static/js/research/panel.js:1121`

## `startAllQueuedSequential` — function, line 230
- **called from:**
- `static/js/research/jobs.js:230`
- `static/js/research/panel.js:1122`

## `retryJob` — function, line 243
- **called from:**
- `static/js/research/jobs.js:243`
- `static/js/research/panel.js:1347`

## `cancelJob` — function, line 259
- **called from:**
- `static/js/galleryEditor.js:3090`
- `static/js/research/jobs.js:259`
- `static/js/research/panel.js:1201`

## `removeJob` — function, line 267
- **called from:**
- `static/js/research/jobs.js:267`
- `static/js/research/panel.js:681`
- `static/js/research/panel.js:757`
- `static/js/research/panel.js:963`
- `static/js/research/panel.js:1164`
- `static/js/research/panel.js:1325`
- `static/js/research/panel.js:1330`
- `static/js/research/panel.js:1354`

## `clearAll` — function, line 279
- **called from:**
- `static/js/document.js:17531`
- `static/js/research/jobs.js:279`

## `formatElapsed` — function, line 292
- **called from:**
- `static/js/research/jobs.js:292`
- `static/js/research/panel.js:1135`

## `formatPhase` — function, line 298
- **called from:**
- `static/js/research/jobs.js:298`
- `static/js/research/panel.js:1172`

## `_makeJob` — function, line 313
- **called from:**
- `static/js/research/jobs.js:205`
- `static/js/research/jobs.js:313`

## `_launchJob` — function, line 327
- **called from:**
- `static/js/research/jobs.js:213`
- `static/js/research/jobs.js:220`
- `static/js/research/jobs.js:225`
- `static/js/research/jobs.js:233`
- `static/js/research/jobs.js:256`
- `static/js/research/jobs.js:327`

## `_connectStream` — function, line 361
- **called from:**
- `static/js/research/jobs.js:126`
- `static/js/research/jobs.js:357`
- `static/js/research/jobs.js:361`

## `_pollFallback` — function, line 398
- **called from:**
- `static/js/research/jobs.js:394`
- `static/js/research/jobs.js:398`
- `static/js/research/jobs.js:417`

## `_finishJob` — function, line 421
- **called from:**
- `static/js/research/jobs.js:264`
- `static/js/research/jobs.js:373`
- `static/js/research/jobs.js:384`
- `static/js/research/jobs.js:402`
- `static/js/research/jobs.js:413`
- `static/js/research/jobs.js:418`
- `static/js/research/jobs.js:421`

## `onComplete` — function, line 437
- **called from:**
- `static/js/research/jobs.js:437`
- `static/js/research/panel.js:212`

## `_fetchResult` — function, line 439
- **called from:**
- `static/js/research/jobs.js:385`
- `static/js/research/jobs.js:414`
- `static/js/research/jobs.js:439`

## `_notify` — function, line 460
- **called from:**
- `static/js/research/jobs.js:131`
- `static/js/research/jobs.js:171`
- `static/js/research/jobs.js:189`
- `static/js/research/jobs.js:207`
- `static/js/research/jobs.js:255`
- `static/js/research/jobs.js:262`
- `static/js/research/jobs.js:276`
- `static/js/research/jobs.js:289`
- `static/js/research/jobs.js:341`
- `static/js/research/jobs.js:349`
- `static/js/research/jobs.js:358`
- `static/js/research/jobs.js:364`
- `static/js/research/jobs.js:388`
- `static/js/research/jobs.js:433`
- `static/js/research/jobs.js:456`
- `static/js/research/jobs.js:460`
