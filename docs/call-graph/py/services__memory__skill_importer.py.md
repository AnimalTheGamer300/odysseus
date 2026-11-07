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
- `services/memory/skills.py:468`
- `tests/test_skill_importer_ssrf_redirect.py:120`

## `_safe_relpath` — function, line 57
- **called from:**
- `services/memory/skill_importer.py:343`
- `services/memory/skill_importer.py:348`
- `services/memory/skill_importer.py:416`
- `services/memory/skill_importer.py:439`
- `services/memory/skills.py:486`

## `_is_text_file` — function, line 67
- **called from:**
- `services/memory/skill_importer.py:421`
- `src/document_processor.py:388`
- `src/document_processor.py:996`
- `tests/test_nix_upload_text.py:9`

## `_validated_ips` — function, line 78
- **called from:**
- `services/memory/skill_importer.py:113`
- `src/integrations.py:589`
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
- `tests/test_security_regressions.py:1332`
- `tests/test_skill_importer_dns_pinning.py:39`
- `tests/test_skill_importer_dns_pinning.py:58`

## `_PinnedBackend.__init__` — method, line 126
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

## `_PinnedBackend.connect_tcp` — method, line 130
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

## `_PinnedBackend.connect_unix_socket` — method, line 158
- **called from:**
- `services/memory/skill_importer.py:159`
- `src/integrations.py:413`
- `src/outbound_fetch.py:139`
- `src/webhook_manager.py:196`

## `_PinnedBackend.sleep` — method, line 161
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

## `_PinnedTransport` — class, line 183
- **called from:**
- `services/memory/skill_importer.py:249`
- `src/agent_tools/web_tools.py:1259`
- `src/agent_tools/web_tools_prewave3.py:1263`
- `tests/test_security_regressions.py:1388`
- `tests/test_security_regressions.py:1434`
- `tests/test_skill_importer_dns_pinning.py:86`
- `tests/test_skill_importer_dns_pinning.py:205`

## `_PinnedTransport.__init__` — method, line 186
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

## `_PinnedTransport.handle_request` — method, line 195
- **called from:**
- `services/memory/skill_importer.py:210`
- `src/outbound_fetch.py:195`
- `tests/test_security_regressions.py:1439`

## `_PinnedTransport.close` — method, line 228
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
- `routes/skills_routes.py:470`

## `pick_skill_md` — function, line 479
- **called from:**
- `services/memory/skills.py:469`

## `default_category_from_source` — function, line 486
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
