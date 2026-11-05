# `static/js/cookbook-hwfit.js` — definitions & call sites

87 definitions (regex-based, best-effort).
**Exports:** `_cachedModelIds`, `_cancelHwfitRequests`, `_expandModelRow`, `_fitColors`, `_gpuToggleTotal`, `_hwfitCache`, `_hwfitColumns`, `_hwfitDebounce`, `_hwfitFetch`, `_hwfitInit`, `_hwfitRenderHw`, `_hwfitRenderList`, `_renderGpuToggles`, `_resetGpuToggleState`

## `_fetchHwfitWithTimeout` — function, line 45
- **called from:**
- `static/js/cookbook-hwfit.js:45`
- `static/js/cookbook-hwfit.js:138`
- `static/js/cookbook-hwfit.js:618`
- `static/js/cookbook-hwfit.js:807`
- `static/js/cookbook-hwfit.js:888`
- `static/js/cookbook-hwfit.js:909`
- `static/js/cookbook-hwfit.js:1821`
- `static/js/cookbook-hwfit.js:1875`
- `static/js/cookbook-hwfit.js:2027`
- `static/js/cookbook-hwfit.js:2460`
- `static/js/cookbook-hwfit.js:2506`
- `static/js/cookbook-hwfit.js:2763`

## `abortFromParent` — arrow, line 49
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_dependencyPkgForModel` — function, line 59
- **called from:**
- `static/js/cookbook-hwfit.js:59`
- `static/js/cookbook-hwfit.js:127`

## `_normalizeCookbookModelDir` — function, line 66
- **called from:**
- `static/js/cookbook-hwfit.js:66`
- `static/js/cookbook-hwfit.js:2413`
- `static/js/cookbook.js:57`
- `static/js/cookbook.js:2083`
- `static/js/cookbook.js:2169`
- `static/js/cookbook.js:3323`
- `static/js/cookbookServe.js:81`
- `static/js/cookbookServe.js:4049`
- `static/js/cookbookServe.js:4289`
- `static/js/cookbookServe.js:4302`

## `_wireServerColorPicker` — function, line 71
- **called from:**
- `static/js/cookbook-hwfit.js:71`
- `static/js/cookbook-hwfit.js:2649`

## `close` — arrow, line 78
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

## `open` — arrow, line 82
- **called from:**
- `app.py:1102`
- `app.py:1168`
- `app.py:1334`
- `app.py:1389`
- `companion/pairing.py:167`
- `core/atomic_io.py:38`
- `core/atomic_io.py:74`
- `core/atomic_io.py:95`
- `core/auth.py:135`
- `core/auth.py:158`
- `core/database.py:1681`
- `core/database.py:1739`
- `core/database.py:1747`
- `core/database.py:1757`
- `core/database.py:1779`
- `core/platform_compat.py:325`
- `launcher.py:92`
- `launcher.py:131`
- `mcp_servers/email_server.py:2400`
- `routes/admin_wipe/admin_wipe_routes.py:48`
- `routes/auth_routes.py:559`
- `routes/chat_helpers.py:245`
- `routes/chat_helpers.py:264`
- `routes/chat_helpers.py:282`
- `routes/chat_helpers.py:286`
- `routes/chat_helpers.py:311`
- `routes/chat_helpers.py:346`
- `routes/chat_helpers.py:349`
- `routes/chat_helpers.py:1425`
- `routes/cookbook_routes.py:749`
- `routes/diagnostics_routes.py:42`
- `routes/document/document_routes.py:1385`
- `routes/document/document_routes.py:1445`
- `routes/document/document_routes.py:1520`
- `routes/email/email_helpers.py:661`
- `routes/email/email_helpers.py:1766`
- `routes/email/email_routes.py:4974`
- `routes/email/email_routes.py:4998`
- `routes/email/email_routes.py:5005`
- `routes/email/email_routes.py:5662`
- `routes/email/email_routes.py:5686`
- `routes/gallery/gallery_helpers.py:35`
- `routes/gallery/gallery_routes.py:62`
- `routes/gallery/gallery_routes.py:303`
- `routes/gallery/gallery_routes.py:359`
- `routes/gallery/gallery_routes.py:362`
- `routes/gallery/gallery_routes.py:391`
- `routes/gallery/gallery_routes.py:967`
- `routes/gallery/gallery_routes.py:1040`
- `routes/gallery/gallery_routes.py:1855`
- `routes/gallery/gallery_routes.py:1856`
- `routes/gallery/gallery_routes.py:1980`
- `routes/gallery/gallery_routes.py:2861`
- `routes/history/history_routes.py:62`
- `routes/history/history_routes.py:88`
- `routes/history/history_routes.py:93`
- `routes/mcp/mcp_routes.py:249`
- `routes/mcp/mcp_routes.py:470`
- `routes/mcp/mcp_routes.py:586`
- `routes/mcp/mcp_routes.py:616`
- … +499 more (grep the name in repo)

## `onDocumentClick` — arrow, line 113
- **called from:**
- `static/js/editor/actions-panel.js:192`

## `_ensureBackendInstalled` — function, line 125
- **called from:**
- `static/js/cookbook-hwfit.js:125`
- `static/js/cookbook-hwfit.js:2001`

## `_firstGgufSource` — function, line 176
- **called from:**
- `static/js/cookbook-hwfit.js:176`
- `static/js/cookbook-hwfit.js:188`
- `static/js/cookbookDownload.js:69`
- `static/js/cookbookDownload.js:81`

## `_looksLikeGgufRepo` — function, line 181
- **called from:**
- `static/js/cookbook-hwfit.js:181`
- `static/js/cookbook-hwfit.js:190`
- `static/js/cookbookDownload.js:74`
- `static/js/cookbookDownload.js:83`

## `_downloadSourceRepo` — function, line 186
- **called from:**
- `static/js/cookbook-hwfit.js:186`
- `static/js/cookbook-hwfit.js:1709`

## `_resetGpuToggleState` — function, line 203
- **called from:**
- `static/js/cookbook-hwfit.js:203`
- `static/js/cookbook-hwfit.js:569`
- `static/js/cookbook-hwfit.js:763`
- `static/js/cookbook-hwfit.js:1076`
- `static/js/cookbook-hwfit.js:1223`
- `static/js/cookbook-hwfit.js:1245`
- `static/js/cookbook-hwfit.js:1253`
- `static/js/cookbook-hwfit.js:1275`
- `static/js/cookbook-hwfit.js:1316`
- `static/js/cookbook-hwfit.js:2340`
- `static/js/cookbook-hwfit.js:2932`
- `static/js/cookbook.js:1988`
- `static/js/cookbook.js:2139`

## `_shortGpuName` — function, line 221
- **called from:**
- `static/js/cookbook-hwfit.js:221`
- `static/js/cookbook-hwfit.js:279`
- `static/js/cookbook-hwfit.js:1162`

## `_validTpCounts` — function, line 232
- **called from:**
- `static/js/cookbook-hwfit.js:232`
- `static/js/cookbook-hwfit.js:284`

## `_renderGpuToggles` — function, line 238
- **called from:**
- `static/js/cookbook-hwfit.js:238`
- `static/js/cookbook-hwfit.js:328`
- `static/js/cookbook-hwfit.js:1018`

## `_ctxLabel` — function, line 381
- **called from:**
- `static/js/cookbook-hwfit.js:381`
- `static/js/cookbook-hwfit.js:400`
- `static/js/cookbook-hwfit.js:2297`

## `_ctxValue` — function, line 387
- **called from:**
- `static/js/cookbook-hwfit.js:379`
- `static/js/cookbook-hwfit.js:387`
- `static/js/cookbook-hwfit.js:400`
- `static/js/cookbook-hwfit.js:501`
- `static/js/cookbook-hwfit.js:838`
- `static/js/cookbook-hwfit.js:2297`
- `static/js/cookbook-hwfit.js:2300`
- `static/js/cookbook.js:3283`

## `_syncCtxControl` — function, line 393
- **called from:**
- `static/js/cookbook-hwfit.js:393`
- `static/js/cookbook-hwfit.js:2265`

## `_manualHwState` — function, line 403
- **called from:**
- `static/js/cookbook-hwfit.js:403`
- `static/js/cookbook-hwfit.js:419`
- `static/js/cookbook-hwfit.js:719`
- `static/js/cookbook-hwfit.js:1191`
- `static/js/cookbook-hwfit.js:1279`

## `_saveManualHwState` — function, line 411
- **called from:**
- `static/js/cookbook-hwfit.js:411`
- `static/js/cookbook-hwfit.js:1240`
- `static/js/cookbook-hwfit.js:1271`
- `static/js/cookbook-hwfit.js:1315`

## `_manualHwParams` — function, line 418
- **called from:**
- `static/js/cookbook-hwfit.js:418`
- `static/js/cookbook-hwfit.js:504`
- `static/js/cookbook-hwfit.js:867`

## `_manualNumber` — function, line 430
- **called from:**
- `static/js/cookbook-hwfit.js:430`
- `static/js/cookbook-hwfit.js:1310`
- `static/js/cookbook-hwfit.js:1311`

## `_manualOptionalNumber` — function, line 438
- **called from:**
- `static/js/cookbook-hwfit.js:438`
- `static/js/cookbook-hwfit.js:1312`

## `_manualHwLabel` — function, line 446
- **called from:**
- `static/js/cookbook-hwfit.js:446`
- `static/js/cookbook-hwfit.js:1194`

## `_manualDisplaySystem` — function, line 458
- **called from:**
- `static/js/cookbook-hwfit.js:458`
- `static/js/cookbook-hwfit.js:1320`

## `_scanSig` — function, line 493
- **called from:**
- `static/js/cookbook-hwfit.js:493`
- `static/js/cookbook-hwfit.js:724`

## `_readScanCache` — function, line 509
- **called from:**
- `static/js/cookbook-hwfit.js:509`
- `static/js/cookbook-hwfit.js:725`

## `_readNearestScanCache` — function, line 518
- **called from:**
- `static/js/cookbook-hwfit.js:518`
- `static/js/cookbook-hwfit.js:727`

## `_writeScanCache` — function, line 539
- **called from:**
- `static/js/cookbook-hwfit.js:539`
- `static/js/cookbook-hwfit.js:1012`

## `_hwfitShowError` — function, line 556
- **called from:**
- `static/js/cookbook-hwfit.js:556`
- `static/js/cookbook-hwfit.js:941`
- `static/js/cookbook-hwfit.js:1026`

## `_applyEngineFilter` — function, line 577
- **called from:**
- `static/js/cookbook-hwfit.js:577`
- `static/js/cookbook-hwfit.js:739`
- `static/js/cookbook-hwfit.js:1010`
- `static/js/cookbook-hwfit.js:2288`

## `_ensureOllamaLib` — function, line 613
- **called from:**
- `static/js/cookbook-hwfit.js:613`
- `static/js/cookbook-hwfit.js:950`

## `pending` — arrow, line 616
- **called from:**
- `routes/chatgpt_subscription_routes.py:338`
- `routes/chatgpt_subscription_routes.py:359`
- `routes/chatgpt_subscription_routes.py:364`
- `routes/copilot_routes.py:143`
- `routes/copilot_routes.py:157`
- `routes/copilot_routes.py:163`
- `tests/test_device_flow_routes.py:40`
- `tests/test_device_flow_routes.py:112`
- `tests/test_device_flow_routes.py:128`
- `static/app.js:641`

## `clearPending` — arrow, line 626
- **called from:**
- `static/js/fileHandler.js:249`
- `static/js/fileHandler.js:478`

## `_olParseSize` — function, line 636
- **called from:**
- `static/js/cookbook-hwfit.js:636`
- `static/js/cookbook-hwfit.js:661`

## `_ollamaToHwfitRows` — function, line 648
- **called from:**
- `static/js/cookbook-hwfit.js:648`
- `static/js/cookbook-hwfit.js:951`

## `_ramFitLevel` — arrow, line 651
- **called from:**
- `static/js/cookbook-hwfit.js:668`
- `static/js/cookbook-hwfit.js:671`

## `_hwfitFetch` — function, line 705
- **called from:**
- `static/js/cookbook-hwfit.js:329`
- `static/js/cookbook-hwfit.js:361`
- `static/js/cookbook-hwfit.js:569`
- `static/js/cookbook-hwfit.js:705`
- `static/js/cookbook-hwfit.js:764`
- `static/js/cookbook-hwfit.js:1078`
- `static/js/cookbook-hwfit.js:1225`
- `static/js/cookbook-hwfit.js:1247`
- `static/js/cookbook-hwfit.js:1255`
- `static/js/cookbook-hwfit.js:1277`
- `static/js/cookbook-hwfit.js:1321`
- `static/js/cookbook-hwfit.js:1571`
- `static/js/cookbook-hwfit.js:1587`
- `static/js/cookbook-hwfit.js:2269`
- `static/js/cookbook-hwfit.js:2273`
- `static/js/cookbook-hwfit.js:2277`
- `static/js/cookbook-hwfit.js:2290`
- `static/js/cookbook-hwfit.js:2317`
- `static/js/cookbook-hwfit.js:2342`
- `static/js/cookbook-hwfit.js:2356`
- `static/js/cookbook-hwfit.js:2675`
- `static/js/cookbook-hwfit.js:2703`
- `static/js/cookbook-hwfit.js:2748`
- `static/js/cookbook-hwfit.js:2933`
- `static/js/cookbook.js:1990`
- `static/js/cookbook.js:2030`
- `static/js/cookbook.js:2140`
- `static/js/cookbook.js:2887`
- `static/js/cookbook.js:3432`
- `static/js/cookbookRunning.js:223`

## `is` — class, line 771
- **called from:**
- `static/js/skills.js:1124`
- `static/js/windowResize.js:81`

## `_fitOnly` — arrow, line 884
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderHwVisibilityWarning` — function, line 1032
- **called from:**
- `static/js/cookbook-hwfit.js:1032`
- `static/js/cookbook-hwfit.js:1204`

