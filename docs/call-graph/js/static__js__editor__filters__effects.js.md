# `static/js/editor/filters/effects.js` — definitions & call sites

67 definitions (regex-based, best-effort).
**Exports:** `addNoise`, `chalkCharcoal`, `charcoal`, `clouds`, `craquelure`, `crosshatch`, `crystallize`, `customKernel`, `cutout`, `despeckle`, `differenceClouds`, `diffuse`, `emboss`, `fibers`, `findEdges`, `glass`, `grain`, `graphicPen`, `halftonePattern`, `inkOutlines`, `lensCorrection`, `lensFlare`, `maximum`, `median`, `minimum`, `mosaicTiles`, `notePaper`, `oceanRipple`, `oilPaint`, `patchwork`, `photocopy`, `pinch`, `pixelate`, `polarCoordinates`, `posterEdges`, `replaceColor`, `reticulation`, `ripple`, `sharpen`, `sharpenEdges`, `sharpenMore`, `shear`, `solarize`, `spherize`, `stainedGlass`, `texturizer`, `traceContour`, `twirl`, `unsharpMask`, `waterPaper`, `wind`

## `readSource` — function, line 6
- **called from:**
- `static/js/editor/filters/effects.js:6`
- `static/js/editor/filters/effects.js:53`
- `static/js/editor/filters/effects.js:74`
- `static/js/editor/filters/effects.js:78`
- `static/js/editor/filters/effects.js:104`
- `static/js/editor/filters/effects.js:130`
- `static/js/editor/filters/effects.js:134`
- `static/js/editor/filters/effects.js:154`
- `static/js/editor/filters/effects.js:166`
- `static/js/editor/filters/effects.js:193`
- `static/js/editor/filters/effects.js:228`
- `static/js/editor/filters/effects.js:273`
- `static/js/editor/filters/effects.js:293`
- `static/js/editor/filters/effects.js:298`
- `static/js/editor/filters/effects.js:302`
- `static/js/editor/filters/effects.js:341`
- `static/js/editor/filters/effects.js:348`
- `static/js/editor/filters/effects.js:398`
- `static/js/editor/filters/effects.js:427`
- `static/js/editor/filters/effects.js:461`
- `static/js/editor/filters/effects.js:493`
- `static/js/editor/filters/effects.js:519`
- `static/js/editor/filters/effects.js:561`
- `static/js/editor/filters/effects.js:581`
- `static/js/editor/filters/effects.js:623`
- `static/js/editor/filters/effects.js:660`
- `static/js/editor/filters/effects.js:688`
- `static/js/editor/filters/effects.js:712`
- `static/js/editor/filters/effects.js:736`
- `static/js/editor/filters/effects.js:768`
- `static/js/editor/filters/effects.js:798`
- `static/js/editor/filters/effects.js:823`
- `static/js/editor/filters/effects.js:861`
- `static/js/editor/filters/effects.js:881`
- `static/js/editor/filters/effects.js:901`
- `static/js/editor/filters/effects.js:929`
- `static/js/editor/filters/effects.js:953`
- `static/js/editor/filters/effects.js:977`
- `static/js/editor/filters/effects.js:1006`
- `static/js/editor/filters/effects.js:1034`
- `static/js/editor/filters/effects.js:1065`
- `static/js/editor/filters/effects.js:1072`
- `static/js/editor/filters/effects.js:1101`
- `static/js/editor/filters/effects.js:1116`
- `static/js/editor/filters/effects.js:1145`
- `static/js/editor/filters/effects.js:1208`
- `static/js/editor/filters/effects.js:1228`
- `static/js/editor/filters/effects.js:1257`
- `static/js/editor/filters/effects.js:1292`
- `static/js/editor/filters/effects.js:1323`

