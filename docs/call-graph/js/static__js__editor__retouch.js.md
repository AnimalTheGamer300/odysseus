# `static/js/editor/retouch.js` — definitions & call sites

22 definitions (regex-based, best-effort).
**Exports:** `analyzeAutoTone`, `applyAutoTone`, `blemishRemoval`, `boxBlurRGB`, `default`, `dilateAlpha`, `featureExclusionMask`, `frequencySeparationSmooth`, `guidedClarity`, `meanAbsDelta`, `skinMaskFromData`, `subtractMask`, `teethWhitening`

## `clamp255` — function, line 9
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

## `boxBlurRGB` — function, line 14
- **called from:**
- `static/js/editor/retouch.js:14`
- `static/js/editor/retouch.js:192`
- `static/js/editor/retouch.js:276`

## `clampX` — function, line 50
- **called from:**
- `static/js/editor/retouch.js:28`
- `static/js/editor/retouch.js:29`
- `static/js/editor/retouch.js:50`
- `static/js/editor/retouch.js:329`
- `static/js/editor/retouch.js:329`

## `clampY` — function, line 51
- **called from:**
- `static/js/editor/retouch.js:38`
- `static/js/editor/retouch.js:41`
- `static/js/editor/retouch.js:42`
- `static/js/editor/retouch.js:51`
- `static/js/editor/retouch.js:334`
- `static/js/editor/retouch.js:337`
- `static/js/editor/retouch.js:337`

## `toGray` — function, line 53
- **called from:**
- `static/js/editor/retouch.js:53`

## `analyzeAutoTone` — function, line 58
- **called from:**
- `static/js/editor/retouch.js:58`

## `pctLo` — arrow, line 80
- **called from:**
- `static/js/editor/retouch.js:82`
- `static/js/editor/retouch.js:89`

## `pctHi` — arrow, line 81
- **called from:**
- `static/js/editor/retouch.js:82`
- `static/js/editor/retouch.js:89`

## `clampRange` — function, line 132
- **called from:**
- `static/js/editor/retouch.js:112`
- `static/js/editor/retouch.js:113`
- `static/js/editor/retouch.js:114`
- `static/js/editor/retouch.js:117`
- `static/js/editor/retouch.js:120`
- `static/js/editor/retouch.js:125`
- `static/js/editor/retouch.js:132`

## `applyAutoTone` — function, line 134
- **called from:**
- `static/js/editor/retouch.js:134`

## `skinMaskFromData` — function, line 164
- **called from:**
- `static/js/editor/retouch.js:164`

## `frequencySeparationSmooth` — function, line 187
- **called from:**
- `static/js/editor/retouch.js:187`

## `featureExclusionMask` — function, line 211
- **called from:**
- `static/js/editor/retouch.js:211`

## `dilateAlpha` — function, line 235
- **called from:**
- `static/js/editor/retouch.js:235`

## `subtractMask` — function, line 261
- **called from:**
- `static/js/editor/retouch.js:261`

## `blemishRemoval` — function, line 273
- **called from:**
- `static/js/editor/retouch.js:273`

## `data_alpha` — function, line 290
- **called from:**
- `static/js/editor/retouch.js:279`
- `static/js/editor/retouch.js:290`

## `teethWhitening` — function, line 293
- **called from:**
- `static/js/editor/retouch.js:293`

## `boxBlurFloat` — function, line 317
- **called from:**
- `static/js/editor/retouch.js:317`
- `static/js/editor/retouch.js:365`
- `static/js/editor/retouch.js:366`
- `static/js/editor/retouch.js:375`
- `static/js/editor/retouch.js:376`
- `static/js/editor/retouch.js:390`
- `static/js/editor/retouch.js:391`

## `guidedClarity` — function, line 351
- **called from:**
- `static/js/editor/retouch.js:351`

## `guidedBase` — arrow, line 361
- **called from:**
- `static/js/editor/retouch.js:399`
- `static/js/editor/retouch.js:400`
- `static/js/editor/retouch.js:401`

## `meanAbsDelta` — function, line 419
- **called from:**
- `static/js/editor/retouch.js:419`
