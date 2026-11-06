# `static/js/chatRenderer.js` — definitions & call sites

107 definitions (regex-based, best-effort).
**Exports:** `addMessage`, `appendReportButton`, `applyModelColor`, `buildAttachCards`, `buildFindingsBox`, `buildImageBubble`, `buildRagSourcesBox`, `buildSourcesBox`, `copyMessageText`, `createMsgFooter`, `createUserMsgFooter`, `default`, `displayMetrics`, `getImageCost`, `getModelCost`, `getModelInfo`, `getSessionCost`, `getToolActionTarget`, `getToolIcon`, `hideWelcomeScreen`, `isCostTrackedEndpoint`, `isLocalEndpoint`, `isSubscriptionEndpoint`, `modelColor`, `modelRouteLabel`, `recordSessionMetricsCost`, `removeAskUserCards`, `renderAskUserCard`, `renderToolIcon`, `replyModelPair`, `resetSessionCost`, `roleTimestamp`, `safeDisplayImageSrc`, `safeToolScreenshotSrc`, `sameModelName`, `setUserModePill`, `shortModel`, `showWelcomeScreen`, `stripToolBlocks`, `updateMessageAttachments`, `updateSessionCostUI`

## `getToolIcon` — function, line 68
- **called from:**
- `static/js/chatRenderer.js:68`
- `static/js/chatRenderer.js:329`

## `_safeHref` — function, line 85
- **called from:**
- `static/js/chatRenderer.js:85`
- `static/js/chatRenderer.js:333`
- `static/js/chatRenderer.js:1602`
- `static/js/chatRenderer.js:1658`

## `safeToolScreenshotSrc` — function, line 94
- **called from:**
- `static/js/chat.js:435`
- `static/js/chat.js:514`
- `static/js/chat.js:5731`
- `static/js/chatRenderer.js:94`
- `static/js/chatRenderer.js:3413`

## `safeDisplayImageSrc` — function, line 102
- **called from:**
- `static/js/chatRenderer.js:102`
- `static/js/chatRenderer.js:2023`
- `static/js/compare/stream.js:608`
- `static/js/group.js:924`

## `_isPrivateBrowserTool` — function, line 117
- **called from:**
- `static/js/chat.js:380`
- `static/js/chat.js:501`
- `static/js/chat.js:5556`
- `static/js/chat.js:5557`
- `static/js/chat.js:5562`
- `static/js/chat.js:5702`
- `static/js/chat.js:5732`
- `static/js/chatRenderer.js:117`
- `static/js/chatRenderer.js:3414`
- `static/js/chatRenderer.js:3444`

## `_privateBrowserActionLabel` — function, line 126
- **called from:**
- `static/js/chat.js:389`
- `static/js/chat.js:441`
- `static/js/chat.js:486`
- `static/js/chat.js:504`
- `static/js/chatRenderer.js:126`
- `static/js/chatRenderer.js:344`

## `_privateBrowserUrlFromCommand` — function, line 140
- **called from:**
- `static/js/chat.js:403`
- `static/js/chat.js:436`
- `static/js/chat.js:487`
- `static/js/chat.js:505`
- `static/js/chatRenderer.js:140`
- `static/js/chatRenderer.js:339`
- `static/js/chatRenderer.js:3415`

## `_safeExternalToolUrl` — function, line 155
- **called from:**
- `static/js/chat.js:3861`
- `static/js/chat.js:3876`
- `static/js/chat.js:3878`
- `static/js/chat.js:3908`
- `static/js/chatRenderer.js:155`
- `static/js/chatRenderer.js:170`
- `static/js/chatRenderer.js:172`
- `static/js/chatRenderer.js:202`
- `static/js/chatRenderer.js:272`

## `_webFetchUrlFromCommand` — function, line 165
- **called from:**
- `static/js/chat.js:3871`
- `static/js/chat.js:3954`
- `static/js/chatRenderer.js:165`
- `static/js/chatRenderer.js:272`
- `static/js/chatRenderer.js:370`

## `_webSearchQueryFromCommand` — function, line 176
- **called from:**
- `static/js/chat.js:3882`
- `static/js/chat.js:3945`
- `static/js/chatRenderer.js:176`
- `static/js/chatRenderer.js:361`

