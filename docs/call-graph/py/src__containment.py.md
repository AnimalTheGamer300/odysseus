# `src/containment.py` — definitions & call sites

74 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_protected_writable_destination` — function, line 143
- **called from:**
- `src/containment.py:595`

## `ContainmentUnavailable` — class, line 157
- **called from:**
- `src/agent_tools/subprocess_tools.py:419`
- `src/containment.py:732`
- `src/containment.py:850`
- `src/containment.py:1036`
- `src/containment.py:1121`
- `src/containment.py:1134`
- `src/containment.py:1190`
- `src/containment.py:1260`

## `ContainmentUnavailable.__init__` — method, line 166
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

## `ContainmentSpec` — class, line 178
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_tools/subprocess_tools.py:493`
- `src/containment.py:613`
- `src/containment.py:1563`
- `src/containment_worker.py:29`
- `src/process_reaper.py:245`
- `tests/test_containment_contract.py:72`
- `tests/test_containment_contract.py:259`
- `tests/test_containment_contract.py:390`
- `tests/test_containment_contract.py:400`
- `tests/test_containment_enforcement.py:127`
- `tests/test_containment_enforcement.py:157`
- `tests/test_containment_enforcement.py:178`
- `tests/test_containment_enforcement.py:377`
- `tests/test_containment_enforcement.py:398`
- `tests/test_containment_process_tree.py:62`
- `tests/test_containment_process_tree.py:310`
- `tests/test_containment_process_tree.py:340`
- `tests/test_containment_process_tree.py:367`
- `tests/test_native_execution_containment.py:69`
- `tests/test_native_execution_containment.py:84`
- `tests/test_native_execution_containment.py:108`
- `tests/test_native_execution_containment.py:160`
- `tests/test_orphan_reaping.py:217`

## `ContainmentSpec.__post_init__` — method, line 197
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContainmentSpec.requested` — method, line 207
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContainmentGrant` — class, line 225
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/containment.py:735`
- `src/containment.py:775`
- `src/containment.py:1569`
- `src/containment_worker.py:31`
- `src/process_reaper.py:247`
- `tests/test_containment_contract.py:184`
- `tests/test_containment_enforcement.py:74`
- `tests/test_orphan_reaping.py:220`

## `ContainmentGrant.contained` — method, line 248
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContainmentGrant.to_dict` — method, line 252
- **called from:**
- `core/models.py:175`
- `routes/chat_routes.py:5646`
- `services/memory/builtin_skills.py:66`
- `services/memory/builtin_skills.py:73`
- `services/memory/skills.py:280`
- `services/memory/skills.py:453`
- `services/memory/skills.py:501`
- `src/agent_evidence.py:1270`
- `src/agent_loop.py:28809`
- `src/agent_loop.py:31378`
- `src/agent_loop.py:31851`
- `src/agent_loop.py:32116`
- `src/agent_loop.py:32156`
- `src/agent_loop.py:32187`
- `src/agent_loop.py:32240`
- `src/agent_loop.py:32368`
- `src/agent_loop.py:32700`
- `src/agent_loop.py:34920`
- `src/agent_loop.py:36929`
- `src/agent_loop.py:37252`
- `src/agent_loop.py:37465`
- `src/agent_loop.py:37520`
- `src/agent_loop.py:37577`
- `src/agent_loop.py:37911`
- `src/agent_loop.py:37923`
- `src/agent_loop.py:38029`
- `src/agent_loop.py:38963`
- `src/agent_loop.py:38964`
- `src/agent_loop.py:38969`
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

## `ContainmentResult` — class, line 277
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/containment.py:1203`

## `Mechanism` — class, line 294
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/containment.py:418`
- `src/containment.py:419`
- `src/containment.py:420`
- `tests/test_containment_contract.py:49`
- `tests/test_containment_contract.py:279`
- `tests/test_containment_enforcement.py:338`
- `tests/test_native_execution_containment.py:125`

## `_bwrap_available` — function, line 307
- **called from:**
- `src/agent_tools/subprocess_tools.py:460`
- `tests/test_containment_enforcement.py:29`
- `tests/test_containment_enforcement.py:42`
- `tests/test_workspace_artifact_tool_floor.py:2217`

