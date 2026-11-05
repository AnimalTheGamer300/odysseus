# `static/js/settings/shell.js` — definitions & call sites

8 definitions (regex-based, best-effort).
**Exports:** `createSettingsShell`

## `createSettingsShell` — function, line 27
- **called from:**
- `static/js/settings.js:59`
- `static/js/settings/shell.js:27`

## `_modal` — arrow, line 35
- **called from:**
- `static/js/settings/shell.js:41`
- `static/js/settings/shell.js:59`
- `static/js/settings/shell.js:72`
- `static/js/settings/shell.js:93`
- `static/js/signature.js:318`
- `static/js/signature.js:382`
- `static/js/signature.js:475`

## `_admin` — arrow, line 36
- **called from:**
- `static/js/settings/shell.js:50`
- `static/js/settings/shell.js:86`

## `onPanelActivated` — function, line 38
- **called from:**
- `static/js/settings/navigation.js:53`
- `static/js/settings/shell.js:38`
- `static/js/settings/shell.js:83`

## `openAdminTab` — function, line 49
- **called from:**
- `static/js/settings/navigation.js:46`
- `static/js/settings/shell.js:49`

## `syncAdminVisibility` — function, line 58
- **called from:**
- `static/js/settings.js:5352`
- `static/js/settings.js:5352`
- `static/js/settings/shell.js:58`
- `static/js/settings/shell.js:74`

## `open` — function, line 67
- **called from:**
- `app.py:1102`
- `app.py:1168`
- `app.py:1334`
- `app.py:1389`
- `companion/pairing.py:167`
- `core/atomic_io.py:38`
- `core/atomic_io.py:74`
- `core/atomic_io.py:95`
- `core/auth.py:135`
- `core/auth.py:158`
- `core/database.py:1681`
- `core/database.py:1739`
- `core/database.py:1747`
- `core/database.py:1757`
- `core/database.py:1779`
- `core/platform_compat.py:325`
- `launcher.py:92`
- `launcher.py:131`
- `mcp_servers/email_server.py:2400`
- `routes/admin_wipe/admin_wipe_routes.py:48`
- `routes/auth_routes.py:559`
- `routes/chat_helpers.py:245`
- `routes/chat_helpers.py:264`
- `routes/chat_helpers.py:282`
- `routes/chat_helpers.py:286`
- `routes/chat_helpers.py:311`
- `routes/chat_helpers.py:346`
- `routes/chat_helpers.py:349`
- `routes/chat_helpers.py:1425`
- `routes/cookbook_routes.py:749`
- `routes/diagnostics_routes.py:42`
- `routes/document/document_routes.py:1385`
- `routes/document/document_routes.py:1445`
- `routes/document/document_routes.py:1520`
- `routes/email/email_helpers.py:661`
- `routes/email/email_helpers.py:1766`
- `routes/email/email_routes.py:4974`
- `routes/email/email_routes.py:4998`
- `routes/email/email_routes.py:5005`
- `routes/email/email_routes.py:5662`
- `routes/email/email_routes.py:5686`
- `routes/gallery/gallery_helpers.py:35`
- `routes/gallery/gallery_routes.py:62`
- `routes/gallery/gallery_routes.py:303`
- `routes/gallery/gallery_routes.py:359`
- `routes/gallery/gallery_routes.py:362`
- `routes/gallery/gallery_routes.py:391`
- `routes/gallery/gallery_routes.py:967`
- `routes/gallery/gallery_routes.py:1040`
- `routes/gallery/gallery_routes.py:1855`
- `routes/gallery/gallery_routes.py:1856`
- `routes/gallery/gallery_routes.py:1980`
- `routes/gallery/gallery_routes.py:2861`
- `routes/history/history_routes.py:62`
- `routes/history/history_routes.py:88`
- `routes/history/history_routes.py:93`
- `routes/mcp/mcp_routes.py:249`
- `routes/mcp/mcp_routes.py:470`
- `routes/mcp/mcp_routes.py:586`
- `routes/mcp/mcp_routes.py:616`
- … +499 more (grep the name in repo)

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