## `_searxngSearchUrl` — function, line 187
- **called from:**
- `static/js/chat.js:3893`
- `static/js/chatRenderer.js:187`

## `_toolHeaderLinkHtml` — function, line 201
- **called from:**
- `static/js/chat.js:3907`
- `static/js/chat.js:3957`
- `static/js/chatRenderer.js:201`
- `static/js/chatRenderer.js:373`

## `_toolHeaderHashLinkHtml` — function, line 207
- **called from:**
- `static/js/chat.js:3913`
- `static/js/chat.js:3993`
- `static/js/chatRenderer.js:207`
- `static/js/chatRenderer.js:410`

## `_calendarEventUidFromToolData` — function, line 214
- **called from:**
- `static/js/chat.js:3920`
- `static/js/chat.js:3968`
- `static/js/chatRenderer.js:214`
- `static/js/chatRenderer.js:276`
- `static/js/chatRenderer.js:384`

## `_safeToolTargetId` — function, line 224
- **called from:**
- `static/js/chatRenderer.js:224`
- `static/js/chatRenderer.js:231`
- `static/js/chatRenderer.js:243`

## `_hashTargetFromText` — function, line 229
- **called from:**
- `static/js/chatRenderer.js:229`
- `static/js/chatRenderer.js:299`
- `static/js/chatRenderer.js:317`
- `static/js/chatRenderer.js:323`

## `_toolOutputText` — function, line 234
- **called from:**
- `static/js/chatRenderer.js:234`
- `static/js/chatRenderer.js:263`

## `_target` — function, line 242
- **called from:**
- `static/js/chatRenderer.js:242`
- `static/js/chatRenderer.js:255`
- `static/js/chatRenderer.js:277`
- `static/js/chatRenderer.js:296`
- `static/js/chatRenderer.js:300`
- `static/js/chatRenderer.js:303`
- `static/js/chatRenderer.js:307`
- `static/js/chatRenderer.js:311`
- `static/js/chatRenderer.js:317`
- `static/js/chatRenderer.js:320`
- `static/js/chatRenderer.js:323`

## `_emailTarget` — function, line 247
- **called from:**
- `static/js/chatRenderer.js:247`
- `static/js/chatRenderer.js:317`
- `static/js/chatRenderer.js:406`

## `clean` — arrow, line 254
- **called from:**
- `routes/codex_routes.py:362`
- `routes/codex_routes.py:363`
- `routes/codex_routes.py:364`
- `routes/codex_routes.py:365`
- `routes/codex_routes.py:366`
- `routes/codex_routes.py:367`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:294`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:335`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:336`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:300`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:343`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:344`
- `src/visual_report.py:98`
- `static/js/chat.js:3936`
- `static/js/chat.js:3936`
- `static/js/chatRenderer.js:255`
- `static/js/chatRenderer.js:255`
- `static/js/editor/nl-edit.js:203`

## `getToolActionTarget` — function, line 259
- **called from:**
- `static/js/chatRenderer.js:259`
- `static/js/chatRenderer.js:331`

## `renderToolIcon` — function, line 328
- **called from:**
- `static/js/chat.js:5553`
- `static/js/chat.js:5704`
- `static/js/chat.js:7407`
- `static/js/chat.js:7426`
- `static/js/chatRenderer.js:328`
- `static/js/chatRenderer.js:3450`

## `_browserPreviewHtml` — function, line 338
- **called from:**
- `static/js/chatRenderer.js:338`
- `static/js/chatRenderer.js:3417`

## `_renderAssistantBody` — function, line 347
- **called from:**
- `static/js/chatRenderer.js:347`
- `static/js/chatRenderer.js:3658`

## `_toolDisplayInfo` — function, line 355
- **called from:**
- `static/js/chat.js:3939`
- `static/js/chat.js:5551`
- `static/js/chat.js:5701`
- `static/js/chatRenderer.js:355`
- `static/js/chatRenderer.js:3448`

## `_suppressRawToolOutput` — function, line 436
- **called from:**
- `static/js/chat.js:4019`
- `static/js/chat.js:5672`
- `static/js/chatRenderer.js:436`
- `static/js/chatRenderer.js:3410`

