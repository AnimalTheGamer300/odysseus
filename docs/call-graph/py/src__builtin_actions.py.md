# `src/builtin_actions.py` — definitions & call sites

67 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_read_email_urgency_state` — function, line 23
- **called from:**
- `src/builtin_actions.py:121`
- `src/builtin_actions.py:2389`

## `_email_urgency_account_generations` — function, line 39
- **called from:**
- `src/builtin_actions.py:242`
- `src/builtin_actions.py:251`
- `src/builtin_actions.py:252`
- `src/builtin_actions.py:282`
- `src/builtin_actions.py:2349`
- `src/builtin_actions.py:2391`

## `_email_urgency_string_set` — function, line 75
- **called from:**
- `src/builtin_actions.py:235`
- `src/builtin_actions.py:335`
- `src/builtin_actions.py:341`
- `src/builtin_actions.py:2990`

## `_acquire_email_urgency_state_lock` — function, line 81
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_close_email_urgency_state_lock` — function, line 126
- **called from:**
- `src/builtin_actions.py:199`
- `src/builtin_actions.py:216`

## `_commit_email_urgency_state` — function, line 138
- **called from:**
- `src/builtin_actions.py:211`

## `_run_email_urgency_state_transaction` — function (async), line 159
- **called from:**
- `src/builtin_actions.py:2359`
- `src/builtin_actions.py:2423`
- `src/builtin_actions.py:3053`
- `tests/test_email_urgency_checkpoint.py:182`
- `tests/test_email_urgency_checkpoint.py:408`
- `tests/test_email_urgency_checkpoint.py:414`
- `tests/test_email_urgency_checkpoint.py:426`

## `_email_urgency_account_key` — function, line 220
- **called from:**
- `src/builtin_actions.py:232`
- `src/builtin_actions.py:234`
- `src/builtin_actions.py:285`
- `src/builtin_actions.py:314`
- `src/builtin_actions.py:317`
- `src/builtin_actions.py:328`
- `src/builtin_actions.py:339`
- `src/builtin_actions.py:342`
- `src/builtin_actions.py:349`
- `src/builtin_actions.py:353`
- `src/builtin_actions.py:2994`
- `src/builtin_actions.py:3007`

## `_email_urgency_payload_account_ids` — function, line 224
- **called from:**
- `src/builtin_actions.py:241`
- `src/builtin_actions.py:292`
- `src/builtin_actions.py:2394`

## `_email_urgency_known_account_ids` — function, line 239
- **called from:**
- `src/builtin_actions.py:2395`

## `_email_urgency_stale_accounts` — function, line 246
- **called from:**
- `src/builtin_actions.py:287`
- `src/builtin_actions.py:2996`

## `_merge_email_urgency_state` — function, line 263
- **called from:**
- `src/builtin_actions.py:2341`
- `src/builtin_actions.py:2409`
- `src/builtin_actions.py:3040`
- `tests/test_email_urgency_checkpoint.py:219`
- `tests/test_email_urgency_checkpoint.py:254`
- `tests/test_email_urgency_checkpoint.py:271`
- `tests/test_email_urgency_checkpoint.py:308`
- `tests/test_email_urgency_checkpoint.py:347`
- `tests/test_email_urgency_checkpoint.py:375`

## `TaskNoop` — class, line 412
- **called from:**
- `src/builtin_actions.py:496`
- `src/builtin_actions.py:743`
- `src/builtin_actions.py:826`
- `src/builtin_actions.py:833`
- `src/builtin_actions.py:846`
- `src/builtin_actions.py:886`
- `src/builtin_actions.py:1018`
- `src/builtin_actions.py:1039`
- `src/builtin_actions.py:1075`
- `src/builtin_actions.py:1103`
- `src/builtin_actions.py:1277`
- `src/builtin_actions.py:1515`
- `src/builtin_actions.py:1551`
- `src/builtin_actions.py:1557`
- `src/builtin_actions.py:1561`
- `src/builtin_actions.py:1931`
- `src/builtin_actions.py:2054`
- `src/builtin_actions.py:2063`
- `src/builtin_actions.py:2168`
- `src/builtin_actions.py:2237`
- `src/builtin_actions.py:2429`
- `src/builtin_actions.py:3068`
- `src/document_actions.py:192`

## `TaskDeferred` — class, line 424
- **called from:**
- `src/builtin_actions.py:2072`

