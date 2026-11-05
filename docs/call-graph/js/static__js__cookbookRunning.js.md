# `static/js/cookbookRunning.js` — definitions & call sites

154 definitions (regex-based, best-effort).
**Exports:** `_addTask`, `_clearCookbookNotif`, `_launchServeTask`, `_loadTasks`, `_nextAvailablePort`, `_parseServePhase`, `_processQueue`, `_removeTask`, `_renderRunningTab`, `_retryDownload`, `_saveTasks`, `_selfHealStaleTasks`, `_serveAutoFix`, `_serveAutoRetry`, `_serveAutoRetryRemove`, `_serveAutoRetryReplace`, `_startBackgroundMonitor`, `_syncFromServer`, `_taskPort`, `_tmuxCmd`, `_tmuxForceKill`, `_tmuxGracefulKill`, `_tmuxIsAliveCheck`, `initRunning`

## `_isFinishedDownload` — function, line 17
- **called from:**
- `static/js/cookbookRunning.js:17`
- `static/js/cookbookRunning.js:23`
- `static/js/cookbookRunning.js:2395`
- `static/js/cookbookRunning.js:2458`
- `static/js/cookbookRunning.js:2458`

## `_statusLabel` — function, line 21
- **called from:**
- `static/js/cookbookRunning.js:21`
- `static/js/cookbookRunning.js:56`
- `static/js/cookbookRunning.js:2922`
- `static/js/cookbookRunning.js:3165`
- `static/js/cookbookRunning.js:3195`
- `static/js/cookbookRunning.js:3241`
- `static/js/cookbookRunning.js:3301`
- `static/js/cookbookRunning.js:3341`
- `static/js/cookbookRunning.js:3354`
- `static/js/cookbookRunning.js:3572`
- `static/js/cookbookRunning.js:3592`
- `static/js/cookbookRunning.js:3945`

## `_downloadBadgeText` — function, line 28
- **called from:**
- `static/js/cookbookRunning.js:28`
- `static/js/cookbookRunning.js:49`
- `static/js/cookbookRunning.js:4442`

## `_taskBadge` — function, line 46
- **called from:**
- `static/js/cookbookRunning.js:46`
- `static/js/cookbookRunning.js:2401`
- `static/js/cookbookRunning.js:2452`

## `_ggufDisplayPartFromPath` — function, line 59
- **called from:**
- `static/js/cookbookRunning.js:59`
- `static/js/cookbookRunning.js:72`
- `static/js/cookbookRunning.js:90`
- `static/js/cookbookRunning.js:100`

## `_downloadDisplayName` — function, line 69
- **called from:**
- `static/js/cookbookRunning.js:69`
- `static/js/cookbookRunning.js:96`

## `_downloadNameFromPayload` — function, line 76
- **called from:**
- `static/js/cookbookRunning.js:76`
- `static/js/cookbookRunning.js:96`
- `static/js/cookbookRunning.js:1561`

## `_taskDisplayName` — function, line 94
- **called from:**
- `static/js/cookbookRunning.js:94`
- `static/js/cookbookRunning.js:2454`

## `_canLaunchDownloadedTask` — function, line 104
- **called from:**
- `static/js/cookbookRunning.js:104`
- `static/js/cookbookRunning.js:2460`

## `_downloadServeFields` — function, line 108
- **called from:**
- `static/js/cookbookRunning.js:108`
- `static/js/cookbookRunning.js:2536`

## `_downloadOutputLooksActive` — function, line 122
- **called from:**
- `static/js/cookbookRunning.js:122`
- `static/js/cookbookRunning.js:140`
- `static/js/cookbookRunning.js:145`
- `static/js/cookbookRunning.js:2145`
- `static/js/cookbookRunning.js:2556`
- `static/js/cookbookRunning.js:3812`

## `_canClearTask` — function, line 133
- **called from:**
- `static/js/cookbookRunning.js:133`
- `static/js/cookbookRunning.js:2292`
- `static/js/cookbookRunning.js:2307`
- `static/js/cookbookRunning.js:2411`
- `static/js/cookbookRunning.js:2460`

## `_clearPillLabel` — function, line 144
- **called from:**
- `static/js/cookbookRunning.js:144`
- `static/js/cookbookRunning.js:2413`
- `static/js/cookbookRunning.js:2460`

## `_venvRootFromPath` — function, line 149
- **called from:**
- `static/js/cookbook.js:641`
- `static/js/cookbook.js:674`
- `static/js/cookbookRunning.js:149`
- `static/js/cookbookRunning.js:2027`

## `_depInstallSucceeded` — function, line 164
- **called from:**
- `static/js/cookbookRunning.js:164`
- `static/js/cookbookRunning.js:3186`
- `static/js/cookbookRunning.js:4269`

## `_shouldOfferCrashReport` — function, line 173
- **called from:**
- `static/js/cookbookRunning.js:173`
- `static/js/cookbookRunning.js:2768`

## `_serveTaskLooksAwqOnLocalBackend` — function, line 179
- **called from:**
- `static/js/cookbookRunning.js:179`
- `static/js/cookbookRunning.js:246`
- `static/js/cookbookRunning.js:3211`
- `static/js/cookbookRunning.js:3216`

## `_serveTaskLooksAwqWithoutUsableAccelerator` — function, line 185
- **called from:**
- `static/js/cookbookRunning.js:185`
- `static/js/cookbookRunning.js:256`

## `_openDownloadForGgufTask` — function, line 192
- **called from:**
- `static/js/cookbookRunning.js:192`
- `static/js/cookbookRunning.js:251`
- `static/js/cookbookRunning.js:261`

## `_terminalServeDiagnosis` — function, line 228
- **called from:**
- `static/js/cookbookRunning.js:228`
- `static/js/cookbookRunning.js:2423`
- `static/js/cookbookRunning.js:2472`

## `_redactCrashReportText` — function, line 277
- **called from:**
- `static/js/cookbookRunning.js:277`
- `static/js/cookbookRunning.js:290`
- `static/js/cookbookRunning.js:310`

## `_lastLines` — function, line 289
- **called from:**
- `static/js/cookbookRunning.js:289`
- `static/js/cookbookRunning.js:333`

