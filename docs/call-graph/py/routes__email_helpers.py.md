# `routes/email_helpers.py` — definitions & call sites

58 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `EmailNotConfiguredError` — class, line 43
- **called from:**
- `routes/email_helpers.py:1214`

## `_xoauth2_raw` — function, line 53
- **called from:**
- `routes/email_helpers.py:65`
- `routes/email_helpers.py:176`
- `routes/email_routes.py:5964`
- `tests/test_email_oauth.py:142`

## `_xoauth2_bytes` — function, line 63
- **called from:**
- `routes/email_helpers.py:1235`
- `routes/email_routes.py:5901`
- `tests/test_email_oauth.py:148`

## `make_oauth_state` — function, line 68
- **called from:**
- `routes/email_routes.py:6020`
- `tests/test_email_oauth.py:42`
- `tests/test_email_oauth.py:54`
- `tests/test_email_oauth.py:55`
- `tests/test_email_oauth.py:62`
- `tests/test_email_oauth.py:77`
- `tests/test_email_oauth.py:298`
- `tests/test_email_oauth.py:355`
- `tests/test_email_oauth.py:403`
- `tests/test_email_oauth.py:468`
- `tests/test_email_oauth.py:504`
- `tests/test_email_oauth.py:573`
- `tests/test_email_oauth.py:622`
- `tests/test_email_oauth.py:676`

## `verify_oauth_state` — function, line 83
- **called from:**
- `routes/email_routes.py:6046`
- `tests/test_email_oauth.py:43`
- `tests/test_email_oauth.py:54`
- `tests/test_email_oauth.py:55`
- `tests/test_email_oauth.py:71`
- `tests/test_email_oauth.py:82`
- `tests/test_email_oauth.py:89`

## `_refresh_google_token` — function, line 102
- **called from:**
- `routes/email_helpers.py:150`
- `tests/test_email_oauth.py:216`
- `tests/test_email_oauth.py:248`
- `tests/test_email_oauth.py:759`
- `tests/test_email_oauth.py:769`

## `_get_valid_google_token` — function, line 139
- **called from:**
- `routes/email_helpers.py:172`
- `routes/email_helpers.py:1232`
- `routes/email_routes.py:5864`
- `tests/test_email_oauth.py:715`
- `tests/test_email_oauth.py:734`

## `_smtp_security_mode` — function, line 153
- **called from:**
- `routes/email_helpers.py:180`
- `routes/email_helpers.py:1073`
- `routes/email_helpers.py:1106`
- `routes/email_routes.py:5636`
- `routes/email_routes.py:5678`
- `routes/email_routes.py:5725`
- `routes/email_routes.py:5821`
- `routes/email_routes.py:5922`
- `routes/email_routes.py:5927`

## `_send_smtp_message` — function, line 163
- **called from:**
- `routes/email_pollers.py:365`
- `routes/email_pollers.py:1226`
- `routes/email_pollers.py:1467`
- `routes/email_routes.py:2653`
- `routes/email_routes.py:4289`
- `routes/email_routes.py:4606`
- `routes/note/note_routes.py:389`
- `src/task_scheduler.py:1843`
- `tests/test_email_smtp_security.py:60`
- `tests/test_email_smtp_security.py:74`
- `tests/test_email_smtp_security.py:89`
- `tests/test_email_smtp_security.py:102`

## `_auth_smtp` — function, line 170
- **called from:**
- `routes/email_helpers.py:184`
- `routes/email_helpers.py:191`

## `_friendly_email_auth_error` — function, line 195
- **called from:**
- `routes/email_routes.py:5909`
- `routes/email_routes.py:5969`

## `_strip_think` — function, line 227
- **called from:**
- `routes/email_helpers.py:278`
- `routes/email_helpers.py:374`
- `routes/email_pollers.py:943`
- `routes/email_pollers.py:1139`
- `routes/email_pollers.py:1270`
- `routes/email_routes.py:4867`
- `routes/note/note_routes.py:233`
- `routes/task/task_routes.py:1143`
- `services/memory/memory_extractor.py:402`
- `services/memory/skill_extractor.py:224`

