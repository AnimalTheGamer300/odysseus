# `static/js/editor/transform-frame-geometry.js` — definitions & call sites

15 definitions (regex-based, best-effort).
**Exports:** `distortTransformFrame`, `hitTestTransformHandle`, `pointInTransformFrame`, `resizeTransformFrame`, `skewTransformFrame`, `transformFrameGeometry`

## `finite` — function, line 14
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

## `transformFrameGeometry` — function, line 19
- **called from:**
- `static/js/editor/snap.js:127`
- `static/js/editor/tools/transform-handles.js:117`
- `static/js/editor/tools/transform-handles.js:189`
- `static/js/editor/tools/transform-handles.js:291`
- `static/js/editor/tools/transform-handles.js:304`
- `static/js/editor/tools/transform-handles.js:318`
- `static/js/editor/transform-frame-geometry.js:19`
- `static/js/editor/transform-frame-geometry.js:133`
- `static/js/editor/transform-frame-geometry.js:205`
- `static/js/editor/transform-frame-geometry.js:245`

## `localToWorld` — arrow, line 35
- **called from:**
- `static/js/editor/transform-frame-geometry.js:65`
- `static/js/editor/transform-frame-geometry.js:77`

## `localOf` — arrow, line 47
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delta` — arrow, line 51
- **called from:**
- `static/js/editor/editor-agent.js:73`
- `static/js/editor/transform-frame-geometry.js:53`
- `static/js/editor/transform-frame-geometry.js:54`
- `static/js/group.js:882`
- `static/js/group.js:891`

## `corner` — arrow, line 52
- **called from:**
- `static/js/document.js:2400`
- `static/js/editor/transform-frame-geometry.js:56`
- `static/js/editor/transform-frame-geometry.js:57`
- `static/js/editor/transform-frame-geometry.js:58`
- `static/js/editor/transform-frame-geometry.js:59`
- `static/js/fileHandler.js:266`

## `mid` — arrow, line 60
- **called from:**
- `static/js/editor/transform-frame-geometry.js:61`
- `static/js/editor/transform-frame-geometry.js:61`
- `static/js/editor/transform-frame-geometry.js:61`
- `static/js/editor/transform-frame-geometry.js:61`
- `static/js/signature.js:235`
- `static/js/signature.js:235`

## `hitTestTransformHandle` — function, line 103
- **called from:**
- `static/js/editor/tools/transform-handles.js:295`
- `static/js/editor/tools/transform-handles.js:308`
- `static/js/editor/transform-frame-geometry.js:103`

## `pointInTransformFrame` — function, line 118
- **called from:**
- `static/js/editor/tools/transform-handles.js:318`
- `static/js/editor/transform-frame-geometry.js:118`

## `resizeTransformFrame` — function, line 132
- **called from:**
- `static/js/editor/tools/transform-drag.js:215`
- `static/js/editor/transform-frame-geometry.js:132`

## `skewTransformFrame` — function, line 204
- **called from:**
- `static/js/editor/tools/transform-drag.js:189`
- `static/js/editor/transform-frame-geometry.js:204`

## `clamp` — arrow, line 216
- **called from:**
- `static/js/colorPicker.js:19`
- `static/js/colorPicker.js:31`
- `static/js/colorPicker.js:100`
- `static/js/colorPicker.js:366`
- `static/js/colorPicker.js:367`
- `static/js/colorPicker.js:374`
- `static/js/editor/canvas-context-menu.js:228`
- `static/js/editor/canvas-context-menu.js:229`
- `static/js/editor/canvas-context-menu.js:250`
- `static/js/editor/canvas-context-menu.js:259`
- `static/js/editor/filters/dehaze.js:23`
- `static/js/editor/filters/dehaze.js:120`
- `static/js/editor/filters/dehaze.js:122`
- `static/js/editor/filters/dehaze.js:127`
- `static/js/editor/filters/dehaze.js:200`
- `static/js/editor/filters/dehaze.js:206`
- `static/js/editor/filters/dehaze.js:232`
- `static/js/editor/filters/dehaze.js:233`
- `static/js/editor/filters/dehaze.js:234`
- `static/js/editor/tools/perspective-crop.js:11`
- `static/js/editor/tools/perspective-crop.js:32`
- `static/js/editor/tools/perspective-crop.js:33`
- `static/js/editor/transform-frame-geometry.js:223`
- `static/js/editor/transform-frame-geometry.js:225`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/galleryEditor.js:7986`
- `static/js/galleryEditor.js:7987`
- `static/js/galleryEditor.js:7988`
- `static/js/galleryEditor.js:7989`
- `static/js/galleryEditor.js:7996`
- `static/js/memory.js:411`
- `static/js/memory.js:419`

## `distortTransformFrame` — function, line 244
- **called from:**
- `static/js/editor/tools/transform-drag.js:168`
- `static/js/editor/transform-frame-geometry.js:244`

## `base` — arrow, line 263
- **called from:**
- `services/skills/publication.py:193`
- `services/skills/publication.py:193`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:269`

## `clamp` — arrow, line 265
- **called from:**
- `static/js/colorPicker.js:19`
- `static/js/colorPicker.js:31`
- `static/js/colorPicker.js:100`
- `static/js/colorPicker.js:366`
- `static/js/colorPicker.js:367`
- `static/js/colorPicker.js:374`
- `static/js/editor/canvas-context-menu.js:228`
- `static/js/editor/canvas-context-menu.js:229`
- `static/js/editor/canvas-context-menu.js:250`
- `static/js/editor/canvas-context-menu.js:259`
- `static/js/editor/filters/dehaze.js:23`
- `static/js/editor/filters/dehaze.js:120`
- `static/js/editor/filters/dehaze.js:122`
- `static/js/editor/filters/dehaze.js:127`
- `static/js/editor/filters/dehaze.js:200`
- `static/js/editor/filters/dehaze.js:206`
- `static/js/editor/filters/dehaze.js:232`
- `static/js/editor/filters/dehaze.js:233`
- `static/js/editor/filters/dehaze.js:234`
- `static/js/editor/tools/perspective-crop.js:11`
- `static/js/editor/tools/perspective-crop.js:32`
- `static/js/editor/tools/perspective-crop.js:33`
- `static/js/editor/transform-frame-geometry.js:223`
- `static/js/editor/transform-frame-geometry.js:225`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/editor/transform-frame-geometry.js:268`
- `static/js/galleryEditor.js:7986`
- `static/js/galleryEditor.js:7987`
- `static/js/galleryEditor.js:7988`
- `static/js/galleryEditor.js:7989`
- `static/js/galleryEditor.js:7996`
- `static/js/memory.js:411`
- `static/js/memory.js:419`
