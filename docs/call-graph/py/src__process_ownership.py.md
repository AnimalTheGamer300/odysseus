# `src/process_ownership.py` — definitions & call sites

17 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `InspectionUnavailable` — class, line 100
- **called from:**
- `src/process_ownership.py:143`
- `src/process_ownership.py:150`
- `src/process_ownership.py:154`
- `src/process_ownership.py:156`
- `src/process_ownership.py:172`
- `src/process_ownership.py:179`
- `src/process_ownership.py:207`
- `src/process_ownership.py:238`
- `src/process_ownership.py:305`
- `src/process_ownership.py:343`
- `src/process_ownership.py:345`
- `src/process_ownership.py:378`
- `tests/test_agent_tmux_retirement.py:159`
- `tests/test_cookbook_stop_without_procfs.py:187`
- `tests/test_cookbook_stop_without_procfs.py:321`
- `tests/test_process_lifecycle.py:203`
- `tests/test_process_lifecycle.py:335`
- `tests/test_process_lifecycle.py:336`
- `tests/test_process_ownership.py:137`

## `InspectionUnavailable.__init__` — method, line 109
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

## `inspection_mechanism` — function, line 114
- **called from:**
- `src/containment.py:1389`
- `src/process_ownership.py:131`
- `src/process_ownership.py:231`
- `src/process_ownership.py:370`
- `src/process_reaper.py:115`
- `src/process_reaper.py:297`
- `tests/test_orphan_reaping.py:440`
- `tests/test_process_ownership.py:186`
- `tests/test_process_ownership.py:195`
- `tests/test_process_ownership.py:204`

## `inspection_available` — function, line 130
- **called from:**
- `tests/test_process_ownership.py:196`
- `tests/test_process_ownership.py:205`

## `_procfs_token` — function, line 135
- **called from:**
- `src/process_ownership.py:235`

## `_ps_token` — function, line 162
- **called from:**
- `src/process_ownership.py:237`

## `_win32_token` — function, line 185
- **called from:**
- `src/process_ownership.py:233`

## `start_token` — function, line 214
- **called from:**
- `src/process_lifecycle.py:192`
- `src/process_lifecycle.py:205`
- `src/process_lifecycle.py:239`
- `src/process_ownership.py:257`
- `src/process_ownership.py:281`
- `src/process_reaper.py:214`
- `tests/test_containment_enforcement.py:129`
- `tests/test_containment_enforcement.py:159`
- `tests/test_process_lifecycle.py:264`
- `tests/test_process_ownership.py:49`
- `tests/test_process_ownership.py:58`
- `tests/test_process_ownership.py:65`
- `tests/test_process_ownership.py:111`
- `tests/test_process_ownership.py:117`
- `tests/test_process_ownership.py:130`
- `tests/test_process_ownership.py:228`
- `tests/test_process_ownership.py:229`
- `tests/test_process_ownership.py:231`

## `verify` — function, line 241
- **called from:**
- `core/auth.py:563`
- `core/auth.py:599`
- `src/agent_runtime/process_resources.py:482`
- `src/bg_jobs.py:253`
- `src/bg_jobs.py:324`
- `src/bg_jobs.py:465`
- `src/containment.py:1427`
- `src/containment.py:1653`
- `src/containment.py:1672`
- `src/process_lifecycle.py:145`
- `src/process_lifecycle.py:255`
- `src/process_lifecycle.py:373`
- `src/process_ownership.py:270`
- `src/process_reaper.py:234`
- `src/process_reaper.py:235`
- `src/process_reaper.py:243`
- `src/process_reaper.py:266`
- `tests/test_ca_trust.py:152`
- `tests/test_ca_trust.py:154`
- `tests/test_ca_trust.py:157`
- `tests/test_orphan_reaping.py:414`
- `tests/test_process_ownership.py:52`
- `tests/test_process_ownership.py:60`
- `tests/test_process_ownership.py:69`
- `tests/test_process_ownership.py:74`
- `tests/test_process_ownership.py:86`
- `tests/test_process_ownership.py:87`
- `tests/test_process_ownership.py:97`
- `tests/test_process_ownership.py:98`
- `tests/test_process_ownership.py:107`
- `tests/test_process_ownership.py:111`
- `tests/test_process_ownership.py:122`
- `tests/test_process_ownership.py:141`
- `tests/test_process_ownership.py:155`