## `_cancelHwfitRequests` — function, line 1108
- **called from:**
- `static/js/cookbook-hwfit.js:1108`
- `static/js/cookbook.js:3672`

## `_hwfitRenderHw` — function, line 1116
- **called from:**
- `static/js/cookbook-hwfit.js:735`
- `static/js/cookbook-hwfit.js:746`
- `static/js/cookbook-hwfit.js:966`
- `static/js/cookbook-hwfit.js:1116`
- `static/js/cookbook-hwfit.js:1320`

## `_shortGpuName` — arrow, line 1153
- **called from:**
- `static/js/cookbook-hwfit.js:221`
- `static/js/cookbook-hwfit.js:279`
- `static/js/cookbook-hwfit.js:1162`

## `_wireManualHardwareControls` — function, line 1261
- **called from:**
- `static/js/cookbook-hwfit.js:1258`
- `static/js/cookbook-hwfit.js:1261`

## `syncManualButton` — arrow, line 1265
- **called from:**
- `static/js/cookbook-hwfit.js:1274`
- `static/js/cookbook-hwfit.js:1280`
- `static/js/cookbook-hwfit.js:1296`
- `static/js/cookbook-hwfit.js:1302`
- `static/js/cookbook-hwfit.js:1319`
- `static/js/cookbook-hwfit.js:1326`

