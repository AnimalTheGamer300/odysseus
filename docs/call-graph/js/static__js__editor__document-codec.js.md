# `static/js/editor/document-codec.js` — definitions & call sites

16 definitions (regex-based, best-effort).
**Exports:** `EDITOR_DOCUMENT_VERSION`, `EDITOR_MAX_DIMENSION`, `EDITOR_MAX_DOCUMENT_PIXELS`, `EDITOR_MAX_GROUPS`, `EDITOR_MAX_LAYERS`, `EDITOR_MAX_MASKS_PER_LAYER`, `EDITOR_MAX_SAVED_SELECTIONS`, `EDITOR_MAX_SURFACE_PIXELS`, `EDITOR_PROJECT_MAX_BYTES`, `cloneDocumentValue`, `nextLayerIdFromDocument`, `normalizeEditorView`, `prepareEditorDocument`, `serializeEditorDocument`

## `normalizeGuideValues` — function, line 31
- **called from:**
- `static/js/editor/document-codec.js:31`
- `static/js/editor/document-codec.js:59`
- `static/js/editor/document-codec.js:60`

## `normalizeEditorView` — function, line 43
- **called from:**
- `static/js/editor/document-codec.js:43`
- `static/js/editor/document-codec.js:122`
- `static/js/editor/document-codec.js:602`
- `static/js/editor/document-codec.js:647`

## `cloneDocumentValue` — function, line 65
- **called from:**
- `static/js/editor/document-codec.js:65`
- `static/js/editor/document-codec.js:698`
- `static/js/editor/document-codec.js:699`
- `static/js/editor/document-codec.js:700`
- `static/js/editor/document-codec.js:713`
- `static/js/editor/document-codec.js:714`

## `EditorDocumentError` — class, line 73
- **called from:**
- `static/js/editor/document-codec.js:189`
- `static/js/editor/document-codec.js:193`
- `static/js/editor/document-codec.js:196`
- `static/js/editor/document-codec.js:205`
- `static/js/editor/document-codec.js:257`
- `static/js/editor/document-codec.js:260`
- `static/js/editor/document-codec.js:263`
- `static/js/editor/document-codec.js:266`
- `static/js/editor/document-codec.js:375`
- `static/js/editor/document-codec.js:378`
- `static/js/editor/document-codec.js:416`
- `static/js/editor/document-codec.js:510`
- `static/js/editor/document-codec.js:513`
- `static/js/editor/document-codec.js:540`
- `static/js/editor/document-codec.js:543`

## `constructor` — method?, line 74
- **called from:**
- `static/js/editor/document-codec.js:74`
- `static/js/signature.js:39`
- `static/js/spinner.js:15`
- `static/js/tts-ai.js:7`

## `migrateEditorDocument` — function, line 187
- **called from:**
- `static/js/editor/document-codec.js:187`
- `static/js/editor/document-codec.js:249`

## `positiveDimension` — function, line 211
- **called from:**
- `static/js/editor/document-codec.js:211`
- `static/js/editor/document-codec.js:227`
- `static/js/editor/document-codec.js:228`
- `static/js/editor/document-codec.js:254`
- `static/js/editor/document-codec.js:255`
- `static/js/editor/document-codec.js:283`
- `static/js/editor/document-codec.js:284`
- `static/js/editor/document-codec.js:338`
- `static/js/editor/document-codec.js:339`
- `static/js/editor/document-codec.js:458`
- `static/js/editor/document-codec.js:459`

## `isEmbeddedPng` — function, line 216
- **called from:**
- `static/js/editor/document-codec.js:216`
- `static/js/editor/document-codec.js:232`
- `static/js/editor/document-codec.js:305`
- `static/js/editor/document-codec.js:309`
- `static/js/editor/document-codec.js:312`
- `static/js/editor/document-codec.js:315`
- `static/js/editor/document-codec.js:340`
- `static/js/editor/document-codec.js:460`
- `static/js/editor/document-codec.js:525`

