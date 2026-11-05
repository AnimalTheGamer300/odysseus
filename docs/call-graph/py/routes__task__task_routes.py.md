# `routes/task/task_routes.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_seal_request_task_authority` — function, line 29
- **called from:**
- `routes/task/task_routes.py:545`
- `routes/task/task_routes.py:755`
- `tests/test_request_authority.py:436`

## `_maybe_cascade_calendar_event` — function, line 37
- **called from:**
- `routes/task/task_routes.py:843`

## `_try_delete` — function, line 71
- **called from:**
- `routes/task/task_routes.py:90`
- `routes/task/task_routes.py:140`

## `TaskCreate` — class, line 150
- **called from:**
- `tests/test_auth_regressions.py:356`
- `tests/test_endpoint_registered_authority.py:205`
- `tests/test_endpoint_registered_authority.py:231`
- `tests/test_endpoint_registered_authority.py:256`
- `tests/test_endpoint_registered_authority.py:271`
- `tests/test_task_chain_owner_scope.py:70`
- `tests/test_task_cookbook_admin_gate.py:103`

## `TaskUpdate` — class, line 171
- **called from:**
- `tests/test_endpoint_registered_authority.py:218`
- `tests/test_endpoint_registered_authority.py:236`
- `tests/test_endpoint_registered_authority.py:260`
- `tests/test_endpoint_registered_authority.py:275`
- `tests/test_endpoint_registered_authority.py:282`
- `tests/test_task_chain_owner_scope.py:91`
- `tests/test_task_chain_owner_scope.py:112`
- `tests/test_task_cookbook_admin_gate.py:167`
- `tests/test_task_cookbook_admin_gate.py:196`

## `_display_task_name` — function, line 192
- **called from:**
- `routes/task/task_routes.py:203`
- `routes/task/task_routes.py:1017`

## `_task_to_dict` — function, line 199
- **called from:**
- `routes/task/task_routes.py:378`
- `routes/task/task_routes.py:571`
- `routes/task/task_routes.py:727`
- `routes/task/task_routes.py:824`
- `routes/task/task_routes.py:925`

## `_run_to_dict` — function, line 252
- **called from:**
- `routes/task/task_routes.py:1005`
- `routes/task/task_routes.py:1050`

## `_run_research_id` — function, line 266
- **called from:**
- `routes/task/task_routes.py:1025`

## `_resolve_run_endpoint` — function, line 272
- **called from:**
- `routes/task/task_routes.py:1023`
- `tests/test_pinned_model_route_selection.py:72`
- `tests/test_pinned_model_route_selection.py:79`
- `tests/test_pinned_model_route_selection.py:85`

## `setup_task_routes` — function, line 307
- **called from:**
- `app.py:872`
- `tests/test_codeql_python_residual_security.py:143`
- `tests/test_email_owner_scope.py:435`
- `tests/test_endpoint_registered_authority.py:203`
- `tests/test_endpoint_registered_authority.py:216`
- `tests/test_endpoint_registered_authority.py:228`
- `tests/test_endpoint_registered_authority.py:253`
- `tests/test_endpoint_registered_authority.py:268`
- `tests/test_endpoint_registered_authority.py:280`
- `tests/test_task_chain_owner_scope.py:38`
- `tests/test_task_cookbook_admin_gate.py:95`
- `tests/test_task_cookbook_admin_gate.py:215`

