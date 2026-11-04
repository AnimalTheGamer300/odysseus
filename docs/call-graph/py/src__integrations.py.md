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
- `routes/auth_routes.py:770`
- `routes/auth_routes.py:786`
- `routes/auth_routes.py:798`
- `tests/test_security_regressions.py:181`

## `_normalize_integration_base_url` — function, line 209
- **called from:**
- `src/integrations.py:292`
- `src/integrations.py:309`
- `src/integrations.py:524`

## `_join_integration_url` — function, line 221
- **called from:**
- `src/integrations.py:552`
- `tests/test_integrations_url_join.py:73`

## `load_integrations` — function, line 232
- **called from:**
- `routes/auth_routes.py:768`
- `routes/note/note_routes.py:416`
- `routes/note/note_routes.py:475`
- `src/integrations.py:263`
- `src/integrations.py:296`
- `src/integrations.py:313`
- `src/integrations.py:325`
- `src/integrations.py:347`
- `src/integrations.py:751`
- `src/integrations.py:792`
- `src/service_health.py:427`
- `src/task_scheduler.py:1401`
- `src/tools/system.py:516`
- `tests/test_integrations_store_shape.py:15`
- `tests/test_integrations_store_shape.py:68`
- `tests/test_integrations_store_shape.py:83`
- `tests/test_integrations_store_shape.py:104`
- `tests/test_integrations_store_shape.py:127`
- `tests/test_integrations_store_shape.py:150`
- `tests/test_integrations_store_shape.py:179`
- `tests/test_security_regressions.py:179`
- `tests/test_security_regressions.py:200`

## `save_integrations` — function, line 254
- **called from:**
- `src/integrations.py:247`
- `src/integrations.py:298`
- `src/integrations.py:318`
- `src/integrations.py:329`
- `tests/test_integrations_store_shape.py:111`
- `tests/test_integrations_store_shape.py:134`
- `tests/test_integrations_store_shape.py:163`
- `tests/test_security_regressions.py:164`

## `get_integration` — function, line 261
- **called from:**
- `routes/auth_routes.py:817`

## `add_integration` — function, line 269
- **called from:**
- `routes/auth_routes.py:785`
- `src/integrations.py:798`

## `update_integration` — function, line 302
- **called from:**
- `routes/auth_routes.py:795`
- `tests/test_integrations_store_shape.py:120`
- `tests/test_integrations_store_shape.py:143`
- `tests/test_integrations_store_shape.py:172`

## `delete_integration` — function, line 323
- **called from:**
- `routes/auth_routes.py:806`

## `_strip_html_tags` — function, line 338
- **called from:**
- `src/integrations.py:709`

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

## `_PinnedAsyncBackend.connect_tcp` — method (async), line 393
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

## `_PinnedAsyncBackend.connect_unix_socket` — method (async), line 412
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedAsyncBackend.sleep` — method (async), line 415
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
- `src/llm_core.py:2797`
- `src/llm_core.py:2860`
- `src/llm_core.py:2866`
- `src/llm_core.py:2877`
- `src/llm_core.py:2888`
- `src/llm_core.py:2899`
- `src/llm_core.py:2910`
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

## `_PinnedAsyncTransport` — class, line 419
- **called from:**
- `src/integrations.py:626`
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

## `_PinnedAsyncTransport.handle_async_request` — method (async), line 442
- **called from:**
- `src/integrations.py:456`
- `src/webhook_manager.py:233`

## `_PinnedAsyncTransport.aclose` — method (async), line 471
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

## `_validated_ips` — function, line 475
- **called from:**
- `services/memory/skill_importer.py:113`
- `src/integrations.py:583`
- `tests/test_integration_api_call_ssrf.py:315`
- `tests/test_integration_api_call_ssrf.py:326`
- `tests/test_integration_api_call_ssrf.py:332`
- `tests/test_integration_api_call_ssrf.py:338`

## `execute_api_call` — function (async), line 506
- **called from:**
- `routes/auth_routes.py:914`
- `src/tools/system.py:523`
- `tests/test_integration_api_call_ssrf.py:56`
- `tests/test_integration_api_call_ssrf.py:132`
- `tests/test_integrations_api_call_truncation.py:91`
- `tests/test_integrations_api_call_truncation.py:110`
- `tests/test_integrations_url_join.py:110`

## `_recording_resolver` — function, line 573
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_integrations_prompt` — function, line 746
- **called from:**
- `src/agent_loop.py:3166`

## `migrate_from_settings` — function, line 772
- **called from:**
- `routes/auth_routes.py:760`
