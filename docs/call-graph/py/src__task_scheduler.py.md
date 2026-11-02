# `src/task_scheduler.py` — definitions & call sites

50 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow` — function, line 22
- **called from:**
- `src/cleanup_service.py:51`
- `src/cleanup_service.py:66`
- `src/cleanup_service.py:92`
- `src/cleanup_service.py:171`
- `src/cleanup_service.py:172`
- `src/task_scheduler.py:142`
- `src/task_scheduler.py:147`
- `src/task_scheduler.py:403`
- `src/task_scheduler.py:424`
- `src/task_scheduler.py:470`
- `src/task_scheduler.py:491`
- `src/task_scheduler.py:693`
- `src/task_scheduler.py:705`
- `src/task_scheduler.py:752`
- `src/task_scheduler.py:807`
- `src/task_scheduler.py:809`
- `src/task_scheduler.py:835`
- `src/task_scheduler.py:850`
- `src/task_scheduler.py:853`
- `src/task_scheduler.py:876`
- `src/task_scheduler.py:885`
- `src/task_scheduler.py:948`
- `src/task_scheduler.py:971`
- `src/task_scheduler.py:972`
- `src/task_scheduler.py:974`
- `src/task_scheduler.py:979`
- `src/task_scheduler.py:996`
- `src/task_scheduler.py:997`
- `src/task_scheduler.py:1002`
- `src/task_scheduler.py:1018`
- `src/task_scheduler.py:1021`
- `src/task_scheduler.py:1030`
- `src/task_scheduler.py:1118`
- `src/task_scheduler.py:1123`
- `src/task_scheduler.py:1128`
- `src/task_scheduler.py:1153`
- `src/task_scheduler.py:1158`
- `src/task_scheduler.py:1159`
- `src/task_scheduler.py:1342`
- `src/task_scheduler.py:1345`
- `src/task_scheduler.py:1349`
- `src/task_scheduler.py:1550`
- `src/task_scheduler.py:1551`
- `src/task_scheduler.py:1728`
- `src/task_scheduler.py:1729`
- `src/task_scheduler.py:1778`
- `src/task_scheduler.py:1786`
- `src/task_scheduler.py:2096`
- `src/task_scheduler.py:2097`
- `src/task_scheduler.py:2421`
- `src/task_scheduler.py:2456`
- `src/task_scheduler.py:2473`
- `src/task_scheduler.py:2612`
- `src/task_scheduler.py:2613`
- `src/webhook_manager.py:418`
- `src/webhook_manager.py:432`
- `src/webhook_manager.py:441`
- `tests/test_cleanup_service_utcnow.py:13`
- `tests/test_cleanup_service_utcnow.py:23`
- `tests/test_cleanup_service_utcnow.py:25`
- … +1 more (grep the name in repo)

## `compose_task_relevant_tools` — function, line 41
- **called from:**
- `tests/test_task_shell_tools.py:30`
- `tests/test_task_shell_tools.py:37`
- `tests/test_task_shell_tools.py:50`
- `tests/test_task_shell_tools.py:65`
- `tests/test_task_shell_tools.py:80`

## `_cached` — function (async), line 65
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

## `compute_next_run` — function, line 113
- **called from:**
- `routes/assistant_routes.py:226`
- `routes/assistant_routes.py:248`
- `routes/task/task_routes.py:411`
- `routes/task/task_routes.py:499`
- `routes/task/task_routes.py:744`
- `routes/task/task_routes.py:807`
- `routes/task/task_routes.py:847`
- `src/task_scheduler.py:976`
- `src/task_scheduler.py:999`
- `src/task_scheduler.py:1027`
- `src/task_scheduler.py:1125`
- `src/task_scheduler.py:2419`
- `src/task_scheduler.py:2453`
- `src/task_scheduler.py:2471`
- `src/tools/system.py:345`
- `src/tools/system.py:420`
- `src/tools/system.py:456`
- `tests/test_compute_next_run_monthly_clamp.py:27`
- `tests/test_compute_next_run_monthly_clamp.py:32`
- `tests/test_compute_next_run_monthly_clamp.py:39`
- `tests/test_compute_next_run_monthly_clamp.py:46`
- `tests/test_compute_next_run_monthly_clamp.py:53`
- `tests/test_scheduler_scheduled_time_validation.py:21`
- `tests/test_scheduler_scheduled_time_validation.py:26`

## `_to_utc_naive` — function, line 149
- **called from:**
- `src/caldav_sync.py:386`
- `src/caldav_sync.py:390`
- `src/task_scheduler.py:162`
- `src/task_scheduler.py:168`
- `src/task_scheduler.py:192`
- `src/task_scheduler.py:201`
- `src/task_scheduler.py:228`

## `_resolve_task_timezone` — function, line 233
- **called from:**
- `src/task_scheduler.py:981`
- `src/task_scheduler.py:1004`
- `src/task_scheduler.py:1032`
- `src/task_scheduler.py:1130`
- `src/task_scheduler.py:1337`
- `src/task_scheduler.py:1596`
- `src/task_scheduler.py:2422`
- `src/task_scheduler.py:2457`

## `_digest_windows` — function, line 272
- **called from:**
- `src/task_scheduler.py:1360`
- `tests/test_digest_windows.py:9`
- `tests/test_digest_windows.py:21`

## `_checkin_calendar_events` — function, line 286
- **called from:**
- `src/task_scheduler.py:1364`
- `tests/test_checkin_digest_owner_scope.py:49`
- `tests/test_checkin_digest_owner_scope.py:51`
- `tests/test_checkin_digest_owner_scope.py:67`

## `_normalize_chat_endpoint` — function, line 309
- **called from:**
- `src/task_scheduler.py:1533`
- `src/task_scheduler.py:1716`
- `src/task_scheduler.py:2041`
- `tests/test_task_endpoint_normalization.py:16`
- `tests/test_task_endpoint_normalization.py:23`
- `tests/test_task_endpoint_normalization.py:25`
- `tests/test_task_endpoint_normalization.py:25`
- `tests/test_task_endpoint_normalization.py:30`
- `tests/test_task_endpoint_normalization.py:31`
- `tests/test_task_endpoint_normalization.py:35`
- `tests/test_task_endpoint_normalization.py:36`
- `tests/test_task_endpoint_normalization.py:41`

## `TaskScheduler` — class, line 345
- **called from:**
- `app.py:784`
- `tests/test_email_urgency_checkpoint.py:488`
- `tests/test_scheduler_prompt_cache_time.py:60`
- `tests/test_scheduler_prompt_cache_time.py:105`
- `tests/test_scheduler_prompt_cache_time.py:139`
- `tests/test_task_shell_tools.py:120`

## `TaskScheduler.__init__` — method, line 346
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

## `TaskScheduler._set_run_progress` — method, line 366
- **called from:**
- `src/task_scheduler.py:1254`

## `TaskScheduler._mark_run_aborted` — method, line 383
- **called from:**
- `src/task_scheduler.py:783`
- `src/task_scheduler.py:2279`
- `src/task_scheduler.py:2298`

## `TaskScheduler.add_notification` — method, line 412
- **called from:**
- `routes/note/note_routes.py:520`
- `src/task_scheduler.py:1051`
- `src/task_scheduler.py:1059`
- `src/task_scheduler.py:1110`
- `tests/test_auth_regressions.py:313`
- `tests/test_auth_regressions.py:314`
- `tests/test_auth_regressions.py:315`
- `tests/test_auth_regressions.py:316`

## `TaskScheduler.pop_notifications` — method, line 430
- **called from:**
- `routes/task/task_routes.py:569`
- `tests/test_auth_regressions.py:317`
- `tests/test_auth_regressions.py:325`
- `tests/test_email_urgency_checkpoint.py:505`

## `TaskScheduler.start` — method (async), line 455
- **called from:**
- `app.py:1218`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `routes/chat_helpers.py:1149`
- `routes/chat_helpers.py:1150`
- `routes/chat_helpers.py:1151`
- `routes/chat_routes.py:3068`
- `routes/cookbook_routes.py:3678`
- `routes/email_helpers.py:273`
- `routes/email_routes.py:1003`
- `routes/model_routes.py:1537`
- `routes/skills_routes.py:849`
- `scripts/add_hwfit_models.py:64`
- `services/hwfit/hf_discovery.py:115`
- `services/search/content.py:720`
- `services/search/content.py:720`
- `src/agent_tools/document_tools.py:205`
- `src/agent_tools/filesystem_tools.py:864`
- `src/agent_tools/filesystem_tools.py:865`
- `src/agent_tools/filesystem_tools.py:954`
- `src/llm_core.py:346`
- `src/pdf_form_doc.py:86`
- `src/text_helpers.py:110`
- `src/text_helpers.py:111`
- `src/tool_parsing.py:595`
- `src/tool_parsing.py:762`
- `src/tool_parsing.py:785`
- `src/tool_parsing.py:1211`
- `src/tool_parsing.py:1211`
- `src/tool_parsing.py:1245`
- `src/tool_parsing.py:1272`
- `src/tool_parsing.py:1344`
- `src/visual_report.py:1706`
- `src/visual_report.py:1709`
- `tests/markdown_browser_check.py:32`
- `tests/markdown_screenshot.py:57`
- `tests/test_agent_thread_dot_alignment_css.py:35`
- `tests/test_app_config_shared_fetch_js.py:210`
- `tests/test_app_config_shared_fetch_js.py:210`
- `tests/test_app_config_shared_fetch_js.py:212`
- `tests/test_atomic_io.py:114`
- `tests/test_atomic_io.py:115`
- `tests/test_auth_config_lock_concurrency.py:185`
- `tests/test_auth_config_lock_concurrency.py:234`
- `tests/test_auth_config_lock_concurrency.py:235`
- `tests/test_caldav_redirect_hardening.py:65`
- `tests/test_caldav_redirect_hardening.py:66`
- `tests/test_calendar_default_transaction.py:287`
- `tests/test_calendar_default_transaction.py:288`
- `tests/test_compare_stop_disconnect_poll.py:105`
- `tests/test_compare_stop_disconnect_poll.py:135`
- `tests/test_compare_stop_disconnect_poll.py:167`
- `tests/test_compare_stop_disconnect_poll.py:180`
- `tests/test_compare_stop_disconnect_poll.py:186`
- `tests/test_compare_stop_disconnect_poll.py:200`
- `tests/test_compare_stop_disconnect_poll.py:206`
- `tests/test_compare_stop_disconnect_poll.py:227`
- `tests/test_compare_stop_disconnect_poll.py:229`
- `tests/test_compare_stop_disconnect_poll.py:262`
- … +98 more (grep the name in repo)

## `TaskScheduler.stop` — method (async), line 588
- **called from:**
- `app.py:1290`
- `launcher.py:96`
- `routes/chat_routes.py:3099`
- `tests/test_compare_stop_disconnect_poll.py:146`
- `tests/test_compare_stop_disconnect_poll.py:232`
- `tests/test_compare_stop_disconnect_poll.py:233`
- `tests/test_compare_stop_disconnect_poll.py:235`
- `static/js/admin.js:673`
- `static/js/chat.js:4889`
- `static/js/chat.js:4980`
- `static/js/chatRenderer.js:145`
- `static/js/compare/stream.js:250`
- `static/js/compare/stream.js:287`
- `static/js/cookbookRunning.js:2895`
- `static/js/documentLibrary.js:3280`
- `static/js/documentLibrary.js:3433`
- `static/js/emailLibrary.js:8414`
- `static/js/fileHandler.js:347`
- `static/js/galleryEditor.js:3664`
- `static/js/keyboard-shortcuts.js:171`
- `static/js/models.js:220`
- `static/js/settings.js:2652`
- `static/js/spinner.js:260`
- `static/js/spinner.js:268`
- `static/js/spinner.js:274`
- `static/js/spinner.js:288`
- `static/js/spinner.js:367`
- `static/js/spinner.js:408`
- `static/js/spinner.js:425`
- `static/js/spinner.js:437`
- `static/js/tasks.js:2865`
- `static/js/tts-ai.js:179`
- `static/js/tts-ai.js:224`
- `static/js/tts-ai.js:503`
- `static/js/tts-ai.js:517`
- `static/js/voiceRecorder.js:102`
- `static/js/voiceRecorder.js:178`
- `static/js/voiceRecorder.js:251`

## `TaskScheduler._note_pings_loop` — method (async), line 604
- **called from:**
- `src/task_scheduler.py:559`

## `TaskScheduler._event_pings_loop` — method (async), line 624
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._known_task_owners` — method, line 644
- **called from:**
- `src/task_scheduler.py:614`
- `src/task_scheduler.py:634`