## `_owner` — function, line 310
- **called from:**
- `routes/assistant_routes.py:127`
- `routes/assistant_routes.py:140`
- `routes/assistant_routes.py:161`
- `routes/assistant_routes.py:279`
- `routes/assistant_routes.py:303`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:274`
- `routes/memory/memory_routes.py:299`
- `routes/memory/memory_routes.py:357`
- `routes/memory/memory_routes.py:398`
- `routes/memory/memory_routes.py:512`
- `routes/memory/memory_routes.py:526`
- `routes/memory/memory_routes.py:537`
- `routes/memory/memory_routes.py:559`
- `routes/note/note_routes.py:632`
- `routes/note/note_routes.py:656`
- `routes/note/note_routes.py:694`
- `routes/note/note_routes.py:711`
- `routes/note/note_routes.py:771`
- `routes/note/note_routes.py:790`
- `routes/note/note_routes.py:809`
- `routes/note/note_routes.py:828`
- `routes/note/note_routes.py:867`
- `routes/note/note_routes.py:913`
- `routes/skills_routes.py:317`
- `routes/skills_routes.py:326`
- `routes/skills_routes.py:337`
- `routes/skills_routes.py:463`
- `routes/skills_routes.py:491`
- `routes/skills_routes.py:529`
- `routes/skills_routes.py:565`
- `routes/skills_routes.py:576`
- `routes/skills_routes.py:605`
- `routes/skills_routes.py:666`
- `routes/skills_routes.py:720`
- `routes/skills_routes.py:736`
- `routes/skills_routes.py:767`
- `routes/skills_routes.py:772`
- `routes/skills_routes.py:779`
- `routes/skills_routes.py:830`
- `routes/skills_routes.py:853`
- `routes/skills_routes.py:870`
- `routes/task/task_routes.py:353`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:393`
- `routes/task/task_routes.py:462`
- `routes/task/task_routes.py:580`
- `routes/task/task_routes.py:589`
- `routes/task/task_routes.py:617`
- `routes/task/task_routes.py:640`
- `routes/task/task_routes.py:719`
- `routes/task/task_routes.py:733`
- `routes/task/task_routes.py:830`
- … +16 more (grep the name in repo)

## `_generate_task_name` — function (async), line 313
- **called from:**
- `routes/task/task_routes.py:492`