## `_makeActionBtn` — function, line 453
- **called from:**
- `static/js/chatRenderer.js:453`
- `static/js/chatRenderer.js:2377`
- `static/js/chatRenderer.js:2555`

## `_attachIcon` — function, line 465
- **called from:**
- `static/js/chatRenderer.js:465`
- `static/js/chatRenderer.js:604`

## `_formatSize` — function, line 476
- **called from:**
- `static/js/chatRenderer.js:476`
- `static/js/chatRenderer.js:613`

## `buildAttachCards` — function, line 485
- **called from:**
- `static/js/chatRenderer.js:485`
- `static/js/chatRenderer.js:630`
- `static/js/chatRenderer.js:3710`

## `_reveal` — arrow, line 538
- **called from:**
- `static/js/chatRenderer.js:550`

## `updateMessageAttachments` — function, line 626
- **called from:**
- `static/js/chat.js:3150`
- `static/js/chatRenderer.js:626`

## `_openImageLightbox` — function, line 637
- **called from:**
- `static/js/chatRenderer.js:503`
- `static/js/chatRenderer.js:637`

## `_onKey` — arrow, line 659
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_close` — arrow, line 660
- **called from:**
- `static/js/chat.js:7858`
- `static/js/chat.js:7866`
- `static/js/chat.js:7874`
- `static/js/chat.js:7877`
- `static/js/chatRenderer.js:659`
- `static/js/document.js:8109`
- `static/js/document.js:8140`
- `static/js/document.js:8147`
- `static/js/document.js:8153`
- `static/js/modelPicker.js:210`
- `static/js/modelPicker.js:233`
- `static/js/modelPicker.js:698`
- `static/js/modelPicker.js:826`
- `static/js/modelPicker.js:864`
- `static/js/settings.js:3493`
- `static/js/settings.js:3502`

## `_closeVisionEditor` — function, line 690
- **called from:**
- `static/js/chatRenderer.js:690`
- `static/js/chatRenderer.js:696`
- `static/js/chatRenderer.js:699`
- `static/js/chatRenderer.js:745`
- `static/js/chatRenderer.js:765`
- `static/js/chatRenderer.js:787`

## `_openVisionEditor` — function, line 694
- **called from:**
- `static/js/chatRenderer.js:570`
- `static/js/chatRenderer.js:694`

## `_saveVisionText` — arrow, line 725
- **called from:**
- `static/js/chatRenderer.js:743`
- `static/js/chatRenderer.js:764`

## `escapeRegex` — function, line 829
- **called from:**
- `static/js/chatRenderer.js:829`

## `stripExecutedFence` — function, line 833
- **called from:**
- `static/js/chatRenderer.js:833`

## `loadExecFenceRegex` — function, line 846
- **called from:**
- `static/js/chatRenderer.js:846`
- `static/js/chatRenderer.js:872`

## `shortModel` — function, line 990
- **called from:**
- `static/js/chatRenderer.js:990`
- `static/js/chatRenderer.js:1019`
- `static/js/chatRenderer.js:1019`
- `static/js/chatRenderer.js:1046`
- `static/js/chatRenderer.js:1052`
- `static/js/chatRenderer.js:1052`
- `static/js/chatRenderer.js:1141`
- `static/js/group.js:736`

## `modelValue` — function, line 1009
- **called from:**
- `static/js/chatRenderer.js:1009`
- `static/js/chatRenderer.js:1015`
- `static/js/chatRenderer.js:1016`
- `static/js/chatRenderer.js:1023`
- `static/js/chatRenderer.js:1036`
- `static/js/chatRenderer.js:1037`
- `static/js/chatRenderer.js:1038`
- `static/js/chatRenderer.js:1039`
- `static/js/chatRenderer.js:1057`
- `static/js/chatRenderer.js:1058`
- `static/js/chatRenderer.js:1060`
- `static/js/chatRenderer.js:1071`

## `sameModelName` — function, line 1014
- **called from:**
- `static/js/chatRenderer.js:1014`
- `static/js/chatRenderer.js:1045`
- `static/js/chatRenderer.js:3349`
- `static/js/chatRenderer.js:3572`

## `shortEndpointLabel` — function, line 1022
- **called from:**
- `static/js/chatRenderer.js:1022`
- `static/js/chatRenderer.js:1048`
- `static/js/chatRenderer.js:1049`

## `modelRouteLabel` — function, line 1028
- **called from:**
- `static/js/chatRenderer.js:1028`
- `static/js/chatRenderer.js:3337`
- `static/js/chatRenderer.js:3545`

## `replyModelPair` — function, line 1055
- **called from:**
- `static/js/chatRenderer.js:1055`
- `static/js/chatRenderer.js:3329`
- `static/js/chatRenderer.js:3543`

## `modelColor` — function, line 1087
- **called from:**
- `static/js/chatRenderer.js:1087`
- `static/js/chatRenderer.js:1115`
- `static/js/cookbookServe.js:1182`
- `static/js/models.js:104`

## `getModelInfo` — function, line 1099
- **called from:**
- `static/js/chatRenderer.js:1099`
- `static/js/chatRenderer.js:1140`

## `_fmtCtx` — function, line 1105
- **called from:**
- `static/js/chatRenderer.js:1105`
- `static/js/chatRenderer.js:1158`
- `static/js/chatRenderer.js:1159`
- `static/js/chatRenderer.js:1162`
- `static/js/chatRenderer.js:1174`
- `static/js/chatRenderer.js:1176`

## `applyModelColor` — function, line 1113
- **called from:**
- `static/js/chatRenderer.js:1113`
- `static/js/chatRenderer.js:3356`
- `static/js/chatRenderer.js:3576`
- `static/js/group.js:739`

## `getModelCost` — function, line 1210
- **called from:**
- `static/js/chatRenderer.js:1210`
- `static/js/chatRenderer.js:1282`
- `static/js/compare/stream.js:820`
- `static/js/compare/vote.js:111`

## `isLocalEndpoint` — function, line 1227
- **called from:**
- `static/js/chatRenderer.js:1227`
- `static/js/chatRenderer.js:1267`

## `isSubscriptionEndpoint` — function, line 1249
- **called from:**
- `static/js/chatRenderer.js:1249`
- `static/js/chatRenderer.js:1267`

## `_currentEndpointUrl` — function, line 1261
- **called from:**
- `static/js/chatRenderer.js:1261`
- `static/js/chatRenderer.js:1277`

## `isCostTrackedEndpoint` — function, line 1266
- **called from:**
- `static/js/chatRenderer.js:1192`
- `static/js/chatRenderer.js:1266`
- `static/js/chatRenderer.js:1279`
- `static/js/slashCommands.js:2038`

## `_billableCost` — function, line 1271
- **called from:**
- `static/js/chatRenderer.js:1271`
- `static/js/chatRenderer.js:1289`
- `static/js/chatRenderer.js:1301`

## `_metricsBillableCost` — function, line 1286
- **called from:**
- `static/js/chatRenderer.js:1286`
- `static/js/chatRenderer.js:1420`
- `static/js/chatRenderer.js:2638`

## `getImageCost` — function, line 1315
- **called from:**
- `static/js/chatRenderer.js:1315`
- `static/js/chatRenderer.js:2220`

## `_readCostLedger` — function, line 1341
- **called from:**
- `static/js/chatRenderer.js:1341`
- `static/js/chatRenderer.js:1352`
- `static/js/chatRenderer.js:1377`
- `static/js/chatRenderer.js:1392`
- `static/js/chatRenderer.js:1455`
- `static/js/chatRenderer.js:1471`

## `_writeCostLedger` — function, line 1347
- **called from:**
- `static/js/chatRenderer.js:1347`
- `static/js/chatRenderer.js:1369`
- `static/js/chatRenderer.js:1394`
- `static/js/chatRenderer.js:1464`
- `static/js/chatRenderer.js:1473`

## `_readCostRunLedger` — function, line 1351
- **called from:**
- `static/js/chatRenderer.js:1351`
- `static/js/chatRenderer.js:1378`
- `static/js/chatRenderer.js:1395`
- `static/js/chatRenderer.js:1446`

## `_writeCostRunLedger` — function, line 1364
- **called from:**
- `static/js/chatRenderer.js:1364`
- `static/js/chatRenderer.js:1397`
- `static/js/chatRenderer.js:1467`

## `getSessionCost` — function, line 1373
- **called from:**
- `static/js/chatRenderer.js:1373`
- `static/js/chatRenderer.js:1408`
- `static/js/chatRenderer.js:2696`
- `static/js/slashCommands.js:2039`

## `resetSessionCost` — function, line 1388
- **called from:**
- `static/js/chatRenderer.js:1388`

## `updateSessionCostUI` — function, line 1403
- **called from:**
- `static/js/chatRenderer.js:1399`
- `static/js/chatRenderer.js:1403`
- `static/js/chatRenderer.js:1479`
- `static/js/sessions.js:2400`

## `recordSessionMetricsCost` — function, line 1418
- **called from:**
- `static/js/chat.js:5415`
- `static/js/chat.js:5438`
- `static/js/chat.js:7507`
- `static/js/chatRenderer.js:1418`
- `static/js/chatRenderer.js:2650`

## `writeCost` — arrow, line 1443
- **called from:**
- `static/js/chatRenderer.js:1485`

## `guardedWrite` — arrow, line 1483
- **called from:**
- `static/js/chatRenderer.js:1496`
- `static/js/chatRenderer.js:1500`
- `static/js/chatRenderer.js:1503`

## `roleTimestamp` — function, line 1511
- **called from:**
- `static/js/chat.js:8768`
- `static/js/chatRenderer.js:1511`
- `static/js/chatRenderer.js:3357`
- `static/js/chatRenderer.js:3577`
- `static/js/chatRenderer.js:3859`

## `userModePill` — function, line 1525
- **called from:**
- `static/js/chatRenderer.js:1525`
- `static/js/chatRenderer.js:1548`
- `static/js/chatRenderer.js:3563`

## `setUserModePill` — function, line 1543
- **called from:**
- `static/js/chat.js:4726`
- `static/js/chatRenderer.js:1543`

## `stripToolBlocks` — function, line 1558
- **called from:**
- `static/js/chat.js:1440`
- `static/js/chatRenderer.js:1558`
- `static/js/chatRenderer.js:1584`
- `static/js/chatRenderer.js:3583`

## `copyMessageText` — function, line 1582
- **called from:**
- `static/js/chatRenderer.js:1582`
- `static/js/chatRenderer.js:2325`
- `static/js/slashCommands.js:407`

## `buildSourcesBox` — function, line 1591
- **called from:**
- `static/js/chat.js:7651`
- `static/js/chatRenderer.js:1591`
- `static/js/chatRenderer.js:3369`
- `static/js/chatRenderer.js:3371`
- `static/js/chatRenderer.js:3621`
- `static/js/chatRenderer.js:3623`

## `buildRagSourcesBox` — function, line 1627
- **called from:**
- `static/js/chat.js:7655`
- `static/js/chatRenderer.js:1627`
- `static/js/chatRenderer.js:3378`
- `static/js/chatRenderer.js:3630`

## `buildFindingsBox` — function, line 1646
- **called from:**
- `static/js/chat.js:3705`
- `static/js/chat.js:6215`
- `static/js/chat.js:6228`
- `static/js/chat.js:7652`
- `static/js/chat.js:8754`
- `static/js/chat.js:8925`
- `static/js/chatRenderer.js:1646`
- `static/js/chatRenderer.js:3374`
- `static/js/chatRenderer.js:3626`

## `appendReportButton` — function, line 1682
- **called from:**
- `static/js/chat.js:1407`
- `static/js/chatRenderer.js:1682`

## `_appendContinuePrompt` — function, line 1687
- **called from:**
- `static/js/chatRenderer.js:1684`
- `static/js/chatRenderer.js:1687`

## `_appendReportButton` — function, line 1697
- **called from:**
- `static/js/chatRenderer.js:1683`
- `static/js/chatRenderer.js:1697`
- `static/js/chatRenderer.js:3672`

## `resolveDocumentPlaceholderLinks` — function, line 1780
- **called from:**
- `static/js/chatRenderer.js:1780`
- `static/js/chatRenderer.js:3308`
- `static/js/chatRenderer.js:3585`

## `_activateEntityAnchor` — function, line 1799
- **called from:**
- `static/js/chatRenderer.js:1799`
- `static/js/chatRenderer.js:1984`
- `static/js/chatRenderer.js:2001`

## `fallback` — arrow, line 1866
- **called from:**
- `static/js/chat.js:6354`
- `static/js/chatRenderer.js:1881`
- `static/js/chatRenderer.js:1883`
- `static/js/cookbook.js:1281`
- `static/js/document.js:17487`
- `static/js/galleryEditor.js:4553`
- `static/js/galleryEditor.js:4559`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4575`
- `static/js/langIcons.js:149`
- `static/js/slashCommands.js:3265`
- `static/js/tasks.js:470`
- `static/js/tasks.js:472`

