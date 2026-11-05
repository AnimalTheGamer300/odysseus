# `src/builtin_actions.py` — definitions & call sites

70 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_heuristic_email_urgency_verdict` — function, line 30
- **called from:**
- `src/builtin_actions.py:2967`
- `tests/test_email_urgency_checkpoint.py:155`
- `tests/test_email_urgency_checkpoint.py:174`

## `add_response` — function, line 51
- **called from:**
- `src/builtin_actions.py:93`
- `src/builtin_actions.py:106`

## `add_type` — function, line 55
- **called from:**
- `app.py:29`
- `app.py:30`
- `src/builtin_actions.py:81`
- `src/builtin_actions.py:83`
- `src/builtin_actions.py:85`
- `src/builtin_actions.py:87`
- `src/builtin_actions.py:89`
- `src/builtin_actions.py:91`

## `_read_email_urgency_state` — function, line 147
- **called from:**
- `src/builtin_actions.py:245`
- `src/builtin_actions.py:2735`

## `_email_urgency_account_generations` — function, line 163
- **called from:**
- `src/builtin_actions.py:366`
- `src/builtin_actions.py:375`
- `src/builtin_actions.py:376`
- `src/builtin_actions.py:406`
- `src/builtin_actions.py:2695`
- `src/builtin_actions.py:2737`

## `_email_urgency_string_set` — function, line 199
- **called from:**
- `src/builtin_actions.py:359`
- `src/builtin_actions.py:459`
- `src/builtin_actions.py:465`
- `src/builtin_actions.py:3273`

## `_acquire_email_urgency_state_lock` — function, line 205
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_close_email_urgency_state_lock` — function, line 250
- **called from:**
- `src/builtin_actions.py:323`
- `src/builtin_actions.py:340`

## `_commit_email_urgency_state` — function, line 262
- **called from:**
- `src/builtin_actions.py:335`

## `_run_email_urgency_state_transaction` — function (async), line 283
- **called from:**
- `src/builtin_actions.py:2705`
- `src/builtin_actions.py:2769`
- `src/builtin_actions.py:3336`
- `tests/test_email_urgency_checkpoint.py:220`
- `tests/test_email_urgency_checkpoint.py:446`
- `tests/test_email_urgency_checkpoint.py:452`
- `tests/test_email_urgency_checkpoint.py:464`

## `_email_urgency_account_key` — function, line 344
- **called from:**
- `src/builtin_actions.py:356`
- `src/builtin_actions.py:358`
- `src/builtin_actions.py:409`
- `src/builtin_actions.py:438`
- `src/builtin_actions.py:441`
- `src/builtin_actions.py:452`
- `src/builtin_actions.py:463`
- `src/builtin_actions.py:466`
- `src/builtin_actions.py:473`
- `src/builtin_actions.py:477`
- `src/builtin_actions.py:3277`
- `src/builtin_actions.py:3290`

## `_email_urgency_payload_account_ids` — function, line 348
- **called from:**
- `src/builtin_actions.py:365`
- `src/builtin_actions.py:416`
- `src/builtin_actions.py:2740`

## `_email_urgency_known_account_ids` — function, line 363
- **called from:**
- `src/builtin_actions.py:2741`

## `_email_urgency_stale_accounts` — function, line 370
- **called from:**
- `src/builtin_actions.py:411`
- `src/builtin_actions.py:3279`

## `_merge_email_urgency_state` — function, line 387
- **called from:**
- `src/builtin_actions.py:2687`
- `src/builtin_actions.py:2755`
- `src/builtin_actions.py:3323`
- `tests/test_email_urgency_checkpoint.py:257`
- `tests/test_email_urgency_checkpoint.py:292`
- `tests/test_email_urgency_checkpoint.py:309`
- `tests/test_email_urgency_checkpoint.py:346`
- `tests/test_email_urgency_checkpoint.py:385`
- `tests/test_email_urgency_checkpoint.py:413`

