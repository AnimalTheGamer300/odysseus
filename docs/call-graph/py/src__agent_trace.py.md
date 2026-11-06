# `src/agent_trace.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `TraceKind` — class, line 19
- **called from:**
- `src/agent_trace.py:73`

## `CanonicalTraceEvent` — class, line 40
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/agent_trace.py:210`
- `src/agent_trace.py:564`
- `src/agent_trace.py:573`

## `CanonicalTraceEvent.to_dict` — method, line 54
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

## `CanonicalTraceEvent.from_dict` — method, line 60
- decorator: `classmethod`
- **called from:**
- `src/agent_runtime/authority.py:319`
- `src/agent_runtime/authority.py:320`
- `src/agent_runtime/authority.py:321`
- `src/agent_runtime/authority.py:322`
- `src/agent_runtime/authority.py:323`
- `src/agent_runtime/authority.py:324`
- `src/agent_runtime/authority.py:325`
- `src/agent_runtime/authority.py:689`
- `src/agent_runtime/authority.py:711`
- `src/agent_runtime/authority.py:714`
- `src/agent_runtime/effect_log.py:91`
- `src/agent_runtime/effects.py:277`
- `src/agent_runtime/effects.py:340`
- `src/agent_runtime/effects.py:341`
- `src/agent_runtime/effects.py:342`
- `src/agent_runtime/effects.py:343`
- `src/agent_runtime/effects.py:493`
- `src/agent_runtime/effects.py:576`
- `src/agent_runtime/process_resources.py:80`
- `src/agent_runtime/process_resources.py:89`
- `src/agent_runtime/process_resources.py:129`
- `src/agent_runtime/process_resources.py:475`
- `src/agent_runtime/resources.py:238`
- `src/agent_runtime/resources.py:275`
- `src/agent_runtime/resources.py:531`
- `src/agent_runtime/resources.py:570`
- `src/agent_runtime/resources.py:608`
- `src/agent_trace.py:124`
- `src/bg_jobs.py:227`
- `src/containment_worker.py:52`
- `src/containment_worker.py:53`
- `tests/test_background_resource_identity.py:54`
- `tests/test_background_resource_identity.py:65`
- `tests/test_background_resource_identity.py:187`
- `tests/test_background_resource_identity.py:191`
- `tests/test_browser_resource_identity.py:160`
- `tests/test_browser_resource_identity.py:321`
- `tests/test_effect_journal_persistence.py:43`
- `tests/test_effects_foundation.py:139`
- `tests/test_effects_foundation.py:141`
- `tests/test_effects_foundation.py:143`
- `tests/test_effects_foundation.py:160`
- `tests/test_model_capabilities.py:43`
- `tests/test_model_capabilities.py:83`
- `tests/test_owned_resource_identity.py:180`
- `tests/test_owned_resource_identity.py:322`
- `tests/test_owned_resource_identity.py:327`
- `tests/test_process_resource_identity.py:31`
- `tests/test_process_resource_identity.py:37`
- `tests/test_process_resource_identity.py:41`
- `tests/test_process_resource_identity.py:88`
- `tests/test_remote_resource_identity.py:68`
- `tests/test_remote_resource_identity.py:162`
- `tests/test_request_authority.py:115`
- `tests/test_resource_identity.py:379`
- `tests/test_resource_identity.py:393`
- `tests/test_resource_identity.py:660`
- `tests/test_resource_identity.py:683`
- `tests/test_runtime_resource_integration.py:416`
- `tests/test_wave3_launch_cost_lifecycle.py:102`
- … +1 more (grep the name in repo)

## `CanonicalTrace` — class, line 84
- **called from:**
- `src/agent_trace.py:233`

## `CanonicalTrace.__init__` — method, line 85
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

## `CanonicalTrace._validate` — method, line 92
- **called from:**
- `src/agent_trace.py:90`

## `CanonicalTrace.to_list` — method, line 103
- **called from:**
- `src/agent_loop.py:38903`
- `src/agent_runtime/completion.py:388`
- `src/agent_runtime/completion.py:389`
- `tests/test_agent_evidence.py:850`
- `tests/test_agent_trace.py:45`
- `tests/test_agent_trace.py:45`
- `tests/test_agent_trace.py:215`
- `tests/test_nested_invocation_ownership.py:117`
- `tests/test_nested_invocation_ownership.py:128`
- `tests/test_nested_invocation_ownership.py:132`
- `tests/test_runtime_evidence_contract.py:284`
- `tests/test_runtime_evidence_contract.py:284`

## `CanonicalTrace.write_jsonl` — method, line 106
- **called from:**
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:421`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:422`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:423`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:497`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:498`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:499`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:464`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:465`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:466`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:486`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:487`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:488`
- `scripts/build_odysseus_web_teacher_sft.py:437`
- `scripts/build_odysseus_web_teacher_sft.py:438`
- `scripts/build_odysseus_web_teacher_sft.py:439`
- `scripts/build_odysseus_web_v53_repair_sft.py:427`
- `scripts/build_odysseus_web_v53_repair_sft.py:428`
- `scripts/build_odysseus_web_v53_repair_sft.py:429`
- `scripts/curate_sft_trace_run.py:169`
- `scripts/run_sft_overnight_fixture_flows.py:706`
- `scripts/run_sft_overnight_fixture_flows.py:708`
- `tests/test_agent_trace.py:42`
- `tests/test_curate_sft_trace_run.py:102`

## `CanonicalTrace.read_jsonl` — method, line 117
- decorator: `classmethod`
- **called from:**
- `scripts/build_sft_expansion_manifest.py:49`
- `scripts/build_sft_expansion_manifest.py:59`
- `scripts/build_sft_expansion_manifest.py:79`
- `tests/test_agent_trace.py:43`
- `tests/test_agent_trace.py:220`

## `CanonicalTrace.summary` — method, line 131
- **called from:**
- `scripts/pr_blocker_audit.py:235`
- `tests/test_agent_trace.py:47`
- `tests/test_agent_trace.py:150`
- `tests/test_agent_trace.py:158`
- `tests/test_agent_trace.py:180`
- `static/js/emailLibrary/reader.js:643`

## `_TraceBuilder` — class, line 191
- **called from:**
- `src/agent_trace.py:294`
- `src/agent_trace.py:496`
- `src/agent_trace.py:601`

## `_TraceBuilder.__init__` — method, line 192
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

## `_TraceBuilder.add` — method, line 197
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3606`
- `routes/chat_routes.py:3707`
- `routes/chat_routes.py:3943`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2020 more (grep the name in repo)