## `_codeFence` — function, line 295
- **called from:**
- `static/js/cookbookRunning.js:295`
- `static/js/cookbookRunning.js:331`
- `static/js/cookbookRunning.js:333`

## `_taskHostLabel` — function, line 299
- **called from:**
- `static/js/cookbookRunning.js:299`
- `static/js/cookbookRunning.js:323`

## `_taskPort` — function, line 304
- **called from:**
- `static/js/cookbook-hwfit.js:1801`
- `static/js/cookbookRunning.js:304`
- `static/js/cookbookRunning.js:327`
- `static/js/cookbookRunning.js:522`
- `static/js/cookbookServe.js:115`
- `static/js/cookbookServe.js:3468`

## `_buildCrashReport` — function, line 308
- **called from:**
- `static/js/cookbookRunning.js:308`
- `static/js/cookbookRunning.js:2771`

## `_taskServerSelection` — function, line 361
- **called from:**
- `static/js/cookbookRunning.js:361`
- `static/js/cookbookRunning.js:401`

## `_serverColorForTaskGroup` — function, line 372
- **called from:**
- `static/js/cookbookRunning.js:372`
- `static/js/cookbookRunning.js:2279`

## `_serverHeaderStyle` — function, line 385
- **called from:**
- `static/js/cookbookRunning.js:385`
- `static/js/cookbookRunning.js:2280`

## `_shouldAutoExpandTaskOutput` — function, line 394
- **called from:**
- `static/js/cookbookRunning.js:394`
- `static/js/cookbookRunning.js:2466`

## `_selectTaskServer` — function, line 400
- **called from:**
- `static/js/cookbookRunning.js:400`
- `static/js/cookbookRunning.js:1658`
- `static/js/cookbookRunning.js:2533`

## `_parseServePhase` — function, line 442
- **called from:**
- `static/js/cookbookRunning.js:442`
- `static/js/cookbookRunning.js:3617`

## `_nextAvailablePort` — function, line 516
- **called from:**
- `static/js/cookbook-hwfit.js:1788`
- `static/js/cookbookRunning.js:516`
- `static/js/cookbookServe.js:1585`

## `_removeEndpointByUrl` — function, line 534
- **called from:**
- `static/js/cookbookRunning.js:534`
- `static/js/cookbookRunning.js:2939`
- `static/js/cookbookRunning.js:3017`

## `_refreshModelsAfterEndpointChange` — function, line 549
- **called from:**
- `static/js/cookbookRunning.js:544`
- `static/js/cookbookRunning.js:549`
- `static/js/cookbookRunning.js:2077`
- `static/js/cookbookRunning.js:2719`
- `static/js/cookbookRunning.js:2737`
- `static/js/cookbookRunning.js:3024`
- `static/js/cookbookRunning.js:3625`

## `_appendCookbookEndpointScope` — function, line 582
- **called from:**
- `static/js/cookbookRunning.js:582`
- `static/js/cookbookRunning.js:2730`
- `static/js/cookbookRunning.js:3716`
- `static/js/cookbookRunning.js:4396`

## `_connectHostFromRemote` — function, line 589
- **called from:**
- `static/js/cookbookRunning.js:589`
- `static/js/cookbookRunning.js:1170`
- `static/js/cookbookRunning.js:2707`
- `static/js/cookbookRunning.js:3672`
- `static/js/cookbookRunning.js:3912`
- `static/js/cookbookRunning.js:4350`

## `_isAnyBindHost` — function, line 595
- **called from:**
- `static/js/cookbookRunning.js:595`
- `static/js/cookbookRunning.js:603`

## `_endpointFromAdvertisedUrl` — function, line 600
- **called from:**
- `static/js/cookbookRunning.js:600`
- `static/js/cookbookRunning.js:3683`
- `static/js/cookbookRunning.js:4358`

## `_serveExpectedModel` — function, line 612
- **called from:**
- `static/js/cookbookRunning.js:612`
- `static/js/cookbookRunning.js:635`
- `static/js/cookbookRunning.js:642`
- `static/js/cookbookRunning.js:655`

## `_modelIdMatchesExpected` — function, line 624
- **called from:**
- `static/js/cookbookRunning.js:624`
- `static/js/cookbookRunning.js:638`

## `_endpointMatchesServe` — function, line 634
- **called from:**
- `static/js/cookbookRunning.js:634`
- `static/js/cookbookRunning.js:3698`
- `static/js/cookbookRunning.js:4381`

## `_markServeEndpointMismatch` — function, line 641
- **called from:**
- `static/js/cookbookRunning.js:641`
- `static/js/cookbookRunning.js:3699`
- `static/js/cookbookRunning.js:4382`

## `_appendPinnedServeModel` — function, line 654
- **called from:**
- `static/js/cookbookRunning.js:654`
- `static/js/cookbookRunning.js:3717`
- `static/js/cookbookRunning.js:4397`

## `_isImageServeTask` — function, line 659
- **called from:**
- `static/js/cookbookRunning.js:659`
- `static/js/cookbookRunning.js:2731`
- `static/js/cookbookRunning.js:3711`
- `static/js/cookbookRunning.js:4361`

## `_processQueue` — function, line 666
- **called from:**
- `static/js/cookbookRunning.js:666`
- `static/js/cookbookRunning.js:3307`
- `static/js/cookbookRunning.js:3361`
- `static/js/cookbookRunning.js:3368`
- `static/js/cookbookRunning.js:3607`
- `static/js/tts-ai.js:259`
- `static/js/tts-ai.js:263`

## `_startQueuedDownload` — function, line 682
- **called from:**
- `static/js/cookbookRunning.js:678`
- `static/js/cookbookRunning.js:682`
- `static/js/cookbookRunning.js:2593`
- `static/js/cookbookRunning.js:2678`

## `_serveOutputLooksReady` — function, line 750
- **called from:**
- `static/js/cookbookRunning.js:135`
- `static/js/cookbookRunning.js:237`
- `static/js/cookbookRunning.js:750`
- `static/js/cookbookRunning.js:780`
- `static/js/cookbookRunning.js:3181`
- `static/js/cookbookRunning.js:4281`

## `_normalizeTaskForDisplay` — function, line 758
- **called from:**
- `static/js/cookbookRunning.js:758`

