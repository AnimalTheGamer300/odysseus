# `src/webhook_manager.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow` — function, line 42
- **called from:**
- `src/cleanup_service.py:86`
- `src/cleanup_service.py:101`
- `src/cleanup_service.py:127`
- `src/cleanup_service.py:235`
- `src/cleanup_service.py:236`
- `src/task_scheduler.py:181`
- `src/task_scheduler.py:186`
- `src/task_scheduler.py:493`
- `src/task_scheduler.py:511`
- `src/task_scheduler.py:514`
- `src/task_scheduler.py:516`
- `src/task_scheduler.py:520`
- `src/task_scheduler.py:534`
- `src/task_scheduler.py:610`
- `src/task_scheduler.py:631`
- `src/task_scheduler.py:836`
- `src/task_scheduler.py:848`
- `src/task_scheduler.py:896`
- `src/task_scheduler.py:953`
- `src/task_scheduler.py:955`
- `src/task_scheduler.py:981`
- `src/task_scheduler.py:996`
- `src/task_scheduler.py:999`
- `src/task_scheduler.py:1022`
- `src/task_scheduler.py:1031`
- `src/task_scheduler.py:1094`
- `src/task_scheduler.py:1129`
- `src/task_scheduler.py:1130`
- `src/task_scheduler.py:1135`
- `src/task_scheduler.py:1151`
- `src/task_scheduler.py:1154`
- `src/task_scheduler.py:1163`
- `src/task_scheduler.py:1251`
- `src/task_scheduler.py:1256`
- `src/task_scheduler.py:1261`
- `src/task_scheduler.py:1286`
- `src/task_scheduler.py:1291`
- `src/task_scheduler.py:1292`
- `src/task_scheduler.py:1496`
- `src/task_scheduler.py:1499`
- `src/task_scheduler.py:1503`
- `src/task_scheduler.py:1710`
- `src/task_scheduler.py:1711`
- `src/task_scheduler.py:1890`
- `src/task_scheduler.py:1891`
- `src/task_scheduler.py:1940`
- `src/task_scheduler.py:1948`
- `src/task_scheduler.py:2290`
- `src/task_scheduler.py:2291`
- `src/task_scheduler.py:2624`
- `src/task_scheduler.py:2652`
- `src/task_scheduler.py:2687`
- `src/task_scheduler.py:2705`
- `src/task_scheduler.py:2845`
- `src/task_scheduler.py:2846`
- `src/webhook_manager.py:418`
- `src/webhook_manager.py:432`
- `src/webhook_manager.py:441`
- `tests/test_cleanup_service_utcnow.py:13`
- `tests/test_cleanup_service_utcnow.py:23`
- … +2 more (grep the name in repo)

## `_ip_is_private` — function, line 47
- **called from:**
- `src/webhook_manager.py:102`
- `src/webhook_manager.py:110`
- `src/webhook_manager.py:150`
- `src/webhook_manager.py:154`

## `_resolve_hostname_ips` — function, line 65
- **called from:**
- `services/search/content.py:34`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_is_private_url` — function, line 82
- **called from:**
- `src/webhook_manager.py:125`

## `validate_webhook_url` — function, line 115
- **called from:**
- `routes/webhook/webhook_routes.py:108`
- `src/agent_tools/admin_tools.py:415`
- `src/webhook_manager.py:412`
- `tests/test_webhook_ssrf_resilience.py:56`
- `tests/test_webhook_ssrf_resilience.py:61`

## `_validated_public_ips` — function, line 130
- **called from:**
- `src/webhook_manager.py:413`
- `tests/test_webhook_dns_rebinding_pin.py:39`
- `tests/test_webhook_dns_rebinding_pin.py:44`
- `tests/test_webhook_dns_rebinding_pin.py:48`
- `tests/test_webhook_dns_rebinding_pin.py:57`

## `_PinnedAsyncBackend` — class, line 177
- **called from:**
- `src/integrations.py:439`
- `src/webhook_manager.py:216`
- `tests/test_integration_api_call_ssrf.py:189`

## `_PinnedAsyncBackend.__init__` — method, line 185
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

## `_PinnedAsyncBackend.connect_tcp` — method (async), line 189
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

## `_PinnedAsyncBackend.connect_unix_socket` — method (async), line 195
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedAsyncBackend.sleep` — method (async), line 198
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
- `routes/chat_routes.py:4232`
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

## `_PinnedAsyncTransport` — class, line 202
- **called from:**
- `src/integrations.py:632`
- `src/webhook_manager.py:399`
- `tests/test_integration_api_call_ssrf.py:236`
- `tests/test_integration_api_call_ssrf.py:265`
- `tests/test_webhook_dns_rebinding_pin.py:91`

## `_PinnedAsyncTransport.__init__` — method, line 211
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

