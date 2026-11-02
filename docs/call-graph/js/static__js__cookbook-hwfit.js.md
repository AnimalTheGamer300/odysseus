# `static/js/cookbook-hwfit.js` — definitions & call sites

77 definitions (regex-based, best-effort).
**Exports:** `_cachedModelIds`, `_expandModelRow`, `_fitColors`, `_gpuToggleTotal`, `_hwfitCache`, `_hwfitColumns`, `_hwfitDebounce`, `_hwfitFetch`, `_hwfitInit`, `_hwfitRenderHw`, `_hwfitRenderList`, `_renderGpuToggles`, `_resetGpuToggleState`

## `_dependencyPkgForModel` — function, line 44
- **called from:**
- `static/js/cookbook-hwfit.js:44`
- `static/js/cookbook-hwfit.js:104`

## `_normalizeCookbookModelDir` — function, line 51
- **called from:**
- `static/js/cookbook-hwfit.js:51`
- `static/js/cookbook-hwfit.js:2303`
- `static/js/cookbook.js:63`
- `static/js/cookbook.js:2039`
- `static/js/cookbook.js:2125`
- `static/js/cookbook.js:3192`
- `static/js/cookbookServe.js:52`
- `static/js/cookbookServe.js:3944`
- `static/js/cookbookServe.js:4159`
- `static/js/cookbookServe.js:4172`

## `_wireServerColorPicker` — function, line 56
- **called from:**
- `static/js/cookbook-hwfit.js:56`
- `static/js/cookbook-hwfit.js:2537`

## `close` — arrow, line 63
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
- `core/database.py:930`
- `core/database.py:961`
- `core/database.py:984`
- `core/database.py:1009`
- `core/database.py:1032`
- `core/database.py:1055`
- `core/database.py:1086`
- `core/database.py:1111`
- `core/database.py:1135`
- `core/database.py:1163`
- `core/database.py:1186`
- `core/database.py:1209`
- `core/database.py:1232`
- `core/database.py:1255`
- `core/database.py:1287`
- `core/database.py:1310`
- `core/database.py:1333`
- `core/database.py:1357`
- `core/database.py:1381`
- `core/database.py:1415`
- `core/database.py:1444`
- `core/database.py:1517`
- `core/database.py:2106`
- `core/database.py:2340`
- `core/database.py:2402`
- `core/database.py:2518`
- `core/database.py:2545`
- `core/database.py:2571`
- `core/database.py:2596`
- `core/database.py:2623`
- `core/database.py:2645`
- `core/database.py:2658`
- `core/database.py:2674`
- `core/session_manager.py:68`
- `core/session_manager.py:178`
- `core/session_manager.py:442`
- `core/session_manager.py:582`
- `core/session_manager.py:654`
- `core/session_manager.py:689`
- `core/session_manager.py:760`
- `core/session_manager.py:880`
- `core/session_manager.py:984`
- `core/session_manager.py:1014`
- `core/session_manager.py:1028`
- `core/session_manager.py:1074`
- `core/session_manager.py:1118`
- `core/session_manager.py:1149`
- `core/session_manager.py:1173`
- `core/session_manager.py:1209`
- `core/session_manager.py:1233`
- `core/session_manager.py:1253`
- … +763 more (grep the name in repo)

## `open` — arrow, line 67
- **called from:**
- `app.py:1003`
- `app.py:1150`
- `app.py:1197`
- `companion/pairing.py:167`
- `core/atomic_io.py:35`
- `core/atomic_io.py:56`
- `core/auth.py:117`
- `core/auth.py:140`
- `core/database.py:1467`
- `core/database.py:1525`
- `core/database.py:1533`
- `core/database.py:1543`
- `core/database.py:1565`
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
- … +311 more (grep the name in repo)

## `_ensureBackendInstalled` — function, line 103
- **called from:**
- `static/js/cookbook-hwfit.js:103`
- `static/js/cookbook-hwfit.js:1920`

## `_firstGgufSource` — function, line 149
- **called from:**
- `static/js/cookbook-hwfit.js:149`
- `static/js/cookbook-hwfit.js:161`
- `static/js/cookbookDownload.js:62`
- `static/js/cookbookDownload.js:74`

## `_looksLikeGgufRepo` — function, line 154
- **called from:**
- `static/js/cookbook-hwfit.js:154`
- `static/js/cookbook-hwfit.js:163`
- `static/js/cookbookDownload.js:67`
- `static/js/cookbookDownload.js:76`

