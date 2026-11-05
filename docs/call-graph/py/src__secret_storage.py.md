# `src/secret_storage.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_or_create_key` — function, line 37
- **called from:**
- `routes/email/email_helpers.py:83`
- `routes/email/email_helpers.py:98`
- `src/secret_storage.py:53`
- `src/tool_approval_scopes.py:39`

## `_get_fernet` — function, line 50
- **called from:**
- `src/secret_storage.py:64`
- `src/secret_storage.py:77`

## `encrypt` — function, line 57
- **called from:**
- `core/database.py:180`
- `core/database.py:2717`
- `core/database.py:2744`
- `core/database.py:2746`
- `core/database.py:2777`
- `core/database.py:2779`
- `routes/calendar_routes.py:1028`
- `routes/calendar_routes.py:1078`
- `routes/calendar_routes.py:1107`
- `routes/contacts/contacts_routes.py:1012`
- `routes/cookbook_routes.py:461`
- `routes/embedding_routes.py:293`
- `scripts/demo_email/demo_account.py:137`
- `scripts/demo_email/demo_account.py:144`
- `src/api_key_manager.py:41`
- `src/integrations.py:176`
- `src/secret_storage.py:64`
- `tests/test_api_key_manager_resilience.py:15`
- `tests/test_carddav_password_encryption.py:42`
- `tests/test_carddav_password_encryption.py:58`
- `tests/test_carddav_password_encryption.py:140`
- `tests/test_carddav_password_encryption.py:159`
- `tests/test_carddav_password_encryption.py:163`
- `tests/test_cookbook_hf_token.py:16`
- `tests/test_cookbook_hf_token.py:34`
- `tests/test_security_regressions.py:60`
- `tests/test_security_regressions.py:67`
- `tests/test_security_regressions.py:75`
- `tests/test_security_regressions.py:76`
- `tests/test_security_regressions.py:89`
- `tests/test_security_regressions.py:112`

## `decrypt` — function, line 68
- **called from:**
- `core/database.py:186`
- `routes/calendar_routes.py:994`
- `routes/calendar_routes.py:1047`
- `routes/calendar_routes.py:1150`
- `routes/contacts/contacts_routes.py:56`
- `routes/cookbook_helpers.py:106`
- `routes/cookbook_routes.py:457`
- `scripts/audit_email_sft_with_deepseek.py:34`
- `scripts/audit_sft_corpus_with_deepseek.py:48`
- `scripts/odysseus_conversation_qa.py:294`
- `scripts/repair_email_sft_with_kimi.py:31`
- `scripts/repair_sft_corpus_with_kimi.py:27`
- `scripts/repair_sft_corpus_with_kimi.py:47`
- `src/api_key_manager.py:48`
- `src/caldav_sync.py:637`
- `src/caldav_writeback.py:290`
- `src/email_attachment_text.py:16`
- `src/embedding_lanes.py:106`
- `src/embeddings.py:272`
- `src/integrations.py:188`
- `src/secret_storage.py:77`
- `tests/test_security_regressions.py:62`
- `tests/test_security_regressions.py:68`
- `tests/test_security_regressions.py:84`
- `tests/test_security_regressions.py:100`

## `is_encrypted` — function, line 86
- **called from:**
- `core/database.py:2715`
- `core/database.py:2743`
- `core/database.py:2745`
- `core/database.py:2776`
- `core/database.py:2778`
- `src/integrations.py:195`
- `tests/test_security_regressions.py:90`
- `tests/test_security_regressions.py:91`
- `tests/test_security_regressions.py:92`
