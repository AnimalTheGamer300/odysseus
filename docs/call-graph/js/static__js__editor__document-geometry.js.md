# `static/js/editor/document-geometry.js` — definitions & call sites

36 definitions (regex-based, best-effort).
**Exports:** `clipPolygonToRect`, `cropDocument`, `flipDocument`, `flipLayer`, `resizeCanvasDocument`, `resizeImageDocument`, `rotateDocument`, `rotateDocumentArbitrary`, `rotateLayer`

## `makeCanvas` — function, line 14
- **called from:**
- `static/js/editor/document-geometry.js:14`
- `static/js/editor/document-geometry.js:22`
- `static/js/editor/document-geometry.js:32`
- `static/js/editor/document-geometry.js:38`
- `static/js/editor/document-geometry.js:49`
- `static/js/editor/document-geometry.js:63`
- `static/js/editor/document-geometry.js:77`
- `static/js/editor/selection-mask.js:5`
- `static/js/editor/selection-mask.js:87`
- `static/js/editor/selection-mask.js:110`
- `static/js/editor/selection-mask.js:123`
- `static/js/editor/selection-mask.js:130`
- `static/js/editor/selection-mask.js:177`
- `static/js/editor/selection-mask.js:189`
- `static/js/editor/selection-mask.js:230`
- `static/js/editor/selection-mask.js:246`

## `renderWindow` — function, line 21
- **called from:**
- `static/js/editor/document-geometry.js:21`
- `static/js/editor/document-geometry.js:203`
- `static/js/editor/document-geometry.js:239`
- `static/js/editor/document-geometry.js:247`
- `static/js/editor/document-geometry.js:257`
- `static/js/editor/document-geometry.js:269`
- `static/js/editor/document-geometry.js:273`

## `renderTranslated` — function, line 31
- **called from:**
- `static/js/editor/document-geometry.js:31`
- `static/js/editor/document-geometry.js:398`
- `static/js/editor/document-geometry.js:408`
- `static/js/editor/document-geometry.js:411`
- `static/js/editor/document-geometry.js:414`

## `renderScaled` — function, line 37
- **called from:**
- `static/js/editor/document-geometry.js:37`
- `static/js/editor/document-geometry.js:317`
- `static/js/editor/document-geometry.js:330`
- `static/js/editor/document-geometry.js:348`
- `static/js/editor/document-geometry.js:354`
- `static/js/editor/document-geometry.js:363`

## `renderRotated` — function, line 46
- **called from:**
- `static/js/editor/document-geometry.js:46`
- `static/js/editor/document-geometry.js:475`
- `static/js/editor/document-geometry.js:480`
- `static/js/editor/document-geometry.js:498`
- `static/js/editor/document-geometry.js:501`
- `static/js/editor/document-geometry.js:503`
- `static/js/editor/document-geometry.js:826`
- `static/js/editor/document-geometry.js:833`

## `renderRotatedArbitrary` — function, line 57
- **called from:**
- `static/js/editor/document-geometry.js:57`
- `static/js/editor/document-geometry.js:585`
- `static/js/editor/document-geometry.js:593`
- `static/js/editor/document-geometry.js:623`
- `static/js/editor/document-geometry.js:636`
- `static/js/editor/document-geometry.js:639`

## `renderFlipped` — function, line 76
- **called from:**
- `static/js/editor/document-geometry.js:76`
- `static/js/editor/document-geometry.js:669`
- `static/js/editor/document-geometry.js:674`
- `static/js/editor/document-geometry.js:690`
- `static/js/editor/document-geometry.js:692`
- `static/js/editor/document-geometry.js:694`
- `static/js/editor/document-geometry.js:794`
- `static/js/editor/document-geometry.js:801`

