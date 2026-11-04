# `services/memory/skill_importer.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_github_host` — function, line 33
- **called from:**
- `services/memory/skill_importer.py:38`
- `services/memory/skill_importer.py:300`

## `_assert_github_url` — function, line 37
- **called from:**
- `services/memory/skill_importer.py:313`
- `services/memory/skill_importer.py:383`
- `services/memory/skill_importer.py:404`
- `services/memory/skill_importer.py:426`
- `tests/test_skill_importer.py:87`

## `ResolvedSource` — class, line 46
- decorator: `dataclass`
- **called from:**
- `services/memory/skill_importer.py:322`
- `services/memory/skill_importer.py:339`
- `tests/test_skill_importer.py:130`
- `tests/test_skill_importer.py:162`

## `SkillImportError` — class, line 53
- **called from:**
- `services/memory/skill_importer.py:40`
- `services/memory/skill_importer.py:60`
- `services/memory/skill_importer.py:63`
- `services/memory/skill_importer.py:111`
- `services/memory/skill_importer.py:115`
- `services/memory/skill_importer.py:262`
- `services/memory/skill_importer.py:269`
- `services/memory/skill_importer.py:278`
- `services/memory/skill_importer.py:282`
- `services/memory/skill_importer.py:288`
- `services/memory/skill_importer.py:301`
- `services/memory/skill_importer.py:319`
- `services/memory/skill_importer.py:326`
- `services/memory/skill_importer.py:337`
- `services/memory/skill_importer.py:368`
- `services/memory/skill_importer.py:373`
- `services/memory/skill_importer.py:375`
- `services/memory/skill_importer.py:376`
- `services/memory/skill_importer.py:385`
- `services/memory/skill_importer.py:394`
- `services/memory/skill_importer.py:407`
- `services/memory/skill_importer.py:430`
- `services/memory/skill_importer.py:473`
- `services/memory/skill_importer.py:483`
- `services/memory/skills.py:397`
- `tests/test_skill_importer_ssrf_redirect.py:120`

## `_safe_relpath` — function, line 57
- **called from:**
- `services/memory/skill_importer.py:343`
- `services/memory/skill_importer.py:348`
- `services/memory/skill_importer.py:416`
- `services/memory/skill_importer.py:439`
- `services/memory/skills.py:415`

## `_is_text_file` — function, line 67
- **called from:**
- `services/memory/skill_importer.py:421`
- `src/document_processor.py:845`
- `tests/test_nix_upload_text.py:9`

## `_validated_ips` — function, line 78
- **called from:**
- `services/memory/skill_importer.py:113`
- `src/integrations.py:583`
- `tests/test_integration_api_call_ssrf.py:315`
- `tests/test_integration_api_call_ssrf.py:326`
- `tests/test_integration_api_call_ssrf.py:332`
- `tests/test_integration_api_call_ssrf.py:338`

## `_resolve_and_check_url` — function, line 96
- **called from:**
- `services/memory/skill_importer.py:247`

## `_recording_resolver` — function, line 100
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_PinnedBackend` — class, line 123
- **called from:**
- `services/memory/skill_importer.py:192`
- `src/outbound_fetch.py:171`
- `tests/test_security_regressions.py:1330`
- `tests/test_skill_importer_dns_pinning.py:39`
- `tests/test_skill_importer_dns_pinning.py:58`

## `_PinnedBackend.__init__` — method, line 126
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

## `_PinnedBackend.connect_tcp` — method, line 130
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

## `_PinnedBackend.connect_unix_socket` — method, line 158
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedBackend.sleep` — method, line 161
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

## `_PinnedTransport` — class, line 183
- **called from:**
- `services/memory/skill_importer.py:249`
- `tests/test_security_regressions.py:1386`
- `tests/test_security_regressions.py:1432`
- `tests/test_skill_importer_dns_pinning.py:86`
- `tests/test_skill_importer_dns_pinning.py:205`

## `_PinnedTransport.__init__` — method, line 186
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

## `_PinnedTransport.handle_request` — method, line 195
- **called from:**
- `services/memory/skill_importer.py:210`
- `src/outbound_fetch.py:195`
- `tests/test_security_regressions.py:1437`

## `_PinnedTransport.close` — method, line 228
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

## `_get_checked` — function, line 232
- **called from:**
- `services/memory/skill_importer.py:296`
- `services/memory/skill_importer.py:380`
- `services/memory/skill_importer.py:401`
- `tests/test_skill_importer_dns_pinning.py:144`
- `tests/test_skill_importer_ssrf_redirect.py:100`
- `tests/test_skill_importer_ssrf_redirect.py:133`

## `parse_skill_source` — function, line 265
- **called from:**
- `services/memory/skill_importer.py:436`
- `tests/test_skill_importer.py:24`
- `tests/test_skill_importer.py:34`
- `tests/test_skill_importer.py:44`
- `tests/test_skill_importer.py:55`
- `tests/test_skill_importer_security.py:30`
- `tests/test_skill_importer_security.py:43`
- `tests/test_skill_importer_security.py:67`
- `tests/test_skill_importer_security.py:90`
- `tests/test_skill_importer_security.py:105`
- `tests/test_skill_importer_security.py:111`
- `tests/test_skill_importer_ssrf_redirect.py:125`

## `_raw_url` — function, line 342
- **called from:**
- `services/memory/skill_importer.py:441`
- `services/memory/skill_importer.py:452`
- `services/memory/skill_importer.py:458`
- `services/memory/skill_importer.py:471`

## `_api_contents_url` — function, line 347
- **called from:**
- `services/memory/skill_importer.py:400`

## `_github_response_error` — function, line 355
- **called from:**
- `services/memory/skill_importer.py:298`
- `services/memory/skill_importer.py:382`
- `services/memory/skill_importer.py:403`

## `_fetch_bytes` — function, line 379
- **called from:**
- `services/memory/skill_importer.py:390`
- `tests/test_skill_importer.py:83`
- `tests/test_skill_importer.py:178`
- `tests/test_skill_importer_ssrf_redirect.py:108`

## `_fetch_text` — function, line 389
- **called from:**
- `services/memory/skill_importer.py:427`
- `services/memory/skill_importer.py:441`
- `services/memory/skill_importer.py:452`
- `services/memory/skill_importer.py:458`
- `services/memory/skill_importer.py:471`

## `_list_github_dir` — function, line 397
- **called from:**
- `services/memory/skill_importer.py:418`
- `services/memory/skill_importer.py:445`
- `services/memory/skill_importer.py:453`
- `services/memory/skill_importer.py:464`
- `services/memory/skill_importer.py:466`
- `tests/test_skill_importer.py:131`
- `tests/test_skill_importer.py:164`

## `fetch_skill_bundle` — function, line 434
- **called from:**
- `routes/skills_routes.py:1361`

## `pick_skill_md` — function, line 479
- **called from:**
- `services/memory/skills.py:398`

## `default_category_from_source` — function, line 486
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
