# `static/js/editor/fx/pixel-pass.js` — definitions & call sites

15 definitions (regex-based, best-effort).
**Exports:** `applyAdjustment`, `curveLut`, `renderLayerPixelAdjustments`, `renderLayerWithAdjLayers`

## `clampByte` — function, line 20
- **called from:**
- `static/js/editor/fx/pixel-pass.js:20`
- `static/js/editor/fx/pixel-pass.js:38`
- `static/js/editor/fx/pixel-pass.js:46`
- `static/js/editor/fx/pixel-pass.js:46`
- `static/js/editor/fx/pixel-pass.js:68`
- `static/js/editor/fx/pixel-pass.js:154`
- `static/js/editor/fx/pixel-pass.js:155`
- `static/js/editor/fx/pixel-pass.js:156`
- `static/js/editor/fx/pixel-pass.js:167`
- `static/js/editor/fx/pixel-pass.js:168`
- `static/js/editor/fx/pixel-pass.js:169`
- `static/js/editor/fx/pixel-pass.js:186`
- `static/js/editor/fx/pixel-pass.js:186`
- `static/js/editor/fx/pixel-pass.js:186`
- `static/js/editor/fx/pixel-pass.js:205`
- `static/js/editor/fx/pixel-pass.js:206`
- `static/js/editor/fx/pixel-pass.js:207`
- `static/js/editor/fx/pixel-pass.js:221`
- `static/js/editor/fx/pixel-pass.js:222`
- `static/js/editor/fx/pixel-pass.js:223`
- `static/js/editor/fx/pixel-pass.js:246`
- `static/js/editor/fx/pixel-pass.js:247`
- `static/js/editor/fx/pixel-pass.js:248`
- `static/js/editor/fx/pixel-pass.js:339`
- `static/js/editor/fx/pixel-pass.js:339`
- `static/js/editor/fx/pixel-pass.js:339`
- `static/js/editor/fx/pixel-pass.js:355`
- `static/js/editor/fx/pixel-pass.js:356`
- `static/js/editor/fx/pixel-pass.js:357`
- `static/js/editor/fx/pixel-pass.js:377`
- `static/js/editor/fx/pixel-pass.js:378`
- `static/js/editor/fx/pixel-pass.js:379`
- `static/js/editor/fx/pixel-pass.js:410`
- `static/js/editor/fx/pixel-pass.js:410`
- `static/js/editor/fx/pixel-pass.js:410`
- `static/js/editor/fx/pixel-pass.js:428`
- `static/js/editor/fx/pixel-pass.js:429`
- `static/js/editor/fx/pixel-pass.js:429`
- `static/js/editor/fx/pixel-pass.js:429`
- `static/js/editor/fx/pixel-pass.js:464`
- `static/js/editor/fx/pixel-pass.js:465`
- `static/js/editor/fx/pixel-pass.js:466`

## `finiteOr` — function, line 24
- **called from:**
- `static/js/editor/fx/develop.js:17`
- `static/js/editor/fx/develop.js:72`
- `static/js/editor/fx/develop.js:73`
- `static/js/editor/fx/develop.js:74`
- `static/js/editor/fx/develop.js:75`
- `static/js/editor/fx/develop.js:76`
- `static/js/editor/fx/develop.js:77`
- `static/js/editor/fx/develop.js:78`
- `static/js/editor/fx/develop.js:79`
- `static/js/editor/fx/develop.js:80`
- `static/js/editor/fx/develop.js:81`
- `static/js/editor/fx/develop.js:82`
- `static/js/editor/fx/pixel-pass.js:24`
- `static/js/editor/fx/pixel-pass.js:30`
- `static/js/editor/fx/pixel-pass.js:31`
- `static/js/editor/fx/pixel-pass.js:32`
- `static/js/editor/fx/pixel-pass.js:33`
- `static/js/editor/fx/pixel-pass.js:34`
- `static/js/editor/fx/pixel-pass.js:150`
- `static/js/editor/fx/pixel-pass.js:151`
- `static/js/editor/fx/pixel-pass.js:152`
- `static/js/editor/fx/pixel-pass.js:164`
- `static/js/editor/fx/pixel-pass.js:165`
- `static/js/editor/fx/pixel-pass.js:177`
- `static/js/editor/fx/pixel-pass.js:178`
- `static/js/editor/fx/pixel-pass.js:179`
- `static/js/editor/fx/pixel-pass.js:193`
- `static/js/editor/fx/pixel-pass.js:215`
- `static/js/editor/fx/pixel-pass.js:216`
- `static/js/editor/fx/pixel-pass.js:217`
- `static/js/editor/fx/pixel-pass.js:218`
- `static/js/editor/fx/pixel-pass.js:230`
- `static/js/editor/fx/pixel-pass.js:231`
- `static/js/editor/fx/pixel-pass.js:334`
- `static/js/editor/fx/pixel-pass.js:335`
- `static/js/editor/fx/pixel-pass.js:336`
- `static/js/editor/fx/pixel-pass.js:337`
- `static/js/editor/fx/pixel-pass.js:350`
- `static/js/editor/fx/pixel-pass.js:374`
- `static/js/editor/fx/pixel-pass.js:386`
- `static/js/editor/fx/pixel-pass.js:399`
- `static/js/editor/fx/pixel-pass.js:425`
- `static/js/editor/fx/pixel-pass.js:425`
- `static/js/editor/fx/pixel-pass.js:425`
- `static/js/editor/fx/pixel-pass.js:425`
- `static/js/editor/fx/pixel-pass.js:426`
- `static/js/editor/fx/pixel-pass.js:426`
- `static/js/editor/fx/pixel-pass.js:426`
- `static/js/editor/fx/pixel-pass.js:426`
- `static/js/editor/fx/pixel-pass.js:427`
- `static/js/editor/fx/pixel-pass.js:427`
- `static/js/editor/fx/pixel-pass.js:427`
- `static/js/editor/fx/pixel-pass.js:427`

