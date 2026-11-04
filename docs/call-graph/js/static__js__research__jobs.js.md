# `static/js/research/jobs.js` — definitions & call sites

31 definitions (regex-based, best-effort).
**Exports:** `addToQueue`, `adoptSession`, `cancelJob`, `clearAll`, `formatElapsed`, `formatPhase`, `getJobs`, `init`, `onComplete`, `refreshLibrary`, `removeJob`, `retryJob`, `setRenderCallback`, `startAllQueued`, `startAllQueuedSequential`, `startJob`, `startQueued`

## `_loadDismissed` — function, line 13
- **called from:**
- `static/js/research/jobs.js:13`
- `static/js/research/jobs.js:22`
- `static/js/research/jobs.js:24`
- `static/js/research/jobs.js:98`

## `_saveDismissed` — function, line 19
- **called from:**
- `static/js/research/jobs.js:19`
- `static/js/research/jobs.js:26`

## `_isDismissed` — function, line 22
- **called from:**
- `static/js/research/jobs.js:22`

## `_markDismissed` — function, line 23
- **called from:**
- `static/js/research/jobs.js:23`
- `static/js/research/jobs.js:220`
- `static/js/research/jobs.js:229`

## `init` — function, line 35
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

## `adoptSession` — function, line 48
- **called from:**
- `static/js/research/jobs.js:48`

## `refreshLibrary` — function, line 53
- **called from:**
- `static/js/research/jobs.js:53`

## `_reconnectActive` — function, line 57
- **called from:**
- `static/js/research/jobs.js:37`
- `static/js/research/jobs.js:43`
- `static/js/research/jobs.js:50`
- `static/js/research/jobs.js:57`

## `_syncLibrary` — function, line 89
- **called from:**
- `static/js/research/jobs.js:54`
- `static/js/research/jobs.js:81`
- `static/js/research/jobs.js:89`

## `_parseDuration` — function, line 145
- **called from:**
- `static/js/research/jobs.js:102`
- `static/js/research/jobs.js:145`

## `setRenderCallback` — function, line 150
- **called from:**
- `static/js/research/jobs.js:150`
- `static/js/research/panel.js:215`

## `getJobs` — function, line 151
- **called from:**
- `static/js/research/jobs.js:151`
- `static/js/research/panel.js:109`
- `static/js/research/panel.js:548`
- `static/js/research/panel.js:553`
- `static/js/research/panel.js:670`

## `addToQueue` — function, line 153
- **called from:**
- `static/js/research/jobs.js:153`
- `static/js/research/jobs.js:161`
- `static/js/research/panel.js:507`
- `static/js/research/panel.js:550`

## `startJob` — function, line 160
- **called from:**
- `static/js/research/jobs.js:160`
- `static/js/research/panel.js:600`

## `startQueued` — function, line 166
- **called from:**
- `static/js/research/jobs.js:166`
- `static/js/research/panel.js:917`

## `startAllQueued` — function, line 172
- **called from:**
- `static/js/research/jobs.js:172`
- `static/js/research/panel.js:589`
- `static/js/research/panel.js:882`

## `startAllQueuedSequential` — function, line 179
- **called from:**
- `static/js/research/jobs.js:179`
- `static/js/research/panel.js:883`

## `retryJob` — function, line 192
- **called from:**
- `static/js/research/jobs.js:192`
- `static/js/research/panel.js:1068`

## `cancelJob` — function, line 207
- **called from:**
- `static/js/research/jobs.js:207`
- `static/js/research/panel.js:948`

## `removeJob` — function, line 215
- **called from:**
- `static/js/research/jobs.js:215`
- `static/js/research/panel.js:535`
- `static/js/research/panel.js:923`
- `static/js/research/panel.js:1046`
- `static/js/research/panel.js:1050`
- `static/js/research/panel.js:1074`

## `clearAll` — function, line 226
- **called from:**
- `static/js/document.js:11122`
- `static/js/research/jobs.js:226`
- `static/js/research/panel.js:811`

## `formatElapsed` — function, line 238
- **called from:**
- `static/js/research/jobs.js:238`
- `static/js/research/panel.js:894`

## `formatPhase` — function, line 244
- **called from:**
- `static/js/research/jobs.js:244`
- `static/js/research/panel.js:931`

## `_makeJob` — function, line 259
- **called from:**
- `static/js/research/jobs.js:154`
- `static/js/research/jobs.js:259`

## `_launchJob` — function, line 272
- **called from:**
- `static/js/research/jobs.js:162`
- `static/js/research/jobs.js:169`
- `static/js/research/jobs.js:174`
- `static/js/research/jobs.js:182`
- `static/js/research/jobs.js:204`
- `static/js/research/jobs.js:272`

## `_connectStream` — function, line 302
- **called from:**
- `static/js/research/jobs.js:77`
- `static/js/research/jobs.js:298`
- `static/js/research/jobs.js:302`

## `_pollFallback` — function, line 333
- **called from:**
- `static/js/research/jobs.js:329`
- `static/js/research/jobs.js:333`
- `static/js/research/jobs.js:346`

## `_finishJob` — function, line 350
- **called from:**
- `static/js/research/jobs.js:212`
- `static/js/research/jobs.js:314`
- `static/js/research/jobs.js:319`
- `static/js/research/jobs.js:337`
- `static/js/research/jobs.js:342`
- `static/js/research/jobs.js:347`
- `static/js/research/jobs.js:350`

## `onComplete` — function, line 365
- **called from:**
- `static/js/research/jobs.js:365`
- `static/js/research/panel.js:216`

## `_fetchResult` — function, line 367
- **called from:**
- `static/js/research/jobs.js:320`
- `static/js/research/jobs.js:343`
- `static/js/research/jobs.js:367`

## `_notify` — function, line 382
- **called from:**
- `static/js/research/jobs.js:82`
- `static/js/research/jobs.js:121`
- `static/js/research/jobs.js:138`
- `static/js/research/jobs.js:156`
- `static/js/research/jobs.js:203`
- `static/js/research/jobs.js:210`
- `static/js/research/jobs.js:223`
- `static/js/research/jobs.js:235`
- `static/js/research/jobs.js:285`
- `static/js/research/jobs.js:292`
- `static/js/research/jobs.js:299`
- `static/js/research/jobs.js:305`
- `static/js/research/jobs.js:323`
- `static/js/research/jobs.js:361`
- `static/js/research/jobs.js:378`
- `static/js/research/jobs.js:382`