## `replaceCanvas` — function, line 92
- **called from:**
- `static/js/editor/document-geometry.js:92`
- `static/js/editor/document-geometry.js:239`
- `static/js/editor/document-geometry.js:247`
- `static/js/editor/document-geometry.js:257`
- `static/js/editor/document-geometry.js:317`
- `static/js/editor/document-geometry.js:328`
- `static/js/editor/document-geometry.js:348`
- `static/js/editor/document-geometry.js:398`
- `static/js/editor/document-geometry.js:408`
- `static/js/editor/document-geometry.js:475`
- `static/js/editor/document-geometry.js:480`
- `static/js/editor/document-geometry.js:498`
- `static/js/editor/document-geometry.js:585`
- `static/js/editor/document-geometry.js:593`
- `static/js/editor/document-geometry.js:623`
- `static/js/editor/document-geometry.js:669`
- `static/js/editor/document-geometry.js:674`
- `static/js/editor/document-geometry.js:690`
- `static/js/editor/document-geometry.js:794`
- `static/js/editor/document-geometry.js:801`
- `static/js/editor/document-geometry.js:826`
- `static/js/editor/document-geometry.js:833`

## `replaceStandaloneCanvas` — function, line 100
- **called from:**
- `static/js/editor/document-geometry.js:100`
- `static/js/editor/document-geometry.js:267`
- `static/js/editor/document-geometry.js:273`
- `static/js/editor/document-geometry.js:352`
- `static/js/editor/document-geometry.js:363`
- `static/js/editor/document-geometry.js:411`
- `static/js/editor/document-geometry.js:414`
- `static/js/editor/document-geometry.js:501`
- `static/js/editor/document-geometry.js:503`
- `static/js/editor/document-geometry.js:636`
- `static/js/editor/document-geometry.js:639`
- `static/js/editor/document-geometry.js:692`
- `static/js/editor/document-geometry.js:694`

## `invalidateLayerCaches` — function, line 108
- **called from:**
- `static/js/editor/document-geometry.js:108`
- `static/js/editor/document-geometry.js:254`
- `static/js/editor/document-geometry.js:345`
- `static/js/editor/document-geometry.js:495`
- `static/js/editor/document-geometry.js:616`
- `static/js/editor/document-geometry.js:687`
- `static/js/editor/document-geometry.js:810`
- `static/js/editor/document-geometry.js:846`

## `syncActiveMask` — function, line 117
- **called from:**
- `static/js/editor/document-geometry.js:117`
- `static/js/editor/document-geometry.js:142`

## `syncDocumentCanvas` — function, line 131
- **called from:**
- `static/js/editor/document-geometry.js:131`
- `static/js/editor/document-geometry.js:293`
- `static/js/editor/document-geometry.js:382`
- `static/js/editor/document-geometry.js:431`
- `static/js/editor/document-geometry.js:533`
- `static/js/editor/document-geometry.js:648`
- `static/js/editor/document-geometry.js:721`

## `normalizedGuideValues` — function, line 145
- **called from:**
- `static/js/editor/document-geometry.js:145`
- `static/js/editor/document-geometry.js:157`
- `static/js/editor/document-geometry.js:158`

## `transformGuides` — function, line 155
- **called from:**
- `static/js/editor/document-geometry.js:155`
- `static/js/editor/document-geometry.js:285`
- `static/js/editor/document-geometry.js:377`
- `static/js/editor/document-geometry.js:426`
- `static/js/editor/document-geometry.js:515`
- `static/js/editor/document-geometry.js:521`
- `static/js/editor/document-geometry.js:527`
- `static/js/editor/document-geometry.js:708`

## `clipPolygonAxis` — function, line 162
- **called from:**
- `static/js/editor/document-geometry.js:162`
- `static/js/editor/document-geometry.js:190`
- `static/js/editor/document-geometry.js:191`
- `static/js/editor/document-geometry.js:192`
- `static/js/editor/document-geometry.js:193`

## `clipPolygonToRect` — function, line 178
- **called from:**
- `static/js/editor/document-geometry.js:178`
- `static/js/editor/document-geometry.js:279`
- `static/js/editor/document-geometry.js:416`

