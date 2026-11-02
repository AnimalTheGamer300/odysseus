# `src/outbound_fetch.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_is_private_address` — function, line 36
- **called from:**
- `services/search/content.py:34`
- `src/outbound_fetch.py:83`
- `src/outbound_fetch.py:87`
- `src/outbound_fetch.py:106`
- `src/outbound_fetch.py:114`

## `_resolve_hostname_ips` — function, line 50
- **called from:**
- `services/search/content.py:38`
- `src/url_security.py:68`
- `src/webhook_manager.py:106`
- `src/webhook_manager.py:153`

## `_public_http_url` — function, line 64
- **called from:**
- `services/search/content.py:42`
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
- `services/search/content.py:46`
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
- `core/database.py:930`
- `core/database.py:961`
- `core/database.py:984`
- `core/database.py:1009`
- `core/database.py:1032`
- `core/database.py:1055`
- `core/database.py:1086`
- `core/database.py:1111`
- `core/database.py:1135`
- `core/database.py:1163`
- `core/database.py:1186`
- `core/database.py:1209`
- `core/database.py:1232`
- `core/database.py:1255`
- `core/database.py:1287`
- `core/database.py:1310`
- `core/database.py:1333`
- `core/database.py:1357`
- `core/database.py:1381`
- `core/database.py:1415`
- `core/database.py:1444`
- `core/database.py:1517`
- `core/database.py:2106`
- `core/database.py:2340`
- `core/database.py:2402`
- `core/database.py:2518`
- `core/database.py:2545`
- `core/database.py:2571`
- `core/database.py:2596`
- `core/database.py:2623`
- `core/database.py:2645`
- `core/database.py:2658`
- `core/database.py:2674`
- `core/session_manager.py:68`
- `core/session_manager.py:178`
- `core/session_manager.py:442`
- `core/session_manager.py:582`
- `core/session_manager.py:654`
- `core/session_manager.py:689`
- `core/session_manager.py:760`
- `core/session_manager.py:880`
- `core/session_manager.py:984`
- `core/session_manager.py:1014`
- `core/session_manager.py:1028`
- `core/session_manager.py:1074`
- `core/session_manager.py:1118`
- `core/session_manager.py:1149`
- `core/session_manager.py:1173`
- `core/session_manager.py:1209`
- `core/session_manager.py:1233`
- `core/session_manager.py:1253`
- … +763 more (grep the name in repo)

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
- `core/database.py:509`
- `core/database.py:1581`
- `core/database.py:1584`
- `core/database.py:1603`
- `core/database.py:1605`
- `core/database.py:1622`
- `core/database.py:1625`
- `core/database.py:1628`
- `core/database.py:1648`
- `core/database.py:1652`
- `core/database.py:1663`
- `core/database.py:1664`
- `core/database.py:1692`
- `core/database.py:1702`
- `core/database.py:1713`
- `core/database.py:1722`
- `core/database.py:1732`
- `core/database.py:1734`
- `core/database.py:1744`
- `core/database.py:1746`
- `core/database.py:1761`
- `core/database.py:1763`
- `core/database.py:1778`
- `core/database.py:1781`
- `core/database.py:1783`
- `core/database.py:1798`
- `core/database.py:1802`
- `core/database.py:1814`
- `core/database.py:1816`
- `core/database.py:1827`
- `core/database.py:1829`
- `core/database.py:1832`
- `core/database.py:1834`
- `core/database.py:1844`
- `core/database.py:1846`
- `core/database.py:1850`
- `core/database.py:1993`
- `core/database.py:2014`
- `core/database.py:2017`
- `core/database.py:2063`
- `core/database.py:2068`
- `core/database.py:2131`
- `core/database.py:2243`
- `core/database.py:2246`
- `core/database.py:2417`
- `core/database.py:2421`
- `core/database.py:2442`
- `core/database.py:2454`
- `core/database.py:2474`
- `core/database.py:2488`
- `scripts/update_database.py:98`
- `scripts/update_database.py:108`
- `scripts/update_database.py:118`
- `scripts/update_database.py:124`
- `scripts/update_database.py:134`
- `scripts/update_database.py:145`
- `scripts/update_database.py:148`
- `services/search/providers.py:430`
- `src/session_search.py:121`
- `src/session_search.py:265`
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
- `services/search/content.py:395`
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
- `src/llm_core.py:2227`
- `src/llm_core.py:2244`

## `_get_public_url` — function, line 271
- **called from:**
- `services/search/content.py:56`
- `services/search/content.py:389`
- `tests/test_security_regressions.py:963`
- `tests/test_security_regressions.py:1496`
