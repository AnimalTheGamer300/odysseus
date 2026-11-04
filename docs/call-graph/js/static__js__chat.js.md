# `static/js/chat.js` — definitions & call sites

186 definitions (regex-based, best-effort).
**Exports:** `abortCurrentRequest`, `checkBackgroundStream`, `checkPendingResearch`, `compactCurrentChatContext`, `continueFrom`, `continueFromBubble`, `default`, `deleteMessage`, `detachCurrentStream`, `editAIMessage`, `editUserMessage`, `forkFrom`, `handleChatSubmit`, `init`, `initListeners`, `queueStreamingComposerRequest`, `refreshChatContextHeader`, `regenerateFrom`, `resendUserMessage`, `resumeStream`, `rewriteWith`, `setContinuePrefill`, `setDisplayOverride`, `setHideUserBubble`, `setPendingContinue`

## `_submitToolApprovalWhenIdle` — function, line 67
- **called from:**
- `static/js/chat.js:67`
- `static/js/chat.js:73`
- `static/js/chat.js:93`

## `_fmtContextNumber` — function, line 96
- **called from:**
- `static/js/chat.js:96`
- `static/js/chat.js:199`
- `static/js/chat.js:199`
- `static/js/chat.js:313`
- `static/js/chat.js:313`

## `_contextColorClass` — function, line 101
- **called from:**
- `static/js/chat.js:101`
- `static/js/chat.js:180`
- `static/js/chat.js:315`

## `_contextRingColor` — function, line 108
- **called from:**
- `static/js/chat.js:108`
- `static/js/chat.js:133`
- `static/js/chat.js:142`

## `_contextRingMarkup` — function, line 115
- **called from:**
- `static/js/chat.js:115`
- `static/js/chat.js:134`
- `static/js/chat.js:145`

## `_renderContextHeaderRing` — function, line 131
- **called from:**
- `static/js/chat.js:131`
- `static/js/chat.js:311`

## `_renderCompactMenuContextIcon` — function, line 137
- **called from:**
- `static/js/chat.js:137`
- `static/js/chat.js:312`

## `_liveSessionModule` — function, line 148
- **called from:**
- `static/js/chat.js:148`
- `static/js/chat.js:266`
- `static/js/chat.js:291`
- `static/js/chat.js:307`

## `_closeContextHeaderPopup` — function, line 154
- **called from:**
- `static/js/chat.js:154`
- `static/js/chat.js:175`
- `static/js/chat.js:247`
- `static/js/chat.js:276`
- `static/js/chat.js:297`
- `static/js/chat.js:319`
- `static/js/chat.js:327`

## `_positionContextHeaderPopup` — function, line 160
- **called from:**
- `static/js/chat.js:160`
- `static/js/chat.js:242`

## `_showContextHeaderPopup` — function, line 171
- **called from:**
- `static/js/chat.js:171`
- `static/js/chat.js:261`
- `static/js/chat.js:320`

## `close` — arrow, line 244
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

## `_bindContextHeaderPill` — function, line 253
- **called from:**
- `static/js/chat.js:253`
- `static/js/chat.js:288`

## `compactCurrentChatContext` — function, line 265
- **called from:**
- `static/app.js:506`
- `static/js/chat.js:232`
- `static/js/chat.js:265`

## `refreshChatContextHeader` — function, line 287
- **called from:**
- `static/js/chat.js:278`
- `static/js/chat.js:287`
- `static/js/chat.js:3926`
- `static/js/modelPicker.js:726`
- `static/js/sessions.js:2050`
- `static/js/sessions.js:2362`
- `static/js/sessions.js:2452`

## `_setForegroundChatBusy` — function, line 333
- **called from:**
- `static/js/chat.js:333`
- `static/js/chat.js:1012`
- `static/js/chat.js:1246`
- `static/js/chat.js:1254`
- `static/js/chat.js:1638`

## `_createChatSendPerf` — function, line 345
- **called from:**
- `static/js/chat.js:345`
- `static/js/chat.js:1635`

