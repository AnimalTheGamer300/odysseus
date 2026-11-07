# `static/js/features/notes/infrastructure/http.js` — definitions & call sites

5 definitions (regex-based, best-effort).
**Exports:** `createNotesApi`

## `createNotesApi` — function, line 2
- **called from:**
- `static/js/features/notes/index.js:53`
- `static/js/features/notes/infrastructure/http.js:2`

## `json` — arrow, line 3
- **called from:**
- `app.py:1062`
- `mcp_servers/image_gen_server.py:113`
- `mcp_servers/image_gen_server.py:119`
- `routes/api_token_routes.py:160`
- `routes/auth_routes.py:369`
- `routes/auth_routes.py:764`
- `routes/auth_routes.py:794`
- `routes/auth_routes.py:932`
- `routes/auth_routes.py:942`
- `routes/backup_routes.py:69`
- `routes/calendar_routes.py:87`
- `routes/calendar_routes.py:1813`
- `routes/chat_routes.py:842`
- `routes/chat_routes.py:2660`
- `routes/chat_routes.py:5713`
- `routes/cookbook_routes.py:420`
- `routes/cookbook_routes.py:3293`
- `routes/cookbook_routes.py:3426`
- `routes/cookbook_routes.py:3789`
- `routes/cookbook_routes.py:3951`
- `routes/document/document_routes.py:782`
- `routes/document/document_routes.py:1478`
- `routes/editor_agent_routes.py:1240`
- `routes/email/email_helpers.py:130`
- `routes/email/email_routes.py:4219`
- `routes/email/email_routes.py:4354`
- `routes/email/email_routes.py:7733`
- `routes/email/email_routes.py:7867`
- `routes/email/email_routes.py:7884`
- `routes/gallery/gallery_routes.py:139`
- `routes/gallery/gallery_routes.py:195`
- `routes/gallery/gallery_routes.py:261`
- `routes/gallery/gallery_routes.py:329`
- `routes/gallery/gallery_routes.py:819`
- `routes/gallery/gallery_routes.py:826`
- `routes/gallery/gallery_routes.py:989`
- `routes/gallery/gallery_routes.py:1017`
- `routes/gallery/gallery_routes.py:1101`
- `routes/gallery/gallery_routes.py:1147`
- `routes/gallery/gallery_routes.py:1364`
- `routes/gallery/gallery_routes.py:1509`
- `routes/gallery/gallery_routes.py:1774`
- `routes/gallery/gallery_routes.py:1947`
- `routes/gallery/gallery_routes.py:1955`
- `routes/gallery/gallery_routes.py:2085`
- `routes/gallery/gallery_routes.py:2103`
- `routes/gallery/gallery_routes.py:2130`
- `routes/gallery/gallery_routes.py:2136`
- `routes/gallery/gallery_routes.py:2176`
- `routes/gallery/gallery_routes.py:2199`
- `routes/gallery/gallery_routes.py:2282`
- `routes/gallery/gallery_routes.py:2306`
- `routes/gallery/gallery_routes.py:2459`
- `routes/gallery/gallery_routes.py:2502`
- `routes/gallery/gallery_routes.py:2525`
- `routes/gallery/gallery_routes.py:2578`
- `routes/gallery/gallery_routes.py:2633`
- `routes/gallery/gallery_routes.py:2705`
- `routes/gallery/gallery_routes.py:2843`
- `routes/gallery/gallery_routes.py:2933`
- … +1088 more (grep the name in repo)

## `saveNote` — function, line 4
- **called from:**
- `static/js/features/notes/application/submission.js:51`
- `static/js/features/notes/application/workflows.js:73`
- `static/js/features/notes/infrastructure/http.js:4`

## `patchNote` — function, line 9
- **called from:**
- `static/js/features/notes/application/cardOperations.js:22`
- `static/js/features/notes/application/cardOperations.js:29`
- `static/js/features/notes/application/cardOperations.js:42`
- `static/js/features/notes/application/cardOperations.js:52`
- `static/js/features/notes/application/checklistOperations.js:19`
- `static/js/features/notes/application/checklistOperations.js:29`
- `static/js/features/notes/application/checklistOperations.js:43`
- `static/js/features/notes/application/checklistOperations.js:54`
- `static/js/features/notes/application/checklistOperations.js:63`
- `static/js/features/notes/application/drafts.js:32`
- `static/js/features/notes/application/selection.js:25`
- `static/js/features/notes/infrastructure/http.js:9`

## `deleteNote` — function, line 14
- **called from:**
- `static/js/features/notes/application/cardOperations.js:61`
- `static/js/features/notes/application/selection.js:35`
- `static/js/features/notes/application/workflows.js:75`
- `static/js/features/notes/infrastructure/http.js:14`