## `_loadTasks` — function, line 786
- **called from:**
- `static/js/cookbook-diagnosis.js:171`
- `static/js/cookbook-diagnosis.js:930`
- `static/js/cookbook-hwfit.js:1796`
- `static/js/cookbook.js:1041`
- `static/js/cookbook.js:1058`
- `static/js/cookbook.js:2108`
- `static/js/cookbookDownload.js:565`
- `static/js/cookbookDownload.js:603`
- `static/js/cookbookDownload.js:620`
- `static/js/cookbookRunning.js:517`
- `static/js/cookbookRunning.js:693`
- `static/js/cookbookRunning.js:724`
- `static/js/cookbookRunning.js:786`
- `static/js/cookbookRunning.js:832`
- `static/js/cookbookRunning.js:919`
- `static/js/cookbookRunning.js:958`
- `static/js/cookbookRunning.js:988`
- `static/js/cookbookRunning.js:1369`
- `static/js/cookbookRunning.js:1428`
- `static/js/cookbookRunning.js:1558`
- `static/js/cookbookRunning.js:1608`
- `static/js/cookbookRunning.js:1672`
- `static/js/cookbookRunning.js:1714`
- `static/js/cookbookRunning.js:1747`
- `static/js/cookbookRunning.js:1974`
- `static/js/cookbookRunning.js:1993`
- `static/js/cookbookRunning.js:2135`
- `static/js/cookbookRunning.js:2291`
- `static/js/cookbookRunning.js:2346`
- `static/js/cookbookRunning.js:2557`
- `static/js/cookbookRunning.js:3323`
- `static/js/cookbookRunning.js:3344`
- `static/js/cookbookRunning.js:3807`
- `static/js/cookbookRunning.js:3896`
- `static/js/cookbookRunning.js:4013`
- `static/js/cookbookRunning.js:4050`
- `static/js/cookbookRunning.js:4080`
- `static/js/cookbookRunning.js:4199`
- `static/js/cookbookRunning.js:4229`
- `static/js/cookbookRunning.js:4347`
- `static/js/cookbookServe.js:109`
- `static/js/cookbookServe.js:3458`

## `_downloadRepoKey` — function, line 791
- **called from:**
- `static/js/cookbookRunning.js:791`
- `static/js/cookbookRunning.js:801`

## `_downloadHostKey` — function, line 795
- **called from:**
- `static/js/cookbookRunning.js:795`
- `static/js/cookbookRunning.js:803`

## `_downloadDedupeKey` — function, line 799
- **called from:**
- `static/js/cookbookRunning.js:722`
- `static/js/cookbookRunning.js:734`
- `static/js/cookbookRunning.js:799`
- `static/js/cookbookRunning.js:811`
- `static/js/cookbookRunning.js:819`
- `static/js/cookbookRunning.js:933`
- `static/js/cookbookRunning.js:936`

## `_pruneQueuedDownloadDuplicates` — function, line 806
- **called from:**
- `static/js/cookbookRunning.js:806`
- `static/js/cookbookRunning.js:833`

## `_loadPrunedTasks` — function, line 831
- **called from:**
- `static/js/cookbookRunning.js:667`
- `static/js/cookbookRunning.js:831`
- `static/js/cookbookRunning.js:2091`

## `_loadTombstones` — function, line 845
- **called from:**
- `static/js/cookbookRunning.js:845`
- `static/js/cookbookRunning.js:866`
- `static/js/cookbookRunning.js:873`
- `static/js/cookbookRunning.js:1370`
- `static/js/cookbookRunning.js:1431`

## `_saveTombstones` — function, line 861
- **called from:**
- `static/js/cookbookRunning.js:861`
- `static/js/cookbookRunning.js:870`
- `static/js/cookbookRunning.js:1436`

## `_tombstoneTask` — function, line 864
- **called from:**
- `static/js/cookbookRunning.js:864`
- `static/js/cookbookRunning.js:987`
- `static/js/cookbookRunning.js:2306`

## `_isTombstoned` — function, line 872
- **called from:**
- `static/js/cookbookRunning.js:872`
- `static/js/cookbookRunning.js:1439`
- `static/js/cookbookRunning.js:1441`
- `static/js/cookbookRunning.js:4204`
- `static/js/cookbookRunning.js:4235`

## `_redactStoredText` — function, line 877
- **called from:**
- `static/js/cookbookRunning.js:877`
- `static/js/cookbookRunning.js:891`
- `static/js/cookbookRunning.js:896`
- `static/js/cookbookRunning.js:897`
- `static/js/cookbookRunning.js:1277`
- `static/js/cookbookRunning.js:1278`

## `_isServeOutputPlaceholder` — function, line 883
- **called from:**
- `static/js/cookbookRunning.js:883`
- `static/js/cookbookRunning.js:4310`

## `_redactTaskForStorage` — function, line 888
- **called from:**
- `static/js/cookbookRunning.js:736`
- `static/js/cookbookRunning.js:888`
- `static/js/cookbookRunning.js:939`
- `static/js/cookbookRunning.js:4240`

## `_stripStateSecrets` — function, line 902
- **called from:**
- `static/js/cookbookRunning.js:902`
- `static/js/cookbookRunning.js:1384`

## `_saveTasks` — function, line 913
- **called from:**
- `static/js/cookbook.js:1041`
- `static/js/cookbook.js:1058`
- `static/js/cookbook.js:2108`
- `static/js/cookbookDownload.js:608`
- `static/js/cookbookDownload.js:622`
- `static/js/cookbookRunning.js:699`
- `static/js/cookbookRunning.js:737`
- `static/js/cookbookRunning.js:834`
- `static/js/cookbookRunning.js:913`
- `static/js/cookbookRunning.js:941`
- `static/js/cookbookRunning.js:962`
- `static/js/cookbookRunning.js:989`
- `static/js/cookbookRunning.js:1569`
- `static/js/cookbookRunning.js:2308`
- `static/js/cookbookRunning.js:2562`
- `static/js/cookbookRunning.js:4086`
- `static/js/cookbookRunning.js:4327`

## `_addTask` — function, line 918
- **called from:**
- `static/js/cookbook-hwfit.js:2035`
- `static/js/cookbook.js:1509`
- `static/js/cookbook.js:1570`
- `static/js/cookbook.js:1786`
- `static/js/cookbookDownload.js:655`
- `static/js/cookbookRunning.js:918`
- `static/js/cookbookRunning.js:1574`
- `static/js/cookbookRunning.js:1577`
- `static/js/cookbookRunning.js:2072`

