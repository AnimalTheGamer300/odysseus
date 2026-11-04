# `static/js/slashCommands.js` — definitions & call sites

254 definitions (regex-based, best-effort).
**Exports:** `COMMANDS`, `LEGACY_ALIASES`, `clearSetupMode`, `default`, `getSetupMode`, `handleSetupInput`, `handleSetupWizard`, `handleSlashCommand`, `initSlashCommands`, `isCommand`, `slashReply`, `typewriterInto`, `typewriterReply`

## `cancelActiveTour` — function, line 4
- **called from:**
- `static/js/slashCommands.js:4`

## `_isStreamingFn` — arrow, line 38
- **called from:**
- `static/js/slashCommands.js:2538`
- `static/js/slashCommands.js:2542`

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
- `static/js/slashCommands.js:5097`

## `_setupDeviceAuthProviderFromInput` — function, line 111
- **called from:**
- `static/js/slashCommands.js:111`
- `static/js/slashCommands.js:786`
- `static/js/slashCommands.js:5092`

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
- `static/js/slashCommands.js:5122`

## `_clearSetupGuideMessages` — function, line 167
- **called from:**
- `static/js/slashCommands.js:167`
- `static/js/slashCommands.js:712`
- `static/js/slashCommands.js:5039`
- `static/js/slashCommands.js:5099`
- `static/js/slashCommands.js:5119`
- `static/js/slashCommands.js:5137`
- `static/js/slashCommands.js:5142`
- `static/js/slashCommands.js:5205`

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
- `static/js/slashCommands.js:5042`
- `static/js/slashCommands.js:5045`
- `static/js/slashCommands.js:5061`
- `static/js/slashCommands.js:5070`
- `static/js/slashCommands.js:5075`
- `static/js/slashCommands.js:5079`
- `static/js/slashCommands.js:5083`
- `static/js/slashCommands.js:5112`
- `static/js/slashCommands.js:5126`

## `_showSetupEndpointChoices` — function, line 198
- **called from:**
- `static/js/slashCommands.js:172`
- `static/js/slashCommands.js:198`
- `static/js/slashCommands.js:5017`

## `_showSetupEndpointChoicesStreamed` — function, line 226
- **called from:**
- `static/js/slashCommands.js:226`
- `static/js/slashCommands.js:5022`

## `_hasConfiguredModels` — function, line 263
- **called from:**
- `static/js/slashCommands.js:263`
- `static/js/slashCommands.js:2115`

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
- `static/js/slashCommands.js:6289`

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
- `static/js/slashCommands.js:1283`
- `static/js/slashCommands.js:1290`
- `static/js/slashCommands.js:1303`
- `static/js/slashCommands.js:1313`
- `static/js/slashCommands.js:1352`
- `static/js/slashCommands.js:1393`
- `static/js/slashCommands.js:1419`
- `static/js/slashCommands.js:1433`
- `static/js/slashCommands.js:1458`
- `static/js/slashCommands.js:1474`
- `static/js/slashCommands.js:1479`
- `static/js/slashCommands.js:1488`
- `static/js/slashCommands.js:1491`
- `static/js/slashCommands.js:1504`
- `static/js/slashCommands.js:1522`
- `static/js/slashCommands.js:1530`
- `static/js/slashCommands.js:1540`
- `static/js/slashCommands.js:1552`
- `static/js/slashCommands.js:1557`
- … +93 more (grep the name in repo)

## `_loadSkillSlashCatalog` — function, line 343
- **called from:**
- `static/js/slashCommands.js:343`
- `static/js/slashCommands.js:1655`
- `static/js/slashCommands.js:1710`
- `static/js/slashCommands.js:5735`
- `static/js/slashCommands.js:6389`

## `_submitComposedMessage` — function, line 358
- **called from:**
- `static/js/slashCommands.js:358`
- `static/js/slashCommands.js:385`

## `_invokeSkillByName` — function, line 372
- **called from:**
- `static/js/slashCommands.js:372`
- `static/js/slashCommands.js:1702`
- `static/js/slashCommands.js:6392`

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
- `static/js/slashCommands.js:1343`
- `static/js/slashCommands.js:1484`
- `static/js/slashCommands.js:1493`
- `static/js/slashCommands.js:1497`
- `static/js/slashCommands.js:1515`
- `static/js/slashCommands.js:1591`
- `static/js/slashCommands.js:1615`
- `static/js/slashCommands.js:1630`
- `static/js/slashCommands.js:1642`
- `static/js/slashCommands.js:1725`
- `static/js/slashCommands.js:1831`
- `static/js/slashCommands.js:1855`
- `static/js/slashCommands.js:1917`
- `static/js/slashCommands.js:1943`
- `static/js/slashCommands.js:1952`
- `static/js/slashCommands.js:2117`
- `static/js/slashCommands.js:2480`
- `static/js/slashCommands.js:2549`
- `static/js/slashCommands.js:2832`
- `static/js/slashCommands.js:3058`
- `static/js/slashCommands.js:3304`
- `static/js/slashCommands.js:3536`
- `static/js/slashCommands.js:3751`
- `static/js/slashCommands.js:3954`
- `static/js/slashCommands.js:4155`
- `static/js/slashCommands.js:4357`
- `static/js/slashCommands.js:4595`
- `static/js/slashCommands.js:4838`
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
- `static/js/chat.js:2544`
- `static/js/chat.js:5079`
- `static/js/chat.js:5292`
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
- `static/js/slashCommands.js:5102`
- `static/js/slashCommands.js:5123`

## `handleSetupInput` — function, line 732
- **called from:**
- `static/js/chat.js:1679`
- `static/js/slashCommands.js:732`
- `static/js/slashCommands.js:776`

## `handleSetupWizard` — function, line 772
- **called from:**
- `static/js/chat.js:1681`
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
- `static/js/slashCommands.js:1306`

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