## `now` — arrow, line 350
- **called from:**
- `app.py:957`
- `app.py:1252`
- `core/database.py:25`
- `core/database.py:216`
- `core/database.py:216`
- `core/session_manager.py:422`
- `core/session_manager.py:562`
- `core/session_manager.py:727`
- `core/session_manager.py:738`
- `core/session_manager.py:809`
- `core/session_manager.py:1022`
- `core/session_manager.py:1050`
- `core/session_manager.py:1051`
- `core/session_manager.py:1225`
- `core/session_manager.py:1245`
- `core/session_manager.py:1262`
- `routes/backup_routes.py:46`
- `routes/backup_routes.py:56`
- `routes/calendar_routes.py:401`
- `routes/calendar_routes.py:525`
- `routes/document/document_routes.py:657`
- `routes/document/document_routes.py:875`
- `routes/email_routes.py:4314`
- `routes/history/history_routes.py:546`
- `routes/history/history_routes.py:839`
- `routes/history/history_routes.py:1056`
- `routes/history/history_routes.py:1180`
- `routes/history/history_routes.py:1201`
- `routes/history/history_routes.py:1225`
- `routes/note/note_routes.py:192`
- `routes/note/note_routes.py:554`
- `routes/session_routes.py:1035`
- `routes/session_routes.py:1043`
- `routes/session_routes.py:1094`
- `routes/task/task_routes.py:104`
- `routes/task/task_routes.py:1107`
- `scripts/agent_migration_manifest.py:47`
- `scripts/demo_email/seed_demo_emails.py:100`
- `scripts/demo_email/seed_demo_emails.py:116`
- `scripts/demo_email/seed_demo_emails.py:212`
- `scripts/demo_email/seed_demo_emails.py:212`
- `scripts/demo_email/seed_demo_emails.py:272`
- `scripts/pr_blocker_audit.py:524`
- `services/memory/skill_format.py:483`
- `services/search/cache.py:42`
- `services/search/content.py:367`
- `services/search/content.py:603`
- `services/search/content.py:606`
- `services/search/core.py:155`
- `services/search/core.py:198`
- `services/search/core.py:200`
- `services/search/core.py:206`
- `services/search/ranking.py:17`
- `src/agent_loop.py:5130`
- `src/agent_loop.py:6408`
- `src/agent_tools/document_tools.py:793`
- `src/agent_tools/session_tools.py:127`
- `src/agent_tools/spawn_agent_tools.py:171`
- `src/builtin_actions.py:1792`
- `src/builtin_actions.py:2170`
- … +303 more (grep the name in repo)

## `mark` — method?, line 352
- **called from:**
- `static/js/chat.js:352`
- `static/js/chat.js:1748`
- `static/js/chat.js:1750`
- `static/js/chat.js:1778`
- `static/js/chat.js:1781`
- `static/js/chat.js:1793`
- `static/js/chat.js:1795`
- `static/js/chat.js:1797`
- `static/js/chat.js:2012`
- `static/js/chat.js:2049`
- `static/js/chat.js:2051`
- `static/js/chat.js:2054`
- `static/js/chat.js:2162`
- `static/js/chat.js:2166`
- `static/js/chat.js:2184`
- `static/js/chat.js:2256`
- `static/js/chat.js:2258`
- `static/js/chat.js:2260`
- `static/js/chat.js:2509`
- `static/js/chat.js:2516`
- `static/js/chat.js:2565`

## `report` — method?, line 357
- **called from:**
- `static/js/chat.js:357`
- `static/js/chat.js:2517`
- `static/js/chat.js:2566`

## `_hashSessionCandidate` — function, line 389
- **called from:**
- `static/js/chat.js:389`
- `static/js/chat.js:418`

## `_adoptOpenedSessionBeforeAutoCreate` — function, line 400
- **called from:**
- `static/app.js:845`
- `static/app.js:3333`
- `static/js/chat.js:400`
- `static/js/chat.js:1712`

## `_setRoleModelLabel` — function, line 449
- **called from:**
- `static/js/chat.js:449`
- `static/js/chat.js:3694`
- `static/js/chat.js:3722`
- `static/js/chat.js:3775`
- `static/js/chat.js:4502`
- `static/js/chat.js:5825`
- `static/js/chat.js:5847`

## `_bestKnownStreamModel` — function, line 482
- **called from:**
- `static/js/chat.js:482`
- `static/js/chat.js:2436`

## `_clearResearchTimer` — function, line 509
- **called from:**
- `static/js/chat.js:509`
- `static/js/chat.js:1510`
- `static/js/chat.js:3610`
- `static/js/chat.js:3632`
- `static/js/chat.js:5167`
- `static/js/chat.js:7189`
- `static/js/chat.js:7203`
- `static/js/chat.js:7219`

## `_appendViewReportLink` — function, line 525
- **called from:**
- `static/js/chat.js:525`
- `static/js/chat.js:4721`
- `static/js/chat.js:7087`
- `static/js/chat.js:7238`

## `_stripDocumentFenceForChat` — function, line 530
- **called from:**
- `static/js/chat.js:530`
- `static/js/chat.js:560`

## `_stripIncompleteRawToolJsonForChat` — function, line 543
- **called from:**
- `static/js/chat.js:543`
- `static/js/chat.js:560`

## `_streamDisplayText` — function, line 559
- **called from:**
- `static/js/chat.js:559`
- `static/js/chat.js:741`
- `static/js/chat.js:2775`
- `static/js/chat.js:2783`
- `static/js/chat.js:2984`
- `static/js/chat.js:3035`
- `static/js/chat.js:3095`
- `static/js/chat.js:4555`
- `static/js/chat.js:4663`
- `static/js/chat.js:4667`
- `static/js/chat.js:5694`

## `_showDocumentWritingStatus` — function, line 563
- **called from:**
- `static/js/chat.js:563`
- `static/js/chat.js:3123`
- `static/js/chat.js:5696`

## `_finishDocumentWritingStatus` — function, line 614
- **called from:**
- `static/js/chat.js:614`
- `static/js/chat.js:4550`
- `static/js/chat.js:5890`

