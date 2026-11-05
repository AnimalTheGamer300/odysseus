# `src/browser_identity.py` — definitions & call sites

42 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `digest` — function, line 55
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

## `incarnation` — function, line 59
- **called from:**
- `src/agent_runtime/resources.py:198`
- `src/browser_identity.py:433`
- `tests/test_effect_verification_adapters.py:291`

## `browser_digest` — function, line 65
- **called from:**
- `src/browser_identity.py:297`
- `src/browser_identity.py:428`
- `src/browser_identity.py:463`
- `src/browser_identity.py:591`
- `tests/test_browser_resource_identity.py:44`
- `tests/test_browser_resource_identity.py:223`

## `page_unavailable` — function, line 77
- **called from:**
- `src/browser_identity.py:618`
- `src/tool_execution.py:1809`
- `src/tool_execution.py:1816`
- `src/tool_execution.py:1818`
- `src/tool_execution.py:1827`
- `src/tool_execution.py:1845`
- `src/tool_execution.py:2023`

## `parse_operation` — function, line 83
- **called from:**
- `src/agent_tools/web_tools.py:2362`
- `src/agent_tools/web_tools.py:2370`
- `src/browser_identity.py:534`
- `src/browser_identity.py:553`
- `src/browser_identity.py:614`
- `tests/test_browser_resource_identity.py:152`

## `native_browser` — function, line 109
- **called from:**
- `src/tool_approvals.py:441`
- `src/tool_execution.py:1842`
- `src/tool_execution.py:2022`
- `tests/test_browser_identity_transport.py:148`

## `TrustedProducer` — class, line 114
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/browser_identity.py:133`

## `TrustedProducer.validate` — method, line 119
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

## `trusted_producer` — function (async), line 128
- **called from:**
- `src/browser_identity.py:243`
- `tests/test_browser_resource_identity.py:203`
- `tests/test_browser_resource_identity.py:208`
- `tests/test_wave3_browser_platform.py:15`

## `run_client` — function (async), line 141
- **called from:**
- `src/browser_identity.py:135`
- `src/browser_identity.py:214`
- `tests/test_browser_identity_transport.py:37`

## `response` — function, line 172
- **called from:**
- `src/browser_identity.py:216`
- `tests/test_browser_resource_identity.py:217`
- `static/js/admin.js:1025`
- `static/js/chat.js:2916`
- `static/js/chat.js:8960`
- `static/js/chat.js:8972`
- `static/js/chat.js:9030`
- `static/js/chatRenderer.js:2297`
- `static/js/fileHandler.js:356`

## `RegisteredBrowser` — class, line 185
- decorator: `dataclass`
- **called from:**
- `src/browser_identity.py:256`

## `RegisteredBrowser.validate_config` — method, line 201
- **called from:**
- `src/browser_identity.py:213`
- `src/browser_identity.py:258`
- `src/browser_identity.py:487`
- `src/config.py:208`
- `tests/test_browser_resource_identity.py:235`

## `RegisteredBrowser.command` — method (async), line 212
- **called from:**
- `scripts/check_brotli.py:31`
- `scripts/check_brotli.py:45`
- `scripts/check_brotli.py:95`
- `src/browser_identity.py:421`
- `src/browser_identity.py:422`
- `src/browser_identity.py:435`
- `src/browser_identity.py:461`
- `src/browser_identity.py:462`
- `src/browser_identity.py:589`
- `tests/test_browser_identity_transport.py:65`
- `tests/test_browser_producer_live_contract.py:33`
- `tests/test_browser_producer_live_contract.py:38`
- `tests/test_browser_producer_live_contract.py:54`
- `tests/test_browser_producer_live_contract.py:56`
- `tests/test_browser_producer_live_contract.py:59`
- `tests/test_browser_producer_live_contract.py:62`
- `tests/test_browser_producer_live_contract.py:65`
- `tests/test_browser_producer_live_contract.py:72`
- `tests/test_browser_producer_live_contract.py:79`
- `tests/test_browser_producer_live_contract.py:83`
- `tests/test_browser_producer_live_contract.py:85`
- `tests/test_browser_producer_live_contract.py:86`
- `tests/test_browser_producer_live_contract.py:91`
- `tests/test_browser_producer_live_contract.py:92`
- `tests/test_browser_producer_live_contract.py:106`
- `static/js/cookbook.js:1216`
- `static/js/cookbook.js:1728`
- `static/js/cookbookRunning.js:1640`
- `static/js/cookbookServe.js:3421`
- `static/js/slashAutocomplete.js:217`
- `static/js/slashAutocomplete.js:218`
- `static/js/slashCommands.js:6408`

## `RegisteredBrowser.invalidate` — method, line 218
- **called from:**
- `companion/routes.py:78`
- `routes/chatgpt_subscription_routes.py:212`
- `routes/model_routes.py:706`
- `src/agent_tools/web_tools.py:2710`
- `src/browser_identity.py:415`
- `src/browser_identity.py:469`
- `src/browser_identity.py:479`
- `src/browser_identity.py:597`
- `src/browser_identity.py:646`
- `src/chatgpt_subscription.py:772`
- `static/js/editor/render-cancellation.js:13`
- `static/js/galleryEditor.js:4011`
- `static/js/galleryEditor.js:14218`

## `owned_environment` — function, line 225
- **called from:**
- `src/browser_identity.py:203`
- `src/browser_identity.py:256`
- `tests/test_browser_resource_identity.py:231`

## `register_producer` — function (async), line 233
- **called from:**
- `tests/test_browser_producer_live_contract.py:31`
- `tests/test_browser_resource_identity.py:77`

## `registered` — function, line 263
- **called from:**
- `src/agent_tools/web_tools.py:2699`
- `src/agent_tools/web_tools_prewave3.py:3835`
- `src/browser_identity.py:484`
- `src/browser_identity.py:492`
- `src/browser_identity.py:498`
- `src/browser_identity.py:560`
- `src/browser_identity.py:584`
- `src/browser_identity.py:633`
- `src/browser_identity.py:644`
- `tests/test_browser_resource_identity.py:326`
- `static/js/modalManager.js:1238`

## `daemon_observation` — function, line 267
- **called from:**
- `src/browser_identity.py:421`
- `src/browser_identity.py:461`
- `src/browser_identity.py:589`
- `tests/test_browser_identity_transport.py:67`

## `executable` — function, line 286
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CDPSidecar` — class, line 294
- **called from:**
- `src/browser_identity.py:437`
- `src/browser_identity.py:593`
- `tests/test_browser_identity_transport.py:46`
- `tests/test_browser_identity_transport.py:53`

