# `routes/codex_routes.py` — definitions & call sites

46 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ssh_prefix_for_task` — function, line 42
- **called from:**
- `routes/codex_routes.py:657`
- `routes/codex_routes.py:730`
- `tests/test_codex_ssh_host_validation.py:62`
- `tests/test_codex_ssh_host_validation.py:69`
- `tests/test_codex_ssh_host_validation.py:74`
- `tests/test_codex_ssh_host_validation.py:80`
- `tests/test_codex_ssh_host_validation.py:88`
- `tests/test_codex_ssh_host_validation.py:96`

## `_as_owner` — function (async), line 61
- **called from:**
- `routes/codex_routes.py:402`
- `routes/codex_routes.py:442`
- `routes/codex_routes.py:462`
- `routes/codex_routes.py:471`
- `routes/codex_routes.py:484`
- `routes/codex_routes.py:502`
- `routes/codex_routes.py:519`
- `routes/codex_routes.py:532`
- `routes/codex_routes.py:539`
- `routes/codex_routes.py:546`
- `routes/codex_routes.py:559`
- `tests/test_api_token_user_route_gate.py:53`

## `_scope_owner` — function, line 86
- **called from:**
- `routes/codex_routes.py:133`
- `routes/codex_routes.py:244`
- `routes/codex_routes.py:282`
- `routes/codex_routes.py:292`
- `routes/codex_routes.py:308`
- `routes/codex_routes.py:337`
- `routes/codex_routes.py:386`
- `routes/codex_routes.py:411`
- `routes/codex_routes.py:424`
- `routes/codex_routes.py:439`
- `routes/codex_routes.py:446`
- `routes/codex_routes.py:468`
- `routes/codex_routes.py:475`
- `routes/codex_routes.py:498`
- `routes/codex_routes.py:516`
- `routes/codex_routes.py:529`
- `routes/codex_routes.py:536`
- `routes/codex_routes.py:543`
- `routes/codex_routes.py:550`

## `_scope_owner_all` — function, line 100
- **called from:**
- `routes/codex_routes.py:387`

## `_require_cookbook_scope` — function, line 114
- **called from:**
- `routes/codex_routes.py:616`
- `routes/codex_routes.py:623`
- `routes/codex_routes.py:642`
- `routes/codex_routes.py:684`
- `routes/codex_routes.py:723`
- `routes/codex_routes.py:743`
- `routes/codex_routes.py:805`
- `routes/codex_routes.py:825`
- `routes/codex_routes.py:877`
- `tests/test_codex_cookbook_admin_gate.py:59`
- `tests/test_codex_cookbook_admin_gate.py:66`
- `tests/test_codex_cookbook_admin_gate.py:72`
- `tests/test_codex_cookbook_admin_gate.py:78`
- `tests/test_codex_cookbook_admin_gate.py:88`
- `tests/test_codex_cookbook_admin_gate.py:95`

## `_find_endpoint` — function, line 139
- **called from:**
- `routes/codex_routes.py:168`
- `routes/codex_routes.py:169`
- `routes/codex_routes.py:170`
- `routes/codex_routes.py:171`
- `routes/codex_routes.py:172`
- `routes/codex_routes.py:173`
- `routes/codex_routes.py:174`
- `routes/codex_routes.py:175`
- `routes/codex_routes.py:176`
- `routes/codex_routes.py:177`
- `routes/codex_routes.py:178`
- `routes/codex_routes.py:179`
- `routes/codex_routes.py:523`
- `routes/codex_routes.py:524`
- `routes/codex_routes.py:525`
- `routes/codex_routes.py:708`
- `routes/codex_routes.py:781`
- `routes/codex_routes.py:859`

## `_clamp_pagination` — function, line 148
- **called from:**
- `routes/codex_routes.py:247`
- `routes/codex_routes.py:501`

## `setup_codex_routes` — function, line 160
- **called from:**
- `app.py:955`
- `tests/test_codex_chat_history.py:59`
- `tests/test_codex_chat_history.py:80`
- `tests/test_codex_chat_history.py:93`
- `tests/test_codex_chat_history.py:102`
- `tests/test_codex_ssh_host_validation.py:20`
- `tests/test_codex_ssh_host_validation.py:130`
- `tests/test_codex_ssh_host_validation.py:236`
- `tests/test_wave3_local_control.py:219`

## `capabilities` — function, line 182
- **route:** `GET /capabilities`
- decorator: `router.get("/capabilities")`
- **called from:**
- `tests/test_codex_chat_history.py:105`
- `tests/test_codex_chat_history.py:106`
- `static/js/skills.js:30`
- `static/js/skills.js:611`

## `scoped` — function, line 185
- **called from:**
- `routes/codex_routes.py:192`
- `routes/codex_routes.py:193`
- `routes/codex_routes.py:197`
- `routes/codex_routes.py:198`
- `routes/codex_routes.py:199`
- `routes/codex_routes.py:203`
- `routes/codex_routes.py:204`
- `routes/codex_routes.py:209`
- `routes/codex_routes.py:210`
- `routes/codex_routes.py:215`
- `routes/codex_routes.py:216`
- `routes/codex_routes.py:221`
- `routes/codex_routes.py:222`
- `routes/codex_routes.py:226`

## `read_chat` — function (async), line 238
- **route:** `GET /chat/{session_id}`
- decorator: `router.get("/chat/{session_id}")`
- **called from:**
- `tests/test_codex_chat_history.py:63`
- `tests/test_codex_chat_history.py:84`
- `tests/test_codex_chat_history.py:96`

## `plugin_zip` — function, line 265
- **route:** `GET /plugin.zip`
- decorator: `router.get("/plugin.zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_todos` — function (async), line 281
- **route:** `GET /todos`
- decorator: `router.get("/todos")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `manage_todos` — function (async), line 289
- **route:** `POST /todos`
- decorator: `router.post("/todos")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_emails` — function (async), line 298
- **route:** `GET /emails`
- decorator: `router.get("/emails")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_email` — function (async), line 330
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

## `_email_draft_document_content` — function, line 356
- **called from:**
- `routes/codex_routes.py:400`

## `clean` — function, line 357
- **called from:**
- `routes/codex_routes.py:362`
- `routes/codex_routes.py:363`
- `routes/codex_routes.py:364`
- `routes/codex_routes.py:365`
- `routes/codex_routes.py:366`
- `routes/codex_routes.py:367`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:294`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:335`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:336`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:300`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:343`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:344`
- `src/visual_report.py:98`
- `static/js/chat.js:3936`
- `static/js/chat.js:3936`
- `static/js/chatRenderer.js:255`
- `static/js/chatRenderer.js:255`
- `static/js/editor/nl-edit.js:203`

## `codex_email_draft_document` — function (async), line 385
- **route:** `POST /emails/draft-document`
- decorator: `router.post("/emails/draft-document")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_email_draft` — function (async), line 410
- **route:** `POST /emails/draft`
- decorator: `router.post("/emails/draft")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_email_send` — function (async), line 423
- **route:** `POST /emails/send`
- decorator: `router.post("/emails/send")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_list` — function (async), line 438
- **route:** `GET /memory`
- decorator: `router.get("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_add` — function (async), line 445
- **route:** `POST /memory`
- decorator: `router.post("/memory")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_list` — function (async), line 467
- **route:** `GET /calendar/events`
- decorator: `router.get("/calendar/events")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_create` — function (async), line 474
- **route:** `POST /calendar/events`
- decorator: `router.post("/calendar/events")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_library` — function (async), line 489
- **route:** `GET /documents`
- decorator: `router.get("/documents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_get` — function (async), line 515
- **route:** `GET /documents/{doc_id}`
- decorator: `router.get("/documents/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_memory_delete` — function (async), line 528
- **route:** `DELETE /memory/{memory_id}`
- decorator: `router.delete("/memory/{memory_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_calendar_delete` — function (async), line 535
- **route:** `DELETE /calendar/events/{uid}`
- decorator: `router.delete("/calendar/events/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_delete` — function (async), line 542
- **route:** `DELETE /documents/{doc_id}`
- decorator: `router.delete("/documents/{doc_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_documents_create` — function (async), line 549
- **route:** `POST /documents`
- decorator: `router.post("/documents")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_run_shell` — function (async), line 572
- **called from:**
- `routes/codex_routes.py:673`
- `routes/codex_routes.py:735`
- `routes/codex_routes.py:894`
- `tests/test_cookbook_dependency_completion_regression.py:695`
- `tests/test_cookbook_dependency_completion_regression.py:713`
- `tests/test_cookbook_dependency_completion_regression.py:730`
- `tests/test_cookbook_dependency_completion_regression.py:745`
- `tests/test_cookbook_dependency_completion_regression.py:777`
- `tests/test_cookbook_dependency_completion_regression.py:799`
- `tests/test_cookbook_dependency_completion_regression.py:814`
- `tests/test_cookbook_dependency_completion_regression.py:831`
- `tests/test_cookbook_dependency_completion_regression.py:845`
- `tests/test_cookbook_dependency_completion_regression.py:862`
- `tests/test_cookbook_dependency_completion_regression.py:882`
- `tests/test_cookbook_dependency_completion_regression.py:899`
- `tests/test_cookbook_dependency_completion_regression.py:929`
- `tests/test_cookbook_dependency_completion_regression.py:945`
- `tests/test_cookbook_dependency_completion_regression.py:978`
- `tests/test_cookbook_dependency_completion_regression.py:994`
- `tests/test_cookbook_dependency_completion_regression.py:1012`
- `tests/test_cookbook_dependency_completion_regression.py:1131`
- `tests/test_cookbook_dependency_completion_regression.py:1159`
- `tests/test_cookbook_dependency_completion_regression.py:1191`
- `tests/test_cookbook_dependency_completion_regression.py:1220`
- `tests/test_cookbook_dependency_completion_regression.py:1246`
- `tests/test_cookbook_dependency_completion_regression.py:1272`
- `tests/test_cookbook_dependency_completion_regression.py:1345`

## `_read_cookbook_state` — function, line 594
- **called from:**
- `routes/codex_routes.py:617`
- `routes/codex_routes.py:624`
- `routes/codex_routes.py:652`
- `routes/codex_routes.py:727`
- `routes/codex_routes.py:746`
- `routes/codex_routes.py:806`
- `routes/codex_routes.py:829`

## `_redact_task` — function, line 605
- **called from:**
- `routes/codex_routes.py:619`
- `routes/codex_routes.py:679`

## `codex_cookbook_tasks` — function (async), line 615
- **route:** `GET /cookbook/tasks`
- decorator: `router.get("/cookbook/tasks")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_servers` — function (async), line 622
- **route:** `GET /cookbook/servers`
- decorator: `router.get("/cookbook/servers")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_output` — function (async), line 641
- **route:** `GET /cookbook/output/{session_id}`
- decorator: `router.get("/cookbook/output/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_serve` — function (async), line 683
- **route:** `POST /cookbook/serve`
- decorator: `router.post("/cookbook/serve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_stop` — function (async), line 722
- **route:** `POST /cookbook/stop/{session_id}`
- decorator: `router.post("/cookbook/stop/{session_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_cached` — function (async), line 739
- **route:** `GET /cookbook/cached`
- decorator: `router.get("/cookbook/cached")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_dirs_for` — function, line 750
- **called from:**
- `routes/codex_routes.py:774`
- `src/tools/cookbook.py:2046`
- `src/tools/cookbook.py:2060`
- `src/tools/cookbook.py:2067`
- `src/tools/cookbook.py:2080`

## `codex_cookbook_presets` — function (async), line 801
- **route:** `GET /cookbook/presets`
- decorator: `router.get("/cookbook/presets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_serve_preset` — function (async), line 822
- **route:** `POST /cookbook/preset/{name}`
- decorator: `router.post("/cookbook/preset/{name}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `codex_cookbook_adopt` — function (async), line 872
- **route:** `POST /cookbook/adopt`
- decorator: `router.post("/cookbook/adopt")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_claude_routes` — function, line 928
- **called from:**
- `app.py:962`

## `plugin_zip` — function, line 938
- **route:** `GET /plugin.zip`
- decorator: `router.get("/plugin.zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