## `_isEntityHref` — arrow, line 1970
- **called from:**
- `static/js/chatRenderer.js:1974`

## `buildImageBubble` — function, line 2007
- **called from:**
- `static/js/chatRenderer.js:2007`
- `static/js/chatRenderer.js:3464`

## `hideWelcomeScreen` — function, line 2229
- **called from:**
- `static/app.js:1996`
- `static/app.js:2618`
- `static/app.js:3992`
- `static/app.js:3999`
- `static/js/chat.js:8757`
- `static/js/chatRenderer.js:2229`
- `static/js/chatRenderer.js:3215`
- `static/js/sessions.js:214`
- `static/js/sessions.js:3454`

## `showWelcomeScreen` — function, line 2240
- **called from:**
- `static/app.js:891`
- `static/js/chatRenderer.js:2240`
- `static/js/keyboard-shortcuts.js:217`
- `static/js/sessions.js:536`
- `static/js/sessions.js:2240`
- `static/js/sessions.js:2492`
- `static/js/sessions.js:2506`
- `static/js/sessions.js:2715`

## `_hasAdjacentUserPrompt` — function, line 2290
- **called from:**
- `static/js/chatRenderer.js:2290`
- `static/js/chatRenderer.js:2337`

## `createMsgFooter` — function, line 2312
- **called from:**
- `static/js/chat.js:2638`
- `static/js/chat.js:6309`
- `static/js/chat.js:6385`
- `static/js/chat.js:6629`
- `static/js/chat.js:6724`
- `static/js/chat.js:7121`
- `static/js/chat.js:7647`
- `static/js/chat.js:8777`
- `static/js/chatRenderer.js:2312`
- `static/js/chatRenderer.js:2908`
- `static/js/chatRenderer.js:3474`
- `static/js/chatRenderer.js:3855`
- `static/js/group.js:956`