## `CDPSidecar.__init__` — method, line 296
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

## `CDPSidecar.__aenter__` — method (async), line 301
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CDPSidecar.__aexit__` — method (async), line 319
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `CDPSidecar._send` — method (async), line 326
- **called from:**
- `src/browser_identity.py:349`
- `src/browser_identity.py:367`

## `CDPSidecar._message` — method (async), line 335
- **called from:**
- `src/browser_identity.py:369`

## `CDPSidecar.call` — method (async), line 359
- **called from:**
- `src/browser_identity.py:438`
- `src/browser_identity.py:446`
- `src/browser_identity.py:451`
- `src/browser_identity.py:456`
- `src/browser_identity.py:460`
- `src/browser_identity.py:594`
- `tests/test_browser_identity_transport.py:48`
- `tests/test_browser_identity_transport.py:59`
- `tests/test_browser_transport_recovery.py:62`
- `tests/test_browser_transport_recovery.py:63`
- `tests/test_browser_transport_recovery.py:64`
- `tests/test_clean_agent_preview.py:1240`
- `tests/test_clean_agent_preview.py:1242`
- `tests/test_clean_agent_preview.py:2146`
- `tests/test_clean_agent_preview.py:2147`
- `tests/test_clean_agent_preview.py:2148`
- `tests/test_clean_agent_preview.py:5446`
- `tests/test_clean_agent_preview.py:5447`
- `tests/test_clean_tool_loop.py:28`
- `tests/test_clean_tool_loop.py:35`
- `tests/test_clean_tool_loop.py:39`
- `tests/test_clean_tool_loop.py:54`
- `tests/test_effect_resource_bindings.py:47`
- `tests/test_effect_resource_bindings.py:466`
- `tests/test_gallery_album_input.py:33`
- `tests/test_gallery_album_input.py:48`
- `tests/test_gallery_image_bad_input.py:38`
- `tests/test_gallery_image_bad_input.py:45`
- `tests/test_manage_tasks_cron.py:29`
- `tests/test_manage_tasks_cron.py:40`
- `tests/test_manage_tasks_cron.py:41`
- `tests/test_manage_tasks_cron.py:45`
- `tests/test_manage_tasks_cron.py:47`
- `tests/test_manage_tasks_cron.py:56`
- `tests/test_manage_tasks_cron.py:80`
- `tests/test_manage_tasks_cron.py:88`
- `tests/test_manage_tasks_cron.py:90`
- `tests/test_manage_tasks_cron.py:109`
- `tests/test_manage_tasks_cron.py:118`
- `tests/test_manage_tasks_cron.py:125`
- `tests/test_manage_tasks_cron.py:133`
- `tests/test_manage_tasks_cron.py:142`
- `tests/test_manage_tasks_cron.py:153`
- `tests/test_manage_tasks_cron.py:155`
- `tests/test_manage_tasks_cron.py:166`
- `tests/test_manage_tasks_cron.py:168`
- `tests/test_notes_checklist_state.py:35`
- `tests/test_notes_checklist_state.py:37`
- `tests/test_notes_checklist_state.py:39`
- `tests/test_notes_checklist_state.py:44`
- `tests/test_notes_checklist_state.py:45`
- `tests/test_notes_checklist_state.py:48`
- `tests/test_notes_checklist_state.py:53`
- `tests/test_notes_checklist_state.py:54`
- `tests/test_notes_checklist_state.py:57`
- `tests/test_notes_checklist_state.py:62`
- `tests/test_notes_checklist_state.py:63`
- `tests/test_notes_checklist_state.py:64`
- `tests/test_notes_checklist_state.py:65`
- `tests/test_notes_checklist_state.py:66`
- … +67 more (grep the name in repo)

## `CDPSidecar.exchange` — method (async), line 366
- **called from:**
- `src/browser_identity.py:380`

## `tabs_schema` — function, line 385
- **called from:**
- `src/browser_identity.py:435`
- `tests/test_browser_producer_live_contract.py:92`

## `observe_registered` — function (async), line 404
- **called from:**
- `tests/test_browser_identity_transport.py:73`
- `tests/test_browser_producer_live_contract.py:45`
- `tests/test_browser_producer_live_contract.py:46`
- `tests/test_browser_producer_live_contract.py:55`
- `tests/test_browser_producer_live_contract.py:57`
- `tests/test_browser_producer_live_contract.py:60`
- `tests/test_browser_producer_live_contract.py:63`
- `tests/test_browser_producer_live_contract.py:66`
- `tests/test_browser_producer_live_contract.py:73`
- `tests/test_browser_producer_live_contract.py:80`
- `tests/test_browser_producer_live_contract.py:104`
- `tests/test_browser_resource_identity.py:78`
- `tests/test_browser_resource_identity.py:173`
- `tests/test_browser_resource_identity.py:184`
- `tests/test_browser_resource_identity.py:192`
- `tests/test_browser_resource_identity.py:196`
- `tests/test_browser_resource_identity.py:297`

## `_observe_registered_locked` — function (async), line 419
- **called from:**
- `src/browser_identity.py:413`

## `validate_session` — function, line 483
- **called from:**
- `src/agent_runtime/resources.py:229`

## `validate_page` — function, line 490
- **called from:**
- `src/agent_runtime/resources.py:266`

## `seal_browser_resources` — function, line 497
- **called from:**
- `src/agent_runtime/authority.py:195`

## `intersect_browser` — function, line 508
- **called from:**
- `src/agent_runtime/authority.py:253`

## `BoundBrowserOperation` — class, line 522
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/browser_identity.py:570`
- `tests/test_effect_verification_adapters.py:298`
- `tests/test_effect_verification_adapters.py:299`
- `tests/test_effect_verification_adapters.py:317`

