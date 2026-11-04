# `static/js/chatRenderer.js` — definitions & call sites

73 definitions (regex-based, best-effort).
**Exports:** `addMessage`, `appendReportButton`, `applyModelColor`, `buildAttachCards`, `buildFindingsBox`, `buildImageBubble`, `buildRagSourcesBox`, `buildSourcesBox`, `copyMessageText`, `createMsgFooter`, `createUserMsgFooter`, `default`, `displayMetrics`, `getImageCost`, `getModelCost`, `getModelInfo`, `getSessionCost`, `hideWelcomeScreen`, `isCostTrackedEndpoint`, `isLocalEndpoint`, `isSubscriptionEndpoint`, `modelColor`, `modelRouteLabel`, `recordSessionMetricsCost`, `removeAskUserCards`, `renderAskUserCard`, `replyModelPair`, `resetSessionCost`, `roleTimestamp`, `safeDisplayImageSrc`, `safeToolScreenshotSrc`, `sameModelName`, `shortModel`, `showWelcomeScreen`, `stripToolBlocks`, `updateMessageAttachments`, `updateSessionCostUI`

## `_safeHref` — function, line 24
- **called from:**
- `static/js/chatRenderer.js:24`
- `static/js/chatRenderer.js:1134`
- `static/js/chatRenderer.js:1190`

## `safeToolScreenshotSrc` — function, line 33
- **called from:**
- `static/js/chat.js:4169`
- `static/js/chatRenderer.js:33`
- `static/js/chatRenderer.js:2727`

## `safeDisplayImageSrc` — function, line 41
- **called from:**
- `static/js/chatRenderer.js:41`
- `static/js/chatRenderer.js:1445`
- `static/js/compare/stream.js:560`
- `static/js/group.js:922`

## `_makeActionBtn` — function, line 56
- **called from:**
- `static/js/chatRenderer.js:56`
- `static/js/chatRenderer.js:1798`
- `static/js/chatRenderer.js:1970`

## `_attachIcon` — function, line 67
- **called from:**
- `static/js/chatRenderer.js:67`
- `static/js/chatRenderer.js:206`

## `_formatSize` — function, line 78
- **called from:**
- `static/js/chatRenderer.js:78`
- `static/js/chatRenderer.js:215`

## `buildAttachCards` — function, line 87
- **called from:**
- `static/js/chatRenderer.js:87`
- `static/js/chatRenderer.js:232`
- `static/js/chatRenderer.js:2970`

## `_reveal` — arrow, line 140
- **called from:**
- `static/js/chatRenderer.js:152`

## `updateMessageAttachments` — function, line 228
- **called from:**
- `static/js/chat.js:2092`
- `static/js/chatRenderer.js:228`

## `_openImageLightbox` — function, line 239
- **called from:**
- `static/js/chatRenderer.js:105`
- `static/js/chatRenderer.js:239`