## `_extract_reply` — function, line 253
- **called from:**
- `mcp_servers/email_server.py:1862`
- `routes/email_helpers.py:370`
- `routes/email_pollers.py:852`
- `routes/email_routes.py:3073`
- `routes/email_routes.py:5101`
- `routes/email_routes.py:5183`
- `routes/email_routes.py:5376`
- `routes/email_routes.py:5406`
- `src/builtin_actions.py:1173`

## `_build_email_summary_messages` — function, line 281
- **called from:**
- `routes/email_helpers.py:328`
- `routes/email_helpers.py:354`

## `_generate_email_summary` — function (async), line 311
- **called from:**
- `routes/email_routes.py:4941`
- `tests/test_email_summary_llm.py:46`

## `_generate_scheduled_email_summary` — function (async), line 338
- **called from:**
- `routes/email_pollers.py:790`
- `tests/test_email_summary_llm.py:101`
- `tests/test_email_summary_llm.py:164`

## `_normalize_email_summary` — function, line 366
- **called from:**
- `routes/email_helpers.py:335`
- `routes/email_helpers.py:363`

## `_email_summary_failure_log_detail` — function, line 389
- **called from:**
- `routes/email_pollers.py:825`
- `routes/email_routes.py:4954`
- `routes/email_routes.py:4992`

## `_apply_email_style_mechanics` — function, line 400
- **called from:**
- `mcp_servers/email_server.py:1862`
- `routes/email_pollers.py:852`
- `routes/email_routes.py:3073`
- `routes/email_routes.py:5183`
- `routes/email_routes.py:5376`
- `routes/email_routes.py:5406`

## `_require_auth` — function, line 412
- **called from:**
- `routes/email_helpers.py:446`
- `routes/email_helpers.py:455`

## `require_owner` — function, line 440
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `require_user` — function, line 452
- **called from:**
- `routes/calendar_routes.py:75`
- `routes/codex_routes.py:96`
- `routes/codex_routes.py:110`
- `routes/history/history_routes.py:931`
- `routes/memory/memory_routes.py:241`
- `routes/note/note_routes.py:598`
- `routes/note/note_routes.py:852`
- `src/auth_helpers.py:93`
- `src/auth_helpers.py:172`
- `tests/test_api_token_user_route_gate.py:32`
- `tests/test_api_token_user_route_gate.py:51`
- `tests/test_security_regressions.py:544`
- `tests/test_security_regressions.py:598`
- `tests/test_security_regressions.py:631`
- `tests/test_security_regressions.py:663`
- `tests/test_security_regressions.py:695`

## `_assert_owns_account` — function, line 458
- **called from:**
- `routes/codex_routes.py:270`
- `routes/codex_routes.py:297`
- `routes/email_helpers.py:448`
- `routes/email_routes.py:2595`
- `routes/email_routes.py:2619`
- `routes/email_routes.py:2687`
- `routes/email_routes.py:3835`
- `routes/email_routes.py:4305`
- `routes/email_routes.py:4525`
- `routes/email_routes.py:4730`
- `routes/email_routes.py:4787`
- `routes/email_routes.py:4896`
- `routes/email_routes.py:5165`
- `routes/email_routes.py:5448`
- `routes/email_routes.py:5460`
- `routes/email_routes.py:5475`
- `routes/email_routes.py:5523`
- `routes/email_routes.py:5707`
- `routes/email_routes.py:5805`
- `routes/email_routes.py:6012`
- `tests/test_email_ownerless_account_owner_scope.py:61`
- `tests/test_email_ownerless_account_owner_scope.py:70`
- `tests/test_email_ownerless_account_owner_scope.py:80`
- `tests/test_email_ownerless_account_owner_scope.py:89`

## `_account_visible_to_owner` — function, line 488
- **called from:**
- `mcp_servers/email_server.py:119`
- `routes/email_helpers.py:474`
- `routes/email_helpers.py:1054`
- `routes/email_routes.py:223`
- `routes/email_routes.py:243`

