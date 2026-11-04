# `static/js/sessions.js` — definitions & call sites

130 definitions (regex-based, best-effort).
**Exports:** `clearResearching`, `clearStreamComplete`, `clearStreaming`, `closeArchive`, `closeLibrary`, `createDirectChat`, `default`, `deleteCurrentSessionFromTopMenu`, `getCurrentEndpointUrl`, `getCurrentModel`, `getCurrentSessionId`, `getPendingChat`, `getSessions`, `getSortMode`, `hasPendingChat`, `initDependencies`, `initDragSort`, `isCurrentSessionIncognito`, `loadSessions`, `markResearching`, `markStreamComplete`, `markStreaming`, `materializePendingSession`, `openArchive`, `openLibrary`, `preMaterializePendingSession`, `renderSessionList`, `selectSession`, `setCurrentSessionId`, `setSessionHasDocs`, `setSortMode`, `updateModelPicker`

## `_mirrorTabTitle` — function, line 28
- **called from:**
- `static/js/sessions.js:28`

## `apply` — arrow, line 31
- **called from:**
- `static/app.js:199`
- `static/js/admin.js:1765`
- `static/js/admin.js:1769`
- `static/js/composerHistoryRecall.js:175`
- `static/js/composerHistoryRecall.js:189`
- `static/js/composerHistoryRecall.js:193`
- `static/js/cookbookSchedule.js:22`
- `static/js/document.js:812`
- `static/js/document.js:821`
- `static/js/document.js:6225`
- `static/js/sessions.js:38`
- `static/js/settings.js:194`
- `static/js/settings.js:213`
- `static/js/skills.js:54`
- `static/js/theme.js:775`
- `static/js/theme.js:780`
- `static/js/ui.js:587`

## `_shouldPreserveStartupComposer` — function, line 57
- **called from:**
- `static/js/sessions.js:57`
- `static/js/sessions.js:65`

## `_clearComposerUnlessStartupTyped` — function, line 63
- **called from:**
- `static/js/sessions.js:63`
- `static/js/sessions.js:2018`
- `static/js/sessions.js:2374`

## `_paintSessionLoading` — function, line 73
- **called from:**
- `static/js/sessions.js:73`
- `static/js/sessions.js:2071`

## `_updateSessionLoading` — function, line 104
- **called from:**
- `static/js/sessions.js:104`
- `static/js/sessions.js:2123`

## `_nextPaint` — function, line 109
- **called from:**
- `static/js/sessions.js:109`
- `static/js/sessions.js:2073`
- `static/js/sessions.js:2124`

## `_displayHistoryContent` — function, line 113
- **called from:**
- `static/js/sessions.js:113`
- `static/js/sessions.js:177`
- `static/js/sessions.js:179`

## `_stripUserVisionBlocks` — function, line 132
- **called from:**
- `static/js/sessions.js:132`
- `static/js/sessions.js:184`

## `_historyPageLimit` — function, line 139
- **called from:**
- `static/js/sessions.js:139`
- `static/js/sessions.js:220`
- `static/js/sessions.js:2076`

## `_historyUrl` — function, line 143
- **called from:**
- `static/js/sessions.js:143`
- `static/js/sessions.js:243`
- `static/js/sessions.js:2076`

## `_addHistoryMessageWithFullRenderer` — function, line 150
- **called from:**
- `static/js/sessions.js:150`
- `static/js/sessions.js:201`

## `_renderHistoryMessage` — function, line 173
- **called from:**
- `static/js/sessions.js:173`
- `static/js/sessions.js:251`
- `static/js/sessions.js:2153`

## `_clearHistoryPager` — function, line 204
- **called from:**
- `static/js/sessions.js:204`
- `static/js/sessions.js:214`
- `static/js/sessions.js:1948`

## `_installHistoryPager` — function, line 212
- **called from:**
- `static/js/sessions.js:212`
- `static/js/sessions.js:2170`

## `loadOlder` — arrow, line 227
- **called from:**
- `static/js/sessions.js:287`
- `static/js/sessions.js:301`

## `_getIncognitoIds` — function, line 307
- **called from:**
- `static/js/sessions.js:307`
- `static/js/sessions.js:311`
- `static/js/sessions.js:314`
- `static/js/sessions.js:316`

## `_markIncognito` — function, line 310
- **called from:**
- `static/js/sessions.js:310`
- `static/js/sessions.js:2434`

## `_isIncognitoSession` — function, line 314
- **called from:**
- `static/js/sessions.js:314`
- `static/js/sessions.js:1176`
- `static/js/sessions.js:1775`
- `static/js/sessions.js:2488`

## `_cleanupIncognitoSessions` — function, line 315
- **called from:**
- `static/js/sessions.js:315`
- `static/js/sessions.js:1765`

## `_deselectCurrentSession` — function, line 339
- **called from:**
- `static/js/sessions.js:339`
- `static/js/sessions.js:378`
- `static/js/sessions.js:981`
- `static/js/sessions.js:1335`
- `static/js/sessions.js:1458`
- `static/js/sessions.js:2542`
- `static/js/sessions.js:2595`

## `_removeSessionFromLocalState` — function, line 359
- **called from:**
- `static/js/sessions.js:359`
- `static/js/sessions.js:982`
- `static/js/sessions.js:2543`

## `_normalizeSessionsList` — function, line 381
- **called from:**
- `static/js/sessions.js:381`
- `static/js/sessions.js:1794`

## `initDependencies` — function, line 396
- **called from:**
- `static/app.js:4311`
- `static/js/sessions.js:396`

## `loadFolderState` — function, line 402
- **called from:**
- `static/js/sessions.js:402`
- `static/js/sessions.js:1257`
- `static/js/sessions.js:1351`
- `static/js/sessions.js:1427`
- `static/js/sessions.js:1469`