## `_updateTask` — function, line 957
- **called from:**
- `static/js/cookbookRunning.js:645`
- `static/js/cookbookRunning.js:684`
- `static/js/cookbookRunning.js:710`
- `static/js/cookbookRunning.js:716`
- `static/js/cookbookRunning.js:743`
- `static/js/cookbookRunning.js:957`
- `static/js/cookbookRunning.js:1525`
- `static/js/cookbookRunning.js:1548`
- `static/js/cookbookRunning.js:1554`
- `static/js/cookbookRunning.js:1582`
- `static/js/cookbookRunning.js:2351`
- `static/js/cookbookRunning.js:2718`
- `static/js/cookbookRunning.js:2735`
- `static/js/cookbookRunning.js:2919`
- `static/js/cookbookRunning.js:2935`
- `static/js/cookbookRunning.js:3162`
- `static/js/cookbookRunning.js:3192`
- `static/js/cookbookRunning.js:3238`
- `static/js/cookbookRunning.js:3298`
- `static/js/cookbookRunning.js:3320`
- `static/js/cookbookRunning.js:3336`
- `static/js/cookbookRunning.js:3348`
- `static/js/cookbookRunning.js:3440`
- `static/js/cookbookRunning.js:3470`
- `static/js/cookbookRunning.js:3574`
- `static/js/cookbookRunning.js:3598`
- `static/js/cookbookRunning.js:3620`
- `static/js/cookbookRunning.js:3638`
- `static/js/cookbookRunning.js:3646`
- `static/js/cookbookRunning.js:3648`
- `static/js/cookbookRunning.js:3703`
- `static/js/cookbookRunning.js:3725`
- `static/js/cookbookRunning.js:3766`
- `static/js/cookbookRunning.js:3779`
- `static/js/cookbookRunning.js:3784`
- `static/js/cookbookRunning.js:3927`
- `static/js/cookbookRunning.js:3932`
- `static/js/cookbookRunning.js:4363`
- `static/js/cookbookRunning.js:4385`
- `static/js/cookbookRunning.js:4404`
- `static/js/tasks.js:91`
- `static/js/tasks.js:1878`

## `_refreshDepsAfterInstall` — function, line 979
- **called from:**
- `static/js/cookbookRunning.js:979`
- `static/js/cookbookRunning.js:3305`
- `static/js/cookbookRunning.js:3359`
- `static/js/cookbookRunning.js:3601`
- `static/js/cookbookRunning.js:4335`

## `_removeTask` — function, line 986
- **called from:**
- `static/js/cookbookRunning.js:986`
- `static/js/cookbookRunning.js:996`
- `static/js/cookbookRunning.js:1001`
- `static/js/cookbookRunning.js:1521`
- `static/js/cookbookRunning.js:1981`
- `static/js/cookbookRunning.js:2004`
- `static/js/cookbookRunning.js:3566`

## `_animateOutThenRemove` — function, line 995
- **called from:**
- `static/js/cookbookRunning.js:995`
- `static/js/cookbookRunning.js:1622`
- `static/js/cookbookRunning.js:1685`
- `static/js/cookbookRunning.js:1727`
- `static/js/cookbookRunning.js:1760`
- `static/js/cookbookRunning.js:2539`
- `static/js/cookbookRunning.js:2585`
- `static/js/cookbookRunning.js:2961`
- `static/js/cookbookRunning.js:3028`
- `static/js/research/panel.js:479`
- `static/js/research/panel.js:1325`
- `static/js/research/panel.js:1330`

## `_taskRemoteHost` — function, line 1006
- **called from:**
- `static/js/cookbookRunning.js:1006`
- `static/js/cookbookRunning.js:1018`
- `static/js/cookbookRunning.js:1026`
- `static/js/cookbookRunning.js:1058`
- `static/js/cookbookRunning.js:1064`
- `static/js/cookbookRunning.js:1078`
- `static/js/cookbookRunning.js:1105`
- `static/js/cookbookRunning.js:1122`
- `static/js/cookbookRunning.js:1159`
- `static/js/cookbookRunning.js:1170`

## `_remoteTmuxPrefix` — function, line 1010
- **called from:**
- `static/js/cookbookRunning.js:1010`
- `static/js/cookbookRunning.js:1020`
- `static/js/cookbookRunning.js:1053`
- `static/js/cookbookRunning.js:1080`
- `static/js/cookbookRunning.js:1107`
- `static/js/cookbookRunning.js:1124`

## `_tmuxCmd` — function, line 1014
- **called from:**
- `static/js/cookbookRunning.js:1014`
- `static/js/cookbookRunning.js:1613`
- `static/js/cookbookRunning.js:1681`
- `static/js/cookbookRunning.js:1723`
- `static/js/cookbookRunning.js:1756`
- `static/js/cookbookRunning.js:2582`
- `static/js/cookbookRunning.js:2998`
- `static/js/cookbookRunning.js:3117`
- `static/js/cookbookRunning.js:3131`
- `static/js/cookbookRunning.js:3330`
- `static/js/cookbookRunning.js:3448`
- `static/js/cookbookRunning.js:3563`
- `static/js/cookbookRunning.js:3605`
- `static/js/cookbookRunning.js:4075`

## `_winSessionCmd` — function, line 1025
- **called from:**
- `static/js/cookbookRunning.js:1016`
- `static/js/cookbookRunning.js:1025`

## `_winPowerShellCmd` — function, line 1056
- **called from:**
- `static/js/cookbookRunning.js:1035`
- `static/js/cookbookRunning.js:1041`
- `static/js/cookbookRunning.js:1045`
- `static/js/cookbookRunning.js:1051`
- `static/js/cookbookRunning.js:1056`
- `static/js/cookbookRunning.js:1076`

## `_winSessionStopTreePs` — function, line 1063
- **called from:**
- `static/js/cookbookRunning.js:1044`
- `static/js/cookbookRunning.js:1063`
- `static/js/cookbookRunning.js:1075`