## `handler` — method?, line 2338
- **called from:**
- `tests/process_resource_helpers.py:74`
- `tests/process_resource_helpers.py:83`
- `tests/test_admin_tools_registry.py:44`
- `tests/test_api_token_routes.py:125`
- `tests/test_contacts_add_null_name.py:44`
- `tests/test_contacts_add_null_name.py:52`
- `tests/test_contacts_add_null_name.py:59`
- `tests/test_contacts_import_nonstring.py:22`
- `tests/test_delete_user_invalidates_token_cache.py:56`
- `tests/test_delete_user_invalidates_token_cache.py:66`
- `tests/test_delete_user_invalidates_token_cache.py:76`
- `tests/test_embeddings_client.py:15`
- `tests/test_hwfit_gpu_count_nonnumeric.py:75`
- `tests/test_hwfit_gpu_count_nonnumeric.py:86`
- `tests/test_hwfit_gpu_count_nonnumeric.py:101`
- `static/app.js:402`
- `static/app.js:3980`
- `static/js/chat.js:5559`
- `static/js/chatRenderer.js:2322`
- `static/js/chatRenderer.js:2329`
- `static/js/chatRenderer.js:2338`
- `static/js/chatRenderer.js:2342`
- `static/js/chatRenderer.js:2349`
- `static/js/chatRenderer.js:2353`
- `static/js/chatRenderer.js:2357`
- `static/js/chatRenderer.js:2361`
- `static/js/chatRenderer.js:2378`
- `static/js/chatRenderer.js:2415`
- `static/js/chatRenderer.js:2528`
- `static/js/chatRenderer.js:2532`
- `static/js/chatRenderer.js:2536`
- `static/js/chatRenderer.js:2543`
- `static/js/chatRenderer.js:2556`
- `static/js/chatRenderer.js:2593`
- `static/js/compare/scoreboard.js:42`
- `static/js/cookbook-hwfit.js:2750`
- `static/js/editor/wire-extra-menus.js:131`
- `static/js/emailLibrary/index.js:2947`
- `static/js/emailLibrary/reader.js:134`
- `static/js/galleryEditor.js:11724`
- `static/js/init.js:122`
- `static/js/markdown.js:416`
- `static/js/slashCommands.js:2507`
- `static/js/slashCommands.js:6345`
- `static/js/slashCommands.js:6354`
- `static/js/slashCommands.js:6390`
- `static/js/slashCommands.js:6399`
- `static/js/slashCommands.js:6414`
- `static/js/windowDrag.js:311`

