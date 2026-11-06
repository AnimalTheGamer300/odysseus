# `src/agent_runtime/process_resources.py` — definitions & call sites

33 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `digest` — function, line 33
- **called from:**
- `src/agent_runtime/journal.py:41`
- `src/agent_runtime/journal.py:56`
- `src/agent_runtime/process_resources.py:259`
- `src/agent_runtime/process_resources.py:275`
- `src/agent_runtime/process_resources.py:298`
- `src/agent_runtime/process_resources.py:299`
- `src/browser_identity.py:62`
- `src/browser_identity.py:74`
- `src/browser_identity.py:244`
- `src/browser_identity.py:310`
- `src/browser_identity.py:431`

## `_thread` — function, line 37
- **called from:**
- `src/agent_runtime/process_resources.py:290`
- `src/agent_runtime/process_resources.py:298`
- `src/agent_runtime/process_resources.py:300`
- `src/agent_runtime/process_resources.py:318`
- `src/agent_runtime/process_resources.py:368`

## `launch_path` — function, line 41
- **called from:**
- `src/agent_runtime/process_resources.py:130`
- `src/agent_runtime/process_resources.py:415`
- `src/agent_runtime/process_resources.py:436`
- `src/agent_runtime/process_resources.py:482`
- `src/agent_runtime/process_resources.py:501`
- `src/bg_jobs.py:181`
- `tests/test_background_resource_identity.py:160`
- `tests/test_background_resource_identity.py:276`
- `tests/test_runtime_resource_integration.py:388`
- `tests/test_runtime_resource_integration.py:414`
- `tests/test_runtime_resource_integration.py:441`
- `tests/test_runtime_resource_integration.py:501`
- `tests/test_wave3_background_followup.py:71`
- `tests/test_wave3_background_followup.py:80`
- `tests/test_wave3_launch_cost_lifecycle.py:59`
- `tests/test_wave3_launch_cost_lifecycle.py:86`
- `tests/test_wave3_launch_cost_lifecycle.py:100`
- `tests/test_wave3_launch_cost_lifecycle.py:112`
- `tests/test_wave3_launch_cost_lifecycle.py:131`
- `tests/test_wave3_launch_cost_lifecycle.py:133`
- `tests/test_wave3_launch_cost_lifecycle.py:146`
- `tests/test_wave3_launch_cost_lifecycle.py:148`
- `tests/test_wave3_launch_cost_lifecycle.py:149`
- `tests/test_wave3_launch_cost_lifecycle.py:151`
- `tests/test_wave3_launch_cost_lifecycle.py:169`
- `tests/test_wave3_launch_cost_lifecycle.py:177`
- `tests/test_wave3_launch_cost_lifecycle.py:195`
- `tests/test_wave3_launch_cost_lifecycle.py:206`
- `tests/test_wave3_launch_cost_lifecycle.py:217`

## `seal_launch_scopes` — function, line 47
- **called from:**
- `src/agent_runtime/authority.py:178`

## `seal_launch_scope` — function, line 54
- **called from:**
- `src/agent_runtime/process_resources.py:48`
- `src/tool_approvals.py:438`
- `tests/process_resource_helpers.py:80`
- `tests/runtime_evidence_helpers.py:36`

## `validate_launch_spec` — function, line 67
- **called from:**
- `src/agent_tools/subprocess_tools.py:535`
- `src/bg_jobs.py:111`
- `src/containment_worker.py:55`

## `job_from_record` — function, line 76
- **called from:**
- `src/agent_runtime/process_resources.py:125`
- `src/agent_runtime/process_resources.py:173`
- `src/bg_jobs.py:226`
- `src/bg_jobs.py:400`
- `src/bg_monitor.py:147`
- `src/bg_monitor.py:175`
- `src/bg_monitor.py:218`
- `tests/process_resource_helpers.py:31`
- `tests/test_background_resource_identity.py:107`