## `_q` — function, line 507
- **called from:**
- `mcp_servers/email_server.py:664`
- `mcp_servers/email_server.py:721`
- `mcp_servers/email_server.py:982`
- `mcp_servers/email_server.py:1112`
- `mcp_servers/email_server.py:1228`
- `mcp_servers/email_server.py:1527`
- `mcp_servers/email_server.py:1731`
- `mcp_servers/email_server.py:1881`
- `mcp_servers/email_server.py:1926`
- `mcp_servers/email_server.py:1948`
- `mcp_servers/email_server.py:1975`
- `mcp_servers/email_server.py:1986`
- `mcp_servers/email_server.py:2007`
- `mcp_servers/email_server.py:2019`
- `mcp_servers/email_server.py:2029`
- `mcp_servers/email_server.py:2066`
- `routes/document/document_routes.py:1769`
- `routes/email_helpers.py:1429`
- `routes/email_helpers.py:1435`
- `routes/email_helpers.py:1709`
- `routes/email_helpers.py:1886`
- `routes/email_pollers.py:555`
- `routes/email_pollers.py:563`
- `routes/email_pollers.py:684`
- `routes/email_pollers.py:1473`
- `routes/email_routes.py:1346`
- `routes/email_routes.py:1349`
- `routes/email_routes.py:1861`
- `routes/email_routes.py:2287`
- `routes/email_routes.py:2532`
- `routes/email_routes.py:2622`
- `routes/email_routes.py:2658`
- `routes/email_routes.py:2706`
- `routes/email_routes.py:2832`
- `routes/email_routes.py:2955`
- `routes/email_routes.py:2966`
- `routes/email_routes.py:3164`
- `routes/email_routes.py:3287`
- `routes/email_routes.py:3305`
- `routes/email_routes.py:3332`
- `routes/email_routes.py:3394`
- `routes/email_routes.py:3445`
- `routes/email_routes.py:3715`
- `routes/email_routes.py:3737`
- `routes/email_routes.py:3754`
- `routes/email_routes.py:3769`
- `routes/email_routes.py:3786`
- `routes/email_routes.py:3801`
- `routes/email_routes.py:3816`
- `routes/email_routes.py:3863`
- `routes/email_routes.py:3887`
- `routes/email_routes.py:3907`
- `routes/email_routes.py:3993`
- `routes/email_routes.py:4009`
- `routes/email_routes.py:4206`
- `routes/email_routes.py:4478`
- `routes/email_routes.py:4642`
- `routes/email_routes.py:4654`
- `routes/email_routes.py:4680`
- `routes/email_routes.py:4792`
- … +10 more (grep the name in repo)

## `_attach_compose_uploads` — function, line 515
- **called from:**
- `routes/email_pollers.py:1460`
- `routes/email_routes.py:4285`
- `routes/email_routes.py:4574`

## `_cleanup_compose_uploads` — function, line 542
- **called from:**
- `routes/email_pollers.py:1477`
- `routes/email_routes.py:4291`
- `routes/email_routes.py:4702`

## `email_translation_body_hash` — function, line 576
- **called from:**
- `routes/email_routes.py:5018`
- `src/builtin_actions.py:1226`

## `_email_cache_owner_clause` — function, line 582
- **called from:**
- `routes/email_pollers.py:588`
- `routes/email_routes.py:2183`
- `routes/email_routes.py:2227`
- `routes/email_routes.py:3061`
- `routes/email_routes.py:5021`
- `routes/email_routes.py:5176`
- `routes/task/task_routes.py:615`
- `src/builtin_actions.py:1108`
- `src/builtin_actions.py:1649`

## `_ensure_owner_scoped_email_cache_table` — function, line 589
- **called from:**
- `routes/email_helpers.py:722`
- `routes/email_helpers.py:737`
- `routes/email_helpers.py:749`
- `routes/email_helpers.py:835`
- `routes/email_helpers.py:846`