## `clearManual` — arrow, line 1270
- **called from:**
- `static/js/cookbook-hwfit.js:1237`

## `syncMode` — arrow, line 1285
- **called from:**
- `static/js/cookbook-hwfit.js:1297`
- `static/js/cookbook-hwfit.js:1303`
- `static/js/cookbook-hwfit.js:1325`

## `_requiresAcceleratorBackend` — function, line 1331
- **called from:**
- `static/js/cookbook-hwfit.js:1331`
- `static/js/cookbook-hwfit.js:1339`
- `static/js/cookbook-hwfit.js:1502`
- `static/js/cookbook-hwfit.js:1728`

## `_modeLabel` — function, line 1337
- **called from:**
- `static/js/cookbook-hwfit.js:1337`
- `static/js/cookbook-hwfit.js:1466`

## `_sortHwfitRows` — function, line 1357
- **called from:**
- `static/js/cookbook-hwfit.js:1357`
- `static/js/cookbook-hwfit.js:1396`

## `_hwfitRenderList` — function, line 1394
- **called from:**
- `static/js/cookbook-hwfit.js:739`
- `static/js/cookbook-hwfit.js:1010`
- `static/js/cookbook-hwfit.js:1394`
- `static/js/cookbook-hwfit.js:2288`

## `_fitOnly` — arrow, line 1442
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_syncHostFromScanDropdown` — function, line 1601
- **called from:**
- `static/js/cookbook-hwfit.js:1601`
- `static/js/cookbook-hwfit.js:1749`
- `static/js/cookbook-hwfit.js:1762`

## `_minBackendVersion` — function, line 1628
- **called from:**
- `static/js/cookbook-hwfit.js:1628`
- `static/js/cookbook-hwfit.js:1897`

## `_cmpSemver` — function, line 1651
- **called from:**
- `static/js/cookbook-hwfit.js:1651`
- `static/js/cookbook-hwfit.js:1900`

## `_parse` — arrow, line 1652
- **called from:**
- `src/agent_runtime/effect_log.py:229`
- `src/agent_runtime/effect_log.py:420`
- `src/agent_tools/editor_tools.py:364`
- `src/agent_tools/editor_tools.py:392`
- `src/agent_tools/editor_tools.py:442`
- `src/agent_tools/editor_tools.py:468`
- `src/agent_tools/editor_tools.py:644`
- `src/copilot.py:207`
- `tests/test_calendar_config_body.py:23`
- `tests/test_calendar_config_body.py:28`
- `tests/test_calendar_config_body.py:34`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/cookbook-hwfit.js:1653`
- `static/js/emailLibrary/index.js:3728`
- `static/js/emailLibrary/index.js:3729`