## `TaskDeferred.__init__` — method, line 427
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `action_tidy_sessions` — function (async), line 433
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_tidy_documents` — function (async), line 453
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_consolidate_memory` — function (async), line 464
- **called from:**
- `tests/test_builtin_memory_consolidation.py:80`
- `tests/test_builtin_memory_consolidation.py:109`
- `tests/test_builtin_memory_consolidation.py:153`
- `tests/test_consolidate_memory_explicit_drops.py:51`

## `_memory_owner` — function, line 480
- **called from:**
- `src/builtin_actions.py:487`
- `src/builtin_actions.py:492`

## `_normalized_memory_text` — function, line 505
- **called from:**
- `src/builtin_actions.py:525`
- `src/builtin_actions.py:526`

## `_memory_rank` — function, line 510
- **called from:**
- `src/builtin_actions.py:554`
- `src/builtin_actions.py:554`

## `_same_memory_fact` — function, line 520
- **called from:**
- `src/builtin_actions.py:547`

## `_dedupe_group` — function, line 536
- **called from:**
- `src/builtin_actions.py:688`

## `_try_ai_tidy_group` — function (async), line 563
- **called from:**
- `src/builtin_actions.py:699`

## `_run_subprocess` — function (async), line 752
- **called from:**
- `src/builtin_actions.py:779`
- `src/builtin_actions.py:780`
- `src/builtin_actions.py:781`
- `src/builtin_actions.py:782`
- `src/builtin_actions.py:794`
- `src/builtin_actions.py:795`
- `src/builtin_actions.py:796`
- `src/builtin_actions.py:804`
- `src/builtin_actions.py:805`

## `action_ssh_command` — function (async), line 771
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_run_script` — function (async), line 787
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_run_local` — function (async), line 799
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_tidy_research` — function (async), line 808
- **called from:**
- `tests/test_tidy_research_owner_scope.py:74`
- `tests/test_tidy_research_owner_scope.py:93`
- `tests/test_tidy_research_owner_scope.py:104`
- `tests/test_tidy_research_owner_scope.py:128`
- `tests/test_tidy_research_owner_scope.py:140`
- `tests/test_tidy_research_owner_scope.py:153`

## `action_tidy_calendar` — function (async), line 853
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_result_has_work` — function, line 957
- **called from:**
- `src/builtin_actions.py:1017`
- `src/builtin_actions.py:1038`
- `src/builtin_actions.py:1548`
- `tests/test_builtin_actions_nonstring.py:11`
- `tests/test_builtin_actions_nonstring.py:12`
- `tests/test_builtin_actions_nonstring.py:21`

## `_result_is_config_error` — function, line 975
- **called from:**
- `src/builtin_actions.py:1015`
- `src/builtin_actions.py:1036`
- `src/builtin_actions.py:1546`

## `_email_task_account_id` — function, line 986
- **called from:**
- `src/builtin_actions.py:1013`
- `src/builtin_actions.py:1032`
- `src/builtin_actions.py:1078`
- `src/builtin_actions.py:1524`
- `src/builtin_actions.py:2304`

## `action_summarize_emails` — function (async), line 1006
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_draft_email_replies` — function (async), line 1025
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_email_auto_translate` — function (async), line 1046
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cached` — function, line 1105
- **called from:**
- `src/builtin_actions.py:1227`
- `src/task_scheduler.py:1439`
- `src/task_scheduler.py:1476`
- `tests/test_task_scheduler_cache.py:25`
- `tests/test_task_scheduler_cache.py:31`
- `tests/test_task_scheduler_cache.py:46`
- `tests/test_task_scheduler_cache.py:62`
- `tests/test_task_scheduler_cache.py:68`
- `tests/test_task_scheduler_cache.py:86`

## `_store` — function, line 1118
- **called from:**
- `src/builtin_actions.py:1232`
- `src/builtin_actions.py:1248`
- `tests/test_rag_keyword_fallback_owner.py:38`
- `tests/test_rag_keyword_fallback_owner.py:51`
- `tests/test_rag_vector_rename_owner.py:64`

## `_translate` — function (async), line 1144
- **called from:**
- `src/builtin_actions.py:1230`

## `_classify_event_heuristic` — function, line 1322
- **called from:**
- `src/builtin_actions.py:1404`
- `tests/test_builtin_actions_nonstring.py:16`

## `_memory_context_lines` — function, line 1337
- **called from:**
- `src/builtin_actions.py:1388`
- `tests/test_classify_events_memory_text.py:18`
- `tests/test_classify_events_memory_text.py:28`
- `tests/test_classify_events_memory_text.py:33`

## `action_classify_events` — function (async), line 1355
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:92`

## `action_ping_events` — function (async), line 1513
- **called from:**
- `src/task_scheduler.py:637`

