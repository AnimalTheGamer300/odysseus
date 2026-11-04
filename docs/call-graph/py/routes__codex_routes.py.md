# `routes/codex_routes.py` — definitions & call sites

45 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ssh_prefix_for_task` — function, line 41
- **called from:**
- `routes/codex_routes.py:611`
- `routes/codex_routes.py:684`
- `tests/test_codex_ssh_host_validation.py:62`
- `tests/test_codex_ssh_host_validation.py:69`
- `tests/test_codex_ssh_host_validation.py:74`
- `tests/test_codex_ssh_host_validation.py:80`
- `tests/test_codex_ssh_host_validation.py:88`
- `tests/test_codex_ssh_host_validation.py:96`

## `_as_owner` — function (async), line 60
- **called from:**
- `routes/codex_routes.py:356`
- `routes/codex_routes.py:396`
- `routes/codex_routes.py:416`
- `routes/codex_routes.py:425`
- `routes/codex_routes.py:438`
- `routes/codex_routes.py:456`
- `routes/codex_routes.py:473`
- `routes/codex_routes.py:486`
- `routes/codex_routes.py:493`
- `routes/codex_routes.py:500`
- `routes/codex_routes.py:513`
- `tests/test_api_token_user_route_gate.py:53`

## `_scope_owner` — function, line 85
- **called from:**
- `routes/codex_routes.py:121`
- `routes/codex_routes.py:236`
- `routes/codex_routes.py:246`
- `routes/codex_routes.py:262`
- `routes/codex_routes.py:291`
- `routes/codex_routes.py:340`
- `routes/codex_routes.py:365`
- `routes/codex_routes.py:378`
- `routes/codex_routes.py:393`
- `routes/codex_routes.py:400`
- `routes/codex_routes.py:422`
- `routes/codex_routes.py:429`
- `routes/codex_routes.py:452`
- `routes/codex_routes.py:470`
- `routes/codex_routes.py:483`
- `routes/codex_routes.py:490`
- `routes/codex_routes.py:497`
- `routes/codex_routes.py:504`

## `_scope_owner_all` — function, line 99
- **called from:**
- `routes/codex_routes.py:341`

## `_require_cookbook_scope` — function, line 113
- **called from:**
- `routes/codex_routes.py:570`
- `routes/codex_routes.py:577`
- `routes/codex_routes.py:596`
- `routes/codex_routes.py:638`
- `routes/codex_routes.py:677`
- `routes/codex_routes.py:697`
- `routes/codex_routes.py:759`
- `routes/codex_routes.py:779`
- `routes/codex_routes.py:831`
- `tests/test_codex_cookbook_admin_gate.py:59`
- `tests/test_codex_cookbook_admin_gate.py:66`
- `tests/test_codex_cookbook_admin_gate.py:72`
- `tests/test_codex_cookbook_admin_gate.py:78`
- `tests/test_codex_cookbook_admin_gate.py:88`
- `tests/test_codex_cookbook_admin_gate.py:95`

## `_find_endpoint` — function, line 127
- **called from:**
- `routes/codex_routes.py:155`
- `routes/codex_routes.py:156`
- `routes/codex_routes.py:157`
- `routes/codex_routes.py:158`
- `routes/codex_routes.py:159`
- `routes/codex_routes.py:160`
- `routes/codex_routes.py:161`
- `routes/codex_routes.py:162`
- `routes/codex_routes.py:163`
- `routes/codex_routes.py:164`
- `routes/codex_routes.py:165`
- `routes/codex_routes.py:477`
- `routes/codex_routes.py:478`
- `routes/codex_routes.py:479`
- `routes/codex_routes.py:662`
- `routes/codex_routes.py:735`
- `routes/codex_routes.py:813`

## `_clamp_pagination` — function, line 136
- **called from:**
- `routes/codex_routes.py:455`

## `setup_codex_routes` — function, line 148
- **called from:**
- `app.py:871`
- `tests/test_codex_ssh_host_validation.py:20`
- `tests/test_codex_ssh_host_validation.py:130`
- `tests/test_codex_ssh_host_validation.py:236`

## `capabilities` — function, line 168
- **route:** `GET /capabilities`
- decorator: `router.get("/capabilities")`
- **called from:**
- `static/js/skills.js:15`
- `static/js/skills.js:463`

## `scoped` — function, line 171
- **called from:**
- `routes/codex_routes.py:178`
- `routes/codex_routes.py:179`
- `routes/codex_routes.py:183`
- `routes/codex_routes.py:184`
- `routes/codex_routes.py:185`
- `routes/codex_routes.py:189`
- `routes/codex_routes.py:190`
- `routes/codex_routes.py:195`
- `routes/codex_routes.py:196`
- `routes/codex_routes.py:201`
- `routes/codex_routes.py:202`
- `routes/codex_routes.py:207`
- `routes/codex_routes.py:208`

## `plugin_zip` — function, line 219
- **route:** `GET /plugin.zip`
- decorator: `router.get("/plugin.zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_todos` — function (async), line 235
- **route:** `GET /todos`
- decorator: `router.get("/todos")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `manage_todos` — function (async), line 243
- **route:** `POST /todos`
- decorator: `router.post("/todos")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_emails` — function (async), line 252
- **route:** `GET /emails`
- decorator: `router.get("/emails")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_email` — function (async), line 284
- **route:** `GET /emails/{uid}`
- decorator: `router.get("/emails/{uid}")`
- **called from:**
- `tests/test_email_owner_scope.py:380`
- `tests/test_email_read_mark_seen.py:98`
- `tests/test_email_read_mark_seen.py:128`
- `tests/test_email_read_mark_seen.py:138`
- `tests/test_email_read_mark_seen.py:165`
- `tests/test_email_read_mark_seen.py:192`
- `tests/test_email_read_mark_seen.py:217`
- `tests/test_email_read_mark_seen.py:220`
- `tests/test_email_read_mark_seen.py:240`
- `tests/test_email_read_mark_seen.py:263`
- `tests/test_email_read_mark_seen.py:266`

## `_email_draft_document_content` — function, line 310
- **called from:**
- `routes/codex_routes.py:354`

## `clean` — function, line 311
- **called from:**
- `routes/codex_routes.py:316`
- `routes/codex_routes.py:317`
- `routes/codex_routes.py:318`
- `routes/codex_routes.py:319`
- `routes/codex_routes.py:320`
- `routes/codex_routes.py:321`
- `src/visual_report.py:94`

## `codex_email_draft_document` — function (async), line 339
- **route:** `POST /emails/draft-document`
- decorator: `router.post("/emails/draft-document")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_email_draft` — function (async), line 364
- **route:** `POST /emails/draft`
- decorator: `router.post("/emails/draft")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_email_send` — function (async), line 377
- **route:** `POST /emails/send`
- decorator: `router.post("/emails/send")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_list` — function (async), line 392
- **route:** `GET /memory`
- decorator: `router.get("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_add` — function (async), line 399
- **route:** `POST /memory`
- decorator: `router.post("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_list` — function (async), line 421
- **route:** `GET /calendar/events`
- decorator: `router.get("/calendar/events")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_create` — function (async), line 428
- **route:** `POST /calendar/events`
- decorator: `router.post("/calendar/events")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_library` — function (async), line 443
- **route:** `GET /documents`
- decorator: `router.get("/documents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_get` — function (async), line 469
- **route:** `GET /documents/{doc_id}`
- decorator: `router.get("/documents/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_delete` — function (async), line 482
- **route:** `DELETE /memory/{memory_id}`
- decorator: `router.delete("/memory/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_delete` — function (async), line 489
- **route:** `DELETE /calendar/events/{uid}`
- decorator: `router.delete("/calendar/events/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_delete` — function (async), line 496
- **route:** `DELETE /documents/{doc_id}`
- decorator: `router.delete("/documents/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_create` — function (async), line 503
- **route:** `POST /documents`
- decorator: `router.post("/documents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_shell` — function (async), line 526
- **called from:**
- `routes/codex_routes.py:627`
- `routes/codex_routes.py:689`
- `routes/codex_routes.py:848`

## `_read_cookbook_state` — function, line 548
- **called from:**
- `routes/codex_routes.py:571`
- `routes/codex_routes.py:578`
- `routes/codex_routes.py:606`
- `routes/codex_routes.py:681`
- `routes/codex_routes.py:700`
- `routes/codex_routes.py:760`
- `routes/codex_routes.py:783`

## `_redact_task` — function, line 559
- **called from:**
- `routes/codex_routes.py:573`
- `routes/codex_routes.py:633`

## `codex_cookbook_tasks` — function (async), line 569
- **route:** `GET /cookbook/tasks`
- decorator: `router.get("/cookbook/tasks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_servers` — function (async), line 576
- **route:** `GET /cookbook/servers`
- decorator: `router.get("/cookbook/servers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_output` — function (async), line 595
- **route:** `GET /cookbook/output/{session_id}`
- decorator: `router.get("/cookbook/output/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_serve` — function (async), line 637
- **route:** `POST /cookbook/serve`
- decorator: `router.post("/cookbook/serve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_stop` — function (async), line 676
- **route:** `POST /cookbook/stop/{session_id}`
- decorator: `router.post("/cookbook/stop/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_cached` — function (async), line 693
- **route:** `GET /cookbook/cached`
- decorator: `router.get("/cookbook/cached")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_dirs_for` — function, line 704
- **called from:**
- `routes/codex_routes.py:728`
- `src/tools/cookbook.py:1627`
- `src/tools/cookbook.py:1631`
- `src/tools/cookbook.py:1644`

## `codex_cookbook_presets` — function (async), line 755
- **route:** `GET /cookbook/presets`
- decorator: `router.get("/cookbook/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_serve_preset` — function (async), line 776
- **route:** `POST /cookbook/preset/{name}`
- decorator: `router.post("/cookbook/preset/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_adopt` — function (async), line 826
- **route:** `POST /cookbook/adopt`
- decorator: `router.post("/cookbook/adopt")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_claude_routes` — function, line 882
- **called from:**
- `app.py:877`

## `plugin_zip` — function, line 892
- **route:** `GET /plugin.zip`
- decorator: `router.get("/plugin.zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