## `_tabSyncPost` — function, line 675
- **called from:**
- `static/js/chat.js:675`
- `static/js/chat.js:686`
- `static/js/chat.js:2011`
- `static/js/chat.js:3218`
- `static/js/chat.js:3960`
- `static/js/chat.js:4815`
- `static/js/chat.js:4915`
- `static/js/chat.js:4935`
- `static/js/chat.js:4955`
- `static/js/chat.js:4974`
- `static/js/chat.js:5021`
- `static/js/chat.js:5363`
- `static/js/chat.js:5918`
- `static/js/chat.js:5931`
- `static/js/chat.js:6562`
- `static/js/chat.js:7422`
- `static/js/chat.js:7523`

## `_tabSyncPostDelta` — function, line 682
- **called from:**
- `static/js/chat.js:682`
- `static/js/chat.js:3336`
- `static/js/chat.js:5791`

## `_tabSyncCurrentSession` — function, line 690
- **called from:**
- `static/js/chat.js:690`
- `static/js/chat.js:796`
- `static/js/chat.js:816`
- `static/js/chat.js:829`
- `static/js/chat.js:860`
- `static/js/chat.js:868`
- `static/js/chat.js:933`
- `static/js/chat.js:952`
- `static/js/chat.js:957`
- `static/js/chat.js:962`
- `static/js/chat.js:967`
- `static/js/chat.js:972`
- `static/js/chat.js:977`

## `_tabSyncEnsureBubble` — function, line 696
- **called from:**
- `static/js/chat.js:696`
- `static/js/chat.js:752`
- `static/js/chat.js:948`

## `_tabSyncRenderDelta` — function, line 729
- **called from:**
- `static/js/chat.js:729`
- `static/js/chat.js:761`

## `_tabSyncQueueDelta` — function, line 751
- **called from:**
- `static/js/chat.js:751`
- `static/js/chat.js:953`

## `_tabSyncClearMirror` — function, line 765
- **called from:**
- `static/js/chat.js:765`
- `static/js/chat.js:784`
- `static/js/chat.js:835`
- `static/js/chat.js:940`
- `static/js/chat.js:5610`

## `_tabSyncReloadSession` — function, line 783
- **called from:**
- `static/js/chat.js:783`
- `static/js/chat.js:798`
- `static/js/chat.js:840`
- `static/js/chat.js:873`

## `_tabSyncScheduleReload` — function, line 792
- **called from:**
- `static/js/chat.js:792`
- `static/js/chat.js:958`
- `static/js/chat.js:978`

## `_tabSyncScheduleTakeover` — function, line 805
- **called from:**
- `static/js/chat.js:805`
- `static/js/chat.js:963`

## `_tabSyncTakeover` — function, line 815
- **called from:**
- `static/js/chat.js:810`
- `static/js/chat.js:815`
- `static/js/chat.js:871`

## `_tabSyncStaleSweep` — function, line 850
- **called from:**
- `static/js/chat.js:850`

## `_tabSyncStampUserBubble` — function, line 884
- **called from:**
- `static/js/chat.js:884`
- `static/js/chat.js:973`

## `_tabSyncApplyDelete` — function, line 893
- **called from:**
- `static/js/chat.js:893`
- `static/js/chat.js:968`

## `_initTabSync` — function, line 921
- **called from:**
- `static/js/chat.js:921`
- `static/js/chat.js:1168`

## `hasActiveStream` — function, line 993
- **called from:**
- `static/js/chat.js:797`
- `static/js/chat.js:817`
- `static/js/chat.js:830`
- `static/js/chat.js:855`
- `static/js/chat.js:869`
- `static/js/chat.js:933`
- `static/js/chat.js:952`
- `static/js/chat.js:957`
- `static/js/chat.js:962`
- `static/js/chat.js:977`
- `static/js/chat.js:993`
- `static/js/chat.js:5397`
- `static/js/chat.js:5583`
- `static/js/sessions.js:2806`

## `_getForegroundStreamState` — function, line 998
- **called from:**
- `static/js/chat.js:998`
- `static/js/chat.js:1008`
- `static/js/chat.js:1169`
- `static/js/chat.js:1558`
- `static/js/chat.js:5248`
- `static/js/chat.js:5339`
- `static/js/chat.js:5351`
- `static/js/chat.js:5496`
- `static/js/chat.js:6354`
- `static/js/chat.js:6367`

## `_syncForegroundStreamGlobals` — function, line 1007
- **called from:**
- `static/js/chat.js:1007`
- `static/js/chat.js:1646`
- `static/js/chat.js:2433`
- `static/js/chat.js:5121`
- `static/js/chat.js:5360`
- `static/js/chat.js:5531`
- `static/js/chat.js:6383`

## `_touchStreamActivity` — function, line 1016
- **called from:**
- `static/js/chat.js:1016`
- `static/js/chat.js:1878`
- `static/js/chat.js:3148`

## `_metricsCostRecordId` — function, line 1025
- **called from:**
- `static/js/chat.js:1025`
- `static/js/chat.js:3876`
- `static/js/chat.js:3910`
- `static/js/chat.js:5813`
- `static/js/chat.js:5868`

## `_postExactStop` — function, line 1031
- **called from:**
- `static/js/chat.js:1031`
- `static/js/chat.js:1054`
- `static/js/chat.js:1071`

## `_stopExactRun` — function, line 1040
- **called from:**
- `static/js/chat.js:1040`
- `static/js/chat.js:2389`
- `static/js/chat.js:2390`
- `static/js/chat.js:5260`