## `validate_job` — function, line 98
- **called from:**
- `src/agent_runtime/authority.py:713`
- `src/agent_runtime/process_resources.py:175`
- `src/agent_runtime/process_resources.py:270`
- `src/agent_runtime/process_resources.py:535`
- `src/bg_jobs.py:380`
- `src/bg_jobs.py:394`
- `src/bg_jobs.py:396`
- `src/bg_jobs.py:420`
- `src/bg_monitor.py:148`
- `src/bg_monitor.py:176`
- `src/bg_monitor.py:190`
- `tests/test_background_resource_identity.py:56`
- `tests/test_background_resource_identity.py:65`
- `tests/test_wave3_background_followup.py:48`
- `tests/test_wave3_launch_cost_lifecycle.py:138`

## `validate_job_receipt` — function, line 107
- **called from:**
- `src/agent_runtime/process_resources.py:149`
- `src/containment_worker.py:59`

## `_validate_job` — function, line 120
- **called from:**
- `src/agent_runtime/process_resources.py:100`

## `seal_jobs` — function, line 166
- **called from:**
- `src/agent_runtime/authority.py:180`

## `intersect_observed` — function, line 182
- **called from:**
- `src/agent_runtime/authority.py:250`
- `src/agent_runtime/authority.py:251`
- `tests/test_stale_process_intersection.py:45`
- `tests/test_stale_process_intersection.py:56`
- `tests/test_stale_process_intersection.py:65`
- `tests/test_stale_process_intersection.py:75`
- `tests/test_stale_process_intersection.py:84`
- `tests/test_stale_process_intersection.py:93`
- `tests/test_stale_process_intersection.py:105`
- `tests/test_stale_process_intersection.py:117`
- `tests/test_stale_process_intersection.py:124`

## `intersect_launch_scopes` — function, line 205
- **called from:**
- `src/agent_runtime/authority.py:249`

## `_LaunchUse` — class, line 224
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_LaunchUse.__init__` — method, line 226
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

## `_LaunchUse.claim` — method, line 230
- **called from:**
- `src/agent_runtime/effect_adapters.py:263`
- `src/agent_runtime/journal.py:89`
- `src/agent_runtime/process_resources.py:422`
- `src/tool_execution.py:1946`
- `tests/test_effect_journal_persistence.py:26`
- `tests/test_effect_journal_persistence.py:39`
- `tests/test_effect_journal_persistence.py:53`
- `tests/test_effect_journal_persistence.py:59`
- `tests/test_effect_journal_persistence.py:72`
- `tests/test_effect_journal_persistence.py:77`
- `tests/test_effect_journal_persistence.py:95`
- `tests/test_effect_journal_persistence.py:105`
- `tests/test_effect_journal_persistence.py:118`
- `tests/test_effect_journal_persistence.py:130`
- `tests/test_effect_journal_persistence.py:135`
- `tests/test_effect_journal_persistence.py:163`
- `tests/test_effect_journal_persistence.py:182`
- `tests/test_effect_journal_persistence.py:186`
- `tests/test_effect_journal_persistence.py:193`
- `tests/test_effect_journal_persistence.py:205`
- `tests/test_effect_journal_persistence.py:209`
- `tests/test_effect_journal_persistence.py:220`
- `tests/test_effect_journal_persistence.py:221`
- `tests/test_effect_journal_persistence.py:222`
- `tests/test_effect_journal_persistence.py:237`
- `tests/test_effect_journal_persistence.py:281`
- `tests/test_effect_journal_persistence.py:296`
- `tests/test_effect_journal_persistence.py:353`
- `tests/test_effect_journal_persistence.py:354`
- `tests/test_effect_verification_adapters.py:365`
- `tests/test_effects_foundation.py:189`
- `tests/test_effects_foundation.py:205`
- `tests/test_effects_foundation.py:214`
- `tests/test_effects_foundation.py:227`
- `tests/test_effects_foundation.py:236`
- `tests/test_effects_foundation.py:248`
- `tests/test_effects_foundation.py:256`
- `tests/test_effects_foundation.py:266`
- `tests/test_effects_foundation.py:269`
- `tests/test_effects_foundation.py:280`
- `tests/test_effects_foundation.py:282`
- `tests/test_effects_foundation.py:291`
- `tests/test_effects_foundation.py:294`
- `tests/test_effects_foundation.py:302`
- `tests/test_effects_foundation.py:305`
- `tests/test_effects_foundation.py:314`
- `tests/test_effects_foundation.py:317`
- `tests/test_effects_foundation.py:325`
- `tests/test_effects_foundation.py:339`
- `tests/test_effects_foundation.py:347`
- `tests/test_effects_foundation.py:356`
- `tests/test_effects_foundation.py:367`
- `tests/test_effects_foundation.py:378`
- `tests/test_effects_foundation.py:389`
- `tests/test_effects_foundation.py:400`
- `tests/test_effects_foundation.py:409`
- `tests/test_effects_foundation.py:420`
- `tests/test_effects_foundation.py:434`
- `tests/test_effects_foundation.py:448`
- `tests/test_tool_approvals.py:58`
- … +3 more (grep the name in repo)

## `BoundProcessOperation` — class, line 238
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_runtime/process_resources.py:300`
- `src/agent_runtime/process_resources.py:318`
- `tests/test_effect_verification_adapters.py:67`
- `tests/test_effect_verification_adapters.py:76`