## `verify_record` — function, line 266
- **called from:**
- `src/process_reaper.py:89`

## `capture` — function, line 273
- **called from:**
- `routes/shell_routes.py:739`
- `scripts/css_snapshot.py:258`
- `scripts/run_sft_environment_expansion.py:695`
- `scripts/verify_notes_browser_runtime.py:74`
- `src/agent_tools/web_tools.py:115`
- `src/agent_tools/web_tools_prewave3.py:119`
- `src/bg_jobs.py:162`
- `src/containment.py:475`
- `src/containment.py:1096`
- `src/containment.py:1127`
- `src/containment.py:1254`
- `src/process_lifecycle.py:122`
- `tests/test_ai_interaction_owner_scope.py:52`
- `tests/test_ai_interaction_owner_scope.py:57`
- `tests/test_css_computed_style_snapshot.py:94`
- `tests/test_css_computed_style_snapshot.py:103`
- `tests/test_css_computed_style_snapshot.py:152`
- `tests/test_css_computed_style_snapshot.py:153`
- `tests/test_css_computed_style_snapshot.py:166`
- `tests/test_css_computed_style_snapshot.py:183`
- `tests/test_css_computed_style_snapshot.py:186`
- `tests/test_notes_native_cleanup.py:24`
- `tests/test_notes_native_cleanup.py:28`
- `tests/test_process_lifecycle.py:185`
- `tests/test_process_lifecycle.py:242`
- `tests/test_process_ownership.py:103`
- `tests/test_process_ownership.py:152`
- `static/js/signature.js:4`
- `static/js/signature.js:379`
- `static/js/signature.js:517`

## `ProcessInfo` — class, line 289
- **called from:**
- `src/process_ownership.py:327`
- `src/process_ownership.py:354`
- `tests/test_agent_tmux_retirement.py:48`
- `tests/test_agent_tmux_retirement.py:49`
- `tests/test_agent_tmux_retirement.py:86`
- `tests/test_agent_tmux_retirement.py:143`
- `tests/test_agent_tmux_retirement.py:145`
- `tests/test_agent_tmux_retirement.py:148`
- `tests/test_cookbook_stop_without_procfs.py:120`
- `tests/test_cookbook_stop_without_procfs.py:357`
- `tests/test_process_ownership.py:264`
- `tests/test_process_ownership.py:265`
- `tests/test_process_ownership.py:266`
- `tests/test_process_ownership.py:267`
- `tests/test_process_ownership.py:281`
- `tests/test_process_ownership.py:282`

## `_procfs_process_table` — function, line 300
- **called from:**
- `src/process_ownership.py:372`
- `tests/test_process_ownership.py:175`

## `_ps_process_table` — function, line 331
- **called from:**
- `src/process_ownership.py:374`

## `process_table` — function, line 358
- **called from:**
- `src/process_lifecycle.py:233`
- `src/process_lifecycle.py:245`
- `src/process_ownership.py:383`
- `src/process_ownership.py:399`
- `src/process_reaper.py:216`
- `src/tools/cookbook.py:1168`
- `tests/test_process_ownership.py:162`
- `tests/test_process_ownership.py:305`
- `tests/test_process_ownership.py:324`

## `command_lines` — function, line 381
- **called from:**
- `tests/test_process_ownership.py:331`

## `descendants` — function, line 386
- **called from:**
- `src/process_lifecycle.py:234`
- `src/process_lifecycle.py:246`
- `tests/test_native_document_stream.py:14`
- `tests/test_native_document_stream.py:15`
- `tests/test_process_ownership.py:242`
- `tests/test_process_ownership.py:253`
- `tests/test_process_ownership.py:275`
- `tests/test_process_ownership.py:285`
- `tests/test_process_ownership.py:309`
