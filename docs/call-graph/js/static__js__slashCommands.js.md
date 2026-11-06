# `static/js/slashCommands.js` — definitions & call sites

255 definitions (regex-based, best-effort).
**Exports:** `COMMANDS`, `LEGACY_ALIASES`, `clearSetupMode`, `default`, `getSetupMode`, `handleSetupInput`, `handleSetupWizard`, `handleSlashCommand`, `initSlashCommands`, `isCommand`, `slashReply`, `typewriterInto`, `typewriterReply`

## `cancelActiveTour` — function, line 4
- **called from:**
- `static/js/slashCommands.js:4`

## `_isStreamingFn` — arrow, line 38
- **called from:**
- `static/js/slashCommands.js:2542`
- `static/js/slashCommands.js:2546`

## `_setupApiProviderChips` — function, line 75
- **called from:**
- `static/js/slashCommands.js:75`
- `static/js/slashCommands.js:199`
- `static/js/slashCommands.js:257`

## `_setupDeviceAuthProviderChips` — function, line 81
- **called from:**
- `static/js/slashCommands.js:81`
- `static/js/slashCommands.js:200`
- `static/js/slashCommands.js:258`

## `_setupProviderFromInput` — function, line 87
- **called from:**
- `static/js/slashCommands.js:87`
- `static/js/slashCommands.js:794`
- `static/js/slashCommands.js:852`
- `static/js/slashCommands.js:5108`

## `_setupDeviceAuthProviderFromInput` — function, line 111
- **called from:**
- `static/js/slashCommands.js:111`
- `static/js/slashCommands.js:786`
- `static/js/slashCommands.js:5103`

## `_extractSetupProviderCredential` — function, line 122
- **called from:**
- `static/js/slashCommands.js:122`
- `static/js/slashCommands.js:737`
- `static/js/slashCommands.js:793`
- `static/js/slashCommands.js:821`
- `static/js/slashCommands.js:837`

## `_normalizeSetupBaseUrl` — function, line 149
- **called from:**
- `static/js/slashCommands.js:149`
- `static/js/slashCommands.js:5133`

## `_clearSetupGuideMessages` — function, line 167
- **called from:**
- `static/js/slashCommands.js:167`
- `static/js/slashCommands.js:712`
- `static/js/slashCommands.js:5043`
- `static/js/slashCommands.js:5110`
- `static/js/slashCommands.js:5130`
- `static/js/slashCommands.js:5148`
- `static/js/slashCommands.js:5153`
- `static/js/slashCommands.js:5216`

## `_showSetupRetryPrompt` — function, line 171
- **called from:**
- `static/js/slashCommands.js:171`

## `_showSetupUserBubble` — function, line 176
- **called from:**
- `static/js/slashCommands.js:176`
- `static/js/slashCommands.js:735`
- `static/js/slashCommands.js:782`
- `static/js/slashCommands.js:802`
- `static/js/slashCommands.js:820`

## `_setupReply` — function, line 194
- **called from:**
- `static/js/slashCommands.js:194`
- `static/js/slashCommands.js:748`
- `static/js/slashCommands.js:798`
- `static/js/slashCommands.js:809`
- `static/js/slashCommands.js:817`
- `static/js/slashCommands.js:5046`
- `static/js/slashCommands.js:5054`
- `static/js/slashCommands.js:5071`
- `static/js/slashCommands.js:5081`
- `static/js/slashCommands.js:5086`
- `static/js/slashCommands.js:5090`
- `static/js/slashCommands.js:5094`
- `static/js/slashCommands.js:5123`
- `static/js/slashCommands.js:5137`

## `_showSetupEndpointChoices` — function, line 198
- **called from:**
- `static/js/slashCommands.js:172`
- `static/js/slashCommands.js:198`
- `static/js/slashCommands.js:5021`

## `_showSetupEndpointChoicesStreamed` — function, line 226
- **called from:**
- `static/js/slashCommands.js:226`
- `static/js/slashCommands.js:5026`

## `_hasConfiguredModels` — function, line 263
- **called from:**
- `static/js/slashCommands.js:263`
- `static/js/slashCommands.js:2119`

## `_setupProviderPrompt` — function, line 278
- **called from:**
- `static/js/slashCommands.js:278`
- `static/js/slashCommands.js:762`
- `static/js/slashCommands.js:783`

## `_persistMsg` — function, line 291
- **called from:**
- `static/js/slashCommands.js:291`
- `static/js/slashCommands.js:337`
- `static/js/slashCommands.js:460`
- `static/js/slashCommands.js:565`
- `static/js/slashCommands.js:6321`

## `slashReply` — function, line 309
- **called from:**
- `static/js/slashCommands.js:201`
- `static/js/slashCommands.js:282`
- `static/js/slashCommands.js:309`
- `static/js/slashCommands.js:381`
- `static/js/slashCommands.js:386`
- `static/js/slashCommands.js:881`
- `static/js/slashCommands.js:1000`
- `static/js/slashCommands.js:1018`
- `static/js/slashCommands.js:1032`
- `static/js/slashCommands.js:1042`
- `static/js/slashCommands.js:1048`
- `static/js/slashCommands.js:1057`
- `static/js/slashCommands.js:1058`
- `static/js/slashCommands.js:1064`
- `static/js/slashCommands.js:1071`
- `static/js/slashCommands.js:1077`
- `static/js/slashCommands.js:1081`
- `static/js/slashCommands.js:1100`
- `static/js/slashCommands.js:1116`
- `static/js/slashCommands.js:1121`
- `static/js/slashCommands.js:1123`
- `static/js/slashCommands.js:1130`
- `static/js/slashCommands.js:1137`
- `static/js/slashCommands.js:1143`
- `static/js/slashCommands.js:1149`
- `static/js/slashCommands.js:1162`
- `static/js/slashCommands.js:1174`
- `static/js/slashCommands.js:1179`
- `static/js/slashCommands.js:1182`
- `static/js/slashCommands.js:1183`
- `static/js/slashCommands.js:1194`
- `static/js/slashCommands.js:1199`
- `static/js/slashCommands.js:1216`
- `static/js/slashCommands.js:1230`
- `static/js/slashCommands.js:1244`
- `static/js/slashCommands.js:1254`
- `static/js/slashCommands.js:1256`
- `static/js/slashCommands.js:1267`
- `static/js/slashCommands.js:1271`
- `static/js/slashCommands.js:1276`
- `static/js/slashCommands.js:1277`
- `static/js/slashCommands.js:1286`
- `static/js/slashCommands.js:1306`
- `static/js/slashCommands.js:1316`
- `static/js/slashCommands.js:1355`
- `static/js/slashCommands.js:1397`
- `static/js/slashCommands.js:1423`
- `static/js/slashCommands.js:1437`
- `static/js/slashCommands.js:1462`
- `static/js/slashCommands.js:1478`
- `static/js/slashCommands.js:1483`
- `static/js/slashCommands.js:1492`
- `static/js/slashCommands.js:1495`
- `static/js/slashCommands.js:1508`
- `static/js/slashCommands.js:1526`
- `static/js/slashCommands.js:1534`
- `static/js/slashCommands.js:1544`
- `static/js/slashCommands.js:1556`
- `static/js/slashCommands.js:1561`
- `static/js/slashCommands.js:1570`
- … +92 more (grep the name in repo)