## `_posix_group_available` — function, line 327
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_windows_available` — function, line 331
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_rlimit_fits` — function, line 343
- **called from:**
- `src/containment.py:376`
- `src/containment.py:382`

## `_rlimit_dimensions` — function, line 364
- **called from:**
- `src/containment.py:394`
- `src/containment.py:403`

## `_bwrap_provides` — function, line 388
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_posix_group_provides` — function, line 400
- **called from:**
- `tests/test_containment_enforcement.py:68`

## `_windows_provides` — function, line 406
- **called from:**
- `tests/test_containment_enforcement.py:69`

## `_store_path` — function, line 425
- **called from:**
- `src/agent_runtime/process_resources.py:390`
- `src/agent_runtime/process_resources.py:466`
- `src/agent_runtime/resources.py:101`
- `src/bg_jobs.py:118`
- `src/containment.py:431`
- `src/containment.py:450`
- `src/containment.py:468`
- `src/containment.py:500`
- `src/containment.py:523`
- `tests/process_resource_helpers.py:63`
- `tests/test_background_containment.py:69`
- `tests/test_background_resource_identity.py:92`
- `tests/test_background_resource_identity.py:161`
- `tests/test_background_resource_identity.py:201`
- `tests/test_background_resource_identity.py:254`
- `tests/test_wave3_launch_cost_lifecycle.py:147`
- `tests/test_wave3_launch_cost_lifecycle.py:186`
- `tests/test_wave3_launch_cost_lifecycle.py:195`

## `_load_records` — function, line 429
- **called from:**
- `src/agent_runtime/process_resources.py:141`
- `src/agent_runtime/process_resources.py:502`
- `src/agent_tools/subprocess_tools.py:554`
- `src/agent_tools/subprocess_tools.py:568`
- `src/bg_jobs.py:328`
- `src/bg_jobs.py:340`
- `src/containment.py:470`
- `src/containment.py:502`
- `src/containment.py:518`
- `src/containment.py:526`
- `src/containment.py:1028`
- `src/containment.py:1405`
- `src/containment.py:1483`
- `src/containment_worker.py:58`
- `src/containment_worker.py:94`
- `src/containment_worker.py:97`
- `src/process_reaper.py:255`
- `tests/process_resource_helpers.py:59`
- `tests/test_background_containment.py:144`
- `tests/test_background_resource_identity.py:89`
- `tests/test_background_resource_identity.py:198`
- `tests/test_wave3_launch_cost_lifecycle.py:152`
- `tests/test_wave3_launch_cost_lifecycle.py:178`

## `_save_records` — function, line 448
- **called from:**
- `src/containment.py:497`
- `src/containment.py:508`
- `src/containment.py:528`
- `tests/test_orphan_reaping.py:71`
- `tests/test_runtime_resource_integration.py:368`
- `tests/test_runtime_resource_integration.py:401`
- `tests/test_runtime_resource_integration.py:473`

## `_prune` — function, line 457
- **called from:**
- `src/bg_jobs.py:310`
- `src/containment.py:470`
- `src/containment.py:518`
- `tests/test_caldav_sync_prune_local_events.py:82`
- `tests/test_caldav_sync_prune_local_events.py:96`
- `tests/test_wave3_launch_cost_lifecycle.py:114`

## `_write_record` — function, line 469
- decorator: `store_transaction(lambda: _store_path())`
- **called from:**
- `src/containment.py:757`
- `src/containment.py:792`
- `src/process_reaper.py:253`

## `_update_record` — function, line 501
- decorator: `store_transaction(lambda: _store_path())`
- **called from:**
- `src/agent_tools/subprocess_tools.py:540`
- `src/bg_jobs.py:173`
- `src/containment.py:1095`
- `src/containment.py:1127`
- `src/containment.py:1128`
- `src/containment.py:1136`
- `src/containment.py:1201`
- `src/containment.py:1646`
- `src/containment.py:1689`
- `src/containment.py:1694`
- `src/process_reaper.py:254`
- `tests/test_containment_enforcement.py:160`

## `active_grants` — function, line 511
- **called from:**
- `src/process_reaper.py:61`
- `tests/test_agent_tmux_retirement.py:133`
- `tests/test_background_containment.py:83`
- `tests/test_containment_contract.py:434`
- `tests/test_containment_contract.py:452`
- `tests/test_containment_contract.py:460`
- `tests/test_containment_contract.py:488`
- `tests/test_containment_enforcement.py:143`
- `tests/test_containment_enforcement.py:163`
- `tests/test_containment_enforcement.py:170`
- `tests/test_containment_enforcement.py:290`
- `tests/test_containment_enforcement.py:303`
- `tests/test_containment_enforcement.py:333`
- `tests/test_containment_enforcement.py:359`
- `tests/test_containment_enforcement.py:389`
- `tests/test_containment_enforcement.py:413`
- `tests/test_containment_process_tree.py:223`
- `tests/test_containment_process_tree.py:258`
- `tests/test_execution_filesystem_boundary.py:254`
- `tests/test_native_execution_containment.py:45`
- `tests/test_native_execution_containment.py:64`
- `tests/test_orphan_reaping.py:128`
- `tests/test_orphan_reaping.py:142`
- `tests/test_orphan_reaping.py:262`
- `tests/test_orphan_reaping.py:274`
- `tests/test_orphan_reaping.py:293`
- `tests/test_orphan_reaping.py:311`
- `tests/test_orphan_reaping.py:327`
- `tests/test_runtime_resource_integration.py:162`
- `tests/test_runtime_resource_integration.py:219`

## `forget` — function, line 524
- decorator: `store_transaction(lambda: _store_path())`
- **called from:**
- `src/agent_tools/web_tools.py:2703`
- `src/agent_tools/web_tools_prewave3.py:2679`
- `src/agent_tools/web_tools_prewave3.py:3859`
- `src/process_reaper.py:71`
- `src/process_reaper.py:97`
- `src/process_reaper.py:106`
- `src/process_reaper.py:126`
- `tests/test_containment_contract.py:459`

## `_validate_abs_path` — function, line 532
- **called from:**
- `src/containment.py:582`
- `src/containment.py:586`
- `src/containment.py:589`

## `_validate_spec` — function, line 543
- **called from:**
- `src/containment.py:689`
- `src/containment.py:722`
- `src/containment.py:774`

## `agent_spec` — function, line 600
- **called from:**
- `src/agent_tools/subprocess_tools.py:318`
- `src/agent_tools/subprocess_tools.py:513`
- `src/tool_execution.py:385`
- `tests/test_agent_tmux_retirement.py:106`
- `tests/test_background_containment.py:66`
- `tests/test_containment_contract.py:128`
- `tests/test_containment_contract.py:153`
- `tests/test_containment_contract.py:170`
- `tests/test_containment_contract.py:183`
- `tests/test_containment_contract.py:204`
- `tests/test_containment_contract.py:220`
- `tests/test_containment_contract.py:300`
- `tests/test_containment_contract.py:309`
- `tests/test_containment_contract.py:321`
- `tests/test_containment_contract.py:332`
- `tests/test_containment_contract.py:340`
- `tests/test_containment_contract.py:431`
- `tests/test_containment_contract.py:447`
- `tests/test_containment_contract.py:458`
- `tests/test_containment_contract.py:478`
- `tests/test_containment_contract.py:487`
- `tests/test_containment_contract.py:496`
- `tests/test_containment_enforcement.py:67`
- `tests/test_containment_enforcement.py:73`
- `tests/test_execution_filesystem_boundary.py:250`
- `tests/test_execution_filesystem_boundary.py:262`
- `tests/test_execution_filesystem_boundary.py:272`
- `tests/test_execution_filesystem_boundary.py:286`
- `tests/test_production_external_bridge.py:171`

## `_select` — function, line 623
- **called from:**
- `src/containment.py:690`
- `src/containment.py:724`
- `tests/test_null_owner_gates.py:298`
- `tests/test_null_owner_gates.py:304`
- `tests/test_null_owner_gates.py:312`
- `tests/test_null_owner_gates.py:317`
- `tests/test_null_owner_gates.py:325`
- `tests/test_null_owner_gates.py:332`

## `ContainmentProbe` — class, line 650
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_tools/subprocess_tools.py:337`
- `src/containment.py:693`
- `tests/test_execution_filesystem_boundary.py:211`

