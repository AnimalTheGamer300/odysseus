# `src/integrations.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ensure_data_dir` — function, line 165
- **called from:**
- `src/integrations.py:256`

## `_encrypt_integration_secrets` — function, line 169
- **called from:**
- `src/integrations.py:257`

## `_decrypt_integration_secrets` — function, line 181
- **called from:**
- `src/integrations.py:247`
- `src/integrations.py:248`

## `_has_plaintext_api_key` — function, line 193
- **called from:**
- `src/integrations.py:246`

## `mask_integration_secret` — function, line 200
- **called from:**
- `routes/auth_routes.py:920`
- `routes/auth_routes.py:936`
- `routes/auth_routes.py:948`
- `tests/test_security_regressions.py:182`

## `_normalize_integration_base_url` — function, line 209
- **called from:**
- `src/integrations.py:292`
- `src/integrations.py:309`
- `src/integrations.py:530`

## `_join_integration_url` — function, line 221
- **called from:**
- `src/integrations.py:558`
- `tests/test_integrations_url_join.py:73`

## `load_integrations` — function, line 232
- **called from:**
- `routes/auth_routes.py:918`
- `routes/note/note_routes.py:419`
- `routes/note/note_routes.py:478`
- `src/agent_runtime/remote_resources.py:121`
- `src/integrations.py:263`
- `src/integrations.py:296`
- `src/integrations.py:313`
- `src/integrations.py:325`
- `src/integrations.py:347`
- `src/integrations.py:757`
- `src/integrations.py:798`
- `src/service_health.py:446`
- `src/task_scheduler.py:1555`
- `src/tools/system.py:736`
- `tests/test_integrations_store_shape.py:15`
- `tests/test_integrations_store_shape.py:68`
- `tests/test_integrations_store_shape.py:83`
- `tests/test_integrations_store_shape.py:104`
- `tests/test_integrations_store_shape.py:127`
- `tests/test_integrations_store_shape.py:150`
- `tests/test_integrations_store_shape.py:179`
- `tests/test_integrations_store_shape.py:191`
- `tests/test_integrations_store_shape.py:204`
- `tests/test_security_regressions.py:180`
- `tests/test_security_regressions.py:201`

## `save_integrations` — function, line 254
- **called from:**
- `src/integrations.py:247`
- `src/integrations.py:298`
- `src/integrations.py:318`
- `src/integrations.py:329`
- `tests/test_integrations_store_shape.py:111`
- `tests/test_integrations_store_shape.py:134`
- `tests/test_integrations_store_shape.py:163`
- `tests/test_integrations_store_shape.py:198`
- `tests/test_security_regressions.py:165`

## `get_integration` — function, line 261
- **called from:**
- `routes/auth_routes.py:963`

## `add_integration` — function, line 269
- **called from:**
- `routes/auth_routes.py:935`
- `src/integrations.py:804`

## `update_integration` — function, line 302
- **called from:**
- `routes/auth_routes.py:945`
- `tests/test_integrations_store_shape.py:120`
- `tests/test_integrations_store_shape.py:143`
- `tests/test_integrations_store_shape.py:172`
- `tests/test_integrations_store_shape.py:201`

## `delete_integration` — function, line 323
- **called from:**
- `routes/auth_routes.py:954`

## `_strip_html_tags` — function, line 338
- **called from:**
- `src/integrations.py:715`

## `_find_integration` — function, line 345
- **called from:**
- `src/integrations.py:516`

## `_PinnedAsyncBackend` — class, line 378
- **called from:**
- `src/integrations.py:439`
- `src/webhook_manager.py:216`
- `tests/test_integration_api_call_ssrf.py:189`

## `_PinnedAsyncBackend.__init__` — method, line 389
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

## `_PinnedAsyncBackend.connect_tcp` — method (async), line 393
- **called from:**
- `services/memory/skill_importer.py:143`
- `src/integrations.py:403`
- `src/outbound_fetch.py:134`
- `src/webhook_manager.py:191`
- `tests/test_integration_api_call_ssrf.py:203`
- `tests/test_integration_api_call_ssrf.py:218`
- `tests/test_security_regressions.py:1335`
- `tests/test_skill_importer_dns_pinning.py:41`
- `tests/test_skill_importer_dns_pinning.py:61`
- `tests/test_vision_inline.py:347`
- `tests/test_vision_inline.py:350`