## `_loadSkillSlashCatalog` — function, line 343
- **called from:**
- `static/js/slashCommands.js:343`
- `static/js/slashCommands.js:1659`
- `static/js/slashCommands.js:1714`
- `static/js/slashCommands.js:5767`
- `static/js/slashCommands.js:6421`

## `_submitComposedMessage` — function, line 358
- **called from:**
- `static/js/slashCommands.js:358`
- `static/js/slashCommands.js:385`

## `_invokeSkillByName` — function, line 372
- **called from:**
- `static/js/slashCommands.js:372`
- `static/js/slashCommands.js:1706`
- `static/js/slashCommands.js:6424`

## `_slashFooter` — function, line 392
- **called from:**
- `static/js/slashCommands.js:334`
- `static/js/slashCommands.js:392`
- `static/js/slashCommands.js:459`
- `static/js/slashCommands.js:564`

## `typewriterReply` — function, line 428
- **called from:**
- `static/js/slashCommands.js:195`
- `static/js/slashCommands.js:428`
- `static/js/slashCommands.js:696`
- `static/js/slashCommands.js:704`
- `static/js/slashCommands.js:711`
- `static/js/slashCommands.js:719`
- `static/js/slashCommands.js:725`
- `static/js/slashCommands.js:756`
- `static/js/slashCommands.js:841`
- `static/js/slashCommands.js:849`
- `static/js/slashCommands.js:859`
- `static/js/slashCommands.js:876`
- `static/js/slashCommands.js:879`
- `static/js/slashCommands.js:898`
- `static/js/slashCommands.js:900`
- `static/js/slashCommands.js:902`
- `static/js/slashCommands.js:906`
- `static/js/slashCommands.js:928`
- `static/js/slashCommands.js:940`
- `static/js/slashCommands.js:1017`
- `static/js/slashCommands.js:1054`
- `static/js/slashCommands.js:1068`
- `static/js/slashCommands.js:1070`
- `static/js/slashCommands.js:1080`
- `static/js/slashCommands.js:1088`
- `static/js/slashCommands.js:1095`
- `static/js/slashCommands.js:1115`
- `static/js/slashCommands.js:1129`
- `static/js/slashCommands.js:1156`
- `static/js/slashCommands.js:1157`
- `static/js/slashCommands.js:1169`
- `static/js/slashCommands.js:1172`
- `static/js/slashCommands.js:1346`
- `static/js/slashCommands.js:1488`
- `static/js/slashCommands.js:1497`
- `static/js/slashCommands.js:1501`
- `static/js/slashCommands.js:1519`
- `static/js/slashCommands.js:1595`
- `static/js/slashCommands.js:1619`
- `static/js/slashCommands.js:1634`
- `static/js/slashCommands.js:1646`
- `static/js/slashCommands.js:1729`
- `static/js/slashCommands.js:1835`
- `static/js/slashCommands.js:1859`
- `static/js/slashCommands.js:1921`
- `static/js/slashCommands.js:1947`
- `static/js/slashCommands.js:1956`
- `static/js/slashCommands.js:2121`
- `static/js/slashCommands.js:2484`
- `static/js/slashCommands.js:2553`
- `static/js/slashCommands.js:2836`
- `static/js/slashCommands.js:3062`
- `static/js/slashCommands.js:3308`
- `static/js/slashCommands.js:3540`
- `static/js/slashCommands.js:3755`
- `static/js/slashCommands.js:3958`
- `static/js/slashCommands.js:4159`
- `static/js/slashCommands.js:4361`
- `static/js/slashCommands.js:4599`
- `static/js/slashCommands.js:4842`
- … +10 more (grep the name in repo)

## `typewriterBlocksReply` — function, line 467
- **called from:**
- `static/js/slashCommands.js:260`
- `static/js/slashCommands.js:467`

## `makeBlock` — function, line 491
- **called from:**
- `static/js/slashCommands.js:491`
- `static/js/slashCommands.js:569`

## `useNow` — arrow, line 508
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `copyNow` — arrow, line 535
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `appendContainer` — function, line 552
- **called from:**
- `static/js/slashCommands.js:552`
- `static/js/slashCommands.js:572`

## `typewriterInto` — function, line 593
- **called from:**
- `static/js/chat.js:3610`
- `static/js/chat.js:6718`
- `static/js/chat.js:6947`
- `static/js/slashCommands.js:593`

## `maskKey` — function, line 608
- **called from:**
- `static/js/slashCommands.js:177`
- `static/js/slashCommands.js:608`

## `detectProvider` — function, line 617
- **called from:**
- `static/js/slashCommands.js:617`
- `static/js/slashCommands.js:753`
- `static/js/slashCommands.js:774`

## `setupChatUrlForEndpoint` — function, line 652
- **called from:**
- `static/js/slashCommands.js:652`
- `static/js/slashCommands.js:707`

## `connectDetectedSetupEndpoint` — function, line 659
- **called from:**
- `static/js/slashCommands.js:659`
- `static/js/slashCommands.js:740`
- `static/js/slashCommands.js:766`
- `static/js/slashCommands.js:803`
- `static/js/slashCommands.js:823`
- `static/js/slashCommands.js:844`
- `static/js/slashCommands.js:862`
- `static/js/slashCommands.js:5113`
- `static/js/slashCommands.js:5134`

## `handleSetupInput` — function, line 732
- **called from:**
- `static/js/chat.js:2701`
- `static/js/slashCommands.js:732`
- `static/js/slashCommands.js:776`

## `handleSetupWizard` — function, line 772
- **called from:**
- `static/js/chat.js:2703`
- `static/js/slashCommands.js:772`

## `_syncToggleUI` — function, line 909
- **called from:**
- `static/js/slashCommands.js:909`
- `static/js/slashCommands.js:926`
- `static/js/slashCommands.js:938`

## `_quickToggle` — function, line 921
- **called from:**
- `static/js/slashCommands.js:921`
- `static/js/slashCommands.js:1222`
- `static/js/slashCommands.js:1223`
- `static/js/slashCommands.js:1224`
- `static/js/slashCommands.js:1225`
- `static/js/slashCommands.js:1234`

## `_applyToggle` — function, line 932
- **called from:**
- `static/js/slashCommands.js:932`
- `static/js/slashCommands.js:1222`
- `static/js/slashCommands.js:1223`
- `static/js/slashCommands.js:1224`
- `static/js/slashCommands.js:1225`
- `static/js/slashCommands.js:1234`
- `static/js/slashCommands.js:1309`

## `_resolveSession` — function, line 948
- **called from:**
- `static/js/slashCommands.js:948`
- `static/js/slashCommands.js:1047`
- `static/js/slashCommands.js:1063`

## `_cmdSessionNew` — function, line 956
- **called from:**
- `static/js/slashCommands.js:956`

## `_cmdSessionDelete` — function, line 1022
- **called from:**
- `static/js/slashCommands.js:1022`

## `_cmdSessionArchive` — function, line 1062
- **called from:**
- `static/js/slashCommands.js:1062`