## `saveFolderState` — function, line 405
- **called from:**
- `static/js/sessions.js:405`
- `static/js/sessions.js:1354`
- `static/js/sessions.js:1471`

## `loadFolderOrder` — function, line 408
- **called from:**
- `static/js/sessions.js:408`
- `static/js/sessions.js:1281`

## `saveFolderOrder` — function, line 411
- **called from:**
- `static/js/sessions.js:411`
- `static/js/sessions.js:2629`

## `getFolderNames` — function, line 416
- **called from:**
- `static/js/sessions.js:416`
- `static/js/sessions.js:435`

## `moveToFolder` — function, line 423
- **called from:**
- `static/js/sessions.js:423`
- `static/js/sessions.js:453`
- `static/js/sessions.js:467`
- `static/js/sessions.js:490`
- `static/js/sessions.js:1368`

## `buildFolderSubmenu` — function, line 434
- **called from:**
- `static/js/sessions.js:434`
- `static/js/sessions.js:877`

## `createSessionItem` — function, line 547
- **called from:**
- `static/js/sessions.js:547`
- `static/js/sessions.js:1149`
- `static/js/sessions.js:1158`

## `commit` — arrow, line 644
- **called from:**
- `app.py:449`
- `app.py:1047`
- `core/database.py:924`
- `core/database.py:955`
- `core/database.py:978`
- `core/database.py:1003`
- `core/database.py:1026`
- `core/database.py:1049`
- `core/database.py:1080`
- `core/database.py:1105`
- `core/database.py:1129`
- `core/database.py:1158`
- `core/database.py:1180`
- `core/database.py:1203`
- `core/database.py:1227`
- `core/database.py:1249`
- `core/database.py:1282`
- `core/database.py:1304`
- `core/database.py:1327`
- `core/database.py:1351`
- `core/database.py:1375`
- `core/database.py:1409`
- `core/database.py:1438`
- `core/database.py:1512`
- `core/database.py:1591`
- `core/database.py:1606`
- `core/database.py:1632`
- `core/database.py:1704`
- `core/database.py:1723`
- `core/database.py:1735`
- `core/database.py:1747`
- `core/database.py:1764`
- `core/database.py:1784`
- `core/database.py:1805`
- `core/database.py:1817`
- `core/database.py:1830`
- `core/database.py:1835`
- `core/database.py:1847`
- `core/database.py:1851`
- `core/database.py:2098`
- `core/database.py:2251`
- `core/database.py:2335`
- `core/database.py:2396`
- `core/database.py:2425`
- `core/database.py:2457`
- `core/database.py:2491`
- `core/database.py:2512`
- `core/database.py:2539`
- `core/database.py:2565`
- `core/database.py:2595`
- `core/database.py:2618`
- `core/database.py:2640`
- `core/database.py:2669`
- `core/database.py:2745`
- `core/database.py:2813`
- `core/session_manager.py:429`
- `core/session_manager.py:479`
- `core/session_manager.py:504`
- `core/session_manager.py:569`
- `core/session_manager.py:647`
- … +406 more (grep the name in repo)

## `close` — arrow, line 698
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

## `_icon` — arrow, line 733
- **called from:**
- `tests/test_lang_icon_null_opts_js.py:33`
- `tests/test_lang_icon_null_opts_js.py:40`
- `static/js/emailInbox.js:1120`
- `static/js/emailLibrary.js:7898`
- `static/js/emailLibrary.js:7919`
- `static/js/emailLibrary.js:8109`
- `static/js/emailLibrary.js:8126`
- `static/js/sessions.js:741`
- `static/js/sessions.js:745`
- `static/js/sessions.js:749`
- `static/js/sessions.js:760`
- `static/js/sessions.js:767`
- `static/js/sessions.js:801`
- `static/js/sessions.js:817`
- `static/js/sessions.js:859`
- `static/js/sessions.js:894`

## `commit` — arrow, line 945
- **called from:**
- `app.py:449`
- `app.py:1047`
- `core/database.py:924`
- `core/database.py:955`
- `core/database.py:978`
- `core/database.py:1003`
- `core/database.py:1026`
- `core/database.py:1049`
- `core/database.py:1080`
- `core/database.py:1105`
- `core/database.py:1129`
- `core/database.py:1158`
- `core/database.py:1180`
- `core/database.py:1203`
- `core/database.py:1227`
- `core/database.py:1249`
- `core/database.py:1282`
- `core/database.py:1304`
- `core/database.py:1327`
- `core/database.py:1351`
- `core/database.py:1375`
- `core/database.py:1409`
- `core/database.py:1438`
- `core/database.py:1512`
- `core/database.py:1591`
- `core/database.py:1606`
- `core/database.py:1632`
- `core/database.py:1704`
- `core/database.py:1723`
- `core/database.py:1735`
- `core/database.py:1747`
- `core/database.py:1764`
- `core/database.py:1784`
- `core/database.py:1805`
- `core/database.py:1817`
- `core/database.py:1830`
- `core/database.py:1835`
- `core/database.py:1847`
- `core/database.py:1851`
- `core/database.py:2098`
- `core/database.py:2251`
- `core/database.py:2335`
- `core/database.py:2396`
- `core/database.py:2425`
- `core/database.py:2457`
- `core/database.py:2491`
- `core/database.py:2512`
- `core/database.py:2539`
- `core/database.py:2565`
- `core/database.py:2595`
- `core/database.py:2618`
- `core/database.py:2640`
- `core/database.py:2669`
- `core/database.py:2745`
- `core/database.py:2813`
- `core/session_manager.py:429`
- `core/session_manager.py:479`
- `core/session_manager.py:504`
- `core/session_manager.py:569`
- `core/session_manager.py:647`
- … +406 more (grep the name in repo)