## `BoundProcessOperation.__post_init__` — method, line 249
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `BoundProcessOperation.validate` — method, line 264
- **called from:**
- `scripts/eval_ajax_basic_tools.py:59`
- `scripts/test_clean_tool_loop.py:118`
- `src/agent_runtime/authority.py:250`
- `src/agent_runtime/effect_adapters.py:392`
- `src/agent_runtime/effect_adapters.py:397`
- `src/agent_runtime/effect_adapters.py:408`
- `src/agent_runtime/owned_resources.py:229`
- `src/agent_runtime/owned_resources.py:408`
- `src/agent_runtime/owned_resources.py:422`
- `src/agent_runtime/owned_resources.py:438`
- `src/agent_runtime/owned_resources.py:450`
- `src/agent_runtime/process_resources.py:69`
- `src/agent_runtime/process_resources.py:153`
- `src/agent_runtime/process_resources.py:191`
- `src/agent_runtime/process_resources.py:198`
- `src/agent_runtime/process_resources.py:208`
- `src/agent_runtime/process_resources.py:266`
- `src/agent_runtime/process_resources.py:272`
- `src/agent_runtime/process_resources.py:326`
- `src/agent_runtime/process_resources.py:339`
- `src/agent_runtime/process_resources.py:357`
- `src/agent_runtime/process_resources.py:412`
- `src/agent_runtime/remote_resources.py:219`
- `src/agent_runtime/resource_binding.py:66`
- `src/agent_runtime/resource_binding.py:81`
- `src/agent_runtime/resource_binding.py:87`
- `src/agent_runtime/resource_binding.py:197`
- `src/agent_runtime/resource_binding.py:213`
- `src/agent_runtime/resources.py:380`
- `src/agent_runtime/resources.py:432`
- `src/agent_runtime/resources.py:433`
- `src/agent_runtime/resources.py:517`
- `src/agent_runtime/resources.py:560`
- `src/agent_tools/bg_job_tools.py:95`
- `src/agent_tools/filesystem_tools.py:1001`
- `src/ai_interaction.py:405`
- `src/bg_jobs.py:168`
- `src/browser_identity.py:134`
- `src/browser_identity.py:202`
- `src/browser_identity.py:491`
- `src/browser_identity.py:502`
- `src/browser_identity.py:511`
- `src/browser_identity.py:537`
- `src/browser_identity.py:541`
- `src/browser_identity.py:572`
- `src/browser_identity.py:583`
- `src/browser_identity.py:595`
- `src/browser_identity.py:604`
- `src/browser_identity.py:632`
- `src/browser_identity.py:636`
- `src/clean_agent_preview.py:7436`
- `src/clean_agent_preview.py:7809`
- `src/containment_worker.py:54`
- `src/containment_worker.py:57`
- `src/tool_execution.py:1251`
- `src/tool_execution.py:1635`
- `src/tool_execution.py:1673`
- `src/tool_execution.py:1989`
- `src/tool_execution.py:2159`
- `src/tool_execution.py:2162`
- … +28 more (grep the name in repo)