## `_cmdSessionRename` — function, line 1075
- **called from:**
- `static/js/slashCommands.js:1075`

## `_cmdSessionImportant` — function, line 1085
- **called from:**
- `static/js/slashCommands.js:1085`

## `_cmdSessionUnimportant` — function, line 1092
- **called from:**
- `static/js/slashCommands.js:1092`

## `_cmdSessionFork` — function, line 1099
- **called from:**
- `static/js/slashCommands.js:1099`

## `_cmdSessionTruncate` — function, line 1120
- **called from:**
- `static/js/slashCommands.js:1120`

## `_cmdSessionList` — function, line 1134
- **called from:**
- `static/js/slashCommands.js:1134`

## `_cmdSessionSwitch` — function, line 1147
- **called from:**
- `static/js/slashCommands.js:1147`

## `_cmdSessionSort` — function, line 1161
- **called from:**
- `static/js/slashCommands.js:1161`

## `_cmdSessionInfo` — function, line 1178
- **called from:**
- `static/js/slashCommands.js:1178`

## `_cmdSessionClear` — function, line 1192
- **called from:**
- `static/js/slashCommands.js:1192`

## `_cmdSessionExport` — function, line 1198
- **called from:**
- `static/js/slashCommands.js:1198`

## `_cmdToggleWeb` — function, line 1222
- **called from:**
- `static/js/slashCommands.js:1222`

## `_cmdToggleBash` — function, line 1223
- **called from:**
- `static/js/slashCommands.js:1223`

## `_cmdToggleRag` — function, line 1224
- **called from:**
- `static/js/slashCommands.js:1224`

## `_cmdToggleResearch` — function, line 1225
- **called from:**
- `static/js/slashCommands.js:1225`

## `_cmdToggleIncognito` — function, line 1226
- **called from:**
- `static/js/slashCommands.js:1226`

## `_cmdToggleDoc` — function, line 1238
- **called from:**
- `static/js/slashCommands.js:1238`

## `_cmdWorkspace` — function, line 1262
- **called from:**
- `static/js/slashCommands.js:1262`

## `setWorkspace` — arrow, line 1270
- **called from:**
- `static/js/chat.js:5187`
- `static/js/slashCommands.js:1282`
- `static/js/slashCommands.js:1294`
- `static/js/workspace.js:61`
- `static/js/workspace.js:79`
- `static/js/workspace.js:95`
- `static/js/workspace.js:105`
- `static/js/workspace.js:198`

## `_cmdToggleShow` — function, line 1297
- **called from:**
- `static/js/slashCommands.js:1297`

## `_cmdToggleSidebar` — function, line 1313
- **called from:**
- `static/js/slashCommands.js:1313`

## `_cmdOpen` — function, line 1352
- **called from:**
- `static/js/slashCommands.js:1352`
- `static/js/slashCommands.js:1445`

## `clickFirst` — arrow, line 1358
- **called from:**
- `static/js/slashCommands.js:1368`
- `static/js/slashCommands.js:1373`
- `static/js/slashCommands.js:1393`

## `_cmdToolPanel` — function, line 1401
- **called from:**
- `static/js/slashCommands.js:1401`
- `static/js/slashCommands.js:6031`
- `static/js/slashCommands.js:6038`
- `static/js/slashCommands.js:6045`
- `static/js/slashCommands.js:6052`
- `static/js/slashCommands.js:6059`
- `static/js/slashCommands.js:6066`
- `static/js/slashCommands.js:6073`
- `static/js/slashCommands.js:6080`
- `static/js/slashCommands.js:6087`

## `_cmdSettings` — function, line 1448
- **called from:**
- `static/js/slashCommands.js:1448`

## `_cmdTheme` — function, line 1470
- **called from:**
- `static/js/slashCommands.js:1470`

## `_cmdModels` — function, line 1525
- **called from:**
- `static/js/slashCommands.js:1525`
- `static/js/slashCommands.js:1540`

## `_cmdModel` — function, line 1538
- **called from:**
- `static/js/slashCommands.js:1538`

## `_cmdMcp` — function, line 1553
- **called from:**
- `static/js/slashCommands.js:1553`

## `_cmdMemoryList` — function, line 1576
- **called from:**
- `static/js/slashCommands.js:1576`

## `_cmdMemoryAdd` — function, line 1587
- **called from:**
- `static/js/slashCommands.js:1587`

## `_cmdMemoryDelete` — function, line 1600
- **called from:**
- `static/js/slashCommands.js:1600`

## `_cmdMemorySearch` — function, line 1639
- **called from:**
- `static/js/slashCommands.js:1639`

## `_cmdSkills` — function, line 1654
- **called from:**
- `static/js/slashCommands.js:1654`

## `_cmdReloadSkills` — function, line 1713
- **called from:**
- `static/js/slashCommands.js:1713`

## `_cmdNote` — function, line 1721
- **called from:**
- `static/js/slashCommands.js:1721`

## `_pad2` — function, line 1739
- **called from:**
- `static/js/slashCommands.js:1739`
- `static/js/slashCommands.js:1743`
- `static/js/slashCommands.js:1743`
- `static/js/slashCommands.js:1743`
- `static/js/slashCommands.js:1743`

## `_toLocalIso` — function, line 1742
- **called from:**
- `static/js/slashCommands.js:1742`
- `static/js/slashCommands.js:1849`
- `static/js/slashCommands.js:1850`

## `_parseTimeSpec` — function, line 1756
- **called from:**
- `static/js/slashCommands.js:1756`
- `static/js/slashCommands.js:1843`

## `_cmdTodo` — function, line 1815
- **called from:**
- `static/js/slashCommands.js:1815`

## `_cmdEvent` — function, line 1840
- **called from:**
- `static/js/slashCommands.js:1840`

## `_cmdShell` — function, line 1869
- **called from:**
- `static/js/slashCommands.js:1869`

## `_cmdRagList` — function, line 1894
- **called from:**
- `static/js/slashCommands.js:1894`

## `_cmdRagAdd` — function, line 1911
- **called from:**
- `static/js/slashCommands.js:1911`

## `_cmdRagRemove` — function, line 1926
- **called from:**
- `static/js/slashCommands.js:1926`

## `_cmdWebSearch` — function, line 1963
- **called from:**
- `static/js/slashCommands.js:1963`

## `_cmdSearch` — function, line 1977
- **called from:**
- `static/js/slashCommands.js:1977`

## `_cmdStats` — function, line 1998
- **called from:**
- `static/js/slashCommands.js:1998`

## `_cmdUsage` — function, line 2011
- **called from:**
- `static/js/slashCommands.js:2011`

## `_cmdCompact` — function, line 2060
- **called from:**
- `static/js/slashCommands.js:2060`

## `_cmdTts` — function, line 2094
- **called from:**
- `static/js/slashCommands.js:2094`

## `_cmdDemo` — function, line 2118
- **called from:**
- `static/js/slashCommands.js:2118`

## `_clearTour` — arrow, line 2135
- **called from:**
- `static/js/slashCommands.js:2536`
- `static/js/slashCommands.js:2552`

## `_restoreIfCleared` — arrow, line 2164
- **called from:**
- `static/js/slashCommands.js:2172`

