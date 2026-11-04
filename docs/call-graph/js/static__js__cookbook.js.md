# `static/js/cookbook.js` — definitions & call sites

119 definitions (regex-based, best-effort).
**Exports:** `_MODELDIR_CHECK_OFF`, `_MODELDIR_CHECK_ON`, `_applyServerSelectColor`, `_buildEnvPrefix`, `_buildServeCmd`, `_copyText`, `_currentServerValue`, `_detectBackend`, `_detectReasoningParser`, `_detectToolParser`, `_envState`, `_getPlatform`, `_isMetal`, `_isWindows`, `_lastCacheHost`, `_loadPresets`, `_persistEnvState`, `_psQuote`, `_savePresets`, `_selectedServer`, `_serverByVal`, `_serverDefaultHtml`, `_serverEntryHtml`, `_serverKey`, `_setLastCacheHost`, `_shellQuote`, `_sshCmd`, `_syncServerSelectColors`, `close`, `default`, `esc`, `isVisible`, `modelLogo`, `open`

## `_normalizeCookbookModelDir` — function, line 63
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

## `_platformIcon` — function, line 70
- **called from:**
- `static/js/cookbook.js:70`
- `static/js/cookbook.js:2923`

## `_lastCacheHost` — function, line 87
- **called from:**
- `static/js/cookbook-hwfit.js:756`
- `static/js/cookbook.js:87`

## `_setLastCacheHost` — function, line 88
- **called from:**
- `static/js/cookbook-hwfit.js:772`
- `static/js/cookbook-hwfit.js:785`
- `static/js/cookbook.js:88`

## `_setCookbookOpening` — function, line 90
- **called from:**
- `static/js/cookbook.js:90`
- `static/js/cookbook.js:3364`
- `static/js/cookbook.js:3437`

## `_isLocalEntry` — function, line 124
- **called from:**
- `static/js/cookbook.js:124`
- `static/js/cookbook.js:130`
- `static/js/cookbook.js:278`
- `static/js/cookbook.js:2054`

## `_serverKey` — function, line 129
- **called from:**
- `static/js/cookbook-hwfit.js:1532`
- `static/js/cookbook-hwfit.js:2271`
- `static/js/cookbook-hwfit.js:2498`
- `static/js/cookbook-hwfit.js:2802`
- `static/js/cookbook.js:129`
- `static/js/cookbook.js:143`
- `static/js/cookbook.js:161`
- `static/js/cookbook.js:280`
- `static/js/cookbook.js:1908`
- `static/js/cookbookDownload.js:493`
- `static/js/cookbookRunning.js:364`
- `static/js/cookbookRunning.js:1921`

## `_serverByVal` — function, line 140
- **called from:**
- `static/js/cookbook-hwfit.js:553`
- `static/js/cookbook-hwfit.js:757`
- `static/js/cookbook-hwfit.js:811`
- `static/js/cookbook-hwfit.js:1528`
- `static/js/cookbook-hwfit.js:1915`
- `static/js/cookbook-hwfit.js:2321`
- `static/js/cookbook-hwfit.js:2498`
- `static/js/cookbook-hwfit.js:2504`
- `static/js/cookbook-hwfit.js:2799`
- `static/js/cookbook.js:140`
- `static/js/cookbook.js:152`
- `static/js/cookbook.js:243`
- `static/js/cookbook.js:303`
- `static/js/cookbook.js:317`
- `static/js/cookbook.js:1097`
- `static/js/cookbook.js:1408`
- `static/js/cookbook.js:1905`
- `static/js/cookbook.js:2120`
- `static/js/cookbook.js:2526`
- `static/js/cookbook.js:2642`
- `static/js/cookbookRunning.js:360`
- `static/js/cookbookRunning.js:361`
- `static/js/cookbookRunning.js:1918`
- `static/js/cookbookRunning.js:1919`
- `static/js/cookbookRunning.js:2180`
- `static/js/cookbookRunning.js:2187`

