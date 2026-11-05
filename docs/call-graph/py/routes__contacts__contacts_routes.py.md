# `routes/contacts/contacts_routes.py` — definitions & call sites

41 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_load_settings` — function, line 39
- **called from:**
- `routes/auth_routes.py:780`
- `routes/auth_routes.py:795`
- `routes/auth_routes.py:986`
- `routes/contacts/contacts_routes.py:52`
- `routes/contacts/contacts_routes.py:1000`
- `routes/email/email_helpers.py:1240`
- `routes/email/email_pollers.py:504`
- `routes/email/email_pollers.py:526`
- `routes/email/email_pollers.py:640`
- `routes/email/email_pollers.py:1576`
- `routes/email/email_routes.py:6573`
- `routes/email/email_routes.py:6930`
- `routes/email/email_routes.py:7219`
- `routes/email/email_routes.py:7231`
- `routes/email/email_routes.py:7257`
- `routes/email/email_routes.py:7304`
- `routes/model_routes.py:184`
- `routes/model_routes.py:2365`
- `routes/model_routes.py:2799`
- `routes/model_routes.py:2967`
- `routes/model_routes.py:2971`
- `routes/model_routes.py:3108`
- `routes/model_routes.py:3128`
- `services/stt/stt_service.py:42`
- `services/stt/stt_service.py:66`
- `services/stt/stt_service.py:157`
- `services/stt/stt_service.py:177`
- `services/tts/tts_service.py:66`
- `services/tts/tts_service.py:200`
- `services/tts/tts_service.py:254`
- `src/agent_loop.py:14918`
- `src/agent_loop.py:15156`
- `src/builtin_actions.py:3583`
- `tests/test_carddav_password_encryption.py:39`
- `tests/test_carddav_password_encryption.py:145`
- `tests/test_carddav_password_encryption.py:158`
- `tests/test_carddav_password_encryption.py:162`

## `_save_settings` — function, line 45
- **called from:**
- `routes/auth_routes.py:829`
- `routes/contacts/contacts_routes.py:1014`
- `routes/email/email_pollers.py:514`
- `routes/email/email_pollers.py:532`
- `routes/email/email_routes.py:6575`
- `routes/email/email_routes.py:7233`
- `routes/email/email_routes.py:7314`
- `routes/model_routes.py:193`
- `routes/model_routes.py:2387`
- `routes/model_routes.py:2974`
- `routes/model_routes.py:3130`
- `src/builtin_actions.py:3594`
- `tests/test_carddav_password_encryption.py:43`
- `tests/test_carddav_password_encryption.py:143`
- `tests/test_carddav_password_encryption.py:146`
- `tests/test_carddav_password_encryption.py:160`
- `tests/test_carddav_password_encryption.py:164`

## `_get_carddav_config` — function, line 50
- **called from:**
- `routes/contacts/contacts_routes.py:65`
- `routes/contacts/contacts_routes.py:348`
- `routes/contacts/contacts_routes.py:441`
- `routes/contacts/contacts_routes.py:509`
- `routes/contacts/contacts_routes.py:563`
- `routes/contacts/contacts_routes.py:573`
- `routes/contacts/contacts_routes.py:769`
- `routes/contacts/contacts_routes.py:823`
- `routes/contacts/contacts_routes.py:992`
- `tests/test_carddav_password_encryption.py:50`
- `tests/test_carddav_password_encryption.py:66`
- `tests/test_carddav_password_encryption.py:82`
- `tests/test_carddav_password_encryption.py:96`
- `tests/test_carddav_password_encryption.py:110`
- `tests/test_carddav_password_encryption.py:123`
- `tests/test_carddav_password_encryption.py:130`
- `tests/test_carddav_password_encryption.py:148`
- `tests/test_carddav_password_encryption.py:169`

## `_carddav_configured` — function, line 64
- **called from:**
- `routes/contacts/contacts_routes.py:326`
- `routes/contacts/contacts_routes.py:442`
- `routes/contacts/contacts_routes.py:511`
- `routes/contacts/contacts_routes.py:771`
- `routes/contacts/contacts_routes.py:825`

## `_validate_carddav_url` — function, line 69
- **called from:**
- `routes/contacts/contacts_routes.py:81`
- `routes/contacts/contacts_routes.py:355`
- `routes/contacts/contacts_routes.py:1005`
- `tests/test_contacts_carddav_security.py:16`
- `tests/test_contacts_carddav_security.py:27`

## `_carddav_base_url` — function, line 80
- **called from:**
- `routes/contacts/contacts_routes.py:349`
- `routes/contacts/contacts_routes.py:457`
- `routes/contacts/contacts_routes.py:536`
- `routes/contacts/contacts_routes.py:564`
- `routes/contacts/contacts_routes.py:596`

## `_normalize_contact` — function, line 84
- **called from:**
- `routes/contacts/contacts_routes.py:128`
- `routes/contacts/contacts_routes.py:138`
- `routes/contacts/contacts_routes.py:139`
- `routes/contacts/contacts_routes.py:529`
- `routes/contacts/contacts_routes.py:588`
- `routes/contacts/contacts_routes.py:786`
- `routes/contacts/contacts_routes.py:794`

## `_contact_visible_to_owner` — function, line 112
- **called from:**
- `routes/contacts/contacts_routes.py:129`
- `routes/contacts/contacts_routes.py:515`
- `routes/contacts/contacts_routes.py:777`
- `routes/contacts/contacts_routes.py:829`
- `routes/contacts/contacts_routes.py:1027`

## `_load_local_contacts` — function, line 122
- **called from:**
- `routes/contacts/contacts_routes.py:437`
- `routes/contacts/contacts_routes.py:443`
- `routes/contacts/contacts_routes.py:512`
- `routes/contacts/contacts_routes.py:576`
- `routes/contacts/contacts_routes.py:772`
- `routes/contacts/contacts_routes.py:826`
- `routes/contacts/contacts_routes.py:1026`

## `_save_local_contacts` — function, line 135
- **called from:**
- `routes/contacts/contacts_routes.py:530`
- `routes/contacts/contacts_routes.py:593`
- `routes/contacts/contacts_routes.py:795`
- `routes/contacts/contacts_routes.py:831`
- `routes/contacts/contacts_routes.py:1029`
- `routes/contacts/contacts_routes.py:1031`

## `_vunesc` — function, line 147
- **called from:**
- `routes/contacts/contacts_routes.py:196`
- `routes/contacts/contacts_routes.py:200`
- `routes/contacts/contacts_routes.py:205`
- `routes/contacts/contacts_routes.py:215`
- `routes/contacts/contacts_routes.py:218`

## `_parse_vcards` — function, line 171
- **called from:**
- `routes/contacts/contacts_routes.py:392`
- `routes/contacts/contacts_routes.py:469`
- `routes/contacts/contacts_routes.py:575`
- `tests/test_contacts_vcard_parse.py:21`
- `tests/test_contacts_vcard_parse.py:34`
- `tests/test_vcard_unfolding.py:21`
- `tests/test_vcard_unfolding.py:36`
- `tests/test_vcard_unfolding.py:42`

## `_vesc` — function, line 224
- **called from:**
- `routes/contacts/contacts_routes.py:262`
- `routes/contacts/contacts_routes.py:262`
- `routes/contacts/contacts_routes.py:266`
- `routes/contacts/contacts_routes.py:267`
- `routes/contacts/contacts_routes.py:272`
- `routes/contacts/contacts_routes.py:272`
- `routes/contacts/contacts_routes.py:274`
- `routes/contacts/contacts_routes.py:280`

## `_build_vcard` — function, line 239
- **called from:**
- `routes/contacts/contacts_routes.py:534`
- `routes/contacts/contacts_routes.py:739`
- `routes/contacts/contacts_routes.py:798`

## `_cached_contacts` — function, line 303
- **called from:**
- `routes/contacts/contacts_routes.py:312`
- `routes/contacts/contacts_routes.py:432`
- `routes/contacts/contacts_routes.py:454`

## `_mark_contact_fetch_failure` — function, line 310
- **called from:**
- `routes/contacts/contacts_routes.py:468`
- `routes/contacts/contacts_routes.py:479`

## `_contact_sync_status` — function, line 324
- **called from:**
- `routes/contacts/contacts_routes.py:873`
- `routes/contacts/contacts_routes.py:880`
- `routes/contacts/contacts_routes.py:891`

## `_abs_url` — function, line 341
- **called from:**
- `routes/contacts/contacts_routes.py:492`
- `tests/test_contacts_carddav_security.py:43`

## `_fetch_via_report` — function, line 371
- **called from:**
- `routes/contacts/contacts_routes.py:462`

## `_fetch_contacts` — function, line 411
- **called from:**
- `routes/contacts/contacts_routes.py:499`
- `routes/contacts/contacts_routes.py:703`
- `routes/contacts/contacts_routes.py:723`
- `routes/contacts/contacts_routes.py:845`
- `routes/contacts/contacts_routes.py:910`
- `routes/contacts/contacts_routes.py:931`
- `routes/email/email_helpers.py:1976`
- `routes/email/email_helpers.py:2076`

## `_resolve_resource_url` — function, line 484
- **called from:**
- `routes/contacts/contacts_routes.py:802`
- `routes/contacts/contacts_routes.py:835`

## `_lookup` — function, line 489
- **called from:**
- `routes/contacts/contacts_routes.py:494`
- `routes/contacts/contacts_routes.py:502`

## `_create_contact` — function, line 505
- **called from:**
- `routes/contacts/contacts_routes.py:715`
- `routes/contacts/contacts_routes.py:923`
- `routes/contacts/contacts_routes.py:925`

## `_vcard_url` — function, line 558
- **called from:**
- `routes/contacts/contacts_routes.py:502`
- `tests/test_contacts_carddav_security.py:63`

## `_import_vcards` — function, line 567
- **called from:**
- `routes/contacts/contacts_routes.py:956`

## `_import_csv_contacts` — function, line 648
- **called from:**
- `routes/contacts/contacts_routes.py:958`

## `_contacts_to_vcf` — function, line 737
- **called from:**
- `routes/contacts/contacts_routes.py:981`

## `_contacts_to_csv` — function, line 750
- **called from:**
- `routes/contacts/contacts_routes.py:977`

## `_update_contact` — function, line 767
- **called from:**
- `routes/contacts/contacts_routes.py:726`
- `routes/contacts/contacts_routes.py:934`
- `routes/contacts/contacts_routes.py:1052`

## `_delete_contact` — function, line 821
- **called from:**
- `routes/contacts/contacts_routes.py:1060`

## `setup_contacts_routes` — function, line 866
- **called from:**
- `app.py:969`
- `tests/test_contact_tool_partial_update.py:29`
- `tests/test_contacts_add_null_name.py:17`
- `tests/test_contacts_import_nonstring.py:13`

## `list_contacts` — function (async), line 870
- **route:** `GET /list`
- decorator: `router.get("/list")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_contacts` — function (async), line 876
- **route:** `GET /search`
- decorator: `router.get("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `add_contact` — function (async), line 894
- **route:** `POST /add`
- decorator: `router.post("/add")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `import_vcf` — function (async), line 946
- **route:** `POST /import`
- decorator: `router.post("/import")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `export_contacts` — function (async), line 965
- **route:** `GET /export`
- decorator: `router.get("/export")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_config` — function (async), line 991
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
- `tests/test_email_oauth.py:911`

## `update_config` — function (async), line 999
- **route:** `PUT /config`
- decorator: `router.put("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_contacts` — function (async), line 1021
- **route:** `DELETE /clear`
- decorator: `router.delete("/clear")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `edit_contact` — function (async), line 1038
- **route:** `PUT /{uid}`
- decorator: `router.put("/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_contact` — function (async), line 1056
- **route:** `DELETE /{uid}`
- decorator: `router.delete("/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