## `positionTooltip` — function, line 2218
- **called from:**
- `static/js/slashCommands.js:2218`
- `static/js/slashCommands.js:2362`
- `static/js/slashCommands.js:4267`
- `static/js/slashCommands.js:4302`

## `streamHTML` — function, line 2273
- **called from:**
- `static/js/slashCommands.js:2273`
- `static/js/slashCommands.js:2366`

## `on` — class, line 2293
- **called from:**
- `tests/test_editor_layer_scoped_actions_browser.py:851`
- `static/js/chat.js:3092`
- `static/js/compare/index.js:1050`
- `static/js/cookbook-hwfit.js:2587`
- `static/js/editor/tools/eyedropper.js:12`
- `static/js/gallery.js:2869`
- `static/js/streamingSegmenter.js:15`
- `static/js/windowResize.js:245`

## `makeHalo` — function, line 2295
- **called from:**
- `static/js/slashCommands.js:2295`
- `static/js/slashCommands.js:4228`
- `static/js/slashCommands.js:4292`

## `update` — arrow, line 2299
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `destroy` — method?, line 2312
- **called from:**
- `static/app.js:1512`
- `static/js/admin.js:2381`
- `static/js/admin.js:2618`
- `static/js/backgroundToolJobs.js:6`
- `static/js/calendar.js:2640`
- `static/js/chat.js:1398`
- `static/js/chat.js:1617`
- `static/js/chat.js:1650`
- `static/js/chat.js:2559`
- `static/js/chat.js:2564`
- `static/js/chat.js:3818`
- `static/js/chat.js:4212`
- `static/js/chat.js:4214`
- `static/js/chat.js:4429`
- `static/js/chat.js:4711`
- `static/js/chat.js:4742`
- `static/js/chat.js:4775`
- `static/js/chat.js:4969`
- `static/js/chat.js:5510`
- `static/js/chat.js:5948`
- `static/js/chat.js:5990`
- `static/js/chat.js:6033`
- `static/js/chat.js:6068`
- `static/js/chat.js:6077`
- `static/js/chat.js:6492`
- `static/js/chat.js:7342`
- `static/js/chat.js:7399`
- `static/js/chat.js:7476`
- `static/js/chat.js:7493`
- `static/js/chat.js:8880`
- `static/js/chat.js:8894`
- `static/js/chat.js:8910`
- `static/js/chat.js:9197`
- `static/js/codeRunner.js:236`
- `static/js/compare/panes.js:407`
- `static/js/compare/stream.js:217`
- `static/js/compare/stream.js:541`
- `static/js/compare/stream.js:566`
- `static/js/compare/stream.js:607`
- `static/js/compare/stream.js:665`
- `static/js/compare/stream.js:693`
- `static/js/compare/stream.js:893`
- `static/js/cookbook-diagnosis.js:1020`
- `static/js/cookbook-hwfit.js:743`
- `static/js/cookbook-hwfit.js:792`
- `static/js/cookbook-hwfit.js:891`
- `static/js/cookbook-hwfit.js:905`
- `static/js/cookbook-hwfit.js:910`
- `static/js/cookbook-hwfit.js:937`
- `static/js/cookbook-hwfit.js:1022`
- `static/js/cookbook-hwfit.js:2344`
- `static/js/cookbookServe.js:2109`
- `static/js/cookbookServe.js:2884`
- `static/js/cookbookServe.js:4005`
- `static/js/cookbookServe.js:4329`
- `static/js/cookbookServe.js:4333`
- `static/js/cookbookServe.js:4340`
- `static/js/cookbookServe.js:4344`
- `static/js/cookbookServe.js:4370`
- `static/js/cookbookServe.js:4376`
- … +85 more (grep the name in repo)

## `showStep` — function, line 2320
- **called from:**
- `static/js/slashCommands.js:2320`
- `static/js/slashCommands.js:2535`
- `static/js/slashCommands.js:4284`
- `static/js/slashCommands.js:4322`

## `onClick` — arrow, line 2372
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `onDocClickCapture` — arrow, line 2386
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `onMessageInput` — arrow, line 2406
- **called from:**
- `static/js/slashCommands.js:2457`

## `_restore` — arrow, line 2419
- **called from:**
- `tests/test_fastembed_cache_path.py:49`
- `tests/test_fastembed_cache_path.py:58`
- `tests/test_fastembed_cache_path.py:69`
- `static/js/slashCommands.js:2427`

## `onModelPicked` — arrow, line 2433
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup` — arrow, line 2435
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `delay` — arrow, line 2481
- **called from:**
- `static/app.js:3977`
- `static/js/chat.js:6872`
- `static/js/emailLibrary/index.js:1568`
- `static/js/slashCommands.js:2486`
- `static/js/slashCommands.js:2540`
- `static/js/slashCommands.js:2548`

## `before` — method?, line 2520
- **called from:**
- `static/js/admin.js:566`
- `static/js/document.js:7742`
- `static/js/document.js:7750`
- `static/js/document.js:7751`
- `static/js/document.js:7752`
- `static/js/document.js:7753`
- `static/js/markdown.js:706`
- `static/js/slashCommands.js:2520`
- `static/js/slashCommands.js:2528`
- `static/js/slashCommands.js:2534`
- `static/js/slashCommands.js:2972`
- `static/js/slashCommands.js:3008`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4287`
- `static/js/slashCommands.js:4535`
- `static/js/slashCommands.js:4751`