## `_downloadSourceRepo` — function, line 159
- **called from:**
- `static/js/cookbook-hwfit.js:159`
- `static/js/cookbook-hwfit.js:1628`

## `_resetGpuToggleState` — function, line 176
- **called from:**
- `static/js/cookbook-hwfit.js:176`
- `static/js/cookbook-hwfit.js:542`
- `static/js/cookbook-hwfit.js:722`
- `static/js/cookbook-hwfit.js:1025`
- `static/js/cookbook-hwfit.js:1162`
- `static/js/cookbook-hwfit.js:1184`
- `static/js/cookbook-hwfit.js:1192`
- `static/js/cookbook-hwfit.js:1212`
- `static/js/cookbook-hwfit.js:1253`
- `static/js/cookbook-hwfit.js:2233`
- `static/js/cookbook-hwfit.js:2820`
- `static/js/cookbook.js:1956`
- `static/js/cookbook.js:2095`

## `_shortGpuName` — function, line 194
- **called from:**
- `static/js/cookbook-hwfit.js:194`
- `static/js/cookbook-hwfit.js:252`
- `static/js/cookbook-hwfit.js:1101`

## `_validTpCounts` — function, line 205
- **called from:**
- `static/js/cookbook-hwfit.js:205`
- `static/js/cookbook-hwfit.js:257`

## `_renderGpuToggles` — function, line 211
- **called from:**
- `static/js/cookbook-hwfit.js:211`
- `static/js/cookbook-hwfit.js:301`
- `static/js/cookbook-hwfit.js:968`

## `_ctxLabel` — function, line 354
- **called from:**
- `static/js/cookbook-hwfit.js:354`
- `static/js/cookbook-hwfit.js:373`
- `static/js/cookbook-hwfit.js:2190`

## `_ctxValue` — function, line 360
- **called from:**
- `static/js/cookbook-hwfit.js:352`
- `static/js/cookbook-hwfit.js:360`
- `static/js/cookbook-hwfit.js:373`
- `static/js/cookbook-hwfit.js:474`
- `static/js/cookbook-hwfit.js:791`
- `static/js/cookbook-hwfit.js:2190`
- `static/js/cookbook-hwfit.js:2193`
- `static/js/cookbook.js:3154`

## `_syncCtxControl` — function, line 366
- **called from:**
- `static/js/cookbook-hwfit.js:366`
- `static/js/cookbook-hwfit.js:2170`

## `_manualHwState` — function, line 376
- **called from:**
- `static/js/cookbook-hwfit.js:376`
- `static/js/cookbook-hwfit.js:392`
- `static/js/cookbook-hwfit.js:678`
- `static/js/cookbook-hwfit.js:1130`
- `static/js/cookbook-hwfit.js:1216`

## `_saveManualHwState` — function, line 384
- **called from:**
- `static/js/cookbook-hwfit.js:384`
- `static/js/cookbook-hwfit.js:1179`
- `static/js/cookbook-hwfit.js:1208`
- `static/js/cookbook-hwfit.js:1252`

## `_manualHwParams` — function, line 391
- **called from:**
- `static/js/cookbook-hwfit.js:391`
- `static/js/cookbook-hwfit.js:477`
- `static/js/cookbook-hwfit.js:820`

## `_manualNumber` — function, line 403
- **called from:**
- `static/js/cookbook-hwfit.js:403`
- `static/js/cookbook-hwfit.js:1247`
- `static/js/cookbook-hwfit.js:1248`

## `_manualOptionalNumber` — function, line 411
- **called from:**
- `static/js/cookbook-hwfit.js:411`
- `static/js/cookbook-hwfit.js:1249`

## `_manualHwLabel` — function, line 419
- **called from:**
- `static/js/cookbook-hwfit.js:419`
- `static/js/cookbook-hwfit.js:1133`

## `_manualDisplaySystem` — function, line 431
- **called from:**
- `static/js/cookbook-hwfit.js:431`
- `static/js/cookbook-hwfit.js:1257`

## `_scanSig` — function, line 466
- **called from:**
- `static/js/cookbook-hwfit.js:466`
- `static/js/cookbook-hwfit.js:683`

## `_readScanCache` — function, line 482
- **called from:**
- `static/js/cookbook-hwfit.js:482`
- `static/js/cookbook-hwfit.js:684`

## `_readNearestScanCache` — function, line 491
- **called from:**
- `static/js/cookbook-hwfit.js:491`
- `static/js/cookbook-hwfit.js:686`

## `_writeScanCache` — function, line 512
- **called from:**
- `static/js/cookbook-hwfit.js:512`
- `static/js/cookbook-hwfit.js:962`

