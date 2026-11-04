# `src/webhook_manager.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow` — function, line 42
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

## `_ip_is_private` — function, line 47
- **called from:**
- `src/webhook_manager.py:102`
- `src/webhook_manager.py:110`
- `src/webhook_manager.py:150`
- `src/webhook_manager.py:154`

## `_resolve_hostname_ips` — function, line 65
- **called from:**
- `services/search/content.py:33`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_is_private_url` — function, line 82
- **called from:**
- `src/webhook_manager.py:125`

## `validate_webhook_url` — function, line 115
- **called from:**
- `routes/webhook/webhook_routes.py:108`
- `src/agent_tools/admin_tools.py:401`
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

## `_PinnedAsyncBackend.connect_tcp` — method (async), line 189
- **called from:**
- `services/memory/skill_importer.py:143`
- `src/integrations.py:403`
- `src/outbound_fetch.py:134`
- `src/webhook_manager.py:191`
- `tests/test_integration_api_call_ssrf.py:203`
- `tests/test_integration_api_call_ssrf.py:218`
- `tests/test_security_regressions.py:1333`
- `tests/test_skill_importer_dns_pinning.py:41`
- `tests/test_skill_importer_dns_pinning.py:61`

## `_PinnedAsyncBackend.connect_unix_socket` — method (async), line 195
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedAsyncBackend.sleep` — method (async), line 198
- **called from:**
- `app.py:1136`
- `app.py:1140`
- `app.py:1230`
- `app.py:1235`
- `app.py:1256`
- `core/session_manager.py:66`
- `launcher.py:121`
- `routes/chat_helpers.py:1363`
- `routes/chat_helpers.py:1371`
- `routes/chat_routes.py:1961`
- `routes/cookbook_routes.py:1693`
- `routes/email_pollers.py:1314`
- `routes/email_pollers.py:1377`
- `routes/email_pollers.py:1507`
- `routes/email_routes.py:3259`
- `routes/email_routes.py:3272`
- `routes/research/research_routes.py:605`
- `routes/shell_routes.py:833`
- `routes/shell_routes.py:850`
- `routes/shell_routes.py:929`
- `routes/shell_routes.py:947`
- `routes/upload_routes.py:530`
- `scripts/backfill_model_release_dates.py:109`
- `scripts/dump_agent_prompt.py:414`
- `scripts/import_from_vllm_recipes.py:292`
- `scripts/import_from_vllm_recipes.py:320`
- `services/memory/skill_importer.py:162`
- `services/youtube/youtube_handler.py:156`
- `src/agent_jobs.py:355`
- `src/agent_runs.py:88`
- `src/agent_tools/subprocess_tools.py:184`
- `src/agent_tools/subprocess_tools.py:234`
- `src/agent_tools/subprocess_tools.py:244`
- `src/ai_interaction.py:1370`
- `src/ai_interaction.py:1637`
- `src/bg_monitor.py:158`
- `src/builtin_mcp.py:204`
- `src/cookbook_serve_lifecycle.py:213`
- `src/cookbook_serve_lifecycle.py:219`
- `src/integrations.py:416`
- `src/llm_core.py:118`
- `src/llm_core.py:2765`
- `src/llm_core.py:2828`
- `src/llm_core.py:2834`
- `src/llm_core.py:2845`
- `src/llm_core.py:2856`
- `src/llm_core.py:2867`
- `src/llm_core.py:2878`
- `src/outbound_fetch.py:142`
- `src/task_scheduler.py:611`
- `src/task_scheduler.py:622`
- `src/task_scheduler.py:631`
- `src/task_scheduler.py:642`
- `src/task_scheduler.py:674`
- `src/task_scheduler.py:699`
- `src/task_scheduler.py:909`
- `src/task_scheduler.py:912`
- `src/webhook_manager.py:199`
- `tests/markdown_browser_check.py:40`
- `tests/markdown_screenshot.py:63`
- … +57 more (grep the name in repo)

## `_PinnedAsyncTransport` — class, line 202
- **called from:**
- `src/integrations.py:626`
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

## `_PinnedAsyncTransport.handle_async_request` — method (async), line 219
- **called from:**
- `src/integrations.py:456`
- `src/webhook_manager.py:233`