## `_TraceBuilder.gap` — method, line 226
- **called from:**
- `src/agent_trace.py:312`
- `src/agent_trace.py:395`
- `src/agent_trace.py:462`
- `src/agent_trace.py:467`
- `src/agent_trace.py:562`
- `src/agent_trace.py:577`
- `src/agent_trace.py:625`

## `_TraceBuilder.build` — method, line 232
- **called from:**
- `scripts/dump_agent_prompt.py:424`
- `scripts/generate_env_reference.py:1232`
- `src/agent_runtime/effect_log.py:303`
- `src/agent_runtime/effect_log.py:330`
- `src/agent_trace.py:468`
- `src/agent_trace.py:578`
- `src/agent_trace.py:655`
- `src/model_capabilities.py:523`
- `src/model_capabilities.py:582`
- `src/model_capabilities.py:583`
- `src/model_capabilities.py:639`
- `src/model_capabilities.py:640`
- `src/model_capabilities.py:711`
- `src/model_capabilities.py:712`
- `src/model_capabilities.py:732`
- `src/model_capabilities.py:774`
- `src/model_capabilities.py:792`
- `src/model_capabilities.py:911`
- `src/model_capabilities.py:923`
- `src/model_capabilities.py:929`
- `src/model_capability_readers/base.py:259`
- `src/model_capability_readers/google_ai_studio_mapping.py:89`
- `src/model_capability_readers/llamacpp.py:172`
- `src/model_capability_readers/llamacpp.py:182`
- `tests/test_env_reference.py:37`
- `tests/test_model_capabilities.py:85`
- `tests/test_model_capabilities.py:107`
- `tests/test_model_capabilities.py:115`
- `tests/test_model_capabilities.py:116`
- `tests/test_model_capabilities.py:117`
- `tests/test_model_capabilities.py:118`
- `tests/test_model_capabilities.py:122`
- `tests/test_model_capabilities.py:129`
- `tests/test_model_capabilities.py:142`
- `tests/test_model_capabilities.py:165`
- `tests/test_model_capabilities.py:177`