## `_tmuxGracefulKill` — function, line 1073
- **called from:**
- `static/js/cookbook-hwfit.js:1825`
- `static/js/cookbookRunning.js:1073`
- `static/js/cookbookRunning.js:1093`
- `static/js/cookbookRunning.js:1516`
- `static/js/cookbookRunning.js:1979`
- `static/js/cookbookRunning.js:2001`
- `static/js/cookbookRunning.js:2956`
- `static/js/cookbookRunning.js:2987`
- `static/js/cookbookServe.js:3505`

## `_tmuxForceKill` — function, line 1089
- **called from:**
- `static/js/cookbookRunning.js:1089`

## `_tmuxIsAliveCheck` — function, line 1115
- **called from:**
- `static/js/cookbookRunning.js:1115`

## `_shQuote` — function, line 1129
- **called from:**
- `static/js/cookbookRunning.js:1060`
- `static/js/cookbookRunning.js:1107`
- `static/js/cookbookRunning.js:1124`
- `static/js/cookbookRunning.js:1129`
- `static/js/cookbookRunning.js:1158`
- `static/js/cookbookRunning.js:1158`
- `static/js/cookbookRunning.js:1161`

## `_taskLooksOllama` — function, line 1133
- **called from:**
- `static/js/cookbookRunning.js:1133`
- `static/js/cookbookRunning.js:1153`
- `static/js/cookbookRunning.js:1167`

## `_ollamaBaseUrlForTask` — function, line 1138
- **called from:**
- `static/js/cookbookRunning.js:1138`
- `static/js/cookbookRunning.js:1156`
- `static/js/cookbookRunning.js:1168`

## `_ollamaModelForTask` — function, line 1148
- **called from:**
- `static/js/cookbookRunning.js:1148`
- `static/js/cookbookRunning.js:1154`

## `_ollamaUnloadCommand` — function, line 1152
- **called from:**
- `static/js/cookbookRunning.js:1152`
- `static/js/cookbookRunning.js:2941`
- `static/js/cookbookRunning.js:2972`

## `_endpointUrlForTask` — function, line 1166
- **called from:**
- `static/js/cookbookRunning.js:1166`
- `static/js/cookbookRunning.js:2939`
- `static/js/cookbookRunning.js:3016`

## `_startWaveSync` — function, line 1183
- **called from:**
- `static/js/cookbookRunning.js:1183`
- `static/js/cookbookRunning.js:1195`
- `static/js/cookbookRunning.js:3070`

## `_registerWaveEl` — function, line 1195
- **called from:**
- `static/js/cookbookRunning.js:1195`
- `static/js/cookbookRunning.js:2470`

## `_disposeTaskCard` — function, line 1201
- **called from:**
- `static/js/cookbookRunning.js:1201`
- `static/js/cookbookRunning.js:2314`
- `static/js/cookbookRunning.js:2325`
- `static/js/cookbookRunning.js:2437`

## `_showCookbookNotif` — function, line 1225
- **called from:**
- `static/js/cookbookRunning.js:1225`
- `static/js/cookbookRunning.js:3166`
- `static/js/cookbookRunning.js:3286`
- `static/js/cookbookRunning.js:3304`
- `static/js/cookbookRunning.js:3358`
- `static/js/cookbookRunning.js:3443`
- `static/js/cookbookRunning.js:3481`
- `static/js/cookbookRunning.js:3586`
- `static/js/cookbookRunning.js:3600`
- `static/js/cookbookRunning.js:3769`
- `static/js/cookbookRunning.js:3951`
- `static/js/cookbookRunning.js:4419`
- `static/js/cookbookRunning.js:4421`
- `static/js/cookbookRunning.js:4423`

## `_clearCookbookNotif` — function, line 1241
- **called from:**
- `static/js/cookbook.js:3583`
- `static/js/cookbookRunning.js:1241`
- `static/js/cookbookRunning.js:2092`
- `static/js/cookbookRunning.js:4425`
- `static/js/cookbookRunning.js:4464`

## `_presetEnvFields` — function, line 1260
- **called from:**
- `static/js/cookbookRunning.js:1260`
- `static/js/cookbookRunning.js:1290`
- `static/js/cookbookRunning.js:1346`

## `_redactPresetForStorage` — function, line 1274
- **called from:**
- `static/js/cookbookRunning.js:1274`
- `static/js/cookbookRunning.js:1290`
- `static/js/cookbookRunning.js:1342`

## `_saveTaskAsPreset` — function, line 1284
- **called from:**
- `static/js/cookbookRunning.js:1284`
- `static/js/cookbookRunning.js:2696`

## `_presetsForModelLocal` — function, line 1297
- **called from:**
- `static/js/cookbookRunning.js:1297`
- `static/js/cookbookRunning.js:1338`

## `_autoConfigLabel` — function, line 1307
- **called from:**
- `static/js/cookbookRunning.js:1307`
- `static/js/cookbookRunning.js:1345`

## `_autoSaveWorkingConfig` — function, line 1323
- **called from:**
- `static/js/cookbookRunning.js:1323`
- `static/js/cookbookRunning.js:3704`
- `static/js/cookbookRunning.js:3726`
- `static/js/cookbookRunning.js:4364`

## `_syncToServer` — function, line 1356
- **called from:**
- `static/js/cookbookRunning.js:915`
- `static/js/cookbookRunning.js:1356`
- `static/js/cookbookRunning.js:1391`
- `static/js/theme.js:687`
- `static/js/theme.js:690`

## `_normalizeState` — function, line 1398
- **called from:**
- `static/js/cookbookRunning.js:1398`
- `static/js/cookbookRunning.js:1425`

## `_syncFromServerImpl` — function, line 1421
- **called from:**
- `static/js/cookbookRunning.js:1421`
- `static/js/cookbookRunning.js:1490`

## `_syncFromServer` — function, line 1488
- **called from:**
- `static/js/cookbook.js:1980`
- `static/js/cookbook.js:3566`
- `static/js/cookbook.js:3601`
- `static/js/cookbook.js:3759`
- `static/js/cookbookRunning.js:1488`
- `static/js/cookbookRunning.js:4505`

## `clearPending` — arrow, line 1491
- **called from:**
- `static/js/fileHandler.js:249`
- `static/js/fileHandler.js:478`

## `_retryTask` — function, line 1508
- **called from:**
- `static/js/cookbookRunning.js:1508`
- `static/js/cookbookRunning.js:3032`
- `static/js/cookbookRunning.js:3264`
- `static/js/cookbookRunning.js:3272`
- `static/js/cookbookRunning.js:3436`