## `TaskNoop` — class, line 536
- **called from:**
- `src/builtin_actions.py:620`
- `src/builtin_actions.py:871`
- `src/builtin_actions.py:960`
- `src/builtin_actions.py:967`
- `src/builtin_actions.py:980`
- `src/builtin_actions.py:1020`
- `src/builtin_actions.py:1162`
- `src/builtin_actions.py:1185`
- `src/builtin_actions.py:1221`
- `src/builtin_actions.py:1249`
- `src/builtin_actions.py:1440`
- `src/builtin_actions.py:1688`
- `src/builtin_actions.py:1726`
- `src/builtin_actions.py:1732`
- `src/builtin_actions.py:1736`
- `src/builtin_actions.py:2142`
- `src/builtin_actions.py:2269`
- `src/builtin_actions.py:2278`
- `src/builtin_actions.py:2400`
- `src/builtin_actions.py:2487`
- `src/builtin_actions.py:2775`
- `src/builtin_actions.py:3351`
- `src/document_actions.py:192`

## `TaskDeferred` — class, line 548
- **called from:**
- `src/builtin_actions.py:2290`
- `src/builtin_actions.py:2297`
- `src/builtin_actions.py:2316`

## `TaskDeferred.__init__` — method, line 551
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email/email_helpers.py:205`
- `routes/email/email_helpers.py:220`
- `routes/email/email_helpers.py:232`
- `routes/email/email_helpers.py:248`
- `routes/email/email_routes.py:1664`
- `scripts/css_snapshot.py:194`
- `scripts/probe_browser_budget.py:56`
- `src/agent_tools/document_tools.py:759`
- `src/agent_tools/filesystem_tools.py:384`
- `src/builtin_actions.py:552`
- `src/chatgpt_subscription.py:495`
- `src/containment.py:170`
- `src/outbound_fetch.py:220`
- `src/path_confinement.py:81`
- `src/process_ownership.py:110`
- `src/report_math.py:31`
- `tests/conftest.py:199`
- `tests/test_admin_routes_auth_disabled.py:16`
- `tests/test_agent_state_dir_confinement.py:799`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_action_planning.py:11`
- `tests/test_deep_research_browser_fallback.py:10`
- `tests/test_deep_research_browser_fallback.py:29`
- `tests/test_deep_research_browser_fallback.py:56`
- `tests/test_deep_research_extraction_controls.py:13`
- `tests/test_deep_research_full_loop_navigation.py:11`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_llm_core_streaming.py:50`
- `tests/test_retired_settings_interfaces.py:31`
- `tests/test_searxng_ca_validation.py:35`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:155`

## `action_tidy_sessions` — function (async), line 557
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_tidy_documents` — function (async), line 577
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_consolidate_memory` — function (async), line 588
- **called from:**
- `tests/test_builtin_memory_consolidation.py:80`
- `tests/test_builtin_memory_consolidation.py:109`
- `tests/test_builtin_memory_consolidation.py:153`
- `tests/test_consolidate_memory_explicit_drops.py:51`

## `_memory_owner` — function, line 604
- **called from:**
- `src/builtin_actions.py:611`
- `src/builtin_actions.py:616`

## `_normalized_memory_text` — function, line 629
- **called from:**
- `src/builtin_actions.py:649`
- `src/builtin_actions.py:650`

## `_memory_rank` — function, line 634
- **called from:**
- `src/builtin_actions.py:678`
- `src/builtin_actions.py:678`

## `_same_memory_fact` — function, line 644
- **called from:**
- `src/builtin_actions.py:671`

## `_dedupe_group` — function, line 660
- **called from:**
- `src/builtin_actions.py:816`

## `_try_ai_tidy_group` — function (async), line 687
- **called from:**
- `src/builtin_actions.py:827`

## `_run_subprocess` — function (async), line 880
- **called from:**
- `src/builtin_actions.py:913`
- `src/builtin_actions.py:914`
- `src/builtin_actions.py:915`
- `src/builtin_actions.py:916`
- `src/builtin_actions.py:928`
- `src/builtin_actions.py:929`
- `src/builtin_actions.py:930`
- `src/builtin_actions.py:938`
- `src/builtin_actions.py:939`
- `tests/test_scheduled_remote_ssh_refusal.py:20`
- `tests/test_scheduled_remote_ssh_refusal.py:38`

## `action_ssh_command` — function (async), line 905
- **called from:**
- `tests/test_runtime_resource_integration.py:90`
- `tests/test_scheduled_remote_ssh_refusal.py:25`