## `ContainmentProbe.contained` — method, line 671
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `ContainmentProbe.refuses` — method, line 675
- decorator: `property`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `probe` — function, line 680
- **called from:**
- `scripts/probe_browser_budget.py:100`
- `scripts/probe_empty_search_recovery.py:76`
- `src/agent_tools/subprocess_tools.py:317`
- `src/service_health.py:381`
- `tests/test_execution_filesystem_boundary.py:249`
- `tests/test_execution_filesystem_boundary.py:263`
- `tests/test_execution_filesystem_boundary.py:274`
- `tests/test_execution_filesystem_boundary.py:276`
- `tests/test_execution_filesystem_boundary.py:285`
- `static/js/cookbook-hwfit.js:2320`
- `static/js/cookbookRunning.js:4149`
- `static/js/cookbookRunning.js:4150`
- `static/js/cookbookServe.js:3113`

## `acquire` — function, line 702
- **called from:**
- `routes/contacts/contacts_routes.py:453`
- `src/agent_tools/subprocess_tools.py:536`
- `src/agent_tools/web_tools_prewave3.py:2653`
- `src/bg_jobs.py:112`
- `src/email_calendar_import.py:42`
- `src/llm_core.py:157`
- `tests/test_agent_tmux_retirement.py:106`
- `tests/test_background_containment.py:67`
- `tests/test_browser_identity_transport.py:72`
- `tests/test_containment_contract.py:87`
- `tests/test_containment_contract.py:97`
- `tests/test_containment_contract.py:111`
- `tests/test_containment_contract.py:130`
- `tests/test_containment_contract.py:155`
- `tests/test_containment_contract.py:170`
- `tests/test_containment_contract.py:207`
- `tests/test_containment_contract.py:221`
- `tests/test_containment_contract.py:234`
- `tests/test_containment_contract.py:245`
- `tests/test_containment_contract.py:266`
- `tests/test_containment_contract.py:282`
- `tests/test_containment_contract.py:301`
- `tests/test_containment_contract.py:321`
- `tests/test_containment_contract.py:332`
- `tests/test_containment_contract.py:343`
- `tests/test_containment_contract.py:347`
- `tests/test_containment_contract.py:381`
- `tests/test_containment_contract.py:394`
- `tests/test_containment_contract.py:402`
- `tests/test_containment_contract.py:408`
- `tests/test_containment_contract.py:416`
- `tests/test_containment_contract.py:432`
- `tests/test_containment_contract.py:447`
- `tests/test_containment_contract.py:458`
- `tests/test_containment_contract.py:478`
- `tests/test_containment_contract.py:487`
- `tests/test_containment_contract.py:535`
- `tests/test_containment_contract.py:541`
- `tests/test_containment_enforcement.py:128`
- `tests/test_containment_enforcement.py:158`
- `tests/test_containment_enforcement.py:179`
- `tests/test_containment_enforcement.py:298`
- `tests/test_containment_enforcement.py:325`
- `tests/test_containment_enforcement.py:379`
- `tests/test_containment_enforcement.py:400`
- `tests/test_containment_process_tree.py:102`
- `tests/test_containment_process_tree.py:117`
- `tests/test_containment_process_tree.py:136`
- `tests/test_containment_process_tree.py:169`
- `tests/test_containment_process_tree.py:190`
- `tests/test_containment_process_tree.py:216`
- `tests/test_containment_process_tree.py:251`
- `tests/test_containment_process_tree.py:262`
- `tests/test_containment_process_tree.py:276`
- `tests/test_containment_process_tree.py:285`
- `tests/test_containment_process_tree.py:294`
- `tests/test_containment_process_tree.py:302`
- `tests/test_containment_process_tree.py:319`
- `tests/test_containment_process_tree.py:347`
- `tests/test_containment_process_tree.py:377`
- … +7 more (grep the name in repo)