## `_jsonable` — function, line 236
- **called from:**
- `src/agent_trace.py:238`
- `src/agent_trace.py:240`
- `src/agent_trace.py:250`
- `src/agent_trace.py:258`
- `src/agent_trace.py:309`
- `src/agent_trace.py:323`
- `src/agent_trace.py:420`
- `src/agent_trace.py:425`
- `src/agent_trace.py:436`
- `src/agent_trace.py:442`
- `src/agent_trace.py:444`
- `src/agent_trace.py:446`
- `src/agent_trace.py:459`
- `src/agent_trace.py:507`
- `src/agent_trace.py:516`
- `src/agent_trace.py:516`
- `src/agent_trace.py:526`
- `src/agent_trace.py:538`
- `src/agent_trace.py:540`
- `src/agent_trace.py:550`
- `src/agent_trace.py:552`
- `src/agent_trace.py:554`
- `src/agent_trace.py:557`
- `src/agent_trace.py:559`
- `src/agent_trace.py:561`
- `src/agent_trace.py:607`
- `src/agent_trace.py:613`
- `src/agent_trace.py:616`
- `src/agent_trace.py:629`
- `src/agent_trace.py:637`
- `src/agent_trace.py:639`
- `src/agent_trace.py:651`
- `src/agent_trace.py:752`

## `_command_from_arguments` — function, line 246
- **called from:**
- `src/agent_trace.py:522`
- `src/agent_trace.py:626`
- `src/agent_trace.py:669`

## `_exit_code` — function, line 261
- **called from:**
- `src/agent_trace.py:396`
- `src/agent_trace.py:531`
- `src/agent_trace.py:640`

## `_native_sse_payload` — function, line 272
- **called from:**
- `src/agent_trace.py:314`

## `decode_native_trace` — function, line 286
- **called from:**
- `src/agent_trace.py:488`
- `tests/test_agent_trace.py:41`
- `tests/test_agent_trace.py:51`
- `tests/test_agent_trace.py:80`
- `tests/test_agent_trace.py:154`
- `tests/test_agent_trace.py:162`
- `tests/test_agent_trace.py:191`
- `tests/test_agent_trace.py:214`
- `tests/test_agent_trace.py:246`
- `tests/test_agent_trace.py:271`
- `tests/test_agent_trace.py:295`

## `decode_native_trace_path` — function, line 471
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `decode_typed_trace` — function, line 491
- **called from:**
- `src/agent_trace.py:593`
- `tests/test_agent_trace.py:62`
- `tests/test_agent_trace.py:90`
- `tests/test_agent_trace.py:224`

## `decode_typed_trace_path` — function, line 581
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `decode_nemo_trajectory` — function, line 596
- **called from:**
- `tests/test_agent_trace.py:125`

## `tool_events_from_trace` — function, line 658
- **called from:**
- `src/agent_trace.py:683`
- `tests/test_agent_trace.py:240`

## `evidence_ledger_from_trace` — function, line 679
- **called from:**
- `src/agent_trace.py:693`

## `completion_from_trace` — function, line 686
- **called from:**
- `src/agent_trace.py:734`
- `tests/test_agent_trace.py:46`
- `tests/test_agent_trace.py:117`
- `tests/test_agent_trace.py:118`

## `audit_completion_trace` — function, line 699
- **called from:**
- `tests/test_agent_trace.py:263`
- `tests/test_agent_trace.py:289`
- `tests/test_agent_trace.py:300`