## `action_run_script` — function (async), line 921
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_run_local` — function (async), line 933
- **called from:**
- `tests/test_runtime_resource_integration.py:82`
- `tests/test_runtime_resource_integration.py:86`
- `tests/test_runtime_resource_integration.py:88`

## `action_tidy_research` — function (async), line 942
- **called from:**
- `tests/test_tidy_research_owner_scope.py:74`
- `tests/test_tidy_research_owner_scope.py:93`
- `tests/test_tidy_research_owner_scope.py:104`
- `tests/test_tidy_research_owner_scope.py:128`
- `tests/test_tidy_research_owner_scope.py:140`
- `tests/test_tidy_research_owner_scope.py:153`

## `action_tidy_calendar` — function (async), line 987
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_result_has_work` — function, line 1091
- **called from:**
- `src/builtin_actions.py:1161`
- `src/builtin_actions.py:1184`
- `src/builtin_actions.py:1723`
- `tests/test_builtin_actions_nonstring.py:11`
- `tests/test_builtin_actions_nonstring.py:12`
- `tests/test_builtin_actions_nonstring.py:21`

## `_result_is_config_error` — function, line 1117
- **called from:**
- `src/builtin_actions.py:1159`
- `src/builtin_actions.py:1182`
- `src/builtin_actions.py:1721`

## `_email_task_account_id` — function, line 1128
- **called from:**
- `src/builtin_actions.py:1155`
- `src/builtin_actions.py:1176`
- `src/builtin_actions.py:1224`
- `src/builtin_actions.py:1697`
- `src/builtin_actions.py:2650`

## `action_summarize_emails` — function (async), line 1148
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_draft_email_replies` — function (async), line 1169
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_email_auto_translate` — function (async), line 1192
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_cached` — function, line 1251
- **called from:**
- `src/builtin_actions.py:1390`
- `src/task_scheduler.py:1593`
- `src/task_scheduler.py:1630`
- `tests/test_task_scheduler_cache.py:25`
- `tests/test_task_scheduler_cache.py:31`
- `tests/test_task_scheduler_cache.py:46`
- `tests/test_task_scheduler_cache.py:62`
- `tests/test_task_scheduler_cache.py:68`
- `tests/test_task_scheduler_cache.py:86`

## `_store` — function, line 1264
- **called from:**
- `src/builtin_actions.py:1395`
- `src/builtin_actions.py:1411`
- `tests/test_rag_keyword_fallback_owner.py:38`
- `tests/test_rag_keyword_fallback_owner.py:51`
- `tests/test_rag_vector_rename_owner.py:64`

## `_translate` — function (async), line 1290
- **called from:**
- `src/builtin_actions.py:1393`

## `_classify_event_heuristic` — function, line 1485
- **called from:**
- `src/builtin_actions.py:1571`
- `tests/test_builtin_actions_nonstring.py:16`

## `_memory_context_lines` — function, line 1500
- **called from:**
- `src/builtin_actions.py:1555`
- `tests/test_classify_events_memory_text.py:18`
- `tests/test_classify_events_memory_text.py:28`
- `tests/test_classify_events_memory_text.py:33`

## `action_classify_events` — function (async), line 1518
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:92`

## `action_ping_events` — function (async), line 1686
- **called from:**
- `src/task_scheduler.py:779`

## `action_extract_email_events` — function (async), line 1691
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_learn_sender_signatures` — function (async), line 1754
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:129`
- `tests/test_builtin_actions_owner_scope.py:212`
- `tests/test_imap_uid_commands.py:55`
- `tests/test_imap_uid_commands.py:72`

## `_pull_headers` — function, line 1770
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_bodies` — function, line 1861
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_daily_brief_utc_boundary` — function, line 1960
- **called from:**
- `src/builtin_actions.py:1991`
- `src/builtin_actions.py:1992`
- `tests/test_daily_brief_local_calendar.py:87`
- `tests/test_daily_brief_local_calendar.py:88`
- `tests/test_daily_brief_local_calendar.py:92`
- `tests/test_daily_brief_local_calendar.py:93`

## `_daily_brief_local_start` — function, line 1967
- **called from:**
- `src/builtin_actions.py:2093`
- `tests/test_daily_brief_local_calendar.py:103`

## `action_daily_brief` — function (async), line 1977
- **called from:**
- `tests/test_daily_brief_local_calendar.py:72`
- `tests/test_imap_uid_commands.py:104`

