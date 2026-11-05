# `static/js/escMenuStack.js` — definitions & call sites

12 definitions (regex-based, best-effort).
**Exports:** `_openMenuCount`, `bindExpandedCardDismiss`, `bindMenuDismiss`, `dismissOrRemove`, `dismissTopEscapeLayer`, `dismissTopMenu`, `registerEscapeLayer`, `registerMenuDismiss`, `unbindExpandedCardDismiss`

## `registerEscapeLayer` — function, line 15
- **called from:**
- `static/js/escMenuStack.js:15`
- `static/js/escMenuStack.js:29`
- `static/js/escMenuStack.js:114`
- `static/js/sessions.js:721`
- `static/js/sessions.js:1003`
- `static/js/sessions.js:1372`
- `static/js/tourHintDismiss.js:9`

## `registerMenuDismiss` — function, line 28
- **called from:**
- `static/js/cookbookRunning.js:2896`
- `static/js/documentLibrary.js:377`
- `static/js/documentLibrary.js:780`
- `static/js/escMenuStack.js:28`
- `static/js/escMenuStack.js:103`

## `dismissTopEscapeLayer` — function, line 33
- **called from:**
- `static/js/escMenuStack.js:7`
- `static/js/escMenuStack.js:33`
- `static/js/escMenuStack.js:47`
- `static/js/ui.js:1479`

## `dismissTopMenu` — function, line 46
- **called from:**
- `static/js/document.js:14633`
- `static/js/emailLibrary/index.js:3057`
- `static/js/escMenuStack.js:46`

## `_openMenuCount` — function, line 51
- **called from:**
- `static/js/escMenuStack.js:51`

## `dismissOrRemove` — function, line 62
- **called from:**
- `static/js/document.js:6656`
- `static/js/document.js:7774`
- `static/js/document.js:15234`
- `static/js/emailInbox.js:1234`
- `static/js/emailInbox.js:1244`
- `static/js/emailLibrary/menus.js:49`
- `static/js/emailLibrary/menus.js:360`
- `static/js/escMenuStack.js:62`
- `static/js/features/notes/ui/panel.js:66`
- `static/js/gallery.js:3058`
- `static/js/tasks.js:1183`
- `static/js/ui.js:1147`

## `bindMenuDismiss` — function, line 85
- **called from:**
- `static/js/calendar.js:656`
- `static/js/chatRenderer.js:1205`
- `static/js/chatRenderer.js:2432`
- `static/js/chatRenderer.js:2507`
- `static/js/chatRenderer.js:2610`
- `static/js/chatRenderer.js:2761`
- `static/js/chatRenderer.js:2902`
- `static/js/compare/index.js:164`
- `static/js/compare/index.js:1213`
- `static/js/compare/panes.js:168`
- `static/js/compare/panes.js:724`
- `static/js/compare/panes.js:1013`
- `static/js/cookbook.js:1900`
- `static/js/cookbookServe.js:1371`
- `static/js/cookbookServe.js:2699`
- `static/js/cookbookServe.js:2815`
- `static/js/cookbookServe.js:2867`
- `static/js/document.js:468`
- `static/js/document.js:1007`
- `static/js/document.js:6714`
- `static/js/document.js:7794`
- `static/js/document.js:15344`
- `static/js/emailInbox.js:1199`
- `static/js/emailLibrary/index.js:4793`
- `static/js/emailLibrary/index.js:4869`
- `static/js/emailLibrary/menus.js:351`
- `static/js/emailLibrary/menus.js:573`
- `static/js/emailLibrary/menus.js:661`
- `static/js/escMenuStack.js:75`
- `static/js/escMenuStack.js:85`
- `static/js/features/notes/ui/clipboard.js:39`
- `static/js/features/notes/ui/reminderPicker.js:321`
- `static/js/gallery.js:3049`
- `static/js/memory.js:85`
- `static/js/research/panel.js:1115`
- `static/js/research/panel.js:1440`
- `static/js/research/panel.js:1520`
- `static/js/sessions.js:3405`
- `static/js/settings.js:3491`
- `static/js/settings.js:4243`
- `static/js/settings.js:5340`
- `static/js/skills.js:607`
- `static/js/tasks.js:1221`

## `unreg` — arrow, line 87
- **called from:**
- `static/js/escMenuStack.js:95`

## `onDocClick` — arrow, line 88
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `close` — function, line 92
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)

## `bindExpandedCardDismiss` — function, line 111
- **called from:**
- `static/js/cookbookServe.js:1871`
- `static/js/documentLibrary.js:1135`
- `static/js/documentLibrary.js:2189`
- `static/js/documentLibrary.js:2628`
- `static/js/documentLibrary.js:3000`
- `static/js/emailLibrary/index.js:5970`
- `static/js/escMenuStack.js:111`
- `static/js/skills.js:697`
- `static/js/skills.js:1188`
- `static/js/tasks.js:1105`
- `static/js/tasks.js:2480`
- `static/js/tasks.js:3314`

## `unbindExpandedCardDismiss` — function, line 121
- **called from:**
- `static/js/cookbookServe.js:1400`
- `static/js/cookbookServe.js:1416`
- `static/js/cookbookServe.js:1872`
- `static/js/documentLibrary.js:211`
- `static/js/documentLibrary.js:2174`
- `static/js/documentLibrary.js:2182`
- `static/js/documentLibrary.js:2190`
- `static/js/documentLibrary.js:2614`
- `static/js/documentLibrary.js:2622`
- `static/js/documentLibrary.js:2629`
- `static/js/documentLibrary.js:2985`
- `static/js/documentLibrary.js:2993`
- `static/js/documentLibrary.js:3001`
- `static/js/emailLibrary/index.js:1782`
- `static/js/emailLibrary/index.js:5921`
- `static/js/emailLibrary/index.js:5959`
- `static/js/escMenuStack.js:113`
- `static/js/escMenuStack.js:121`
- `static/js/skills.js:688`
- `static/js/skills.js:693`
- `static/js/skills.js:698`
- `static/js/skills.js:1162`
- `static/js/tasks.js:1106`
- `static/js/tasks.js:1111`
- `static/js/tasks.js:2481`
- `static/js/tasks.js:2485`
- `static/js/tasks.js:3315`
