# `static/js/editor/nl-edit.js` — definitions & call sites

23 definitions (regex-based, best-effort).
**Exports:** `CHECK_INSTRUCTION`, `OP_CATALOG`, `SYSTEM_INSTRUCTION`, `activeGuidance`, `buildPlannerMessage`, `colorForName`, `createNaturalLanguageEditor`, `default`, `ensureFormatCrop`, `ensureGenericAutoTone`, `extractJson`, `fetchStyleGuide`, `formatCropRect`, `getStyleGuide`, `isGenericIntent`, `localPlan`, `sanitizeSteps`, `setStyleGuide`

## `setStyleGuide` — function, line 151
- **called from:**
- `static/js/editor/nl-edit.js:151`
- `static/js/editor/nl-edit.js:168`

## `getStyleGuide` — function, line 155
- **called from:**
- `static/js/editor/nl-edit.js:155`

## `activeGuidance` — function, line 156
- **called from:**
- `static/js/editor/nl-edit.js:156`
- `static/js/editor/nl-edit.js:476`
- `static/js/editor/nl-edit.js:476`
- `static/js/editor/nl-edit.js:501`

## `fetchStyleGuide` — function, line 161
- **called from:**
- `static/js/editor/nl-edit.js:161`
- `static/js/editor/nl-edit.js:460`

## `_matchGuideIntent` — function, line 171
- **called from:**
- `static/js/editor/nl-edit.js:171`
- `static/js/editor/nl-edit.js:220`

## `buildPlannerMessage` — function, line 185
- **called from:**
- `static/js/editor/nl-edit.js:185`
- `static/js/editor/nl-edit.js:501`

## `isGenericIntent` — function, line 200
- **called from:**
- `static/js/editor/editor-agent.js:161`
- `static/js/editor/nl-edit.js:200`
- `static/js/editor/nl-edit.js:438`

## `colorForName` — function, line 213
- **called from:**
- `static/js/editor/nl-edit.js:213`
- `static/js/editor/nl-edit.js:321`
- `static/js/editor/nl-edit.js:334`

## `localPlan` — function, line 219
- **called from:**
- `static/js/editor/nl-edit.js:219`
- `static/js/editor/nl-edit.js:528`
- `static/js/galleryEditor.js:2692`

## `first` — arrow, line 224
- **called from:**
- `app.py:586`
- `app.py:592`
- `app.py:601`
- `core/database.py:3056`
- `core/database.py:3093`
- `core/database.py:3124`
- `core/session_manager.py:370`
- `core/session_manager.py:464`
- `core/session_manager.py:498`
- `core/session_manager.py:527`
- `core/session_manager.py:532`
- `core/session_manager.py:597`
- `core/session_manager.py:639`
- `core/session_manager.py:674`
- `core/session_manager.py:843`
- `core/session_manager.py:882`
- `core/session_manager.py:909`
- `core/session_manager.py:997`
- `core/session_manager.py:1033`
- `core/session_manager.py:1053`
- `core/session_manager.py:1070`
- `mcp_servers/email_server.py:2837`
- `routes/api_token_routes.py:166`
- `routes/api_token_routes.py:200`
- `routes/assistant_routes.py:103`
- `routes/assistant_routes.py:116`
- `routes/assistant_routes.py:168`
- `routes/assistant_routes.py:215`
- `routes/assistant_routes.py:263`
- `routes/assistant_routes.py:282`
- `routes/assistant_routes.py:288`
- `routes/assistant_routes.py:308`
- `routes/assistant_routes.py:313`
- `routes/calendar_routes.py:96`
- `routes/calendar_routes.py:110`
- `routes/calendar_routes.py:196`
- `routes/calendar_routes.py:292`
- `routes/calendar_routes.py:300`
- `routes/calendar_routes.py:312`
- `routes/calendar_routes.py:344`
- `routes/calendar_routes.py:1350`
- `routes/calendar_routes.py:1600`
- `routes/calendar_routes.py:1644`
- `routes/chat_helpers.py:1060`
- `routes/chat_helpers.py:1643`
- `routes/chat_routes.py:1356`
- `routes/chat_routes.py:1949`
- `routes/chat_routes.py:1954`
- `routes/chat_routes.py:2168`
- `routes/chat_routes.py:2227`
- `routes/chat_routes.py:2272`
- `routes/chat_routes.py:3374`
- `routes/chat_routes.py:3415`
- `routes/chat_routes.py:3423`
- `routes/chat_routes.py:3438`
- `routes/chat_routes.py:5795`
- `routes/chatgpt_subscription_routes.py:101`
- `routes/chatgpt_subscription_routes.py:169`
- `routes/chatgpt_subscription_routes.py:175`
- `routes/chatgpt_subscription_routes.py:254`
- … +389 more (grep the name in repo)

## `sanitizeSteps` — function, line 383
- **called from:**
- `static/js/editor/nl-edit.js:383`
- `static/js/editor/nl-edit.js:529`
- `static/js/editor/nl-edit.js:588`

## `formatCropRect` — function, line 409
- **called from:**
- `static/js/editor/editor-agent.js:258`
- `static/js/editor/nl-edit.js:409`
- `static/js/editor/nl-edit.js:431`

## `ensureFormatCrop` — function, line 428
- **called from:**
- `static/js/editor/nl-edit.js:428`
- `static/js/editor/nl-edit.js:529`
- `static/js/editor/nl-edit.js:588`

## `ensureGenericAutoTone` — function, line 436
- **called from:**
- `static/js/editor/nl-edit.js:436`
- `static/js/editor/nl-edit.js:529`

## `extractJson` — function, line 443
- **called from:**
- `static/js/editor/nl-edit.js:443`
- `static/js/editor/nl-edit.js:504`

## `createNaturalLanguageEditor` — function, line 452
- **called from:**
- `static/js/editor/nl-edit.js:452`

## `ensureGuide` — function, line 457
- **called from:**
- `static/js/editor/nl-edit.js:457`
- `static/js/editor/nl-edit.js:520`

## `postJson` — function, line 463
- **called from:**
- `static/js/editor/nl-edit.js:463`
- `static/js/editor/nl-edit.js:477`
- `static/js/editor/nl-edit.js:502`

## `requestPlanEndpoint` — function, line 473
- **called from:**
- `static/js/editor/nl-edit.js:473`
- `static/js/editor/nl-edit.js:514`

## `requestViaChat` — function, line 490
- **called from:**
- `static/js/editor/nl-edit.js:490`
- `static/js/editor/nl-edit.js:514`

## `requestPlan` — function, line 512
- **called from:**
- `static/js/editor/nl-edit.js:512`
- `static/js/editor/nl-edit.js:526`
- `static/js/editor/nl-edit.js:586`

## `execute` — function, line 517
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `runSteps` — arrow, line 540
- **called from:**
- `static/js/editor/nl-edit.js:570`
- `static/js/editor/nl-edit.js:599`
