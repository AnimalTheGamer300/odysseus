# `scripts/hf_download.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `PipeTqdm` — class, line 20
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `PipeTqdm.__init__` — method, line 23
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

## `PipeTqdm.__iter__` — method, line 39
- **called from:**
- `static/js/cookbookDownload.js:153`

## `PipeTqdm.__enter__` — method, line 46
- **called from:**
- `src/outbound_fetch.py:175`
- `tests/test_caldav_test_connection_ssl.py:89`
- `tests/test_web_fetch_size_caps.py:45`
- `static/js/cookbookDownload.js:156`

## `PipeTqdm.__exit__` — method, line 49
- **called from:**
- `src/outbound_fetch.py:179`
- `tests/test_caldav_test_connection_ssl.py:97`
- `tests/test_web_fetch_size_caps.py:51`
- `static/js/cookbookDownload.js:157`

## `PipeTqdm.__len__` — method, line 52
- **called from:**
- `static/js/cookbookDownload.js:158`

## `PipeTqdm.update` — method, line 55
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2770`
- `core/session_manager.py:606`
- `core/session_manager.py:1087`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:707`
- … +205 more (grep the name in repo)

## `PipeTqdm.set_description` — method, line 93
- **called from:**
- `static/js/cookbookDownload.js:170`

## `PipeTqdm.set_postfix` — method, line 96
- **called from:**
- `static/js/cookbookDownload.js:171`

## `PipeTqdm.set_postfix_str` — method, line 99
- **called from:**
- `static/js/cookbookDownload.js:172`

## `PipeTqdm.reset` — method, line 102
- **called from:**
- `mcp_servers/email_server.py:2899`
- `src/tool_execution.py:988`
- `tests/test_agent_state_dir_confinement.py:70`
- `tests/test_agent_state_dir_confinement.py:357`
- `tests/test_agent_state_dir_confinement.py:400`
- `tests/test_mcp_email_decode_header_spaces.py:177`
- `tests/test_workspace_confine.py:92`
- `static/js/admin.js:1160`
- `static/js/admin.js:1244`
- `static/js/admin.js:1248`
- `static/js/admin.js:1253`
- `static/js/admin.js:1258`
- `static/js/chat.js:2658`
- `static/js/chat.js:2659`
- `static/js/chat.js:2660`
- `static/js/chat.js:3072`
- `static/js/chat.js:4328`
- `static/js/chat.js:4329`
- `static/js/chat.js:4330`
- `static/js/compare/state.js:39`
- `static/js/cookbookDownload.js:173`
- `static/js/liveThinkingThrottle.js:116`
- `static/js/liveThinkingThrottle.js:137`
- `static/js/liveThinkingThrottle.js:158`
- `static/js/settings/search.js:65`
- `static/js/settings/search.js:76`
- `static/js/settings/search.js:139`
- `static/js/sidebar-layout.js:546`
- `static/js/theme.js:911`

## `PipeTqdm.refresh` — method, line 108
- **called from:**
- `routes/calendar_routes.py:1443`
- `routes/document/document_routes.py:174`
- `routes/document/document_routes.py:204`
- `routes/document/document_routes.py:317`
- `routes/document/document_routes.py:687`
- `routes/document/document_routes.py:726`
- `routes/document/document_routes.py:841`
- `routes/editor_draft_routes.py:128`
- `routes/editor_draft_routes.py:158`
- `routes/gallery/gallery_routes.py:978`
- `routes/note/note_routes.py:682`
- `routes/note/note_routes.py:754`
- `routes/signature_routes.py:121`
- `routes/task/task_routes.py:556`
- `routes/task/task_routes.py:751`
- `routes/task/task_routes.py:852`
- `src/bg_jobs.py:241`
- `src/bg_jobs.py:254`
- `src/bg_jobs.py:263`
- `src/chatgpt_subscription.py:271`
- `src/chatgpt_subscription.py:281`
- `static/js/chatRenderer.js:3112`
- `static/js/chatStream.js:171`
- `static/js/cookbookDownload.js:174`
- `static/js/editor/tools/transform-session.js:148`
- `static/js/editor/tools/transform-session.js:161`
- `static/js/search.js:42`
- `static/js/settings.js:488`
- `static/js/settings.js:775`
- `static/js/settings.js:1167`
- `static/js/slashAutocomplete.js:253`
- `static/js/slashAutocomplete.js:266`

## `PipeTqdm.close` — method, line 111
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