## `clamp255` — function, line 11
- **called from:**
- `static/js/editor/filters/effects.js:11`
- `static/js/editor/filters/effects.js:43`
- `static/js/editor/filters/effects.js:44`
- `static/js/editor/filters/effects.js:45`
- `static/js/editor/filters/effects.js:61`
- `static/js/editor/filters/effects.js:62`
- `static/js/editor/filters/effects.js:63`
- `static/js/editor/filters/effects.js:65`
- `static/js/editor/filters/effects.js:66`
- `static/js/editor/filters/effects.js:67`
- `static/js/editor/filters/effects.js:145`
- `static/js/editor/filters/effects.js:284`
- `static/js/editor/filters/effects.js:285`
- `static/js/editor/filters/effects.js:286`
- `static/js/editor/filters/effects.js:327`
- `static/js/editor/filters/effects.js:471`
- `static/js/editor/filters/effects.js:472`
- `static/js/editor/filters/effects.js:473`
- `static/js/editor/filters/effects.js:508`
- `static/js/editor/filters/effects.js:509`
- `static/js/editor/filters/effects.js:510`
- `static/js/editor/filters/effects.js:549`
- `static/js/editor/filters/effects.js:550`
- `static/js/editor/filters/effects.js:551`
- `static/js/editor/filters/effects.js:570`
- `static/js/editor/filters/effects.js:571`
- `static/js/editor/filters/effects.js:572`
- `static/js/editor/filters/effects.js:647`
- `static/js/editor/filters/effects.js:648`
- `static/js/editor/filters/effects.js:649`
- `static/js/editor/filters/effects.js:871`
- `static/js/editor/filters/effects.js:917`
- `static/js/editor/filters/effects.js:942`
- `static/js/editor/filters/effects.js:967`
- `static/js/editor/filters/effects.js:1053`
- `static/js/editor/filters/effects.js:1089`
- `static/js/editor/filters/effects.js:1130`
- `static/js/editor/filters/effects.js:1131`
- `static/js/editor/filters/effects.js:1132`
- `static/js/editor/filters/effects.js:1133`
- `static/js/editor/filters/effects.js:1217`
- `static/js/editor/filters/effects.js:1218`
- `static/js/editor/filters/effects.js:1219`
- `static/js/editor/filters/effects.js:1244`
- `static/js/editor/filters/effects.js:1245`
- `static/js/editor/filters/effects.js:1246`
- `static/js/editor/filters/effects.js:1277`
- `static/js/editor/filters/effects.js:1278`
- `static/js/editor/filters/effects.js:1279`
- `static/js/editor/filters/effects.js:1310`
- `static/js/editor/filters/effects.js:1311`
- `static/js/editor/filters/effects.js:1312`
- `static/js/editor/filters/effects.js:1340`
- `static/js/editor/filters/effects.js:1341`
- `static/js/editor/filters/effects.js:1342`
- `static/js/editor/retouch.js:9`
- `static/js/editor/retouch.js:25`
- `static/js/editor/retouch.js:150`
- `static/js/editor/retouch.js:202`
- `static/js/editor/retouch.js:266`
- … +1 more (grep the name in repo)

## `clampIndex` — function, line 15
- **called from:**
- `static/js/editor/filters/effects.js:15`
- `static/js/editor/filters/effects.js:362`
- `static/js/editor/filters/effects.js:363`
- `static/js/editor/filters/effects.js:407`
- `static/js/editor/filters/effects.js:409`
- `static/js/editor/filters/effects.js:449`
- `static/js/editor/filters/effects.js:449`
- `static/js/editor/filters/effects.js:595`
- `static/js/editor/filters/effects.js:597`
- `static/js/editor/filters/effects.js:643`
- `static/js/editor/filters/effects.js:643`
- `static/js/editor/filters/effects.js:675`
- `static/js/editor/filters/effects.js:676`
- `static/js/editor/filters/effects.js:698`
- `static/js/editor/filters/effects.js:699`
- `static/js/editor/filters/effects.js:724`
- `static/js/editor/filters/effects.js:725`
- `static/js/editor/filters/effects.js:780`
- `static/js/editor/filters/effects.js:781`
- `static/js/editor/filters/effects.js:890`
- `static/js/editor/filters/effects.js:1049`
- `static/js/editor/filters/effects.js:1050`
- `static/js/editor/filters/effects.js:1239`
- `static/js/editor/filters/effects.js:1239`
- `static/js/editor/filters/effects.js:1240`
- `static/js/editor/filters/effects.js:1240`

## `convolve` — function, line 19
- **called from:**
- `static/js/editor/filters/effects.js:19`
- `static/js/editor/filters/effects.js:74`
- `static/js/editor/filters/effects.js:130`
- `static/js/editor/filters/effects.js:293`
- `static/js/editor/filters/effects.js:298`
- `static/js/editor/filters/effects.js:341`
- `static/js/editor/filters/effects.js:1065`

## `addNoise` — function, line 52
- **called from:**
- `static/js/editor/filters/effects.js:52`

## `despeckle` — function, line 73
- **called from:**
- `static/js/editor/filters/effects.js:73`

## `pixelate` — function, line 77
- **called from:**
- `static/js/editor/filters/effects.js:77`

## `crystallize` — function, line 103
- **called from:**
- `static/js/editor/filters/effects.js:103`

## `emboss` — function, line 128
- **called from:**
- `static/js/editor/filters/effects.js:128`

## `findEdges` — function, line 133
- **called from:**
- `static/js/editor/filters/effects.js:133`

## `lum` — arrow, line 138
- **called from:**
- `static/js/editor/blend-modes.js:69`
- `static/js/editor/blend-modes.js:205`
- `static/js/editor/blend-modes.js:206`
- `static/js/editor/filters/effects.js:143`
- `static/js/editor/filters/effects.js:143`
- `static/js/editor/filters/effects.js:144`
- `static/js/editor/filters/effects.js:144`