## `closeMenu` — arrow, line 2405
- **called from:**
- `static/js/calendar.js:643`
- `static/js/calendar.js:648`
- `static/js/chatRenderer.js:2414`
- `static/js/chatRenderer.js:2592`
- `static/js/compare/panes.js:674`
- `static/js/compare/panes.js:923`
- `static/js/cookbookServe.js:2647`
- `static/js/cookbookServe.js:2776`
- `static/js/cookbookServe.js:2814`
- `static/js/cookbookServe.js:2836`
- `static/js/cookbookServe.js:2866`
- `static/js/document.js:11730`
- `static/js/document.js:11734`
- `static/js/document.js:11745`
- `static/js/document.js:11767`
- `static/js/editor/wire-selection-controls.js:302`
- `static/js/editor/wire-selection-controls.js:305`

## `closeDetail` — arrow, line 2461
- **called from:**
- `static/js/chatRenderer.js:2477`

## `createUserMsgFooter` — function, line 2520
- **called from:**
- `static/js/chatRenderer.js:2520`
- `static/js/chatRenderer.js:3861`

## `closeMenu` — arrow, line 2583
- **called from:**
- `static/js/calendar.js:643`
- `static/js/calendar.js:648`
- `static/js/chatRenderer.js:2414`
- `static/js/chatRenderer.js:2592`
- `static/js/compare/panes.js:674`
- `static/js/compare/panes.js:923`
- `static/js/cookbookServe.js:2647`
- `static/js/cookbookServe.js:2776`
- `static/js/cookbookServe.js:2814`
- `static/js/cookbookServe.js:2836`
- `static/js/cookbookServe.js:2866`
- `static/js/document.js:11730`
- `static/js/document.js:11734`
- `static/js/document.js:11745`
- `static/js/document.js:11767`
- `static/js/editor/wire-selection-controls.js:302`
- `static/js/editor/wire-selection-controls.js:305`