## `PipeTqdm.clear` — method, line 114
- **called from:**
- `app.py:334`
- `routes/admin_wipe/admin_wipe_routes.py:84`
- `routes/admin_wipe/admin_wipe_routes.py:101`
- `routes/email_routes.py:1643`
- `routes/model_routes.py:1394`
- `routes/session_routes.py:841`
- `routes/skills_routes.py:462`
- `scripts/diffusion_server.py:101`
- `services/search/core.py:228`
- `src/agent_jobs.py:108`
- `src/agent_jobs.py:119`
- `src/agent_jobs.py:120`
- `src/email_thread_parser.py:318`
- `src/llm_core.py:126`
- `src/llm_core.py:141`
- `src/llm_core.py:4116`
- `src/task_scheduler.py:441`
- `tests/test_api_token_routes.py:160`
- `tests/test_budget_auto_sentinel.py:72`
- `tests/test_budget_auto_sentinel.py:75`
- `tests/test_budget_auto_sentinel.py:80`
- `tests/test_caldav_writeback_route.py:104`
- `tests/test_companion_pairing.py:28`
- `tests/test_context_cache_per_endpoint.py:17`
- `tests/test_email_urgency_checkpoint.py:854`
- `tests/test_hwfit_cpu_arch_detection.py:10`
- `tests/test_hwfit_cpu_arch_detection.py:15`
- `tests/test_hwfit_remote_validation.py:79`
- `tests/test_hwfit_remote_validation.py:89`
- `tests/test_hwfit_unified_nvidia.py:113`
- `tests/test_hwfit_unified_nvidia.py:142`
- `tests/test_kimi_code_user_agent.py:63`
- `tests/test_kimi_code_user_agent.py:68`
- `tests/test_kimi_code_user_agent.py:79`
- `tests/test_kimi_code_user_agent.py:94`
- `tests/test_kimi_code_user_agent.py:98`
- `tests/test_kimi_code_user_agent.py:132`
- `tests/test_kimi_code_user_agent.py:136`
- `tests/test_kimi_code_user_agent.py:167`
- `tests/test_kimi_code_user_agent.py:171`
- `tests/test_kimi_code_user_agent.py:212`
- `tests/test_llm_core_async_mistral_content.py:36`
- `tests/test_llm_core_fallback.py:503`
- `tests/test_llm_core_fallback.py:537`
- `tests/test_llm_core_fallback.py:787`
- `tests/test_llm_core_fallback.py:788`
- `tests/test_llm_core_fallback.py:824`
- `tests/test_llm_core_fallback.py:825`
- `tests/test_llm_core_ollama.py:91`
- `tests/test_llm_core_temperature_moonshot.py:59`
- `tests/test_llm_core_temperature_reasoning.py:39`
- `tests/test_lmstudio_vision.py:35`
- `tests/test_lmstudio_vision.py:37`
- `tests/test_lmstudio_vision.py:131`
- `tests/test_lmstudio_vision.py:133`
- `tests/test_mcp_email_decode_header_spaces.py:23`
- `tests/test_mcp_email_decode_header_spaces.py:25`
- `tests/test_mcp_email_decode_header_spaces.py:98`
- `tests/test_mcp_email_decode_header_spaces.py:112`
- `tests/test_mcp_email_decode_header_spaces.py:170`
- … +110 more (grep the name in repo)

## `PipeTqdm.display` — method, line 117
- **called from:**
- `static/js/cookbookDownload.js:177`
- `static/js/document.js:1434`

## `PipeTqdm.format_dict` — method, line 121
- decorator: `property`
- **called from:**
- `static/js/cookbookDownload.js:179`

## `_patch_tqdm` — function, line 125
- **called from:**
- `scripts/hf_download.py:161`

## `main` — function, line 144
- **called from:**
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:218`
- `integrations/codex/scripts/odysseus_api.py:218`
- `scripts/add_hwfit_models.py:422`
- `scripts/agent_migration_manifest.py:635`
- `scripts/backfill_model_release_dates.py:133`
- `scripts/claim_ownerless.py:106`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:341`
- `scripts/index_documents.py:117`
- `scripts/migrate_searxng_settings.py:166`
- `scripts/mlx_image_server.py:470`
- `scripts/pr_blocker_audit.py:1051`
- `tests/run_focus.py:325`
- `tests/run_order_report.py:156`
- `tests/test_agent_migration_manifest.py:302`
- `tests/test_agent_migration_manifest.py:325`
- `tests/test_app.py:98`
- `tests/test_backup_import_skills_dedup.py:112`
- `tests/test_pr_blocker_audit.py:219`
- `tests/test_pr_blocker_audit.py:230`
- `tests/test_pr_blocker_audit.py:255`
- `tests/test_pr_blocker_audit.py:270`
- `tests/test_pr_blocker_audit.py:289`
- `tests/test_pr_blocker_audit.py:307`
- `tests/test_pr_blocker_audit.py:324`
- `tests/test_pr_blocker_audit.py:342`
- `tests/test_pr_blocker_audit.py:362`
- `tests/test_pr_blocker_audit.py:383`
- `tests/test_pr_blocker_audit.py:704`
- `tests/test_pr_blocker_audit.py:716`
- `tests/test_pr_blocker_audit.py:753`
- `tests/test_pr_blocker_audit.py:763`
- `tests/test_pr_blocker_audit.py:802`
- `tests/test_pr_blocker_audit.py:815`
- `tests/test_pr_blocker_audit.py:835`
- `tests/test_pr_blocker_audit.py:853`
- `tests/test_pr_blocker_audit.py:870`
- `tests/test_pr_blocker_audit.py:892`
- `tests/test_pr_blocker_audit.py:919`
- `tests/test_pr_blocker_audit.py:947`
- `tests/test_rag_search_signature.py:22`
- `tests/test_research_session_id_validation.py:55`
- `tests/test_setup_admin_user.py:61`
- `tests/tools/build_oversized_test_split_plan.py:574`