## `before` — method?, line 2528
- **called from:**
- `static/js/admin.js:566`
- `static/js/document.js:7742`
- `static/js/document.js:7750`
- `static/js/document.js:7751`
- `static/js/document.js:7752`
- `static/js/document.js:7753`
- `static/js/markdown.js:706`
- `static/js/slashCommands.js:2520`
- `static/js/slashCommands.js:2528`
- `static/js/slashCommands.js:2534`
- `static/js/slashCommands.js:2972`
- `static/js/slashCommands.js:3008`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4287`
- `static/js/slashCommands.js:4535`
- `static/js/slashCommands.js:4751`

## `_cmdTourCompare` — function, line 2558
- **called from:**
- `static/js/slashCommands.js:2558`

## `_makeHalo` — function, line 2614
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 2618
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `destroy` — method?, line 2630
- **called from:**
- `static/app.js:1512`
- `static/js/admin.js:2381`
- `static/js/admin.js:2618`
- `static/js/backgroundToolJobs.js:6`
- `static/js/calendar.js:2640`
- `static/js/chat.js:1398`
- `static/js/chat.js:1617`
- `static/js/chat.js:1650`
- `static/js/chat.js:2559`
- `static/js/chat.js:2564`
- `static/js/chat.js:3818`
- `static/js/chat.js:4212`
- `static/js/chat.js:4214`
- `static/js/chat.js:4429`
- `static/js/chat.js:4711`
- `static/js/chat.js:4742`
- `static/js/chat.js:4775`
- `static/js/chat.js:4969`
- `static/js/chat.js:5510`
- `static/js/chat.js:5948`
- `static/js/chat.js:5990`
- `static/js/chat.js:6033`
- `static/js/chat.js:6068`
- `static/js/chat.js:6077`
- `static/js/chat.js:6492`
- `static/js/chat.js:7342`
- `static/js/chat.js:7399`
- `static/js/chat.js:7476`
- `static/js/chat.js:7493`
- `static/js/chat.js:8880`
- `static/js/chat.js:8894`
- `static/js/chat.js:8910`
- `static/js/chat.js:9197`
- `static/js/codeRunner.js:236`
- `static/js/compare/panes.js:407`
- `static/js/compare/stream.js:217`
- `static/js/compare/stream.js:541`
- `static/js/compare/stream.js:566`
- `static/js/compare/stream.js:607`
- `static/js/compare/stream.js:665`
- `static/js/compare/stream.js:693`
- `static/js/compare/stream.js:893`
- `static/js/cookbook-diagnosis.js:1020`
- `static/js/cookbook-hwfit.js:743`
- `static/js/cookbook-hwfit.js:792`
- `static/js/cookbook-hwfit.js:891`
- `static/js/cookbook-hwfit.js:905`
- `static/js/cookbook-hwfit.js:910`
- `static/js/cookbook-hwfit.js:937`
- `static/js/cookbook-hwfit.js:1022`
- `static/js/cookbook-hwfit.js:2344`
- `static/js/cookbookServe.js:2109`
- `static/js/cookbookServe.js:2884`
- `static/js/cookbookServe.js:4005`
- `static/js/cookbookServe.js:4329`
- `static/js/cookbookServe.js:4333`
- `static/js/cookbookServe.js:4340`
- `static/js/cookbookServe.js:4344`
- `static/js/cookbookServe.js:4370`
- `static/js/cookbookServe.js:4376`
- … +85 more (grep the name in repo)

## `_clearHalos` — function, line 2637
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 2643
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 2650
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 2677
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 2706
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `onTargetClick` — arrow, line 2718
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `name` — class, line 2736
- **called from:**
- `static/js/compare/selector.js:311`
- `static/js/cookbook-hwfit.js:2560`
- `static/js/cookbookRunning.js:2275`
- `static/js/cookbookSchedule.js:272`
- `static/js/cookbookServe.js:4102`
- `static/js/galleryEditor.js:653`
- `static/js/galleryEditor.js:2214`
- `static/js/galleryEditor.js:2229`
- `static/js/langIcons.js:175`
- `static/js/modelPicker.js:510`
- `static/js/presets.js:283`
- `static/js/presets.js:975`
- `static/js/sessions.js:25`
- `static/js/skills.js:109`
- `static/js/skills.js:906`
- `static/js/skills.js:1547`
- `static/js/slashCommands.js:6251`
- `static/js/tasks.js:916`

## `onClick` — arrow, line 2785
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `tick` — arrow, line 2794
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_cmdTourCookbook` — function, line 2841
- **called from:**
- `static/js/slashCommands.js:2841`

## `_makeHalo` — function, line 2895
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 2899
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `_clearHalos` — function, line 2916
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 2921
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 2928
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 2964
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 2991
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_clickTab` — function, line 3002
- **called from:**
- `static/js/slashCommands.js:3002`
- `static/js/slashCommands.js:3018`
- `static/js/slashCommands.js:3021`
- `static/js/slashCommands.js:3024`
- `static/js/slashCommands.js:3027`
- `static/js/slashCommands.js:3030`
- `static/js/slashCommands.js:3033`
- `static/js/slashCommands.js:3043`
- `static/js/slashCommands.js:3060`
- `static/js/slashCommands.js:3257`
- `static/js/slashCommands.js:3270`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3289`
- `static/js/slashCommands.js:3716`
- `static/js/slashCommands.js:3725`
- `static/js/slashCommands.js:3728`
- `static/js/slashCommands.js:3731`
- `static/js/slashCommands.js:3734`
- `static/js/slashCommands.js:3737`
- `static/js/slashCommands.js:3753`

## `_cmdTourTheme` — function, line 3067
- **called from:**
- `static/js/slashCommands.js:3067`

## `_makeHalo` — function, line 3124
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 3128
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `_clearHalos` — function, line 3145
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 3150
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 3157
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 3196
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `cleanup` — arrow, line 3229
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `onClick` — arrow, line 3236
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_clickTab` — function, line 3257
- **called from:**
- `static/js/slashCommands.js:3002`
- `static/js/slashCommands.js:3018`
- `static/js/slashCommands.js:3021`
- `static/js/slashCommands.js:3024`
- `static/js/slashCommands.js:3027`
- `static/js/slashCommands.js:3030`
- `static/js/slashCommands.js:3033`
- `static/js/slashCommands.js:3043`
- `static/js/slashCommands.js:3060`
- `static/js/slashCommands.js:3257`
- `static/js/slashCommands.js:3270`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3289`
- `static/js/slashCommands.js:3716`
- `static/js/slashCommands.js:3725`
- `static/js/slashCommands.js:3728`
- `static/js/slashCommands.js:3731`
- `static/js/slashCommands.js:3734`
- `static/js/slashCommands.js:3737`
- `static/js/slashCommands.js:3753`

## `_cmdTourSettings` — function, line 3313
- **called from:**
- `static/js/slashCommands.js:3313`

## `_makeHalo` — function, line 3368
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 3372
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `tick` — arrow, line 3383
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_clearHalos` — function, line 3398
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 3403
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 3409
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 3444
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 3472
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_clickNav` — function, line 3484
- **called from:**
- `static/js/slashCommands.js:3484`
- `static/js/slashCommands.js:3495`
- `static/js/slashCommands.js:3498`
- `static/js/slashCommands.js:3501`
- `static/js/slashCommands.js:3504`
- `static/js/slashCommands.js:3507`
- `static/js/slashCommands.js:3510`
- `static/js/slashCommands.js:3513`
- `static/js/slashCommands.js:3516`
- `static/js/slashCommands.js:3519`
- `static/js/slashCommands.js:3522`
- `static/js/slashCommands.js:3538`

## `_cmdTourGallery` — function, line 3545
- **called from:**
- `static/js/slashCommands.js:3545`

## `_makeHalo` — function, line 3601
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 3605
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `tick` — arrow, line 3615
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_clearHalos` — function, line 3630
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 3635
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 3641
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 3676
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 3704
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_clickTab` — function, line 3716
- **called from:**
- `static/js/slashCommands.js:3002`
- `static/js/slashCommands.js:3018`
- `static/js/slashCommands.js:3021`
- `static/js/slashCommands.js:3024`
- `static/js/slashCommands.js:3027`
- `static/js/slashCommands.js:3030`
- `static/js/slashCommands.js:3033`
- `static/js/slashCommands.js:3043`
- `static/js/slashCommands.js:3060`
- `static/js/slashCommands.js:3257`
- `static/js/slashCommands.js:3270`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3289`
- `static/js/slashCommands.js:3716`
- `static/js/slashCommands.js:3725`
- `static/js/slashCommands.js:3728`
- `static/js/slashCommands.js:3731`
- `static/js/slashCommands.js:3734`
- `static/js/slashCommands.js:3737`
- `static/js/slashCommands.js:3753`

## `_cmdTourNotes` — function, line 3760
- **called from:**
- `static/js/slashCommands.js:3760`

## `_makeHalo` — function, line 3814
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 3818
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `tick` — arrow, line 3828
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_clearHalos` — function, line 3843
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 3848
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 3854
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 3889
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 3917
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_cmdTourBrain` — function, line 3963
- **called from:**
- `static/js/slashCommands.js:3963`

## `_makeHalo` — function, line 4014
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 4018
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `tick` — arrow, line 4028
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `_clearHalos` — function, line 4043
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 4048
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 4054
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 4089
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 4117
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_tab` — arrow, line 4129
- **called from:**
- `static/js/slashCommands.js:4133`
- `static/js/slashCommands.js:4137`
- `static/js/slashCommands.js:4140`
- `static/js/slashCommands.js:4143`

