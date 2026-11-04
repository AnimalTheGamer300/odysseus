# `services/memory/memory_extractor.py` — definitions & call sites

26 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_tidy_state_path` — function, line 25
- **called from:**
- `services/memory/memory_extractor.py:54`
- `services/memory/memory_extractor.py:64`

## `_fingerprint_entries` — function, line 34
- **called from:**
- `services/memory/memory_extractor.py:712`
- `services/memory/memory_extractor.py:855`
- `tests/test_memory_extractor_rows.py:5`
- `tests/test_memory_extractor_rows.py:11`

## `_memory_dicts` — function, line 47
- **called from:**
- `services/memory/memory_extractor.py:39`
- `services/memory/memory_extractor.py:379`

## `_load_tidy_state` — function, line 53
- **called from:**
- `services/memory/memory_extractor.py:65`
- `services/memory/memory_extractor.py:713`

## `_save_tidy_state` — function, line 63
- **called from:**
- `services/memory/memory_extractor.py:855`

## `_extract_state_path` — function, line 77
- **called from:**
- `services/memory/memory_extractor.py:90`
- `services/memory/memory_extractor.py:102`

## `_load_extract_state` — function, line 89
- **called from:**
- `services/memory/memory_extractor.py:113`
- `services/memory/memory_extractor.py:118`
- `services/memory/memory_extractor.py:124`
- `services/memory/memory_extractor.py:129`

## `_save_extract_state` — function, line 101
- **called from:**
- `services/memory/memory_extractor.py:120`
- `services/memory/memory_extractor.py:131`

## `_last_extracted_count` — function, line 112
- **called from:**
- `services/memory/memory_extractor.py:464`

## `_set_last_extracted_count` — function, line 117
- **called from:**
- `services/memory/memory_extractor.py:541`

## `_pending_audit_count` — function, line 123
- **called from:**
- `services/memory/memory_extractor.py:663`

## `_set_pending_audit_count` — function, line 128
- **called from:**
- `services/memory/memory_extractor.py:670`

## `_message_text` — function, line 192
- **called from:**
- `routes/history/history_routes.py:1084`
- `routes/session_routes.py:1157`
- `services/memory/memory_extractor.py:294`

## `_message_role` — function, line 209
- **called from:**
- `routes/history/history_routes.py:1083`
- `routes/session_routes.py:624`
- `routes/session_routes.py:674`
- `services/memory/memory_extractor.py:292`

## `_clean_memory_value` — function, line 216
- **called from:**
- `services/memory/memory_extractor.py:282`
- `services/memory/memory_extractor.py:300`
- `services/memory/memory_extractor.py:306`
- `services/memory/memory_extractor.py:312`
- `services/memory/memory_extractor.py:331`
- `services/memory/memory_extractor.py:337`
- `services/memory/memory_extractor.py:348`

## `_is_deictic_preference` — function, line 243
- **called from:**
- `services/memory/memory_extractor.py:338`

## `_is_pinnable_identity` — function, line 263
- **called from:**
- `services/memory/memory_extractor.py:631`

## `_fallback_memory_candidates` — function, line 271
- **called from:**
- `services/memory/memory_extractor.py:560`
- `tests/test_memory_fallback_dislike.py:13`

## `add` — function, line 281
- **called from:**
- `companion/pairing.py:196`
- `core/database.py:517`
- `core/database.py:1972`
- `core/platform_compat.py:205`
- `core/session_manager.py:402`
- `core/session_manager.py:464`
- `core/session_manager.py:698`
- `core/session_manager.py:747`
- `core/session_manager.py:924`
- `mcp_servers/email_server.py:552`
- `mcp_servers/email_server.py:1665`
- `mcp_servers/email_server.py:1706`
- `mcp_servers/email_server.py:1707`
- `mcp_servers/email_server.py:1828`
- `mcp_servers/image_gen_server.py:143`
- `mcp_servers/memory_server.py:190`
- `mcp_servers/memory_server.py:219`
- `routes/api_token_routes.py:135`
- `routes/api_token_routes.py:179`
- `routes/backup_routes.py:105`
- `routes/backup_routes.py:176`
- `routes/backup_routes.py:178`
- `routes/backup_routes.py:179`
- `routes/calendar_routes.py:190`
- `routes/calendar_routes.py:316`
- `routes/calendar_routes.py:324`
- `routes/calendar_routes.py:1253`
- `routes/calendar_routes.py:1374`
- `routes/calendar_routes.py:1441`
- `routes/calendar_routes.py:1540`
- `routes/chat_helpers.py:86`
- `routes/chat_routes.py:1688`
- `routes/chat_routes.py:1742`
- `routes/chatgpt_subscription_routes.py:54`
- `routes/chatgpt_subscription_routes.py:79`
- `routes/compare/compare_routes.py:218`
- `routes/compare/compare_routes.py:313`
- `routes/contacts/contacts_routes.py:476`
- `routes/contacts/contacts_routes.py:604`
- `routes/cookbook_routes.py:1579`
- `routes/cookbook_routes.py:1916`
- `routes/cookbook_routes.py:3006`
- `routes/cookbook_routes.py:3788`
- `routes/cookbook_routes.py:3855`
- `routes/cookbook_routes.py:3971`
- `routes/cookbook_routes.py:4058`
- `routes/copilot_routes.py:77`
- `routes/device_flow.py:154`
- `routes/document/document_routes.py:165`
- `routes/document/document_routes.py:201`
- `routes/document/document_routes.py:202`
- `routes/document/document_routes.py:545`
- `routes/document/document_routes.py:604`
- `routes/document/document_routes.py:683`
- `routes/document/document_routes.py:839`
- `routes/editor_draft_routes.py:126`
- `routes/email_helpers.py:1700`
- `routes/email_helpers.py:1732`
- `routes/email_helpers.py:1868`
- `routes/email_pollers.py:810`
- … +1221 more (grep the name in repo)

## `_dedup_tokens` — function, line 364
- **called from:**
- `services/memory/memory_extractor.py:376`
- `services/memory/memory_extractor.py:380`

## `_is_text_duplicate` — function, line 374
- **called from:**
- `services/memory/memory_extractor.py:622`
- `tests/test_memory_extractor_rows.py:25`

## `_parse_extraction_json` — function, line 390
- **called from:**
- `services/memory/memory_extractor.py:546`
- `tests/test_memory_extraction_parse.py:14`
- `tests/test_memory_extraction_parse.py:19`
- `tests/test_memory_extraction_parse.py:24`
- `tests/test_memory_extraction_parse.py:31`
- `tests/test_memory_extraction_parse.py:35`
- `tests/test_memory_extraction_parse.py:36`

## `extract_and_store` — function (async), line 427
- **called from:**
- `routes/chat_helpers.py:1428`
- `tests/test_memory_extractor_vector_cross_tenant.py:112`
- `tests/test_memory_extractor_vector_degraded.py:71`
- `tests/test_memory_extractor_vector_degraded.py:119`

## `_flatten_msg` — function, line 502
- **called from:**
- `services/memory/memory_extractor.py:511`

## `audit_memories` — function (async), line 678
- **called from:**
- `routes/memory/memory_routes.py:316`
- `services/memory/memory_extractor.py:667`

## `_loads_list` — function, line 754
- **called from:**
- `services/memory/memory_extractor.py:766`
- `services/memory/memory_extractor.py:770`
- `services/memory/memory_extractor.py:774`
