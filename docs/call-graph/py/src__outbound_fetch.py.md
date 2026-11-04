# `src/outbound_fetch.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_private_address` — function, line 36
- **called from:**
- `services/search/content.py:29`
- `src/outbound_fetch.py:83`
- `src/outbound_fetch.py:87`
- `src/outbound_fetch.py:106`
- `src/outbound_fetch.py:114`

## `_resolve_hostname_ips` — function, line 50
- **called from:**
- `services/search/content.py:33`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_public_http_url` — function, line 64
- **called from:**
- `services/search/content.py:37`
- `tests/test_search_content_url_guards.py:20`
- `tests/test_search_content_url_guards.py:31`
- `tests/test_search_content_url_guards.py:36`
- `tests/test_security_regressions.py:848`
- `tests/test_security_regressions.py:849`
- `tests/test_security_regressions.py:850`
- `tests/test_security_regressions.py:860`
- `tests/test_security_regressions.py:900`
- `tests/test_security_regressions.py:905`
- `tests/test_security_regressions.py:912`
- `tests/test_security_regressions.py:919`

## `_resolve_public_ips` — function, line 92
- **called from:**
- `services/search/content.py:41`
- `tests/test_security_regressions.py:1299`

## `_PinnedBackend` — class, line 119
- **called from:**
- `services/memory/skill_importer.py:192`
- `src/outbound_fetch.py:171`
- `tests/test_security_regressions.py:1330`
- `tests/test_skill_importer_dns_pinning.py:39`
- `tests/test_skill_importer_dns_pinning.py:58`

## `_PinnedBackend.__init__` — method, line 122
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

## `_PinnedBackend.connect_tcp` — method, line 126
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

## `_PinnedBackend.connect_unix_socket` — method, line 138
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedBackend.sleep` — method, line 141
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

## `_PinnedTransport` — class, line 163
- **called from:**
- `services/memory/skill_importer.py:249`
- `tests/test_security_regressions.py:1386`
- `tests/test_security_regressions.py:1432`
- `tests/test_skill_importer_dns_pinning.py:86`
- `tests/test_skill_importer_dns_pinning.py:205`

## `_PinnedTransport.__init__` — method, line 166
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

## `_PinnedTransport.__enter__` — method, line 174
- **called from:**
- `src/outbound_fetch.py:175`
- `tests/test_caldav_test_connection_ssl.py:89`
- `tests/test_web_fetch_size_caps.py:45`
- `static/js/cookbookDownload.js:156`

## `_PinnedTransport.__exit__` — method, line 178
- **called from:**
- `src/outbound_fetch.py:179`
- `tests/test_caldav_test_connection_ssl.py:97`
- `tests/test_web_fetch_size_caps.py:51`
- `static/js/cookbookDownload.js:157`

## `_PinnedTransport.handle_request` — method, line 181
- **called from:**
- `services/memory/skill_importer.py:210`
- `src/outbound_fetch.py:195`
- `tests/test_security_regressions.py:1437`

## `_PinnedTransport.close` — method, line 210
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

## `BodyTooLargeError` — class, line 214
- **called from:**
- `src/outbound_fetch.py:327`

## `BodyTooLargeError.__init__` — method, line 217
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

## `_CappedFetch` — class, line 226
- **called from:**
- `src/outbound_fetch.py:301`
- `src/outbound_fetch.py:342`

## `_CappedFetch.__init__` — method, line 239
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

## `_CappedFetch.text` — method, line 258
- decorator: `property`
- **called from:**
- `core/database.py:502`
- `core/database.py:1543`
- `core/database.py:1546`
- `core/database.py:1565`
- `core/database.py:1567`
- `core/database.py:1584`
- `core/database.py:1587`
- `core/database.py:1590`
- `core/database.py:1610`
- `core/database.py:1614`
- `core/database.py:1625`
- `core/database.py:1626`
- `core/database.py:1654`
- `core/database.py:1664`
- `core/database.py:1675`
- `core/database.py:1684`
- `core/database.py:1694`
- `core/database.py:1696`
- `core/database.py:1706`
- `core/database.py:1708`
- `core/database.py:1723`
- `core/database.py:1725`
- `core/database.py:1740`
- `core/database.py:1743`
- `core/database.py:1745`
- `core/database.py:1760`
- `core/database.py:1764`
- `core/database.py:1776`
- `core/database.py:1778`
- `core/database.py:1789`
- `core/database.py:1791`
- `core/database.py:1794`
- `core/database.py:1796`
- `core/database.py:1806`
- `core/database.py:1808`
- `core/database.py:1812`
- `core/database.py:1955`
- `core/database.py:1976`
- `core/database.py:1979`
- `core/database.py:2025`
- `core/database.py:2030`
- `core/database.py:2093`
- `core/database.py:2204`
- `core/database.py:2207`
- `core/database.py:2378`
- `core/database.py:2382`
- `core/database.py:2403`
- `core/database.py:2415`
- `core/database.py:2435`
- `core/database.py:2449`
- `scripts/update_database.py:98`
- `scripts/update_database.py:108`
- `scripts/update_database.py:118`
- `scripts/update_database.py:124`
- `scripts/update_database.py:134`
- `scripts/update_database.py:145`
- `scripts/update_database.py:148`
- `services/search/providers.py:430`
- `src/session_search.py:121`
- `src/session_search.py:263`
- … +69 more (grep the name in repo)

## `_CappedFetch.raise_for_status` — method, line 261
- **called from:**
- `routes/email_helpers.py:125`
- `routes/email_routes.py:6066`
- `routes/embedding_routes.py:283`
- `routes/model_routes.py:943`
- `routes/model_routes.py:989`
- `routes/model_routes.py:1010`
- `routes/model_routes.py:1053`
- `routes/webhook/webhook_routes.py:346`
- `scripts/import_from_vllm_recipes.py:113`
- `services/search/content.py:230`
- `services/search/providers.py:193`
- `services/search/providers.py:325`
- `services/search/providers.py:395`
- `services/search/providers.py:495`
- `services/search/providers.py:553`
- `services/search/providers.py:614`
- `services/stt/stt_service.py:145`
- `services/tts/tts_service.py:190`
- `src/agent_tools/model_interaction_tools.py:164`
- `src/ai_interaction.py:159`
- `src/ai_interaction.py:1007`
- `src/copilot.py:160`
- `src/copilot.py:179`
- `src/copilot.py:192`
- `src/embeddings.py:123`
- `src/llm_core.py:2195`
- `src/llm_core.py:2212`
- `src/tools/image.py:42`

## `_get_public_url` — function, line 271
- **called from:**
- `services/search/content.py:51`
- `services/search/content.py:224`
- `tests/test_security_regressions.py:963`
- `tests/test_security_regressions.py:1496`