## `list_tasks` — function (async), line 351
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_tasks_onboarding` — function (async), line 383
- **route:** `GET /onboarding`
- decorator: `router.get("/onboarding")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_tasks_onboarding` — function (async), line 392
- **route:** `POST /onboarding`
- decorator: `router.post("/onboarding")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_is_admin` — function, line 439
- **called from:**
- `routes/editor_agent_routes.py:1985`
- `routes/editor_agent_routes.py:2052`
- `routes/task/task_routes.py:443`
- `routes/task/task_routes.py:1100`

## `_require_admin_for_task_action` — function, line 442
- **called from:**
- `routes/task/task_routes.py:472`
- `routes/task/task_routes.py:744`
- `routes/task/task_routes.py:876`
- `routes/task/task_routes.py:939`

## `_validate_then_task_id` — function, line 446
- **called from:**
- `routes/task/task_routes.py:519`
- `routes/task/task_routes.py:780`

## `create_task` — function (async), line 461
- decorator: `router.post("")`
- **called from:**
- `app.py:232`
- `app.py:497`
- `app.py:742`
- `app.py:1228`
- `app.py:1231`
- `app.py:1261`
- `app.py:1283`
- `app.py:1308`
- `app.py:1326`
- `app.py:1429`
- `app.py:1443`
- `app.py:1451`
- `routes/chat_helpers.py:370`
- `routes/chat_routes.py:4412`
- `routes/chat_routes.py:4422`
- `routes/cookbook_routes.py:2685`
- `routes/cookbook_routes.py:4124`
- `routes/email/email_pollers.py:1746`
- `routes/email/email_routes.py:477`
- `routes/email/email_routes.py:4089`
- `routes/email/email_routes.py:6861`
- `routes/model_routes.py:1896`
- `routes/shell_routes.py:876`
- `routes/shell_routes.py:1295`
- `routes/shell_routes.py:1296`
- `services/research/research_handler.py:102`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `services/skills/job_coordinator.py:49`
- `services/skills/job_coordinator.py:110`
- `services/skills/job_coordinator.py:189`
- `src/agent_jobs.py:181`
- `src/agent_jobs.py:363`
- `src/agent_loop.py:25995`
- `src/agent_loop.py:34298`
- `src/agent_runs.py:97`
- `src/agent_runs.py:213`
- `src/agent_tools/subprocess_tools.py:790`
- `src/ai_interaction.py:1769`
- `src/ai_interaction.py:2087`
- `src/bg_monitor.py:245`
- `src/browser_identity.py:152`
- `src/builtin_mcp.py:102`
- `src/clean_agent_preview.py:5601`
- `src/clean_agent_preview.py:5606`
- `src/containment.py:1049`
- `src/containment.py:1109`
- `src/containment.py:1140`
- `src/containment.py:1164`
- `src/event_bus.py:50`
- `src/mcp_manager.py:348`
- `src/mcp_manager.py:510`
- `src/research_handler.py:421`
- `src/task_scheduler.py:691`
- `src/task_scheduler.py:700`
- `src/task_scheduler.py:877`
- `src/task_scheduler.py:1066`
- `src/task_scheduler.py:1218`
- `src/task_scheduler.py:2453`
- `src/task_scheduler.py:2459`
- … +67 more (grep the name in repo)

## `get_notifications` — function (async), line 576
- **route:** `GET /notifications`
- decorator: `router.get("/notifications")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_notification_logs` — function (async), line 587
- **route:** `GET /notification-logs`
- decorator: `router.get("/notification-logs")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_notification_log` — function (async), line 615
- **route:** `POST /notification-logs`
- decorator: `router.post("/notification-logs")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_task_cache` — function (async), line 638
- **route:** `POST /{task_id}/clear-cache`
- decorator: `router.post("/{task_id}/clear-cache")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_task` — function (async), line 718
- **route:** `GET /{task_id}`
- decorator: `router.get("/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_task` — function (async), line 732
- **route:** `PUT /{task_id}`
- decorator: `router.put("/{task_id}")`
- **called from:**
- `tests/test_task_chain_owner_scope.py:88`
- `tests/test_task_chain_owner_scope.py:109`
- `tests/test_task_cookbook_admin_gate.py:164`
- `tests/test_task_cookbook_admin_gate.py:193`

## `delete_task` — function (async), line 829
- **route:** `DELETE /{task_id}`
- decorator: `router.delete("/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `pause_task` — function (async), line 851
- **route:** `POST /{task_id}/pause`
- decorator: `router.post("/{task_id}/pause")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `resume_task` — function (async), line 867
- **route:** `POST /{task_id}/resume`
- decorator: `router.post("/{task_id}/resume")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `revert_task` — function (async), line 890
- **route:** `POST /{task_id}/revert`
- decorator: `router.post("/{task_id}/revert")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_task_now` — function (async), line 930
- **route:** `POST /{task_id}/run`
- decorator: `router.post("/{task_id}/run")`
- **called from:**
- `routes/assistant_routes.py:296`
- `routes/task/task_routes.py:942`
- `routes/task/task_routes.py:1139`
- `src/event_bus.py:121`
- `src/tools/system.py:688`
- `tests/test_task_scheduler_cancel.py:212`

## `stop_task_now` — function (async), line 948
- **route:** `POST /{task_id}/stop`
- decorator: `router.post("/{task_id}/stop")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_recent_runs` — function (async), line 965
- **route:** `GET /runs/recent`
- decorator: `router.get("/runs/recent")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_clip_run` — function, line 1004
- **called from:**
- `routes/task/task_routes.py:1016`

## `list_runs` — function (async), line 1037
- **route:** `GET /{task_id}/runs`
- decorator: `router.get("/{task_id}/runs")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_output_targets` — function (async), line 1055
- **route:** `GET /meta/output-targets`
- decorator: `router.get("/meta/output-targets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_actions` — function (async), line 1093
- **route:** `GET /meta/actions`
- decorator: `router.get("/meta/actions")`
- **called from:**
- `tests/test_task_cookbook_admin_gate.py:302`
- `tests/test_task_cookbook_admin_gate.py:329`

## `list_events` — function (async), line 1104
- **route:** `GET /meta/events`
- decorator: `router.get("/meta/events")`
- **called from:**
- `tests/test_calendar_owner_scope.py:292`

## `webhook_trigger` — function (async), line 1118
- **route:** `POST /{task_id}/webhook/{token}`
- decorator: `router.post("/{task_id}/webhook/{token}")`
- **called from:**
- `tests/test_task_cookbook_admin_gate.py:244`

## `regenerate_webhook` — function (async), line 1145
- **route:** `POST /{task_id}/webhook-regenerate`
- decorator: `router.post("/{task_id}/webhook-regenerate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `parse_task` — function (async), line 1162
- **route:** `POST /parse`
- decorator: `router.post("/parse")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