## `_rememberStreamRunId` — function, line 1058
- **called from:**
- `static/js/chat.js:1058`
- `static/js/chat.js:2557`

## `_appendGeneratedImageBubble` — function, line 1089
- **called from:**
- `static/js/chat.js:1089`
- `static/js/chat.js:3277`
- `static/js/chat.js:4163`
- `static/js/chat.js:4717`

## `_normalizeEndpointForCompare` — function, line 1120
- **called from:**
- `static/js/chat.js:1120`
- `static/js/chat.js:1144`
- `static/js/chat.js:1150`

## `_probeCurrentEndpointStatus` — function, line 1143
- **called from:**
- `static/js/chat.js:1143`

## `init` — function, line 1166
- **called from:**
- `static/app.js:3724`
- `static/app.js:3725`
- `static/app.js:3726`
- `static/app.js:3727`
- `static/app.js:3728`
- `static/app.js:3729`
- `static/app.js:3731`
- `static/app.js:3734`
- `static/app.js:3736`
- `static/app.js:3739`
- `static/app.js:3748`
- `static/app.js:4370`
- `static/app.js:4371`
- `static/js/a11y.js:121`
- `static/js/a11y.js:163`
- `static/js/censor.js:44`
- `static/js/chat.js:1166`
- `static/js/chat.js:1171`
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

## `_wireHistoryRecall` — arrow, line 1185
- **called from:**
- `static/js/chat.js:1196`
- `static/js/chat.js:1198`
- `static/js/chat.js:1199`

## `_wireArrowUpRecall` — arrow, line 1190
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `updateSubmitButton` — function, line 1214
- **called from:**
- `static/js/chat.js:1214`
- `static/js/chat.js:1549`
- `static/js/chat.js:1620`
- `static/js/chat.js:1839`
- `static/js/chat.js:2062`
- `static/js/chat.js:2178`
- `static/js/chat.js:2196`
- `static/js/chat.js:5145`
- `static/js/chat.js:5370`
- `static/js/chat.js:5534`
- `static/js/chat.js:5646`
- `static/js/chat.js:5680`
- `static/js/chat.js:6393`

## `_extractPlanText` — function, line 1284
- **called from:**
- `static/js/chat.js:1284`
- `static/js/chat.js:1304`
- `static/js/chat.js:1324`

## `_getStoredPlan` — function, line 1299
- **called from:**
- `static/js/chat.js:1299`
- `static/js/chat.js:1324`

## `_setStoredPlan` — function, line 1303
- **called from:**
- `static/js/chat.js:1303`
- `static/js/chat.js:4289`
- `static/js/chat.js:4728`

## `_clearStoredPlan` — function, line 1309
- **called from:**
- `static/js/chat.js:1309`
- `static/js/chat.js:1332`

## `_attachPlanActions` — function, line 1313
- **called from:**
- `static/js/chat.js:1313`
- `static/js/chat.js:4729`

## `_escapeQueueText` — function, line 1338
- **called from:**
- `static/js/chat.js:1338`
- `static/js/chat.js:1364`

## `_ensureQueuedBubbleHost` — function, line 1342
- **called from:**
- `static/js/chat.js:1342`
- `static/js/chat.js:1358`

## `_createQueuedBubble` — function, line 1357
- **called from:**
- `static/js/chat.js:1357`
- `static/js/chat.js:1433`

## `_removeQueuedRequest` — function, line 1374
- **called from:**
- `static/js/chat.js:1374`
- `static/js/chat.js:1412`
- `static/js/chat.js:1465`

## `_setComposerAndSend` — function, line 1382
- **called from:**
- `static/js/chat.js:1329`
- `static/js/chat.js:1382`
- `static/js/chat.js:1405`
- `static/js/chat.js:1415`
- `static/js/chat.js:1466`

## `handleChatSubmit` — method?, line 1389
- **called from:**
- `static/js/chat.js:1389`
- `static/js/chat.js:1474`
- `static/js/chat.js:7308`

## `_sendQueuedWhenIdle` — function, line 1397
- **called from:**
- `static/js/chat.js:1397`
- `static/js/chat.js:1426`

## `trySend` — arrow, line 1399
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_promoteQueuedRequest` — function, line 1411
- **called from:**
- `static/js/chat.js:1367`
- `static/js/chat.js:1411`

## `_queueAgentRequest` — function, line 1429
- **called from:**
- `static/js/chat.js:1429`
- `static/js/chat.js:1448`

## `queueStreamingComposerRequest` — function, line 1439
- **called from:**
- `static/app.js:113`
- `static/app.js:3481`
- `static/app.js:4108`
- `static/js/chat.js:1439`
- `static/js/chat.js:1499`

## `_drainQueuedAgentRequests` — function, line 1457
- **called from:**
- `static/js/chat.js:1457`
- `static/js/chat.js:1553`
- `static/js/chat.js:5225`
- `static/js/chat.js:5373`

## `handleChatSubmit` — function, line 1474
- **called from:**
- `static/js/chat.js:1389`
- `static/js/chat.js:1474`
- `static/js/chat.js:7308`

## `_releaseSendFlag` — arrow, line 1644
- **called from:**
- `static/js/chat.js:1680`
- `static/js/chat.js:1694`
- `static/js/chat.js:1703`
- `static/js/chat.js:1751`
- `static/js/chat.js:1761`
- `static/js/chat.js:1798`
- `static/js/chat.js:1807`
- `static/js/chat.js:1818`
- `static/js/chat.js:1826`
- `static/js/chat.js:2063`
- `static/js/chat.js:2179`
- `static/js/chat.js:2197`

## `selectedRouteForSend` — arrow, line 1715
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_renderStream` — arrow, line 1901
- **called from:**
- `static/js/chat.js:2929`
- `static/js/chat.js:2965`
- `static/js/chat.js:3369`
- `static/js/chat.js:3371`
- `static/js/chat.js:3516`
- `static/js/chat.js:3518`