## `_sglangHashFor` — function, line 1668
- **called from:**
- `static/js/cookbook-hwfit.js:1668`

## `_expandModelRow` — function, line 1689
- **called from:**
- `static/js/cookbook-hwfit.js:1550`
- `static/js/cookbook-hwfit.js:1689`

## `_hwfitEngineGlyph` — function, line 2093
- **called from:**
- `static/js/cookbook-hwfit.js:2093`
- `static/js/cookbook-hwfit.js:2206`
- `static/js/cookbook-hwfit.js:2216`

## `_hwfitUsecaseGlyph` — function, line 2104
- **called from:**
- `static/js/cookbook-hwfit.js:2104`
- `static/js/cookbook-hwfit.js:2136`
- `static/js/cookbook-hwfit.js:2146`

## `_bindHwfitUsecasePicker` — function, line 2108
- **called from:**
- `static/js/cookbook-hwfit.js:2108`
- `static/js/cookbook-hwfit.js:2266`

## `setOpen` — arrow, line 2126
- **called from:**
- `static/js/cookbook-hwfit.js:2160`
- `static/js/cookbook-hwfit.js:2169`
- `static/js/cookbook-hwfit.js:2173`
- `static/js/cookbook-hwfit.js:2176`
- `static/js/cookbook-hwfit.js:2230`
- `static/js/cookbook-hwfit.js:2239`
- `static/js/cookbook-hwfit.js:2243`
- `static/js/cookbook-hwfit.js:2246`
- `static/js/features/notes/ui/panel.js:34`
- `static/js/features/notes/ui/panel.js:117`
- `static/js/features/notes/ui/panel.js:323`
- `static/js/galleryEditor.js:1351`
- `static/js/galleryEditor.js:1352`
- `static/js/galleryEditor.js:1353`
- `static/js/galleryEditor.js:1354`

