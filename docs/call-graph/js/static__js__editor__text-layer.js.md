# `static/js/editor/text-layer.js` — definitions & call sites

20 definitions (regex-based, best-effort).
**Exports:** `DEFAULT_TEXT_DATA`, `EDITOR_TEXT_FONTS`, `WARP_STYLES`, `availableEditorFonts`, `flipTextLayer`, `hasTextPath`, `loadEditorFonts`, `normalizeTextData`, `pathTextCanvas`, `pathTextPadding`, `rasterizeTextLayer`, `renderTextLayer`, `rotateTextLayer`, `scaleTextLayer`, `warpCanvas`

## `loadEditorFonts` — function, line 44
- **called from:**
- `static/js/editor/text-layer.js:44`

## `availableEditorFonts` — function, line 52
- **called from:**
- `static/js/editor/panels/studio-panels.js:9`
- `static/js/editor/panels/studio-panels.js:9`
- `static/js/editor/text-layer.js:52`

## `finite` — function, line 59
- **called from:**
- `static/js/editor/fx/adj-popup.js:545`
- `static/js/editor/fx/adj-popup.js:703`
- `static/js/editor/fx/adj-popup.js:852`
- `static/js/editor/gradient-stops.js:5`
- `static/js/editor/gradient-stops.js:25`
- `static/js/editor/gradient-stops.js:36`
- `static/js/editor/shape-layer.js:28`
- `static/js/editor/shape-layer.js:38`
- `static/js/editor/shape-layer.js:42`
- `static/js/editor/shape-layer.js:43`
- `static/js/editor/shape-layer.js:58`
- `static/js/editor/shape-layer.js:60`
- `static/js/editor/shape-layer.js:61`
- `static/js/editor/shape-layer.js:62`
- `static/js/editor/shape-layer.js:64`
- `static/js/editor/shape-layer.js:64`
- `static/js/editor/shape-layer.js:68`
- `static/js/editor/shape-layer.js:69`
- `static/js/editor/shape-layer.js:70`
- `static/js/editor/text-layer.js:59`
- `static/js/editor/text-layer.js:69`
- `static/js/editor/text-layer.js:75`
- `static/js/editor/text-layer.js:76`
- `static/js/editor/text-layer.js:77`
- `static/js/editor/text-layer.js:78`
- `static/js/editor/text-layer.js:79`
- `static/js/editor/text-layer.js:87`
- `static/js/editor/text-layer.js:94`
- `static/js/editor/text-layer.js:95`
- `static/js/editor/text-layer.js:96`
- `static/js/editor/transform-frame-geometry.js:14`
- `static/js/editor/transform-frame-geometry.js:20`
- `static/js/editor/transform-frame-geometry.js:21`
- `static/js/editor/transform-frame-geometry.js:22`
- `static/js/editor/transform-frame-geometry.js:23`
- `static/js/editor/transform-frame-geometry.js:24`
- `static/js/editor/transform-frame-geometry.js:31`
- `static/js/editor/transform-frame-geometry.js:32`
- `static/js/editor/transform-frame-geometry.js:68`
- `static/js/editor/transform-frame-geometry.js:69`
- `static/js/editor/transform-frame-geometry.js:105`
- `static/js/editor/transform-frame-geometry.js:111`
- `static/js/editor/transform-frame-geometry.js:112`
- `static/js/editor/transform-frame-geometry.js:120`
- `static/js/editor/transform-frame-geometry.js:121`
- `static/js/editor/transform-frame-geometry.js:145`
- `static/js/editor/transform-frame-geometry.js:145`
- `static/js/editor/transform-frame-geometry.js:146`
- `static/js/editor/transform-frame-geometry.js:146`
- `static/js/editor/transform-frame-geometry.js:208`
- `static/js/editor/transform-frame-geometry.js:208`
- `static/js/editor/transform-frame-geometry.js:209`
- `static/js/editor/transform-frame-geometry.js:209`
- `static/js/editor/transform-frame-geometry.js:217`
- `static/js/editor/transform-frame-geometry.js:218`
- `static/js/editor/transform-frame-geometry.js:253`
- `static/js/editor/transform-frame-geometry.js:253`
- `static/js/editor/transform-frame-geometry.js:254`
- `static/js/editor/transform-frame-geometry.js:254`
- `static/js/editor/transform-frame-geometry.js:263`
- … +1 more (grep the name in repo)