## `_PinnedAsyncBackend.connect_unix_socket` — method (async), line 412
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedAsyncBackend.sleep` — method (async), line 415
- **called from:**
- `app.py:1320`
- `app.py:1324`
- `app.py:1422`
- `app.py:1427`
- `core/session_manager.py:66`
- `launcher.py:121`
- `routes/chat_helpers.py:821`
- `routes/chat_helpers.py:825`
- `routes/chat_helpers.py:2033`
- `routes/chat_helpers.py:2041`
- `routes/chat_routes.py:4254`
- `routes/cookbook_routes.py:1593`
- `routes/email/email_pollers.py:1514`
- `routes/email/email_pollers.py:1577`
- `routes/email/email_pollers.py:1707`
- `routes/email/email_routes.py:4073`
- `routes/email/email_routes.py:4086`
- `routes/research/research_routes.py:706`
- `routes/session_routes.py:351`
- `routes/shell_routes.py:1067`
- `routes/shell_routes.py:1084`
- `routes/shell_routes.py:1163`
- `routes/shell_routes.py:1181`
- `routes/upload_routes.py:642`
- `scripts/audit_email_sft_with_deepseek.py:270`
- `scripts/audit_email_sft_with_deepseek.py:281`
- `scripts/audit_sft_corpus_with_deepseek.py:304`
- `scripts/backfill_model_release_dates.py:112`
- `scripts/dump_agent_prompt.py:414`
- `scripts/eval_followup_domain_continuity.py:156`
- `scripts/eval_followup_domain_continuity.py:173`
- `scripts/generate_sft_environment_expansion.py:199`
- `scripts/generate_sft_flow_variants_with_kimi.py:101`
- `scripts/import_from_vllm_recipes.py:299`
- `scripts/import_from_vllm_recipes.py:327`
- `scripts/odysseus_conversation_qa.py:388`
- `scripts/odysseus_conversation_qa.py:732`
- `scripts/odysseus_related_flow_audit.py:568`
- `scripts/repair_email_sft_with_kimi.py:230`
- `scripts/repair_sft_corpus_with_kimi.py:209`
- `scripts/run_odysseus_search_teacher_pipeline.py:170`
- `scripts/run_sft_overnight_fixture_flows.py:796`
- `scripts/verify_notes_browser_runtime.py:87`
- `services/memory/skill_importer.py:162`
- `services/youtube/youtube_handler.py:156`
- `src/agent_jobs.py:355`
- `src/agent_runs.py:90`
- `src/agent_tools/subprocess_tools.py:756`
- `src/ai_interaction.py:1767`
- `src/ai_interaction.py:2085`
- `src/background_tool_jobs.py:193`
- `src/bg_monitor.py:237`
- `src/builtin_mcp.py:205`
- `src/clean_agent_preview.py:5591`
- `src/containment.py:1156`
- `src/containment.py:1242`
- `src/containment.py:1525`
- `src/cookbook_serve_lifecycle.py:193`
- `src/cookbook_serve_lifecycle.py:199`
- `src/email_calendar_import.py:47`
- … +148 more (grep the name in repo)

## `_PinnedAsyncTransport` — class, line 419
- **called from:**
- `src/integrations.py:632`
- `src/webhook_manager.py:399`
- `tests/test_integration_api_call_ssrf.py:236`
- `tests/test_integration_api_call_ssrf.py:265`
- `tests/test_webhook_dns_rebinding_pin.py:91`

## `_PinnedAsyncTransport.__init__` — method, line 429
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

## `_PinnedAsyncTransport.handle_async_request` — method (async), line 442
- **called from:**
- `src/integrations.py:456`
- `src/webhook_manager.py:233`

## `_PinnedAsyncTransport.aclose` — method (async), line 471
- **called from:**
- `src/agent_runs.py:161`
- `src/integrations.py:458`
- `src/integrations.py:472`
- `src/mcp_manager.py:273`
- `src/mcp_manager.py:335`
- `src/mcp_manager.py:400`
- `src/mcp_manager.py:467`
- `src/mcp_manager.py:495`
- `src/webhook_manager.py:235`
- `src/webhook_manager.py:249`
- `tests/test_compare_stop_disconnect_poll.py:113`
- `tests/test_compare_stop_disconnect_poll.py:145`
- `tests/test_compare_stop_disconnect_poll.py:322`
- `tests/test_integration_api_call_ssrf.py:241`
- `tests/test_integration_api_call_ssrf.py:272`
- `tests/test_llm_core_fallback.py:737`
- `tests/test_partial_tool_events.py:137`
- `tests/test_request_authority.py:188`
- `tests/test_request_authority.py:353`
- `tests/test_spec_contract_security.py:117`
- `tests/test_tool_task_cancelled_on_disconnect.py:90`
- `tests/test_turn_contract_integration.py:167`
- `tests/test_turn_contract_integration.py:175`
- `tests/test_turn_contract_integration.py:264`
- `tests/test_turn_contract_integration.py:270`
- `tests/test_turn_contract_integration.py:303`
- `tests/test_turn_contract_integration.py:312`

## `_validated_ips` — function, line 475
- **called from:**
- `services/memory/skill_importer.py:113`
- `src/integrations.py:589`
- `tests/test_integration_api_call_ssrf.py:315`
- `tests/test_integration_api_call_ssrf.py:326`
- `tests/test_integration_api_call_ssrf.py:332`
- `tests/test_integration_api_call_ssrf.py:338`

## `execute_api_call` — function (async), line 506
- **called from:**
- `routes/auth_routes.py:1060`
- `src/tools/system.py:743`
- `tests/test_integration_api_call_ssrf.py:56`
- `tests/test_integration_api_call_ssrf.py:132`
- `tests/test_integrations_api_call_truncation.py:91`
- `tests/test_integrations_api_call_truncation.py:110`
- `tests/test_integrations_url_join.py:111`

## `_recording_resolver` — function, line 579
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_integrations_prompt` — function, line 752
- **called from:**
- `src/agent_loop.py:15401`

## `migrate_from_settings` — function, line 778
- **called from:**
- `routes/auth_routes.py:912`