## `_dateBucketLabel` — function, line 1062
- **called from:**
- `static/js/sessions.js:1062`
- `static/js/sessions.js:1142`

## `dayStart` — arrow, line 1066
- **called from:**
- `static/js/emailLibrary.js:4904`
- `static/js/emailLibrary.js:4905`
- `static/js/sessions.js:1067`
- `static/js/sessions.js:1068`

## `_sessionBucketDate` — function, line 1083
- **called from:**
- `static/js/sessions.js:1083`
- `static/js/sessions.js:1142`

## `_loadDateSectionCollapseState` — function, line 1087
- **called from:**
- `static/js/sessions.js:1087`
- `static/js/sessions.js:1102`
- `static/js/sessions.js:1106`

## `_saveDateSectionCollapseState` — function, line 1093
- **called from:**
- `static/js/sessions.js:1093`
- `static/js/sessions.js:1109`

## `_dateSectionKey` — function, line 1097
- **called from:**
- `static/js/sessions.js:1097`
- `static/js/sessions.js:1102`
- `static/js/sessions.js:1107`

## `_isDateSectionCollapsed` — function, line 1101
- **called from:**
- `static/js/sessions.js:1101`
- `static/js/sessions.js:1117`
- `static/js/sessions.js:1145`
- `static/js/sessions.js:1156`

## `_toggleDateSection` — function, line 1105
- **called from:**
- `static/js/sessions.js:1105`
- `static/js/sessions.js:1127`
- `static/js/sessions.js:1133`

## `_createDateSectionHeader` — function, line 1113
- **called from:**
- `static/js/sessions.js:1113`
- `static/js/sessions.js:1144`
- `static/js/sessions.js:1155`

## `_appendSessionItemsWithDateHeaders` — function, line 1138
- **called from:**
- `static/js/sessions.js:1138`
- `static/js/sessions.js:1235`
- `static/js/sessions.js:1388`
- `static/js/sessions.js:1488`

## `_appendFavoriteSessionItems` — function, line 1153
- **called from:**
- `static/js/sessions.js:1153`
- `static/js/sessions.js:1234`

## `renderSessionList` — function, line 1163
- **called from:**
- `static/js/keyboard-shortcuts.js:190`
- `static/js/sessions.js:430`
- `static/js/sessions.js:614`
- `static/js/sessions.js:654`
- `static/js/sessions.js:660`
- `static/js/sessions.js:776`
- `static/js/sessions.js:810`
- `static/js/sessions.js:955`
- `static/js/sessions.js:961`
- `static/js/sessions.js:1110`
- `static/js/sessions.js:1163`
- `static/js/sessions.js:1245`
- `static/js/sessions.js:1355`
- `static/js/sessions.js:1398`
- `static/js/sessions.js:1472`
- `static/js/sessions.js:1500`
- `static/js/sessions.js:1795`
- `static/js/sessions.js:3748`
- `static/js/sessions.js:3755`

## `_renderSessionListImpl` — function, line 1169
- **called from:**
- `static/js/sessions.js:1169`

## `starPartition` — arrow, line 1271
- **called from:**
- `static/js/sessions.js:1277`
- `static/js/sessions.js:1278`

## `_postRenderSessionList` — function, line 1513
- **called from:**
- `static/js/sessions.js:1252`
- `static/js/sessions.js:1509`
- `static/js/sessions.js:1513`

## `_initKeyboardNav` — function, line 1528
- **called from:**
- `static/js/sessions.js:1522`
- `static/js/sessions.js:1528`

## `_initSwipeToDelete` — function, line 1539
- **called from:**
- `static/js/sessions.js:1523`
- `static/js/sessions.js:1539`

## `_showSwipeHint` — function, line 1543
- **called from:**
- `static/js/sessions.js:1525`
- `static/js/sessions.js:1543`

## `_forceSidebarOpen` — function, line 1560
- **called from:**
- `static/js/sessions.js:653`
- `static/js/sessions.js:660`
- `static/js/sessions.js:931`
- `static/js/sessions.js:954`
- `static/js/sessions.js:961`
- `static/js/sessions.js:973`
- `static/js/sessions.js:996`
- `static/js/sessions.js:1007`
- `static/js/sessions.js:1014`
- `static/js/sessions.js:1560`

## `_guardSidebarDuringRename` — function, line 1581
- **called from:**
- `static/js/sessions.js:643`
- `static/js/sessions.js:944`
- `static/js/sessions.js:1581`

## `_enterSelectMode` — function, line 1602
- **called from:**
- `static/js/notes.js:1329`
- `static/js/notes.js:1456`
- `static/js/sessions.js:863`
- `static/js/sessions.js:1602`
- `static/js/sessions.js:1660`
- `static/js/sessions.js:1672`
- `static/js/skills.js:414`
- `static/js/skills.js:1673`
- `static/js/skills.js:2004`

## `_exitSelectMode` — function, line 1633
- **called from:**
- `static/js/gallery.js:2520`
- `static/js/gallery.js:2523`
- `static/js/gallery.js:2652`
- `static/js/gallery.js:2691`
- `static/js/gallery.js:2729`
- `static/js/gallery.js:2757`
- `static/js/gallery.js:2769`
- `static/js/gallery.js:2787`
- `static/js/notes.js:1329`
- `static/js/notes.js:1342`
- `static/js/notes.js:1356`
- `static/js/notes.js:1369`
- `static/js/notes.js:1416`
- `static/js/notes.js:1467`
- `static/js/sessions.js:1633`
- `static/js/sessions.js:1659`
- `static/js/sessions.js:1664`
- `static/js/sessions.js:1679`
- `static/js/sessions.js:1720`
- `static/js/sessions.js:1741`
- `static/js/skills.js:641`
- `static/js/skills.js:1684`
- `static/js/skills.js:1754`
- `static/js/skills.js:1813`
- `static/js/skills.js:1833`
- `static/js/skills.js:1844`
- `static/js/skills.js:2004`