## `levelLut` — function, line 29
- **called from:**
- `static/js/editor/fx/pixel-pass.js:29`
- `static/js/editor/fx/pixel-pass.js:256`
- `static/js/editor/fx/pixel-pass.js:257`
- `static/js/editor/fx/pixel-pass.js:258`
- `static/js/editor/fx/pixel-pass.js:259`

## `normalizedCurvePoints` — function, line 43
- **called from:**
- `static/js/editor/fx/pixel-pass.js:43`
- `static/js/editor/fx/pixel-pass.js:59`

## `curveLut` — function, line 58
- **called from:**
- `static/js/editor/fx/pixel-pass.js:58`
- `static/js/editor/fx/pixel-pass.js:271`
- `static/js/editor/fx/pixel-pass.js:272`
- `static/js/editor/fx/pixel-pass.js:273`
- `static/js/editor/fx/pixel-pass.js:274`

## `rgbToHsl` — function, line 73
- **called from:**
- `static/js/editor/fx/pixel-pass.js:73`
- `static/js/editor/fx/pixel-pass.js:181`
- `static/js/editor/fx/pixel-pass.js:330`

## `hueChannel` — function, line 87
- **called from:**
- `static/js/editor/fx/pixel-pass.js:87`
- `static/js/editor/fx/pixel-pass.js:100`
- `static/js/editor/fx/pixel-pass.js:100`
- `static/js/editor/fx/pixel-pass.js:100`

## `hslToRgb` — function, line 96
- **called from:**
- `static/js/editor/fx/pixel-pass.js:96`
- `static/js/editor/fx/pixel-pass.js:185`

## `parseHexColor` — function, line 103
- **called from:**
- `static/js/editor/fx/pixel-pass.js:103`
- `static/js/editor/fx/pixel-pass.js:347`
- `static/js/editor/fx/pixel-pass.js:348`
- `static/js/editor/fx/pixel-pass.js:398`

## `hueDistance` — function, line 109
- **called from:**
- `static/js/editor/fx/pixel-pass.js:109`
- `static/js/editor/fx/pixel-pass.js:118`

## `selectiveRangeWeight` — function, line 114
- **called from:**
- `static/js/editor/fx/pixel-pass.js:114`
- `static/js/editor/fx/pixel-pass.js:332`

## `applyAdjustment` — function, line 122
- **called from:**
- `static/js/editor/adjustment-layer.js:106`
- `static/js/editor/adjustment-layer.js:174`
- `static/js/editor/adjustment-layer.js:180`
- `static/js/editor/adjustment-layer.js:190`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/adjustments-worker.js:14`
- `static/js/editor/fx/pixel-pass.js:7`
- `static/js/editor/fx/pixel-pass.js:122`
- `static/js/editor/fx/pixel-pass.js:606`
- `static/js/editor/fx/pixel-pass.js:621`
- `static/js/editor/layer-panel.js:1876`

## `toTone` — arrow, line 290
- **called from:**
- `static/js/editor/fx/pixel-pass.js:297`
- `static/js/editor/fx/pixel-pass.js:297`
- `static/js/editor/fx/pixel-pass.js:297`

## `renderLayerPixelAdjustments` — function, line 492
- **called from:**
- `static/js/editor/fx/pixel-pass.js:492`

## `renderLayerWithAdjLayers` — function, line 589
- **called from:**
- `static/js/editor/fx/pixel-pass.js:589`