## `TaskScheduler._loop` — method (async), line 673
- **called from:**
- `src/agent_jobs.py:363`
- `src/bg_monitor.py:166`
- `src/task_scheduler.py:550`

## `TaskScheduler._check_due_tasks` — method (async), line 701
- **called from:**
- `src/task_scheduler.py:677`
- `tests/test_scheduler_restart_doublefire.py:110`
- `tests/test_scheduler_restart_doublefire.py:111`

## `TaskScheduler._execute_task` — method (async), line 737
- **called from:**
- `src/task_scheduler.py:733`
- `src/task_scheduler.py:2148`
- `src/task_scheduler.py:2258`
- `src/task_scheduler.py:2264`
- `tests/test_task_scheduler_cancel.py:69`

## `TaskScheduler._defer_immediately_due_task` — method, line 794
- **called from:**
- `src/task_scheduler.py:784`

## `TaskScheduler._execute_task_locked` — method (async), line 816
- **called from:**
- `src/task_scheduler.py:765`
- `src/task_scheduler.py:774`
- `tests/test_task_cookbook_admin_gate.py:277`

## `TaskScheduler._cancel_if_foreground_active` — method (async), line 905
- **called from:**
- `src/task_scheduler.py:920`

## `TaskScheduler._task_needs_model_slot` — method, line 1210
- **called from:**
- `src/task_scheduler.py:764`