## `_ensure_sender_signatures_table` — function, line 636
- **called from:**
- `routes/email_helpers.py:992`

## `attachment_extract_dir` — function, line 685
- **called from:**
- `routes/email_routes.py:3313`
- `routes/email_routes.py:3345`
- `routes/email_routes.py:3415`
- `routes/email_routes.py:3452`
- `routes/email_routes.py:3722`
- `routes/email_routes.py:4212`

## `_init_scheduled_db` — function, line 699
- **called from:**
- `routes/email_helpers.py:997`
- `src/builtin_actions.py:2845`
- `tests/test_builtin_actions_owner_scope.py:145`
- `tests/test_email_owner_scope.py:79`
- `tests/test_email_owner_scope.py:151`
- `tests/test_email_owner_scope.py:193`
- `tests/test_email_owner_scope.py:230`
- `tests/test_email_owner_scope.py:276`
- `tests/test_email_owner_scope.py:325`
- `tests/test_email_owner_scope.py:392`
- `tests/test_email_owner_scope.py:459`
- `tests/test_email_owner_scope.py:502`
- `tests/test_email_owner_scope.py:550`
- `tests/test_email_owner_scope.py:598`
- `tests/test_email_read_mark_seen.py:66`
- `tests/test_email_summary_llm.py:204`
- `tests/test_email_summary_llm.py:334`
- `tests/test_schedule_email_offset_normalization.py:33`
- `tests/test_scheduled_poll_race.py:31`

## `_load_settings` — function, line 1000
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

## `_save_settings` — function, line 1006
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

## `_get_email_config` — function, line 1011
- **called from:**
- `routes/email_helpers.py:1139`
- `routes/email_helpers.py:1144`
- `routes/email_helpers.py:1208`
- `routes/email_pollers.py:322`
- `routes/email_pollers.py:628`
- `routes/email_pollers.py:1169`
- `routes/email_pollers.py:1434`
- `routes/email_routes.py:266`
- `routes/email_routes.py:1300`
- `routes/email_routes.py:1316`
- `routes/email_routes.py:3839`
- `routes/email_routes.py:4731`
- `routes/email_routes.py:5476`
- `routes/note/note_routes.py:313`
- `routes/note/note_routes.py:326`
- `src/task_scheduler.py:2205`
- `tests/test_email_ownerless_account_owner_scope.py:105`
- `tests/test_email_ownerless_account_owner_scope.py:116`

## `_owner_or_matching_legacy_account` — function, line 1033
- **called from:**
- `routes/email_helpers.py:1060`
- `routes/email_helpers.py:1064`

## `_list_email_accounts` — function, line 1126
- **called from:**
- `src/service_health.py:432`

## `_coerce_imap_timeout_seconds` — function, line 1149
- **called from:**
- `routes/email_helpers.py:1157`
- `tests/test_email_imap_timeout.py:53`
- `tests/test_email_imap_timeout.py:54`
- `tests/test_email_imap_timeout.py:55`
- `tests/test_email_imap_timeout.py:56`

## `_open_imap_connection` — function, line 1160
- **called from:**
- `routes/email_helpers.py:1224`
- `routes/email_routes.py:5893`
- `tests/test_email_imap_timeout.py:66`
- `tests/test_email_imap_timeout.py:81`
- `tests/test_imap_leak_fixes.py:288`