## `BoundProcessOperation.to_dict` — method, line 274
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5643`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31336`
- `src/agent_loop.py:31809`
- `src/agent_loop.py:32074`
- `src/agent_loop.py:32114`
- `src/agent_loop.py:32145`
- `src/agent_loop.py:32198`
- `src/agent_loop.py:32326`
- `src/agent_loop.py:32658`
- `src/agent_loop.py:34878`
- `src/agent_loop.py:36887`
- `src/agent_loop.py:37210`
- `src/agent_loop.py:37423`
- `src/agent_loop.py:37478`
- `src/agent_loop.py:37535`
- `src/agent_loop.py:37869`
- `src/agent_loop.py:37881`
- `src/agent_loop.py:37987`
- `src/agent_loop.py:38909`
- `src/agent_loop.py:38910`
- `src/agent_loop.py:38915`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:681`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/authority.py:705`
- `src/agent_runtime/completion.py:356`
- `src/agent_runtime/completion.py:385`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `src/agent_runtime/completion.py:392`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:78`
- `src/agent_runtime/context_resolution.py:154`
- `src/agent_runtime/context_resolution.py:155`
- `src/agent_runtime/context_resolution.py:502`
- `src/agent_runtime/context_resolution.py:518`
- `src/agent_runtime/effect_adapters.py:296`
- `src/agent_runtime/effect_log.py:263`
- `src/agent_runtime/effects.py:156`
- `src/agent_runtime/effects.py:161`
- `src/agent_runtime/effects.py:168`
- `src/agent_runtime/effects.py:173`
- `src/agent_runtime/effects.py:177`
- `src/agent_runtime/effects.py:181`
- `src/agent_runtime/effects.py:186`
- … +146 more (grep the name in repo)

## `needs_process_binding` — function, line 281
- **called from:**
- `src/agent_runtime/process_resources.py:286`
- `src/tool_approvals.py:420`
- `src/tool_execution.py:1851`

## `resolve_process_operation` — function, line 285
- **called from:**
- `src/builtin_actions.py:896`
- `src/tool_approvals.py:439`
- `src/tool_execution.py:1854`
- `tests/process_resource_helpers.py:17`
- `tests/process_resource_helpers.py:50`
- `tests/test_background_resource_identity.py:119`
- `tests/test_background_resource_identity.py:133`
- `tests/test_bg_job_tools.py:68`
- `tests/test_process_resource_identity.py:91`
- `tests/test_process_resource_identity.py:97`
- `tests/test_process_resource_identity.py:102`
- `tests/test_runtime_resource_integration.py:73`
- `tests/test_runtime_resource_integration.py:187`
- `tests/test_runtime_resource_integration.py:363`
- `tests/test_runtime_resource_integration.py:396`
- `tests/test_runtime_resource_integration.py:468`
- `tests/test_wave3_launch_cost_lifecycle.py:43`
- `tests/test_wave3_launch_cost_lifecycle.py:78`
- `tests/test_wave3_launch_cost_lifecycle.py:162`
- `tests/test_wave3_launch_cost_lifecycle.py:192`
- `tests/test_wave3_launch_cost_lifecycle.py:202`
- `tests/test_wave3_launch_cost_lifecycle.py:211`

## `active_process_operation` — function, line 330
- **called from:**
- `src/agent_runtime/effect_adapters.py:59`
- `src/agent_runtime/process_resources.py:353`
- `src/agent_runtime/process_resources.py:418`
- `src/agent_runtime/process_resources.py:523`
- `src/agent_tools/bg_job_tools.py:85`
- `src/bg_jobs.py:95`
- `src/tool_execution.py:1249`
- `tests/process_resource_helpers.py:73`
- `tests/test_runtime_resource_integration.py:143`
- `tests/test_runtime_resource_integration.py:155`
- `tests/test_runtime_resource_integration.py:190`
- `tests/test_runtime_resource_integration.py:197`
- `tests/test_runtime_resource_integration.py:198`
- `tests/test_runtime_resource_integration.py:203`
- `tests/test_wave3_launch_cost_lifecycle.py:58`

## `bind_process_operation` — function, line 335
- decorator: `contextmanager`
- **called from:**
- `src/builtin_actions.py:897`
- `src/tool_execution.py:1998`
- `tests/process_resource_helpers.py:18`
- `tests/test_bg_job_tools.py:69`
- `tests/test_runtime_resource_integration.py:75`
- `tests/test_runtime_resource_integration.py:189`
- `tests/test_runtime_resource_integration.py:196`
- `tests/test_wave3_launch_cost_lifecycle.py:49`
- `tests/test_wave3_launch_cost_lifecycle.py:82`
- `tests/test_wave3_launch_cost_lifecycle.py:91`

## `require_launch` — function, line 352
- **called from:**
- `src/agent_tools/subprocess_tools.py:529`
- `src/agent_tools/subprocess_tools.py:638`
- `src/agent_tools/subprocess_tools.py:934`
- `src/bg_jobs.py:94`

## `require_process_admission` — function, line 365
- **called from:**
- `src/agent_runtime/process_resources.py:356`
- `src/agent_runtime/process_resources.py:526`
- `src/agent_tools/bg_job_tools.py:92`

## `guard_launch_workspace` — function, line 379
- **called from:**
- `src/agent_runtime/process_resources.py:344`
- `tests/test_background_resource_identity.py:176`
- `tests/test_background_resource_identity.py:179`
- `tests/test_browser_resource_identity.py:247`
- `tests/test_wave3_launch_cost_lifecycle.py:184`
- `tests/test_wave3_launch_cost_lifecycle.py:187`

## `unresolved` — function, line 395
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `publish_launch` — function, line 410
- decorator: `store_transaction(lambda: _LAUNCH_DIR / "publication")`
- **called from:**
- `src/agent_tools/subprocess_tools.py:541`
- `src/bg_jobs.py:178`
- `tests/process_resource_helpers.py:64`
- `tests/test_runtime_resource_integration.py:367`
- `tests/test_runtime_resource_integration.py:400`
- `tests/test_runtime_resource_integration.py:472`
- `tests/test_wave3_launch_cost_lifecycle.py:164`
- `tests/test_wave3_launch_cost_lifecycle.py:193`
- `tests/test_wave3_launch_cost_lifecycle.py:203`
- `tests/test_wave3_launch_cost_lifecycle.py:212`

## `retire_launch` — function, line 429
- decorator: `store_transaction(lambda: _LAUNCH_DIR / "publication")`
- **called from:**
- `src/agent_tools/subprocess_tools.py:573`
- `src/bg_jobs.py:227`
- `tests/test_wave3_launch_cost_lifecycle.py:103`
- `tests/test_wave3_launch_cost_lifecycle.py:145`
- `tests/test_wave3_launch_cost_lifecycle.py:150`

## `prune_foreground_publications` — function, line 451
- decorator: `store_transaction(lambda: _LAUNCH_DIR / "publication")`
- **called from:**
- `src/process_reaper.py:292`
- `tests/test_wave3_launch_cost_lifecycle.py:168`
- `tests/test_wave3_launch_cost_lifecycle.py:176`
- `tests/test_wave3_launch_cost_lifecycle.py:194`
- `tests/test_wave3_launch_cost_lifecycle.py:205`
- `tests/test_wave3_launch_cost_lifecycle.py:216`

## `attach_containment_processes` — function, line 496
- decorator: `store_transaction(lambda: _LAUNCH_DIR / "publication")`
- **called from:**
- `src/agent_tools/subprocess_tools.py:549`
- `tests/test_runtime_resource_integration.py:385`
- `tests/test_runtime_resource_integration.py:413`
- `tests/test_runtime_resource_integration.py:495`

## `expected_job` — function, line 522
- **called from:**
- `src/agent_tools/bg_job_tools.py:107`