## `_selectedServer` — function, line 150
- **called from:**
- `static/js/cookbook.js:150`
- `static/js/cookbook.js:160`
- `static/js/cookbook.js:302`
- `static/js/cookbook.js:316`

## `_currentServerValue` — function, line 159
- **called from:**
- `static/js/cookbook-hwfit.js:470`
- `static/js/cookbook-hwfit.js:755`
- `static/js/cookbook-hwfit.js:2262`
- `static/js/cookbook-hwfit.js:2275`
- `static/js/cookbook-hwfit.js:2501`
- `static/js/cookbook-hwfit.js:2815`
- `static/js/cookbook.js:159`
- `static/js/cookbook.js:1919`
- `static/js/cookbook.js:1940`
- `static/js/cookbook.js:2069`

## `_isGemma4ThinkingModel` — function, line 167
- **called from:**
- `static/js/cookbook.js:167`
- `static/js/cookbook.js:173`

## `_gemma4ThinkingChatTemplateArg` — function, line 172
- **called from:**
- `static/js/cookbook.js:172`
- `static/js/cookbook.js:714`
- `static/js/cookbook.js:762`

## `_serverColorValue` — function, line 194
- **called from:**
- `static/js/cookbook.js:194`
- `static/js/cookbook.js:200`
- `static/js/cookbook.js:2034`

## `_serverColor` — function, line 199
- **called from:**
- `static/js/cookbook.js:199`
- `static/js/cookbook.js:210`
- `static/js/cookbook.js:214`
- `static/js/cookbook.js:224`
- `static/js/cookbook.js:2904`

## `_serverColorLabel` — function, line 203
- **called from:**
- `static/js/cookbook.js:203`
- `static/js/cookbook.js:2910`
- `static/js/cookbook.js:2910`
- `static/js/cookbook.js:2914`

## `_autoServerColor` — function, line 208
- **called from:**
- `static/js/cookbook.js:208`
- `static/js/cookbook.js:224`

## `_resolvedServerColor` — function, line 223
- **called from:**
- `static/js/cookbook.js:223`
- `static/js/cookbook.js:245`
- `static/js/cookbook.js:271`
- `static/js/cookbook.js:281`
- `static/js/cookbook.js:2905`

## `_serverOptionLabel` — function, line 227
- **called from:**
- `static/js/cookbook.js:227`
- `static/js/cookbook.js:272`
- `static/js/cookbook.js:287`

## `_serverOptionStyle` — function, line 231
- **called from:**
- `static/js/cookbook.js:231`
- `static/js/cookbook.js:272`
- `static/js/cookbook.js:287`

## `_serverColorOptionStyle` — function, line 235
- **called from:**
- `static/js/cookbook.js:235`
- `static/js/cookbook.js:2908`

## `_serverColorForValue` — function, line 242
- **called from:**
- `static/js/cookbook.js:242`
- `static/js/cookbook.js:250`

## `_applyServerSelectColor` — function, line 248
- **called from:**
- `static/js/cookbook-hwfit.js:2277`
- `static/js/cookbook-hwfit.js:2808`
- `static/js/cookbook-hwfit.js:2816`
- `static/js/cookbook.js:248`
- `static/js/cookbook.js:1933`
- `static/js/cookbook.js:2073`

## `_syncServerSelectColors` — function, line 260
- **called from:**
- `static/js/cookbook-hwfit.js:2824`
- `static/js/cookbook.js:260`
- `static/js/cookbook.js:2195`

## `_buildServerOpts` — function, line 264
- **called from:**
- `static/js/cookbook.js:264`
- `static/js/cookbook.js:1929`
- `static/js/cookbook.js:3049`
- `static/js/cookbook.js:3092`
- `static/js/cookbook.js:3198`
- `static/js/cookbook.js:3231`

## `_sshCmd` — function, line 293
- **called from:**
- `static/js/cookbook-diagnosis.js:1050`
- `static/js/cookbook.js:293`
- `static/js/cookbookDownload.js:201`
- `static/js/cookbookDownload.js:357`
- `static/js/cookbookServe.js:3848`

