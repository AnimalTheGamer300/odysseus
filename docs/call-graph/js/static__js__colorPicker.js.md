# `static/js/colorPicker.js` — definitions & call sites

28 definitions (regex-based, best-effort).
**Exports:** `attachColorPicker`, `initColorPickers`, `refreshColorPickers`

## `clamp` — function, line 17
- **called from:**
- `static/js/colorPicker.js:17`
- `static/js/colorPicker.js:29`
- `static/js/colorPicker.js:93`
- `static/js/colorPicker.js:272`
- `static/js/colorPicker.js:273`
- `static/js/colorPicker.js:280`
- `static/js/galleryEditor.js:2372`
- `static/js/galleryEditor.js:2373`
- `static/js/galleryEditor.js:2374`
- `static/js/galleryEditor.js:2375`
- `static/js/galleryEditor.js:2382`
- `static/js/memory.js:305`
- `static/js/memory.js:313`

## `hexToRgb` — function, line 19
- **called from:**
- `static/js/color/hex.js:8`
- `static/js/colorPicker.js:19`
- `static/js/colorPicker.js:69`
- `static/js/theme.js:133`
- `static/js/theme.js:1980`
- `static/js/theme.js:2164`

## `rgbToHex` — function, line 27
- **called from:**
- `static/js/colorPicker.js:27`
- `static/js/colorPicker.js:67`

## `rgbToHsv` — function, line 33
- **called from:**
- `static/js/colorPicker.js:33`
- `static/js/colorPicker.js:69`

## `hsvToRgb` — function, line 47
- **called from:**
- `static/js/colorPicker.js:47`
- `static/js/colorPicker.js:67`

## `hsvToHex` — function, line 67
- **called from:**
- `static/js/colorPicker.js:67`
- `static/js/colorPicker.js:89`
- `static/js/colorPicker.js:90`
- `static/js/colorPicker.js:91`
- `static/js/colorPicker.js:92`
- `static/js/colorPicker.js:93`
- `static/js/colorPicker.js:140`
- `static/js/colorPicker.js:148`
- `static/js/colorPicker.js:169`

## `hexToHsv` — function, line 69
- **called from:**
- `static/js/colorPicker.js:69`
- `static/js/colorPicker.js:176`

## `getRecents` — function, line 72
- **called from:**
- `static/js/colorPicker.js:72`
- `static/js/colorPicker.js:79`
- `static/js/colorPicker.js:161`

## `addRecent` — function, line 77
- **called from:**
- `static/js/colorPicker.js:77`
- `static/js/colorPicker.js:288`

## `computeSuggestions` — function, line 86
- **called from:**
- `static/js/colorPicker.js:86`
- `static/js/colorPicker.js:154`

## `buildPopover` — function, line 98
- **called from:**
- `static/js/colorPicker.js:98`
- `static/js/colorPicker.js:335`

## `syncUI` — function, line 131
- **called from:**
- `static/js/colorPicker.js:131`
- `static/js/colorPicker.js:172`
- `static/js/colorPicker.js:289`
- `static/js/colorPicker.js:346`

## `applyToInput` — function, line 167
- **called from:**
- `static/js/colorPicker.js:167`
- `static/js/colorPicker.js:216`
- `static/js/colorPicker.js:228`
- `static/js/colorPicker.js:245`
- `static/js/colorPicker.js:276`
- `static/js/colorPicker.js:282`

## `setFromHex` — function, line 175
- **called from:**
- `static/js/colorPicker.js:175`
- `static/js/colorPicker.js:215`
- `static/js/colorPicker.js:227`
- `static/js/colorPicker.js:244`
- `static/js/colorPicker.js:337`

## `_installWindowPointer` — function, line 184
- **called from:**
- `static/js/colorPicker.js:184`
- `static/js/colorPicker.js:209`

## `wireHandlers` — function, line 196
- **called from:**
- `static/js/colorPicker.js:126`
- `static/js/colorPicker.js:196`

## `onDown` — arrow, line 202
- **called from:**
- `static/js/colorPicker.js:207`
- `static/js/colorPicker.js:208`

## `handleDrag` — function, line 268
- **called from:**
- `static/js/colorPicker.js:187`
- `static/js/colorPicker.js:204`
- `static/js/colorPicker.js:268`

## `commitCurrent` — function, line 286
- **called from:**
- `static/js/colorPicker.js:191`
- `static/js/colorPicker.js:220`
- `static/js/colorPicker.js:229`
- `static/js/colorPicker.js:246`
- `static/js/colorPicker.js:286`

## `position` — function, line 293
- **called from:**
- `static/js/colorPicker.js:293`
- `static/js/colorPicker.js:344`
- `static/js/modalManager.js:166`
- `static/js/tileManager.js:186`

## `_detachOutsideHandlers` — function, line 308
- **called from:**
- `static/js/colorPicker.js:240`
- `static/js/colorPicker.js:308`
- `static/js/colorPicker.js:322`

## `_destroyPopover` — function, line 321
- **called from:**
- `static/js/colorPicker.js:321`
- `static/js/colorPicker.js:334`
- `static/js/colorPicker.js:388`