## `_finalizeRoundRender` — arrow, line 1902
- **called from:**
- `static/js/chat.js:3004`
- `static/js/chat.js:3974`
- `static/js/chat.js:4301`

## `_finalizeInterruptedView` — arrow, line 1903
- **called from:**
- `static/js/chat.js:2431`
- `static/js/chat.js:4855`

## `_cancelThinkingTimer` — arrow, line 1904
- **called from:**
- `static/js/chat.js:3282`
- `static/js/chat.js:3288`
- `static/js/chat.js:3296`
- `static/js/chat.js:3966`
- `static/js/chat.js:4280`
- `static/js/chat.js:4294`
- `static/js/chat.js:4370`
- `static/js/chat.js:4380`
- `static/js/chat.js:4396`
- `static/js/chat.js:4478`
- `static/js/chat.js:4864`

## `_removeThinkingSpinner` — arrow, line 1905
- **called from:**
- `static/js/chat.js:2706`
- `static/js/chat.js:3289`
- `static/js/chat.js:3297`
- `static/js/chat.js:3967`
- `static/js/chat.js:4281`
- `static/js/chat.js:4295`
- `static/js/chat.js:4371`
- `static/js/chat.js:4381`
- `static/js/chat.js:4397`
- `static/js/chat.js:4479`
- `static/js/chat.js:4865`

## `_flushLiveThinking` — arrow, line 1906
- **called from:**
- `static/js/chat.js:2856`
- `static/js/chat.js:3176`

## `_cancelLiveThinkingWork` — arrow, line 1907
- **called from:**
- `static/js/chat.js:2430`
- `static/js/chat.js:2857`
- `static/js/chat.js:2884`
- `static/js/chat.js:3177`
- `static/js/chat.js:3479`
- `static/js/chat.js:4299`
- `static/js/chat.js:4476`
- `static/js/chat.js:4841`
- `static/js/chat.js:5094`

## `_closeOpenThinkingMarkup` — arrow, line 1913
- **called from:**
- `static/js/chat.js:3002`
- `static/js/chat.js:3194`
- `static/js/chat.js:3964`
- `static/js/chat.js:4292`
- `static/js/chat.js:4839`

## `_endThinkingOnTerminalPath` — arrow, line 1914
- **called from:**
- `static/js/chat.js:3003`
- `static/js/chat.js:4859`

## `clearResponseTimeout` — arrow, line 1917
- **called from:**
- `static/js/chat.js:2520`
- `static/js/chat.js:3271`
- `static/js/chat.js:5095`

## `clearFirstTokenWaitTimers` — arrow, line 1919
- **called from:**
- `static/js/chat.js:1924`
- `static/js/chat.js:3143`
- `static/js/chat.js:3273`
- `static/js/chat.js:5097`

## `scheduleFirstTokenWaitMessages` — arrow, line 1923
- **called from:**
- `static/js/chat.js:2478`

## `clearProcessingProbe` — arrow, line 1936
- **called from:**
- `static/js/chat.js:3272`
- `static/js/chat.js:5096`

## `_dropReadonly` — arrow, line 2026
- **called from:**
- `static/js/chat.js:2040`
- `static/js/compare/index.js:622`

## `_idleTimeoutHandler` — arrow, line 2376
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_armIdleTimeout` — arrow, line 2404
- **called from:**
- `static/js/chat.js:2409`
- `static/js/chat.js:3150`

## `enableResearchBtn` — arrow, line 2489
- **called from:**
- `static/js/chat.js:2553`

## `_tzName` — arrow, line 2505
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_rememberGeneratedImage` — function, line 2590
- **called from:**
- `static/js/chat.js:2590`
- `static/js/chat.js:3276`
- `static/js/chat.js:4162`

## `_metricsTargetForTurn` — function, line 2598
- **called from:**
- `static/js/chat.js:2598`
- `static/js/chat.js:3904`
- `static/js/chat.js:3924`
- `static/js/chat.js:4765`

## `_ensureStreamLayout` — function, line 2608
- **called from:**
- `static/js/chat.js:2608`
- `static/js/chat.js:2992`
- `static/js/chat.js:3027`
- `static/js/chat.js:3456`

## `_ensureVisibleRoundForDelta` — function, line 2620
- **called from:**
- `static/js/chat.js:2620`
- `static/js/chat.js:3339`