## `_getPort` — function, line 299
- **called from:**
- `static/js/cookbook.js:299`
- `static/js/cookbook.js:301`
- `static/js/cookbook.js:1101`
- `static/js/cookbook.js:1469`
- `static/js/cookbook.js:1546`
- `static/js/cookbook.js:1607`
- `static/js/cookbook.js:1755`
- `static/js/cookbook.js:1802`
- `static/js/cookbook.js:2535`
- `static/js/cookbookDownload.js:201`
- `static/js/cookbookDownload.js:357`
- `static/js/cookbookDownload.js:533`
- `static/js/cookbookRunning.js:919`
- `static/js/cookbookRunning.js:1016`
- `static/js/cookbookRunning.js:1025`
- `static/js/cookbookRunning.js:1056`
- `static/js/cookbookRunning.js:1076`
- `static/js/cookbookRunning.js:1103`
- `static/js/cookbookRunning.js:1120`
- `static/js/cookbookRunning.js:1157`
- `static/js/cookbookRunning.js:1992`
- `static/js/cookbookRunning.js:2021`
- `static/js/cookbookRunning.js:2700`
- `static/js/cookbookServe.js:737`
- `static/js/cookbookServe.js:3831`
- `static/js/cookbookServe.js:3848`
- `static/js/cookbookServe.js:3936`
- `static/js/cookbookServe.js:4180`

## `_getPlatform` — function, line 308
- **called from:**
- `static/js/cookbook.js:308`
- `static/js/cookbook.js:314`
- `static/js/cookbook.js:323`
- `static/js/cookbook.js:2536`
- `static/js/cookbookRunning.js:920`
- `static/js/cookbookServe.js:3939`
- `static/js/cookbookServe.js:4180`

## `_isWindows` — function, line 322
- **called from:**
- `static/js/cookbook-hwfit.js:917`
- `static/js/cookbook.js:322`
- `static/js/cookbook.js:536`
- `static/js/cookbook.js:613`
- `static/js/cookbook.js:796`
- `static/js/cookbook.js:796`
- `static/js/cookbook.js:951`
- `static/js/cookbook.js:974`
- `static/js/cookbook.js:989`
- `static/js/cookbook.js:1176`
- `static/js/cookbook.js:1428`
- `static/js/cookbook.js:1434`
- `static/js/cookbook.js:1450`
- `static/js/cookbookDownload.js:119`
- `static/js/cookbookDownload.js:141`
- `static/js/cookbookDownload.js:520`
- `static/js/cookbookRunning.js:1011`
- `static/js/cookbookRunning.js:1070`
- `static/js/cookbookRunning.js:1086`
- `static/js/cookbookRunning.js:1112`
- `static/js/cookbookRunning.js:1973`
- `static/js/cookbookRunning.js:2696`
- `static/js/cookbookServe.js:3815`

## `_isMetal` — function, line 329
- **called from:**
- `static/js/cookbook.js:329`
- `static/js/cookbookServe.js:205`
- `static/js/cookbookServe.js:753`

## `_isStepFunStepModel` — function, line 334
- **called from:**
- `static/js/cookbook.js:334`
- `static/js/cookbook.js:349`
- `static/js/cookbook.js:434`
- `static/js/cookbook.js:473`

## `_detectModelOptimizations` — function, line 342
- **called from:**
- `static/js/cookbook.js:342`
- `static/js/cookbook.js:692`
- `static/js/cookbookServe.js:1437`
- `static/js/cookbookServe.js:1685`

## `_detectReasoningParser` — function, line 430
- **called from:**
- `static/js/cookbook.js:396`
- `static/js/cookbook.js:430`
- `static/js/cookbook.js:740`
- `static/js/cookbook.js:775`

## `_detectToolParser` — function, line 471
- **called from:**
- `static/js/cookbook-hwfit.js:1866`
- `static/js/cookbook.js:471`
- `static/js/cookbook.js:734`
- `static/js/cookbook.js:771`
- `static/js/cookbookServe.js:1407`