## `displayMetrics` — function, line 2622
- **called from:**
- `static/js/chat.js:5423`
- `static/js/chat.js:5444`
- `static/js/chat.js:6360`
- `static/js/chat.js:7562`
- `static/js/chat.js:7658`
- `static/js/chatRenderer.js:2622`
- `static/js/chatRenderer.js:3475`
- `static/js/chatRenderer.js:3856`

## `fmtNum` — arrow, line 2797
- **called from:**
- `static/js/chatRenderer.js:2807`
- `static/js/chatRenderer.js:2808`
- `static/js/chatRenderer.js:2813`

## `removeAskUserCards` — function, line 2943
- **called from:**
- `static/js/chatRenderer.js:2943`
- `static/js/chatRenderer.js:3041`

## `_markAskUserAnswered` — function, line 2958
- **called from:**
- `static/js/chatRenderer.js:2958`
- `static/js/chatRenderer.js:2983`
- `static/js/chatRenderer.js:3090`
- `static/js/chatRenderer.js:3093`
- `static/js/chatRenderer.js:3141`
- `static/js/chatRenderer.js:3143`

## `_answerAskUserCards` — function, line 2980
- **called from:**
- `static/js/chatRenderer.js:2980`
- `static/js/chatRenderer.js:3223`

## `_handleAskUserShortcut` — function, line 2993
- **called from:**
- `static/js/chatRenderer.js:2993`