## `_hwfitShowError` — function, line 529
- **called from:**
- `static/js/cookbook-hwfit.js:529`
- `static/js/cookbook-hwfit.js:891`
- `static/js/cookbook-hwfit.js:975`

## `_applyEngineFilter` — function, line 550
- **called from:**
- `static/js/cookbook-hwfit.js:550`
- `static/js/cookbook-hwfit.js:698`
- `static/js/cookbook-hwfit.js:960`
- `static/js/cookbook-hwfit.js:2182`

## `_ensureOllamaLib` — function, line 585
- **called from:**
- `static/js/cookbook-hwfit.js:585`
- `static/js/cookbook-hwfit.js:900`

## `_olParseSize` — function, line 598
- **called from:**
- `static/js/cookbook-hwfit.js:598`
- `static/js/cookbook-hwfit.js:623`

## `_ollamaToHwfitRows` — function, line 610
- **called from:**
- `static/js/cookbook-hwfit.js:610`
- `static/js/cookbook-hwfit.js:901`

## `_ramFitLevel` — arrow, line 613
- **called from:**
- `static/js/cookbook-hwfit.js:630`
- `static/js/cookbook-hwfit.js:633`

## `_hwfitFetch` — function, line 667
- **called from:**
- `static/js/cookbook-hwfit.js:302`
- `static/js/cookbook-hwfit.js:334`
- `static/js/cookbook-hwfit.js:542`
- `static/js/cookbook-hwfit.js:667`
- `static/js/cookbook-hwfit.js:723`
- `static/js/cookbook-hwfit.js:1027`
- `static/js/cookbook-hwfit.js:1164`
- `static/js/cookbook-hwfit.js:1186`
- `static/js/cookbook-hwfit.js:1194`
- `static/js/cookbook-hwfit.js:1214`
- `static/js/cookbook-hwfit.js:1258`
- `static/js/cookbook-hwfit.js:1490`
- `static/js/cookbook-hwfit.js:1506`
- `static/js/cookbook-hwfit.js:2172`
- `static/js/cookbook-hwfit.js:2173`
- `static/js/cookbook-hwfit.js:2174`
- `static/js/cookbook-hwfit.js:2184`
- `static/js/cookbook-hwfit.js:2210`
- `static/js/cookbook-hwfit.js:2235`
- `static/js/cookbook-hwfit.js:2247`
- `static/js/cookbook-hwfit.js:2563`
- `static/js/cookbook-hwfit.js:2591`
- `static/js/cookbook-hwfit.js:2636`
- `static/js/cookbook-hwfit.js:2821`
- `static/js/cookbook.js:1958`
- `static/js/cookbook.js:1986`
- `static/js/cookbook.js:2096`
- `static/js/cookbook.js:3289`
- `static/js/cookbookRunning.js:219`

## `is` — class, line 730
- **called from:**
- `static/js/skills.js:886`
- `static/js/windowResize.js:44`

## `_fitOnly` — arrow, line 835
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderHwVisibilityWarning` — function, line 981
- **called from:**
- `static/js/cookbook-hwfit.js:981`
- `static/js/cookbook-hwfit.js:1143`

## `_hwfitRenderHw` — function, line 1055
- **called from:**
- `static/js/cookbook-hwfit.js:694`
- `static/js/cookbook-hwfit.js:705`
- `static/js/cookbook-hwfit.js:916`
- `static/js/cookbook-hwfit.js:1055`
- `static/js/cookbook-hwfit.js:1257`

## `_shortGpuName` — arrow, line 1092
- **called from:**
- `static/js/cookbook-hwfit.js:194`
- `static/js/cookbook-hwfit.js:252`
- `static/js/cookbook-hwfit.js:1101`

## `_wireManualHardwareControls` — function, line 1200
- **called from:**
- `static/js/cookbook-hwfit.js:1197`
- `static/js/cookbook-hwfit.js:1200`

## `syncManualButton` — arrow, line 1204
- **called from:**
- `static/js/cookbook-hwfit.js:1211`
- `static/js/cookbook-hwfit.js:1217`
- `static/js/cookbook-hwfit.js:1233`
- `static/js/cookbook-hwfit.js:1239`
- `static/js/cookbook-hwfit.js:1256`
- `static/js/cookbook-hwfit.js:1263`

## `clearManual` — arrow, line 1207
- **called from:**
- `static/js/cookbook-hwfit.js:1176`

## `syncMode` — arrow, line 1222
- **called from:**
- `static/js/cookbook-hwfit.js:1234`
- `static/js/cookbook-hwfit.js:1240`
- `static/js/cookbook-hwfit.js:1262`

## `_requiresAcceleratorBackend` — function, line 1268
- **called from:**
- `static/js/cookbook-hwfit.js:1268`
- `static/js/cookbook-hwfit.js:1276`
- `static/js/cookbook-hwfit.js:1435`
- `static/js/cookbook-hwfit.js:1647`

## `_modeLabel` — function, line 1274
- **called from:**
- `static/js/cookbook-hwfit.js:1274`
- `static/js/cookbook-hwfit.js:1399`

## `_sortHwfitRows` — function, line 1294
- **called from:**
- `static/js/cookbook-hwfit.js:1294`
- `static/js/cookbook-hwfit.js:1333`

## `_hwfitRenderList` — function, line 1331
- **called from:**
- `static/js/cookbook-hwfit.js:698`
- `static/js/cookbook-hwfit.js:960`
- `static/js/cookbook-hwfit.js:1331`
- `static/js/cookbook-hwfit.js:2182`

## `_fitOnly` — arrow, line 1375
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_syncHostFromScanDropdown` — function, line 1520
- **called from:**
- `static/js/cookbook-hwfit.js:1520`
- `static/js/cookbook-hwfit.js:1668`
- `static/js/cookbook-hwfit.js:1681`