## `_detectBackend` — function, line 495
- **called from:**
- `static/js/cookbook-hwfit.js:546`
- `static/js/cookbook-hwfit.js:576`
- `static/js/cookbook-hwfit.js:1277`
- `static/js/cookbook-hwfit.js:1623`
- `static/js/cookbook-hwfit.js:1705`
- `static/js/cookbook-hwfit.js:1871`
- `static/js/cookbook.js:495`
- `static/js/cookbookServe.js:1162`
- `static/js/cookbookServe.js:1416`
- `static/js/cookbookServe.js:3333`

## `_shellQuote` — function, line 560
- **called from:**
- `static/js/cookbook-hwfit.js:1884`
- `static/js/cookbook-hwfit.js:1887`
- `static/js/cookbook-hwfit.js:1907`
- `static/js/cookbook-hwfit.js:1909`
- `static/js/cookbook.js:174`
- `static/js/cookbook.js:560`
- `static/js/cookbook.js:618`
- `static/js/cookbook.js:620`
- `static/js/cookbook.js:623`
- `static/js/cookbook.js:625`
- `static/js/cookbook.js:962`
- `static/js/cookbook.js:966`
- `static/js/cookbook.js:976`
- `static/js/cookbook.js:981`
- `static/js/cookbook.js:983`
- `static/js/cookbook.js:991`
- `static/js/cookbook.js:1246`
- `static/js/cookbook.js:1459`
- `static/js/cookbook.js:1461`
- `static/js/cookbook.js:1747`
- `static/js/cookbook.js:1749`
- `static/js/cookbook.js:2547`
- `static/js/cookbook.js:2549`
- `static/js/cookbookServe.js:1075`
- `static/js/cookbookServe.js:1076`
- `static/js/cookbookServe.js:1091`
- `static/js/cookbookServe.js:1095`
- `static/js/cookbookServe.js:1096`
- `static/js/cookbookServe.js:1875`
- `static/js/cookbookServe.js:3955`
- `static/js/cookbookServe.js:3957`

## `_listField` — function, line 564
- **called from:**
- `static/js/cookbook.js:564`
- `static/js/cookbook.js:727`
- `static/js/cookbook.js:965`
- `static/js/cookbook.js:984`
- `static/js/cookbook.js:986`

## `_numField` — function, line 571
- **called from:**
- `static/js/cookbook.js:571`
- `static/js/cookbook.js:961`
- `static/js/cookbook.js:967`

## `_psQuote` — function, line 576
- **called from:**
- `static/js/cookbook.js:576`
- `static/js/cookbook.js:636`
- `static/js/cookbook.js:638`
- `static/js/cookbook.js:640`
- `static/js/cookbook.js:642`
- `static/js/cookbook.js:1452`
- `static/js/cookbook.js:1454`
- `static/js/cookbook.js:2540`
- `static/js/cookbook.js:2542`
- `static/js/cookbookDownload.js:542`
- `static/js/cookbookRunning.js:1975`
- `static/js/cookbookServe.js:3948`
- `static/js/cookbookServe.js:3950`

## `_gpuEnvVarName` — function, line 587
- **called from:**
- `static/js/cookbook.js:587`
- `static/js/cookbook.js:606`
- `static/js/cookbook.js:624`
- `static/js/cookbook.js:641`

## `_gpuEnvPrefix` — function, line 603
- **called from:**
- `static/js/cookbook.js:603`
- `static/js/cookbook.js:690`
- `static/js/cookbook.js:754`
- `static/js/cookbook.js:828`
- `static/js/cookbook.js:832`
- `static/js/cookbook.js:950`

## `_buildEnvPrefix` — function, line 612
- **called from:**
- `static/js/cookbook.js:612`
- `static/js/cookbookDownload.js:198`
- `static/js/cookbookDownload.js:354`

## `_buildEnvPrefixWindows` — function, line 631
- **called from:**
- `static/js/cookbook.js:613`
- `static/js/cookbook.js:631`

## `_venvRootFromPath` — function, line 647
- **called from:**
- `static/js/cookbook.js:647`
- `static/js/cookbook.js:680`
- `static/js/cookbookRunning.js:145`
- `static/js/cookbookRunning.js:1981`

