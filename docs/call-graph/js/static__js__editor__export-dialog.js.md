# `static/js/editor/export-dialog.js` — definitions & call sites

11 definitions (regex-based, best-effort).
**Exports:** `encodeExportCanvas`, `normalizeExportSettings`, `openExportDialog`, `prepareExportCanvas`

## `clampNumber` — function, line 12
- **called from:**
- `static/js/editor/export-dialog.js:12`
- `static/js/editor/export-dialog.js:21`
- `static/js/editor/export-dialog.js:22`
- `static/js/editor/export-dialog.js:23`

## `normalizeExportSettings` — function, line 17
- **called from:**
- `static/js/editor/export-dialog.js:17`
- `static/js/editor/export-dialog.js:31`
- `static/js/editor/export-dialog.js:47`
- `static/js/editor/export-dialog.js:141`

## `prepareExportCanvas` — function, line 30
- **called from:**
- `static/js/editor/export-dialog.js:30`
- `static/js/editor/export-dialog.js:48`

## `encodeExportCanvas` — function, line 46
- **called from:**
- `static/js/editor/export-dialog.js:46`
- `static/js/editor/export-dialog.js:181`

## `formatBytes` — function, line 67
- **called from:**
- `static/js/editor/export-dialog.js:67`
- `static/js/editor/export-dialog.js:182`

## `openExportDialog` — function, line 74
- **called from:**
- `static/js/editor/export-dialog.js:74`

## `settings` — arrow, line 141
- **called from:**
- `static/js/cookbookRunning.js:1452`
- `static/js/cookbookRunning.js:2070`
- `static/js/cookbookRunning.js:4364`
- `static/js/cookbookServe.js:3814`
- `static/js/editor/export-dialog.js:152`
- `static/js/editor/export-dialog.js:181`
- `static/js/editor/export-dialog.js:229`
- `static/js/editor/tools/gradient.js:17`
- `static/js/editor/tools/gradient.js:38`
- `static/js/galleryEditor.js:585`
- `static/js/galleryEditor.js:11791`
- `static/js/settings.js:2047`

## `renderPreview` — arrow, line 151
- **called from:**
- `static/js/editor/export-dialog.js:175`

## `update` — arrow, line 168
- **called from:**
- `app.py:487`
- `app.py:1336`
- `app.py:1356`
- `core/database.py:3084`
- `core/session_manager.py:989`
- `routes/auth_routes.py:474`
- `routes/auth_routes.py:487`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:919`
- `routes/chat_helpers.py:1062`
- `routes/chat_helpers.py:1079`
- `routes/chat_helpers.py:1096`
- `routes/chat_routes.py:1442`
- `routes/chat_routes.py:1493`
- `routes/chat_routes.py:3580`
- `routes/chat_routes.py:3639`
- `routes/chat_routes.py:3651`
- `routes/chat_routes.py:3669`
- `routes/chat_routes.py:3685`
- `routes/chat_routes.py:3687`
- `routes/chat_routes.py:3690`
- `routes/chat_routes.py:3692`
- `routes/chat_routes.py:3694`
- `routes/chat_routes.py:3697`
- `routes/chat_routes.py:3705`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3717`
- `routes/chat_routes.py:3721`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3735`
- `routes/chat_routes.py:3742`
- `routes/chat_routes.py:3826`
- `routes/chat_routes.py:3835`
- `routes/chat_routes.py:3839`
- `routes/chat_routes.py:4025`
- `routes/chat_routes.py:4439`
- `routes/chat_routes.py:4680`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:5001`
- `routes/chat_routes.py:5005`
- `routes/cookbook_routes.py:3264`
- `routes/cookbook_routes.py:3268`
- `routes/cookbook_routes.py:3271`
- `routes/cookbook_routes.py:3386`
- `routes/cookbook_routes.py:4121`
- `routes/device_flow.py:156`
- `routes/email/email_pollers.py:969`
- `routes/email/email_routes.py:187`
- `routes/email/email_routes.py:1307`
- `routes/email/email_routes.py:2526`
- `routes/email/email_routes.py:2872`
- `routes/email/email_routes.py:4906`
- `routes/email/email_routes.py:4976`
- `routes/email/email_routes.py:5502`
- `routes/email/email_routes.py:5503`
- `routes/email/email_routes.py:5506`
- `routes/email/email_routes.py:5511`
- `routes/email/email_routes.py:6640`
- … +548 more (grep the name in repo)

## `close` — arrow, line 213
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)

## `onKey` — arrow, line 222
- **called from:**
- `static/js/cookbookServe.js:1082`
- `static/js/document.js:9403`
- `static/js/document.js:9453`
- `static/js/document.js:9491`
- `static/js/editor/tools/perspective-crop.js:85`
- `static/js/galleryEditor.js:13664`
- `static/js/settings.js:1644`
- `static/js/skills.js:1773`
- `static/js/ui.js:848`
- `static/js/ui.js:951`