## `declare_external_bridge` — function, line 761
- **called from:**
- `src/agent_tools/subprocess_tools.py:711`
- `src/tool_execution.py:386`
- `tests/test_containment_contract.py:497`
- `tests/test_production_external_bridge.py:172`

## `unavailable_tool_result` — function, line 796
- **called from:**
- `src/agent_tools/subprocess_tools.py:551`
- `src/containment_worker.py:105`
- `src/tool_execution.py:2257`
- `tests/test_containment_contract.py:132`

## `_dir_chain` — function, line 819
- **called from:**
- `src/containment.py:866`
- `src/containment.py:875`

## `_bwrap_prefix` — function, line 839
- **called from:**
- `src/agent_tools/subprocess_tools.py:497`
- `src/containment.py:945`
- `tests/test_containment_enforcement.py:94`

## `_rlimit_preexec` — function, line 883
- **called from:**
- `src/containment.py:959`

## `_apply` — function, line 904
- **called from:**
- `static/js/markdown.js:1806`
- `static/js/markdown.js:1810`
- `static/js/theme.js:775`

## `_launch_argv` — function, line 913
- **called from:**
- `src/containment.py:1045`

## `_spawn_kwargs` — function, line 949
- **called from:**
- `src/containment.py:1046`

## `_drain` — function (async), line 965
- **called from:**
- `src/agent_runs.py:213`
- `src/containment.py:1109`
- `src/containment.py:1140`
- `src/llm_core.py:380`
- `src/llm_core.py:383`
- `tests/test_kv_cache_invalidation_2927.py:407`
- `tests/test_kv_cache_invalidation_2927.py:408`
- `tests/test_kv_cache_invalidation_2927.py:409`
- `tests/test_kv_cache_invalidation_2927.py:438`
- `tests/test_kv_cache_invalidation_2927.py:459`
- `tests/test_model_routes.py:1169`
- `tests/test_model_routes.py:1206`