## `_venvLooksWrongForPlatform` — function, line 654
- **called from:**
- `static/js/cookbook.js:654`
- `static/js/cookbook.js:679`

## `_isDeepSeekV4Model` — function, line 663
- **called from:**
- `static/js/cookbook.js:663`
- `static/js/cookbook.js:755`

## `_envHasKey` — function, line 668
- **called from:**
- `static/js/cookbook.js:668`
- `static/js/cookbook.js:757`

## `_buildServeCmd` — function, line 672
- **called from:**
- `static/js/cookbook.js:672`
- `static/js/cookbookDownload.js:353`
- `static/js/cookbookServe.js:1899`

## `lcPrefix` — arrow, line 822
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_llamaNum` — arrow, line 845
- **called from:**
- `static/js/cookbook.js:883`
- `static/js/cookbook.js:885`
- `static/js/cookbook.js:887`
- `static/js/cookbook.js:889`

## `_llamaCsv` — arrow, line 849
- **called from:**
- `static/js/cookbook.js:881`

## `modelLogo` — function, line 1006
- **called from:**
- `static/js/cookbook-hwfit.js:1424`
- `static/js/cookbook.js:1006`
- `static/js/cookbookRunning.js:2404`
- `static/js/cookbookServe.js:1159`

## `_copyText` — function, line 1017
- **called from:**
- `static/js/cookbook-diagnosis.js:271`
- `static/js/cookbook-diagnosis.js:272`
- `static/js/cookbook-diagnosis.js:281`
- `static/js/cookbook-diagnosis.js:321`
- `static/js/cookbook-diagnosis.js:364`
- `static/js/cookbook-diagnosis.js:503`
- `static/js/cookbook-diagnosis.js:536`
- `static/js/cookbook-diagnosis.js:537`
- `static/js/cookbook-diagnosis.js:546`
- `static/js/cookbook-diagnosis.js:556`
- `static/js/cookbook-diagnosis.js:565`
- `static/js/cookbook-diagnosis.js:578`
- `static/js/cookbook-diagnosis.js:669`
- `static/js/cookbook-diagnosis.js:685`
- `static/js/cookbook-diagnosis.js:686`
- `static/js/cookbook-diagnosis.js:687`
- `static/js/cookbook-diagnosis.js:695`
- `static/js/cookbook-diagnosis.js:703`
- `static/js/cookbook-diagnosis.js:711`
- `static/js/cookbook-diagnosis.js:737`
- `static/js/cookbook-diagnosis.js:963`
- `static/js/cookbook-hwfit.js:1051`
- `static/js/cookbook-hwfit.js:2533`
- `static/js/cookbook.js:1017`
- `static/js/cookbookDownload.js:302`
- `static/js/cookbookDownload.js:330`
- `static/js/cookbookRunning.js:2703`
- `static/js/cookbookRunning.js:2709`
- `static/js/cookbookRunning.js:2715`
- `static/js/cookbookRunning.js:2727`
- `static/js/cookbookRunning.js:2986`
- `static/js/cookbookRunning.js:3211`
- `static/js/cookbookRunning.js:3219`
- `static/js/cookbookServe.js:2715`
- `static/js/cookbookServe.js:3730`

## `_fallbackCopy` — function, line 1024
- **called from:**
- `static/js/cookbook.js:1019`
- `static/js/cookbook.js:1021`
- `static/js/cookbook.js:1024`

## `_loadPresets` — function, line 1039
- **called from:**
- `static/js/cookbook.js:1039`
- `static/js/cookbook.js:2990`
- `static/js/cookbookDownload.js:317`
- `static/js/cookbookRunning.js:514`
- `static/js/cookbookRunning.js:1258`
- `static/js/cookbookRunning.js:1300`
- `static/js/cookbookRunning.js:1341`
- `static/js/cookbookServe.js:1463`
- `static/js/cookbookServe.js:2340`
- `static/js/cookbookServe.js:2463`
- `static/js/cookbookServe.js:2475`
- `static/js/cookbookServe.js:2514`
- `static/js/cookbookServe.js:2589`
- `static/js/cookbookServe.js:2602`

## `_savePresets` — function, line 1044
- **called from:**
- `static/js/cookbook.js:1044`
- `static/js/cookbookDownload.js:319`
- `static/js/cookbookRunning.js:1261`
- `static/js/cookbookRunning.js:1304`
- `static/js/cookbookRunning.js:1318`
- `static/js/cookbookServe.js:2503`
- `static/js/cookbookServe.js:2593`
- `static/js/cookbookServe.js:2607`

## `_envStateForStorage` — function, line 1050
- **called from:**
- `static/js/cookbook.js:1050`
- `static/js/cookbook.js:1062`
- `static/js/cookbook.js:2063`

## `_readStoredEnvState` — function, line 1055
- **called from:**
- `static/js/cookbook.js:1055`
- `static/js/cookbook.js:1953`
- `static/js/cookbook.js:3392`
- `static/js/cookbook.js:3550`
- `static/js/cookbook.js:3572`

## `_persistEnvState` — function, line 1061
- **called from:**
- `static/js/cookbook-diagnosis.js:415`
- `static/js/cookbook-hwfit.js:1538`
- `static/js/cookbook-hwfit.js:2323`
- `static/js/cookbook-hwfit.js:2486`
- `static/js/cookbook-hwfit.js:2499`
- `static/js/cookbook-hwfit.js:2807`
- `static/js/cookbook.js:1061`
- `static/js/cookbook.js:1918`
- `static/js/cookbook.js:2862`
- `static/js/cookbook.js:3036`
- `static/js/cookbookDownload.js:250`
- `static/js/cookbookDownload.js:251`
- `static/js/cookbookDownload.js:252`
- `static/js/cookbookDownload.js:253`

## `_fetchDependencies` — function, line 1071
- **called from:**
- `static/js/cookbook.js:1071`
- `static/js/cookbook.js:1619`
- `static/js/cookbook.js:1992`
- `static/js/cookbook.js:2192`

## `_statusTag` — arrow, line 1132
- **called from:**
- `static/js/cookbook.js:1232`

## `_depGlyphHtml` — arrow, line 1168
- **called from:**
- `static/js/cookbook.js:1224`

## `_depRow` — arrow, line 1173
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_recipeRuntimeCommands` — function, line 1242
- **called from:**
- `static/js/cookbook.js:1242`
- `static/js/cookbook.js:1250`
- `static/js/cookbook.js:1280`
- `static/js/cookbook.js:1665`