## `open` — function, line 331
- **called from:**
- `app.py:1003`
- `app.py:1150`
- `app.py:1197`
- `companion/pairing.py:167`
- `core/atomic_io.py:35`
- `core/atomic_io.py:56`
- `core/auth.py:117`
- `core/auth.py:140`
- `core/database.py:1429`
- `core/database.py:1487`
- `core/database.py:1495`
- `core/database.py:1505`
- `core/database.py:1527`
- `core/platform_compat.py:303`
- `launcher.py:92`
- `launcher.py:131`
- `mcp_servers/email_server.py:1212`
- `routes/admin_wipe/admin_wipe_routes.py:48`
- `routes/auth_routes.py:509`
- `routes/chat_helpers.py:855`
- `routes/cookbook_routes.py:875`
- `routes/diagnostics_routes.py:42`
- `routes/document/document_routes.py:1161`
- `routes/document/document_routes.py:1221`
- `routes/document/document_routes.py:1296`
- `routes/email_helpers.py:532`
- `routes/email_helpers.py:1619`
- `routes/email_routes.py:4028`
- `routes/email_routes.py:4052`
- `routes/gallery/gallery_helpers.py:35`
- `routes/gallery/gallery_routes.py:45`
- `routes/gallery/gallery_routes.py:461`
- `routes/gallery/gallery_routes.py:534`
- `routes/gallery/gallery_routes.py:1326`
- `routes/gallery/gallery_routes.py:1327`
- `routes/gallery/gallery_routes.py:1400`
- `routes/gallery/gallery_routes.py:1440`
- `routes/gallery/gallery_routes.py:1441`
- `routes/gallery/gallery_routes.py:1727`
- `routes/gallery/gallery_routes.py:1760`
- `routes/gallery/gallery_routes.py:1810`
- `routes/gallery/gallery_routes.py:1986`
- `routes/gallery/gallery_routes.py:1994`
- `routes/gallery/gallery_routes.py:2070`
- `routes/mcp/mcp_routes.py:229`
- `routes/mcp/mcp_routes.py:445`
- `routes/mcp/mcp_routes.py:539`
- `routes/mcp/mcp_routes.py:569`
- `routes/model_routes.py:134`
- `routes/model_routes.py:251`
- `routes/personal_routes.py:354`
- `routes/prefs_routes.py:19`
- `routes/shell_routes.py:1553`
- `routes/upload_routes.py:391`
- `routes/upload_routes.py:476`
- `routes/upload_routes.py:489`
- `routes/upload_routes.py:522`
- `scripts/add_hwfit_models.py:189`
- `scripts/add_hwfit_models.py:364`
- `scripts/add_hwfit_models.py:405`
- … +307 more (grep the name in repo)

## `close` — function, line 387
- **called from:**
- `app.py:333`
- `app.py:451`
- `app.py:532`
- `app.py:1050`
- `app.py:1174`
- `app.py:1295`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:923`
- `core/database.py:946`
- `core/database.py:971`
- `core/database.py:994`
- `core/database.py:1017`
- `core/database.py:1048`
- `core/database.py:1073`
- `core/database.py:1097`
- `core/database.py:1125`
- `core/database.py:1148`
- `core/database.py:1171`
- `core/database.py:1194`
- `core/database.py:1217`
- `core/database.py:1249`
- `core/database.py:1272`
- `core/database.py:1295`
- `core/database.py:1319`
- `core/database.py:1343`
- `core/database.py:1377`
- `core/database.py:1406`
- `core/database.py:1479`
- `core/database.py:2068`
- `core/database.py:2301`
- `core/database.py:2363`
- `core/database.py:2479`
- `core/database.py:2506`
- `core/database.py:2532`
- `core/database.py:2557`
- `core/database.py:2584`
- `core/database.py:2606`
- `core/database.py:2619`
- `core/database.py:2635`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:428`
- `core/session_manager.py:568`
- `core/session_manager.py:603`
- `core/session_manager.py:651`
- `core/session_manager.py:771`
- `core/session_manager.py:858`
- `core/session_manager.py:885`
- `core/session_manager.py:899`
- `core/session_manager.py:945`
- `core/session_manager.py:989`
- `core/session_manager.py:1013`
- `core/session_manager.py:1033`
- `core/session_manager.py:1054`
- `core/session_manager.py:1140`
- `mcp_servers/email_server.py:220`
- `mcp_servers/email_server.py:815`
- `mcp_servers/email_server.py:1351`
- … +754 more (grep the name in repo)

## `_syncSwatch` — function, line 395
- **called from:**
- `static/js/colorPicker.js:395`
- `static/js/colorPicker.js:419`

## `attachColorPicker` — function, line 400
- **called from:**
- `static/js/calendar.js:2676`
- `static/js/colorPicker.js:400`
- `static/js/editor/wire-inpaint-controls.js:166`
- `static/js/notes.js:4061`
- `static/js/theme.js:1367`
- `static/js/theme.js:1401`

## `initColorPickers` — function, line 446
- **called from:**
- `static/js/colorPicker.js:446`
- `static/js/colorPicker.js:452`
- `static/js/theme.js:683`
- `static/js/theme.js:1362`

## `refreshColorPickers` — function, line 451
- **called from:**
- `static/js/colorPicker.js:451`
