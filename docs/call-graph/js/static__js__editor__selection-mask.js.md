# `static/js/editor/selection-mask.js` — definitions & call sites

20 definitions (regex-based, best-effort).
**Exports:** `createMarqueeMask`, `mergeSelectionMasks`, `normalizeConstrainedSelectionRect`, `normalizeSelectionRect`, `paintSelectionBoundary`, `refineSelectionMask`, `selectionBoundary`, `selectionBoundaryPixels`, `selectionMaskBounds`, `selectionMaskContains`, `selectionMaskForLayer`, `selectionMaskToDocument`, `transformSelectionMask`, `translateSelectionMask`

## `makeCanvas` — function, line 5
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

## `normalizeSelectionRect` — function, line 12
- **called from:**
- `static/js/editor/selection-mask.js:12`
- `static/js/editor/selection-mask.js:34`

## `normalizeConstrainedSelectionRect` — function, line 32
- **called from:**
- `static/js/editor/selection-mask.js:32`
- `static/js/editor/tools/marquee.js:66`
- `static/js/editor/tools/marquee.js:127`

## `createMarqueeMask` — function, line 86
- **called from:**
- `static/js/editor/keyboard-shortcuts.js:270`
- `static/js/editor/selection-mask.js:86`
- `static/js/editor/tools/marquee.js:187`

## `mergeSelectionMasks` — function, line 108
- **called from:**
- `static/js/editor/selection-mask.js:108`
- `static/js/editor/tools/marquee.js:193`

## `copyMask` — function, line 121
- **called from:**
- `static/js/editor/selection-mask.js:121`
- `static/js/editor/selection-mask.js:129`
- `static/js/editor/selection-mask.js:139`
- `static/js/editor/selection-mask.js:160`

## `blurMask` — function, line 128
- **called from:**
- `static/js/editor/selection-mask.js:128`
- `static/js/editor/selection-mask.js:161`
- `static/js/editor/selection-mask.js:171`

## `thresholdMask` — function, line 138
- **called from:**
- `static/js/editor/selection-mask.js:138`
- `static/js/editor/selection-mask.js:161`

## `refineSelectionMask` — function, line 154
- **called from:**
- `static/js/editor/selection-mask.js:154`

## `selectionMaskToDocument` — function, line 174
- **called from:**
- `static/js/editor/ai-rembg.js:183`
- `static/js/editor/selection-mask.js:174`
- `static/js/editor/tools/marquee.js:180`

## `selectionMaskForLayer` — function, line 186
- **called from:**
- `static/js/editor/selection-mask.js:186`

## `selectionMaskContains` — function, line 198
- **called from:**
- `static/js/editor/selection-mask.js:198`
- `static/js/editor/tools/marquee.js:56`

## `selectionMaskBounds` — function, line 207
- **called from:**
- `static/js/editor/selection-mask.js:207`
- `static/js/editor/tools/marquee.js:91`
- `static/js/editor/tools/transform-session.js:199`

## `translateSelectionMask` — function, line 228
- **called from:**
- `static/js/editor/selection-mask.js:228`
- `static/js/editor/tools/marquee.js:29`
- `static/js/editor/tools/marquee.js:59`
- `static/js/editor/tools/marquee.js:113`

## `transformSelectionMask` — function, line 240
- **called from:**
- `static/js/editor/selection-mask.js:240`
- `static/js/editor/tools/transform-session.js:635`

## `selectionBoundaryPixels` — function, line 269
- **called from:**
- `static/js/editor/selection-mask.js:269`

## `selected` — arrow, line 274
- **called from:**
- `tests/test_research_chat_runtime.py:26`
- `tests/test_research_chat_runtime.py:34`
- `tests/test_research_chat_runtime.py:46`
- `tests/test_research_chat_runtime.py:53`
- `tests/test_research_chat_runtime.py:56`
- `tests/test_research_chat_runtime.py:98`
- `static/js/chat.js:9028`
- `static/js/cookbookRunning.js:2524`
- `static/js/document.js:3594`
- `static/js/editor/selection-mask.js:279`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:386`
- `static/js/editor/selection-mask.js:387`
- `static/js/editor/selection-mask.js:388`
- `static/js/editor/selection-mask.js:389`
- `static/js/settings.js:2058`

## `selectionBoundary` — function, line 293
- **called from:**
- `static/js/editor/selection-mask.js:293`

## `paintSelectionBoundary` — function, line 345
- **called from:**
- `static/js/editor/selection-mask.js:345`

## `selected` — arrow, line 375
- **called from:**
- `tests/test_research_chat_runtime.py:26`
- `tests/test_research_chat_runtime.py:34`
- `tests/test_research_chat_runtime.py:46`
- `tests/test_research_chat_runtime.py:53`
- `tests/test_research_chat_runtime.py:56`
- `tests/test_research_chat_runtime.py:98`
- `static/js/chat.js:9028`
- `static/js/cookbookRunning.js:2524`
- `static/js/document.js:3594`
- `static/js/editor/selection-mask.js:279`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:280`
- `static/js/editor/selection-mask.js:386`
- `static/js/editor/selection-mask.js:387`
- `static/js/editor/selection-mask.js:388`
- `static/js/editor/selection-mask.js:389`
- `static/js/settings.js:2058`