## `_thinkingLabel` — function, line 2677
- **called from:**
- `static/js/chat.js:2677`
- `static/js/chat.js:2716`

## `_showThinkingSpinner` — function, line 2690
- **called from:**
- `static/js/chat.js:2690`
- `static/js/chat.js:2707`
- `static/js/chat.js:2716`

## `_replaceThinkingSpinner` — function, line 2705
- **called from:**
- `static/js/chat.js:2705`
- `static/js/chat.js:3283`

## `_scheduleThinkingSpinner` — function, line 2712
- **called from:**
- `static/js/chat.js:2712`
- `static/js/chat.js:2930`
- `static/js/chat.js:3373`
- `static/js/chat.js:3520`
- `static/js/chat.js:4230`

## `_estimateThinkingTokens` — function, line 2749
- **called from:**
- `static/js/chat.js:2749`
- `static/js/chat.js:2793`

## `_formatThinkStats` — function, line 2755
- **called from:**
- `static/js/chat.js:2755`
- `static/js/chat.js:2829`
- `static/js/chat.js:2897`
- `static/js/chat.js:2942`
- `static/js/chat.js:3237`

## `_stripThinkingWrappers` — function, line 2761
- **called from:**
- `static/js/chat.js:2761`
- `static/js/chat.js:2776`
- `static/js/chat.js:2787`

## `_liveThinkingText` — function, line 2774
- **called from:**
- `static/js/chat.js:2774`
- `static/js/chat.js:2788`
- `static/js/chat.js:2807`

## `_closedThinkingText` — function, line 2782
- **called from:**
- `static/js/chat.js:2782`
- `static/js/chat.js:2882`
- `static/js/chat.js:2894`
- `static/js/chat.js:2912`
- `static/js/chat.js:3228`

## `_commitLiveThinkingText` — function, line 2791
- **called from:**
- `static/js/chat.js:2791`

## `_ensureLiveThinkingThrottle` — function, line 2804
- **called from:**
- `static/js/chat.js:2804`
- `static/js/chat.js:2834`

## `_stopLiveThinkTimer` — function, line 2813
- **called from:**
- `static/js/chat.js:2813`
- `static/js/chat.js:2824`
- `static/js/chat.js:2851`

## `_startLiveThinkTimer` — function, line 2818
- **called from:**
- `static/js/chat.js:2818`
- `static/js/chat.js:2835`

## `_queueLiveThinking` — function, line 2833
- **called from:**
- `static/js/chat.js:2833`
- `static/js/chat.js:2839`
- `static/js/chat.js:3363`
- `static/js/chat.js:3480`
- `static/js/chat.js:3506`

## `_finalizeLiveThinking` — function, line 2855
- **called from:**
- `static/js/chat.js:2855`
- `static/js/chat.js:2882`
- `static/js/chat.js:2894`
- `static/js/chat.js:2914`
- `static/js/chat.js:3228`

## `_endLiveThinkingSection` — function, line 2890
- **called from:**
- `static/js/chat.js:2890`
- `static/js/chat.js:3970`
- `static/js/chat.js:4297`

## `_cancelThinkingGrace` — function, line 2901
- **called from:**
- `static/js/chat.js:2657`
- `static/js/chat.js:2852`
- `static/js/chat.js:2901`
- `static/js/chat.js:2911`
- `static/js/chat.js:3440`

## `_finishLiveThinkingTransition` — function, line 2907
- **called from:**
- `static/js/chat.js:2907`
- `static/js/chat.js:2974`
- `static/js/chat.js:3509`

## `_scheduleThinkingGrace` — function, line 2968
- **called from:**
- `static/js/chat.js:2968`
- `static/js/chat.js:3437`
- `static/js/chat.js:3504`

## `_replyAfterClosedThinking` — function, line 3014
- **called from:**
- `static/js/chat.js:3014`
- `static/js/chat.js:3036`

## `markFirstVisibleOutput` — arrow, line 3140
- **called from:**
- `static/js/chat.js:3165`

## `resetFn` — arrow, line 4741
- **called from:**
- `static/js/tts-ai.js:235`
- `static/js/tts-ai.js:341`

## `failures` — class, line 5040
- **called from:**
- `static/js/chat.js:5274`

## `abortCurrentRequest` — function, line 5237
- **called from:**
- `static/app.js:839`
- `static/js/chat.js:1512`
- `static/js/chat.js:5237`
- `static/js/chat.js:5332`
- `static/js/chat.js:5499`
- `static/js/keyboard-shortcuts.js:247`
- `static/js/sessions.js:979`
- `static/js/sessions.js:1993`
- `static/js/sessions.js:1999`
- `static/js/sessions.js:2540`

## `failures` — class, line 5274
- **called from:**
- `static/js/chat.js:5274`

## `_tryAutoRecover` — function, line 5278
- **called from:**
- `static/js/chat.js:5043`
- `static/js/chat.js:5278`

## `_removeStallBanner` — function, line 5300
- **called from:**
- `static/js/chat.js:5300`
- `static/js/chat.js:5321`
- `static/js/chat.js:5332`
- `static/js/chat.js:5430`
- `static/js/chat.js:5435`

## `_showStallBanner` — function, line 5305
- **called from:**
- `static/js/chat.js:5305`

