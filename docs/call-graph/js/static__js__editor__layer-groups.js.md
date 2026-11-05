# `static/js/editor/layer-groups.js` — definitions & call sites

28 definitions (regex-based, best-effort).
**Exports:** `allLayerIdsInGroup`, `createGroupFromSelection`, `drawGroupedLayers`, `drawGroupedLayersAsync`, `groupAncestors`, `groupDepth`, `groupForLayer`, `groupSiblingUnits`, `groupsForLayer`, `isLayerEffectivelyLocked`, `isLayerPixelLocked`, `isLayerPositionLocked`, `isLayerTransparencyLocked`, `layerHasAnyLock`, `normalizeLayerGroups`, `normalizeLayerLocks`, `reorderGroupAmongSiblings`, `ungroupLayers`

## `groupMap` — function, line 7
- **called from:**
- `static/js/editor/layer-groups.js:7`
- `static/js/editor/layer-groups.js:225`
- `static/js/editor/layer-groups.js:232`

## `breakParentCycles` — function, line 11
- **called from:**
- `static/js/editor/layer-groups.js:11`
- `static/js/editor/layer-groups.js:66`

## `normalizeLayerGroups` — function, line 28
- **called from:**
- `static/js/editor/layer-groups.js:28`
- `static/js/editor/layer-groups.js:88`
- `static/js/editor/layer-groups.js:92`
- `static/js/editor/layer-groups.js:114`
- `static/js/editor/layer-groups.js:171`
- `static/js/editor/layer-groups.js:220`
- `static/js/editor/layer-groups.js:229`
- `static/js/editor/layer-groups.js:243`
- `static/js/editor/layer-groups.js:248`
- `static/js/editor/layer-groups.js:274`
- `static/js/editor/layer-groups.js:313`
- `static/js/editor/layer-groups.js:418`
- `static/js/editor/layer-panel.js:1151`
- `static/js/editor/layer-panel.js:1159`
- `static/js/editor/layer-panel.js:1187`
- `static/js/editor/layer-panel.js:1235`
- `static/js/editor/layer-panel.js:2249`
- `static/js/editor/wire-merge-buttons.js:72`
- `static/js/editor/wire-merge-buttons.js:101`

## `groupForLayer` — function, line 87
- **called from:**
- `static/js/editor/layer-groups.js:87`
- `static/js/editor/layer-groups.js:109`
- `static/js/editor/layer-groups.js:184`
- `static/js/editor/wire-merge-buttons.js:56`
- `static/js/editor/wire-merge-buttons.js:56`
- `static/js/editor/wire-merge-buttons.js:165`
- `static/js/editor/wire-merge-buttons.js:165`

## `groupAncestors` — function, line 91
- **called from:**
- `static/js/editor/layer-groups.js:91`
- `static/js/editor/layer-groups.js:105`
- `static/js/editor/layer-groups.js:110`
- `static/js/editor/layer-groups.js:177`
- `static/js/editor/layer-panel.js:1257`

## `groupDepth` — function, line 104
- **called from:**
- `static/js/editor/layer-groups.js:104`
- `static/js/editor/layer-panel.js:1256`
- `static/js/editor/layer-panel.js:1256`
- `static/js/editor/layer-panel.js:1258`

## `groupsForLayer` — function, line 108
- **called from:**
- `static/js/editor/layer-groups.js:108`
- `static/js/editor/layer-groups.js:135`
- `static/js/editor/layer-panel.js:1260`

## `allLayerIdsInGroup` — function, line 113
- **called from:**
- `static/js/editor/layer-groups.js:113`
- `static/js/editor/layer-groups.js:172`
- `static/js/editor/layer-groups.js:222`
- `static/js/editor/layer-groups.js:231`
- `static/js/editor/layer-groups.js:262`
- `static/js/editor/layer-panel.js:428`
- `static/js/editor/layer-panel.js:810`
- `static/js/editor/layer-panel.js:854`
- `static/js/editor/layer-panel.js:883`
- `static/js/editor/layer-panel.js:913`
- `static/js/editor/layer-panel.js:951`
- `static/js/editor/layer-panel.js:1127`
- `static/js/editor/layer-panel.js:1240`
- `static/js/editor/layer-panel.js:2250`

## `visit` — arrow, line 125
- **called from:**
- `src/browser_observation.py:12`
- `src/browser_observation.py:34`
- `src/browser_observation.py:44`
- `src/browser_observation.py:49`
- `src/browser_observation.py:53`
- `src/clean_agent_preview.py:608`
- `src/clean_agent_preview.py:615`
- `src/clean_agent_preview.py:626`
- `src/clean_agent_preview.py:628`
- `static/js/editor/layer-groups.js:127`
- `static/js/editor/layer-groups.js:129`
- `static/js/gallery.js:2293`

## `isLayerEffectivelyLocked` — function, line 133
- **called from:**
- `static/js/editor/layer-groups.js:133`
- `static/js/editor/layer-groups.js:153`
- `static/js/editor/layer-groups.js:157`
- `static/js/editor/layer-groups.js:161`
- `static/js/editor/layer-selection.js:35`

