# `src/agent_runs.py` — definitions & call sites

15 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_Run` — class, line 26
- **called from:**
- `src/agent_runs.py:199`

## `_Run.__init__` — method, line 29
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

## `_publish` — function, line 54
- **called from:**
- `src/agent_runs.py:141`
- `src/agent_runs.py:165`
- `src/agent_runs.py:170`

## `_wake_run_subscribers` — function, line 65
- **called from:**
- `src/agent_runs.py:131`
- `src/agent_runs.py:194`

## `_schedule_evict` — function, line 74
- **called from:**
- `src/agent_runs.py:177`
- `src/agent_runs.py:272`

## `_evict` — function (async), line 86
- **called from:**
- `src/agent_runs.py:95`

## `is_active` — function, line 98
- **called from:**
- `routes/chat_routes.py:3115`
- `routes/session_routes.py:132`
- `src/agent_jobs.py:295`
- `src/bg_monitor.py:115`

## `get_status` — function, line 103
- **called from:**
- `routes/chat_routes.py:1943`
- `routes/research/research_routes.py:284`
- `routes/research/research_routes.py:589`
- `services/research/service.py:163`
- `tests/test_research_handler_path_confinement.py:54`
- `tests/test_research_status_avg_duration.py:22`
- `tests/test_research_status_avg_duration.py:34`
- `tests/test_research_status_avg_duration.py:35`
- `tests/test_research_status_avg_duration.py:36`

## `get_run_id` — function, line 108
- **called from:**
- `tests/test_compare_stop_disconnect_poll.py:182`
- `tests/test_compare_stop_disconnect_poll.py:184`
- `tests/test_compare_stop_disconnect_poll.py:188`
- `tests/test_compare_stop_disconnect_poll.py:211`

## `get_active_run` — function, line 114
- **called from:**
- `routes/chat_routes.py:3082`

## `_drain` — function (async), line 120
- **called from:**
- `src/agent_runs.py:201`
- `src/llm_core.py:310`
- `src/llm_core.py:313`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_model_routes.py:1169`
- `tests/test_model_routes.py:1206`

## `_wake_subscribers` — function, line 126
- **called from:**
- `src/agent_runs.py:156`
- `src/agent_runs.py:173`

## `start` — function, line 180
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

## `subscribe` — function (async), line 205
- **called from:**
- `routes/chat_routes.py:3070`
- `routes/chat_routes.py:3086`
- `tests/test_compare_stop_disconnect_poll.py:87`
- `tests/test_compare_stop_disconnect_poll.py:109`
- `tests/test_compare_stop_disconnect_poll.py:139`
- `tests/test_compare_stop_disconnect_poll.py:204`
- `tests/test_compare_stop_disconnect_poll.py:315`
- `tests/test_compare_stop_disconnect_poll.py:328`
- `tests/test_pr6020_browser_review_regressions.py:262`

## `stop` — function, line 275
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