## `emit` — function, line 979
- **called from:**
- `scripts/eval_exact_file_routing.py:170`
- `scripts/eval_exact_file_routing.py:184`
- `src/containment.py:992`
- `src/containment.py:998`
- `src/email_reply_stream.py:26`
- `src/email_reply_stream.py:42`
- `src/email_reply_stream.py:48`
- `static/js/editor/brush-engine.js:24`

## `run` — function (async), line 1004
- **called from:**
- `app.py:1228`
- `app.py:1530`
- `core/platform_compat.py:428`
- `core/platform_compat.py:469`
- `launcher.py:114`
- `launcher.py:149`
- `mcp_servers/email_server.py:4704`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/image_gen_server.py:188`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/memory_server.py:281`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/rag_server.py:156`
- `mcp_servers/rag_server.py:160`
- `mcp_servers/rag_server.py:160`
- `routes/cookbook_routes.py:1527`
- `routes/cookbook_routes.py:3626`
- `routes/cookbook_routes.py:3639`
- `routes/cookbook_routes.py:3650`
- `routes/cookbook_routes.py:3711`
- `routes/cookbook_routes.py:4177`
- `routes/cookbook_routes.py:4179`
- `routes/cookbook_routes.py:4201`
- `routes/cookbook_routes.py:4203`
- `routes/cookbook_routes.py:4368`
- `routes/cookbook_routes.py:4378`
- `routes/document/document_routes.py:489`
- `routes/email/email_routes.py:5062`
- `routes/email/email_routes.py:6861`
- `routes/hwfit_routes.py:147`
- `scripts/build_frontend.py:69`
- `scripts/build_frontend.py:70`
- `scripts/check_brotli.py:39`
- `scripts/css_snapshot.py:92`
- `scripts/css_snapshot.py:131`
- `scripts/diffusion_server.py:1506`
- `scripts/dump_agent_prompt.py:415`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_qwen_tool_groups_stream.py:276`
- `scripts/mlx_image_server.py:207`
- `scripts/mlx_image_server.py:281`
- `scripts/mlx_image_server.py:379`
- `scripts/mlx_image_server.py:466`
- `scripts/pr_blocker_audit.py:253`
- `scripts/probe_browser_budget.py:112`
- `scripts/probe_empty_search_recovery.py:90`
- `scripts/probe_fixed_search_evidence.py:81`
- `scripts/ref_parity_audit.py:142`
- `scripts/ref_parity_audit.py:232`
- `scripts/review_sft_environment_expansion.py:115`
- `scripts/run_odysseus_cases_chunked.py:107`
- `scripts/run_odysseus_search_teacher_pipeline.py:305`
- `scripts/run_odysseus_search_teacher_pipeline.py:412`
- `scripts/test_clean_tool_loop.py:209`
- … +1417 more (grep the name in repo)