## `_onKey` — arrow, line 261
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_close` — arrow, line 262
- **called from:**
- `static/js/chat.js:6178`
- `static/js/chat.js:6186`
- `static/js/chat.js:6194`
- `static/js/chat.js:6197`
- `static/js/chatRenderer.js:261`
- `static/js/document.js:5281`
- `static/js/document.js:5311`
- `static/js/document.js:5318`
- `static/js/document.js:5324`
- `static/js/modelPicker.js:209`
- `static/js/modelPicker.js:232`
- `static/js/modelPicker.js:677`
- `static/js/modelPicker.js:807`
- `static/js/modelPicker.js:845`
- `static/js/settings.js:3778`
- `static/js/settings.js:3787`

## `_closeVisionEditor` — function, line 292
- **called from:**
- `static/js/chatRenderer.js:292`
- `static/js/chatRenderer.js:298`
- `static/js/chatRenderer.js:301`
- `static/js/chatRenderer.js:347`
- `static/js/chatRenderer.js:367`
- `static/js/chatRenderer.js:389`

## `_openVisionEditor` — function, line 296
- **called from:**
- `static/js/chatRenderer.js:172`
- `static/js/chatRenderer.js:296`

## `_saveVisionText` — arrow, line 327
- **called from:**
- `static/js/chatRenderer.js:345`
- `static/js/chatRenderer.js:366`

## `escapeRegex` — function, line 431
- **called from:**
- `static/js/chatRenderer.js:431`

## `stripExecutedFence` — function, line 435
- **called from:**
- `static/js/chatRenderer.js:435`

## `loadExecFenceRegex` — function, line 448
- **called from:**
- `static/js/chatRenderer.js:448`
- `static/js/chatRenderer.js:474`

## `shortModel` — function, line 592
- **called from:**
- `static/js/chatRenderer.js:592`
- `static/js/chatRenderer.js:621`
- `static/js/chatRenderer.js:621`
- `static/js/chatRenderer.js:648`
- `static/js/chatRenderer.js:654`
- `static/js/chatRenderer.js:654`
- `static/js/chatRenderer.js:743`
- `static/js/group.js:736`

## `modelValue` — function, line 611
- **called from:**
- `static/js/chatRenderer.js:611`
- `static/js/chatRenderer.js:617`
- `static/js/chatRenderer.js:618`
- `static/js/chatRenderer.js:625`
- `static/js/chatRenderer.js:638`
- `static/js/chatRenderer.js:639`
- `static/js/chatRenderer.js:640`
- `static/js/chatRenderer.js:641`
- `static/js/chatRenderer.js:659`
- `static/js/chatRenderer.js:660`
- `static/js/chatRenderer.js:662`
- `static/js/chatRenderer.js:673`

## `sameModelName` — function, line 616
- **called from:**
- `static/js/chatRenderer.js:616`
- `static/js/chatRenderer.js:647`
- `static/js/chatRenderer.js:2663`
- `static/js/chatRenderer.js:2849`

## `shortEndpointLabel` — function, line 624
- **called from:**
- `static/js/chatRenderer.js:624`
- `static/js/chatRenderer.js:650`
- `static/js/chatRenderer.js:651`

## `modelRouteLabel` — function, line 630
- **called from:**
- `static/js/chatRenderer.js:630`
- `static/js/chatRenderer.js:2651`
- `static/js/chatRenderer.js:2826`

## `replyModelPair` — function, line 657
- **called from:**
- `static/js/chatRenderer.js:657`
- `static/js/chatRenderer.js:2643`
- `static/js/chatRenderer.js:2824`

## `modelColor` — function, line 689
- **called from:**
- `static/js/chatRenderer.js:689`
- `static/js/chatRenderer.js:717`
- `static/js/cookbookServe.js:1151`
- `static/js/models.js:104`

## `getModelInfo` — function, line 701
- **called from:**
- `static/js/chatRenderer.js:701`
- `static/js/chatRenderer.js:742`

## `_fmtCtx` — function, line 707
- **called from:**
- `static/js/chatRenderer.js:707`
- `static/js/chatRenderer.js:760`
- `static/js/chatRenderer.js:761`
- `static/js/chatRenderer.js:764`
- `static/js/chatRenderer.js:776`
- `static/js/chatRenderer.js:778`

## `applyModelColor` — function, line 715
- **called from:**
- `static/js/chatRenderer.js:715`
- `static/js/chatRenderer.js:2670`
- `static/js/chatRenderer.js:2853`
- `static/js/group.js:739`

## `getModelCost` — function, line 812
- **called from:**
- `static/js/chatRenderer.js:812`
- `static/js/chatRenderer.js:884`
- `static/js/compare/stream.js:761`
- `static/js/compare/vote.js:110`

## `isLocalEndpoint` — function, line 829
- **called from:**
- `static/js/chatRenderer.js:829`
- `static/js/chatRenderer.js:869`

## `isSubscriptionEndpoint` — function, line 851
- **called from:**
- `static/js/chatRenderer.js:851`
- `static/js/chatRenderer.js:869`

## `_currentEndpointUrl` — function, line 863
- **called from:**
- `static/js/chatRenderer.js:863`
- `static/js/chatRenderer.js:879`

## `isCostTrackedEndpoint` — function, line 868
- **called from:**
- `static/js/chatRenderer.js:794`
- `static/js/chatRenderer.js:868`
- `static/js/chatRenderer.js:881`
- `static/js/slashCommands.js:2034`

## `_billableCost` — function, line 873
- **called from:**
- `static/js/chatRenderer.js:873`
- `static/js/chatRenderer.js:891`
- `static/js/chatRenderer.js:903`

## `_metricsBillableCost` — function, line 888
- **called from:**
- `static/js/chatRenderer.js:888`
- `static/js/chatRenderer.js:985`
- `static/js/chatRenderer.js:2051`

## `getImageCost` — function, line 917
- **called from:**
- `static/js/chatRenderer.js:917`
- `static/js/chatRenderer.js:1642`

## `getSessionCost` — function, line 936
- **called from:**
- `static/js/chatRenderer.js:936`
- `static/js/chatRenderer.js:973`
- `static/js/chatRenderer.js:2102`
- `static/js/slashCommands.js:2035`

## `resetSessionCost` — function, line 953
- **called from:**
- `static/js/chatRenderer.js:953`

## `updateSessionCostUI` — function, line 968
- **called from:**
- `static/js/chatRenderer.js:964`
- `static/js/chatRenderer.js:968`
- `static/js/chatRenderer.js:1041`
- `static/js/sessions.js:2053`

## `recordSessionMetricsCost` — function, line 983
- **called from:**
- `static/js/chat.js:3897`
- `static/js/chat.js:3919`
- `static/js/chat.js:5816`
- `static/js/chat.js:5927`
- `static/js/chatRenderer.js:983`
- `static/js/chatRenderer.js:2063`

## `writeCost` — arrow, line 1005
- **called from:**
- `static/js/chatRenderer.js:1047`

## `guardedWrite` — arrow, line 1045
- **called from:**
- `static/js/chatRenderer.js:1058`
- `static/js/chatRenderer.js:1062`
- `static/js/chatRenderer.js:1065`

## `roleTimestamp` — function, line 1073
- **called from:**
- `static/js/chat.js:7074`
- `static/js/chatRenderer.js:1073`
- `static/js/chatRenderer.js:2671`
- `static/js/chatRenderer.js:2854`
- `static/js/chatRenderer.js:3119`

## `stripToolBlocks` — function, line 1090
- **called from:**
- `static/js/chat.js:560`
- `static/js/chatRenderer.js:1090`
- `static/js/chatRenderer.js:1116`
- `static/js/chatRenderer.js:2860`

## `copyMessageText` — function, line 1114
- **called from:**
- `static/js/chatRenderer.js:1114`
- `static/js/chatRenderer.js:1746`
- `static/js/slashCommands.js:407`

## `buildSourcesBox` — function, line 1123
- **called from:**
- `static/js/chatRenderer.js:1123`
- `static/js/chatRenderer.js:2683`
- `static/js/chatRenderer.js:2685`
- `static/js/chatRenderer.js:2898`
- `static/js/chatRenderer.js:2900`

## `buildRagSourcesBox` — function, line 1159
- **called from:**
- `static/js/chatRenderer.js:1159`
- `static/js/chatRenderer.js:2692`
- `static/js/chatRenderer.js:2907`

## `buildFindingsBox` — function, line 1178
- **called from:**
- `static/js/chat.js:4619`
- `static/js/chat.js:4632`
- `static/js/chat.js:7060`
- `static/js/chat.js:7233`
- `static/js/chatRenderer.js:1178`
- `static/js/chatRenderer.js:2688`
- `static/js/chatRenderer.js:2903`

## `appendReportButton` — function, line 1214
- **called from:**
- `static/js/chat.js:527`
- `static/js/chatRenderer.js:1214`

## `_appendContinuePrompt` — function, line 1219
- **called from:**
- `static/js/chatRenderer.js:1216`
- `static/js/chatRenderer.js:1219`

## `_appendReportButton` — function, line 1229
- **called from:**
- `static/js/chatRenderer.js:1215`
- `static/js/chatRenderer.js:1229`
- `static/js/chatRenderer.js:2947`

## `resolveDocumentPlaceholderLinks` — function, line 1312
- **called from:**
- `static/js/chatRenderer.js:1312`
- `static/js/chatRenderer.js:2622`
- `static/js/chatRenderer.js:2862`

## `buildImageBubble` — function, line 1429
- **called from:**
- `static/js/chatRenderer.js:1429`
- `static/js/chatRenderer.js:2768`

## `hideWelcomeScreen` — function, line 1651
- **called from:**
- `static/app.js:1938`
- `static/app.js:2562`
- `static/app.js:3889`
- `static/app.js:3896`
- `static/js/chat.js:7063`
- `static/js/chatRenderer.js:1651`
- `static/js/chatRenderer.js:2565`
- `static/js/sessions.js:75`
- `static/js/sessions.js:3033`

## `showWelcomeScreen` — function, line 1662
- **called from:**
- `static/app.js:858`
- `static/js/chatRenderer.js:1662`
- `static/js/keyboard-shortcuts.js:216`
- `static/js/sessions.js:347`
- `static/js/sessions.js:1901`
- `static/js/sessions.js:2145`
- `static/js/sessions.js:2159`
- `static/js/sessions.js:2357`

## `_hasAdjacentUserPrompt` — function, line 1712
- **called from:**
- `static/js/chatRenderer.js:1712`
- `static/js/chatRenderer.js:1758`

## `createMsgFooter` — function, line 1734
- **called from:**
- `static/js/chat.js:1613`
- `static/js/chat.js:4714`
- `static/js/chat.js:4792`
- `static/js/chat.js:5014`
- `static/js/chat.js:5087`
- `static/js/chat.js:5460`
- `static/js/chat.js:7086`
- `static/js/chatRenderer.js:1734`
- `static/js/chatRenderer.js:2294`
- `static/js/chatRenderer.js:2777`
- `static/js/chatRenderer.js:3115`
- `static/js/group.js:954`

## `handler` — method?, line 1759
- **called from:**
- `tests/test_admin_tools_registry.py:44`
- `tests/test_api_token_routes.py:125`
- `tests/test_contacts_add_null_name.py:37`
- `tests/test_contacts_add_null_name.py:45`
- `tests/test_contacts_add_null_name.py:52`
- `tests/test_contacts_import_nonstring.py:22`
- `tests/test_delete_user_invalidates_token_cache.py:54`
- `tests/test_delete_user_invalidates_token_cache.py:64`
- `tests/test_delete_user_invalidates_token_cache.py:77`
- `tests/test_embeddings_client.py:15`
- `tests/test_hwfit_gpu_count_nonnumeric.py:21`
- `tests/test_hwfit_gpu_count_nonnumeric.py:27`
- `tests/test_hwfit_gpu_count_nonnumeric.py:37`
- `static/app.js:384`
- `static/app.js:3877`
- `static/js/chat.js:4020`
- `static/js/chatRenderer.js:1743`
- `static/js/chatRenderer.js:1750`
- `static/js/chatRenderer.js:1759`
- `static/js/chatRenderer.js:1763`
- `static/js/chatRenderer.js:1770`
- `static/js/chatRenderer.js:1774`
- `static/js/chatRenderer.js:1778`
- `static/js/chatRenderer.js:1782`
- `static/js/chatRenderer.js:1799`
- `static/js/chatRenderer.js:1835`
- `static/js/chatRenderer.js:1943`
- `static/js/chatRenderer.js:1947`
- `static/js/chatRenderer.js:1951`
- `static/js/chatRenderer.js:1958`
- `static/js/chatRenderer.js:1971`
- `static/js/chatRenderer.js:2007`
- `static/js/compare/scoreboard.js:42`
- `static/js/cookbook-hwfit.js:2638`
- `static/js/emailLibrary.js:3042`
- `static/js/emailLibrary.js:7008`
- `static/js/galleryEditor.js:3478`
- `static/js/init.js:109`
- `static/js/markdown.js:232`
- `static/js/slashCommands.js:2503`
- `static/js/slashCommands.js:6313`
- `static/js/slashCommands.js:6322`
- `static/js/slashCommands.js:6358`
- `static/js/slashCommands.js:6367`
- `static/js/slashCommands.js:6382`
- `static/js/windowDrag.js:293`

## `closeMenu` — arrow, line 1825
- **called from:**
- `static/js/calendar.js:554`
- `static/js/calendar.js:559`
- `static/js/chatRenderer.js:1834`
- `static/js/chatRenderer.js:2006`
- `static/js/compare/panes.js:331`
- `static/js/compare/panes.js:573`
- `static/js/cookbookServe.js:2575`
- `static/js/cookbookServe.js:2704`
- `static/js/cookbookServe.js:2742`
- `static/js/cookbookServe.js:2764`
- `static/js/cookbookServe.js:2794`
- `static/js/document.js:6779`
- `static/js/document.js:6783`
- `static/js/document.js:6794`
- `static/js/document.js:6816`

## `closeDetail` — arrow, line 1881
- **called from:**
- `static/js/chatRenderer.js:1897`

## `createUserMsgFooter` — function, line 1935
- **called from:**
- `static/js/chatRenderer.js:1935`
- `static/js/chatRenderer.js:3121`

## `closeMenu` — arrow, line 1997
- **called from:**
- `static/js/calendar.js:554`
- `static/js/calendar.js:559`
- `static/js/chatRenderer.js:1834`
- `static/js/chatRenderer.js:2006`
- `static/js/compare/panes.js:331`
- `static/js/compare/panes.js:573`
- `static/js/cookbookServe.js:2575`
- `static/js/cookbookServe.js:2704`
- `static/js/cookbookServe.js:2742`
- `static/js/cookbookServe.js:2764`
- `static/js/cookbookServe.js:2794`
- `static/js/document.js:6779`
- `static/js/document.js:6783`
- `static/js/document.js:6794`
- `static/js/document.js:6816`

## `displayMetrics` — function, line 2036
- **called from:**
- `static/js/chat.js:3905`
- `static/js/chat.js:3925`
- `static/js/chat.js:4765`
- `static/js/chat.js:5870`
- `static/js/chatRenderer.js:2036`
- `static/js/chatRenderer.js:2778`
- `static/js/chatRenderer.js:3116`

## `fmtNum` — arrow, line 2183
- **called from:**
- `static/js/chatRenderer.js:2193`
- `static/js/chatRenderer.js:2194`
- `static/js/chatRenderer.js:2199`

## `removeAskUserCards` — function, line 2327
- **called from:**
- `static/js/chatRenderer.js:2327`
- `static/js/chatRenderer.js:2386`
- `static/js/chatRenderer.js:2572`

## `_handleAskUserShortcut` — function, line 2338
- **called from:**
- `static/js/chatRenderer.js:2338`

## `renderAskUserCard` — function, line 2375
- **called from:**
- `static/js/chat.js:4282`
- `static/js/chatRenderer.js:2375`
- `static/js/chatRenderer.js:2789`
- `static/js/compare/stream.js:164`

## `emojiText` — arrow, line 2395
- **called from:**
- `static/js/chatRenderer.js:2414`
- `static/js/chatRenderer.js:2477`
- `static/js/chatRenderer.js:2482`

## `send` — arrow, line 2443
- **called from:**
- `tests/test_history_display_model_hydration.py:535`
- `tests/test_history_display_model_hydration.py:542`
- `tests/test_security_regressions.py:1395`
- `static/app.js:153`
- `static/app.js:154`
- `static/app.js:156`
- `static/app.js:159`
- `static/app.js:161`
- `static/app.js:4090`
- `static/js/chat.js:1594`
- `static/js/chat.js:6876`
- `static/js/chatRenderer.js:2510`
- `static/js/chatRenderer.js:2534`
- `static/js/chatRenderer.js:2536`
- `static/js/document.js:2521`

## `submit` — arrow, line 2529
- **called from:**
- `routes/model_routes.py:1509`
- `services/search/core.py:369`
- `src/model_discovery.py:230`
- `src/service_health.py:169`
- `tests/test_auth_config_lock_concurrency.py:75`
- `tests/test_auth_config_lock_concurrency.py:94`
- `tests/test_auth_config_lock_concurrency.py:119`
- `tests/test_auth_config_lock_concurrency.py:145`
- `tests/test_replace_messages_upload_reservations.py:243`
- `tests/test_replace_messages_upload_reservations.py:245`
- `tests/test_upload_handler_atomicity.py:206`
- `tests/test_upload_handler_atomicity.py:209`
- `tests/test_upload_handler_cleanup.py:312`
- `tests/test_upload_handler_cleanup.py:318`
- `tests/test_upload_handler_cleanup.py:346`
- `tests/test_upload_handler_cleanup.py:348`
- `static/js/chat.js:7262`
- `static/js/chatRenderer.js:2543`
- `static/js/document.js:6140`
- `static/js/document.js:6151`

## `addMessage` — function, line 2563
- **called from:**
- `static/app.js:3890`
- `static/js/chat.js:945`
- `static/js/chat.js:1802`
- `static/js/chat.js:1813`
- `static/js/chat.js:2005`
- `static/js/chat.js:5916`
- `static/js/chatRenderer.js:2563`
- `static/js/sessions.js:157`
- `static/js/sessions.js:2146`

## `_renderVariant` — arrow, line 3021
- **called from:**
- `static/js/chatRenderer.js:3028`
- `static/js/chatRenderer.js:3082`

## `switchFn` — arrow, line 3078
- **called from:**
- `static/js/chatRenderer.js:3094`
- `static/js/chatRenderer.js:3095`
- `static/js/chatRenderer.js:3096`
- `static/js/chatRenderer.js:3097`