## `action_test_skills` — function (async), line 2121
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `action_audit_skills` — function (async), line 2249
- **called from:**
- `tests/test_skill_audit_utility.py:147`

## `action_ping_notes` — function (async), line 2330
- **called from:**
- `src/task_scheduler.py:759`
- `tests/test_note_ping_delivery_retry.py:48`

## `_parse_due` — function, line 2370
- **called from:**
- `src/builtin_actions.py:2410`

## `_spec_triage_email_urgency` — function (async), line 2500
- **called from:**
- `src/builtin_actions.py:2985`
- `tests/test_jeff_decision.py:44`
- `tests/test_jeff_decision.py:56`
- `tests/test_jeff_decision.py:63`
- `tests/test_jeff_decision.py:71`
- `tests/test_jeff_decision.py:78`
- `tests/test_jeff_decision.py:86`
- `tests/test_jeff_decision.py:99`

## `action_check_email_urgency` — function (async), line 2594
- **called from:**
- `tests/test_builtin_actions_owner_scope.py:257`
- `tests/test_email_urgency_checkpoint.py:537`
- `tests/test_email_urgency_checkpoint.py:584`
- `tests/test_email_urgency_checkpoint.py:650`
- `tests/test_email_urgency_checkpoint.py:706`
- `tests/test_email_urgency_checkpoint.py:722`
- `tests/test_email_urgency_checkpoint.py:800`
- `tests/test_email_urgency_checkpoint.py:814`
- `tests/test_email_urgency_checkpoint.py:859`
- `tests/test_email_urgency_checkpoint.py:864`
- `tests/test_email_urgency_checkpoint.py:895`
- `tests/test_email_urgency_checkpoint.py:904`
- `tests/test_email_urgency_checkpoint.py:922`
- `tests/test_email_urgency_checkpoint.py:934`
- `tests/test_email_urgency_checkpoint.py:1001`
- `tests/test_email_urgency_checkpoint.py:1007`
- `tests/test_email_urgency_checkpoint.py:1075`
- `tests/test_email_urgency_checkpoint.py:1081`
- `tests/test_email_urgency_checkpoint.py:1125`
- `tests/test_email_urgency_checkpoint.py:1129`
- `tests/test_email_urgency_checkpoint.py:1133`
- `tests/test_email_urgency_checkpoint.py:1169`
- `tests/test_email_urgency_checkpoint.py:1175`
- `tests/test_email_urgency_checkpoint.py:1212`
- `tests/test_email_urgency_checkpoint.py:1227`
- `tests/test_email_urgency_checkpoint.py:1264`
- `tests/test_email_urgency_checkpoint.py:1271`
- `tests/test_email_urgency_checkpoint.py:1312`
- `tests/test_email_urgency_checkpoint.py:1314`
- `tests/test_email_urgency_checkpoint.py:1330`
- `tests/test_email_urgency_checkpoint.py:1357`
- `tests/test_email_urgency_checkpoint.py:1359`

## `_enumerate_enabled_accounts` — function, line 2656
- **called from:**
- `src/builtin_actions.py:2676`
- `src/builtin_actions.py:2716`

## `_register_accounts` — function (async), line 2686
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_retire_accounts` — function (async), line 2754
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_scan_one` — function, line 2802
- **called from:**
- `src/tools/cookbook.py:2046`
- `src/tools/cookbook.py:2059`
- `src/tools/cookbook.py:2067`
- `src/tools/cookbook.py:2075`

## `_urgency_reminder_payload` — function, line 3226
- **called from:**
- `src/builtin_actions.py:3264`

## `_dispatch_urgency_reminder` — function (async), line 3260
- **called from:**
- `src/builtin_actions.py:3299`

## `_dispatch_and_checkpoint` — function (async), line 3272
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fmt_tag_write` — function, line 3364
- **called from:**
- `src/builtin_actions.py:3398`

## `_fmt_one` — function, line 3379
- **called from:**
- `src/builtin_actions.py:3410`

## `action_cookbook_serve` — function (async), line 3434
- **called from:**
- `tests/test_builtin_actions_cookbook_serve_state.py:29`
- `tests/test_wave3_local_control.py:134`
- `tests/test_wave3_local_control.py:138`

## `_short` — function, line 3491
- **called from:**
- `src/builtin_actions.py:3515`