## `finiteCoordinate` — function, line 220
- **called from:**
- `static/js/editor/document-codec.js:220`
- `static/js/editor/document-codec.js:366`
- `static/js/editor/document-codec.js:367`
- `static/js/editor/document-codec.js:408`
- `static/js/editor/document-codec.js:408`
- `static/js/editor/document-codec.js:728`
- `static/js/editor/document-codec.js:728`

## `normalizePlacedRecord` — function, line 225
- **called from:**
- `static/js/editor/document-codec.js:225`
- `static/js/editor/document-codec.js:292`

## `prepareEditorDocument` — function, line 248
- **called from:**
- `static/js/editor/document-codec.js:248`

## `warn` — arrow, line 251
- **called from:**
- `static/app.js:874`
- `static/app.js:3442`
- `static/app.js:3625`
- `static/app.js:4463`
- `static/app.js:4543`
- `static/js/admin.js:394`
- `static/js/admin.js:408`
- `static/js/admin.js:2359`
- `static/js/chat.js:256`
- `static/js/chat.js:560`
- `static/js/chat.js:1209`
- `static/js/chat.js:1863`
- `static/js/chat.js:2529`
- `static/js/chat.js:2633`
- `static/js/chat.js:2910`
- `static/js/chat.js:3228`
- `static/js/chat.js:3749`
- `static/js/chat.js:4632`
- `static/js/chat.js:4641`
- `static/js/chat.js:4653`
- `static/js/chat.js:5085`
- `static/js/chat.js:6397`
- `static/js/chat.js:6626`
- `static/js/chat.js:7015`
- `static/js/chat.js:7036`
- `static/js/chat.js:7636`
- `static/js/chat.js:7900`
- `static/js/chat.js:8046`
- `static/js/chat.js:8077`
- `static/js/chat.js:8643`
- `static/js/chat.js:8741`
- `static/js/chat.js:8910`
- `static/js/chat.js:9393`
- `static/js/chatRenderer.js:869`
- `static/js/chatRenderer.js:2117`
- `static/js/chatRenderer.js:2882`
- `static/js/chatStream.js:262`
- `static/js/chatStream.js:268`
- `static/js/chatStream.js:272`
- `static/js/compare/index.js:1068`
- `static/js/compare/selector.js:819`
- `static/js/compare/selector.js:823`
- `static/js/compare/stream.js:688`
- `static/js/cookbook-hwfit.js:831`
- `static/js/cookbook.js:1981`
- `static/js/cookbook.js:2006`
- `static/js/cookbook.js:3634`
- `static/js/cookbook.js:3776`
- `static/js/cookbookRunning.js:1952`
- `static/js/cookbookRunning.js:3757`
- `static/js/cookbookRunning.js:3762`
- `static/js/cookbookSchedule.js:23`
- `static/js/cookbookSchedule.js:401`
- `static/js/cookbookServe.js:3337`
- `static/js/cookbookServe.js:4535`
- `static/js/document.js:1581`
- `static/js/document.js:2996`
- `static/js/document.js:3003`
- `static/js/document.js:5592`
- `static/js/document.js:15722`
- … +122 more (grep the name in repo)

## `canvasDataUrl` — function, line 612
- **called from:**
- `static/js/editor/document-codec.js:612`
- `static/js/editor/document-codec.js:632`
- `static/js/editor/document-codec.js:654`
- `static/js/editor/document-codec.js:680`
- `static/js/editor/document-codec.js:706`
- `static/js/editor/document-codec.js:712`
- `static/js/editor/document-codec.js:732`

## `serializeEffect` — function, line 621
- **called from:**
- `static/js/editor/document-codec.js:621`

## `serializeEditorDocument` — function, line 637
- **called from:**
- `static/js/editor/document-codec.js:637`

## `nextLayerIdFromDocument` — function, line 738
- **called from:**
- `static/js/editor/document-codec.js:738`