## `_openTasksForTour` — function, line 4164
- **called from:**
- `static/js/slashCommands.js:4164`
- `static/js/slashCommands.js:4211`

## `_runTaskTour` — function, line 4178
- **called from:**
- `static/js/slashCommands.js:4178`
- `static/js/slashCommands.js:4366`
- `static/js/slashCommands.js:4382`

## `clearHalos` — function, line 4223
- **called from:**
- `static/js/slashCommands.js:4223`
- `static/js/slashCommands.js:4263`
- `static/js/slashCommands.js:4286`
- `static/js/slashCommands.js:4329`

## `makeHalo` — function, line 4228
- **called from:**
- `static/js/slashCommands.js:2295`
- `static/js/slashCommands.js:4228`
- `static/js/slashCommands.js:4292`

## `update` — arrow, line 4232
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `tick` — arrow, line 4247
- **called from:**
- `src/background_tool_jobs.py:190`
- `tests/test_background_tool_jobs.py:35`
- `tests/test_background_tool_jobs.py:39`
- `tests/test_background_tool_jobs.py:40`
- `tests/test_background_tool_jobs.py:51`
- `tests/test_background_tool_jobs.py:85`
- `tests/test_background_tool_jobs.py:88`
- `tests/test_background_tool_jobs.py:113`
- `tests/test_background_tool_jobs.py:204`
- `tests/test_background_tool_jobs.py:219`
- `static/js/backgroundToolJobs.js:125`
- `static/js/backgroundToolJobs.js:127`
- `static/js/document.js:16847`
- `static/js/editor/build/transform-popup.js:152`
- `static/js/editor/build/transform-popup.js:156`
- `static/js/editor/build/transform-popup.js:159`
- `static/js/escMenuStack.js:101`
- `static/js/galleryEditor.js:891`
- `static/js/galleryEditor.js:14278`
- `static/js/slashCommands.js:2802`

## `clear` — function, line 4262
- **called from:**
- `mcp_servers/email_server.py:117`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email/email_routes.py:1936`
- `routes/email/email_routes.py:1937`
- `routes/gallery/gallery_routes.py:109`
- `routes/gallery/gallery_routes.py:110`
- `routes/model_routes.py:1506`
- `routes/session_routes.py:1045`
- `routes/shell_routes.py:2077`
- `routes/shell_routes.py:2204`
- `scripts/diffusion_server.py:101`
- `scripts/odysseus_related_flow_audit.py:651`
- `services/search/core.py:986`
- `services/skills/agent_runner.py:52`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/agent_runtime/context_resolution.py:235`
- `src/agent_tools/filesystem_tools.py:645`
- `src/agent_tools/web_tools.py:2711`
- `src/chatgpt_subscription.py:734`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:4565`
- `src/llm_core.py:4566`
- `src/llm_core.py:4764`
- `src/llm_core.py:5124`
- `src/shutdown.py:34`
- `src/skill_index.py:116`
- `src/task_scheduler.py:581`
- `src/tool_index.py:881`
- `tests/cli/test_gallery_cli_tag_filters.py:37`
- `tests/conftest.py:400`
- `tests/smoke/stub_provider.py:69`
- `tests/test_admin_routes_auth_disabled.py:330`
- `tests/test_agent_editor_routes.py:606`
- `tests/test_agent_editor_routes.py:620`
- `tests/test_agent_editor_routes.py:1357`
- `tests/test_agent_state_dir_confinement.py:283`
- `tests/test_api_token_routes.py:160`
- `tests/test_background_tool_jobs.py:38`
- `tests/test_background_tool_jobs.py:87`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:85`
- `tests/test_browser_identity_transport.py:109`
- `tests/test_browser_identity_transport.py:120`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:92`
- `tests/test_browser_resource_identity.py:112`
- `tests/test_browser_resource_identity.py:113`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_browser_resource_identity.py:271`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_context_resolution_route.py:90`
- `tests/test_editor_generation_model_routing.py:242`
- … +197 more (grep the name in repo)

## `positionTooltip` — function, line 4267
- **called from:**
- `static/js/slashCommands.js:2218`
- `static/js/slashCommands.js:2362`
- `static/js/slashCommands.js:4267`
- `static/js/slashCommands.js:4302`

## `showStep` — function, line 4284
- **called from:**
- `static/js/slashCommands.js:2320`
- `static/js/slashCommands.js:2535`
- `static/js/slashCommands.js:4284`
- `static/js/slashCommands.js:4322`

## `onClick` — arrow, line 4305
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `onClick` — arrow, line 4348
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_cmdTourTask1` — function, line 4365
- **called from:**
- `static/js/slashCommands.js:4365`

## `_cmdTourTask2` — function, line 4381
- **called from:**
- `static/js/slashCommands.js:4377`
- `static/js/slashCommands.js:4381`

## `_cmdTourResearch` — function, line 4405
- **called from:**
- `static/js/slashCommands.js:4405`