## `_cmdToggleShow` — function, line 1294
- **called from:**
- `static/js/slashCommands.js:1294`

## `_cmdToggleSidebar` — function, line 1310
- **called from:**
- `static/js/slashCommands.js:1310`

## `_cmdOpen` — function, line 1349
- **called from:**
- `static/js/slashCommands.js:1349`
- `static/js/slashCommands.js:1441`

## `clickFirst` — arrow, line 1355
- **called from:**
- `static/js/slashCommands.js:1365`
- `static/js/slashCommands.js:1370`
- `static/js/slashCommands.js:1389`

## `_cmdToolPanel` — function, line 1397
- **called from:**
- `static/js/slashCommands.js:1397`
- `static/js/slashCommands.js:5999`
- `static/js/slashCommands.js:6006`
- `static/js/slashCommands.js:6013`
- `static/js/slashCommands.js:6020`
- `static/js/slashCommands.js:6027`
- `static/js/slashCommands.js:6034`
- `static/js/slashCommands.js:6041`
- `static/js/slashCommands.js:6048`
- `static/js/slashCommands.js:6055`

## `_cmdSettings` — function, line 1444
- **called from:**
- `static/js/slashCommands.js:1444`

## `_cmdTheme` — function, line 1466
- **called from:**
- `static/js/slashCommands.js:1466`

## `_cmdModels` — function, line 1521
- **called from:**
- `static/js/slashCommands.js:1521`
- `static/js/slashCommands.js:1536`

## `_cmdModel` — function, line 1534
- **called from:**
- `static/js/slashCommands.js:1534`

## `_cmdMcp` — function, line 1549
- **called from:**
- `static/js/slashCommands.js:1549`

## `_cmdMemoryList` — function, line 1572
- **called from:**
- `static/js/slashCommands.js:1572`

## `_cmdMemoryAdd` — function, line 1583
- **called from:**
- `static/js/slashCommands.js:1583`

## `_cmdMemoryDelete` — function, line 1596
- **called from:**
- `static/js/slashCommands.js:1596`

## `_cmdMemorySearch` — function, line 1635
- **called from:**
- `static/js/slashCommands.js:1635`

## `_cmdSkills` — function, line 1650
- **called from:**
- `static/js/slashCommands.js:1650`

## `_cmdReloadSkills` — function, line 1709
- **called from:**
- `static/js/slashCommands.js:1709`

## `_cmdNote` — function, line 1717
- **called from:**
- `static/js/slashCommands.js:1717`

## `_pad2` — function, line 1735
- **called from:**
- `static/js/slashCommands.js:1735`
- `static/js/slashCommands.js:1739`
- `static/js/slashCommands.js:1739`
- `static/js/slashCommands.js:1739`
- `static/js/slashCommands.js:1739`

## `_toLocalIso` — function, line 1738
- **called from:**
- `static/js/slashCommands.js:1738`
- `static/js/slashCommands.js:1845`
- `static/js/slashCommands.js:1846`

## `_parseTimeSpec` — function, line 1752
- **called from:**
- `static/js/slashCommands.js:1752`
- `static/js/slashCommands.js:1839`

## `_cmdTodo` — function, line 1811
- **called from:**
- `static/js/slashCommands.js:1811`

## `_cmdEvent` — function, line 1836
- **called from:**
- `static/js/slashCommands.js:1836`

## `_cmdShell` — function, line 1865
- **called from:**
- `static/js/slashCommands.js:1865`

## `_cmdRagList` — function, line 1890
- **called from:**
- `static/js/slashCommands.js:1890`

## `_cmdRagAdd` — function, line 1907
- **called from:**
- `static/js/slashCommands.js:1907`

## `_cmdRagRemove` — function, line 1922
- **called from:**
- `static/js/slashCommands.js:1922`

## `_cmdWebSearch` — function, line 1959
- **called from:**
- `static/js/slashCommands.js:1959`

## `_cmdSearch` — function, line 1973
- **called from:**
- `static/js/slashCommands.js:1973`

## `_cmdStats` — function, line 1994
- **called from:**
- `static/js/slashCommands.js:1994`

## `_cmdUsage` — function, line 2007
- **called from:**
- `static/js/slashCommands.js:2007`

## `_cmdCompact` — function, line 2056
- **called from:**
- `static/js/slashCommands.js:2056`

## `_cmdTts` — function, line 2090
- **called from:**
- `static/js/slashCommands.js:2090`

## `_cmdDemo` — function, line 2114
- **called from:**
- `static/js/slashCommands.js:2114`

## `_clearTour` — arrow, line 2131
- **called from:**
- `static/js/slashCommands.js:2532`
- `static/js/slashCommands.js:2548`

## `_restoreIfCleared` — arrow, line 2160
- **called from:**
- `static/js/slashCommands.js:2168`

## `positionTooltip` — function, line 2214
- **called from:**
- `static/js/slashCommands.js:2214`
- `static/js/slashCommands.js:2358`
- `static/js/slashCommands.js:4263`
- `static/js/slashCommands.js:4298`

## `streamHTML` — function, line 2269
- **called from:**
- `static/js/slashCommands.js:2269`
- `static/js/slashCommands.js:2362`

## `on` — class, line 2289
- **called from:**
- `static/js/chat.js:2032`
- `static/js/compare/index.js:937`
- `static/js/cookbook-hwfit.js:2477`
- `static/js/gallery.js:2509`
- `static/js/streamingSegmenter.js:15`
- `static/js/windowResize.js:208`

## `makeHalo` — function, line 2291
- **called from:**
- `static/js/slashCommands.js:2291`
- `static/js/slashCommands.js:4224`
- `static/js/slashCommands.js:4288`