## `_imap_connect` — function, line 1200
- **called from:**
- `mcp_servers/email_server.py:662`
- `mcp_servers/email_server.py:719`
- `mcp_servers/email_server.py:981`
- `mcp_servers/email_server.py:1107`
- `mcp_servers/email_server.py:1227`
- `mcp_servers/email_server.py:1524`
- `mcp_servers/email_server.py:1730`
- `mcp_servers/email_server.py:1880`
- `mcp_servers/email_server.py:1925`
- `mcp_servers/email_server.py:1945`
- `mcp_servers/email_server.py:1972`
- `mcp_servers/email_server.py:2005`
- `mcp_servers/email_server.py:2018`
- `mcp_servers/email_server.py:2065`
- `routes/email_helpers.py:1299`
- `routes/email_helpers.py:1428`
- `routes/email_helpers.py:1704`
- `routes/email_helpers.py:1883`
- `routes/email_pollers.py:544`
- `routes/email_pollers.py:577`
- `routes/email_routes.py:1579`
- `src/builtin_actions.py:1198`
- `src/builtin_actions.py:1597`
- `src/builtin_actions.py:1684`
- `src/builtin_actions.py:1828`
- `src/builtin_actions.py:2542`
- `src/service_health.py:317`
- `tests/test_email_oauth.py:795`
- `tests/test_email_oauth.py:823`
- `tests/test_email_send_only_no_inbox.py:52`
- `tests/test_email_send_only_no_inbox.py:73`
- `tests/test_imap_leak_fixes.py:262`
- `tests/test_imap_leak_fixes.py:325`
- `tests/test_imap_leak_fixes.py:346`

## `_imap` — function, line 1261
- decorator: `contextmanager`
- **called from:**
- `routes/document/document_routes.py:1768`
- `routes/email_helpers.py:1844`
- `routes/email_pollers.py:1471`
- `routes/email_routes.py:2286`
- `routes/email_routes.py:2531`
- `routes/email_routes.py:2621`
- `routes/email_routes.py:2657`
- `routes/email_routes.py:2705`
- `routes/email_routes.py:2811`
- `routes/email_routes.py:2948`
- `routes/email_routes.py:3163`
- `routes/email_routes.py:3286`
- `routes/email_routes.py:3304`
- `routes/email_routes.py:3331`
- `routes/email_routes.py:3393`
- `routes/email_routes.py:3444`
- `routes/email_routes.py:3714`
- `routes/email_routes.py:3736`
- `routes/email_routes.py:3753`
- `routes/email_routes.py:3768`
- `routes/email_routes.py:3785`
- `routes/email_routes.py:3800`
- `routes/email_routes.py:3815`
- `routes/email_routes.py:3854`
- `routes/email_routes.py:3906`
- `routes/email_routes.py:3947`
- `routes/email_routes.py:3992`
- `routes/email_routes.py:4008`
- `routes/email_routes.py:4205`
- `routes/email_routes.py:4474`
- `routes/email_routes.py:4632`
- `routes/email_routes.py:4760`
- `routes/email_routes.py:4791`
- `routes/email_routes.py:4911`

## `_decode_header` — function, line 1309
- **called from:**
- `mcp_servers/email_server.py:579`
- `mcp_servers/email_server.py:581`
- `mcp_servers/email_server.py:582`
- `mcp_servers/email_server.py:1014`
- `mcp_servers/email_server.py:1015`
- `mcp_servers/email_server.py:1126`
- `mcp_servers/email_server.py:1127`
- `mcp_servers/email_server.py:1130`
- `mcp_servers/email_server.py:1131`
- `mcp_servers/email_server.py:1173`
- `mcp_servers/email_server.py:1203`
- `mcp_servers/email_server.py:1248`
- `mcp_servers/email_server.py:1249`
- `mcp_servers/email_server.py:1739`
- `mcp_servers/email_server.py:1745`
- `mcp_servers/email_server.py:1892`
- `mcp_servers/email_server.py:1898`
- `routes/document/document_routes.py:1774`
- `routes/document/document_routes.py:1778`
- `routes/email_helpers.py:1477`
- `routes/email_helpers.py:1537`
- `routes/email_helpers.py:1601`
- `routes/email_helpers.py:1751`
- `routes/email_helpers.py:1870`
- `routes/email_helpers.py:1906`
- `routes/email_helpers.py:1907`
- `routes/email_pollers.py:704`
- `routes/email_pollers.py:705`
- `routes/email_pollers.py:736`
- `routes/email_pollers.py:737`
- `routes/email_routes.py:598`
- `routes/email_routes.py:600`
- `routes/email_routes.py:601`
- `routes/email_routes.py:738`
- `routes/email_routes.py:739`
- `routes/email_routes.py:743`
- `routes/email_routes.py:744`
- `routes/email_routes.py:2304`
- `routes/email_routes.py:2305`
- `routes/email_routes.py:2999`
- `routes/email_routes.py:3000`
- `routes/email_routes.py:3001`
- `routes/email_routes.py:3002`
- `routes/email_routes.py:3549`
- `routes/email_routes.py:3550`
- `routes/email_routes.py:3551`
- `routes/email_routes.py:3552`
- `routes/email_routes.py:4493`
- `src/builtin_actions.py:1219`
- `src/builtin_actions.py:1220`
- `src/builtin_actions.py:1842`
- `src/builtin_actions.py:1843`
- `src/builtin_actions.py:2643`
- `src/builtin_actions.py:2644`
- `tests/test_email_decode_header.py:26`
- `tests/test_email_decode_header.py:32`
- `tests/test_email_decode_header.py:38`
- `tests/test_email_decode_header.py:42`
- `tests/test_email_decode_header.py:46`
- `tests/test_email_decode_header.py:50`
- … +10 more (grep the name in repo)