## `_retryDownload` — function, line 1535
- **called from:**
- `static/js/cookbook.js:2644`
- `static/js/cookbookRunning.js:1530`
- `static/js/cookbookRunning.js:1535`
- `static/js/cookbookRunning.js:3567`
- `static/js/cookbookServe.js:4065`

## `_guardServeRetry` — function, line 1593
- **called from:**
- `static/js/cookbookRunning.js:1593`
- `static/js/cookbookRunning.js:1611`
- `static/js/cookbookRunning.js:1675`
- `static/js/cookbookRunning.js:1717`
- `static/js/cookbookRunning.js:1750`

## `_serveAutoFix` — function, line 1604
- **called from:**
- `static/js/cookbook-diagnosis.js:610`
- `static/js/cookbookRunning.js:1604`

## `_openServeEditForTask` — function, line 1643
- **called from:**
- `static/js/cookbookRunning.js:252`
- `static/js/cookbookRunning.js:262`
- `static/js/cookbookRunning.js:273`
- `static/js/cookbookRunning.js:1643`
- `static/js/cookbookRunning.js:2517`
- `static/js/cookbookRunning.js:2520`
- `static/js/cookbookRunning.js:3221`

## `_serveAutoRetryReplace` — function, line 1668
- **called from:**
- `static/js/cookbook-diagnosis.js:303`
- `static/js/cookbook-diagnosis.js:304`
- `static/js/cookbook-diagnosis.js:305`
- `static/js/cookbook-diagnosis.js:312`
- `static/js/cookbook-diagnosis.js:322`
- `static/js/cookbook-diagnosis.js:323`
- `static/js/cookbook-diagnosis.js:345`
- `static/js/cookbook-diagnosis.js:346`
- `static/js/cookbook-diagnosis.js:354`
- `static/js/cookbook-diagnosis.js:355`
- `static/js/cookbook-diagnosis.js:356`
- `static/js/cookbook-diagnosis.js:357`
- `static/js/cookbook-diagnosis.js:366`
- `static/js/cookbook-diagnosis.js:367`
- `static/js/cookbook-diagnosis.js:387`
- `static/js/cookbook-diagnosis.js:388`
- `static/js/cookbook-diagnosis.js:389`
- `static/js/cookbook-diagnosis.js:397`
- `static/js/cookbook-diagnosis.js:802`
- `static/js/cookbookRunning.js:1668`

## `_serveAutoRetryRemove` — function, line 1710
- **called from:**
- `static/js/cookbook-diagnosis.js:396`
- `static/js/cookbook-diagnosis.js:404`
- `static/js/cookbook-diagnosis.js:412`
- `static/js/cookbookRunning.js:1710`

## `_serveAutoRetry` — function, line 1743
- **called from:**
- `static/js/cookbook-diagnosis.js:313`
- `static/js/cookbook-diagnosis.js:314`
- `static/js/cookbook-diagnosis.js:358`
- `static/js/cookbook-diagnosis.js:627`
- `static/js/cookbook-diagnosis.js:628`
- `static/js/cookbook-diagnosis.js:644`
- `static/js/cookbook-diagnosis.js:651`
- `static/js/cookbook-diagnosis.js:658`
- `static/js/cookbookRunning.js:1743`

## `_promptEditServeCmd` — function, line 1780
- **called from:**
- `static/js/cookbookRunning.js:1780`

## `close` — arrow, line 1798
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

## `onKey` — arrow, line 1803
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

## `_parseServeCmdToFields` — function, line 1819
- **called from:**
- `static/js/cookbookRunning.js:1649`
- `static/js/cookbookRunning.js:1650`
- `static/js/cookbookRunning.js:1819`

## `ex` — arrow, line 1821
- **called from:**
- `static/js/cookbookRunning.js:1829`
- `static/js/cookbookRunning.js:1830`
- `static/js/cookbookRunning.js:1831`
- `static/js/cookbookRunning.js:1831`
- `static/js/cookbookRunning.js:1831`
- `static/js/cookbookRunning.js:1831`
- `static/js/cookbookRunning.js:1831`
- `static/js/cookbookRunning.js:1832`
- `static/js/cookbookRunning.js:1833`
- `static/js/cookbookRunning.js:1834`
- `static/js/cookbookRunning.js:1835`
- `static/js/cookbookRunning.js:1836`
- `static/js/cookbookRunning.js:1837`
- `static/js/cookbookRunning.js:1838`
- `static/js/cookbookRunning.js:1839`
- `static/js/cookbookRunning.js:1840`
- `static/js/cookbookRunning.js:1841`
- `static/js/cookbookRunning.js:1842`
- `static/js/cookbookRunning.js:1843`
- `static/js/cookbookRunning.js:1844`
- `static/js/cookbookRunning.js:1845`
- `static/js/cookbookRunning.js:1846`

## `_serveCmdNeedsGpuPreflight` — function, line 1863
- **called from:**
- `static/js/cookbookRunning.js:1863`
- `static/js/cookbookRunning.js:1930`

## `_selectedGpuIndexes` — function, line 1870
- **called from:**
- `static/js/cookbookRunning.js:1870`
- `static/js/cookbookRunning.js:1941`

## `_gbFromMb` — function, line 1889
- **called from:**
- `static/js/cookbookRunning.js:1889`
- `static/js/cookbookRunning.js:1907`
- `static/js/cookbookRunning.js:1919`
- `static/js/cookbookRunning.js:1919`
- `static/js/cookbookRunning.js:1921`
- `static/js/cookbookRunning.js:1921`

## `_gpuPreflightIssues` — function, line 1895
- **called from:**
- `static/js/cookbookRunning.js:1895`
- `static/js/cookbookRunning.js:1942`

## `_confirmGpuPreflight` — function, line 1929
- **called from:**
- `static/js/cookbookRunning.js:1929`
- `static/js/cookbookRunning.js:2046`