## `_recipeDisplayText` — function, line 1249
- **called from:**
- `static/js/cookbook.js:1249`
- `static/js/cookbook.js:1292`
- `static/js/cookbook.js:1668`

## `_recipePanelHtml` — function, line 1265
- **called from:**
- `static/js/cookbook.js:1199`
- `static/js/cookbook.js:1265`

## `_rowsHtml` — arrow, line 1301
- **called from:**
- `static/js/cookbook.js:1305`
- `static/js/cookbook.js:1339`
- `static/js/cookbook.js:1344`

## `_sectionHeader` — arrow, line 1302
- **called from:**
- `static/js/cookbook.js:1305`
- `static/js/cookbook.js:1338`
- `static/js/cookbook.js:1369`

## `_section` — arrow, line 1304
- **called from:**
- `static/js/cookbook.js:1357`
- `static/js/cookbook.js:1381`

## `_sortDeps` — arrow, line 1312
- **called from:**
- `static/js/cookbook.js:1332`
- `static/js/cookbook.js:1372`

## `_serverDepsHtml` — arrow, line 1322
- **called from:**
- `static/js/cookbook.js:1393`

## `_appDepsHtml` — arrow, line 1361
- **called from:**
- `static/js/cookbook.js:1392`

## `_visibleDep` — arrow, line 1387
- **called from:**
- `static/js/cookbook.js:1388`
- `static/js/cookbook.js:1389`

## `_installDep` — function, line 1399
- **called from:**
- `static/js/cookbook.js:1399`
- `static/js/cookbook.js:1514`
- `static/js/cookbook.js:1850`

