# `services/memory/memory_extractor.py` — definitions & call sites

34 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_tidy_state_path` — function, line 26
- **called from:**
- `services/memory/memory_extractor.py:55`
- `services/memory/memory_extractor.py:65`

## `_fingerprint_entries` — function, line 35
- **called from:**
- `services/memory/memory_extractor.py:1005`
- `services/memory/memory_extractor.py:1152`
- `tests/test_memory_extractor_rows.py:5`
- `tests/test_memory_extractor_rows.py:11`

## `_memory_dicts` — function, line 48
- **called from:**
- `services/memory/memory_extractor.py:40`
- `services/memory/memory_extractor.py:503`
- `services/memory/memory_extractor.py:536`

## `_load_tidy_state` — function, line 54
- **called from:**
- `services/memory/memory_extractor.py:66`
- `services/memory/memory_extractor.py:1006`

## `_save_tidy_state` — function, line 64
- **called from:**
- `services/memory/memory_extractor.py:1152`

## `_extract_state_path` — function, line 78
- **called from:**
- `services/memory/memory_extractor.py:91`
- `services/memory/memory_extractor.py:103`

## `_load_extract_state` — function, line 90
- **called from:**
- `services/memory/memory_extractor.py:114`
- `services/memory/memory_extractor.py:119`
- `services/memory/memory_extractor.py:125`
- `services/memory/memory_extractor.py:130`

## `_save_extract_state` — function, line 102
- **called from:**
- `services/memory/memory_extractor.py:121`
- `services/memory/memory_extractor.py:132`

## `_last_extracted_count` — function, line 113
- **called from:**
- `services/memory/memory_extractor.py:622`

## `_set_last_extracted_count` — function, line 118
- **called from:**
- `services/memory/memory_extractor.py:702`

## `_pending_audit_count` — function, line 124
- **called from:**
- `services/memory/memory_extractor.py:867`

## `_set_pending_audit_count` — function, line 129
- **called from:**
- `services/memory/memory_extractor.py:874`

## `_is_owner_memory` — function, line 214
- **called from:**
- `services/memory/memory_extractor.py:743`

## `_is_auto_pinned_identity` — function, line 220
- **called from:**
- `services/memory/memory_extractor.py:743`

## `_message_text` — function, line 236
- **called from:**
- `routes/history/history_routes.py:1520`
- `routes/session_routes.py:1378`
- `routes/session_routes.py:1429`
- `services/memory/memory_extractor.py:338`

## `_message_role` — function, line 253
- **called from:**
- `routes/history/history_routes.py:1519`
- `routes/session_routes.py:818`
- `routes/session_routes.py:868`
- `services/memory/memory_extractor.py:336`

## `_clean_memory_value` — function, line 260
- **called from:**
- `services/memory/memory_extractor.py:326`
- `services/memory/memory_extractor.py:347`
- `services/memory/memory_extractor.py:353`
- `services/memory/memory_extractor.py:359`
- `services/memory/memory_extractor.py:378`
- `services/memory/memory_extractor.py:384`
- `services/memory/memory_extractor.py:395`

## `_is_deictic_preference` — function, line 287
- **called from:**
- `services/memory/memory_extractor.py:385`

## `_is_pinnable_identity` — function, line 307
- **called from:**
- `services/memory/memory_extractor.py:833`

## `_fallback_memory_candidates` — function, line 315
- **called from:**
- `services/memory/memory_extractor.py:722`
- `tests/test_memory_fallback_dislike.py:13`

## `add` — function, line 325
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:554`
- `core/database.py:2269`
- `core/platform_compat.py:227`
- `core/session_manager.py:418`
- `core/session_manager.py:480`
- `core/session_manager.py:714`
- `core/session_manager.py:763`
- `core/session_manager.py:950`
- `mcp_servers/email_server.py:65`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1027`
- `mcp_servers/email_server.py:1261`
- `mcp_servers/email_server.py:1345`
- `mcp_servers/email_server.py:2037`
- `mcp_servers/email_server.py:2224`
- `mcp_servers/email_server.py:2859`
- `mcp_servers/email_server.py:2905`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:3075`
- `mcp_servers/email_server.py:3435`
- `mcp_servers/email_server.py:3441`
- `mcp_servers/email_server.py:3502`
- `mcp_servers/image_gen_server.py:144`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:202`
- `routes/calendar_routes.py:330`
- `routes/calendar_routes.py:338`
- `routes/calendar_routes.py:760`
- `routes/calendar_routes.py:1390`
- `routes/calendar_routes.py:1545`
- `routes/calendar_routes.py:1612`
- `routes/calendar_routes.py:1713`
- `routes/chat_helpers.py:371`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:3606`
- `routes/chat_routes.py:3707`
- `routes/chat_routes.py:3943`
- `routes/chatgpt_subscription_routes.py:91`
- `routes/chatgpt_subscription_routes.py:155`
- `routes/chatgpt_subscription_routes.py:185`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:590`
- `routes/contacts/contacts_routes.py:718`
- `routes/cookbook_routes.py:1479`
- `routes/cookbook_routes.py:1837`
- `routes/cookbook_routes.py:2885`
- `routes/cookbook_routes.py:3694`
- `routes/cookbook_routes.py:3761`
- `routes/cookbook_routes.py:3877`
- `routes/cookbook_routes.py:3964`
- `routes/copilot_routes.py:77`
- … +2020 more (grep the name in repo)

## `_dedup_tokens` — function, line 412
- **called from:**
- `services/memory/memory_extractor.py:499`
- `services/memory/memory_extractor.py:505`

## `_content_tokens` — function, line 448
- **called from:**
- `src/chat_processor.py:177`
- `src/chat_processor.py:198`

## `_name_slot` — function, line 454
- **called from:**
- `services/memory/memory_extractor.py:479`
- `services/memory/memory_extractor.py:502`
- `services/memory/memory_extractor.py:521`
- `services/memory/memory_extractor.py:531`
- `services/memory/memory_extractor.py:537`

## `_name_slot_tokens` — function, line 478
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_name_vals_close` — function, line 483
- **called from:**
- `services/memory/memory_extractor.py:523`
- `services/memory/memory_extractor.py:541`