## `_makeHalo` — function, line 4459
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 4463
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `_clearHalos` — function, line 4480
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 4485
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 4492
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 4527
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `onClick` — arrow, line 4554
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_ensureSettingsOpen` — function, line 4565
- **called from:**
- `static/js/slashCommands.js:4565`

## `_cmdTourLibrary` — function, line 4619
- **called from:**
- `static/js/slashCommands.js:4619`

## `_makeHalo` — function, line 4673
- **called from:**
- `static/js/slashCommands.js:2614`
- `static/js/slashCommands.js:2686`
- `static/js/slashCommands.js:2776`
- `static/js/slashCommands.js:2895`
- `static/js/slashCommands.js:2975`
- `static/js/slashCommands.js:3124`
- `static/js/slashCommands.js:3210`
- `static/js/slashCommands.js:3212`
- `static/js/slashCommands.js:3368`
- `static/js/slashCommands.js:3456`
- `static/js/slashCommands.js:3601`
- `static/js/slashCommands.js:3688`
- `static/js/slashCommands.js:3814`
- `static/js/slashCommands.js:3901`
- `static/js/slashCommands.js:4014`
- `static/js/slashCommands.js:4101`
- `static/js/slashCommands.js:4459`
- `static/js/slashCommands.js:4538`
- `static/js/slashCommands.js:4673`
- `static/js/slashCommands.js:4754`

## `update` — arrow, line 4677
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `_clearHalos` — function, line 4694
- **called from:**
- `static/js/slashCommands.js:2637`
- `static/js/slashCommands.js:2645`
- `static/js/slashCommands.js:2683`
- `static/js/slashCommands.js:2765`
- `static/js/slashCommands.js:2916`
- `static/js/slashCommands.js:2923`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3145`
- `static/js/slashCommands.js:3152`
- `static/js/slashCommands.js:3205`
- `static/js/slashCommands.js:3398`
- `static/js/slashCommands.js:3404`
- `static/js/slashCommands.js:3451`
- `static/js/slashCommands.js:3630`
- `static/js/slashCommands.js:3636`
- `static/js/slashCommands.js:3683`
- `static/js/slashCommands.js:3843`
- `static/js/slashCommands.js:3849`
- `static/js/slashCommands.js:3896`
- `static/js/slashCommands.js:4043`
- `static/js/slashCommands.js:4049`
- `static/js/slashCommands.js:4096`
- `static/js/slashCommands.js:4480`
- `static/js/slashCommands.js:4487`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4694`
- `static/js/slashCommands.js:4701`
- `static/js/slashCommands.js:4750`

## `_clear` — arrow, line 4699
- **called from:**
- `static/js/galleryEditor.js:1159`
- `static/js/galleryEditor.js:1161`
- `static/js/galleryEditor.js:1164`
- `static/js/slashCommands.js:2760`
- `static/js/slashCommands.js:2805`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:2835`
- `static/js/slashCommands.js:3055`
- `static/js/slashCommands.js:3061`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3307`
- `static/js/slashCommands.js:3533`
- `static/js/slashCommands.js:3539`
- `static/js/slashCommands.js:3748`
- `static/js/slashCommands.js:3754`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:3957`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4158`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4597`
- `static/js/slashCommands.js:4825`
- `static/js/slashCommands.js:4841`
- `static/js/slashCommands.js:4855`
- `static/js/slashCommands.js:4883`
- `static/js/slashCommands.js:4887`

## `_positionTooltip` — function, line 4706
- **called from:**
- `static/js/slashCommands.js:2650`
- `static/js/slashCommands.js:2701`
- `static/js/slashCommands.js:2777`
- `static/js/slashCommands.js:2928`
- `static/js/slashCommands.js:2987`
- `static/js/slashCommands.js:3157`
- `static/js/slashCommands.js:3224`
- `static/js/slashCommands.js:3409`
- `static/js/slashCommands.js:3468`
- `static/js/slashCommands.js:3641`
- `static/js/slashCommands.js:3700`
- `static/js/slashCommands.js:3854`
- `static/js/slashCommands.js:3913`
- `static/js/slashCommands.js:4054`
- `static/js/slashCommands.js:4113`
- `static/js/slashCommands.js:4492`
- `static/js/slashCommands.js:4550`
- `static/js/slashCommands.js:4706`
- `static/js/slashCommands.js:4766`

## `_showStep` — function, line 4741
- **called from:**
- `static/js/slashCommands.js:2677`
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2826`
- `static/js/slashCommands.js:2964`
- `static/js/slashCommands.js:3049`
- `static/js/slashCommands.js:3196`
- `static/js/slashCommands.js:3295`
- `static/js/slashCommands.js:3444`
- `static/js/slashCommands.js:3527`
- `static/js/slashCommands.js:3676`
- `static/js/slashCommands.js:3742`
- `static/js/slashCommands.js:3889`
- `static/js/slashCommands.js:3947`
- `static/js/slashCommands.js:4089`
- `static/js/slashCommands.js:4148`
- `static/js/slashCommands.js:4527`
- `static/js/slashCommands.js:4587`
- `static/js/slashCommands.js:4741`
- `static/js/slashCommands.js:4817`
- `static/js/slashCommands.js:4877`

## `cleanup` — arrow, line 4771
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `onClick` — arrow, line 4775
- **called from:**
- `static/js/calendar.js:636`
- `static/js/cookbookServe.js:2777`
- `static/js/cookbookServe.js:2837`
- `static/js/skills.js:550`
- `static/js/tasks.js:1141`

## `_cmdPrompt` — function, line 4894
- **called from:**
- `static/js/slashCommands.js:4894`

## `_ensureSetupSpotlightStyles` — function, line 4925
- **called from:**
- `static/js/slashCommands.js:4925`
- `static/js/slashCommands.js:4957`

## `_visibleSetupTarget` — function, line 4947
- **called from:**
- `static/js/slashCommands.js:4947`
- `static/js/slashCommands.js:4958`

## `_showSetupSpotlight` — function, line 4956
- **called from:**
- `static/js/slashCommands.js:4956`

## `update` — arrow, line 4965
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
- `routes/chat_routes.py:3599`
- `routes/chat_routes.py:3658`
- `routes/chat_routes.py:3670`
- `routes/chat_routes.py:3688`
- `routes/chat_routes.py:3704`
- `routes/chat_routes.py:3706`
- `routes/chat_routes.py:3709`
- `routes/chat_routes.py:3711`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3716`
- `routes/chat_routes.py:3724`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3736`
- `routes/chat_routes.py:3740`
- `routes/chat_routes.py:3751`
- `routes/chat_routes.py:3754`
- `routes/chat_routes.py:3761`
- `routes/chat_routes.py:3845`
- `routes/chat_routes.py:3854`
- `routes/chat_routes.py:3858`
- `routes/chat_routes.py:4044`
- `routes/chat_routes.py:4458`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:4718`
- `routes/chat_routes.py:5020`
- `routes/chat_routes.py:5024`
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
- … +547 more (grep the name in repo)