## `action_extract_email_events` — function (async), line 1518
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_learn_sender_signatures` — function (async), line 1579
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:129`
- `tests/test_builtin_actions_owner_scope.py:212`
- `tests/test_imap_uid_commands.py:55`
- `tests/test_imap_uid_commands.py:72`

## `_pull_headers` — function, line 1595
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_bodies` — function, line 1682
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_daily_brief` — function (async), line 1781
- **called from:**
- `tests/test_imap_uid_commands.py:104`

## `action_test_skills` — function (async), line 1910
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_audit_skills` — function (async), line 2034
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_ping_notes` — function (async), line 2103
- **called from:**
- `src/task_scheduler.py:617`

## `_parse_due` — function, line 2138
- **called from:**
- `src/builtin_actions.py:2178`

## `action_check_email_urgency` — function (async), line 2250
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:257`
- `tests/test_email_urgency_checkpoint.py:499`
- `tests/test_email_urgency_checkpoint.py:546`
- `tests/test_email_urgency_checkpoint.py:612`
- `tests/test_email_urgency_checkpoint.py:668`
- `tests/test_email_urgency_checkpoint.py:684`
- `tests/test_email_urgency_checkpoint.py:762`
- `tests/test_email_urgency_checkpoint.py:776`
- `tests/test_email_urgency_checkpoint.py:821`
- `tests/test_email_urgency_checkpoint.py:826`
- `tests/test_email_urgency_checkpoint.py:857`
- `tests/test_email_urgency_checkpoint.py:866`
- `tests/test_email_urgency_checkpoint.py:884`
- `tests/test_email_urgency_checkpoint.py:896`
- `tests/test_email_urgency_checkpoint.py:963`
- `tests/test_email_urgency_checkpoint.py:969`
- `tests/test_email_urgency_checkpoint.py:1037`
- `tests/test_email_urgency_checkpoint.py:1043`
- `tests/test_email_urgency_checkpoint.py:1087`
- `tests/test_email_urgency_checkpoint.py:1091`
- `tests/test_email_urgency_checkpoint.py:1095`
- `tests/test_email_urgency_checkpoint.py:1131`
- `tests/test_email_urgency_checkpoint.py:1137`
- `tests/test_email_urgency_checkpoint.py:1174`
- `tests/test_email_urgency_checkpoint.py:1189`
- `tests/test_email_urgency_checkpoint.py:1226`
- `tests/test_email_urgency_checkpoint.py:1233`
- `tests/test_email_urgency_checkpoint.py:1274`
- `tests/test_email_urgency_checkpoint.py:1276`
- `tests/test_email_urgency_checkpoint.py:1292`
- `tests/test_email_urgency_checkpoint.py:1319`
- `tests/test_email_urgency_checkpoint.py:1321`

## `_enumerate_enabled_accounts` — function, line 2310
- **called from:**
- `src/builtin_actions.py:2330`
- `src/builtin_actions.py:2370`

## `_register_accounts` — function (async), line 2340
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_retire_accounts` — function (async), line 2408
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_heuristic_email_verdict` — function, line 2447
- **called from:**
- `src/builtin_actions.py:2703`

## `add_response` — function, line 2455
- **called from:**
- `src/builtin_actions.py:2484`
- `src/builtin_actions.py:2489`

## `add_type` — function, line 2459
- **called from:**
- `app.py:27`
- `app.py:28`
- `src/builtin_actions.py:2472`
- `src/builtin_actions.py:2474`
- `src/builtin_actions.py:2476`
- `src/builtin_actions.py:2478`
- `src/builtin_actions.py:2480`
- `src/builtin_actions.py:2482`

## `_scan_one` — function, line 2538
- **called from:**
- `src/tools/cookbook.py:1627`
- `src/tools/cookbook.py:1631`
- `src/tools/cookbook.py:1639`

## `_urgency_reminder_payload` — function, line 2943
- **called from:**
- `src/builtin_actions.py:2981`

## `_dispatch_urgency_reminder` — function (async), line 2977
- **called from:**
- `src/builtin_actions.py:3016`

## `_dispatch_and_checkpoint` — function (async), line 2989
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fmt_tag_write` — function, line 3081
- **called from:**
- `src/builtin_actions.py:3115`

## `_fmt_one` — function, line 3096
- **called from:**
- `src/builtin_actions.py:3127`

## `action_cookbook_serve` — function (async), line 3151
- **called from:**
- `tests/test_builtin_actions_cookbook_serve_state.py:29`

## `_short` — function, line 3208
- **called from:**
- `src/builtin_actions.py:3232`