## `normalizeTextData` — function, line 64
- **called from:**
- `static/js/editor/text-layer.js:64`
- `static/js/editor/text-layer.js:379`
- `static/js/editor/text-layer.js:422`
- `static/js/editor/text-layer.js:429`
- `static/js/editor/text-layer.js:435`
- `static/js/editor/tools/transform-session.js:765`

## `fontString` — function, line 103
- **called from:**
- `static/js/editor/text-layer.js:103`
- `static/js/editor/text-layer.js:164`
- `static/js/editor/text-layer.js:182`
- `static/js/editor/text-layer.js:218`
- `static/js/editor/text-layer.js:319`

## `measureSpacedText` — function, line 110
- **called from:**
- `static/js/editor/text-layer.js:110`
- `static/js/editor/text-layer.js:119`
- `static/js/editor/text-layer.js:143`
- `static/js/editor/text-layer.js:210`

## `drawSpacedText` — function, line 116
- **called from:**
- `static/js/editor/text-layer.js:116`
- `static/js/editor/text-layer.js:231`
- `static/js/editor/text-layer.js:232`

## `wrapText` — function, line 128
- **called from:**
- `static/js/editor/text-layer.js:128`
- `static/js/editor/text-layer.js:209`

## `applyFontOptions` — function, line 155
- **called from:**
- `static/js/editor/text-layer.js:155`
- `static/js/editor/text-layer.js:165`
- `static/js/editor/text-layer.js:183`
- `static/js/editor/text-layer.js:320`

## `baseTextCanvas` — function, line 161
- **called from:**
- `static/js/editor/text-layer.js:161`
- `static/js/editor/text-layer.js:382`

## `warpCanvas` — function, line 237
- **called from:**
- `static/js/editor/text-layer.js:237`
- `static/js/editor/text-layer.js:382`

## `pathTextPadding` — function, line 294
- **called from:**
- `static/js/editor/text-layer.js:294`
- `static/js/editor/text-layer.js:310`

## `hasTextPath` — function, line 299
- **called from:**
- `static/js/editor/text-layer.js:299`
- `static/js/editor/text-layer.js:380`

## `pathTextCanvas` — function, line 308
- **called from:**
- `static/js/editor/text-layer.js:308`
- `static/js/editor/text-layer.js:381`

## `atDistance` — arrow, line 339
- **called from:**
- `static/js/editor/text-layer.js:364`

## `renderTextLayer` — function, line 376
- **called from:**
- `static/js/editor/text-layer.js:376`
- `static/js/editor/text-layer.js:425`
- `static/js/editor/text-layer.js:431`
- `static/js/editor/text-layer.js:438`
- `static/js/editor/tools/transform-session.js:773`

## `rasterizeTextLayer` — function, line 414
- **called from:**
- `static/js/editor/layer-panel.js:1879`
- `static/js/editor/text-layer.js:414`
- `static/js/editor/wire-merge-buttons.js:40`

## `scaleTextLayer` — function, line 421
- **called from:**
- `static/js/editor/document-geometry.js:312`
- `static/js/editor/text-layer.js:421`

## `rotateTextLayer` — function, line 428
- **called from:**
- `static/js/editor/document-geometry.js:465`
- `static/js/editor/document-geometry.js:571`
- `static/js/editor/document-geometry.js:819`
- `static/js/editor/text-layer.js:428`

## `flipTextLayer` — function, line 434
- **called from:**
- `static/js/editor/document-geometry.js:661`
- `static/js/editor/document-geometry.js:787`
- `static/js/editor/text-layer.js:434`