## `solarize` — function, line 153
- **called from:**
- `static/js/editor/filters/effects.js:153`

## `twirl` — function, line 165
- **called from:**
- `static/js/editor/filters/effects.js:165`

## `radialWarp` — function, line 192
- **called from:**
- `static/js/editor/filters/effects.js:192`
- `static/js/editor/filters/effects.js:219`
- `static/js/editor/filters/effects.js:224`

## `pinch` — function, line 217
- **called from:**
- `static/js/editor/filters/effects.js:217`

## `spherize` — function, line 222
- **called from:**
- `static/js/editor/filters/effects.js:222`

## `ripple` — function, line 227
- **called from:**
- `static/js/editor/filters/effects.js:227`

## `valueNoise` — function, line 245
- **called from:**
- `static/js/editor/filters/effects.js:245`
- `static/js/editor/filters/effects.js:278`
- `static/js/editor/filters/effects.js:279`
- `static/js/editor/filters/effects.js:280`
- `static/js/editor/filters/effects.js:466`
- `static/js/editor/filters/effects.js:467`
- `static/js/editor/filters/effects.js:468`
- `static/js/editor/filters/effects.js:567`
- `static/js/editor/filters/effects.js:718`
- `static/js/editor/filters/effects.js:719`
- `static/js/editor/filters/effects.js:866`
- `static/js/editor/filters/effects.js:867`
- `static/js/editor/filters/effects.js:906`
- `static/js/editor/filters/effects.js:936`
- `static/js/editor/filters/effects.js:960`
- `static/js/editor/filters/effects.js:1042`
- `static/js/editor/filters/effects.js:1043`
- `static/js/editor/filters/effects.js:1234`
- `static/js/editor/filters/effects.js:1298`

## `rand` — arrow, line 250
- **called from:**
- `static/js/editor/filters/effects.js:254`
- `static/js/editor/filters/effects.js:673`
- `static/js/editor/filters/effects.js:674`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1216`
- `static/js/researchSynapse.js:21`
- `static/js/researchSynapse.js:265`
- `static/js/researchSynapse.js:266`

## `clouds` — function, line 272
- **called from:**
- `static/js/editor/filters/effects.js:272`

## `sharpen` — function, line 291
- **called from:**
- `static/js/editor/filters/effects.js:291`
- `static/js/galleryEditor.js:9395`

## `sharpenEdges` — function, line 296
- **called from:**
- `static/js/editor/filters/effects.js:296`

## `unsharpMask` — function, line 301
- **called from:**
- `static/js/editor/filters/effects.js:301`

## `customKernel` — function, line 336
- **called from:**
- `static/js/editor/filters/effects.js:336`

## `morphology` — function, line 347
- **called from:**
- `static/js/editor/filters/effects.js:347`
- `static/js/editor/filters/effects.js:388`
- `static/js/editor/filters/effects.js:392`

## `pass` — arrow, line 354
- **called from:**
- `static/js/editor/ai-rembg.js:87`
- `static/js/editor/filters/effects.js:382`
- `static/js/editor/filters/effects.js:382`
- `static/js/editor/filters/effects.js:733`
- `static/js/editor/layer-helpers.js:17`
- `static/js/editor/state.js:195`
- `static/js/galleryEditor.js:9175`
- `static/js/theme.js:1695`

## `maximum` — function, line 387
- **called from:**
- `scripts/diffusion_server.py:1221`
- `static/js/editor/filters/effects.js:387`

## `minimum` — function, line 391
- **called from:**
- `static/js/calendar.js:1265`
- `static/js/editor/filters/effects.js:391`

## `median` — function, line 397
- **called from:**
- `static/js/editor/filters/effects.js:397`

## `polarCoordinates` — function, line 426
- **called from:**
- `static/js/editor/filters/effects.js:426`

## `differenceClouds` — function, line 460
- **called from:**
- `static/js/editor/filters/effects.js:460`

## `hexToRgb` — function, line 480
- **called from:**
- `static/js/color/hex.js:8`
- `static/js/colorPicker.js:21`
- `static/js/colorPicker.js:71`
- `static/js/editor/filters/effects.js:480`
- `static/js/editor/filters/effects.js:495`
- `static/js/editor/filters/effects.js:496`
- `static/js/editor/tools/bucket.js:12`
- `static/js/editor/tools/bucket.js:119`
- `static/js/editor/tools/color-range.js:3`
- `static/js/theme.js:170`
- `static/js/theme.js:2114`
- `static/js/theme.js:2370`

## `replaceColor` — function, line 492
- **called from:**
- `static/js/editor/filters/effects.js:492`

## `lensFlare` — function, line 518
- **called from:**
- `static/js/editor/filters/effects.js:518`

## `fibers` — function, line 560
- **called from:**
- `static/js/editor/filters/effects.js:560`

## `oilPaint` — function, line 580
- **called from:**
- `static/js/editor/filters/effects.js:580`

## `lensCorrection` — function, line 622
- **called from:**
- `static/js/editor/filters/effects.js:622`

## `diffuse` — function, line 659
- **called from:**
- `static/js/editor/filters/effects.js:659`

## `rand` — arrow, line 667
- **called from:**
- `static/js/editor/filters/effects.js:254`
- `static/js/editor/filters/effects.js:673`
- `static/js/editor/filters/effects.js:674`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1216`
- `static/js/researchSynapse.js:21`
- `static/js/researchSynapse.js:265`
- `static/js/researchSynapse.js:266`