## `_refreshRecipePre` — function, line 1658
- **called from:**
- `static/js/cookbook.js:1658`
- `static/js/cookbook.js:1674`
- `static/js/cookbook.js:1694`

## `_rebuildLlamaCpp` — function, line 1780
- **called from:**
- `static/js/cookbook.js:1780`
- `static/js/cookbook.js:1862`
- `static/js/cookbook.js:1872`

## `_showDepMenu` — function, line 1827
- **called from:**
- `static/js/cookbook.js:1827`
- `static/js/cookbook.js:1887`

## `_applyServerSelection` — function, line 1897
- **called from:**
- `static/js/cookbook.js:1409`
- `static/js/cookbook.js:1537`
- `static/js/cookbook.js:1597`
- `static/js/cookbook.js:1730`
- `static/js/cookbook.js:1782`
- `static/js/cookbook.js:1897`
- `static/js/cookbook.js:1947`
- `static/js/cookbook.js:1954`
- `static/js/cookbook.js:2093`
- `static/js/cookbook.js:2114`
- `static/js/cookbook.js:2189`
- `static/js/cookbook.js:2209`
- `static/js/cookbook.js:2231`

## `_refreshScanDownloadTarget` — function, line 1937
- **called from:**
- `static/js/cookbook.js:1937`

## `_wireTabEvents` — function, line 1974
- **called from:**
- `static/js/cookbook.js:1974`
- `static/js/cookbook.js:3285`

## `_syncServers` — function, line 2025
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

## `setAdvancedOpen` — arrow, line 2161
- **called from:**
- `static/js/cookbook.js:2169`
- `static/js/cookbook.js:2172`
- `static/js/cookbook.js:2174`

## `_updateBulkCount` — function, line 2287
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

## `_stripHfUrl` — function, line 2337
- **called from:**
- `static/js/cookbook.js:2337`
- `static/js/cookbook.js:2389`
- `static/js/cookbook.js:2475`

## `_ggufQuantFromPath` — function, line 2359
- **called from:**
- `static/js/cookbook.js:2359`
- `static/js/cookbook.js:2370`
- `static/js/cookbook.js:2413`
- `static/js/cookbook.js:2554`

## `_ggufIncludeForQuant` — function, line 2369
- **called from:**
- `static/js/cookbook.js:2369`
- `static/js/cookbook.js:2428`

## `_hideGgufPicker` — function, line 2379
- **called from:**
- `static/js/cookbook.js:2379`
- `static/js/cookbook.js:2395`
- `static/js/cookbook.js:2419`
- `static/js/cookbook.js:2436`

## `_scanGgufRepo` — function, line 2387
- **called from:**
- `static/js/cookbook.js:2387`
- `static/js/cookbook.js:2504`
- `static/js/cookbook.js:2566`
- `static/js/cookbook.js:2569`

## `quantRank` — arrow, line 2422
- **called from:**
- `static/js/cookbook.js:2426`
- `static/js/cookbook.js:2426`

## `_splitRepoTag` — function, line 2442
- **called from:**
- `static/js/cookbook.js:2392`
- `static/js/cookbook.js:2442`
- `static/js/cookbook.js:2485`

## `_splitRepoFile` — function, line 2452
- **called from:**
- `static/js/cookbook.js:2391`
- `static/js/cookbook.js:2452`
- `static/js/cookbook.js:2482`

## `_ollamaName` — function, line 2467
- **called from:**
- `static/js/cookbook.js:2390`
- `static/js/cookbook.js:2467`
- `static/js/cookbook.js:2477`

## `triggerDownload` — arrow, line 2474
- **called from:**
- `static/js/cookbook.js:2561`

## `_scheduleGgufScan` — arrow, line 2564
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_setFolded` — arrow, line 2583
- **called from:**
- `static/js/cookbook.js:2595`
- `static/js/cookbook.js:2602`

## `so` — class, line 2584
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_maybeFold` — arrow, line 2600
- **called from:**
- `static/js/cookbook.js:2617`