## `TaskScheduler._log_to_assistant` — method, line 1227
- **called from:**
- `src/task_scheduler.py:1072`

## `TaskScheduler._execute_action` — method (async), line 1242
- **called from:**
- `src/task_scheduler.py:923`

## `TaskScheduler._progress` — method, line 1253
- **called from:**
- `src/deep_research.py:792`

## `TaskScheduler._format_email_output` — method, line 1299
- decorator: `staticmethod`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._execute_checkin` — method (async), line 1331
- **called from:**
- `src/task_scheduler.py:1569`

## `TaskScheduler._fetch_miniflux` — method (async), line 1419
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._call_mcp` — method (async), line 1473
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler._execute_llm_task` — method (async), line 1510
- **called from:**
- `src/task_scheduler.py:934`
- `tests/test_scheduler_prompt_cache_time.py:60`
- `tests/test_scheduler_prompt_cache_time.py:141`
- `tests/test_task_shell_tools.py:137`

## `TaskScheduler._deliver_task_result` — method (async), line 1669
- **called from:**
- `src/task_scheduler.py:941`
- `tests/test_task_scheduler_session_delivery.py:69`
- `tests/test_task_scheduler_session_delivery.py:101`

## `TaskScheduler._is_email_output_target` — method, line 1794
- decorator: `staticmethod`
- **called from:**
- `src/task_scheduler.py:1690`

## `TaskScheduler._deliver_via_email` — method (async), line 1802
- **called from:**
- `src/task_scheduler.py:1691`

## `TaskScheduler._run_agent_loop` — method (async), line 1849
- **called from:**
- `src/task_scheduler.py:1503`
- `src/task_scheduler.py:1636`
- `tests/test_scheduler_prompt_cache_time.py:105`

## `TaskScheduler._execute_research_task` — method (async), line 2005
- **called from:**
- `src/task_scheduler.py:929`

## `TaskScheduler._run_chained` — method (async), line 2140
- **called from:**
- `src/task_scheduler.py:1085`

## `TaskScheduler._has_chain_cycle` — method, line 2150
- **called from:**
- `src/task_scheduler.py:1083`
- `tests/test_task_chain_owner_scope.py:125`

## `TaskScheduler._resolve_defaults` — method, line 2167
- **called from:**
- `src/task_scheduler.py:1530`
- `src/task_scheduler.py:1710`
- `src/task_scheduler.py:2038`
- `src/task_scheduler.py:2543`

## `TaskScheduler._deliver_via_mcp` — method (async), line 2182
- **called from:**
- `src/task_scheduler.py:1687`

## `TaskScheduler.run_task_now` — method (async), line 2255
- **called from:**
- `routes/assistant_routes.py:289`
- `routes/task/task_routes.py:870`
- `routes/task/task_routes.py:1067`
- `src/event_bus.py:109`
- `src/tools/system.py:475`

## `TaskScheduler.stop_task` — method (async), line 2267
- **called from:**
- `routes/task/task_routes.py:887`
- `tests/test_task_scheduler_cancel.py:84`

## `TaskScheduler.stop_background_tasks_for_foreground` — method (async), line 2282
- **called from:**
- `app.py:217`

## `TaskScheduler.ensure_defaults` — method (async), line 2304
- **called from:**
- `app.py:1181`
- `routes/task/task_routes.py:346`
- `routes/task/task_routes.py:360`
- `routes/task/task_routes.py:392`

## `TaskScheduler._score` — method, line 2384
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TaskScheduler.ensure_assistant_defaults` — method (async), line 2517
- **called from:**
- `routes/assistant_routes.py:112`
- `src/task_scheduler.py:2513`