## `update` — arrow, line 2295
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `destroy` — method?, line 2308
- **called from:**
- `static/app.js:1471`
- `static/js/admin.js:1512`
- `static/js/admin.js:1749`
- `static/js/calendar.js:2079`
- `static/js/chat.js:517`
- `static/js/chat.js:736`
- `static/js/chat.js:769`
- `static/js/chat.js:1537`
- `static/js/chat.js:1542`
- `static/js/chat.js:2660`
- `static/js/chat.js:2920`
- `static/js/chat.js:3259`
- `static/js/chat.js:3282`
- `static/js/chat.js:3357`
- `static/js/chat.js:3444`
- `static/js/chat.js:3504`
- `static/js/chat.js:3965`
- `static/js/chat.js:4351`
- `static/js/chat.js:4392`
- `static/js/chat.js:4434`
- `static/js/chat.js:4469`
- `static/js/chat.js:4837`
- `static/js/chat.js:5675`
- `static/js/chat.js:5770`
- `static/js/chat.js:5957`
- `static/js/chat.js:5968`
- `static/js/chat.js:7106`
- `static/js/chat.js:7120`
- `static/js/chat.js:7136`
- `static/js/chat.js:7423`
- `static/js/codeRunner.js:225`
- `static/js/compare/panes.js:66`
- `static/js/compare/stream.js:161`
- `static/js/compare/stream.js:493`
- `static/js/compare/stream.js:518`
- `static/js/compare/stream.js:559`
- `static/js/compare/stream.js:615`
- `static/js/compare/stream.js:644`
- `static/js/cookbook-diagnosis.js:1005`
- `static/js/cookbook-hwfit.js:702`
- `static/js/cookbook-hwfit.js:751`
- `static/js/cookbook-hwfit.js:842`
- `static/js/cookbook-hwfit.js:856`
- `static/js/cookbook-hwfit.js:861`
- `static/js/cookbook-hwfit.js:887`
- `static/js/cookbook-hwfit.js:972`
- `static/js/cookbook-hwfit.js:2237`
- `static/js/cookbookServe.js:2050`
- `static/js/cookbookServe.js:2812`
- `static/js/cookbookServe.js:3900`
- `static/js/cookbookServe.js:4186`
- `static/js/cookbookServe.js:4191`
- `static/js/cookbookServe.js:4218`
- `static/js/cookbookServe.js:4221`
- `static/js/document.js:588`
- `static/js/document.js:3998`
- `static/js/documentLibrary.js:3296`
- `static/js/documentLibrary.js:3307`
- `static/js/editor/ai-inpaint.js:248`
- `static/js/editor/ai-inpaint.js:249`
- … +67 more (grep the name in repo)

## `showStep` — function, line 2316
- **called from:**
- `static/js/slashCommands.js:2316`
- `static/js/slashCommands.js:2531`
- `static/js/slashCommands.js:4280`
- `static/js/slashCommands.js:4318`

## `onClick` — arrow, line 2368
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `onDocClickCapture` — arrow, line 2382
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `onMessageInput` — arrow, line 2402
- **called from:**
- `static/js/slashCommands.js:2453`

## `_restore` — arrow, line 2415
- **called from:**
- `tests/test_fastembed_cache_path.py:49`
- `tests/test_fastembed_cache_path.py:58`
- `tests/test_fastembed_cache_path.py:69`
- `static/js/slashCommands.js:2423`