## `_detect_sent_folder` — function, line 1336
- **called from:**
- `mcp_servers/email_server.py:1526`
- `routes/email_pollers.py:1472`
- `routes/email_routes.py:3855`
- `routes/email_routes.py:4633`
- `routes/email_routes.py:4792`

## `_detect_drafts_folder` — function, line 1371
- **called from:**
- `routes/email_routes.py:4761`

## `_detect_spam_folder` — function, line 1399
- **called from:**
- `routes/email_pollers.py:632`

## `_imap_move` — function, line 1424
- **called from:**
- `routes/email_pollers.py:1294`
- `tests/test_imap_move_uid.py:49`

## `_extract_attachment_text` — function, line 1452
- **called from:**
- `routes/email_helpers.py:1757`
- `routes/email_pollers.py:763`
- `routes/email_routes.py:4918`

## `_list_attachments_from_msg` — function, line 1520
- **called from:**
- `mcp_servers/email_server.py:1253`
- `routes/email_helpers.py:1581`
- `routes/email_routes.py:2307`
- `routes/email_routes.py:3012`
- `routes/email_routes.py:3293`
- `routes/email_routes.py:3339`
- `routes/email_routes.py:3555`

## `_is_likely_signature_image_attachment` — function, line 1564
- **called from:**
- `routes/email_helpers.py:1580`
- `routes/email_routes.py:2308`
- `routes/email_routes.py:3340`

## `_has_visible_attachments` — function, line 1577
- **called from:**
- `routes/email_routes.py:3032`

## `_extract_attachment_to_disk` — function, line 1585
- **called from:**
- `mcp_servers/email_server.py:2078`
- `routes/email_routes.py:3314`
- `routes/email_routes.py:3353`
- `routes/email_routes.py:3416`
- `routes/email_routes.py:3453`
- `routes/email_routes.py:3723`
- `routes/email_routes.py:4213`

## `_extract_html` — function, line 1626
- **called from:**
- `routes/email_routes.py:3008`

## `_extract_text` — function, line 1645
- **called from:**
- `mcp_servers/email_server.py:1252`
- `routes/email_helpers.py:1753`
- `routes/email_helpers.py:1909`
- `routes/email_pollers.py:755`
- `routes/email_routes.py:3007`
- `routes/email_routes.py:3554`
- `src/builtin_actions.py:1221`

## `_fetch_sender_thread_context` — function, line 1674
- **called from:**
- `routes/email_routes.py:5286`
- `tests/test_imap_leak_fixes.py:51`
- `tests/test_imap_leak_fixes.py:68`

## `_pre_retrieve_context` — function, line 1785
- **called from:**
- `routes/email_routes.py:5275`
- `tests/test_imap_leak_fixes.py:97`

## `SendEmailRequest` — class, line 1981
- **called from:**
- `routes/codex_routes.py:371`
- `routes/codex_routes.py:384`

## `ExtractStyleRequest` — class, line 2007
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