## `_launchServeTask` — function, line 1957
- **called from:**
- `static/js/cookbook-diagnosis.js:202`
- `static/js/cookbook-diagnosis.js:218`
- `static/js/cookbook-diagnosis.js:664`
- `static/js/cookbook-diagnosis.js:675`
- `static/js/cookbook-diagnosis.js:762`
- `static/js/cookbook-diagnosis.js:787`
- `static/js/cookbook-diagnosis.js:809`
- `static/js/cookbook-diagnosis.js:828`
- `static/js/cookbook-diagnosis.js:833`
- `static/js/cookbook.js:2315`
- `static/js/cookbookRunning.js:1522`
- `static/js/cookbookRunning.js:1631`
- `static/js/cookbookRunning.js:1704`
- `static/js/cookbookRunning.js:1737`
- `static/js/cookbookRunning.js:1771`
- `static/js/cookbookRunning.js:1957`
- `static/js/cookbookRunning.js:3170`
- `static/js/cookbookServe.js:3816`

## `_renderRunningTab` — function, line 2085
- **called from:**
- `static/js/cookbook-hwfit.js:2036`
- `static/js/cookbook.js:3534`
- `static/js/cookbook.js:3562`
- `static/js/cookbook.js:3584`
- `static/js/cookbook.js:3765`
- `static/js/cookbook.js:3786`
- `static/js/cookbookDownload.js:574`
- `static/js/cookbookDownload.js:610`
- `static/js/cookbookDownload.js:623`
- `static/js/cookbookRunning.js:685`
- `static/js/cookbookRunning.js:711`
- `static/js/cookbookRunning.js:717`
- `static/js/cookbookRunning.js:738`
- `static/js/cookbookRunning.js:741`
- `static/js/cookbookRunning.js:744`
- `static/js/cookbookRunning.js:944`
- `static/js/cookbookRunning.js:990`
- `static/js/cookbookRunning.js:1571`
- `static/js/cookbookRunning.js:2085`
- `static/js/cookbookRunning.js:2165`
- `static/js/cookbookRunning.js:2334`
- `static/js/cookbookRunning.js:2573`
- `static/js/cookbookRunning.js:2679`
- `static/js/cookbookRunning.js:2698`
- `static/js/cookbookRunning.js:3306`
- `static/js/cookbookRunning.js:3360`
- `static/js/cookbookRunning.js:3367`
- `static/js/cookbookRunning.js:3782`
- `static/js/cookbookRunning.js:4104`
- `static/js/cookbookRunning.js:4211`
- `static/js/cookbookRunning.js:4328`

## `_ensureSection` — function, line 2210
- **called from:**
- `static/js/cookbookRunning.js:2210`
- `static/js/cookbookRunning.js:2272`

## `_taskServerKey` — arrow, line 2226
- **called from:**
- `static/js/cookbookRunning.js:2243`
- `static/js/cookbookRunning.js:2292`
- `static/js/cookbookRunning.js:2297`
- `static/js/cookbookRunning.js:2307`
- `static/js/cookbookRunning.js:2346`
- `static/js/cookbookRunning.js:3052`

## `_serverName` — arrow, line 2227
- **called from:**
- `static/js/cookbookRunning.js:2244`
- `static/js/cookbookRunning.js:2299`
- `static/js/cookbookRunning.js:2300`
- `static/js/cookbookRunning.js:2305`
- `static/js/cookbookRunning.js:2347`
- `static/js/cookbookRunning.js:2348`
- `static/js/cookbookRunning.js:2358`

## `_openEdit` — arrow, line 2517
- **called from:**
- `static/js/cookbookRunning.js:2692`

## `_lpStart` — arrow, line 2628
- **called from:**
- `static/js/cookbookRunning.js:2650`

## `_lpCancel` — arrow, line 2639
- **called from:**
- `static/js/cookbookRunning.js:2644`
- `static/js/memory.js:1098`
- `static/js/skills.js:1075`

## `_lpMove` — arrow, line 2642
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_openTaskMenu` — arrow, line 2656
- **called from:**
- `static/js/cookbookRunning.js:2902`

## `closeHandler` — arrow, line 2872
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `scrollClose` — arrow, line 2880
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_unreg` — arrow, line 2881
- **called from:**
- `static/js/cookbookRunning.js:2883`
- `static/js/documentLibrary.js:371`
- `static/js/documentLibrary.js:411`

## `_cleanup` — arrow, line 2882
- **called from:**
- `scripts/diffusion_server.py:439`
- `scripts/diffusion_server.py:443`
- `scripts/diffusion_server.py:457`
- `scripts/diffusion_server.py:468`
- `scripts/diffusion_server.py:488`
- `scripts/diffusion_server.py:504`
- `scripts/diffusion_server.py:635`
- `src/agent_runtime/effect_adapters.py:353`
- `tests/test_process_lifecycle.py:248`
- `tests/test_process_lifecycle.py:269`
- `tests/test_process_lifecycle.py:295`
- `static/js/compare/index.js:1524`
- `static/js/cookbookRunning.js:2840`
- `static/js/cookbookRunning.js:2874`
- `static/js/cookbookRunning.js:2880`
- `static/js/document.js:13672`
- `static/js/document.js:14367`
- `static/js/document.js:14439`
- `static/js/emailInbox.js:1261`
- `static/js/emailInbox.js:1269`
- `static/js/emailInbox.js:1274`

## `_reconnectTask` — function, line 3096
- **called from:**
- `static/js/cookbookRunning.js:2608`
- `static/js/cookbookRunning.js:2923`
- `static/js/cookbookRunning.js:3066`
- `static/js/cookbookRunning.js:3096`
- `static/js/cookbookRunning.js:3246`
- `static/js/cookbookRunning.js:3344`

## `_trySelectModel` — arrow, line 3735
- **called from:**
- `static/js/cookbookRunning.js:3751`
- `static/js/cookbookRunning.js:3754`

## `_hasLiveTasks` — function, line 3806
- **called from:**
- `static/js/cookbookRunning.js:3806`
- `static/js/cookbookRunning.js:4128`
- `static/js/cookbookRunning.js:4507`

## `_isRunningTabVisible` — function, line 3816
- **called from:**
- `static/js/cookbookRunning.js:3065`
- `static/js/cookbookRunning.js:3099`
- `static/js/cookbookRunning.js:3109`
- `static/js/cookbookRunning.js:3816`
- `static/js/cookbookRunning.js:3889`
- `static/js/cookbookRunning.js:4128`