## `_probeStaleLocalStream` — function, line 5338
- **called from:**
- `static/js/chat.js:5338`

## `_convergeAfterAbort` — function, line 5392
- **called from:**
- `static/js/chat.js:4916`
- `static/js/chat.js:4936`
- `static/js/chat.js:4956`
- `static/js/chat.js:4975`
- `static/js/chat.js:5392`

## `_startStallWatchdog` — function, line 5426
- **called from:**
- `static/js/chat.js:1248`
- `static/js/chat.js:5426`

## `_stopStallWatchdog` — function, line 5433
- **called from:**
- `static/js/chat.js:1256`
- `static/js/chat.js:5433`

## `_renderCancelledBubble` — function, line 5441
- **called from:**
- `static/js/chat.js:1547`
- `static/js/chat.js:4984`
- `static/js/chat.js:5441`

## `detachCurrentStream` — function, line 5495
- **called from:**
- `static/app.js:838`
- `static/js/chat.js:5495`
- `static/js/sessions.js:1991`
- `static/js/sessions.js:2319`

## `resumeStream` — function, line 5581
- **called from:**
- `static/js/chat.js:644`
- `static/js/chat.js:837`
- `static/js/chat.js:5291`
- `static/js/chat.js:5387`
- `static/js/chat.js:5414`
- `static/js/chat.js:5581`
- `static/js/sessions.js:2825`
- `static/js/sessions.js:2858`