## `_updateBulkCount` — function, line 1646
- **called from:**
- `static/js/cookbook.js:2272`
- `static/js/cookbook.js:2283`
- `static/js/cookbook.js:2287`
- `static/js/gallery.js:2488`
- `static/js/gallery.js:2517`
- `static/js/gallery.js:2529`
- `static/js/gallery.js:2538`
- `static/js/gallery.js:2568`
- `static/js/sessions.js:865`
- `static/js/sessions.js:1626`
- `static/js/sessions.js:1630`
- `static/js/sessions.js:1646`
- `static/js/sessions.js:1703`

## `_initBulkSelect` — function, line 1654
- **called from:**
- `static/js/sessions.js:1654`
- `static/js/sessions.js:2908`

## `_toggleAll` — arrow, line 1687
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_animateSessionRowsRemoving` — function, line 1749
- **called from:**
- `static/js/sessions.js:1740`
- `static/js/sessions.js:1749`
- `static/js/sessions.js:3075`
- `static/js/sessions.js:3118`

## `loadSessions` — function, line 1762
- **called from:**
- `static/app.js:620`
- `static/app.js:1464`
- `static/app.js:1669`
- `static/app.js:3419`
- `static/app.js:4328`
- `static/app.js:4424`
- `static/js/chat.js:2524`
- `static/js/chat.js:3645`
- `static/js/chat.js:4188`
- `static/js/chat.js:5053`
- `static/js/chat.js:5222`
- `static/js/chat.js:5930`
- `static/js/chat.js:6014`
- `static/js/chat.js:7021`
- `static/js/chat.js:7771`
- `static/js/chatRenderer.js:1265`
- `static/js/document.js:7316`
- `static/js/documentLibrary.js:2083`
- `static/js/documentLibrary.js:2356`
- `static/js/documentLibrary.js:2805`
- `static/js/documentLibrary.js:2863`
- `static/js/documentLibrary.js:3005`
- `static/js/emailInbox.js:1379`
- `static/js/group.js:692`
- `static/js/keyboard-shortcuts.js:208`
- `static/js/keyboard-shortcuts.js:240`
- `static/js/presets.js:433`
- `static/js/research/panel.js:1230`
- `static/js/sessions.js:1002`
- `static/js/sessions.js:1015`
- `static/js/sessions.js:1340`
- `static/js/sessions.js:1369`
- `static/js/sessions.js:1463`
- `static/js/sessions.js:1722`
- `static/js/sessions.js:1743`
- `static/js/sessions.js:1762`
- `static/js/sessions.js:1836`
- `static/js/sessions.js:2453`
- `static/js/sessions.js:2556`
- `static/js/sessions.js:2596`
- `static/js/sessions.js:3066`
- `static/js/sessions.js:3100`
- `static/js/sessions.js:3410`
- `static/js/sessions.js:3427`
- `static/js/sessions.js:3480`
- `static/js/sessions.js:3481`
- `static/js/sessions.js:3510`
- `static/js/slashCommands.js:1013`
- `static/js/slashCommands.js:1038`
- `static/js/slashCommands.js:1055`
- `static/js/slashCommands.js:1070`
- `static/js/slashCommands.js:1080`
- `static/js/slashCommands.js:1113`
- `static/js/slashCommands.js:1166`
- `static/js/startupShell.js:142`
- `static/js/tasks.js:2587`

## `_isTransient` — arrow, line 1809
- **called from:**
- `static/js/sessions.js:1810`
- `static/js/sessions.js:1826`

## `selectSession` — function, line 1928
- **called from:**
- `static/app.js:360`
- `static/app.js:3421`
- `static/app.js:3789`
- `static/app.js:4422`
- `static/js/assistant.js:5`
- `static/js/assistant.js:30`
- `static/js/chat.js:277`
- `static/js/chat.js:427`
- `static/js/chat.js:787`
- `static/js/chat.js:3643`
- `static/js/chat.js:5051`
- `static/js/chat.js:5421`
- `static/js/chat.js:5929`
- `static/js/chat.js:6012`
- `static/js/chat.js:6436`
- `static/js/chat.js:7022`
- `static/js/chatRenderer.js:1266`
- `static/js/chatRenderer.js:2246`
- `static/js/chatStream.js:265`
- `static/js/chatStream.js:291`
- `static/js/chatStream.js:313`
- `static/js/documentLibrary.js:1009`
- `static/js/documentLibrary.js:1022`
- `static/js/documentLibrary.js:2054`
- `static/js/documentLibrary.js:2180`
- `static/js/documentLibrary.js:2535`
- `static/js/documentLibrary.js:3006`
- `static/js/emailInbox.js:1380`
- `static/js/gallery.js:1529`
- `static/js/group.js:693`
- `static/js/keyboard-shortcuts.js:210`
- `static/js/keyboard-shortcuts.js:241`
- `static/js/notes.js:4461`
- `static/js/presets.js:434`
- `static/js/research/panel.js:1231`
- `static/js/search-chat.js:136`
- `static/js/sessions.js:719`
- `static/js/sessions.js:1885`
- `static/js/sessions.js:1928`
- `static/js/sessions.js:2575`
- `static/js/sessions.js:2604`
- `static/js/sessions.js:2652`
- `static/js/sessions.js:2873`
- `static/js/sessions.js:2879`
- `static/js/sessions.js:3474`
- `static/js/sessions.js:3479`
- `static/js/sessions.js:3541`
- `static/js/sessions.js:3548`
- `static/js/slashCommands.js:1014`
- `static/js/slashCommands.js:1114`
- `static/js/slashCommands.js:1155`
- `static/js/slashCommands.js:2076`
- `static/js/tasks.js:2588`

## `_getPreferredDefaultChat` — function, line 2280
- **called from:**
- `static/js/sessions.js:1908`
- `static/js/sessions.js:2280`

## `createDirectChat` — function, line 2305
- **called from:**
- `static/app.js:245`
- `static/app.js:253`
- `static/app.js:259`
- `static/app.js:266`
- `static/app.js:4061`
- `static/js/chat.js:1794`
- `static/js/cookbookRunning.js:568`
- `static/js/cookbookRunning.js:3688`
- `static/js/documentLibrary.js:1061`
- `static/js/gallery.js:1544`
- `static/js/modelPicker.js:694`
- `static/js/models.js:84`
- `static/js/sessions.js:1910`
- `static/js/sessions.js:2305`
- `static/js/slashCommands.js:709`

## `materializePendingSession` — function, line 2380
- **called from:**
- `static/app.js:610`
- `static/app.js:2014`
- `static/js/chat.js:1749`
- `static/js/chat.js:1760`
- `static/js/chat.js:1796`
- `static/js/document.js:7291`
- `static/js/documentLibrary.js:1050`
- `static/js/documentLibrary.js:1062`
- `static/js/sessions.js:2380`
- `static/js/sessions.js:2475`

## `materializePromise` — arrow, line 2385
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `preMaterializePendingSession` — function, line 2467
- **called from:**
- `static/js/sessions.js:2467`

## `hasPendingChat` — function, line 2480
- **called from:**
- `static/app.js:586`
- `static/app.js:2013`
- `static/js/chat.js:416`
- `static/js/chat.js:1747`
- `static/js/document.js:7290`
- `static/js/documentLibrary.js:1049`
- `static/js/sessions.js:2480`

## `getPendingChat` — function, line 2481
- **called from:**
- `static/app.js:243`
- `static/js/admin.js:427`
- `static/js/chat.js:488`
- `static/js/chat.js:1726`
- `static/js/chat.js:1758`
- `static/js/modelPicker.js:130`
- `static/js/modelPicker.js:147`
- `static/js/modelPicker.js:173`
- `static/js/modelPicker.js:665`
- `static/js/modelPicker.js:736`
- `static/js/modelPicker.js:874`
- `static/js/modelPicker.js:938`
- `static/js/sessions.js:2481`

## `getCurrentSessionId` — function, line 2483
- **called from:**
- `static/app.js:250`
- `static/app.js:519`
- `static/app.js:545`
- `static/app.js:583`
- `static/app.js:610`
- `static/app.js:837`
- `static/app.js:1650`
- `static/app.js:1662`
- `static/app.js:2011`
- `static/app.js:2015`
- `static/app.js:2565`
- `static/app.js:3406`
- `static/app.js:3741`
- `static/app.js:4058`
- `static/app.js:4420`
- `static/js/chat.js:267`
- `static/js/chat.js:292`
- `static/js/chat.js:308`
- `static/js/chat.js:368`
- `static/js/chat.js:401`
- `static/js/chat.js:431`
- `static/js/chat.js:692`
- `static/js/chat.js:1000`
- `static/js/chat.js:1482`
- `static/js/chat.js:1506`
- `static/js/chat.js:1607`
- `static/js/chat.js:1751`
- `static/js/chat.js:1754`
- `static/js/chat.js:1761`
- `static/js/chat.js:1766`
- `static/js/chat.js:1798`
- `static/js/chat.js:1850`
- `static/js/chat.js:1958`
- `static/js/chat.js:2050`
- `static/js/chat.js:3170`
- `static/js/chat.js:3535`
- `static/js/chat.js:3612`
- `static/js/chat.js:3642`
- `static/js/chat.js:4487`
- `static/js/chat.js:4489`
- `static/js/chat.js:4802`
- `static/js/chat.js:4837`
- `static/js/chat.js:5010`
- `static/js/chat.js:5050`
- `static/js/chat.js:5140`
- `static/js/chat.js:5198`
- `static/js/chat.js:5238`
- `static/js/chat.js:5240`
- `static/js/chat.js:5290`
- `static/js/chat.js:5342`
- `static/js/chat.js:5344`
- `static/js/chat.js:5395`
- `static/js/chat.js:5466`
- `static/js/chat.js:5645`
- `static/js/chat.js:5679`
- `static/js/chat.js:5747`
- `static/js/chat.js:5894`
- `static/js/chat.js:5993`
- `static/js/chat.js:6011`
- `static/js/chat.js:6139`
- … +65 more (grep the name in repo)

## `isCurrentSessionIncognito` — function, line 2487
- **called from:**
- `static/js/sessions.js:2487`

## `getSessions` — function, line 2491
- **called from:**
- `static/app.js:249`
- `static/app.js:519`
- `static/app.js:547`
- `static/app.js:588`
- `static/app.js:616`
- `static/app.js:1662`
- `static/app.js:3408`
- `static/app.js:4057`
- `static/js/chat.js:701`
- `static/js/chat.js:1483`
- `static/js/chat.js:2631`
- `static/js/chat.js:4338`
- `static/js/chat.js:4489`
- `static/js/chat.js:5614`
- `static/js/chat.js:5977`
- `static/js/chat.js:7071`
- `static/js/chat.js:7109`
- `static/js/chatStream.js:278`
- `static/js/document.js:7297`
- `static/js/documentLibrary.js:1056`
- `static/js/group.js:141`
- `static/js/keyboard-shortcuts.js:183`
- `static/js/keyboard-shortcuts.js:198`
- `static/js/keyboard-shortcuts.js:203`
- `static/js/keyboard-shortcuts.js:227`
- `static/js/modelPicker.js:702`
- `static/js/modelPicker.js:734`
- `static/js/modelPicker.js:873`
- `static/js/presets.js:404`
- `static/js/sessions.js:2491`
- `static/js/slashCommands.js:950`
- `static/js/slashCommands.js:958`
- `static/js/slashCommands.js:1029`
- `static/js/slashCommands.js:1049`
- `static/js/slashCommands.js:1065`
- `static/js/slashCommands.js:1135`
- `static/js/slashCommands.js:1150`
- `static/js/slashCommands.js:1180`
- `static/js/slashCommands.js:1227`
- `static/js/slashCommands.js:2016`

## `getCurrentModel` — function, line 2495
- **called from:**
- `static/js/chat.js:484`
- `static/js/chat.js:1736`
- `static/js/chat.js:6112`
- `static/js/cookbookRunning.js:556`
- `static/js/document.js:4252`
- `static/js/document.js:7296`
- `static/js/documentLibrary.js:1055`
- `static/js/emailInbox.js:839`
- `static/js/sessions.js:2495`
- `static/js/skills.js:1218`
- `static/js/slashCommands.js:1538`

## `getCurrentEndpointUrl` — function, line 2504
- **called from:**
- `static/js/chat.js:1737`
- `static/js/chat.js:6113`
- `static/js/chatRenderer.js:754`
- `static/js/chatRenderer.js:865`
- `static/js/sessions.js:2504`
- `static/js/skills.js:1219`
- `static/js/slashCommands.js:1539`
- `static/js/slashCommands.js:2030`

## `setCurrentSessionId` — function, line 2511
- **called from:**
- `static/app.js:843`
- `static/app.js:2619`
- `static/js/chat.js:429`
- `static/js/document.js:7314`
- `static/js/group.js:163`
- `static/js/group.js:691`
- `static/js/keyboard-shortcuts.js:212`
- `static/js/sessions.js:2511`

## `deleteCurrentSessionFromTopMenu` — function, line 2525
- **called from:**
- `static/app.js:572`
- `static/js/sessions.js:2525`

## `_onSessionListKeydown` — function, line 2561
- **called from:**
- `static/js/sessions.js:2561`

## `initDragSort` — function, line 2610
- **called from:**
- `static/js/sessions.js:1524`
- `static/js/sessions.js:2610`

## `_updateResearchDots` — function, line 2657
- **called from:**
- `static/js/sessions.js:2657`
- `static/js/sessions.js:2695`
- `static/js/sessions.js:2705`
- `static/js/sessions.js:2712`
- `static/js/sessions.js:2718`
- `static/js/sessions.js:2724`
- `static/js/sessions.js:2734`
- `static/js/sessions.js:2744`
- `static/js/sessions.js:2749`
- `static/js/sessions.js:2760`
- `static/js/sessions.js:2894`

## `_startResearchPolling` — function, line 2675
- **called from:**
- `static/js/sessions.js:2675`
- `static/js/sessions.js:2707`

## `markResearching` — function, line 2703
- **called from:**
- `static/js/chat.js:3536`
- `static/js/chat.js:7143`
- `static/js/sessions.js:2703`

## `clearResearching` — function, line 2710
- **called from:**
- `static/js/chat.js:3606`
- `static/js/chat.js:3613`
- `static/js/chat.js:3634`
- `static/js/chat.js:7040`
- `static/js/chat.js:7048`
- `static/js/chat.js:7205`
- `static/js/chat.js:7221`
- `static/js/sessions.js:2710`

## `markStreaming` — function, line 2716
- **called from:**
- `static/js/chat.js:3188`
- `static/js/chat.js:5522`
- `static/js/sessions.js:2716`

## `clearStreaming` — function, line 2722
- **called from:**
- `static/js/chat.js:4851`
- `static/js/chat.js:4879`
- `static/js/chat.js:4884`
- `static/js/chat.js:5524`
- `static/js/sessions.js:2722`

## `_clearRunningState` — function, line 2728
- **called from:**
- `static/js/sessions.js:2728`
- `static/js/sessions.js:2810`
- `static/js/sessions.js:2815`

## `markStreamComplete` — function, line 2739
- **called from:**
- `static/js/chat.js:3213`
- `static/js/notes.js:4531`
- `static/js/notes.js:4601`
- `static/js/sessions.js:2739`

## `setTimeout` — method?, line 2758
- **called from:**
- `static/app.js:288`
- `static/app.js:810`
- `static/app.js:1194`
- `static/app.js:1195`
- `static/app.js:1230`
- `static/app.js:1231`
- `static/app.js:1851`
- `static/app.js:2110`
- `static/app.js:2114`
- `static/app.js:2196`
- `static/app.js:2970`
- `static/app.js:3318`
- `static/app.js:3462`
- `static/app.js:3663`
- `static/app.js:3710`
- `static/app.js:3875`
- `static/app.js:4005`
- `static/app.js:4163`
- `static/app.js:4344`
- `static/app.js:4349`
- `static/app.js:4415`
- `static/app.js:4497`
- `static/js/admin.js:475`
- `static/js/admin.js:599`
- `static/js/admin.js:1232`
- `static/js/admin.js:1429`
- `static/js/admin.js:2262`
- `static/js/admin.js:2461`
- `static/js/admin.js:2629`
- `static/js/admin.js:2674`
- `static/js/admin.js:2719`
- `static/js/admin.js:2812`
- `static/js/admin.js:2829`
- `static/js/assistant.js:396`
- `static/js/calendar.js:45`
- `static/js/calendar.js:496`
- `static/js/calendar.js:824`
- `static/js/calendar.js:865`
- `static/js/calendar.js:869`
- `static/js/calendar.js:2021`
- `static/js/calendar.js:2027`
- `static/js/calendar.js:2216`
- `static/js/calendar.js:2230`
- `static/js/calendar.js:2245`
- `static/js/calendar.js:2247`
- `static/js/calendar.js:2632`
- `static/js/calendar.js:2655`
- `static/js/calendar.js:3127`
- `static/js/censor.js:120`
- `static/js/censor.js:122`
- `static/js/chat.js:73`
- `static/js/chat.js:243`
- `static/js/chat.js:518`
- `static/js/chat.js:795`
- `static/js/chat.js:808`
- `static/js/chat.js:1199`
- `static/js/chat.js:1230`
- `static/js/chat.js:1259`
- `static/js/chat.js:1388`
- `static/js/chat.js:1401`
- … +541 more (grep the name in repo)

## `_updateRailNotifs` — function, line 2767
- **called from:**
- `static/js/research/panel.js:119`
- `static/js/sessions.js:2706`
- `static/js/sessions.js:2713`
- `static/js/sessions.js:2719`
- `static/js/sessions.js:2725`
- `static/js/sessions.js:2735`
- `static/js/sessions.js:2745`
- `static/js/sessions.js:2750`
- `static/js/sessions.js:2767`
- `static/js/sessions.js:2895`

## `_checkServerStream` — function, line 2800
- **called from:**
- `static/js/sessions.js:2218`
- `static/js/sessions.js:2800`

## `clearStreamComplete` — function, line 2887
- **called from:**
- `static/js/chat.js:1958`
- `static/js/sessions.js:2207`
- `static/js/sessions.js:2887`

## `_initAllDropdowns` — function, line 2899
- **called from:**
- `static/js/sessions.js:2899`
- `static/js/sessions.js:2913`

## `_initDropdownDismiss` — function, line 2917
- **called from:**
- `static/js/sessions.js:2907`
- `static/js/sessions.js:2917`

## `_showDropdown` — function, line 2952
- **called from:**
- `static/js/sessions.js:2952`
- `static/js/sessions.js:3245`
- `static/js/sessions.js:3478`
- `static/js/sessions.js:3509`
- `static/js/sessions.js:3547`
- `static/js/sessions.js:3594`

## `close` — function, line 2983
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

## `_arcRelativeTime` — function, line 2996
- **called from:**
- `static/js/sessions.js:2996`
- `static/js/sessions.js:3225`
- `static/js/sessions.js:3625`

## `_arcPeekOpen` — function, line 3013
- **called from:**
- `static/js/sessions.js:3013`
- `static/js/sessions.js:3246`
- `static/js/sessions.js:3260`

## `_checkPeekCleanup` — function, line 3053
- **called from:**
- `static/js/sessions.js:1950`
- `static/js/sessions.js:3053`

## `_arcRestore` — function, line 3059
- **called from:**
- `static/js/sessions.js:3059`
- `static/js/sessions.js:3247`

## `_arcDelete` — function, line 3070
- **called from:**
- `static/js/sessions.js:3070`
- `static/js/sessions.js:3248`

## `_arcRemove` — function, line 3082
- **called from:**
- `static/js/sessions.js:3063`
- `static/js/sessions.js:3076`
- `static/js/sessions.js:3082`
- `static/js/sessions.js:3094`
- `static/js/sessions.js:3114`

## `_arcBulkRestore` — function, line 3088
- **called from:**
- `static/js/sessions.js:3088`

## `_arcBulkDelete` — function, line 3103
- **called from:**
- `static/js/sessions.js:3103`

## `_arcToggleSelectMode` — function, line 3124
- **called from:**
- `static/js/sessions.js:3124`

## `_arcUpdateBulkBar` — function, line 3130
- **called from:**
- `static/js/sessions.js:3130`
- `static/js/sessions.js:3177`
- `static/js/sessions.js:3240`
- `static/js/sessions.js:3258`

## `_arcFetch` — function, line 3144
- **called from:**
- `static/js/sessions.js:3144`
- `static/js/sessions.js:3199`
- `static/js/sessions.js:3709`
- `static/js/sessions.js:3712`
- `static/js/sessions.js:3714`
- `static/js/sessions.js:3725`

## `_arcRefreshUI` — function, line 3172
- **called from:**
- `static/js/sessions.js:3064`
- `static/js/sessions.js:3077`
- `static/js/sessions.js:3098`
- `static/js/sessions.js:3120`
- `static/js/sessions.js:3127`
- `static/js/sessions.js:3164`
- `static/js/sessions.js:3172`
- `static/js/sessions.js:3721`

## `_arcRenderStats` — function, line 3180
- **called from:**
- `static/js/sessions.js:3173`
- `static/js/sessions.js:3180`

## `_arcRenderChips` — function, line 3185
- **called from:**
- `static/js/sessions.js:3174`
- `static/js/sessions.js:3185`

## `mkChip` — arrow, line 3195
- **called from:**
- `static/js/sessions.js:3202`
- `static/js/sessions.js:3203`
- `static/js/tasks.js:784`
- `static/js/tasks.js:785`

## `_arcRenderCard` — function, line 3206
- **called from:**
- `static/js/sessions.js:3206`
- `static/js/sessions.js:3274`

## `_arcRenderGrid` — function, line 3266
- **called from:**
- `static/js/sessions.js:3175`
- `static/js/sessions.js:3266`

## `_arcRenderLoadMore` — function, line 3277
- **called from:**
- `static/js/sessions.js:3176`
- `static/js/sessions.js:3277`

## `openLibrary` — function, line 3288
- **called from:**
- `static/app.js:1049`
- `static/app.js:1236`
- `static/app.js:1251`
- `static/app.js:1277`
- `static/app.js:1284`
- `static/js/document.js:5198`
- `static/js/document.js:9554`
- `static/js/document.js:9658`
- `static/js/documentLibrary.js:1575`
- `static/js/research/panel.js:686`
- `static/js/research/panel.js:734`
- `static/js/research/panel.js:794`
- `static/js/sessions.js:3288`
- `static/js/sessions.js:3291`
- `static/js/sessions.js:3350`
- `static/js/slashCommands.js:4602`

## `_updateLibCount` — function, line 3434
- **called from:**
- `static/js/sessions.js:3395`
- `static/js/sessions.js:3434`
- `static/js/sessions.js:3639`
- `static/js/sessions.js:3646`

## `_renderLibGrid` — function, line 3439
- **called from:**
- `static/js/sessions.js:3367`
- `static/js/sessions.js:3375`
- `static/js/sessions.js:3378`
- `static/js/sessions.js:3386`
- `static/js/sessions.js:3411`
- `static/js/sessions.js:3428`
- `static/js/sessions.js:3431`
- `static/js/sessions.js:3439`
- `static/js/sessions.js:3480`
- `static/js/sessions.js:3481`
- `static/js/sessions.js:3510`
- `static/js/sessions.js:3511`
- `static/js/sessions.js:3549`
- `static/js/sessions.js:3606`

## `_renderLibChats` — function, line 3449
- **called from:**
- `static/js/documentLibrary.js:1913`
- `static/js/documentLibrary.js:1931`
- `static/js/documentLibrary.js:2075`
- `static/js/documentLibrary.js:2113`
- `static/js/documentLibrary.js:2182`
- `static/js/documentLibrary.js:2189`
- `static/js/documentLibrary.js:2285`
- `static/js/documentLibrary.js:2330`
- `static/js/documentLibrary.js:2357`
- `static/js/sessions.js:3443`
- `static/js/sessions.js:3449`

## `_renderLibArchive` — function, line 3488
- **called from:**
- `static/js/documentLibrary.js:1914`
- `static/js/documentLibrary.js:2088`
- `static/js/documentLibrary.js:2113`
- `static/js/documentLibrary.js:2381`
- `static/js/documentLibrary.js:2452`
- `static/js/documentLibrary.js:2457`
- `static/js/documentLibrary.js:2537`
- `static/js/documentLibrary.js:2541`
- `static/js/documentLibrary.js:2584`
- `static/js/documentLibrary.js:2585`
- `static/js/documentLibrary.js:2622`
- `static/js/documentLibrary.js:2623`
- `static/js/documentLibrary.js:2707`
- `static/js/documentLibrary.js:2728`
- `static/js/documentLibrary.js:3037`
- `static/js/documentLibrary.js:3056`
- `static/js/sessions.js:3444`
- `static/js/sessions.js:3488`

## `_renderLibDocuments` — function, line 3519
- **called from:**
- `static/js/sessions.js:3445`
- `static/js/sessions.js:3519`

## `_renderLibResearch` — function, line 3557
- **called from:**
- `static/js/documentLibrary.js:1915`
- `static/js/documentLibrary.js:2893`
- `static/js/documentLibrary.js:3291`
- `static/js/sessions.js:3446`
- `static/js/sessions.js:3557`

## `_buildLibCard` — function, line 3616
- **called from:**
- `static/js/sessions.js:3470`
- `static/js/sessions.js:3502`
- `static/js/sessions.js:3533`
- `static/js/sessions.js:3579`
- `static/js/sessions.js:3616`

## `_toggleLibSelect` — function, line 3644
- **called from:**
- `static/js/sessions.js:3473`
- `static/js/sessions.js:3505`
- `static/js/sessions.js:3537`
- `static/js/sessions.js:3644`

## `closeLibrary` — function, line 3649
- **called from:**
- `static/app.js:1047`
- `static/js/documentLibrary.js:1001`
- `static/js/documentLibrary.js:1017`
- `static/js/documentLibrary.js:1107`
- `static/js/documentLibrary.js:2055`
- `static/js/documentLibrary.js:3008`
- `static/js/documentLibrary.js:3452`
- `static/js/documentLibrary.js:3581`
- `static/js/documentLibrary.js:3592`
- `static/js/documentLibrary.js:3606`
- `static/js/sessions.js:3349`
- `static/js/sessions.js:3474`
- `static/js/sessions.js:3479`
- `static/js/sessions.js:3540`
- `static/js/sessions.js:3548`
- `static/js/sessions.js:3649`

## `openArchive` — function, line 3663
- **called from:**
- `static/js/sessions.js:2993`
- `static/js/sessions.js:3663`

## `closeArchive` — function, line 3728
- **called from:**
- `static/js/sessions.js:3016`
- `static/js/sessions.js:3723`
- `static/js/sessions.js:3728`

## `getSortMode` — function, line 3743
- **called from:**
- `static/app.js:1391`
- `static/app.js:1408`
- `static/js/sessions.js:3743`

## `setSortMode` — function, line 3744
- **called from:**
- `static/app.js:1394`
- `static/app.js:1398`
- `static/app.js:1441`
- `static/js/sessions.js:470`
- `static/js/sessions.js:494`
- `static/js/sessions.js:3744`

## `setSessionHasDocs` — function, line 3751
- **called from:**
- `static/js/document.js:201`
- `static/js/sessions.js:3751`