## `currentLabel` — arrow, line 2130
- **called from:**
- `static/js/cookbook-hwfit.js:2135`
- `static/js/cookbook-hwfit.js:2205`

## `syncButton` — arrow, line 2134
- **called from:**
- `static/js/cookbook-hwfit.js:2159`
- `static/js/cookbook-hwfit.js:2163`
- `static/js/cookbook-hwfit.js:2229`
- `static/js/cookbook-hwfit.js:2233`

## `renderMenu` — arrow, line 2143
- **called from:**
- `static/js/cookbook-hwfit.js:2184`
- `static/js/cookbook-hwfit.js:2254`

## `onDocumentClick` — arrow, line 2172
- **called from:**
- `static/js/editor/actions-panel.js:192`

## `onDocumentKeydown` — arrow, line 2175
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_bindHwfitEnginePicker` — function, line 2187
- **called from:**
- `static/js/cookbook-hwfit.js:2187`
- `static/js/cookbook-hwfit.js:2282`

## `setOpen` — arrow, line 2196
- **called from:**
- `static/js/cookbook-hwfit.js:2160`
- `static/js/cookbook-hwfit.js:2169`
- `static/js/cookbook-hwfit.js:2173`
- `static/js/cookbook-hwfit.js:2176`
- `static/js/cookbook-hwfit.js:2230`
- `static/js/cookbook-hwfit.js:2239`
- `static/js/cookbook-hwfit.js:2243`
- `static/js/cookbook-hwfit.js:2246`
- `static/js/features/notes/ui/panel.js:34`
- `static/js/features/notes/ui/panel.js:117`
- `static/js/features/notes/ui/panel.js:323`
- `static/js/galleryEditor.js:1351`
- `static/js/galleryEditor.js:1352`
- `static/js/galleryEditor.js:1353`
- `static/js/galleryEditor.js:1354`

## `currentLabel` — arrow, line 2200
- **called from:**
- `static/js/cookbook-hwfit.js:2135`
- `static/js/cookbook-hwfit.js:2205`

## `syncButton` — arrow, line 2204
- **called from:**
- `static/js/cookbook-hwfit.js:2159`
- `static/js/cookbook-hwfit.js:2163`
- `static/js/cookbook-hwfit.js:2229`
- `static/js/cookbook-hwfit.js:2233`

## `renderMenu` — arrow, line 2213
- **called from:**
- `static/js/cookbook-hwfit.js:2184`
- `static/js/cookbook-hwfit.js:2254`

## `onDocumentClick` — arrow, line 2242
- **called from:**
- `static/js/editor/actions-panel.js:192`

## `onDocumentKeydown` — arrow, line 2245
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_hwfitInit` — function, line 2257
- **called from:**
- `static/js/cookbook-hwfit.js:2257`
- `static/js/cookbook-hwfit.js:2553`
- `static/js/cookbook.js:2029`
- `static/js/cookbook.js:3431`