## `onModelPicked` — arrow, line 2429
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup` — arrow, line 2431
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `delay` — arrow, line 2477
- **called from:**
- `static/app.js:3873`
- `static/js/chat.js:5217`
- `static/js/slashCommands.js:2482`
- `static/js/slashCommands.js:2536`
- `static/js/slashCommands.js:2544`

## `before` — method?, line 2516
- **called from:**
- `static/js/document.js:5043`
- `static/js/document.js:5051`
- `static/js/document.js:5052`
- `static/js/document.js:5053`
- `static/js/document.js:5054`
- `static/js/markdown.js:522`
- `static/js/slashCommands.js:2516`
- `static/js/slashCommands.js:2524`
- `static/js/slashCommands.js:2530`
- `static/js/slashCommands.js:2968`
- `static/js/slashCommands.js:3004`
- `static/js/slashCommands.js:3202`
- `static/js/slashCommands.js:3448`
- `static/js/slashCommands.js:3680`
- `static/js/slashCommands.js:3893`
- `static/js/slashCommands.js:4093`
- `static/js/slashCommands.js:4283`
- `static/js/slashCommands.js:4531`
- `static/js/slashCommands.js:4747`

## `before` — method?, line 2524
- **called from:**
- `static/js/document.js:5043`
- `static/js/document.js:5051`
- `static/js/document.js:5052`
- `static/js/document.js:5053`
- `static/js/document.js:5054`
- `static/js/markdown.js:522`
- `static/js/slashCommands.js:2516`
- `static/js/slashCommands.js:2524`
- `static/js/slashCommands.js:2530`
- `static/js/slashCommands.js:2968`
- `static/js/slashCommands.js:3004`
- `static/js/slashCommands.js:3202`
- `static/js/slashCommands.js:3448`
- `static/js/slashCommands.js:3680`
- `static/js/slashCommands.js:3893`
- `static/js/slashCommands.js:4093`
- `static/js/slashCommands.js:4283`
- `static/js/slashCommands.js:4531`
- `static/js/slashCommands.js:4747`

## `_cmdTourCompare` — function, line 2554
- **called from:**
- `static/js/slashCommands.js:2554`

## `_makeHalo` — function, line 2610
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 2614
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `destroy` — method?, line 2626
- **called from:**
- `static/app.js:1471`
- `static/js/admin.js:1512`
- `static/js/admin.js:1749`
- `static/js/calendar.js:2079`
- `static/js/chat.js:517`
- `static/js/chat.js:736`
- `static/js/chat.js:769`
- `static/js/chat.js:1537`
- `static/js/chat.js:1542`
- `static/js/chat.js:2660`
- `static/js/chat.js:2920`
- `static/js/chat.js:3259`
- `static/js/chat.js:3282`
- `static/js/chat.js:3357`
- `static/js/chat.js:3444`
- `static/js/chat.js:3504`
- `static/js/chat.js:3965`
- `static/js/chat.js:4351`
- `static/js/chat.js:4392`
- `static/js/chat.js:4434`
- `static/js/chat.js:4469`
- `static/js/chat.js:4837`
- `static/js/chat.js:5675`
- `static/js/chat.js:5770`
- `static/js/chat.js:5957`
- `static/js/chat.js:5968`
- `static/js/chat.js:7106`
- `static/js/chat.js:7120`
- `static/js/chat.js:7136`
- `static/js/chat.js:7423`
- `static/js/codeRunner.js:225`
- `static/js/compare/panes.js:66`
- `static/js/compare/stream.js:161`
- `static/js/compare/stream.js:493`
- `static/js/compare/stream.js:518`
- `static/js/compare/stream.js:559`
- `static/js/compare/stream.js:615`
- `static/js/compare/stream.js:644`
- `static/js/cookbook-diagnosis.js:1005`
- `static/js/cookbook-hwfit.js:702`
- `static/js/cookbook-hwfit.js:751`
- `static/js/cookbook-hwfit.js:842`
- `static/js/cookbook-hwfit.js:856`
- `static/js/cookbook-hwfit.js:861`
- `static/js/cookbook-hwfit.js:887`
- `static/js/cookbook-hwfit.js:972`
- `static/js/cookbook-hwfit.js:2237`
- `static/js/cookbookServe.js:2050`
- `static/js/cookbookServe.js:2812`
- `static/js/cookbookServe.js:3900`
- `static/js/cookbookServe.js:4186`
- `static/js/cookbookServe.js:4191`
- `static/js/cookbookServe.js:4218`
- `static/js/cookbookServe.js:4221`
- `static/js/document.js:588`
- `static/js/document.js:3998`
- `static/js/documentLibrary.js:3296`
- `static/js/documentLibrary.js:3307`
- `static/js/editor/ai-inpaint.js:248`
- `static/js/editor/ai-inpaint.js:249`
- … +67 more (grep the name in repo)

## `_clearHalos` — function, line 2633
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 2639
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 2646
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 2673
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 2702
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `onTargetClick` — arrow, line 2714
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `name` — class, line 2732
- **called from:**
- `static/js/compare/selector.js:311`
- `static/js/cookbook-hwfit.js:2450`
- `static/js/cookbookRunning.js:2224`
- `static/js/cookbookSchedule.js:257`
- `static/js/cookbookServe.js:3997`
- `static/js/galleryEditor.js:248`
- `static/js/langIcons.js:169`
- `static/js/modelPicker.js:500`
- `static/js/notes.js:324`
- `static/js/presets.js:278`
- `static/js/presets.js:927`
- `static/js/sessions.js:23`
- `static/js/skills.js:94`
- `static/js/skills.js:692`
- `static/js/skills.js:1267`
- `static/js/slashCommands.js:6219`
- `static/js/tasks.js:856`

## `onClick` — arrow, line 2781
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `tick` — arrow, line 2790
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `_cmdTourCookbook` — function, line 2837
- **called from:**
- `static/js/slashCommands.js:2837`

## `_makeHalo` — function, line 2891
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 2895
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `_clearHalos` — function, line 2912
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 2917
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 2924
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 2960
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 2987
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_clickTab` — function, line 2998
- **called from:**
- `static/js/slashCommands.js:2998`
- `static/js/slashCommands.js:3014`
- `static/js/slashCommands.js:3017`
- `static/js/slashCommands.js:3020`
- `static/js/slashCommands.js:3023`
- `static/js/slashCommands.js:3026`
- `static/js/slashCommands.js:3029`
- `static/js/slashCommands.js:3039`
- `static/js/slashCommands.js:3056`
- `static/js/slashCommands.js:3253`
- `static/js/slashCommands.js:3266`
- `static/js/slashCommands.js:3273`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3712`
- `static/js/slashCommands.js:3721`
- `static/js/slashCommands.js:3724`
- `static/js/slashCommands.js:3727`
- `static/js/slashCommands.js:3730`
- `static/js/slashCommands.js:3733`
- `static/js/slashCommands.js:3749`

## `_cmdTourTheme` — function, line 3063
- **called from:**
- `static/js/slashCommands.js:3063`

## `_makeHalo` — function, line 3120
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 3124
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `_clearHalos` — function, line 3141
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 3146
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 3153
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 3192
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `cleanup` — arrow, line 3225
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `onClick` — arrow, line 3232
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_clickTab` — function, line 3253
- **called from:**
- `static/js/slashCommands.js:2998`
- `static/js/slashCommands.js:3014`
- `static/js/slashCommands.js:3017`
- `static/js/slashCommands.js:3020`
- `static/js/slashCommands.js:3023`
- `static/js/slashCommands.js:3026`
- `static/js/slashCommands.js:3029`
- `static/js/slashCommands.js:3039`
- `static/js/slashCommands.js:3056`
- `static/js/slashCommands.js:3253`
- `static/js/slashCommands.js:3266`
- `static/js/slashCommands.js:3273`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3712`
- `static/js/slashCommands.js:3721`
- `static/js/slashCommands.js:3724`
- `static/js/slashCommands.js:3727`
- `static/js/slashCommands.js:3730`
- `static/js/slashCommands.js:3733`
- `static/js/slashCommands.js:3749`

## `_cmdTourSettings` — function, line 3309
- **called from:**
- `static/js/slashCommands.js:3309`

## `_makeHalo` — function, line 3364
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 3368
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `tick` — arrow, line 3379
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `_clearHalos` — function, line 3394
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 3399
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 3405
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 3440
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 3468
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_clickNav` — function, line 3480
- **called from:**
- `static/js/slashCommands.js:3480`
- `static/js/slashCommands.js:3491`
- `static/js/slashCommands.js:3494`
- `static/js/slashCommands.js:3497`
- `static/js/slashCommands.js:3500`
- `static/js/slashCommands.js:3503`
- `static/js/slashCommands.js:3506`
- `static/js/slashCommands.js:3509`
- `static/js/slashCommands.js:3512`
- `static/js/slashCommands.js:3515`
- `static/js/slashCommands.js:3518`
- `static/js/slashCommands.js:3534`