## `BoundBrowserOperation.validate` — method, line 531
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

## `BoundBrowserOperation.to_dict` — method, line 545
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5624`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28789`
- `src/agent_loop.py:31316`
- `src/agent_loop.py:31789`
- `src/agent_loop.py:32054`
- `src/agent_loop.py:32094`
- `src/agent_loop.py:32125`
- `src/agent_loop.py:32178`
- `src/agent_loop.py:32306`
- `src/agent_loop.py:32638`
- `src/agent_loop.py:34858`
- `src/agent_loop.py:36867`
- `src/agent_loop.py:37190`
- `src/agent_loop.py:37403`
- `src/agent_loop.py:37458`
- `src/agent_loop.py:37515`
- `src/agent_loop.py:37849`
- `src/agent_loop.py:37861`
- `src/agent_loop.py:37967`
- `src/agent_loop.py:38889`
- `src/agent_loop.py:38890`
- `src/agent_loop.py:38895`
- `src/agent_runtime/authority.py:282`
- `src/agent_runtime/authority.py:283`
- `src/agent_runtime/authority.py:284`
- `src/agent_runtime/authority.py:285`
- `src/agent_runtime/authority.py:286`
- `src/agent_runtime/authority.py:287`
- `src/agent_runtime/authority.py:288`
- `src/agent_runtime/authority.py:289`
- `src/agent_runtime/authority.py:653`
- `src/agent_runtime/authority.py:677`
- `src/agent_runtime/authority.py:677`
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

## `resolve_browser_operation` — function, line 552
- **called from:**
- `src/tool_approvals.py:444`
- `src/tool_execution.py:1848`
- `tests/test_browser_resource_identity.py:295`
- `tests/test_browser_resource_identity.py:304`

## `revalidate_browser_operation` — function (async), line 582
- **called from:**
- `src/browser_identity.py:634`
- `src/tool_execution.py:1850`

## `bind_browser_operation` — function, line 602
- decorator: `contextmanager`
- **called from:**
- `src/tool_execution.py:1998`
- `tests/test_browser_resource_identity.py:306`
- `tests/test_browser_resource_identity.py:310`

## `execute_browser` — function (async), line 612
- **called from:**
- `src/agent_tools/web_tools.py:2344`