## `_PinnedAsyncTransport.handle_async_request` — method (async), line 219
- **called from:**
- `src/integrations.py:456`
- `src/webhook_manager.py:233`

## `_PinnedAsyncTransport.aclose` — method (async), line 248
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

## `validate_events` — function, line 252
- **called from:**
- `routes/webhook/webhook_routes.py:112`
- `src/agent_tools/admin_tools.py:416`

## `_redact_ip_candidate` — function, line 279
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `sanitize_error` — function, line 308
- **called from:**
- `src/webhook_manager.py:443`
- `tests/test_webhook_sanitize_error_ipv6.py:40`
- `tests/test_webhook_sanitize_error_ipv6.py:60`
- `tests/test_webhook_sanitize_error_ipv6.py:64`
- `tests/test_webhook_sanitize_error_ipv6.py:65`
- `tests/test_webhook_sanitize_error_ipv6.py:71`
- `tests/test_webhook_sanitize_error_ipv6.py:79`
- `tests/test_webhook_sanitize_error_ipv6.py:85`
- `tests/test_webhook_sanitize_error_ipv6.py:90`
- `tests/test_webhook_sanitize_error_ipv6.py:98`

## `WebhookManager` — class, line 323
- **called from:**
- `app.py:713`
- `tests/test_webhook_dns_rebinding_pin.py:147`
- `tests/test_webhook_ssrf_resilience.py:102`

## `WebhookManager.__init__` — method, line 324
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

## `WebhookManager._spawn_tracked` — method, line 337
- **called from:**
- `src/webhook_manager.py:366`
- `src/webhook_manager.py:385`
- `tests/test_webhook_task_refs.py:36`
- `tests/test_webhook_task_refs.py:56`

## `WebhookManager.set_loop` — method, line 345
- **called from:**
- `app.py:1199`

## `WebhookManager._decrypt_secret` — method, line 348
- **called from:**
- `routes/cookbook_routes.py:479`
- `src/webhook_manager.py:384`
- `src/webhook_manager.py:389`

## `WebhookManager.fire_and_forget` — method, line 360
- **called from:**
- `routes/chat_helpers.py:959`
- `routes/chat_helpers.py:2182`
- `routes/session_routes.py:679`
- `routes/webhook/webhook_routes.py:388`

## `WebhookManager.fire` — method (async), line 372
- **called from:**
- `src/webhook_manager.py:366`
- `src/webhook_manager.py:370`
- `static/js/documentLibrary.js:619`
- `static/js/tourAutoplay.js:13`
- `static/js/ui.js:1420`

## `WebhookManager.deliver_test` — method (async), line 387
- **called from:**
- `routes/webhook/webhook_routes.py:153`

## `WebhookManager._send_request` — method (async), line 392
- **called from:**
- `src/webhook_manager.py:430`

## `WebhookManager._deliver` — method (async), line 405
- **called from:**
- `src/webhook_manager.py:385`
- `src/webhook_manager.py:390`
- `tests/test_webhook_dns_rebinding_pin.py:149`
- `tests/test_webhook_ssrf_resilience.py:117`

## `WebhookManager.close` — method (async), line 451
- **called from:**
- `app.py:374`
- `app.py:492`
- `app.py:609`
- `app.py:1214`
- `app.py:1358`
- `app.py:1482`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:982`
- `core/database.py:1004`
- `core/database.py:1026`
- `core/database.py:1048`
- `core/database.py:1074`
- `core/database.py:1095`
- `core/database.py:1120`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1197`
- `core/database.py:1222`
- `core/database.py:1246`
- `core/database.py:1274`
- `core/database.py:1297`
- `core/database.py:1320`
- `core/database.py:1344`
- `core/database.py:1367`
- `core/database.py:1390`
- `core/database.py:1442`
- `core/database.py:1465`
- `core/database.py:1488`
- `core/database.py:1511`
- `core/database.py:1548`
- `core/database.py:1571`
- `core/database.py:1595`
- `core/database.py:1629`
- `core/database.py:1658`
- `core/database.py:1731`
- `core/database.py:2365`
- `core/database.py:2635`
- `core/database.py:2697`
- `core/database.py:2813`
- `core/database.py:2840`
- `core/database.py:2866`
- `core/database.py:2891`
- `core/database.py:2918`
- `core/database.py:2940`
- `core/database.py:2962`
- `core/database.py:2974`
- `core/database.py:2990`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:444`
- `core/session_manager.py:584`
- `core/session_manager.py:619`
- `core/session_manager.py:667`
- `core/session_manager.py:787`
- `core/session_manager.py:876`
- `core/session_manager.py:903`
- `core/session_manager.py:917`
- `core/session_manager.py:973`
- … +1048 more (grep the name in repo)