## `renderAskUserCard` — function, line 3030
- **called from:**
- `static/js/chat.js:5864`
- `static/js/chatRenderer.js:3030`
- `static/js/chatRenderer.js:3486`
- `static/js/compare/stream.js:220`

## `emojiText` — arrow, line 3050
- **called from:**
- `static/js/chatRenderer.js:3055`
- `static/js/chatRenderer.js:3114`
- `static/js/chatRenderer.js:3119`

## `send` — arrow, line 3080
- **called from:**
- `src/process_lifecycle.py:478`
- `src/process_lifecycle.py:516`
- `tests/test_history_display_model_hydration.py:539`
- `tests/test_history_display_model_hydration.py:546`
- `tests/test_security_regressions.py:1397`
- `static/app.js:160`
- `static/app.js:161`
- `static/app.js:163`
- `static/app.js:166`
- `static/app.js:168`
- `static/app.js:4199`
- `static/js/chat.js:2615`
- `static/js/chat.js:8582`
- `static/js/chatRenderer.js:3147`
- `static/js/chatRenderer.js:3172`
- `static/js/chatRenderer.js:3174`
- `static/js/document.js:3663`

## `submit` — arrow, line 3167
- **called from:**
- `mcp_servers/email_server.py:1997`
- `routes/model_routes.py:1637`
- `scripts/audit_sft_corpus_with_deepseek.py:310`
- `scripts/cook_sft_alex_conversations.py:270`
- `scripts/generate_sft_environment_expansion.py:348`
- `scripts/generate_sft_flow_variants_with_kimi.py:166`
- `scripts/judge_seeded_harness_replay.py:164`
- `scripts/odysseus_conversation_qa.py:1273`
- `scripts/repair_sft_corpus_with_kimi.py:214`
- `services/search/core.py:1169`
- `src/model_discovery.py:233`
- `src/service_health.py:183`
- `tests/test_auth_config_lock_concurrency.py:75`
- `tests/test_auth_config_lock_concurrency.py:94`
- `tests/test_auth_config_lock_concurrency.py:119`
- `tests/test_auth_config_lock_concurrency.py:145`
- `tests/test_auth_config_lock_concurrency.py:240`
- `tests/test_auth_config_lock_concurrency.py:241`
- `tests/test_replace_messages_upload_reservations.py:243`
- `tests/test_replace_messages_upload_reservations.py:245`
- `tests/test_spec_router_request_scope.py:42`
- `tests/test_spec_router_request_scope.py:43`
- `tests/test_upload_handler_atomicity.py:206`
- `tests/test_upload_handler_atomicity.py:209`
- `tests/test_upload_handler_cleanup.py:312`
- `tests/test_upload_handler_cleanup.py:318`
- `tests/test_upload_handler_cleanup.py:346`
- `tests/test_upload_handler_cleanup.py:348`
- `tests/test_worker_runtime.py:108`
- `static/js/chat.js:8954`
- `static/js/chatRenderer.js:3181`
- `static/js/document.js:9393`
- `static/js/document.js:9416`
- `static/js/document.js:9452`
- `static/js/document.js:9459`
- `static/js/document.js:9490`
- `static/js/document.js:9497`

## `addMessage` — function, line 3213
- **called from:**
- `static/app.js:3832`
- `static/app.js:3993`
- `static/js/backgroundToolJobs.js:119`
- `static/js/chat.js:1825`
- `static/js/chat.js:2827`
- `static/js/chat.js:2838`
- `static/js/chat.js:3063`
- `static/js/chatRenderer.js:3213`
- `static/js/sessions.js:296`
- `static/js/sessions.js:2493`

## `_renderVariant` — arrow, line 3761
- **called from:**
- `static/js/chatRenderer.js:3768`
- `static/js/chatRenderer.js:3822`

## `switchFn` — arrow, line 3818
- **called from:**
- `static/js/chatRenderer.js:3834`
- `static/js/chatRenderer.js:3835`
- `static/js/chatRenderer.js:3836`
- `static/js/chatRenderer.js:3837`