## `_rebuildServerSelect` — function, line 2365
- **called from:**
- `static/js/cookbook-hwfit.js:2365`
- `static/js/cookbook-hwfit.js:2672`
- `static/js/cookbook-hwfit.js:2701`
- `static/js/cookbook-hwfit.js:2712`
- `static/js/cookbook-hwfit.js:2741`
- `static/js/cookbook-hwfit.js:2894`

## `_syncServers` — function, line 2392
- **called from:**
- `static/js/cookbook-hwfit.js:2392`
- `static/js/cookbook-hwfit.js:2671`
- `static/js/cookbook-hwfit.js:2700`
- `static/js/cookbook-hwfit.js:2711`
- `static/js/cookbook-hwfit.js:2740`
- `static/js/cookbook-hwfit.js:2776`
- `static/js/cookbook-hwfit.js:2797`
- `static/js/cookbook-hwfit.js:2801`
- `static/js/cookbook-hwfit.js:2834`
- `static/js/cookbook-hwfit.js:2837`
- `static/js/cookbook-hwfit.js:2840`
- `static/js/cookbook-hwfit.js:2869`
- `static/js/cookbook-hwfit.js:2892`
- `static/js/cookbook.js:2069`

## `_testServerConnection` — function, line 2436
- **called from:**
- `static/js/cookbook-hwfit.js:2436`
- `static/js/cookbook-hwfit.js:2567`
- `static/js/cookbook-hwfit.js:2583`
- `static/js/cookbook-hwfit.js:2691`

## `setMsg` — arrow, line 2441
- **called from:**
- `static/js/cookbook-hwfit.js:2452`
- `static/js/cookbook-hwfit.js:2457`
- `static/js/cookbook-hwfit.js:2474`
- `static/js/cookbook-hwfit.js:2479`
- `static/js/cookbook-hwfit.js:2484`

## `_singleQuote` — function, line 2488
- **called from:**
- `static/js/cookbook-hwfit.js:2488`
- `static/js/cookbook-hwfit.js:2495`
- `static/js/cookbook-hwfit.js:2502`

## `_serverKeyCommand` — function, line 2492
- **called from:**
- `static/js/cookbook-hwfit.js:2492`
- `static/js/cookbook-hwfit.js:2540`

## `_fetchCookbookSshKey` — function, line 2505
- **called from:**
- `static/js/cookbook-hwfit.js:2505`
- `static/js/cookbook-hwfit.js:2538`
- `static/js/cookbook-hwfit.js:2539`

## `_populateServerKeyPanel` — function, line 2515
- **called from:**
- `static/js/cookbook-hwfit.js:2515`
- `static/js/cookbook-hwfit.js:2631`
- `static/js/cookbook-hwfit.js:2637`
- `static/js/cookbook-hwfit.js:2678`

## `_wireServerEntry` — function, line 2552
- **called from:**
- `static/js/cookbook-hwfit.js:2552`
- `static/js/cookbook-hwfit.js:2891`

## `_wireModelDirTarget` — function, line 2850
- **called from:**
- `static/js/cookbook-hwfit.js:2835`
- `static/js/cookbook-hwfit.js:2844`
- `static/js/cookbook-hwfit.js:2850`