## `xAt` — arrow, line 180
- **called from:**
- `static/js/editor/document-geometry.js:190`
- `static/js/editor/document-geometry.js:191`

## `yAt` — arrow, line 185
- **called from:**
- `static/js/editor/document-geometry.js:192`
- `static/js/editor/document-geometry.js:193`

## `normalizeCropRect` — function, line 197
- **called from:**
- `static/js/editor/document-geometry.js:197`
- `static/js/editor/document-geometry.js:227`

## `forEachStoredSelection` — function, line 215
- **called from:**
- `static/js/editor/document-geometry.js:215`
- `static/js/editor/document-geometry.js:272`
- `static/js/editor/document-geometry.js:362`
- `static/js/editor/document-geometry.js:413`
- `static/js/editor/document-geometry.js:502`
- `static/js/editor/document-geometry.js:638`
- `static/js/editor/document-geometry.js:693`

## `cropDocument` — function, line 223
- **called from:**
- `static/js/editor/document-geometry.js:223`

## `resizeImageDocument` — function, line 298
- **called from:**
- `static/js/editor/document-geometry.js:298`
- `static/js/editor/wire-topbar-menus.js:111`

## `resizeCanvasDocument` — function, line 387
- **called from:**
- `static/js/editor/document-geometry.js:387`
- `static/js/editor/wire-topbar-menus.js:101`

## `rotatedPoint` — function, line 435
- **called from:**
- `static/js/editor/document-geometry.js:435`
- `static/js/editor/document-geometry.js:508`
- `static/js/editor/document-geometry.js:512`

## `rotatedOffset` — function, line 443
- **called from:**
- `static/js/editor/document-geometry.js:443`
- `static/js/editor/document-geometry.js:494`

## `rotateDocument` — function, line 452
- **called from:**
- `static/js/editor/canvas-transforms.js:43`
- `static/js/editor/document-geometry.js:452`
- `static/js/editor/document-geometry.js:552`

## `rotateDocumentArbitrary` — function, line 545
- **called from:**
- `static/js/editor/canvas-transforms.js:66`
- `static/js/editor/document-geometry.js:545`

## `mapPoint` — arrow, line 561
- **called from:**
- `static/js/editor/document-geometry.js:568`
- `static/js/editor/document-geometry.js:605`
- `static/js/editor/document-geometry.js:624`
- `static/js/editor/document-geometry.js:642`
- `static/js/editor/document-geometry.js:645`

## `flipDocument` — function, line 653
- **called from:**
- `static/js/editor/canvas-transforms.js:86`
- `static/js/editor/document-geometry.js:653`

## `layerBounds` — function, line 731
- **called from:**
- `static/js/editor/document-geometry.js:567`
- `static/js/editor/document-geometry.js:731`
- `static/js/editor/document-geometry.js:786`
- `static/js/editor/document-geometry.js:818`

## `recenterLayer` — function, line 750
- **called from:**
- `static/js/editor/document-geometry.js:750`
- `static/js/editor/document-geometry.js:795`
- `static/js/editor/document-geometry.js:827`

## `flipMatrixAbout` — function, line 759
- **called from:**
- `static/js/editor/document-geometry.js:759`
- `static/js/editor/document-geometry.js:790`

## `rotateMatrixAbout` — function, line 765
- **called from:**
- `static/js/editor/document-geometry.js:765`
- `static/js/editor/document-geometry.js:822`

## `transformLayerMasks` — function, line 777
- **called from:**
- `static/js/editor/document-geometry.js:777`
- `static/js/editor/document-geometry.js:797`
- `static/js/editor/document-geometry.js:829`

## `flipLayer` — function, line 784
- **called from:**
- `static/js/editor/canvas-transforms.js:92`
- `static/js/editor/document-geometry.js:784`
- `static/js/galleryEditor.js:3520`

## `rotateLayer` — function, line 815
- **called from:**
- `static/js/editor/canvas-transforms.js:102`
- `static/js/editor/document-geometry.js:815`
- `static/js/galleryEditor.js:3519`