## `_isCookbookVisible` — function, line 3823
- **called from:**
- `static/js/cookbookRunning.js:3823`
- `static/js/cookbookRunning.js:4155`
- `static/js/cookbookRunning.js:4164`

## `_foregroundChatBusy` — function, line 3833
- **called from:**
- `static/js/cookbook.js:3716`
- `static/js/cookbook.js:3748`
- `static/js/cookbookRunning.js:3833`
- `static/js/cookbookRunning.js:3863`
- `static/js/cookbookRunning.js:3888`
- `static/js/cookbookRunning.js:4155`
- `static/js/cookbookRunning.js:4164`

## `_claimBackgroundLeader` — function, line 3841
- **called from:**
- `static/js/cookbookRunning.js:3841`
- `static/js/cookbookRunning.js:3865`

## `_canBackgroundPoll` — function, line 3862
- **called from:**
- `static/js/cookbookRunning.js:3862`
- `static/js/cookbookRunning.js:4121`
- `static/js/cookbookRunning.js:4132`
- `static/js/cookbookRunning.js:4187`

## `_fetchWithTimeout` — function, line 3871
- **called from:**
- `static/js/admin.js:2341`
- `static/js/admin.js:2352`
- `static/js/cookbookRunning.js:536`
- `static/js/cookbookRunning.js:543`
- `static/js/cookbookRunning.js:703`
- `static/js/cookbookRunning.js:1381`
- `static/js/cookbookRunning.js:1423`
- `static/js/cookbookRunning.js:1513`
- `static/js/cookbookRunning.js:1541`
- `static/js/cookbookRunning.js:1615`
- `static/js/cookbookRunning.js:1678`
- `static/js/cookbookRunning.js:1720`
- `static/js/cookbookRunning.js:1753`
- `static/js/cookbookRunning.js:1935`
- `static/js/cookbookRunning.js:1976`
- `static/js/cookbookRunning.js:1998`
- `static/js/cookbookRunning.js:2051`
- `static/js/cookbookRunning.js:2579`
- `static/js/cookbookRunning.js:2713`
- `static/js/cookbookRunning.js:2732`
- `static/js/cookbookRunning.js:2944`
- `static/js/cookbookRunning.js:2953`
- `static/js/cookbookRunning.js:2975`
- `static/js/cookbookRunning.js:2984`
- `static/js/cookbookRunning.js:2995`
- `static/js/cookbookRunning.js:3020`
- `static/js/cookbookRunning.js:3024`
- `static/js/cookbookRunning.js:3114`
- `static/js/cookbookRunning.js:3128`
- `static/js/cookbookRunning.js:3327`
- `static/js/cookbookRunning.js:3445`
- `static/js/cookbookRunning.js:3463`
- `static/js/cookbookRunning.js:3560`
- `static/js/cookbookRunning.js:3602`
- `static/js/cookbookRunning.js:3686`
- `static/js/cookbookRunning.js:3719`
- `static/js/cookbookRunning.js:3871`
- `static/js/cookbookRunning.js:3908`
- `static/js/cookbookRunning.js:3909`
- `static/js/cookbookRunning.js:4072`
- `static/js/cookbookRunning.js:4168`
- `static/js/cookbookRunning.js:4171`
- `static/js/cookbookRunning.js:4194`
- `static/js/cookbookRunning.js:4217`
- `static/js/cookbookRunning.js:4374`
- `static/js/cookbookRunning.js:4400`

## `_checkServeReachability` — function, line 3885
- **called from:**
- `static/js/cookbookRunning.js:3885`
- `static/js/cookbookRunning.js:4123`
- `static/js/cookbookRunning.js:4134`

## `_serveTaskFailed` — function, line 3961
- **called from:**
- `static/js/cookbookRunning.js:3961`

## `_setServerDot` — function, line 3966
- **called from:**
- `static/js/cookbookRunning.js:3966`
- `static/js/cookbookRunning.js:3982`
- `static/js/cookbookRunning.js:3990`
- `static/js/cookbookRunning.js:4023`

## `_syncSettingsServerDots` — function, line 3973
- **called from:**
- `static/js/cookbookRunning.js:3973`
- `static/js/cookbookRunning.js:4025`

## `_refreshServerDots` — function, line 4011
- **called from:**
- `static/js/cookbookRunning.js:965`
- `static/js/cookbookRunning.js:3640`
- `static/js/cookbookRunning.js:3953`
- `static/js/cookbookRunning.js:4011`

## `_taskServerKeyForDot` — arrow, line 4015
- **called from:**
- `static/js/cookbookRunning.js:4016`
- `static/js/cookbookRunning.js:4016`

## `_selfHealStaleTasksImpl` — function, line 4037
- **called from:**
- `static/js/cookbookRunning.js:4037`
- `static/js/cookbookRunning.js:4110`

## `_selfHealStaleTasks` — function, line 4108
- **called from:**
- `static/js/cookbook.js:3641`
- `static/js/cookbookRunning.js:3284`
- `static/js/cookbookRunning.js:4108`
- `static/js/cookbookRunning.js:4129`

## `_startBackgroundMonitor` — function, line 4118
- **called from:**
- `static/js/cookbookRunning.js:739`
- `static/js/cookbookRunning.js:947`
- `static/js/cookbookRunning.js:1572`
- `static/js/cookbookRunning.js:4118`
- `static/js/cookbookRunning.js:4507`

## `_stopBackgroundMonitor` — function, line 4138
- **called from:**
- `static/js/cookbookRunning.js:4138`
- `static/js/cookbookRunning.js:4426`

## `_probeEndpointUntilOnline` — function, line 4154
- **called from:**
- `static/js/cookbookRunning.js:2723`
- `static/js/cookbookRunning.js:2741`
- `static/js/cookbookRunning.js:3708`
- `static/js/cookbookRunning.js:3732`
- `static/js/cookbookRunning.js:4154`
- `static/js/cookbookRunning.js:4389`
- `static/js/cookbookRunning.js:4410`

## `_pollBackgroundStatus` — function, line 4186
- **called from:**
- `static/js/cookbookRunning.js:4122`
- `static/js/cookbookRunning.js:4133`
- `static/js/cookbookRunning.js:4186`

## `initRunning` — function, line 4475
- **called from:**
- `static/js/cookbook.js:3852`
- `static/js/cookbookRunning.js:4475`
