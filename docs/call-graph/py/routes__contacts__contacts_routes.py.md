# `routes/contacts/contacts_routes.py` — definitions & call sites

37 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_settings` — function, line 36
- **called from:**
- `routes/auth_routes.py:721`
- `routes/auth_routes.py:733`
- `routes/auth_routes.py:840`
- `routes/contacts/contacts_routes.py:49`
- `routes/contacts/contacts_routes.py:862`
- `routes/email_helpers.py:1100`
- `routes/email_pollers.py:392`
- `routes/email_pollers.py:411`
- `routes/email_pollers.py:516`
- `routes/email_pollers.py:1376`
- `routes/email_routes.py:4872`
- `routes/email_routes.py:5194`
- `routes/email_routes.py:5449`
- `routes/email_routes.py:5461`
- `routes/email_routes.py:5487`
- `routes/email_routes.py:5527`
- `routes/model_routes.py:165`
- `routes/model_routes.py:2182`
- `routes/model_routes.py:2434`
- `routes/model_routes.py:2587`
- `routes/model_routes.py:2591`
- `routes/model_routes.py:2700`
- `routes/model_routes.py:2714`
- `services/stt/stt_service.py:42`
- `services/stt/stt_service.py:66`
- `services/stt/stt_service.py:157`
- `services/stt/stt_service.py:177`
- `services/tts/tts_service.py:66`
- `services/tts/tts_service.py:200`
- `services/tts/tts_service.py:254`
- `src/agent_loop.py:2759`
- `src/agent_loop.py:2993`
- `src/builtin_actions.py:3298`
- `tests/test_carddav_password_encryption.py:39`
- `tests/test_carddav_password_encryption.py:145`
- `tests/test_carddav_password_encryption.py:158`
- `tests/test_carddav_password_encryption.py:162`

## `_save_settings` — function, line 42
- **called from:**
- `routes/auth_routes.py:754`
- `routes/contacts/contacts_routes.py:876`
- `routes/email_pollers.py:402`
- `routes/email_pollers.py:417`
- `routes/email_routes.py:4874`
- `routes/email_routes.py:5463`
- `routes/email_routes.py:5535`
- `routes/model_routes.py:174`
- `routes/model_routes.py:2204`
- `routes/model_routes.py:2594`
- `routes/model_routes.py:2716`
- `src/builtin_actions.py:3309`
- `tests/test_carddav_password_encryption.py:43`
- `tests/test_carddav_password_encryption.py:143`
- `tests/test_carddav_password_encryption.py:146`
- `tests/test_carddav_password_encryption.py:160`
- `tests/test_carddav_password_encryption.py:164`

## `_get_carddav_config` — function, line 47
- **called from:**
- `routes/contacts/contacts_routes.py:62`
- `routes/contacts/contacts_routes.py:277`
- `routes/contacts/contacts_routes.py:347`
- `routes/contacts/contacts_routes.py:401`
- `routes/contacts/contacts_routes.py:449`
- `routes/contacts/contacts_routes.py:459`
- `routes/contacts/contacts_routes.py:655`
- `routes/contacts/contacts_routes.py:699`
- `routes/contacts/contacts_routes.py:854`
- `tests/test_carddav_password_encryption.py:50`
- `tests/test_carddav_password_encryption.py:66`
- `tests/test_carddav_password_encryption.py:82`
- `tests/test_carddav_password_encryption.py:96`
- `tests/test_carddav_password_encryption.py:110`
- `tests/test_carddav_password_encryption.py:123`
- `tests/test_carddav_password_encryption.py:130`
- `tests/test_carddav_password_encryption.py:148`
- `tests/test_carddav_password_encryption.py:169`

## `_carddav_configured` — function, line 61
- **called from:**
- `routes/contacts/contacts_routes.py:348`
- `routes/contacts/contacts_routes.py:402`
- `routes/contacts/contacts_routes.py:656`
- `routes/contacts/contacts_routes.py:700`

## `_validate_carddav_url` — function, line 66
- **called from:**
- `routes/contacts/contacts_routes.py:78`
- `routes/contacts/contacts_routes.py:284`
- `routes/contacts/contacts_routes.py:867`
- `tests/test_contacts_carddav_security.py:16`
- `tests/test_contacts_carddav_security.py:27`

## `_carddav_base_url` — function, line 77
- **called from:**
- `routes/contacts/contacts_routes.py:278`
- `routes/contacts/contacts_routes.py:355`
- `routes/contacts/contacts_routes.py:422`
- `routes/contacts/contacts_routes.py:450`
- `routes/contacts/contacts_routes.py:482`

## `_normalize_contact` — function, line 81
- **called from:**
- `routes/contacts/contacts_routes.py:111`
- `routes/contacts/contacts_routes.py:120`
- `routes/contacts/contacts_routes.py:121`
- `routes/contacts/contacts_routes.py:410`
- `routes/contacts/contacts_routes.py:474`
- `routes/contacts/contacts_routes.py:665`
- `routes/contacts/contacts_routes.py:670`

## `_load_local_contacts` — function, line 105
- **called from:**
- `routes/contacts/contacts_routes.py:349`
- `routes/contacts/contacts_routes.py:403`
- `routes/contacts/contacts_routes.py:462`
- `routes/contacts/contacts_routes.py:657`
- `routes/contacts/contacts_routes.py:701`

## `_save_local_contacts` — function, line 117
- **called from:**
- `routes/contacts/contacts_routes.py:416`
- `routes/contacts/contacts_routes.py:479`
- `routes/contacts/contacts_routes.py:671`
- `routes/contacts/contacts_routes.py:703`
- `routes/contacts/contacts_routes.py:884`

## `_vunesc` — function, line 127
- **called from:**
- `routes/contacts/contacts_routes.py:176`
- `routes/contacts/contacts_routes.py:180`
- `routes/contacts/contacts_routes.py:185`
- `routes/contacts/contacts_routes.py:195`
- `routes/contacts/contacts_routes.py:198`

## `_parse_vcards` — function, line 151
- **called from:**
- `routes/contacts/contacts_routes.py:321`
- `routes/contacts/contacts_routes.py:367`
- `routes/contacts/contacts_routes.py:461`
- `tests/test_contacts_vcard_parse.py:21`
- `tests/test_contacts_vcard_parse.py:34`
- `tests/test_vcard_unfolding.py:21`
- `tests/test_vcard_unfolding.py:36`
- `tests/test_vcard_unfolding.py:42`

## `_vesc` — function, line 204
- **called from:**
- `routes/contacts/contacts_routes.py:242`
- `routes/contacts/contacts_routes.py:242`
- `routes/contacts/contacts_routes.py:246`
- `routes/contacts/contacts_routes.py:247`
- `routes/contacts/contacts_routes.py:252`
- `routes/contacts/contacts_routes.py:252`
- `routes/contacts/contacts_routes.py:254`
- `routes/contacts/contacts_routes.py:260`

## `_build_vcard` — function, line 219
- **called from:**
- `routes/contacts/contacts_routes.py:420`
- `routes/contacts/contacts_routes.py:625`
- `routes/contacts/contacts_routes.py:674`

## `_abs_url` — function, line 270
- **called from:**
- `routes/contacts/contacts_routes.py:384`
- `tests/test_contacts_carddav_security.py:43`

## `_fetch_via_report` — function, line 300
- **called from:**
- `routes/contacts/contacts_routes.py:360`

## `_fetch_contacts` — function, line 340
- **called from:**
- `routes/contacts/contacts_routes.py:391`
- `routes/contacts/contacts_routes.py:589`
- `routes/contacts/contacts_routes.py:609`
- `routes/contacts/contacts_routes.py:717`
- `routes/contacts/contacts_routes.py:744`
- `routes/contacts/contacts_routes.py:750`
- `routes/contacts/contacts_routes.py:781`
- `routes/contacts/contacts_routes.py:799`
- `routes/contacts/contacts_routes.py:837`
- `routes/email_helpers.py:1827`
- `routes/email_helpers.py:1927`

## `_resolve_resource_url` — function, line 376
- **called from:**
- `routes/contacts/contacts_routes.py:678`
- `routes/contacts/contacts_routes.py:707`

## `_lookup` — function, line 381
- **called from:**
- `routes/contacts/contacts_routes.py:386`
- `routes/contacts/contacts_routes.py:394`

## `_create_contact` — function, line 397
- **called from:**
- `routes/contacts/contacts_routes.py:601`
- `routes/contacts/contacts_routes.py:789`
- `routes/contacts/contacts_routes.py:791`
- `routes/contacts/contacts_routes.py:793`

## `_vcard_url` — function, line 444
- **called from:**
- `routes/contacts/contacts_routes.py:394`
- `tests/test_contacts_carddav_security.py:63`

## `_import_vcards` — function, line 453
- **called from:**
- `routes/contacts/contacts_routes.py:823`

## `_import_csv_contacts` — function, line 534
- **called from:**
- `routes/contacts/contacts_routes.py:825`

## `_contacts_to_vcf` — function, line 623
- **called from:**
- `routes/contacts/contacts_routes.py:843`

## `_contacts_to_csv` — function, line 636
- **called from:**
- `routes/contacts/contacts_routes.py:839`

## `_update_contact` — function, line 653
- **called from:**
- `routes/contacts/contacts_routes.py:612`
- `routes/contacts/contacts_routes.py:802`
- `routes/contacts/contacts_routes.py:905`

## `_delete_contact` — function, line 697
- **called from:**
- `routes/contacts/contacts_routes.py:913`

## `setup_contacts_routes` — function, line 738
- **called from:**
- `app.py:884`
- `tests/test_contacts_add_null_name.py:16`
- `tests/test_contacts_import_nonstring.py:13`

## `list_contacts` — function (async), line 742
- **route:** `GET /list`
- decorator: `router.get("/list")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_contacts` — function (async), line 748
- **route:** `GET /search`
- decorator: `router.get("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_contact` — function (async), line 766
- **route:** `POST /add`
- decorator: `router.post("/add")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_vcf` — function (async), line 813
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_contacts` — function (async), line 832
- **route:** `GET /export`
- decorator: `router.get("/export")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_config` — function (async), line 853
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `update_config` — function (async), line 861
- **route:** `PUT /config`
- decorator: `router.put("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_contacts` — function (async), line 882
- **route:** `DELETE /clear`
- decorator: `router.delete("/clear")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `edit_contact` — function (async), line 891
- **route:** `PUT /{uid}`
- decorator: `router.put("/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_contact` — function (async), line 909
- **route:** `DELETE /{uid}`
- decorator: `router.delete("/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