## `oceanRipple` — function, line 687
- **called from:**
- `static/js/editor/filters/effects.js:687`

## `glass` — function, line 711
- **called from:**
- `static/js/editor/filters/effects.js:711`

## `mosaicTiles` — function, line 735
- **called from:**
- `static/js/editor/filters/effects.js:735`

## `wind` — function, line 767
- **called from:**
- `static/js/editor/filters/effects.js:767`

## `traceContour` — function, line 797
- **called from:**
- `static/js/editor/filters/effects.js:797`

## `halftonePattern` — function, line 822
- **called from:**
- `static/js/editor/filters/effects.js:822`

## `reticulation` — function, line 860
- **called from:**
- `static/js/editor/filters/effects.js:860`

## `shear` — function, line 880
- **called from:**
- `static/js/editor/filters/effects.js:880`

## `notePaper` — function, line 900
- **called from:**
- `static/js/editor/filters/effects.js:900`

## `charcoal` — function, line 928
- **called from:**
- `static/js/editor/filters/effects.js:928`

## `chalkCharcoal` — function, line 952
- **called from:**
- `static/js/editor/filters/effects.js:952`

## `graphicPen` — function, line 976
- **called from:**
- `static/js/editor/filters/effects.js:976`

## `photocopy` — function, line 1005
- **called from:**
- `static/js/editor/filters/effects.js:1005`

## `waterPaper` — function, line 1033
- **called from:**
- `static/js/editor/filters/effects.js:1033`

## `sharpenMore` — function, line 1063
- **called from:**
- `static/js/editor/filters/effects.js:1063`

## `posterEdges` — function, line 1071
- **called from:**
- `static/js/editor/filters/effects.js:1071`

## `luma` — arrow, line 1078
- **called from:**
- `static/js/editor/filters/effects.js:1085`
- `static/js/editor/filters/effects.js:1085`
- `static/js/editor/filters/effects.js:1086`
- `static/js/editor/filters/effects.js:1086`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1129`
- `static/js/editor/filters/effects.js:1129`

## `cutout` — function, line 1100
- **called from:**
- `static/js/editor/filters/effects.js:1100`

## `inkOutlines` — function, line 1115
- **called from:**
- `static/js/editor/filters/effects.js:1115`

## `luma` — arrow, line 1120
- **called from:**
- `static/js/editor/filters/effects.js:1085`
- `static/js/editor/filters/effects.js:1085`
- `static/js/editor/filters/effects.js:1086`
- `static/js/editor/filters/effects.js:1086`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1128`
- `static/js/editor/filters/effects.js:1129`
- `static/js/editor/filters/effects.js:1129`

## `stainedGlass` — function, line 1144
- **called from:**
- `static/js/editor/filters/effects.js:1144`

## `rand` — arrow, line 1157
- **called from:**
- `static/js/editor/filters/effects.js:254`
- `static/js/editor/filters/effects.js:673`
- `static/js/editor/filters/effects.js:674`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1216`
- `static/js/researchSynapse.js:21`
- `static/js/researchSynapse.js:265`
- `static/js/researchSynapse.js:266`

## `grain` — function, line 1207
- **called from:**
- `static/js/editor/filters/effects.js:1207`
- `static/js/galleryEditor.js:9456`

## `rand` — arrow, line 1213
- **called from:**
- `static/js/editor/filters/effects.js:254`
- `static/js/editor/filters/effects.js:673`
- `static/js/editor/filters/effects.js:674`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1158`
- `static/js/editor/filters/effects.js:1216`
- `static/js/researchSynapse.js:21`
- `static/js/researchSynapse.js:265`
- `static/js/researchSynapse.js:266`

## `texturizer` — function, line 1227
- **called from:**
- `static/js/editor/filters/effects.js:1227`

## `patchwork` — function, line 1256
- **called from:**
- `static/js/editor/filters/effects.js:1256`

## `craquelure` — function, line 1291
- **called from:**
- `static/js/editor/filters/effects.js:1291`

## `crosshatch` — function, line 1322
- **called from:**
- `static/js/editor/filters/effects.js:1322`