## `_cmdTourGallery` — function, line 3541
- **called from:**
- `static/js/slashCommands.js:3541`

## `_makeHalo` — function, line 3597
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 3601
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `tick` — arrow, line 3611
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `_clearHalos` — function, line 3626
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 3631
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 3637
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 3672
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 3700
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_clickTab` — function, line 3712
- **called from:**
- `static/js/slashCommands.js:2998`
- `static/js/slashCommands.js:3014`
- `static/js/slashCommands.js:3017`
- `static/js/slashCommands.js:3020`
- `static/js/slashCommands.js:3023`
- `static/js/slashCommands.js:3026`
- `static/js/slashCommands.js:3029`
- `static/js/slashCommands.js:3039`
- `static/js/slashCommands.js:3056`
- `static/js/slashCommands.js:3253`
- `static/js/slashCommands.js:3266`
- `static/js/slashCommands.js:3273`
- `static/js/slashCommands.js:3277`
- `static/js/slashCommands.js:3281`
- `static/js/slashCommands.js:3285`
- `static/js/slashCommands.js:3712`
- `static/js/slashCommands.js:3721`
- `static/js/slashCommands.js:3724`
- `static/js/slashCommands.js:3727`
- `static/js/slashCommands.js:3730`
- `static/js/slashCommands.js:3733`
- `static/js/slashCommands.js:3749`

## `_cmdTourNotes` — function, line 3756
- **called from:**
- `static/js/slashCommands.js:3756`

## `_makeHalo` — function, line 3810
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 3814
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `tick` — arrow, line 3824
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `_clearHalos` — function, line 3839
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 3844
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 3850
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 3885
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 3913
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_cmdTourBrain` — function, line 3959
- **called from:**
- `static/js/slashCommands.js:3959`

## `_makeHalo` — function, line 4010
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 4014
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `tick` — arrow, line 4024
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `_clearHalos` — function, line 4039
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 4044
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 4050
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 4085
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 4113
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_tab` — arrow, line 4125
- **called from:**
- `static/js/slashCommands.js:4129`
- `static/js/slashCommands.js:4133`
- `static/js/slashCommands.js:4136`
- `static/js/slashCommands.js:4139`

## `_openTasksForTour` — function, line 4160
- **called from:**
- `static/js/slashCommands.js:4160`
- `static/js/slashCommands.js:4207`

## `_runTaskTour` — function, line 4174
- **called from:**
- `static/js/slashCommands.js:4174`
- `static/js/slashCommands.js:4362`
- `static/js/slashCommands.js:4378`

## `clearHalos` — function, line 4219
- **called from:**
- `static/js/slashCommands.js:4219`
- `static/js/slashCommands.js:4259`
- `static/js/slashCommands.js:4282`
- `static/js/slashCommands.js:4325`

## `makeHalo` — function, line 4224
- **called from:**
- `static/js/slashCommands.js:2291`
- `static/js/slashCommands.js:4224`
- `static/js/slashCommands.js:4288`

## `update` — arrow, line 4228
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `tick` — arrow, line 4243
- **called from:**
- `static/js/document.js:10447`
- `static/js/editor/build/transform-popup.js:88`
- `static/js/editor/build/transform-popup.js:92`
- `static/js/editor/build/transform-popup.js:95`
- `static/js/escMenuStack.js:97`
- `static/js/slashCommands.js:2798`

## `clear` — function, line 4258
- **called from:**
- `app.py:334`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email_routes.py:1643`
- `routes/model_routes.py:1394`
- `routes/session_routes.py:832`
- `routes/skills_routes.py:462`
- `scripts/diffusion_server.py:101`
- `services/search/core.py:228`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:126`
- `src/llm_core.py:141`
- `src/llm_core.py:4084`
- `src/task_scheduler.py:441`
- `tests/test_api_token_routes.py:160`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_email_urgency_checkpoint.py:854`
- `tests/test_hwfit_cpu_arch_detection.py:10`
- `tests/test_hwfit_cpu_arch_detection.py:15`
- `tests/test_hwfit_remote_validation.py:79`
- `tests/test_hwfit_remote_validation.py:89`
- `tests/test_hwfit_unified_nvidia.py:113`
- `tests/test_hwfit_unified_nvidia.py:142`
- `tests/test_kimi_code_user_agent.py:63`
- `tests/test_kimi_code_user_agent.py:68`
- `tests/test_kimi_code_user_agent.py:79`
- `tests/test_kimi_code_user_agent.py:94`
- `tests/test_kimi_code_user_agent.py:98`
- `tests/test_kimi_code_user_agent.py:132`
- `tests/test_kimi_code_user_agent.py:136`
- `tests/test_kimi_code_user_agent.py:167`
- `tests/test_kimi_code_user_agent.py:171`
- `tests/test_kimi_code_user_agent.py:212`
- `tests/test_llm_core_async_mistral_content.py:36`
- `tests/test_llm_core_fallback.py:503`
- `tests/test_llm_core_fallback.py:537`
- `tests/test_llm_core_fallback.py:787`
- `tests/test_llm_core_fallback.py:788`
- `tests/test_llm_core_fallback.py:824`
- `tests/test_llm_core_fallback.py:825`
- `tests/test_llm_core_ollama.py:91`
- `tests/test_llm_core_temperature_moonshot.py:59`
- `tests/test_llm_core_temperature_reasoning.py:39`
- `tests/test_lmstudio_vision.py:35`
- `tests/test_lmstudio_vision.py:37`
- `tests/test_lmstudio_vision.py:131`
- `tests/test_lmstudio_vision.py:133`
- `tests/test_mcp_email_decode_header_spaces.py:23`
- `tests/test_mcp_email_decode_header_spaces.py:25`
- `tests/test_mcp_email_decode_header_spaces.py:98`
- `tests/test_mcp_email_decode_header_spaces.py:112`
- `tests/test_mcp_email_decode_header_spaces.py:170`
- … +105 more (grep the name in repo)