## `_wait` — function (async), line 1112
- **called from:**
- `src/containment.py:1187`

## `_progress` — function (async), line 1154
- **called from:**
- `src/containment.py:1164`
- `src/deep_research.py:1829`
- `src/research_navigator.py:211`

## `_finish` — function (async), line 1167
- **called from:**
- `routes/gallery/gallery_routes.py:2091`
- `routes/gallery/gallery_routes.py:2095`
- `routes/gallery/gallery_routes.py:2097`
- `src/containment.py:1199`

## `_complete_cleanup` — function (async), line 1214
- **called from:**
- `src/containment.py:1064`
- `src/containment.py:1073`
- `src/containment.py:1101`
- `src/containment.py:1199`

## `_capture_namespace_identity` — function (async), line 1231
- **called from:**
- `src/containment.py:1122`
- `src/containment.py:1637`

## `_own_pgid` — function, line 1273
- **called from:**
- `src/containment.py:1290`
- `src/containment.py:1295`

## `_pgid_of` — function, line 1277
- **called from:**
- `src/process_reaper.py:251`

## `_group_present` — function, line 1283
- **called from:**
- `src/containment.py:1308`
- `src/containment.py:1362`
- `src/containment.py:1510`
- `src/process_reaper.py:91`
- `tests/test_containment_process_tree.py:123`
- `tests/test_containment_process_tree.py:246`
- `tests/test_native_execution_containment.py:103`

## `_signal_tree` — function, line 1293
- **called from:**
- `src/containment.py:1508`
- `src/containment.py:1669`
- `src/containment.py:1673`
- `tests/test_containment_process_tree.py:240`

## `_reap_if_child` — function, line 1298
- **called from:**
- `src/containment.py:1307`

## `_tree_gone` — function, line 1305
- **called from:**
- `src/containment.py:1503`
- `src/containment.py:1663`

## `_outcome_for` — function, line 1311
- **called from:**
- `src/containment.py:1364`
- `src/containment.py:1511`
- `src/containment.py:1526`
- `src/containment.py:1544`
- `src/containment.py:1680`

## `_ownership_gate` — function, line 1331
- **called from:**
- `src/containment.py:1516`
- `src/containment.py:1534`