## `normalizeLayerLocks` — function, line 138
- **called from:**
- `static/js/editor/layer-groups.js:138`
- `static/js/editor/layer-groups.js:148`
- `static/js/editor/layer-groups.js:153`
- `static/js/editor/layer-groups.js:157`
- `static/js/editor/layer-groups.js:161`
- `static/js/editor/layer-panel.js:467`
- `static/js/editor/layer-panel.js:485`
- `static/js/editor/layer-panel.js:1570`

## `layerHasAnyLock` — function, line 147
- **called from:**
- `static/js/editor/layer-groups.js:147`
- `static/js/editor/layer-panel.js:1474`
- `static/js/editor/layer-panel.js:1478`

## `isLayerPixelLocked` — function, line 152
- **called from:**
- `static/js/editor/layer-groups.js:152`
- `static/js/editor/layer-panel.js:1865`
- `static/js/editor/layer-panel.js:1868`
- `static/js/editor/layer-panel.js:1872`
- `static/js/editor/tools/clone.js:69`
- `static/js/editor/tools/clone.js:90`
- `static/js/editor/tools/gradient.js:61`
- `static/js/editor/tools/stroke.js:80`
- `static/js/editor/wire-topbar.js:161`

## `isLayerTransparencyLocked` — function, line 156
- **called from:**
- `static/js/editor/layer-groups.js:156`
- `static/js/editor/stroke-pipeline.js:197`
- `static/js/editor/stroke-pipeline.js:277`
- `static/js/editor/stroke-pipeline.js:342`
- `static/js/editor/tools/stroke.js:84`
- `static/js/editor/wire-topbar.js:161`

## `isLayerPositionLocked` — function, line 160
- **called from:**
- `static/js/editor/layer-geometry.js:48`
- `static/js/editor/layer-geometry.js:137`
- `static/js/editor/layer-geometry.js:154`
- `static/js/editor/layer-geometry.js:165`
- `static/js/editor/layer-geometry.js:187`
- `static/js/editor/layer-geometry.js:226`
- `static/js/editor/layer-groups.js:160`
- `static/js/editor/tools/move.js:49`
- `static/js/editor/tools/move.js:64`
- `static/js/editor/tools/transform-session.js:117`

## `createGroupFromSelection` — function, line 164
- **called from:**
- `static/js/editor/layer-groups.js:164`
- `static/js/editor/layer-panel.js:721`

## `ungroupLayers` — function, line 228
- **called from:**
- `static/js/editor/layer-groups.js:228`
- `static/js/editor/layer-panel.js:939`

## `groupSiblingUnits` — function, line 247
- **called from:**
- `static/js/editor/layer-groups.js:247`
- `static/js/editor/layer-groups.js:277`
- `static/js/editor/layer-panel.js:525`

## `reorderGroupAmongSiblings` — function, line 273
- **called from:**
- `static/js/editor/layer-groups.js:273`
- `static/js/editor/layer-panel.js:577`

## `groupCanvas` — function, line 295
- **called from:**
- `static/js/editor/layer-groups.js:295`
- `static/js/editor/layer-groups.js:363`

## `drawGroupedLayers` — function, line 307
- **called from:**
- `static/js/editor/layer-groups.js:307`

## `groupBounds` — arrow, line 325
- **called from:**
- `static/js/editor/layer-groups.js:329`
- `static/js/editor/layer-groups.js:344`
- `static/js/editor/layer-groups.js:434`
- `static/js/editor/layer-groups.js:449`

## `renderScope` — arrow, line 336
- **called from:**
- `static/js/editor/layer-groups.js:366`
- `static/js/editor/layer-groups.js:403`
- `static/js/editor/layer-groups.js:474`
- `static/js/editor/layer-groups.js:510`

## `flushLayers` — arrow, line 349
- **called from:**
- `static/js/editor/layer-groups.js:360`
- `static/js/editor/layer-groups.js:398`
- `static/js/editor/layer-groups.js:466`
- `static/js/editor/layer-groups.js:505`

## `drawGroupedLayersAsync` — function, line 414
- **called from:**
- `static/js/editor/layer-groups.js:414`

## `groupBounds` — arrow, line 430
- **called from:**
- `static/js/editor/layer-groups.js:329`
- `static/js/editor/layer-groups.js:344`
- `static/js/editor/layer-groups.js:434`
- `static/js/editor/layer-groups.js:449`

## `renderScope` — arrow, line 441
- **called from:**
- `static/js/editor/layer-groups.js:366`
- `static/js/editor/layer-groups.js:403`
- `static/js/editor/layer-groups.js:474`
- `static/js/editor/layer-groups.js:510`

## `flushLayers` — arrow, line 454
- **called from:**
- `static/js/editor/layer-groups.js:360`
- `static/js/editor/layer-groups.js:398`
- `static/js/editor/layer-groups.js:466`
- `static/js/editor/layer-groups.js:505`