## `cleanup` — arrow, line 5670
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5889`
- `static/js/chat.js:7465`
- `static/js/chat.js:7473`
- `static/js/chat.js:7479`
- `static/js/chat.js:7482`
- `static/js/chat.js:7485`
- `static/js/chat.js:7533`
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

## `renderDelta` — arrow, line 5693
- **called from:**
- `static/js/chat.js:5714`

## `queueRender` — arrow, line 5708
- **called from:**
- `static/js/chat.js:5803`

## `closeThinkIfOpen` — arrow, line 5723
- **called from:**
- `static/js/chat.js:5864`
- `static/js/chat.js:5880`
- `static/js/chat.js:5912`

## `_finishToolNode` — arrow, line 5732
- **called from:**
- `static/js/chat.js:5675`

## `checkBackgroundStream` — function, line 5939
- **called from:**
- `static/js/chat.js:5939`
- `static/js/sessions.js:2212`

## `_markCompactPre` — function, line 6024
- **called from:**
- `static/js/chat.js:6024`
- `static/js/chat.js:6050`

## `_scanCompactPres` — function, line 6034
- **called from:**
- `static/js/chat.js:6034`
- `static/js/chat.js:6045`
- `static/js/chat.js:6051`

## `_initCompactPreObserver` — function, line 6042
- **called from:**
- `static/js/chat.js:6042`

## `_reasoningKey` — function, line 6067
- **called from:**
- `static/js/chat.js:6067`
- `static/js/chat.js:6070`
- `static/js/chat.js:6076`
- `static/js/chat.js:6077`

## `getReasoningLevel` — function, line 6068
- **called from:**
- `static/js/chat.js:2230`
- `static/js/chat.js:6068`
- `static/js/chat.js:6082`
- `static/js/chat.js:6140`

## `setReasoningLevel` — function, line 6074
- **called from:**
- `static/js/chat.js:6074`
- `static/js/chat.js:6147`
- `static/js/chat.js:6193`

## `updateThinkingUI` — function, line 6081
- **called from:**
- `static/js/chat.js:6079`
- `static/js/chat.js:6081`
- `static/js/chat.js:6149`
- `static/js/chat.js:6201`
- `static/js/sessions.js:1958`

## `refreshThinkingControl` — function, line 6105
- **called from:**
- `static/js/chat.js:6105`
- `static/js/chat.js:6202`
- `static/js/modelPicker.js:857`
- `static/js/sessions.js:1959`

## `_refreshThinkingControlNow` — function, line 6109
- **called from:**
- `static/js/chat.js:6109`

## `mk` — arrow, line 6123
- **called from:**
- `static/js/chat.js:6134`
- `static/js/chat.js:6135`
- `static/js/chat.js:6136`
- `static/js/cookbookServe.js:2709`
- `static/js/cookbookServe.js:2717`
- `static/js/cookbookServe.js:2722`
- `static/js/cookbookServe.js:2723`
- `static/js/cookbookServe.js:2769`
- `static/js/cookbookServe.js:2770`
- `static/js/documentLibrary.js:2221`
- `static/js/documentLibrary.js:2222`
- `static/js/documentLibrary.js:2653`
- `static/js/documentLibrary.js:2654`
- `static/js/documentLibrary.js:2655`
- `static/js/documentLibrary.js:2656`
- `static/js/skills.js:404`
- `static/js/skills.js:405`
- `static/js/skills.js:420`
- `static/js/skills.js:424`
- `static/js/skills.js:426`
- `static/js/skills.js:427`

## `initThinkingControl` — function, line 6154
- **called from:**
- `static/js/chat.js:6154`
- `static/js/chat.js:6209`

## `_position` — function, line 6167
- **called from:**
- `static/js/chat.js:6167`
- `static/js/chat.js:6176`
- `static/js/chat.js:6199`
- `static/js/chat.js:6200`
- `static/js/modalSnap.js:1039`
- `static/js/modalSnap.js:1078`
- `static/js/slashAutocomplete.js:141`
- `static/js/slashAutocomplete.js:211`
- `static/js/slashAutocomplete.js:299`

## `_open` — function, line 6173
- **called from:**
- `static/js/chat.js:6173`
- `static/js/chat.js:6186`
- `static/js/settings.js:3778`

## `_close` — function, line 6178
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

## `initListeners` — function, line 6208
- **called from:**
- `static/app.js:3730`
- `static/js/chat.js:6208`

## `_observeChatHistory` — arrow, line 6230
- **called from:**
- `static/js/chat.js:6235`

## `_dbRowCountBefore` — function, line 6457
- **called from:**
- `static/js/chat.js:6457`
- `static/js/chat.js:6663`
- `static/js/chat.js:6813`

## `editUserMessage` — function, line 6483
- **called from:**
- `static/js/chat.js:6483`
- `static/js/chatRenderer.js:1945`

## `resendUserMessage` — function, line 6586
- **called from:**
- `static/js/chat.js:6586`
- `static/js/chatRenderer.js:369`
- `static/js/chatRenderer.js:1960`

## `regenerateFrom` — function, line 6706
- **called from:**
- `static/js/chat.js:6647`
- `static/js/chat.js:6706`
- `static/js/chatRenderer.js:1761`

## `_attachVariantNav` — function, line 6878
- **called from:**
- `static/js/chat.js:4769`
- `static/js/chat.js:6878`

## `_variantTagText` — function, line 6904
- **called from:**
- `static/js/chat.js:6904`
- `static/js/chat.js:6930`

## `_renderVariantNav` — function, line 6908
- **called from:**
- `static/js/chat.js:6890`
- `static/js/chat.js:6908`
- `static/js/chat.js:6988`
- `static/js/chat.js:7688`

## `_switchVariant` — function, line 6978
- **called from:**
- `static/js/chat.js:6938`
- `static/js/chat.js:6946`
- `static/js/chat.js:6958`
- `static/js/chat.js:6966`
- `static/js/chat.js:6978`

## `forkFrom` — function, line 7001
- **called from:**
- `static/js/chat.js:7001`
- `static/js/chatRenderer.js:1780`

## `checkPendingResearch` — function, line 7035
- **called from:**
- `static/js/chat.js:7035`
- `static/js/sessions.js:2192`

## `updateSpinnerFromProgress` — function, line 7121
- **called from:**
- `static/js/chat.js:7121`
- `static/js/chat.js:7141`
- `static/js/chat.js:7209`

## `setDisplayOverride` — function, line 7258
- **called from:**
- `static/js/chat.js:7258`

## `setHideUserBubble` — function, line 7263
- **called from:**
- `static/js/chat.js:7263`

## `setPendingContinue` — function, line 7268
- **called from:**
- `static/js/chat.js:7268`

## `setContinuePrefill` — function, line 7273
- **called from:**
- `static/js/chat.js:7273`

## `continueFromBubble` — function, line 7286
- **called from:**
- `static/js/chat.js:1601`
- `static/js/chat.js:5004`
- `static/js/chat.js:7286`
- `static/js/chatRenderer.js:1768`
- `static/js/chatRenderer.js:2998`

## `handleChatSubmit` — method?, line 7308
- **called from:**
- `static/js/chat.js:1389`
- `static/js/chat.js:1474`
- `static/js/chat.js:7308`

## `deleteMessage` — function, line 7321
- **called from:**
- `static/js/chat.js:7321`
- `static/js/chatRenderer.js:1784`
- `static/js/chatRenderer.js:1949`

## `editAIMessage` — function, line 7433
- **called from:**
- `static/js/chat.js:7433`
- `static/js/chatRenderer.js:1752`

## `cleanup` — function, line 7465
- **called from:**
- `static/js/calendar.js:2592`
- `static/js/calendar.js:2629`
- `static/js/calendar.js:2750`
- `static/js/calendar.js:2759`
- `static/js/chat.js:5889`
- `static/js/chat.js:7465`
- `static/js/chat.js:7473`
- `static/js/chat.js:7479`
- `static/js/chat.js:7482`
- `static/js/chat.js:7485`
- `static/js/chat.js:7533`
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

## `rewriteWith` — function, line 7547
- **called from:**
- `static/js/chat.js:7547`
- `static/js/chatRenderer.js:1772`
- `static/js/chatRenderer.js:1776`

## `_killRwSpin` — arrow, line 7584
- **called from:**
- `static/js/chat.js:7630`
- `static/js/chat.js:7695`

## `_stripThink` — arrow, line 7649
- **called from:**
- `static/js/chat.js:7655`

## `continueFrom` — function, line 7705
- **called from:**
- `static/js/chat.js:7705`

## `_attachLang` — function, line 7722
- **called from:**
- `static/js/chat.js:7722`
- `static/js/chat.js:7790`

## `openAttachment` — function, line 7732
- **called from:**
- `static/js/chat.js:7732`
- `static/js/chatRenderer.js:202`