## `_minBackendVersion` — function, line 1547
- **called from:**
- `static/js/cookbook-hwfit.js:1547`
- `static/js/cookbook-hwfit.js:1816`

## `_cmpSemver` — function, line 1570
- **called from:**
- `static/js/cookbook-hwfit.js:1570`
- `static/js/cookbook-hwfit.js:1819`

## `_parse` — arrow, line 1571
- **called from:**
- `routes/skills_routes.py:272`
- `src/copilot.py:207`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/cookbook-hwfit.js:1572`
- `static/js/emailLibrary.js:3637`
- `static/js/emailLibrary.js:3638`

## `_sglangHashFor` — function, line 1587
- **called from:**
- `static/js/cookbook-hwfit.js:1587`

## `_expandModelRow` — function, line 1608
- **called from:**
- `static/js/cookbook-hwfit.js:1469`
- `static/js/cookbook-hwfit.js:1608`

## `_hwfitEngineGlyph` — function, line 2011
- **called from:**
- `static/js/cookbook-hwfit.js:2011`
- `static/js/cookbook-hwfit.js:2117`
- `static/js/cookbook-hwfit.js:2127`

## `_hwfitUsecaseGlyph` — function, line 2021
- **called from:**
- `static/js/cookbook-hwfit.js:2021`
- `static/js/cookbook-hwfit.js:2053`
- `static/js/cookbook-hwfit.js:2063`

## `_bindHwfitUsecasePicker` — function, line 2025
- **called from:**
- `static/js/cookbook-hwfit.js:2025`
- `static/js/cookbook-hwfit.js:2171`

## `setOpen` — arrow, line 2043
- **called from:**
- `static/js/cookbook-hwfit.js:2077`
- `static/js/cookbook-hwfit.js:2086`
- `static/js/cookbook-hwfit.js:2090`
- `static/js/cookbook-hwfit.js:2093`
- `static/js/cookbook-hwfit.js:2141`
- `static/js/cookbook-hwfit.js:2150`
- `static/js/cookbook-hwfit.js:2154`
- `static/js/cookbook-hwfit.js:2157`
- `static/js/galleryEditor.js:457`
- `static/js/galleryEditor.js:458`

## `currentLabel` — arrow, line 2047
- **called from:**
- `static/js/cookbook-hwfit.js:2052`
- `static/js/cookbook-hwfit.js:2116`

## `syncButton` — arrow, line 2051
- **called from:**
- `static/js/cookbook-hwfit.js:2076`
- `static/js/cookbook-hwfit.js:2080`
- `static/js/cookbook-hwfit.js:2140`
- `static/js/cookbook-hwfit.js:2144`

## `renderMenu` — arrow, line 2060
- **called from:**
- `static/js/cookbook-hwfit.js:2095`
- `static/js/cookbook-hwfit.js:2159`

## `_bindHwfitEnginePicker` — function, line 2098
- **called from:**
- `static/js/cookbook-hwfit.js:2098`
- `static/js/cookbook-hwfit.js:2178`

## `setOpen` — arrow, line 2107
- **called from:**
- `static/js/cookbook-hwfit.js:2077`
- `static/js/cookbook-hwfit.js:2086`
- `static/js/cookbook-hwfit.js:2090`
- `static/js/cookbook-hwfit.js:2093`
- `static/js/cookbook-hwfit.js:2141`
- `static/js/cookbook-hwfit.js:2150`
- `static/js/cookbook-hwfit.js:2154`
- `static/js/cookbook-hwfit.js:2157`
- `static/js/galleryEditor.js:457`
- `static/js/galleryEditor.js:458`

## `currentLabel` — arrow, line 2111
- **called from:**
- `static/js/cookbook-hwfit.js:2052`
- `static/js/cookbook-hwfit.js:2116`

## `syncButton` — arrow, line 2115
- **called from:**
- `static/js/cookbook-hwfit.js:2076`
- `static/js/cookbook-hwfit.js:2080`
- `static/js/cookbook-hwfit.js:2140`
- `static/js/cookbook-hwfit.js:2144`

## `renderMenu` — arrow, line 2124
- **called from:**
- `static/js/cookbook-hwfit.js:2095`
- `static/js/cookbook-hwfit.js:2159`

## `_hwfitInit` — function, line 2162
- **called from:**
- `static/js/cookbook-hwfit.js:2162`
- `static/js/cookbook-hwfit.js:2443`
- `static/js/cookbook.js:1985`
- `static/js/cookbook.js:3288`

## `_rebuildServerSelect` — function, line 2255
- **called from:**
- `static/js/cookbook-hwfit.js:2255`
- `static/js/cookbook-hwfit.js:2560`
- `static/js/cookbook-hwfit.js:2589`
- `static/js/cookbook-hwfit.js:2600`
- `static/js/cookbook-hwfit.js:2629`
- `static/js/cookbook-hwfit.js:2782`

## `_syncServers` — function, line 2282
- **called from:**
- `static/js/cookbook-hwfit.js:2282`
- `static/js/cookbook-hwfit.js:2559`
- `static/js/cookbook-hwfit.js:2588`
- `static/js/cookbook-hwfit.js:2599`
- `static/js/cookbook-hwfit.js:2628`
- `static/js/cookbook-hwfit.js:2664`
- `static/js/cookbook-hwfit.js:2685`
- `static/js/cookbook-hwfit.js:2689`
- `static/js/cookbook-hwfit.js:2722`
- `static/js/cookbook-hwfit.js:2725`
- `static/js/cookbook-hwfit.js:2728`
- `static/js/cookbook-hwfit.js:2757`
- `static/js/cookbook-hwfit.js:2780`
- `static/js/cookbook.js:2025`

## `_testServerConnection` — function, line 2326
- **called from:**
- `static/js/cookbook-hwfit.js:2326`
- `static/js/cookbook-hwfit.js:2457`
- `static/js/cookbook-hwfit.js:2473`
- `static/js/cookbook-hwfit.js:2579`

## `setMsg` — arrow, line 2331
- **called from:**
- `static/js/cookbook-hwfit.js:2342`
- `static/js/cookbook-hwfit.js:2347`
- `static/js/cookbook-hwfit.js:2364`
- `static/js/cookbook-hwfit.js:2369`
- `static/js/cookbook-hwfit.js:2374`

## `_singleQuote` — function, line 2378
- **called from:**
- `static/js/cookbook-hwfit.js:2378`
- `static/js/cookbook-hwfit.js:2385`
- `static/js/cookbook-hwfit.js:2392`

## `_serverKeyCommand` — function, line 2382
- **called from:**
- `static/js/cookbook-hwfit.js:2382`
- `static/js/cookbook-hwfit.js:2430`

## `_fetchCookbookSshKey` — function, line 2395
- **called from:**
- `static/js/cookbook-hwfit.js:2395`
- `static/js/cookbook-hwfit.js:2428`
- `static/js/cookbook-hwfit.js:2429`

## `_populateServerKeyPanel` — function, line 2405
- **called from:**
- `static/js/cookbook-hwfit.js:2405`
- `static/js/cookbook-hwfit.js:2519`
- `static/js/cookbook-hwfit.js:2525`
- `static/js/cookbook-hwfit.js:2566`

## `_wireServerEntry` — function, line 2442
- **called from:**
- `static/js/cookbook-hwfit.js:2442`
- `static/js/cookbook-hwfit.js:2779`

## `_wireModelDirTarget` — function, line 2738
- **called from:**
- `static/js/cookbook-hwfit.js:2723`
- `static/js/cookbook-hwfit.js:2732`
- `static/js/cookbook-hwfit.js:2738`