## `release` — function, line 1402
- **called from:**
- `routes/contacts/contacts_routes.py:481`
- `src/agent_tools/subprocess_tools.py:556`
- `src/agent_tools/web_tools_prewave3.py:2676`
- `src/bg_jobs.py:138`
- `src/bg_jobs.py:193`
- `src/containment.py:1066`
- `src/containment.py:1077`
- `src/containment.py:1587`
- `src/containment.py:1633`
- `src/containment_worker.py:96`
- `src/llm_core.py:180`
- `src/process_reaper.py:261`
- `tests/test_agent_tmux_retirement.py:109`
- `tests/test_browser_identity_transport.py:77`
- `tests/test_containment_contract.py:448`
- `tests/test_containment_enforcement.py:149`
- `tests/test_containment_enforcement.py:180`
- `tests/test_containment_enforcement.py:184`
- `tests/test_containment_process_tree.py:171`
- `tests/test_containment_process_tree.py:192`
- `tests/test_containment_process_tree.py:219`
- `tests/test_orphan_reaping.py:229`
- `tests/test_runtime_resource_integration.py:148`
- `tests/test_task_scheduler_cancel.py:104`
- `tests/test_task_scheduler_cancel.py:168`
- `static/js/features/notes/ui/cardReorder.js:9`
- `static/js/features/notes/ui/checklistReorder.js:25`
- `static/js/features/notes/ui/lifecycle.js:5`
- `static/js/features/notes/ui/lifecycle.js:24`
- `static/js/features/notes/ui/lifecycle.js:34`
- `static/js/init.js:423`
- `static/js/init.js:431`
- `static/js/modalSnap.js:772`
- `static/js/modalSnap.js:788`
- `static/js/modalSnap.js:819`
- `static/js/windowDrag.js:212`
- `static/js/windowDrag.js:217`
- `static/js/windowDrag.js:226`
- `static/js/windowDrag.js:227`
- `static/js/windowDrag.js:259`
- `static/js/windowDrag.js:260`
- `static/js/windowDrag.js:274`
- `static/js/windowDrag.js:275`
- `static/js/windowDrag.js:280`
- `static/js/windowDrag.js:286`
- `static/js/windowDrag.js:291`
- `static/js/windowDrag.js:292`

## `_release_owner` — function, line 1456
- **called from:**
- `src/containment.py:1415`
- `src/containment.py:1440`

## `finish` — function, line 1471
- **called from:**
- `src/agent_loop.py:33038`
- `src/agent_loop.py:33051`
- `src/agent_loop.py:33059`
- `src/agent_loop.py:34919`
- `src/agent_runtime/journal.py:267`
- `src/agent_runtime/journal.py:269`
- `src/containment.py:1512`
- `src/containment.py:1518`
- `src/containment.py:1527`
- `src/containment.py:1542`
- `src/containment.py:1545`
- `src/pdf_forms.py:338`
- `tests/test_effect_verification_adapters.py:55`
- `tests/test_effect_verification_adapters.py:121`
- `tests/test_effect_verification_adapters.py:215`
- `tests/test_effect_verification_adapters.py:431`
- `static/js/calendar.js:34`
- `static/js/calendar.js:42`
- `static/js/calendar.js:43`
- `static/js/calendar.js:45`
- `static/js/chat.js:2122`
- `static/js/colorPicker.js:237`
- `static/js/colorPicker.js:243`
- `static/js/editor/adjustment-layer.js:205`
- `static/js/editor/adjustment-layer.js:211`
- `static/js/editor/adjustment-layer.js:215`
- `static/js/editor/ai-inpaint.js:280`
- `static/js/editor/ai-operation.js:19`
- `static/js/editor/ai-tool-runner.js:164`
- `static/js/editor/ai-tools-misc.js:157`
- `static/js/editor/ai-tools-misc.js:206`
- `static/js/editor/effects.js:364`
- `static/js/editor/effects.js:372`
- `static/js/editor/effects.js:376`
- `static/js/editor/layer-panel.js:1424`
- `static/js/editor/layer-panel.js:1426`
- `static/js/editor/layer-panel.js:1431`
- `static/js/editor/precision-guides.js:210`
- `static/js/editor/precision-guides.js:229`
- `static/js/editor/tools/pen-path.js:39`
- `static/js/editor/tools/pen-path.js:46`
- `static/js/features/notes/ui/cardInteractions.js:234`
- `static/js/features/notes/ui/cardInteractions.js:238`
- `static/js/features/notes/ui/colors.js:63`
- `static/js/features/notes/ui/colors.js:71`
- `static/js/features/notes/ui/colors.js:72`
- `static/js/features/notes/ui/colors.js:75`
- `static/js/fileHandler.js:96`
- `static/js/fileHandler.js:134`
- `static/js/fileHandler.js:135`
- `static/js/fileHandler.js:172`
- `static/js/fileHandler.js:175`
- `static/js/gallery.js:2484`
- `static/js/gallery.js:2487`
- `static/js/galleryEditor.js:430`
- `static/js/galleryEditor.js:4572`
- `static/js/galleryEditor.js:4573`
- `static/js/galleryEditor.js:4575`
- `static/js/galleryEditor.js:4655`
- `static/js/galleryEditor.js:4659`
- … +4 more (grep the name in repo)