## `positionTooltip` — function, line 4263
- **called from:**
- `static/js/slashCommands.js:2214`
- `static/js/slashCommands.js:2358`
- `static/js/slashCommands.js:4263`
- `static/js/slashCommands.js:4298`

## `showStep` — function, line 4280
- **called from:**
- `static/js/slashCommands.js:2316`
- `static/js/slashCommands.js:2531`
- `static/js/slashCommands.js:4280`
- `static/js/slashCommands.js:4318`

## `onClick` — arrow, line 4301
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `onClick` — arrow, line 4344
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_cmdTourTask1` — function, line 4361
- **called from:**
- `static/js/slashCommands.js:4361`

## `_cmdTourTask2` — function, line 4377
- **called from:**
- `static/js/slashCommands.js:4373`
- `static/js/slashCommands.js:4377`

## `_cmdTourResearch` — function, line 4401
- **called from:**
- `static/js/slashCommands.js:4401`

## `_makeHalo` — function, line 4455
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 4459
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `_clearHalos` — function, line 4476
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 4481
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 4488
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 4523
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `onClick` — arrow, line 4550
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_ensureSettingsOpen` — function, line 4561
- **called from:**
- `static/js/slashCommands.js:4561`

## `_cmdTourLibrary` — function, line 4615
- **called from:**
- `static/js/slashCommands.js:4615`

## `_makeHalo` — function, line 4669
- **called from:**
- `static/js/slashCommands.js:2610`
- `static/js/slashCommands.js:2682`
- `static/js/slashCommands.js:2772`
- `static/js/slashCommands.js:2891`
- `static/js/slashCommands.js:2971`
- `static/js/slashCommands.js:3120`
- `static/js/slashCommands.js:3206`
- `static/js/slashCommands.js:3208`
- `static/js/slashCommands.js:3364`
- `static/js/slashCommands.js:3452`
- `static/js/slashCommands.js:3597`
- `static/js/slashCommands.js:3684`
- `static/js/slashCommands.js:3810`
- `static/js/slashCommands.js:3897`
- `static/js/slashCommands.js:4010`
- `static/js/slashCommands.js:4097`
- `static/js/slashCommands.js:4455`
- `static/js/slashCommands.js:4534`
- `static/js/slashCommands.js:4669`
- `static/js/slashCommands.js:4750`

## `update` — arrow, line 4673
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `_clearHalos` — function, line 4690
- **called from:**
- `static/js/slashCommands.js:2633`
- `static/js/slashCommands.js:2641`
- `static/js/slashCommands.js:2679`
- `static/js/slashCommands.js:2761`
- `static/js/slashCommands.js:2912`
- `static/js/slashCommands.js:2919`
- `static/js/slashCommands.js:2967`
- `static/js/slashCommands.js:3141`
- `static/js/slashCommands.js:3148`
- `static/js/slashCommands.js:3201`
- `static/js/slashCommands.js:3394`
- `static/js/slashCommands.js:3400`
- `static/js/slashCommands.js:3447`
- `static/js/slashCommands.js:3626`
- `static/js/slashCommands.js:3632`
- `static/js/slashCommands.js:3679`
- `static/js/slashCommands.js:3839`
- `static/js/slashCommands.js:3845`
- `static/js/slashCommands.js:3892`
- `static/js/slashCommands.js:4039`
- `static/js/slashCommands.js:4045`
- `static/js/slashCommands.js:4092`
- `static/js/slashCommands.js:4476`
- `static/js/slashCommands.js:4483`
- `static/js/slashCommands.js:4530`
- `static/js/slashCommands.js:4690`
- `static/js/slashCommands.js:4697`
- `static/js/slashCommands.js:4746`

## `_clear` — arrow, line 4695
- **called from:**
- `static/js/slashCommands.js:2756`
- `static/js/slashCommands.js:2801`
- `static/js/slashCommands.js:2827`
- `static/js/slashCommands.js:2831`
- `static/js/slashCommands.js:3051`
- `static/js/slashCommands.js:3057`
- `static/js/slashCommands.js:3299`
- `static/js/slashCommands.js:3303`
- `static/js/slashCommands.js:3529`
- `static/js/slashCommands.js:3535`
- `static/js/slashCommands.js:3744`
- `static/js/slashCommands.js:3750`
- `static/js/slashCommands.js:3949`
- `static/js/slashCommands.js:3953`
- `static/js/slashCommands.js:4150`
- `static/js/slashCommands.js:4154`
- `static/js/slashCommands.js:4589`
- `static/js/slashCommands.js:4593`
- `static/js/slashCommands.js:4821`
- `static/js/slashCommands.js:4837`
- `static/js/slashCommands.js:4851`
- `static/js/slashCommands.js:4879`
- `static/js/slashCommands.js:4883`