## `_PinnedAsyncTransport.aclose` — method (async), line 248
- **called from:**
- `src/agent_runs.py:149`
- `src/integrations.py:458`
- `src/integrations.py:472`
- `src/mcp_manager.py:244`
- `src/mcp_manager.py:305`
- `src/mcp_manager.py:410`
- `src/webhook_manager.py:235`
- `src/webhook_manager.py:249`
- `tests/test_compare_stop_disconnect_poll.py:112`
- `tests/test_compare_stop_disconnect_poll.py:144`
- `tests/test_compare_stop_disconnect_poll.py:321`
- `tests/test_integration_api_call_ssrf.py:241`
- `tests/test_integration_api_call_ssrf.py:272`
- `tests/test_llm_core_fallback.py:715`
- `tests/test_partial_tool_events.py:137`
- `tests/test_tool_task_cancelled_on_disconnect.py:82`

## `validate_events` — function, line 252
- **called from:**
- `routes/webhook/webhook_routes.py:112`
- `src/agent_tools/admin_tools.py:402`

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
- `app.py:635`
- `tests/test_webhook_dns_rebinding_pin.py:147`
- `tests/test_webhook_ssrf_resilience.py:102`

## `WebhookManager.__init__` — method, line 324
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

## `WebhookManager._spawn_tracked` — method, line 337
- **called from:**
- `src/webhook_manager.py:366`
- `src/webhook_manager.py:385`
- `tests/test_webhook_task_refs.py:36`
- `tests/test_webhook_task_refs.py:56`

## `WebhookManager.set_loop` — method, line 345
- **called from:**
- `app.py:1035`

## `WebhookManager._decrypt_secret` — method, line 348
- **called from:**
- `routes/cookbook_routes.py:609`
- `src/webhook_manager.py:384`
- `src/webhook_manager.py:389`

## `WebhookManager.fire_and_forget` — method, line 360
- **called from:**
- `routes/chat_helpers.py:477`
- `routes/chat_helpers.py:1483`
- `routes/session_routes.py:514`
- `routes/webhook/webhook_routes.py:388`

## `WebhookManager.fire` — method (async), line 372
- **called from:**
- `src/webhook_manager.py:366`
- `src/webhook_manager.py:370`
- `static/js/documentLibrary.js:494`
- `static/js/tourAutoplay.js:13`
- `static/js/ui.js:1233`

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
- `app.py:333`
- `app.py:451`
- `app.py:532`
- `app.py:1050`
- `app.py:1174`
- `app.py:1295`
- `companion/pairing.py:151`
- `companion/routes.py:165`
- `core/database.py:161`
- `core/database.py:923`
- `core/database.py:946`
- `core/database.py:971`
- `core/database.py:994`
- `core/database.py:1017`
- `core/database.py:1048`
- `core/database.py:1073`
- `core/database.py:1097`
- `core/database.py:1125`
- `core/database.py:1148`
- `core/database.py:1171`
- `core/database.py:1194`
- `core/database.py:1217`
- `core/database.py:1249`
- `core/database.py:1272`
- `core/database.py:1295`
- `core/database.py:1319`
- `core/database.py:1343`
- `core/database.py:1377`
- `core/database.py:1406`
- `core/database.py:1479`
- `core/database.py:2068`
- `core/database.py:2301`
- `core/database.py:2363`
- `core/database.py:2479`
- `core/database.py:2506`
- `core/database.py:2532`
- `core/database.py:2557`
- `core/database.py:2584`
- `core/database.py:2606`
- `core/database.py:2619`
- `core/database.py:2635`
- `core/session_manager.py:68`
- `core/session_manager.py:177`
- `core/session_manager.py:428`
- `core/session_manager.py:568`
- `core/session_manager.py:603`
- `core/session_manager.py:651`
- `core/session_manager.py:771`
- `core/session_manager.py:858`
- `core/session_manager.py:885`
- `core/session_manager.py:899`
- `core/session_manager.py:945`
- `core/session_manager.py:989`
- `core/session_manager.py:1013`
- `core/session_manager.py:1033`
- `core/session_manager.py:1054`
- `core/session_manager.py:1140`
- `mcp_servers/email_server.py:220`
- `mcp_servers/email_server.py:815`
- `mcp_servers/email_server.py:1351`
- … +754 more (grep the name in repo)