## `gone` — function, line 1500
- **called from:**
- `src/process_lifecycle.py:470`
- `src/process_lifecycle.py:481`
- `src/process_lifecycle.py:483`
- `src/process_lifecycle.py:508`
- `src/process_lifecycle.py:525`
- `src/process_lifecycle.py:527`
- `tests/test_containment_process_tree.py:107`
- `tests/test_containment_process_tree.py:122`
- `tests/test_containment_process_tree.py:141`
- `static/js/chat.js:5482`
- `static/js/chatRenderer.js:2334`
- `static/js/cookbook.js:3186`

## `send` — function, line 1504
- **called from:**
- `src/process_lifecycle.py:478`
- `src/process_lifecycle.py:516`
- `tests/test_history_display_model_hydration.py:539`
- `tests/test_history_display_model_hydration.py:546`
- `tests/test_security_regressions.py:1397`
- `static/app.js:160`
- `static/app.js:161`
- `static/app.js:163`
- `static/app.js:166`
- `static/app.js:168`
- `static/app.js:4199`
- `static/js/chat.js:2615`
- `static/js/chat.js:8620`
- `static/js/chatRenderer.js:3147`
- `static/js/chatRenderer.js:3172`
- `static/js/chatRenderer.js:3174`
- `static/js/document.js:3663`

## `regate` — function, line 1530
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `reap_record` — function, line 1549
- **called from:**
- `src/bg_jobs.py:330`
- `src/bg_jobs.py:342`
- `src/process_reaper.py:120`
- `tests/test_containment_enforcement.py:163`
- `tests/test_orphan_reaping.py:100`
- `tests/test_orphan_reaping.py:124`
- `tests/test_orphan_reaping.py:138`
- `tests/test_orphan_reaping.py:159`
- `tests/test_orphan_reaping.py:177`
- `tests/test_orphan_reaping.py:188`
- `tests/test_orphan_reaping.py:240`

## `_release_awaited` — function (async), line 1590
- **called from:**
- `src/containment.py:1073`
- `src/containment.py:1101`
- `src/containment.py:1169`
- `tests/test_containment_enforcement.py:139`

## `_close_process_handles` — function, line 1601
- **called from:**
- `src/containment.py:1184`
- `src/containment.py:1598`

## `_release_awaited_impl` — function (async), line 1609
- **called from:**
- `src/containment.py:1596`

## `namespace_gone` — function, line 1647
- **called from:**
- `src/containment.py:1664`
- `src/containment.py:1681`

## `gone` — function, line 1657
- **called from:**
- `src/process_lifecycle.py:470`
- `src/process_lifecycle.py:481`
- `src/process_lifecycle.py:483`
- `src/process_lifecycle.py:508`
- `src/process_lifecycle.py:525`
- `src/process_lifecycle.py:527`
- `tests/test_containment_process_tree.py:107`
- `tests/test_containment_process_tree.py:122`
- `tests/test_containment_process_tree.py:141`
- `static/js/chat.js:5482`
- `static/js/chatRenderer.js:2334`
- `static/js/cookbook.js:3186`

## `send` — function, line 1665
- **called from:**
- `src/process_lifecycle.py:478`
- `src/process_lifecycle.py:516`
- `tests/test_history_display_model_hydration.py:539`
- `tests/test_history_display_model_hydration.py:546`
- `tests/test_security_regressions.py:1397`
- `static/app.js:160`
- `static/app.js:161`
- `static/app.js:163`
- `static/app.js:166`
- `static/app.js:168`
- `static/app.js:4199`
- `static/js/chat.js:2615`
- `static/js/chat.js:8620`
- `static/js/chatRenderer.js:3147`
- `static/js/chatRenderer.js:3172`
- `static/js/chatRenderer.js:3174`
- `static/js/document.js:3663`

## `_finish_release` — function, line 1687
- **called from:**
- `src/containment.py:1452`
- `src/containment.py:1473`
- `src/containment.py:1683`
- `tests/test_containment_enforcement.py:351`