## `_positionTooltip` — function, line 4702
- **called from:**
- `static/js/slashCommands.js:2646`
- `static/js/slashCommands.js:2697`
- `static/js/slashCommands.js:2773`
- `static/js/slashCommands.js:2924`
- `static/js/slashCommands.js:2983`
- `static/js/slashCommands.js:3153`
- `static/js/slashCommands.js:3220`
- `static/js/slashCommands.js:3405`
- `static/js/slashCommands.js:3464`
- `static/js/slashCommands.js:3637`
- `static/js/slashCommands.js:3696`
- `static/js/slashCommands.js:3850`
- `static/js/slashCommands.js:3909`
- `static/js/slashCommands.js:4050`
- `static/js/slashCommands.js:4109`
- `static/js/slashCommands.js:4488`
- `static/js/slashCommands.js:4546`
- `static/js/slashCommands.js:4702`
- `static/js/slashCommands.js:4762`

## `_showStep` — function, line 4737
- **called from:**
- `static/js/slashCommands.js:2673`
- `static/js/slashCommands.js:2752`
- `static/js/slashCommands.js:2822`
- `static/js/slashCommands.js:2960`
- `static/js/slashCommands.js:3045`
- `static/js/slashCommands.js:3192`
- `static/js/slashCommands.js:3291`
- `static/js/slashCommands.js:3440`
- `static/js/slashCommands.js:3523`
- `static/js/slashCommands.js:3672`
- `static/js/slashCommands.js:3738`
- `static/js/slashCommands.js:3885`
- `static/js/slashCommands.js:3943`
- `static/js/slashCommands.js:4085`
- `static/js/slashCommands.js:4144`
- `static/js/slashCommands.js:4523`
- `static/js/slashCommands.js:4583`
- `static/js/slashCommands.js:4737`
- `static/js/slashCommands.js:4813`
- `static/js/slashCommands.js:4873`

## `cleanup` — arrow, line 4767
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `onClick` — arrow, line 4771
- **called from:**
- `static/js/calendar.js:547`
- `static/js/cookbookServe.js:2705`
- `static/js/cookbookServe.js:2765`
- `static/js/skills.js:401`
- `static/js/tasks.js:1049`

## `_cmdPrompt` — function, line 4890
- **called from:**
- `static/js/slashCommands.js:4890`

## `_ensureSetupSpotlightStyles` — function, line 4921
- **called from:**
- `static/js/slashCommands.js:4921`
- `static/js/slashCommands.js:4953`

## `_visibleSetupTarget` — function, line 4943
- **called from:**
- `static/js/slashCommands.js:4943`
- `static/js/slashCommands.js:4954`

## `_showSetupSpotlight` — function, line 4952
- **called from:**
- `static/js/slashCommands.js:4952`

## `update` — arrow, line 4961
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2729`
- `core/session_manager.py:958`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:670`
- `routes/history/history_routes.py:674`
- … +204 more (grep the name in repo)

