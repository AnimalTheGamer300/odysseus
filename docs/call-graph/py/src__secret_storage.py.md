# `src/secret_storage.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_or_create_key` — function, line 37
- **called from:**
- `routes/email_helpers.py:79`
- `routes/email_helpers.py:94`
- `src/secret_storage.py:53`
- `src/tool_approval_scopes.py:39`

## `_get_fernet` — function, line 50
- **called from:**
- `src/secret_storage.py:64`
- `src/secret_storage.py:77`

## `encrypt` — function, line 57
- **called from:**
- `core/database.py:180`
- `core/database.py:2383`
- `core/database.py:2410`
- `core/database.py:2412`
- `core/database.py:2443`
- `core/database.py:2445`
- `routes/calendar_routes.py:882`
- `routes/calendar_routes.py:935`
- `routes/calendar_routes.py:967`
- `routes/contacts/contacts_routes.py:874`
- `routes/cookbook_routes.py:422`
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
- `tests/test_security_regressions.py:59`
- `tests/test_security_regressions.py:66`
- `tests/test_security_regressions.py:74`
- `tests/test_security_regressions.py:75`
- `tests/test_security_regressions.py:88`
- `tests/test_security_regressions.py:111`

## `decrypt` — function, line 68
- **called from:**
- `core/database.py:186`
- `routes/calendar_routes.py:845`
- `routes/calendar_routes.py:901`
- `routes/calendar_routes.py:1013`
- `routes/contacts/contacts_routes.py:53`
- `routes/cookbook_helpers.py:105`
- `routes/cookbook_routes.py:418`
- `src/api_key_manager.py:48`
- `src/caldav_sync.py:637`
- `src/caldav_writeback.py:290`
- `src/embedding_lanes.py:106`
- `src/embeddings.py:257`
- `src/integrations.py:188`
- `src/secret_storage.py:77`
- `tests/test_security_regressions.py:61`
- `tests/test_security_regressions.py:67`
- `tests/test_security_regressions.py:83`
- `tests/test_security_regressions.py:99`

## `is_encrypted` — function, line 86
- **called from:**
- `core/database.py:2381`
- `core/database.py:2409`
- `core/database.py:2411`
- `core/database.py:2442`
- `core/database.py:2444`
- `src/integrations.py:195`
- `tests/test_security_regressions.py:89`
- `tests/test_security_regressions.py:90`
- `tests/test_security_regressions.py:91`