## `_is_text_duplicate` — function, line 497
- **called from:**
- `services/memory/memory_extractor.py:823`
- `tests/test_memory_extraction_evidence.py:5`
- `tests/test_memory_extraction_evidence.py:6`
- `tests/test_memory_extractor_rows.py:25`

## `_name_enrichment_target` — function, line 528
- **called from:**
- `services/memory/memory_extractor.py:764`
- `services/memory/memory_extractor.py:804`

## `_parse_extraction_json` — function, line 547
- **called from:**
- `services/memory/memory_extractor.py:707`
- `tests/test_memory_extraction_parse.py:14`
- `tests/test_memory_extraction_parse.py:19`
- `tests/test_memory_extraction_parse.py:24`
- `tests/test_memory_extraction_parse.py:31`
- `tests/test_memory_extraction_parse.py:35`
- `tests/test_memory_extraction_parse.py:36`

## `extract_and_store` — function (async), line 584
- **called from:**
- `routes/chat_helpers.py:2102`
- `tests/test_memory_extractor_vector_cross_tenant.py:125`
- `tests/test_memory_extractor_vector_cross_tenant.py:155`
- `tests/test_memory_extractor_vector_cross_tenant.py:180`
- `tests/test_memory_extractor_vector_degraded.py:71`
- `tests/test_memory_extractor_vector_degraded.py:119`
- `tests/test_utility_reasoning_effort.py:412`

## `_flatten_msg` — function, line 660
- **called from:**
- `services/memory/memory_extractor.py:669`

## `update_persona_memory` — function (async), line 882
- **called from:**
- `routes/chat_helpers.py:2122`
- `services/memory/memory_extractor.py:964`
- `tests/test_preset_atomic_save.py:73`

## `audit_memories` — function (async), line 970
- **called from:**
- `routes/memory/memory_routes.py:319`
- `services/memory/memory_extractor.py:871`

## `_loads_list` — function, line 1049
- **called from:**
- `services/memory/memory_extractor.py:1061`
- `services/memory/memory_extractor.py:1067`
- `services/memory/memory_extractor.py:1071`
