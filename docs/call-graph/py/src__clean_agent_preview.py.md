# `src/clean_agent_preview.py` — definitions & call sites

196 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ProviderStreamError` — class, line 64
- **called from:**
- `src/clean_agent_preview.py:6708`

## `_schema_argument_hint` — function, line 104
- **called from:**
- `src/clean_agent_preview.py:8027`
- `tests/test_stream_error_redaction.py:263`
- `tests/test_stream_error_redaction.py:264`

## `_public_preview_tool_error` — function, line 139
- **called from:**
- `src/clean_agent_preview.py:8031`
- `tests/test_stream_error_redaction.py:208`
- `tests/test_stream_error_redaction.py:209`
- `tests/test_stream_error_redaction.py:220`

## `search_tool_choice_request` — function, line 282
- **called from:**
- `src/clean_agent_preview.py:6606`
- `tests/test_search_observation_budget.py:26`
- `tests/test_search_observation_budget.py:33`
- `tests/test_search_observation_budget.py:35`

## `provider_compatible_tool_choice_request` — function, line 301
- **called from:**
- `src/clean_agent_preview.py:6608`
- `tests/test_ajax_default_tools.py:14`
- `tests/test_ajax_default_tools.py:23`
- `tests/test_clean_agent_preview.py:111`
- `tests/test_clean_agent_preview.py:115`
- `tests/test_clean_agent_preview.py:123`
- `tests/test_clean_agent_preview.py:137`
- `tests/test_clean_agent_preview.py:150`

## `bounded_search_observation` — function, line 353
- **called from:**
- `src/agent_tools/web_tools.py:435`
- `src/agent_tools/web_tools_prewave3.py:439`
- `src/clean_agent_preview.py:415`

## `preview_tool_result_text` — function, line 358
- **called from:**
- `src/clean_agent_preview.py:8046`
- `src/clean_agent_preview.py:8073`
- `src/clean_agent_preview.py:8092`
- `tests/test_browser_observation.py:9`
- `tests/test_browser_observation.py:19`
- `tests/test_browser_observation.py:27`
- `tests/test_browser_observation.py:37`
- `tests/test_clean_agent_preview.py:1922`
- `tests/test_clean_agent_preview.py:4410`
- `tests/test_clean_agent_preview.py:4415`
- `tests/test_document_followup_integrity.py:174`
- `tests/test_editor_saved_observation.py:7`
- `tests/test_editor_saved_observation.py:17`
- `tests/test_preview_execution_evidence.py:19`
- `tests/test_preview_execution_evidence.py:27`
- `tests/test_preview_execution_evidence.py:32`
- `tests/test_preview_execution_evidence.py:39`
- `tests/test_search_observation_budget.py:166`
- `tests/test_search_observation_budget.py:177`
- `tests/test_search_observation_budget.py:226`
- `tests/test_search_observation_budget.py:231`
- `tests/test_web_search_metadata_mode.py:25`

## `canonical` — function, line 421
- **called from:**
- `routes/chat_routes.py:3969`
- `routes/chat_routes.py:3976`
- `routes/chat_routes.py:3986`
- `routes/chat_routes.py:3987`
- `routes/chat_routes.py:4035`
- `src/clean_agent_preview.py:303`
- `src/clean_agent_preview.py:360`
- `src/clean_agent_preview.py:364`
- `src/clean_agent_preview.py:383`
- `src/clean_agent_preview.py:399`
- `src/clean_agent_preview.py:404`
- `src/clean_agent_preview.py:414`
- `src/clean_agent_preview.py:427`
- `src/clean_agent_preview.py:441`
- `src/clean_agent_preview.py:464`
- `src/clean_agent_preview.py:501`
- `src/clean_agent_preview.py:508`
- `src/clean_agent_preview.py:518`
- `src/clean_agent_preview.py:528`
- `src/clean_agent_preview.py:534`
- `src/clean_agent_preview.py:1637`
- `src/clean_agent_preview.py:1806`
- `src/clean_agent_preview.py:1908`
- `src/clean_agent_preview.py:1954`
- `src/clean_agent_preview.py:2013`
- `src/clean_agent_preview.py:2057`
- `src/clean_agent_preview.py:2076`
- `src/clean_agent_preview.py:2333`
- `src/clean_agent_preview.py:2341`
- `src/clean_agent_preview.py:2357`
- `src/clean_agent_preview.py:2361`
- `src/clean_agent_preview.py:2374`
- `src/clean_agent_preview.py:2393`
- `src/clean_agent_preview.py:2462`
- `src/clean_agent_preview.py:2587`
- `src/clean_agent_preview.py:2670`
- `src/clean_agent_preview.py:2680`
- `src/clean_agent_preview.py:2995`
- `src/clean_agent_preview.py:3001`
- `src/clean_agent_preview.py:3019`
- `src/clean_agent_preview.py:3037`
- `src/clean_agent_preview.py:3044`
- `src/clean_agent_preview.py:3051`
- `src/clean_agent_preview.py:3076`
- `src/clean_agent_preview.py:3091`
- `src/clean_agent_preview.py:3105`
- `src/clean_agent_preview.py:3124`
- `src/clean_agent_preview.py:3160`
- `src/clean_agent_preview.py:3197`
- `src/clean_agent_preview.py:3199`
- `src/clean_agent_preview.py:3202`
- `src/clean_agent_preview.py:3210`
- `src/clean_agent_preview.py:3230`
- `src/clean_agent_preview.py:3233`
- `src/clean_agent_preview.py:3236`
- `src/clean_agent_preview.py:3240`
- `src/clean_agent_preview.py:3257`
- `src/clean_agent_preview.py:3264`
- `src/clean_agent_preview.py:3272`
- `src/clean_agent_preview.py:3277`
- … +142 more (grep the name in repo)

## `editor_batch_continues` — function, line 425
- **called from:**
- `src/clean_agent_preview.py:381`
- `src/clean_agent_preview.py:391`
- `src/clean_agent_preview.py:7946`
- `tests/test_editor_writing_action_routing.py:298`
- `tests/test_editor_writing_action_routing.py:299`
- `tests/test_editor_writing_action_routing.py:300`
- `tests/test_editor_writing_action_routing.py:301`
- `tests/test_editor_writing_action_routing.py:302`
- `tests/test_editor_writing_action_routing.py:303`

## `drop_redundant_editor_noops` — function, line 434
- **called from:**
- `src/clean_agent_preview.py:6890`
- `tests/test_editor_writing_action_routing.py:313`
- `tests/test_editor_writing_action_routing.py:314`
- `tests/test_editor_writing_action_routing.py:315`

## `semantic_repeat_scope` — function, line 462
- **called from:**
- `src/clean_agent_preview.py:7668`
- `tests/test_clean_agent_preview.py:7051`
- `tests/test_clean_agent_preview.py:7054`
- `tests/test_clean_agent_preview.py:7059`
- `tests/test_clean_agent_preview.py:7062`

## `shell_native_tool_misuse` — function, line 497
- **called from:**
- `src/clean_agent_preview.py:8049`
- `tests/test_clean_agent_preview.py:7005`
- `tests/test_clean_agent_preview.py:7006`
- `tests/test_clean_agent_preview.py:7007`

## `shell_native_tool_command_misuse` — function, line 514
- **called from:**
- `src/clean_agent_preview.py:7654`
- `tests/test_clean_agent_preview.py:7018`
- `tests/test_clean_agent_preview.py:7021`
- `tests/test_clean_agent_preview.py:7024`

## `shell_sensitive_command_error` — function, line 538
- **called from:**
- `src/clean_agent_preview.py:7647`
- `tests/test_clean_agent_preview.py:7031`
- `tests/test_clean_agent_preview.py:7034`
- `tests/test_clean_agent_preview.py:7035`

## `masked_shell_pipeline_failure` — function, line 559
- **called from:**
- `src/clean_agent_preview.py:8063`
- `tests/test_clean_agent_preview.py:7041`

## `offered_tool_alias` — function, line 591
- **called from:**
- `src/clean_agent_preview.py:7393`
- `src/clean_agent_preview.py:7476`
- `tests/test_clean_agent_preview.py:42`
- `tests/test_clean_agent_preview.py:43`

## `browser_observation_state` — function, line 602
- **called from:**
- `src/clean_agent_preview.py:640`
- `tests/test_browser_progress.py:39`
- `tests/test_browser_progress.py:39`
- `tests/test_browser_progress.py:40`

## `visit` — function, line 605
- **called from:**
- `src/browser_observation.py:12`
- `src/browser_observation.py:34`
- `src/browser_observation.py:44`
- `src/browser_observation.py:49`
- `src/browser_observation.py:53`
- `src/clean_agent_preview.py:608`
- `src/clean_agent_preview.py:615`
- `src/clean_agent_preview.py:626`
- `src/clean_agent_preview.py:628`
- `static/js/editor/layer-groups.js:127`
- `static/js/editor/layer-groups.js:129`
- `static/js/gallery.js:2293`

## `BrowserProgress` — class, line 632
- **called from:**
- `src/clean_agent_preview.py:5881`
- `tests/test_browser_progress.py:13`
- `tests/test_browser_progress.py:22`
- `tests/test_browser_progress.py:29`
- `tests/test_browser_progress.py:44`

## `BrowserProgress.__init__` — method, line 634
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

## `BrowserProgress.observe` — method, line 639
- **called from:**
- `src/agent_runtime/effect_adapters.py:371`
- `src/agent_runtime/process_resources.py:63`
- `src/agent_runtime/resources.py:321`
- `src/agent_runtime/resources.py:325`
- `src/agent_runtime/resources.py:400`
- `src/agent_runtime/resources.py:406`
- `src/agent_runtime/resources.py:519`
- `src/agent_tools/web_tools.py:2457`
- `src/agent_tools/web_tools.py:2500`
- `src/agent_tools/web_tools_prewave3.py:2466`
- `src/agent_tools/web_tools_prewave3.py:2509`
- `src/browser_identity.py:288`
- `src/browser_lifecycle.py:155`
- `src/clean_agent_preview.py:7902`
- `tests/test_browser_progress.py:14`
- `tests/test_browser_progress.py:16`
- `tests/test_browser_progress.py:17`
- `tests/test_browser_progress.py:18`
- `tests/test_browser_progress.py:25`
- `tests/test_browser_progress.py:31`
- `tests/test_browser_progress.py:32`
- `tests/test_browser_progress.py:33`
- `tests/test_browser_progress.py:34`
- `tests/test_browser_progress.py:35`
- `tests/test_browser_progress.py:46`
- `tests/test_effect_journal_persistence.py:75`
- `tests/test_effect_journal_persistence.py:140`
- `tests/test_effect_verification_adapters.py:368`
- `tests/test_effects_foundation.py:216`
- `tests/test_effects_foundation.py:229`
- `tests/test_effects_foundation.py:238`
- `tests/test_effects_foundation.py:240`
- `tests/test_effects_foundation.py:247`
- `tests/test_effects_foundation.py:257`
- `tests/test_effects_foundation.py:268`
- `tests/test_effects_foundation.py:283`
- `tests/test_effects_foundation.py:293`
- `tests/test_effects_foundation.py:304`
- `tests/test_effects_foundation.py:316`
- `tests/test_effects_foundation.py:327`
- `tests/test_effects_foundation.py:330`
- `tests/test_effects_foundation.py:341`
- `tests/test_effects_foundation.py:342`
- `tests/test_effects_foundation.py:349`
- `tests/test_effects_foundation.py:358`
- `tests/test_effects_foundation.py:360`
- `tests/test_effects_foundation.py:369`
- `tests/test_effects_foundation.py:380`
- `tests/test_effects_foundation.py:393`
- `tests/test_effects_foundation.py:411`
- `tests/test_effects_foundation.py:422`
- `tests/test_effects_foundation.py:427`
- `tests/test_effects_foundation.py:450`
- `tests/test_effects_foundation.py:451`
- `tests/test_process_lifecycle.py:320`
- `tests/test_process_lifecycle.py:326`
- `tests/test_process_lifecycle.py:331`
- `tests/test_process_lifecycle.py:340`
- `tests/test_resource_identity.py:62`
- `static/app.js:336`
- … +99 more (grep the name in repo)

## `private_browser_state_transition` — function, line 666
- **called from:**
- `src/clean_agent_preview.py:704`
- `src/clean_agent_preview.py:7898`
- `tests/test_clean_agent_preview.py:159`
- `tests/test_clean_agent_preview.py:161`
- `tests/test_clean_agent_preview.py:163`
- `tests/test_clean_agent_preview.py:170`
- `tests/test_clean_agent_preview.py:173`
- `tests/test_clean_agent_preview.py:176`
- `tests/test_clean_agent_preview.py:179`
- `tests/test_clean_agent_preview.py:194`

## `private_browser_success_repeat_limit` — function, line 710
- **called from:**
- `src/clean_agent_preview.py:7729`
- `tests/test_clean_agent_preview.py:186`
- `tests/test_clean_agent_preview.py:187`
- `tests/test_clean_agent_preview.py:190`

## `email_account_backend_unavailable` — function, line 731
- **called from:**
- `src/clean_agent_preview.py:7923`
- `tests/test_minimal_native_tool_prompt.py:380`
- `tests/test_minimal_native_tool_prompt.py:387`

## `requested_item_limit` — function, line 742
- **called from:**
- `src/clean_agent_preview.py:821`
- `src/clean_agent_preview.py:1034`
- `src/clean_agent_preview.py:1046`
- `src/clean_agent_preview.py:1080`
- `src/clean_agent_preview.py:1112`
- `src/clean_agent_preview.py:1215`
- `src/clean_agent_preview.py:1269`
- `src/clean_agent_preview.py:1322`
- `src/clean_agent_preview.py:1378`
- `src/clean_agent_preview.py:1764`
- `src/clean_agent_preview.py:1867`
- `src/clean_agent_preview.py:8509`
- `tests/test_clean_agent_preview.py:1779`
- `tests/test_clean_agent_preview.py:1780`
- `tests/test_clean_agent_preview.py:1781`
- `tests/test_clean_agent_preview.py:1782`
- `tests/test_clean_agent_preview.py:1783`
- `tests/test_clean_agent_preview.py:1784`
- `tests/test_clean_agent_preview.py:1785`
- `tests/test_clean_agent_preview.py:1786`
- `tests/test_clean_agent_preview.py:1787`
- `tests/test_clean_agent_preview.py:1788`
- `tests/test_clean_agent_preview.py:1789`
- `tests/test_clean_agent_preview.py:1790`
- `tests/test_clean_agent_preview.py:1791`
- `tests/test_clean_agent_preview.py:1794`
- `tests/test_clean_agent_preview.py:1798`
- `tests/test_clean_agent_preview.py:1799`
- `tests/test_clean_agent_preview.py:1800`
- `tests/test_clean_agent_preview.py:1804`
- `tests/test_clean_agent_preview.py:1805`
- `tests/test_clean_agent_preview.py:1808`
- `tests/test_clean_agent_preview.py:1809`
- `tests/test_clean_agent_preview.py:1810`
- `tests/test_clean_agent_preview.py:1811`
- `tests/test_clean_agent_preview.py:1812`
- `tests/test_clean_agent_preview.py:1815`
- `tests/test_clean_agent_preview.py:1816`
- `tests/test_clean_agent_preview.py:1819`
- `tests/test_clean_agent_preview.py:1822`

## `contract_item_limit` — function, line 813
- **called from:**
- `src/clean_agent_preview.py:8582`
- `src/clean_agent_preview.py:8607`
- `src/clean_agent_preview.py:8641`
- `src/clean_agent_preview.py:8685`
- `src/clean_agent_preview.py:8696`
- `src/clean_agent_preview.py:8716`
- `tests/test_clean_agent_preview.py:2063`
- `tests/test_clean_agent_preview.py:2064`

## `_bounded_structured_list` — function, line 819
- **called from:**
- `src/clean_agent_preview.py:1038`
- `src/clean_agent_preview.py:1048`
- `src/clean_agent_preview.py:1217`

## `align_structured_tool_history` — function, line 826
- **called from:**
- `src/clean_agent_preview.py:8957`
- `tests/test_clean_agent_preview.py:1911`

## `_partial_json_string_field` — function, line 836
- **called from:**
- `src/clean_agent_preview.py:890`
- `src/clean_agent_preview.py:1031`
- `src/clean_agent_preview.py:6757`
- `src/clean_agent_preview.py:6761`
- `src/clean_agent_preview.py:6762`

## `explicit_text_artifact_target` — function, line 876
- **called from:**
- `src/clean_agent_preview.py:898`

## `malformed_write_handoff_target` — function, line 887
- **called from:**
- `src/clean_agent_preview.py:8013`
- `tests/test_clean_agent_preview.py:1143`
- `tests/test_clean_agent_preview.py:1147`

## `_listing_allowed` — function, line 914
- **called from:**
- `src/clean_agent_preview.py:922`
- `src/clean_agent_preview.py:934`
- `src/clean_agent_preview.py:962`

## `_allowed_then_space` — function, line 918
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_space_then_allowed` — function, line 928
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_page_listing_request` — function, line 939
- **called from:**
- `src/clean_agent_preview.py:999`
- `tests/test_redos_core_parsers.py:497`
- `tests/test_redos_core_parsers.py:503`
- `tests/test_redos_core_parsers.py:578`

## `page_listing_response` — function, line 997
- **called from:**
- `src/clean_agent_preview.py:8507`
- `tests/test_search_content_extraction_parity.py:86`
- `tests/test_search_content_extraction_parity.py:89`
- `tests/test_search_content_extraction_parity.py:90`
- `tests/test_search_content_extraction_parity.py:91`

## `calendar_terminal_response` — function, line 1019
- **called from:**
- `src/clean_agent_preview.py:8580`
- `tests/test_clean_agent_preview.py:1837`
- `tests/test_clean_agent_preview.py:1854`

## `notes_terminal_response` — function, line 1041
- **called from:**
- `src/clean_agent_preview.py:1056`
- `src/clean_agent_preview.py:8605`
- `tests/test_clean_agent_preview.py:447`
- `tests/test_clean_agent_preview.py:1826`

## `note_locator_followup` — function, line 1051
- **called from:**
- `src/clean_agent_preview.py:8609`

## `documents_terminal_response` — function, line 1067
- **called from:**
- `src/clean_agent_preview.py:8639`
- `tests/test_clean_agent_preview.py:2414`

## `shell_listing_terminal_response` — function, line 1084
- **called from:**
- `src/clean_agent_preview.py:8649`
- `tests/test_clean_agent_preview.py:2420`
- `tests/test_clean_agent_preview.py:2427`

## `shell_output_terminal_response` — function, line 1119
- **called from:**
- `src/clean_agent_preview.py:8653`
- `tests/test_clean_agent_preview.py:2460`
- `tests/test_clean_agent_preview.py:2461`
- `tests/test_clean_agent_preview.py:2465`
- `tests/test_clean_agent_preview.py:2466`

## `direct_shell_output_request` — function, line 1134
- **called from:**
- `src/clean_agent_preview.py:8652`
- `tests/test_clean_agent_preview.py:2434`
- `tests/test_clean_agent_preview.py:2435`
- `tests/test_clean_agent_preview.py:2436`

## `ui_panel_terminal_response` — function, line 1147
- **called from:**
- `src/clean_agent_preview.py:8673`
- `tests/test_clean_agent_preview.py:2564`
- `tests/test_clean_agent_preview.py:2567`
- `tests/test_clean_agent_preview.py:2574`
- `tests/test_clean_agent_preview.py:2578`
- `tests/test_clean_agent_preview.py:2582`
- `tests/test_clean_agent_preview.py:2589`
- `tests/test_clean_agent_preview.py:2592`

## `ui_toggle_state_result` — function, line 1178
- **called from:**
- `src/clean_agent_preview.py:7886`
- `tests/test_clean_agent_preview.py:2586`

## `memory_terminal_response` — function, line 1203
- **called from:**
- `src/clean_agent_preview.py:8683`
- `tests/test_clean_agent_preview.py:1878`

## `tasks_terminal_response` — function, line 1220
- **called from:**
- `src/clean_agent_preview.py:8694`
- `tests/test_clean_agent_preview.py:1867`
- `tests/test_clean_agent_preview.py:1896`
- `tests/test_clean_agent_preview.py:2357`
- `tests/test_clean_agent_preview.py:2359`
- `tests/test_clean_agent_preview.py:2362`
- `tests/test_clean_agent_preview.py:2373`
- `tests/test_clean_agent_preview.py:2376`
- `tests/test_redos_agent_preview_parsers.py:66`

## `task_list_requires_synthesis` — function, line 1289
- **called from:**
- `src/clean_agent_preview.py:8698`
- `tests/test_clean_agent_preview.py:1614`
- `tests/test_clean_agent_preview.py:1618`

## `skills_terminal_response` — function, line 1300
- **called from:**
- `src/clean_agent_preview.py:8714`
- `tests/test_clean_agent_preview.py:2385`
- `tests/test_clean_agent_preview.py:2400`
- `tests/test_redos_agent_preview_parsers.py:83`
- `tests/test_redos_agent_preview_parsers.py:91`

## `skill_name` — function, line 1304
- **called from:**
- `src/clean_agent_preview.py:1330`
- `src/clean_agent_preview.py:1362`

## `cookbook_servers_terminal_response` — function, line 1369
- **called from:**
- `src/clean_agent_preview.py:1962`
- `src/clean_agent_preview.py:8724`
- `tests/test_clean_agent_preview.py:1886`
- `tests/test_clean_agent_preview.py:2599`

## `contentless_final_response` — function, line 1389
- **called from:**
- `src/clean_agent_preview.py:7042`
- `tests/test_clean_agent_preview.py:2608`
- `tests/test_clean_agent_preview.py:2609`
- `tests/test_clean_agent_preview.py:2610`

## `action_promise_response` — function, line 1399
- **called from:**
- `src/clean_agent_preview.py:7062`
- `tests/test_clean_agent_preview.py:771`
- `tests/test_clean_agent_preview.py:774`
- `tests/test_clean_agent_preview.py:777`
- `tests/test_clean_agent_preview.py:780`
- `tests/test_clean_agent_preview.py:7488`
- `tests/test_clean_agent_preview.py:7490`
- `tests/test_clean_agent_preview.py:7491`
- `tests/test_clean_agent_preview.py:7492`
- `tests/test_clean_agent_preview.py:7495`
- `tests/test_clean_agent_preview.py:7501`

## `broad_current_web_request` — function, line 1424
- **called from:**
- `src/clean_agent_preview.py:1431`
- `src/clean_agent_preview.py:5941`
- `src/clean_agent_preview.py:5957`
- `tests/test_clean_agent_preview.py:3026`

## `incomplete_broad_web_answer` — function, line 1429
- **called from:**
- `src/clean_agent_preview.py:7109`
- `tests/test_clean_agent_preview.py:3033`
- `tests/test_clean_agent_preview.py:3034`
- `tests/test_clean_agent_preview.py:3037`
- `tests/test_clean_agent_preview.py:3045`
- `tests/test_clean_agent_preview.py:3046`

## `progressive_thinking_for_turn` — function, line 1440
- **called from:**
- `src/clean_agent_preview.py:5698`
- `tests/test_clean_agent_preview.py:4718`
- `tests/test_clean_agent_preview.py:4719`
- `tests/test_preview_drafting_recovery.py:16`
- `tests/test_preview_drafting_recovery.py:17`

## `spec_router_thinking_decision` — function, line 1448
- **called from:**
- `tests/test_clean_agent_preview.py:7358`
- `tests/test_clean_agent_preview.py:7367`
- `tests/test_clean_agent_preview.py:7374`
- `tests/test_clean_agent_preview.py:7386`

## `spec_router_thinking_decision_async` — function (async), line 1469
- **called from:**
- `src/clean_agent_preview.py:6134`

## `spec_router_think_reason` — function, line 1492
- **called from:**
- `tests/test_clean_agent_preview.py:7359`
- `tests/test_clean_agent_preview.py:7376`
- `tests/test_clean_agent_preview.py:7378`
- `tests/test_clean_agent_preview.py:7379`
- `tests/test_clean_agent_preview.py:7380`
- `tests/test_clean_agent_preview.py:7387`

## `spec_direct_mode` — function, line 1501
- **called from:**
- `src/clean_agent_preview.py:6152`
- `tests/test_spec_direct_notools.py:171`
- `tests/test_spec_direct_notools.py:173`
- `tests/test_spec_direct_notools.py:175`

## `spec_direct_no_tools_p` — function, line 1514
- **called from:**
- `src/clean_agent_preview.py:6145`
- `tests/test_clean_agent_preview.py:7413`
- `tests/test_clean_agent_preview.py:7418`
- `tests/test_clean_agent_preview.py:7424`
- `tests/test_clean_agent_preview.py:7428`
- `tests/test_clean_agent_preview.py:7435`
- `tests/test_clean_agent_preview.py:7442`
- `tests/test_clean_agent_preview.py:7452`
- `tests/test_clean_agent_preview.py:7464`
- `tests/test_spec_router_request_scope.py:38`
- `tests/test_spec_router_request_scope.py:71`

## `spec_driver_active` — function, line 1559
- **called from:**
- `src/clean_agent_preview.py:5635`
- `tests/test_spec_driver_mode.py:122`
- `tests/test_spec_driver_mode.py:124`
- `tests/test_spec_driver_mode.py:129`

## `spec_driver_pick` — function, line 1571
- **called from:**
- `src/clean_agent_preview.py:6514`
- `tests/test_spec_driver_mode.py:139`
- `tests/test_spec_driver_mode.py:147`
- `tests/test_spec_driver_mode.py:155`
- `tests/test_spec_driver_mode.py:163`
- `tests/test_spec_driver_mode.py:168`

## `tool_deliberation_reason` — function, line 1635
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `visible_content_after_qwen_thinking` — function, line 1652
- **called from:**
- `src/clean_agent_preview.py:6790`

## `qwen_think_split_events` — function, line 1667
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `prior_short_answer_for_no_tool_summary` — function, line 1709
- **called from:**
- `src/clean_agent_preview.py:5979`
- `tests/test_clean_agent_preview.py:2530`
- `tests/test_clean_agent_preview.py:2538`
- `tests/test_clean_agent_preview.py:2619`
- `tests/test_clean_agent_preview.py:2622`

## `prior_collection_repeat_answer` — function, line 1735
- **called from:**
- `src/clean_agent_preview.py:5980`
- `tests/test_clean_agent_preview.py:289`
- `tests/test_clean_agent_preview.py:2635`
- `tests/test_clean_agent_preview.py:2639`
- `tests/test_clean_agent_preview.py:2652`
- `tests/test_clean_agent_preview.py:2674`
- `tests/test_clean_agent_preview.py:2695`
- `tests/test_clean_agent_preview.py:2715`
- `tests/test_clean_agent_preview.py:2734`
- `tests/test_clean_agent_preview.py:2736`
- `tests/test_clean_agent_preview.py:2749`
- `tests/test_clean_agent_preview.py:2768`
- `tests/test_clean_agent_preview.py:2786`
- `tests/test_clean_agent_preview.py:2803`

## `prior_failed_operation_answer` — function, line 1886
- **called from:**
- `src/clean_agent_preview.py:5981`
- `tests/test_clean_agent_preview.py:2825`
- `tests/test_clean_agent_preview.py:2828`
- `tests/test_clean_agent_preview.py:2841`

## `prior_cookbook_server_answer` — function, line 1933
- **called from:**
- `src/clean_agent_preview.py:5982`
- `tests/test_clean_agent_preview.py:2855`
- `tests/test_clean_agent_preview.py:2858`
- `tests/test_clean_agent_preview.py:2860`

## `prior_workspace_path_answer` — function, line 1965
- **called from:**
- `src/clean_agent_preview.py:5983`
- `tests/test_clean_agent_preview.py:2446`

## `_prior_web_source_request` — function, line 1986
- **called from:**
- `src/clean_agent_preview.py:2003`
- `tests/test_redos_core_parsers.py:579`

## `prior_web_source_answer` — function, line 2000
- **called from:**
- `src/clean_agent_preview.py:5984`
- `tests/test_clean_agent_preview.py:2523`

## `bounded_web_evidence_answer` — function, line 2029
- **called from:**
- `src/clean_agent_preview.py:8837`
- `tests/test_clean_agent_preview.py:3052`

## `email_reader_event` — function, line 2055
- **called from:**
- `src/clean_agent_preview.py:8393`
- `tests/test_email_reader_handoff.py:11`
- `tests/test_email_reader_handoff.py:17`
- `tests/test_email_reader_handoff.py:21`
- `tests/test_email_reader_handoff.py:22`
- `tests/test_email_reader_handoff.py:23`

## `email_draft_document_id` — function, line 2074
- **called from:**
- `src/clean_agent_preview.py:8396`
- `tests/test_compact_email_editor.py:12`
- `tests/test_compact_email_editor.py:13`
- `tests/test_compact_email_editor.py:14`
- `tests/test_compact_email_editor.py:15`

## `document_suggestions_event` — function, line 2086
- **called from:**
- `src/clean_agent_preview.py:8323`
- `tests/test_clean_agent_preview.py:469`
- `tests/test_clean_agent_preview.py:472`
- `tests/test_clean_agent_preview.py:475`

## `preview_http_timeout` — function, line 2100
- **called from:**
- `src/clean_agent_preview.py:6053`
- `tests/test_clean_v3_native_workspace.py:122`
- `tests/test_clean_v3_native_workspace.py:123`
- `tests/test_clean_v3_native_workspace.py:124`

## `preview_http_limits` — function, line 2106
- **called from:**
- `src/clean_agent_preview.py:6056`
- `tests/test_clean_agent_preview.py:6871`

## `native_execution_limits` — function, line 2118
- **called from:**
- `src/clean_agent_preview.py:6007`
- `tests/test_clean_agent_preview.py:379`
- `tests/test_clean_agent_preview.py:380`
- `tests/test_clean_agent_preview.py:381`

## `native_artifact_completion_timing` — function, line 2127
- **called from:**
- `src/clean_agent_preview.py:5708`

## `standalone_social_turn` — function, line 2150
- **called from:**
- `src/clean_agent_preview.py:5682`
- `tests/test_clean_agent_preview.py:422`

## `interactive_execution_limit` — function, line 2158
- **called from:**
- `src/clean_agent_preview.py:5994`
- `tests/test_clean_agent_preview.py:387`
- `tests/test_clean_agent_preview.py:388`
- `tests/test_clean_agent_preview.py:389`
- `tests/test_clean_agent_preview.py:391`
- `tests/test_clean_agent_preview.py:392`

## `interactive_tool_call_limit` — function, line 2174
- **called from:**
- `src/clean_agent_preview.py:5995`
- `tests/test_clean_agent_preview.py:403`
- `tests/test_clean_agent_preview.py:404`
- `tests/test_clean_agent_preview.py:406`
- `tests/test_clean_agent_preview.py:407`
- `tests/test_clean_agent_preview.py:409`
- `tests/test_clean_agent_preview.py:410`

## `runtime_required_artifacts` — function, line 2194
- **called from:**
- `src/clean_agent_preview.py:6008`
- `tests/test_clean_agent_preview.py:492`
- `tests/test_clean_agent_preview.py:1403`
- `tests/test_clean_agent_preview.py:1410`
- `tests/test_clean_agent_preview.py:1413`
- `tests/test_clean_agent_preview.py:1419`
- `tests/test_clean_agent_preview.py:1426`

## `execution_targets_required_artifact` — function, line 2216
- **called from:**
- `src/clean_agent_preview.py:2279`
- `tests/test_clean_agent_preview.py:1452`
- `tests/test_clean_agent_preview.py:1455`
- `tests/test_clean_agent_preview.py:1458`
- `tests/test_clean_agent_preview.py:1461`

## `required_artifacts_have_content` — function, line 2225
- **called from:**
- `src/clean_agent_preview.py:2275`
- `tests/test_clean_agent_preview.py:505`
- `tests/test_clean_agent_preview.py:518`
- `tests/test_clean_agent_preview.py:519`
- `tests/test_clean_agent_preview.py:520`

## `successful_required_artifact_mutation` — function, line 2257
- **called from:**
- `src/clean_agent_preview.py:7973`
- `tests/test_clean_agent_preview.py:528`
- `tests/test_clean_agent_preview.py:532`
- `tests/test_clean_agent_preview.py:538`

## `artifact_completion_python_code_error` — function, line 2282
- **called from:**
- `src/clean_agent_preview.py:7815`
- `tests/test_clean_agent_preview.py:701`
- `tests/test_clean_agent_preview.py:704`
- `tests/test_clean_agent_preview.py:707`

## `artifact_completion_tool_schemas` — function, line 2313
- **called from:**
- `src/clean_agent_preview.py:6322`
- `src/clean_agent_preview.py:8851`
- `tests/test_clean_agent_preview.py:646`
- `tests/test_clean_agent_preview.py:680`
- `tests/test_clean_agent_preview.py:693`
- `tests/test_clean_agent_preview.py:739`

## `required_artifact_completion_tool_choice` — function, line 2387
- **called from:**
- `src/clean_agent_preview.py:6367`
- `tests/test_clean_agent_preview.py:730`
- `tests/test_clean_agent_preview.py:733`
- `tests/test_clean_agent_preview.py:736`
- `tests/test_clean_agent_preview.py:759`
- `tests/test_clean_agent_preview.py:763`

## `repeated_off_contract_artifact_handoff_target` — function, line 2419
- **called from:**
- `src/clean_agent_preview.py:6938`
- `src/clean_agent_preview.py:7994`
- `tests/test_clean_agent_preview.py:788`
- `tests/test_clean_agent_preview.py:795`
- `tests/test_clean_agent_preview.py:801`
- `tests/test_clean_agent_preview.py:807`

## `protocol_safe_tool_calls` — function, line 2435
- **called from:**
- `src/clean_agent_preview.py:6934`
- `tests/test_browser_transport_recovery.py:124`
- `tests/test_clean_v3_native_workspace.py:134`

## `expand_concatenated_write_calls` — function, line 2448
- **called from:**
- `src/clean_agent_preview.py:6878`
- `tests/test_clean_agent_preview.py:1104`
- `tests/test_clean_agent_preview.py:1105`
- `tests/test_clean_agent_preview.py:1132`

## `artifact_body_from_handoff` — function, line 2559
- **called from:**
- `src/clean_agent_preview.py:7140`

## `artifact_body_matches_target` — function, line 2566
- **called from:**
- `src/clean_agent_preview.py:7141`

## `tool_family` — function, line 2586
- **called from:**
- `scripts/audit_historical_tool_routing.py:50`
- `src/clean_agent_preview.py:3781`
- `src/clean_agent_preview.py:3814`

## `authorized_write_families` — function, line 2600
- **called from:**
- `src/clean_agent_preview.py:3875`
- `src/clean_agent_preview.py:3992`
- `src/clean_agent_preview.py:4655`
- `tests/test_clean_agent_preview.py:3651`
- `tests/test_clean_agent_preview.py:3834`
- `tests/test_clean_agent_preview.py:3839`
- `tests/test_creation_container_routing.py:30`
- `tests/test_creation_container_routing.py:35`
- `tests/test_creation_container_routing.py:40`
- `tests/test_search_observation_budget.py:70`

## `canonical_tools_for_mode` — function, line 2637
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `contract_builder` — function, line 2642
- decorator: `lru_cache(maxsize=1)`
- **called from:**
- `scripts/test_clean_tool_loop.py:33`
- `src/clean_agent_preview.py:2667`

## `compact_schemas` — function, line 2664
- **called from:**
- `scripts/eval_ajax_basic_tools.py:37`
- `src/clean_agent_preview.py:5680`
- `tests/test_ajax_default_tools.py:30`
- `tests/test_ajax_default_tools.py:38`
- `tests/test_clawmm_r44_pdf_visual_recovery.py:8`
- `tests/test_clean_agent_preview.py:212`
- `tests/test_clean_agent_preview.py:220`
- `tests/test_clean_agent_preview.py:229`
- `tests/test_clean_agent_preview.py:240`
- `tests/test_clean_agent_preview.py:267`
- `tests/test_clean_agent_preview.py:358`
- `tests/test_clean_agent_preview.py:1444`
- `tests/test_clean_agent_preview.py:1654`
- `tests/test_clean_agent_preview.py:3236`
- `tests/test_clean_agent_preview.py:3521`
- `tests/test_clean_agent_preview.py:4307`
- `tests/test_clean_agent_preview.py:4325`
- `tests/test_clean_agent_preview.py:4342`
- `tests/test_clean_agent_preview.py:4370`
- `tests/test_clean_agent_preview.py:4380`
- `tests/test_clean_agent_preview.py:4389`
- `tests/test_clean_agent_preview.py:4398`
- `tests/test_clean_agent_preview.py:4439`
- `tests/test_clean_agent_preview.py:4446`
- `tests/test_clean_agent_preview.py:4455`
- `tests/test_code_editor_routing.py:31`
- `tests/test_compact_calendar_create.py:15`
- `tests/test_compact_todo_notes.py:15`
- `tests/test_editor_writing_action_routing.py:287`
- `tests/test_email_attachment_text.py:59`
- `tests/test_image_creation_routing.py:11`
- `tests/test_manage_tasks_cron.py:67`
- `tests/test_preview_drafting_recovery.py:26`
- `tests/test_research_chat_runtime.py:30`

## `normalize_preview_entity_anchor_args` — function, line 2982
- **called from:**
- `src/clean_agent_preview.py:3018`
- `src/clean_agent_preview.py:3165`

## `normalize_preview_function_args` — function, line 3016
- **called from:**
- `src/clean_agent_preview.py:3168`
- `tests/test_clean_agent_preview.py:258`
- `tests/test_clean_agent_preview.py:463`
- `tests/test_clean_agent_preview.py:1559`
- `tests/test_clean_agent_preview.py:1565`
- `tests/test_clean_agent_preview.py:1571`
- `tests/test_clean_agent_preview.py:1584`
- `tests/test_clean_agent_preview.py:1596`
- `tests/test_clean_agent_preview.py:2452`
- `tests/test_clean_agent_preview.py:2924`
- `tests/test_clean_agent_preview.py:3141`
- `tests/test_clean_agent_preview.py:3246`
- `tests/test_clean_agent_preview.py:3258`
- `tests/test_clean_agent_preview.py:3267`
- `tests/test_clean_agent_preview.py:3276`
- `tests/test_clean_agent_preview.py:3388`
- `tests/test_clean_agent_preview.py:3396`
- `tests/test_clean_agent_preview.py:3410`
- `tests/test_clean_agent_preview.py:4359`
- `tests/test_web_fetch_batch.py:134`

## `normalize_preview_call_args` — function, line 3151
- **called from:**
- `src/clean_agent_preview.py:7397`
- `src/clean_agent_preview.py:7493`
- `tests/test_clean_agent_preview.py:296`
- `tests/test_clean_agent_preview.py:306`
- `tests/test_editor_writing_action_routing.py:96`
- `tests/test_editor_writing_action_routing.py:265`

## `private_browser_dom_batch` — function, line 3171
- **called from:**
- `tests/test_clean_agent_preview.py:3420`
- `tests/test_clean_agent_preview.py:3424`

## `scope_preview_contract` — function, line 3186
- **called from:**
- `routes/chat_routes.py:3989`
- `tests/test_clean_agent_preview.py:4478`
- `tests/test_clean_agent_preview.py:4488`
- `tests/test_clean_agent_preview.py:4505`
- `tests/test_clean_agent_preview.py:4528`
- `tests/test_clean_agent_preview.py:4550`
- `tests/test_clean_v3_native_workspace.py:91`
- `tests/test_clean_v3_native_workspace.py:148`
- `tests/test_clean_v3_native_workspace.py:165`
- `tests/test_compact_core_contract_path.py:23`
- `tests/test_image_creation_routing.py:55`
- `tests/test_image_creation_routing.py:66`
- `tests/test_image_creation_routing.py:111`
- `tests/test_photo_editor_family.py:108`

## `required_read_tool_choice` — function, line 3254
- **called from:**
- `src/clean_agent_preview.py:6360`
- `tests/test_clean_agent_preview.py:1655`
- `tests/test_clean_agent_preview.py:1658`
- `tests/test_clean_agent_preview.py:2037`
- `tests/test_clean_agent_preview.py:2044`
- `tests/test_clean_agent_preview.py:2055`
- `tests/test_clean_agent_preview.py:2056`
- `tests/test_session_mutation_lookup.py:24`
- `tests/test_session_mutation_lookup.py:26`
- `tests/test_session_mutation_lookup.py:37`

## `draft_contact_evidence_error` — function, line 3294
- **called from:**
- `src/clean_agent_preview.py:7597`
- `tests/test_draft_contact_evidence.py:7`
- `tests/test_draft_contact_evidence.py:37`

## `dependent_write_prerequisite_error` — function, line 3316
- **called from:**
- `src/clean_agent_preview.py:7601`
- `tests/test_clean_agent_preview.py:50`
- `tests/test_clean_agent_preview.py:51`
- `tests/test_clean_agent_preview.py:59`
- `tests/test_session_mutation_lookup.py:31`
- `tests/test_session_mutation_lookup.py:32`
- `tests/test_session_mutation_lookup.py:33`
- `tests/test_session_mutation_lookup.py:38`

## `bounded_research_tool_policy` — function, line 3343
- **called from:**
- `src/clean_agent_preview.py:6328`
- `tests/test_clean_agent_preview.py:2072`
- `tests/test_clean_agent_preview.py:2085`
- `tests/test_clean_agent_preview.py:2102`
- `tests/test_clean_agent_preview.py:2118`

## `search_embedded_article_urls` — function, line 3376
- **called from:**
- `src/clean_agent_preview.py:8113`
- `tests/test_clean_agent_preview.py:3002`
- `tests/test_clean_agent_preview.py:3003`
- `tests/test_clean_agent_preview.py:3004`
- `tests/test_clean_agent_preview.py:3005`

## `retrieved_source_urls` — function, line 3395
- **called from:**
- `src/clean_agent_preview.py:8180`
- `src/clean_agent_preview.py:8201`
- `src/clean_agent_preview.py:8265`
- `src/clean_agent_preview.py:8266`
- `src/clean_agent_preview.py:8281`
- `src/clean_agent_preview.py:8284`
- `src/clean_agent_preview.py:8292`
- `tests/test_clean_agent_preview.py:2127`
- `tests/test_clean_agent_preview.py:2130`
- `tests/test_clean_agent_preview.py:2133`

## `serialize_required_email_attachment_chain` — function, line 3412
- **called from:**
- `src/clean_agent_preview.py:6886`
- `tests/test_clean_agent_preview.py:70`
- `tests/test_clean_agent_preview.py:72`

## `required_active_editor_tool_choice` — function, line 3432
- **called from:**
- `src/clean_agent_preview.py:6386`
- `tests/test_clean_agent_preview.py:3729`
- `tests/test_clean_agent_preview.py:3736`
- `tests/test_clean_agent_preview.py:3748`
- `tests/test_clean_agent_preview.py:3755`
- `tests/test_editor_writing_action_routing.py:49`
- `tests/test_editor_writing_action_routing.py:88`

## `sealed_read_arguments` — function, line 3458
- **called from:**
- `src/clean_agent_preview.py:7401`
- `src/clean_agent_preview.py:7497`
- `tests/test_clean_agent_preview.py:1659`
- `tests/test_clean_agent_preview.py:1662`
- `tests/test_clean_agent_preview.py:1677`
- `tests/test_clean_agent_preview.py:1692`
- `tests/test_tool_routing_experiment.py:122`
- `tests/test_tool_routing_experiment.py:380`

## `_email_identifiers_from_text` — function, line 3492
- **called from:**
- `src/clean_agent_preview.py:3542`
- `src/clean_agent_preview.py:3572`
- `src/clean_agent_preview.py:6478`

## `_successful_email_identifiers` — function, line 3530
- **called from:**
- `src/clean_agent_preview.py:3617`

## `youtube_reference_error` — function, line 3578
- **called from:**
- `src/clean_agent_preview.py:7426`
- `src/clean_agent_preview.py:7607`
- `tests/test_youtube_target_validation.py:15`

## `email_identifier_error` — function, line 3613
- **called from:**
- `src/clean_agent_preview.py:7422`
- `src/clean_agent_preview.py:7604`
- `tests/test_clean_agent_preview.py:1717`
- `tests/test_clean_agent_preview.py:1731`
- `tests/test_clean_agent_preview.py:1732`
- `tests/test_clean_agent_preview.py:1733`
- `tests/test_clean_agent_preview.py:1736`
- `tests/test_clean_agent_preview.py:1755`
- `tests/test_clean_agent_preview.py:1773`
- `tests/test_email_reader_completion_regression.py:9`
- `tests/test_email_reader_completion_regression.py:14`
- `tests/test_source_question_routing.py:28`
- `tests/test_source_question_routing.py:29`

## `_latest_successful_tool_arguments` — function, line 3637
- **called from:**
- `src/clean_agent_preview.py:3721`

## `_latest_tool_arguments` — function, line 3670
- **called from:**
- `src/clean_agent_preview.py:3701`

## `inherit_referential_read_arguments` — function, line 3688
- **called from:**
- `src/clean_agent_preview.py:7405`
- `src/clean_agent_preview.py:7501`
- `tests/test_clean_agent_preview.py:1946`
- `tests/test_clean_agent_preview.py:1952`
- `tests/test_clean_agent_preview.py:1971`
- `tests/test_clean_agent_preview.py:2483`
- `tests/test_clean_agent_preview.py:2507`

## `_revision_call` — function, line 3744
- **called from:**
- `src/clean_agent_preview.py:3876`

## `recent_successful_write_families` — function, line 3756
- **called from:**
- `src/clean_agent_preview.py:5841`
- `tests/test_clean_agent_preview.py:3670`
- `tests/test_clean_agent_preview.py:3801`

## `PreviewPolicyDecision` — class, line 3789
- decorator: `dataclass(frozen=True)`
- **called from:**
- `src/clean_agent_preview.py:3824`

## `PreviewPolicyDecision.audit` — method, line 3796
- **called from:**
- `scripts/audit_c5_benchmark_evidence.py:1560`
- `scripts/ref_parity_audit.py:562`
- `src/agent_loop.py:21717`
- `src/agent_loop.py:21730`
- `src/agent_loop.py:21762`
- `src/clean_agent_preview.py:6013`
- `src/clean_agent_preview.py:7158`
- `src/clean_agent_preview.py:7450`
- `src/clean_agent_preview.py:7837`
- `src/turn_contract.py:6341`
- `tests/test_audit_c5_benchmark_evidence.py:67`
- `tests/test_audit_c5_benchmark_evidence.py:183`
- `tests/test_audit_c5_benchmark_evidence.py:204`
- `tests/test_audit_c5_benchmark_evidence.py:212`
- `tests/test_audit_c5_benchmark_evidence.py:300`
- `tests/test_audit_c5_benchmark_evidence.py:301`
- `tests/test_audit_c5_benchmark_evidence.py:1191`
- `tests/test_audit_c5_benchmark_evidence.py:1222`
- `tests/test_audit_c5_benchmark_evidence.py:1239`
- `tests/test_audit_c5_benchmark_evidence.py:1243`
- `tests/test_audit_c5_benchmark_evidence.py:1366`
- `tests/test_audit_c5_benchmark_evidence.py:1385`
- `tests/test_audit_c5_benchmark_evidence.py:1406`
- `tests/test_audit_c5_benchmark_evidence.py:1433`
- `tests/test_audit_c5_benchmark_evidence.py:1460`
- `tests/test_audit_c5_benchmark_evidence.py:1475`
- `tests/test_audit_c5_benchmark_evidence.py:1491`
- `tests/test_audit_c5_benchmark_evidence.py:1741`
- `tests/test_audit_c5_benchmark_evidence.py:1757`
- `tests/test_audit_c5_benchmark_evidence.py:1772`
- `tests/test_audit_c5_benchmark_evidence.py:1787`
- `tests/test_audit_c5_benchmark_evidence.py:1802`
- `tests/test_audit_c5_benchmark_evidence.py:1817`
- `tests/test_audit_c5_benchmark_evidence.py:1832`
- `tests/test_audit_c5_benchmark_evidence.py:1847`
- `tests/test_audit_c5_benchmark_evidence.py:1862`
- `tests/test_audit_c5_benchmark_evidence.py:1877`
- `tests/test_audit_c5_benchmark_evidence.py:1897`
- `tests/test_audit_c5_benchmark_evidence.py:1912`
- `tests/test_audit_c5_benchmark_evidence.py:1927`
- `tests/test_audit_c5_benchmark_evidence.py:1952`
- `tests/test_audit_c5_benchmark_evidence.py:1978`
- `tests/test_audit_c5_benchmark_evidence.py:2012`
- `tests/test_audit_c5_benchmark_evidence.py:2041`
- `tests/test_audit_c5_benchmark_evidence.py:2071`
- `tests/test_audit_c5_benchmark_evidence.py:2093`
- `tests/test_audit_c5_benchmark_evidence.py:2117`
- `tests/test_audit_c5_benchmark_evidence.py:2180`
- `tests/test_audit_c5_benchmark_evidence.py:2214`
- `tests/test_audit_c5_benchmark_evidence.py:2273`
- `tests/test_audit_c5_benchmark_evidence.py:2297`
- `tests/test_audit_c5_benchmark_evidence.py:2325`
- `tests/test_audit_c5_benchmark_evidence.py:2342`
- `tests/test_audit_c5_benchmark_evidence.py:2358`
- `tests/test_audit_c5_benchmark_evidence.py:2371`
- `tests/test_audit_c5_benchmark_evidence.py:2388`
- `tests/test_audit_c5_benchmark_evidence.py:2415`
- `tests/test_audit_c5_benchmark_evidence.py:2435`
- `tests/test_audit_c5_benchmark_evidence.py:2556`
- `tests/test_audit_c5_benchmark_evidence.py:2640`
- … +21 more (grep the name in repo)

## `evaluate_preview_call` — function, line 3803
- **called from:**
- `src/clean_agent_preview.py:4024`
- `src/clean_agent_preview.py:7146`
- `src/clean_agent_preview.py:7437`
- `src/clean_agent_preview.py:7822`
- `tests/test_clean_agent_preview.py:321`
- `tests/test_clean_agent_preview.py:328`
- `tests/test_clean_agent_preview.py:337`
- `tests/test_clean_agent_preview.py:346`
- `tests/test_clean_agent_preview.py:368`
- `tests/test_clean_agent_preview.py:371`
- `tests/test_clean_agent_preview.py:372`
- `tests/test_clean_agent_preview.py:1518`
- `tests/test_clean_agent_preview.py:1527`
- `tests/test_clean_agent_preview.py:1544`
- `tests/test_clean_agent_preview.py:1553`
- `tests/test_clean_agent_preview.py:3310`
- `tests/test_clean_agent_preview.py:3317`
- `tests/test_clean_agent_preview.py:3327`
- `tests/test_clean_agent_preview.py:3336`
- `tests/test_clean_agent_preview.py:3339`
- `tests/test_clean_agent_preview.py:3349`
- `tests/test_clean_agent_preview.py:3367`
- `tests/test_clean_agent_preview.py:3372`
- `tests/test_clean_agent_preview.py:3380`
- `tests/test_clean_agent_preview.py:3529`
- `tests/test_clean_agent_preview.py:3561`
- `tests/test_clean_agent_preview.py:3569`
- `tests/test_clean_agent_preview.py:3576`
- `tests/test_clean_agent_preview.py:3584`
- `tests/test_clean_agent_preview.py:3592`
- `tests/test_clean_agent_preview.py:3599`
- `tests/test_clean_agent_preview.py:3851`
- `tests/test_compact_core_contract_path.py:33`
- `tests/test_compact_core_contract_path.py:35`
- `tests/test_compact_core_contract_path.py:37`
- `tests/test_compact_email_editor.py:5`
- `tests/test_email_attachment_text.py:66`
- `tests/test_email_attachment_text.py:70`
- `tests/test_research_chat_runtime.py:35`
- `tests/test_research_chat_runtime.py:37`
- `tests/test_research_chat_runtime.py:40`
- `tests/test_spec_driver_mode.py:226`
- `tests/test_spec_driver_mode.py:237`
- `tests/test_tool_routing_experiment.py:309`
- `tests/test_tool_routing_experiment.py:311`
- `tests/test_tool_routing_experiment.py:312`
- `tests/test_tool_routing_experiment.py:313`
- `tests/test_tool_routing_experiment.py:314`
- `tests/test_tool_routing_experiment.py:323`
- `tests/test_tool_routing_experiment.py:324`
- `tests/test_tool_routing_experiment.py:328`
- `tests/test_tool_routing_experiment.py:329`
- `tests/test_tool_routing_experiment.py:330`
- `tests/test_tool_routing_experiment.py:353`
- `tests/test_tool_routing_experiment.py:357`
- `tests/test_tool_routing_experiment.py:358`
- `tests/test_tool_routing_experiment.py:359`

## `decision` — function, line 3823
- **called from:**
- `src/clean_agent_preview.py:3844`
- `src/clean_agent_preview.py:3849`
- `src/clean_agent_preview.py:3853`
- `src/clean_agent_preview.py:3863`
- `src/clean_agent_preview.py:3872`
- `src/clean_agent_preview.py:3890`
- `src/clean_agent_preview.py:3898`
- `src/clean_agent_preview.py:4007`
- `src/clean_agent_preview.py:4009`
- `src/clean_agent_preview.py:4012`
- `src/clean_agent_preview.py:4015`
- `src/clean_agent_preview.py:4016`

## `preview_call_allowed` — function, line 4019
- **called from:**
- `src/clean_agent_preview.py:4037`
- `tests/test_clean_agent_preview.py:1475`
- `tests/test_clean_agent_preview.py:1476`
- `tests/test_clean_agent_preview.py:1477`
- `tests/test_clean_agent_preview.py:1478`
- `tests/test_clean_agent_preview.py:1479`
- `tests/test_clean_agent_preview.py:1480`
- `tests/test_clean_agent_preview.py:1481`
- `tests/test_clean_agent_preview.py:1482`
- `tests/test_clean_agent_preview.py:1483`
- `tests/test_clean_agent_preview.py:1487`
- `tests/test_clean_agent_preview.py:1491`
- `tests/test_clean_agent_preview.py:3173`
- `tests/test_clean_agent_preview.py:3176`
- `tests/test_clean_agent_preview.py:3179`
- `tests/test_clean_agent_preview.py:3182`
- `tests/test_clean_agent_preview.py:3191`
- `tests/test_clean_agent_preview.py:3194`
- `tests/test_clean_agent_preview.py:3197`
- `tests/test_clean_agent_preview.py:3200`
- `tests/test_clean_agent_preview.py:3203`
- `tests/test_clean_agent_preview.py:3210`
- `tests/test_clean_agent_preview.py:3211`
- `tests/test_clean_agent_preview.py:3222`
- `tests/test_clean_agent_preview.py:3226`
- `tests/test_clean_agent_preview.py:3301`
- `tests/test_clean_agent_preview.py:3304`
- `tests/test_clean_agent_preview.py:3355`
- `tests/test_clean_agent_preview.py:3360`
- `tests/test_clean_agent_preview.py:3652`
- `tests/test_clean_agent_preview.py:3653`
- `tests/test_clean_agent_preview.py:3654`
- `tests/test_clean_agent_preview.py:3672`
- `tests/test_clean_agent_preview.py:3676`
- `tests/test_clean_agent_preview.py:3680`
- `tests/test_clean_agent_preview.py:3688`
- `tests/test_clean_agent_preview.py:3692`
- `tests/test_clean_v3_native_workspace.py:22`
- `tests/test_clean_v3_native_workspace.py:23`
- `tests/test_clean_v3_native_workspace.py:54`
- `tests/test_clean_v3_native_workspace.py:55`
- `tests/test_clean_v3_native_workspace.py:56`
- `tests/test_clean_v3_native_workspace.py:59`
- `tests/test_clean_v3_native_workspace.py:62`
- `tests/test_clean_v3_native_workspace.py:78`
- `tests/test_clean_v3_native_workspace.py:79`
- `tests/test_code_editor_routing.py:40`
- `tests/test_code_editor_routing.py:42`
- `tests/test_image_creation_routing.py:26`
- `tests/test_image_creation_routing.py:104`
- `tests/test_image_creation_routing.py:107`

## `readonly_call` — function, line 4034
- **called from:**
- `tests/test_clean_agent_preview.py:1467`
- `tests/test_clean_agent_preview.py:1468`
- `tests/test_clean_agent_preview.py:1469`
- `tests/test_clean_agent_preview.py:1470`
- `tests/test_clean_agent_preview.py:1471`

## `_rehydrate_recent_image` — function, line 4040
- **called from:**
- `src/clean_agent_preview.py:4222`

## `_conversation_user_text` — function, line 4090
- **called from:**
- `src/clean_agent_preview.py:4160`
- `src/clean_agent_preview.py:4181`
- `src/clean_agent_preview.py:5652`

## `text_only_clean_trace` — function, line 4102
- **called from:**
- `src/clean_agent_preview.py:4166`
- `src/clean_agent_preview.py:9026`

## `recent_source_reference_context` — function, line 4119
- **called from:**
- `src/clean_agent_preview.py:4187`

## `conversation` — function, line 4141
- **called from:**
- `src/clean_agent_preview.py:5790`
- `src/clean_agent_preview.py:6067`
- `tests/test_background_tool_jobs.py:97`
- `tests/test_clean_agent_preview.py:2877`
- `tests/test_clean_agent_preview.py:2898`
- `tests/test_clean_agent_preview.py:3882`
- `tests/test_clean_agent_preview.py:3900`
- `tests/test_clean_agent_preview.py:3917`
- `tests/test_clean_agent_preview.py:3945`
- `tests/test_clean_agent_preview.py:3977`
- `tests/test_clean_agent_preview.py:3991`
- `tests/test_clean_agent_preview.py:4014`
- `tests/test_compact_memory_context.py:10`
- `tests/test_compact_memory_context.py:23`
- `tests/test_compact_memory_context.py:29`
- `tests/test_preview_drafting_recovery.py:42`
- `tests/test_result_reference_followup.py:60`
- `tests/test_result_reference_followup.py:78`
- `tests/test_result_reference_followup.py:85`
- `tests/test_web_history_retention.py:23`
- `static/js/slashCommands.js:1101`

## `event` — function, line 4233
- **called from:**
- `src/clean_agent_preview.py:5636`
- `src/clean_agent_preview.py:6013`
- `src/clean_agent_preview.py:6030`
- `src/clean_agent_preview.py:6037`
- `src/clean_agent_preview.py:6045`
- `src/clean_agent_preview.py:6080`
- `src/clean_agent_preview.py:6123`
- `src/clean_agent_preview.py:6182`
- `src/clean_agent_preview.py:6188`
- `src/clean_agent_preview.py:6225`
- `src/clean_agent_preview.py:6248`
- `src/clean_agent_preview.py:6289`
- `src/clean_agent_preview.py:6497`
- `src/clean_agent_preview.py:6666`
- `src/clean_agent_preview.py:6669`
- `src/clean_agent_preview.py:6745`
- `src/clean_agent_preview.py:6760`
- `src/clean_agent_preview.py:6765`
- `src/clean_agent_preview.py:6773`
- `src/clean_agent_preview.py:6787`
- `src/clean_agent_preview.py:6792`
- `src/clean_agent_preview.py:6850`
- `src/clean_agent_preview.py:6876`
- `src/clean_agent_preview.py:6880`
- `src/clean_agent_preview.py:6924`
- `src/clean_agent_preview.py:6964`
- `src/clean_agent_preview.py:6993`
- `src/clean_agent_preview.py:7001`
- `src/clean_agent_preview.py:7038`
- `src/clean_agent_preview.py:7058`
- `src/clean_agent_preview.py:7082`
- `src/clean_agent_preview.py:7102`
- `src/clean_agent_preview.py:7132`
- `src/clean_agent_preview.py:7159`
- `src/clean_agent_preview.py:7165`
- `src/clean_agent_preview.py:7193`
- `src/clean_agent_preview.py:7199`
- `src/clean_agent_preview.py:7220`
- `src/clean_agent_preview.py:7261`
- `src/clean_agent_preview.py:7295`
- `src/clean_agent_preview.py:7303`
- `src/clean_agent_preview.py:7312`
- `src/clean_agent_preview.py:7320`
- `src/clean_agent_preview.py:7361`
- `src/clean_agent_preview.py:7380`
- `src/clean_agent_preview.py:7382`
- `src/clean_agent_preview.py:7384`
- `src/clean_agent_preview.py:7461`
- `src/clean_agent_preview.py:7850`
- `src/clean_agent_preview.py:7920`
- `src/clean_agent_preview.py:8108`
- `src/clean_agent_preview.py:8153`
- `src/clean_agent_preview.py:8238`
- `src/clean_agent_preview.py:8333`
- `src/clean_agent_preview.py:8375`
- `src/clean_agent_preview.py:8395`
- `src/clean_agent_preview.py:8489`
- `src/clean_agent_preview.py:8502`
- `src/clean_agent_preview.py:8552`
- `src/clean_agent_preview.py:8766`
- … +58 more (grep the name in repo)

## `native_workspace_runtime` — function, line 4237
- **called from:**
- `src/clean_agent_preview.py:5704`

## `native_input_files_clause` — function, line 4248
- **called from:**
- `src/clean_agent_preview.py:5763`
- `tests/test_clean_v3_native_workspace.py:40`
- `tests/test_clean_v3_native_workspace.py:47`

## `multimodal_image_count` — function, line 4272
- **called from:**
- `src/clean_agent_preview.py:4045`
- `src/clean_agent_preview.py:5826`
- `tests/test_clean_agent_preview.py:4002`

## `attachment_reference_count` — function, line 4282
- **called from:**
- `src/clean_agent_preview.py:5827`
- `tests/test_clean_agent_preview.py:4010`

## `active_document_context_message` — function, line 4293
- **called from:**
- `src/clean_agent_preview.py:5821`
- `src/clean_agent_preview.py:7960`
- `tests/test_clean_agent_preview.py:4018`
- `tests/test_clean_agent_preview.py:4029`
- `tests/test_clean_agent_preview.py:4037`

## `_document_context_body` — function, line 4324
- **called from:**
- `src/clean_agent_preview.py:4313`

## `active_email_context_message` — function, line 4354
- **called from:**
- `src/clean_agent_preview.py:5804`
- `src/clean_agent_preview.py:6070`
- `tests/test_clean_agent_preview.py:4055`
- `tests/test_email_reader_completion_regression.py:6`

## `targets_active_editor` — function, line 4373
- **called from:**
- `src/clean_agent_preview.py:5657`
- `tests/test_clean_agent_preview.py:3774`
- `tests/test_clean_agent_preview.py:3788`
- `tests/test_clean_agent_preview.py:4068`
- `tests/test_clean_agent_preview.py:4069`
- `tests/test_clean_agent_preview.py:4070`
- `tests/test_clean_agent_preview.py:4071`
- `tests/test_clean_agent_preview.py:4072`
- `tests/test_clean_agent_preview.py:4073`
- `tests/test_clean_agent_preview.py:4074`
- `tests/test_clean_agent_preview.py:4102`
- `tests/test_clean_agent_preview.py:4114`
- `tests/test_clean_agent_preview.py:4173`
- `tests/test_editor_writing_action_routing.py:33`
- `tests/test_editor_writing_action_routing.py:63`
- `tests/test_editor_writing_action_routing.py:72`

## `active_editor_whole_draft_request` — function, line 4382
- **called from:**
- `src/clean_agent_preview.py:5658`
- `tests/test_clean_agent_preview.py:3703`
- `tests/test_email_targeted_edit_scope.py:17`
- `tests/test_email_targeted_edit_scope.py:26`

## `inline_suggestion_request` — function, line 4398
- **called from:**
- `src/clean_agent_preview.py:4447`
- `src/clean_agent_preview.py:5990`
- `tests/test_clean_agent_preview.py:4080`
- `tests/test_clean_agent_preview.py:4081`
- `tests/test_clean_agent_preview.py:4084`
- `tests/test_clean_agent_preview.py:4088`
- `tests/test_clean_agent_preview.py:4089`
- `tests/test_clean_agent_preview.py:4092`
- `tests/test_inline_review_scope.py:13`
- `tests/test_inline_review_scope.py:22`
- `tests/test_inline_review_scope.py:26`
- `tests/test_search_observation_budget.py:72`

## `active_editor_suggestion_request` — function, line 4445
- **called from:**
- `src/clean_agent_preview.py:5659`
- `tests/test_clean_agent_preview.py:3718`
- `tests/test_clean_agent_preview.py:3775`
- `tests/test_clean_agent_preview.py:3789`
- `tests/test_clean_agent_preview.py:4095`
- `tests/test_clean_agent_preview.py:4103`
- `tests/test_clean_agent_preview.py:4115`
- `tests/test_editor_writing_action_routing.py:34`
- `tests/test_editor_writing_action_routing.py:73`

## `active_document_revision_quality_error` — function, line 4463
- **called from:**
- `src/clean_agent_preview.py:7616`
- `tests/test_clean_agent_preview.py:4220`
- `tests/test_clean_agent_preview.py:4227`

## `document_suggestion_quality_error` — function, line 4495
- **called from:**
- `src/clean_agent_preview.py:7621`
- `tests/test_clean_agent_preview.py:483`
- `tests/test_clean_agent_preview.py:486`
- `tests/test_editor_writing_action_routing.py:276`
- `tests/test_editor_writing_action_routing.py:279`
- `tests/test_editor_writing_action_routing.py:281`
- `tests/tools/editor_writing_smoke.py:123`

## `scope_active_editor_contract` — function, line 4546
- **called from:**
- `src/clean_agent_preview.py:5661`
- `tests/test_clean_agent_preview.py:3707`
- `tests/test_clean_agent_preview.py:3722`
- `tests/test_clean_agent_preview.py:4183`
- `tests/test_clean_agent_preview.py:4196`
- `tests/test_clean_agent_preview.py:4206`
- `tests/test_editor_writing_action_routing.py:38`

## `denied_response` — function, line 4566
- **called from:**
- `src/clean_agent_preview.py:7340`
- `src/clean_agent_preview.py:7459`
- `src/clean_agent_preview.py:8809`
- `tests/test_clean_agent_preview.py:3805`
- `tests/test_clean_agent_preview.py:5006`
- `tests/test_clean_agent_preview.py:5008`
- `tests/test_clean_agent_preview.py:5102`
- `tests/test_clean_agent_preview.py:6814`
- `tests/test_clean_agent_preview.py:7555`

## `workspace_process_denial` — function, line 4576
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `execution_has_write_effect` — function, line 4590
- **called from:**
- `src/clean_agent_preview.py:7934`
- `tests/test_clean_agent_preview.py:14`
- `tests/test_clean_agent_preview.py:23`
- `tests/test_clean_agent_preview.py:32`

## `mutation_action_requested` — function, line 4632
- **called from:**
- `src/clean_agent_preview.py:3819`
- `src/clean_agent_preview.py:3880`
- `src/clean_agent_preview.py:3963`
- `src/clean_agent_preview.py:3979`
- `src/clean_agent_preview.py:3993`
- `src/clean_agent_preview.py:4655`

## `requests_mutation` — function, line 4652
- **called from:**
- `src/clean_agent_preview.py:7323`
- `tests/test_calendar_retiming_routing.py:16`
- `tests/test_clean_agent_preview.py:3815`
- `tests/test_clean_agent_preview.py:3825`
- `tests/test_clean_agent_preview.py:3835`
- `tests/test_clean_agent_preview.py:3840`
- `tests/test_clean_agent_preview.py:3850`
- `tests/test_clean_agent_preview.py:3863`
- `tests/test_clean_agent_preview.py:7511`
- `tests/test_clean_agent_preview.py:7516`
- `tests/test_clean_agent_preview.py:7517`
- `tests/test_creation_container_routing.py:29`
- `tests/test_search_observation_budget.py:71`

## `claims_completion` — function, line 4658
- **called from:**
- `src/clean_agent_preview.py:4666`
- `src/clean_agent_preview.py:7327`
- `tests/test_clean_agent_preview.py:3867`
- `tests/test_clean_agent_preview.py:3868`
- `tests/test_clean_agent_preview.py:3869`
- `tests/test_clean_agent_preview.py:3872`
- `tests/test_clean_agent_preview.py:3873`

## `failed_ui_completion` — function, line 4664
- **called from:**
- `src/clean_agent_preview.py:7300`
- `tests/test_ui_control_rag_toggle.py:37`
- `tests/test_ui_control_rag_toggle.py:38`
- `tests/test_ui_control_rag_toggle.py:39`

## `declared_workspace_artifacts` — function, line 4688
- **called from:**
- `src/clean_agent_preview.py:2209`
- `src/clean_agent_preview.py:4725`
- `src/clean_agent_preview.py:4739`
- `tests/test_clean_agent_preview.py:437`
- `tests/test_clean_agent_preview.py:1435`
- `tests/test_redos_core_parsers.py:294`

## `missing_workspace_artifacts` — function, line 4719
- **called from:**
- `src/clean_agent_preview.py:4740`
- `src/clean_agent_preview.py:4757`
- `src/clean_agent_preview.py:7239`
- `src/clean_agent_preview.py:8850`

## `verified_declared_workspace_artifacts` — function, line 4736
- **called from:**
- `src/clean_agent_preview.py:7331`
- `tests/test_clawmm_r46_verified_artifacts.py:10`
- `tests/test_clawmm_r46_verified_artifacts.py:16`
- `tests/test_clawmm_r46_verified_artifacts.py:20`
- `tests/test_clawmm_r46_verified_artifacts.py:29`

## `successful_duplicate_recovery_message` — function, line 4743
- **called from:**
- `src/clean_agent_preview.py:7757`
- `tests/test_clawmm_r45_duplicate_recovery.py:10`

## `normalized_search_intent` — function, line 4774
- **called from:**
- `src/clean_agent_preview.py:4787`
- `src/clean_agent_preview.py:7562`
- `src/clean_agent_preview.py:8126`
- `src/clean_agent_preview.py:8406`
- `tests/test_clean_agent_preview.py:1980`
- `tests/test_clean_agent_preview.py:1981`

## `repeated_search_refinement` — function, line 4781
- **called from:**
- `src/clean_agent_preview.py:7563`
- `tests/test_clean_agent_preview.py:3069`
- `tests/test_clean_agent_preview.py:3070`
- `tests/test_clean_agent_preview.py:3071`

## `evidence_tool_keeps_distinct_requests_available` — function, line 4800
- **called from:**
- `src/clean_agent_preview.py:7737`
- `tests/test_clean_agent_preview.py:3079`
- `tests/test_clean_agent_preview.py:3080`
- `tests/test_clean_agent_preview.py:3081`

## `_terminal_source_link_clause` — function, line 4814
- **called from:**
- `src/clean_agent_preview.py:4860`
- `tests/test_redos_core_parsers.py:580`

## `matches_at` — function, line 4817
- **called from:**
- `src/clean_agent_preview.py:4855`
- `src/clean_agent_preview.py:4855`

## `requested_web_source_links` — function, line 4858
- **called from:**
- `src/clean_agent_preview.py:5186`
- `src/clean_agent_preview.py:5957`
- `src/clean_agent_preview.py:7014`
- `src/clean_agent_preview.py:8439`
- `tests/test_clean_agent_preview.py:1982`
- `tests/test_clean_agent_preview.py:1983`
- `tests/test_clean_agent_preview.py:3165`
- `tests/test_search_observation_budget.py:48`
- `tests/test_search_observation_budget.py:54`

## `source_link_only_request` — function, line 4873
- **called from:**
- `src/clean_agent_preview.py:8452`
- `tests/test_search_observation_budget.py:18`

## `unbound_lookup_reference` — function, line 4884
- **called from:**
- `src/clean_agent_preview.py:5828`
- `tests/test_search_reference_context.py:8`
- `tests/test_search_reference_context.py:9`
- `tests/test_search_reference_context.py:11`
- `tests/test_search_reference_context.py:16`

## `_web_source_rows` — function, line 4905
- **called from:**
- `src/clean_agent_preview.py:4965`
- `tests/test_redos_core_parsers.py:581`

## `web_source_links` — function, line 4962
- **called from:**
- `src/clean_agent_preview.py:2019`
- `src/clean_agent_preview.py:4129`
- `src/clean_agent_preview.py:8121`
- `src/clean_agent_preview.py:8446`
- `tests/test_clean_agent_preview.py:1986`
- `tests/test_clean_agent_preview.py:1994`
- `tests/test_clean_agent_preview.py:1995`
- `tests/test_clean_agent_preview.py:2003`
- `tests/test_clean_agent_preview.py:2012`
- `tests/test_clean_agent_preview.py:3130`
- `tests/test_clean_agent_preview.py:3137`
- `tests/test_clean_agent_preview.py:3167`

## `official_domains_for_text` — function, line 5006
- **called from:**
- `src/clean_agent_preview.py:4985`
- `src/clean_agent_preview.py:5222`
- `src/clean_agent_preview.py:8443`

## `ground_referenced_note_content` — function, line 5025
- **called from:**
- `src/clean_agent_preview.py:7415`
- `src/clean_agent_preview.py:7516`
- `tests/test_clean_agent_preview.py:2906`
- `tests/test_clean_agent_preview.py:2912`

## `email_search_result_empty` — function, line 5054
- **called from:**
- `src/clean_agent_preview.py:5076`
- `tests/test_email_search_recovery.py:16`
- `tests/test_email_search_recovery.py:30`
- `tests/test_redos_agent_preview_parsers.py:109`

## `email_search_recovery` — function, line 5075
- **called from:**
- `src/clean_agent_preview.py:8590`
- `tests/test_email_search_recovery.py:17`
- `tests/test_email_search_recovery.py:18`
- `tests/test_email_search_recovery.py:19`

## `note_search_result_empty` — function, line 5091
- **called from:**
- `src/clean_agent_preview.py:1054`
- `src/clean_agent_preview.py:5132`
- `src/clean_agent_preview.py:8621`
- `tests/test_clean_agent_preview.py:1633`

## `note_referent_error` — function, line 5103
- **called from:**
- `src/clean_agent_preview.py:7610`
- `tests/test_clean_agent_preview.py:1634`
- `tests/test_clean_agent_preview.py:1638`

## `research_referent_error` — function, line 5140
- **called from:**
- `src/clean_agent_preview.py:7613`
- `tests/test_clean_agent_preview.py:2557`

## `requested_web_link_limit` — function, line 5175
- **called from:**
- `src/clean_agent_preview.py:8441`
- `tests/test_clean_agent_preview.py:1999`
- `tests/test_clean_agent_preview.py:2000`
- `tests/test_clean_agent_preview.py:3166`

## `preserve_requested_web_recency` — function, line 5191
- **called from:**
- `src/clean_agent_preview.py:7409`
- `src/clean_agent_preview.py:7504`
- `tests/test_clean_agent_preview.py:2013`
- `tests/test_clean_agent_preview.py:2018`
- `tests/test_clean_agent_preview.py:2022`
- `tests/test_clean_agent_preview.py:2025`
- `tests/test_clean_agent_preview.py:3085`
- `tests/test_clean_agent_preview.py:3100`
- `tests/test_clean_agent_preview.py:3108`
- `tests/test_clean_agent_preview.py:3115`
- `tests/test_search_observation_budget.py:149`
- `tests/test_search_observation_budget.py:152`
- `tests/test_search_publication_intent.py:29`
- `tests/test_search_publication_intent.py:35`
- `tests/test_search_publication_intent.py:37`
- `tests/test_search_publication_intent.py:42`
- `tests/test_search_publication_intent.py:48`

## `preserve_requested_email_account` — function, line 5252
- **called from:**
- `src/clean_agent_preview.py:7412`
- `src/clean_agent_preview.py:7513`
- `tests/test_clean_agent_preview.py:1500`
- `tests/test_clean_agent_preview.py:1504`

## `private_browser_open_url` — function, line 5266
- **called from:**
- `src/clean_agent_preview.py:5285`
- `src/clean_agent_preview.py:7531`
- `src/clean_agent_preview.py:8146`
- `src/clean_agent_preview.py:8221`
- `src/clean_agent_preview.py:8430`
- `tests/test_clean_agent_preview.py:2944`

## `browser_transport_recovery` — function, line 5283
- **called from:**
- `src/clean_agent_preview.py:8140`
- `tests/test_browser_transport_recovery.py:11`
- `tests/test_browser_transport_recovery.py:19`
- `tests/test_browser_transport_recovery.py:28`
- `tests/test_browser_transport_recovery.py:34`
- `tests/test_browser_transport_recovery.py:42`

## `private_browser_effective_url` — function, line 5323
- **called from:**
- `src/clean_agent_preview.py:8222`
- `src/clean_agent_preview.py:8431`
- `tests/test_clean_agent_preview.py:2945`

## `is_google_sorry_url` — function, line 5342
- **called from:**
- `src/clean_agent_preview.py:8226`
- `tests/test_redos_agent_preview_parsers.py:131`

## `browser_observation_page_missing` — function, line 5352
- **called from:**
- `src/clean_agent_preview.py:3388`
- `src/clean_agent_preview.py:8165`
- `tests/test_clean_agent_preview.py:2978`
- `tests/test_clean_agent_preview.py:2982`
- `tests/test_clean_agent_preview.py:2983`

## `browser_observation_access_blocked` — function, line 5362
- **called from:**
- `src/clean_agent_preview.py:3387`
- `src/clean_agent_preview.py:8160`
- `tests/test_clean_agent_preview.py:2951`
- `tests/test_clean_agent_preview.py:2954`
- `tests/test_clean_agent_preview.py:2955`
- `tests/test_clean_agent_preview.py:2972`

## `web_fetch_observation_is_boilerplate` — function, line 5389
- **called from:**
- `src/clean_agent_preview.py:3389`
- `src/clean_agent_preview.py:8097`
- `tests/test_clean_agent_preview.py:3013`
- `tests/test_clean_agent_preview.py:3014`

## `bounded_visual_result_blocks` — function, line 5406
- **called from:**
- `src/clean_agent_preview.py:8497`
- `tests/test_clean_agent_preview.py:3287`
- `tests/test_clean_v3_native_workspace.py:108`

## `provider_request_messages` — function, line 5487
- **called from:**
- `src/clean_agent_preview.py:5500`
- `src/clean_agent_preview.py:6301`
- `tests/test_clean_agent_preview.py:82`
- `tests/test_clean_agent_preview.py:97`

## `provider_wire_messages` — function, line 5497
- **called from:**
- `src/clean_agent_preview.py:5552`
- `tests/test_clean_agent_preview.py:98`
- `tests/test_clean_agent_preview.py:824`

## `record_tool_execution` — function, line 5516
- **called from:**
- `src/clean_agent_preview.py:8501`
- `tests/test_clean_agent_preview.py:3435`
- `tests/test_clean_agent_preview.py:3436`
- `tests/test_clean_agent_preview.py:3437`

## `preview_model_response` — function (async), line 5526
- decorator: `asynccontextmanager`
- **called from:**
- `src/clean_agent_preview.py:6690`
- `src/spec_driver.py:64`

## `preview_lines_until_finish` — function (async), line 5594
- **called from:**
- `src/clean_agent_preview.py:6696`
- `tests/test_editor_writing_action_routing.py:259`

## `stream_preview` — function (async), line 5625
- decorator: `with_request_authority`
- **called from:**
- `scripts/probe_browser_budget.py:61`
- `scripts/probe_empty_search_recovery.py:50`
- `scripts/probe_fixed_search_evidence.py:61`
- `src/agent_loop.py:21738`
- `tests/test_ajax_email_live.py:45`
- `tests/test_ajax_email_live.py:119`
- `tests/test_ajax_email_live.py:198`
- `tests/test_api_token_tool_authority.py:331`
- `tests/test_browser_transport_recovery.py:100`
- `tests/test_buffered_terminal_answer.py:38`
- `tests/test_calendar_stream_links.py:61`
- `tests/test_clawmm_r47_malformed_write_body.py:73`
- `tests/test_clean_agent_preview.py:607`
- `tests/test_clean_agent_preview.py:869`
- `tests/test_clean_agent_preview.py:962`
- `tests/test_clean_agent_preview.py:1051`
- `tests/test_clean_agent_preview.py:1199`
- `tests/test_clean_agent_preview.py:1278`
- `tests/test_clean_agent_preview.py:1364`
- `tests/test_clean_agent_preview.py:2195`
- `tests/test_clean_agent_preview.py:2307`
- `tests/test_clean_agent_preview.py:4147`
- `tests/test_clean_agent_preview.py:4289`
- `tests/test_clean_agent_preview.py:4583`
- `tests/test_clean_agent_preview.py:4615`
- `tests/test_clean_agent_preview.py:4659`
- `tests/test_clean_agent_preview.py:4700`
- `tests/test_clean_agent_preview.py:4763`
- `tests/test_clean_agent_preview.py:4837`
- `tests/test_clean_agent_preview.py:4918`
- `tests/test_clean_agent_preview.py:4971`
- `tests/test_clean_agent_preview.py:5003`
- `tests/test_clean_agent_preview.py:5053`
- `tests/test_clean_agent_preview.py:5099`
- `tests/test_clean_agent_preview.py:5134`
- `tests/test_clean_agent_preview.py:5186`
- `tests/test_clean_agent_preview.py:5253`
- `tests/test_clean_agent_preview.py:5327`
- `tests/test_clean_agent_preview.py:5404`
- `tests/test_clean_agent_preview.py:5474`
- `tests/test_clean_agent_preview.py:5548`
- `tests/test_clean_agent_preview.py:5616`
- `tests/test_clean_agent_preview.py:5709`
- `tests/test_clean_agent_preview.py:5792`
- `tests/test_clean_agent_preview.py:5907`
- `tests/test_clean_agent_preview.py:5988`
- `tests/test_clean_agent_preview.py:6061`
- `tests/test_clean_agent_preview.py:6123`
- `tests/test_clean_agent_preview.py:6161`
- `tests/test_clean_agent_preview.py:6188`
- `tests/test_clean_agent_preview.py:6215`
- `tests/test_clean_agent_preview.py:6269`
- `tests/test_clean_agent_preview.py:6319`
- `tests/test_clean_agent_preview.py:6387`
- `tests/test_clean_agent_preview.py:6462`
- `tests/test_clean_agent_preview.py:6531`
- `tests/test_clean_agent_preview.py:6617`
- `tests/test_clean_agent_preview.py:6707`
- `tests/test_clean_agent_preview.py:6787`
- `tests/test_clean_agent_preview.py:6854`
- … +41 more (grep the name in repo)

## `permitted_schema` — function, line 5674
- **called from:**
- `src/clean_agent_preview.py:5681`
- `src/clean_agent_preview.py:6325`
- `src/clean_agent_preview.py:6593`