## `cleanup` — arrow, line 4976
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5852`
- `static/js/chat.js:7329`
- `static/js/chat.js:7337`
- `static/js/chat.js:7343`
- `static/js/chat.js:7346`
- `static/js/chat.js:7349`
- `static/js/chat.js:7372`
- `static/js/codeRunner.js:262`
- `static/js/codeRunner.js:283`
- `static/js/compare/selector.js:102`
- `static/js/compare/selector.js:877`
- `static/js/compare/selector.js:910`
- `static/js/compare/selector.js:914`
- `static/js/compare/selector.js:963`
- `static/js/compare/selector.js:1257`
- `static/js/compare/selector.js:1282`
- `static/js/compare/selector.js:1295`
- `static/js/cookbookServe.js:1029`
- `static/js/cookbookServe.js:1040`
- `static/js/cookbookServe.js:1041`
- `static/js/cookbookServe.js:1050`
- `static/js/cookbookServe.js:1052`
- `static/js/cookbookServe.js:1057`
- `static/js/document.js:3847`
- `static/js/document.js:3848`
- `static/js/document.js:3849`
- `static/js/document.js:4393`
- `static/js/document.js:4400`
- `static/js/document.js:4442`
- `static/js/dragSort.js:26`
- `static/js/editor/slider-ux.js:179`
- `static/js/editor/slider-ux.js:188`
- `static/js/gallery.js:1665`
- `static/js/gallery.js:1674`
- `static/js/gallery.js:1818`
- `static/js/gallery.js:1830`
- `static/js/gallery.js:1834`
- `static/js/galleryEditor.js:1863`
- `static/js/galleryEditor.js:1952`
- `static/js/galleryEditor.js:1987`
- `static/js/galleryEditor.js:2663`
- `static/js/galleryEditor.js:2664`
- `static/js/galleryEditor.js:2667`
- `static/js/galleryEditor.js:2668`
- `static/js/galleryEditor.js:2670`
- `static/js/galleryEditor.js:3958`
- `static/js/galleryEditor.js:3969`
- `static/js/galleryEditor.js:3971`
- `static/js/galleryEditor.js:3972`
- `static/js/galleryEditor.js:3975`
- `static/js/settings.js:1928`
- `static/js/settings.js:1938`
- `static/js/settings.js:1969`
- `static/js/skills.js:1454`
- `static/js/skills.js:1463`
- `static/js/skills.js:1464`
- … +21 more (grep the name in repo)

## `_runSetupEndpointSpotlight` — function, line 5008
- **called from:**
- `static/js/slashCommands.js:5008`
- `static/js/slashCommands.js:5019`
- `static/js/slashCommands.js:5024`

## `_showSetupEndpointGuide` — function, line 5015
- **called from:**
- `static/js/slashCommands.js:5015`
- `static/js/slashCommands.js:5138`
- `static/js/slashCommands.js:5143`
- `static/js/slashCommands.js:5207`
- `static/js/slashCommands.js:5210`

## `_clearSetupCommandInput` — function, line 5028
- **called from:**
- `static/js/slashCommands.js:5028`
- `static/js/slashCommands.js:5089`

## `_setupProviderDeviceFlow` — function, line 5038
- **called from:**
- `static/js/slashCommands.js:790`
- `static/js/slashCommands.js:5038`
- `static/js/slashCommands.js:5094`

## `_cmdSetup` — function, line 5087
- **called from:**
- `static/js/slashCommands.js:5087`
- `static/js/slashCommands.js:5871`
- `static/js/slashCommands.js:5872`
- `static/js/slashCommands.js:5873`
- `static/js/slashCommands.js:5874`
- `static/js/slashCommands.js:5875`
- `static/js/slashCommands.js:5876`
- `static/js/slashCommands.js:5877`
- `static/js/slashCommands.js:5878`
- `static/js/slashCommands.js:5879`
- `static/js/slashCommands.js:5880`
- `static/js/slashCommands.js:5883`
- `static/js/slashCommands.js:5886`

## `_cmdShortcuts` — function, line 5215
- **called from:**
- `static/js/slashCommands.js:5215`

## `formatCombo` — arrow, line 5234
- **called from:**
- `static/js/slashCommands.js:5243`
- `static/js/slashCommands.js:5244`
- `static/js/slashCommands.js:5245`
- `static/js/slashCommands.js:5246`
- `static/js/slashCommands.js:5247`
- `static/js/slashCommands.js:5248`
- `static/js/slashCommands.js:5249`

## `_eggRender` — function, line 5318
- **called from:**
- `static/js/slashCommands.js:5318`
- `static/js/slashCommands.js:5374`
- `static/js/slashCommands.js:5390`
- `static/js/slashCommands.js:5405`
- `static/js/slashCommands.js:5416`
- `static/js/slashCommands.js:5444`
- `static/js/slashCommands.js:5493`
- `static/js/slashCommands.js:5517`
- `static/js/slashCommands.js:5537`
- `static/js/slashCommands.js:5687`

## `_cmdFlip` — function, line 5334
- **called from:**
- `static/js/slashCommands.js:5334`

## `_cmdRoll` — function, line 5363
- **called from:**
- `static/js/slashCommands.js:5363`

## `_cmd8Ball` — function, line 5383
- **called from:**
- `static/js/slashCommands.js:5383`

## `_cmdFortune` — function, line 5403
- **called from:**
- `static/js/slashCommands.js:5403`

## `_cmdOdyssey` — function, line 5414
- **called from:**
- `static/js/slashCommands.js:5414`

## `_cmdAscii` — function, line 5424
- **called from:**
- `static/js/slashCommands.js:5424`

## `_cmdMatrix` — function, line 5449
- **called from:**
- `static/js/slashCommands.js:5449`

## `_cmdSay` — function, line 5486
- **called from:**
- `static/js/slashCommands.js:5486`

## `_cmdWisdom` — function, line 5498
- **called from:**
- `static/js/slashCommands.js:5498`

## `_cmdUptime` — function, line 5525
- **called from:**
- `static/js/slashCommands.js:5525`

## `_cmdPing` — function, line 5546
- **called from:**
- `static/js/slashCommands.js:5546`

## `_cmdProbe` — function, line 5578
- **called from:**
- `static/js/slashCommands.js:5578`

## `_cmdColor` — function, line 5684
- **called from:**
- `static/js/slashCommands.js:5684`

## `_cmdHelp` — function, line 5699
- **called from:**
- `static/js/slashCommands.js:5699`

## `_makeCtx` — function, line 6212
- **called from:**
- `static/js/slashCommands.js:6212`
- `static/js/slashCommands.js:6285`

## `_buildAliasMap` — function, line 6220
- **called from:**
- `static/js/slashCommands.js:6220`
- `static/js/slashCommands.js:6228`

## `_resolveCommand` — function, line 6231
- **called from:**
- `static/js/slashCommands.js:6231`
- `static/js/slashCommands.js:6296`

## `_resolveSubcommand` — function, line 6236
- **called from:**
- `static/js/slashCommands.js:6236`
- `static/js/slashCommands.js:6347`

## `_levenshtein` — function, line 6246
- **called from:**
- `static/js/slashCommands.js:6246`
- `static/js/slashCommands.js:6269`

## `_fuzzyMatch` — function, line 6262
- **called from:**
- `static/js/slashCommands.js:6262`
- `static/js/slashCommands.js:6397`

## `_isCmd` — function, line 6277
- **called from:**
- `static/js/slashCommands.js:6277`
- `static/js/slashCommands.js:6488`

## `handleSlashCommand` — function, line 6281
- **called from:**
- `static/js/chat.js:1699`
- `static/js/slashCommands.js:6281`
- `static/js/tourAutoplay.js:61`

## `_showUser` — function, line 6289
- **called from:**
- `static/js/slashCommands.js:6289`
- `static/js/slashCommands.js:6307`
- `static/js/slashCommands.js:6316`
- `static/js/slashCommands.js:6328`
- `static/js/slashCommands.js:6391`
- `static/js/slashCommands.js:6399`
- `static/js/slashCommands.js:6405`

## `initSlashCommands` — function, line 6422
- **called from:**
- `static/js/chat.js:1168`
- `static/js/slashCommands.js:6422`

## `isCommand` — function, line 6487
- **called from:**
- `static/js/chat.js:1672`
- `static/js/chat.js:1686`
- `static/js/chat.js:1698`
- `static/js/slashCommands.js:6487`

## `getSetupMode` — function, line 6494
- **called from:**
- `static/js/chat.js:1671`
- `static/js/slashCommands.js:6494`

## `clearSetupMode` — function, line 6501
- **called from:**
- `static/js/chat.js:1674`
- `static/js/chat.js:1687`
- `static/js/slashCommands.js:6501`