## `cleanup` — arrow, line 4980
- **called from:**
- `tests/test_browser_producer_live_contract.py:41`
- `tests/test_ca_trust.py:43`
- `static/js/calendar.js:3194`
- `static/js/calendar.js:3202`
- `static/js/calendar.js:3239`
- `static/js/calendar.js:3369`
- `static/js/calendar.js:3378`
- `static/js/chat.js:7595`
- `static/js/chat.js:9103`
- `static/js/chat.js:9111`
- `static/js/chat.js:9117`
- `static/js/chat.js:9120`
- `static/js/chat.js:9123`
- `static/js/chat.js:9146`
- `static/js/codeRunner.js:273`
- `static/js/codeRunner.js:294`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:953`
- `static/js/compare/selector.js:986`
- `static/js/compare/selector.js:990`
- `static/js/compare/selector.js:1046`
- `static/js/compare/selector.js:1345`
- `static/js/compare/selector.js:1367`
- `static/js/compare/selector.js:1380`
- `static/js/cookbookServe.js:1058`
- `static/js/cookbookServe.js:1069`
- `static/js/cookbookServe.js:1070`
- `static/js/cookbookServe.js:1079`
- `static/js/cookbookServe.js:1081`
- `static/js/cookbookServe.js:1086`
- `static/js/document.js:6258`
- `static/js/document.js:6263`
- `static/js/document.js:6978`
- `static/js/document.js:6985`
- `static/js/document.js:7028`
- `static/js/document.js:15678`
- `static/js/document.js:15699`
- `static/js/dragSort.js:26`
- `static/js/editor/ai-operation.js:35`
- `static/js/editor/ai-operation.js:41`
- `static/js/editor/ai-operation.js:42`
- `static/js/editor/slider-ux.js:181`
- `static/js/editor/slider-ux.js:190`
- `static/js/editor/wire-topbar-overflow.js:23`
- `static/js/gallery.js:1910`
- `static/js/gallery.js:1919`
- `static/js/gallery.js:2063`
- `static/js/gallery.js:2075`
- `static/js/gallery.js:2079`
- `static/js/galleryEditor.js:7450`
- `static/js/galleryEditor.js:7530`
- `static/js/galleryEditor.js:7565`
- `static/js/galleryEditor.js:8330`
- `static/js/galleryEditor.js:8354`
- `static/js/galleryEditor.js:8357`
- `static/js/galleryEditor.js:8365`
- `static/js/galleryEditor.js:8368`
- `static/js/galleryEditor.js:8372`
- `static/js/galleryEditor.js:8373`
- `static/js/galleryEditor.js:8375`
- … +33 more (grep the name in repo)

## `_runSetupEndpointSpotlight` — function, line 5012
- **called from:**
- `static/js/slashCommands.js:5012`
- `static/js/slashCommands.js:5023`
- `static/js/slashCommands.js:5028`

## `_showSetupEndpointGuide` — function, line 5019
- **called from:**
- `static/js/slashCommands.js:5019`
- `static/js/slashCommands.js:5149`
- `static/js/slashCommands.js:5154`
- `static/js/slashCommands.js:5218`
- `static/js/slashCommands.js:5221`

## `_clearSetupCommandInput` — function, line 5032
- **called from:**
- `static/js/slashCommands.js:5032`
- `static/js/slashCommands.js:5100`

## `_setupProviderDeviceFlow` — function, line 5042
- **called from:**
- `static/js/slashCommands.js:790`
- `static/js/slashCommands.js:5042`
- `static/js/slashCommands.js:5105`

## `_cmdSetup` — function, line 5098
- **called from:**
- `static/js/slashCommands.js:5098`
- `static/js/slashCommands.js:5903`
- `static/js/slashCommands.js:5904`
- `static/js/slashCommands.js:5905`
- `static/js/slashCommands.js:5906`
- `static/js/slashCommands.js:5907`
- `static/js/slashCommands.js:5908`
- `static/js/slashCommands.js:5909`
- `static/js/slashCommands.js:5910`
- `static/js/slashCommands.js:5911`
- `static/js/slashCommands.js:5912`
- `static/js/slashCommands.js:5915`
- `static/js/slashCommands.js:5918`

## `_cmdShortcuts` — function, line 5226
- **called from:**
- `static/js/slashCommands.js:5226`

## `formatCombo` — arrow, line 5244
- **called from:**
- `static/js/slashCommands.js:5253`
- `static/js/slashCommands.js:5254`
- `static/js/slashCommands.js:5255`
- `static/js/slashCommands.js:5256`
- `static/js/slashCommands.js:5257`
- `static/js/slashCommands.js:5258`

## `_eggRender` — function, line 5327
- **called from:**
- `static/js/slashCommands.js:5327`
- `static/js/slashCommands.js:5406`
- `static/js/slashCommands.js:5422`
- `static/js/slashCommands.js:5437`
- `static/js/slashCommands.js:5448`
- `static/js/slashCommands.js:5476`
- `static/js/slashCommands.js:5525`
- `static/js/slashCommands.js:5549`
- `static/js/slashCommands.js:5569`
- `static/js/slashCommands.js:5719`

## `_cmdFlip` — function, line 5366
- **called from:**
- `static/js/slashCommands.js:5366`

## `_cmdRoll` — function, line 5395
- **called from:**
- `static/js/slashCommands.js:5395`

## `_cmd8Ball` — function, line 5415
- **called from:**
- `static/js/slashCommands.js:5415`

## `_cmdFortune` — function, line 5435
- **called from:**
- `static/js/slashCommands.js:5435`

## `_cmdOdyssey` — function, line 5446
- **called from:**
- `static/js/slashCommands.js:5446`

## `_cmdAscii` — function, line 5456
- **called from:**
- `static/js/slashCommands.js:5456`

## `_cmdMatrix` — function, line 5481
- **called from:**
- `static/js/slashCommands.js:5481`

## `_cmdSay` — function, line 5518
- **called from:**
- `static/js/slashCommands.js:5518`

## `_cmdWisdom` — function, line 5530
- **called from:**
- `static/js/slashCommands.js:5530`

## `_cmdUptime` — function, line 5557
- **called from:**
- `static/js/slashCommands.js:5557`

## `_cmdPing` — function, line 5578
- **called from:**
- `static/js/slashCommands.js:5578`

## `_cmdProbe` — function, line 5610
- **called from:**
- `static/js/slashCommands.js:5610`

## `_cmdColor` — function, line 5716
- **called from:**
- `static/js/slashCommands.js:5716`

## `_cmdHelp` — function, line 5731
- **called from:**
- `static/js/slashCommands.js:5731`

## `_makeCtx` — function, line 6244
- **called from:**
- `static/js/slashCommands.js:6244`
- `static/js/slashCommands.js:6317`

## `_buildAliasMap` — function, line 6252
- **called from:**
- `static/js/slashCommands.js:6252`
- `static/js/slashCommands.js:6260`

## `_resolveCommand` — function, line 6263
- **called from:**
- `static/js/slashCommands.js:6263`
- `static/js/slashCommands.js:6328`

## `_resolveSubcommand` — function, line 6268
- **called from:**
- `static/js/slashCommands.js:6268`
- `static/js/slashCommands.js:6379`

## `_levenshtein` — function, line 6278
- **called from:**
- `static/js/slashCommands.js:6278`
- `static/js/slashCommands.js:6301`

## `_fuzzyMatch` — function, line 6294
- **called from:**
- `static/js/slashCommands.js:6294`
- `static/js/slashCommands.js:6429`

## `_isCmd` — function, line 6309
- **called from:**
- `static/js/slashCommands.js:6309`
- `static/js/slashCommands.js:6520`

## `handleSlashCommand` — function, line 6313
- **called from:**
- `static/js/chat.js:2721`
- `static/js/slashCommands.js:6313`
- `static/js/tourAutoplay.js:61`

## `_showUser` — function, line 6321
- **called from:**
- `static/js/slashCommands.js:6321`
- `static/js/slashCommands.js:6339`
- `static/js/slashCommands.js:6348`
- `static/js/slashCommands.js:6360`
- `static/js/slashCommands.js:6423`
- `static/js/slashCommands.js:6431`
- `static/js/slashCommands.js:6437`

## `initSlashCommands` — function, line 6454
- **called from:**
- `static/js/chat.js:2064`
- `static/js/slashCommands.js:6454`

## `isCommand` — function, line 6519
- **called from:**
- `static/js/chat.js:2694`
- `static/js/chat.js:2708`
- `static/js/chat.js:2720`
- `static/js/slashCommands.js:6519`

## `getSetupMode` — function, line 6526
- **called from:**
- `static/js/chat.js:2693`
- `static/js/slashCommands.js:6526`

## `clearSetupMode` — function, line 6533
- **called from:**
- `static/js/chat.js:2696`
- `static/js/chat.js:2709`
- `static/js/slashCommands.js:6533`
