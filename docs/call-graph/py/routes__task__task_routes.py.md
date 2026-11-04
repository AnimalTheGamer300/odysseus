# `routes/task/task_routes.py` — definitions & call sites

38 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_maybe_cascade_calendar_event` — function, line 28
- **called from:**
- `routes/task/task_routes.py:771`

## `_try_delete` — function, line 62
- **called from:**
- `routes/task/task_routes.py:81`
- `routes/task/task_routes.py:131`

## `TaskCreate` — class, line 141
- **called from:**
- `tests/test_auth_regressions.py:349`
- `tests/test_task_chain_owner_scope.py:70`
- `tests/test_task_cookbook_admin_gate.py:103`

## `TaskUpdate` — class, line 162
- **called from:**
- `tests/test_task_chain_owner_scope.py:91`
- `tests/test_task_chain_owner_scope.py:112`
- `tests/test_task_cookbook_admin_gate.py:167`
- `tests/test_task_cookbook_admin_gate.py:196`

## `_display_task_name` — function, line 183
- **called from:**
- `routes/task/task_routes.py:194`
- `routes/task/task_routes.py:945`

## `_task_to_dict` — function, line 190
- **called from:**
- `routes/task/task_routes.py:369`
- `routes/task/task_routes.py:557`
- `routes/task/task_routes.py:662`
- `routes/task/task_routes.py:752`
- `routes/task/task_routes.py:853`

## `_run_to_dict` — function, line 243
- **called from:**
- `routes/task/task_routes.py:933`
- `routes/task/task_routes.py:978`

## `_run_research_id` — function, line 257
- **called from:**
- `routes/task/task_routes.py:953`

## `_resolve_run_endpoint` — function, line 263
- **called from:**
- `routes/task/task_routes.py:951`

## `setup_task_routes` — function, line 298
- **called from:**
- `app.py:788`
- `tests/test_email_owner_scope.py:435`
- `tests/test_task_chain_owner_scope.py:38`
- `tests/test_task_cookbook_admin_gate.py:95`
- `tests/test_task_cookbook_admin_gate.py:215`

## `_owner` — function, line 301
- **called from:**
- `routes/assistant_routes.py:126`
- `routes/assistant_routes.py:139`
- `routes/assistant_routes.py:160`
- `routes/assistant_routes.py:272`
- `routes/assistant_routes.py:296`
- `routes/memory/memory_routes.py:88`
- `routes/memory/memory_routes.py:117`
- `routes/memory/memory_routes.py:151`
- `routes/memory/memory_routes.py:157`
- `routes/memory/memory_routes.py:173`
- `routes/memory/memory_routes.py:211`
- `routes/memory/memory_routes.py:246`
- `routes/memory/memory_routes.py:261`
- `routes/memory/memory_routes.py:296`
- `routes/memory/memory_routes.py:353`
- `routes/memory/memory_routes.py:394`
- `routes/memory/memory_routes.py:505`
- `routes/memory/memory_routes.py:519`
- `routes/memory/memory_routes.py:530`
- `routes/memory/memory_routes.py:552`
- `routes/note/note_routes.py:629`
- `routes/note/note_routes.py:653`
- `routes/note/note_routes.py:690`
- `routes/note/note_routes.py:707`
- `routes/note/note_routes.py:762`
- `routes/note/note_routes.py:781`
- `routes/note/note_routes.py:800`
- `routes/note/note_routes.py:819`
- `routes/note/note_routes.py:858`
- `routes/note/note_routes.py:904`
- `routes/skills_routes.py:1208`
- `routes/skills_routes.py:1217`
- `routes/skills_routes.py:1228`
- `routes/skills_routes.py:1354`
- `routes/skills_routes.py:1382`
- `routes/skills_routes.py:1420`
- `routes/skills_routes.py:1456`
- `routes/skills_routes.py:1467`
- `routes/skills_routes.py:1490`
- `routes/skills_routes.py:1567`
- `routes/skills_routes.py:1685`
- `routes/skills_routes.py:1713`
- `routes/skills_routes.py:1778`
- `routes/skills_routes.py:1792`
- `routes/skills_routes.py:1807`
- `routes/skills_routes.py:1858`
- `routes/skills_routes.py:1877`
- `routes/skills_routes.py:1894`
- `routes/task/task_routes.py:344`
- `routes/task/task_routes.py:375`
- `routes/task/task_routes.py:384`
- `routes/task/task_routes.py:453`
- `routes/task/task_routes.py:566`
- `routes/task/task_routes.py:575`
- `routes/task/task_routes.py:654`
- `routes/task/task_routes.py:668`
- `routes/task/task_routes.py:758`
- `routes/task/task_routes.py:780`
- `routes/task/task_routes.py:796`
- `routes/task/task_routes.py:820`
- … +9 more (grep the name in repo)

## `_generate_task_name` — function (async), line 304
- **called from:**
- `routes/task/task_routes.py:486`

## `list_tasks` — function (async), line 342
- decorator: `router.get("")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_tasks_onboarding` — function (async), line 374
- **route:** `GET /onboarding`
- decorator: `router.get("/onboarding")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_tasks_onboarding` — function (async), line 383
- **route:** `POST /onboarding`
- decorator: `router.post("/onboarding")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_is_admin` — function, line 430
- **called from:**
- `routes/task/task_routes.py:434`
- `routes/task/task_routes.py:1028`

## `_require_admin_for_task_action` — function, line 433
- **called from:**
- `routes/task/task_routes.py:463`
- `routes/task/task_routes.py:679`
- `routes/task/task_routes.py:804`
- `routes/task/task_routes.py:867`

## `_validate_then_task_id` — function, line 437
- **called from:**
- `routes/task/task_routes.py:513`
- `routes/task/task_routes.py:705`

## `create_task` — function (async), line 452
- decorator: `router.post("")`
- **called from:**
- `app.py:220`
- `app.py:456`
- `app.py:664`
- `app.py:1058`
- `app.py:1088`
- `app.py:1105`
- `app.py:1124`
- `app.py:1142`
- `app.py:1237`
- `app.py:1267`
- `app.py:1276`
- `routes/chat_helpers.py:85`
- `routes/chat_routes.py:2136`
- `routes/chat_routes.py:2146`
- `routes/cookbook_routes.py:2806`
- `routes/cookbook_routes.py:4218`
- `routes/email_pollers.py:1546`
- `routes/email_routes.py:433`
- `routes/email_routes.py:3275`
- `routes/model_routes.py:1748`
- `routes/shell_routes.py:639`
- `routes/shell_routes.py:1061`
- `routes/shell_routes.py:1062`
- `routes/skills_routes.py:1558`
- `routes/skills_routes.py:1666`
- `routes/skills_routes.py:1772`
- `services/research/research_handler.py:102`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `src/agent_jobs.py:181`
- `src/agent_jobs.py:363`
- `src/agent_loop.py:5102`
- `src/agent_loop.py:6380`
- `src/agent_runs.py:95`
- `src/agent_runs.py:201`
- `src/agent_tools/subprocess_tools.py:246`
- `src/agent_tools/subprocess_tools.py:247`
- `src/agent_tools/subprocess_tools.py:248`
- `src/ai_interaction.py:1372`
- `src/ai_interaction.py:1639`
- `src/bg_monitor.py:166`
- `src/builtin_mcp.py:102`
- `src/event_bus.py:40`
- `src/mcp_manager.py:318`
- `src/mcp_manager.py:433`
- `src/research_handler.py:403`
- `src/task_scheduler.py:550`
- `src/task_scheduler.py:559`
- `src/task_scheduler.py:733`
- `src/task_scheduler.py:920`
- `src/task_scheduler.py:1085`
- `src/task_scheduler.py:2258`
- `src/task_scheduler.py:2264`
- `src/teacher_escalation.py:502`
- `src/teacher_escalation.py:523`
- `tests/test_builtin_mcp_bg_tasks.py:97`
- `tests/test_compare_stop_disconnect_poll.py:270`
- `tests/test_email_summary_llm.py:164`
- `tests/test_email_summary_llm.py:184`
- `tests/test_email_urgency_checkpoint.py:188`
- … +19 more (grep the name in repo)

## `get_notifications` — function (async), line 562
- **route:** `GET /notifications`
- decorator: `router.get("/notifications")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_task_cache` — function (async), line 573
- **route:** `POST /{task_id}/clear-cache`
- decorator: `router.post("/{task_id}/clear-cache")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_task` — function (async), line 653
- **route:** `GET /{task_id}`
- decorator: `router.get("/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_task` — function (async), line 667
- **route:** `PUT /{task_id}`
- decorator: `router.put("/{task_id}")`
- **called from:**
- `tests/test_task_chain_owner_scope.py:88`
- `tests/test_task_chain_owner_scope.py:109`
- `tests/test_task_cookbook_admin_gate.py:164`
- `tests/test_task_cookbook_admin_gate.py:193`

## `delete_task` — function (async), line 757
- **route:** `DELETE /{task_id}`
- decorator: `router.delete("/{task_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `pause_task` — function (async), line 779
- **route:** `POST /{task_id}/pause`
- decorator: `router.post("/{task_id}/pause")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `resume_task` — function (async), line 795
- **route:** `POST /{task_id}/resume`
- decorator: `router.post("/{task_id}/resume")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `revert_task` — function (async), line 818
- **route:** `POST /{task_id}/revert`
- decorator: `router.post("/{task_id}/revert")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run_task_now` — function (async), line 858
- **route:** `POST /{task_id}/run`
- decorator: `router.post("/{task_id}/run")`
- **called from:**
- `routes/assistant_routes.py:289`
- `routes/task/task_routes.py:870`
- `routes/task/task_routes.py:1067`
- `src/event_bus.py:109`
- `src/tools/system.py:475`

## `stop_task_now` — function (async), line 876
- **route:** `POST /{task_id}/stop`
- decorator: `router.post("/{task_id}/stop")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_recent_runs` — function (async), line 893
- **route:** `GET /runs/recent`
- decorator: `router.get("/runs/recent")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_clip_run` — function, line 932
- **called from:**
- `routes/task/task_routes.py:944`

## `list_runs` — function (async), line 965
- **route:** `GET /{task_id}/runs`
- decorator: `router.get("/{task_id}/runs")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_output_targets` — function (async), line 983
- **route:** `GET /meta/output-targets`
- decorator: `router.get("/meta/output-targets")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_actions` — function (async), line 1021
- **route:** `GET /meta/actions`
- decorator: `router.get("/meta/actions")`
- **called from:**
- `tests/test_task_cookbook_admin_gate.py:302`
- `tests/test_task_cookbook_admin_gate.py:329`

## `list_events` — function (async), line 1032
- **route:** `GET /meta/events`
- decorator: `router.get("/meta/events")`
- **called from:**
- `tests/test_calendar_owner_scope.py:290`

## `webhook_trigger` — function (async), line 1046
- **route:** `POST /{task_id}/webhook/{token}`
- decorator: `router.post("/{task_id}/webhook/{token}")`
- **called from:**
- `tests/test_task_cookbook_admin_gate.py:244`

## `regenerate_webhook` — function (async), line 1073
- **route:** `POST /{task_id}/webhook-regenerate`
- decorator: `router.post("/{task_id}/webhook-regenerate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `parse_task` — function (async), line 1090
- **route:** `POST /parse`
- decorator: `router.post("/parse")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