## `_hfModelLooksAwqLike` — function, line 2629
- **called from:**
- `static/js/cookbook.js:2629`
- `static/js/cookbook.js:2698`

## `_getSelectedServerHw` — function, line 2633
- **called from:**
- `static/js/cookbook.js:2633`
- `static/js/cookbook.js:2686`

## `_loadLatest` — function, line 2668
- **called from:**
- `static/js/cookbook.js:2668`
- `static/js/cookbook.js:2747`
- `static/js/cookbook.js:2753`
- `static/js/cookbook.js:2766`

## `_fetchLatest` — arrow, line 2690
- **called from:**
- `static/js/cookbook.js:2696`

## `_onServerChange` — arrow, line 2764
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_loadOllama` — function, line 2781
- **called from:**
- `static/js/cookbook.js:2781`
- `static/js/cookbook.js:2836`
- `static/js/cookbook.js:2842`

## `_serverDefaultHtml` — function, line 2896
- **called from:**
- `static/js/cookbook-hwfit.js:2490`
- `static/js/cookbook.js:2896`
- `static/js/cookbook.js:2935`

## `_serverEntryHtml` — function, line 2901
- **called from:**
- `static/js/cookbook-hwfit.js:2776`
- `static/js/cookbook.js:2901`
- `static/js/cookbook.js:3277`

## `_renderRecipes` — function, line 2986
- **called from:**
- `static/js/cookbook.js:2986`
- `static/js/cookbook.js:3413`
- `static/js/cookbook.js:3559`

## `_dlTabFolded` — arrow, line 3009
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `alternative` — class, line 3140
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `open` — function, line 3332
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

## `_applyIntent` — arrow, line 3337
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `a` — class, line 3424
- **called from:**
- `static/js/editor/tools/lasso-mask.js:64`

## `_wireCookbookDrag` — function, line 3446
- **called from:**
- `static/js/cookbook.js:3384`
- `static/js/cookbook.js:3446`

## `_doClose` — function, line 3462
- **called from:**
- `static/js/cookbook.js:3381`
- `static/js/cookbook.js:3462`
- `static/js/cookbook.js:3488`

## `close` — function, line 3483
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

## `isVisible` — function, line 3492
- **called from:**
- `static/js/cookbook.js:3492`
- `static/js/cookbook.js:3535`
- `static/js/cookbook.js:3573`
- `static/js/cookbook.js:3585`
- `static/js/cookbookRunning.js:3770`

## `_foregroundChatBusy` — function, line 3505
- **called from:**
- `static/js/cookbook.js:3505`
- `static/js/cookbook.js:3537`
- `static/js/cookbookRunning.js:3777`
- `static/js/cookbookRunning.js:3807`
- `static/js/cookbookRunning.js:3822`
- `static/js/cookbookRunning.js:4078`
- `static/js/cookbookRunning.js:4087`

## `_claimSharedStateLeader` — function, line 3513
- **called from:**
- `static/js/cookbook.js:3513`
- `static/js/cookbook.js:3538`

## `_canRefreshSharedCookbookState` — function, line 3534
- **called from:**
- `static/js/cookbook.js:3534`
- `static/js/cookbook.js:3542`

## `_refreshSharedCookbookState` — function, line 3541
- **called from:**
- `static/js/cookbook.js:3541`
- `static/js/cookbook.js:3580`
- `static/js/cookbook.js:3582`
- `static/js/cookbook.js:3587`

## `_sshPrefix` — function, line 3608
- **called from:**
- `static/js/cookbook.js:3608`
- `static/js/cookbookRunning.js:1016`
- `static/js/cookbookRunning.js:1025`
- `static/js/cookbookRunning.js:1056`
- `static/js/cookbookRunning.js:1076`
- `static/js/cookbookRunning.js:1103`
- `static/js/cookbookRunning.js:1120`
- `static/js/cookbookRunning.js:1157`
- `static/js/cookbookRunning.js:2700`
- `static/js/cookbookServe.js:3604`
- `static/js/cookbookServe.js:3831`
