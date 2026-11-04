# `routes/email_routes.py` — definitions & call sites

177 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalized_mail_host` — function, line 83
- **called from:**
- `routes/email_routes.py:5874`
- `routes/email_routes.py:5915`

## `_google_oauth_imap_transport_allowed` — function, line 88
- **called from:**
- `routes/email_routes.py:5876`

## `_google_oauth_smtp_transport_allowed` — function, line 92
- **called from:**
- `routes/email_routes.py:5920`

## `_email_style_key` — function, line 95
- **called from:**
- `routes/email_routes.py:100`
- `routes/email_routes.py:110`
- `routes/email_routes.py:141`
- `routes/email_routes.py:150`

## `_get_email_writing_style_for_account` — function, line 99
- **called from:**
- `routes/email_routes.py:5195`
- `routes/email_routes.py:5450`

## `_set_email_writing_style_for_account` — function, line 109
- **called from:**
- `routes/email_routes.py:4873`
- `routes/email_routes.py:5462`

## `_get_auto_reply_settings_for_account` — function, line 140
- **called from:**
- `routes/email_routes.py:151`
- `routes/email_routes.py:5488`

## `_set_auto_reply_settings_for_account` — function, line 149
- **called from:**
- `routes/email_routes.py:5534`

## `_safe_attachment_zip_name` — function, line 176
- **called from:**
- `routes/email_routes.py:3357`
- `routes/email_routes.py:3368`
- `routes/email_routes.py:4156`

## `_coerce_port` — function, line 184
- **called from:**
- `routes/email_routes.py:5657`
- `routes/email_routes.py:5660`
- `routes/email_routes.py:5720`
- `routes/email_routes.py:5847`
- `routes/email_routes.py:5912`
- `tests/test_email_account_port_validation.py:22`
- `tests/test_email_account_port_validation.py:23`
- `tests/test_email_account_port_validation.py:28`
- `tests/test_email_account_port_validation.py:29`
- `tests/test_email_account_port_validation.py:34`

## `_lock_email_account_owner_mutation` — function, line 199
- **called from:**
- `routes/email_routes.py:241`
- `routes/email_routes.py:5542`
- `routes/email_routes.py:5665`

## `_email_account_owner_scope` — function, line 206
- **called from:**
- `routes/email_routes.py:5544`
- `routes/email_routes.py:5570`
- `routes/email_routes.py:5692`
- `routes/email_routes.py:5766`
- `routes/email_routes.py:5997`

## `_discover_email_account_mutation_scope` — function, line 216
- **called from:**
- `routes/email_routes.py:5743`
- `routes/email_routes.py:5988`

## `_lock_and_reload_email_account` — function, line 235
- **called from:**
- `routes/email_routes.py:5747`
- `routes/email_routes.py:5992`

## `_email_tag_owner_aliases` — function, line 257
- **called from:**
- `routes/email_routes.py:292`

## `_email_tag_owner_clause` — function, line 291
- **called from:**
- `routes/email_routes.py:341`
- `routes/email_routes.py:1912`
- `routes/email_routes.py:2030`
- `routes/email_routes.py:2088`
- `routes/email_routes.py:2137`
- `routes/email_routes.py:2487`
- `routes/email_routes.py:2505`
- `routes/email_routes.py:2738`
- `tests/test_email_owner_scope.py:26`
- `tests/test_email_owner_scope.py:42`

## `_email_tag_account_clause` — function, line 301
- **called from:**
- `routes/email_routes.py:342`
- `routes/email_routes.py:1913`
- `routes/email_routes.py:2031`
- `routes/email_routes.py:2089`
- `routes/email_routes.py:2138`
- `routes/email_routes.py:2506`

## `_sanitize_visible_email_tags` — function, line 315
- **called from:**
- `routes/email_routes.py:1969`
- `routes/email_routes.py:2043`
- `routes/email_routes.py:2104`
- `routes/email_routes.py:2124`
- `routes/email_routes.py:2163`
- `routes/email_routes.py:2173`

## `_hide_unlinked_calendar_tags` — function, line 330
- **called from:**
- `routes/email_routes.py:2206`
- `routes/email_routes.py:2350`

## `_clear_done_response_tags` — function, line 338
- **called from:**
- `routes/email_routes.py:3997`
- `routes/email_routes.py:4657`

## `_record_email_received_events` — function, line 366
- **called from:**
- `routes/email_routes.py:2397`

## `_run_away_reply_check` — function (async), line 420
- **called from:**
- `routes/email_routes.py:433`

## `_folder_name_from_list_line` — function, line 440
- **called from:**
- `mcp_servers/email_server.py:465`
- `mcp_servers/email_server.py:477`
- `routes/email_routes.py:453`
- `routes/email_routes.py:472`

## `_list_imap_folders` — function, line 448
- **called from:**
- `routes/email_routes.py:461`

## `_resolve_mail_folder` — function, line 459
- **called from:**
- `routes/email_routes.py:1339`

## `_folder_role_from_name` — function, line 488
- **called from:**
- `mcp_servers/email_server.py:1976`
- `mcp_servers/email_server.py:2021`
- `routes/email_routes.py:1339`

## `_uid_bytes` — function, line 499
- **called from:**
- `routes/email_routes.py:505`
- `routes/email_routes.py:523`
- `routes/email_routes.py:1334`
- `routes/email_routes.py:1346`
- `routes/email_routes.py:1349`
- `routes/email_routes.py:1352`
- `routes/email_routes.py:3015`
- `routes/email_routes.py:3165`

## `_uid_exists` — function, line 503
- **called from:**
- `routes/email_routes.py:1331`
- `routes/email_routes.py:1344`

## `_imap_uid_search` — function, line 518
- **called from:**
- `routes/email_routes.py:1872`
- `routes/email_routes.py:1875`
- `routes/email_routes.py:1877`
- `routes/email_routes.py:1880`
- `routes/email_routes.py:1885`
- `routes/email_routes.py:1894`
- `routes/email_routes.py:1900`
- `routes/email_routes.py:1991`
- `routes/email_routes.py:2002`
- `routes/email_routes.py:2004`
- `routes/email_routes.py:2293`
- `routes/email_routes.py:2535`
- `routes/email_routes.py:2836`

## `_imap_uid_fetch` — function, line 522
- **called from:**
- `routes/email_routes.py:2063`
- `routes/email_routes.py:2300`
- `routes/email_routes.py:2548`
- `routes/email_routes.py:2625`
- `routes/email_routes.py:2874`
- `routes/email_routes.py:2970`
- `routes/email_routes.py:3288`
- `routes/email_routes.py:3306`
- `routes/email_routes.py:3333`
- `routes/email_routes.py:3395`
- `routes/email_routes.py:3446`
- `routes/email_routes.py:3716`
- `routes/email_routes.py:4207`
- `routes/email_routes.py:4913`

## `_imap_search_quote` — function, line 526
- **called from:**
- `routes/email_routes.py:1039`
- `routes/email_routes.py:1991`
- `routes/email_routes.py:2293`

## `_message_id_chain` — function, line 530
- **called from:**
- `routes/email_routes.py:2278`

## `_uid_from_fetch_meta` — function, line 541
- **called from:**
- `mcp_servers/email_server.py:691`
- `routes/email_routes.py:730`
- `routes/email_routes.py:2555`
- `tests/test_email_gmail_fetch_flags.py:43`
- `tests/test_email_gmail_fetch_flags.py:47`

## `_parse_list_unsubscribe_header` — function, line 546
- **called from:**
- `mcp_servers/email_server.py:585`
- `routes/email_routes.py:604`
- `tests/test_email_unsubscribe_candidates.py:11`

## `_email_unsubscribe_candidate_from_msg` — function, line 597
- **called from:**
- `mcp_servers/email_server.py:698`
- `mcp_servers/email_server.py:738`
- `routes/email_routes.py:2564`
- `routes/email_routes.py:2634`
- `tests/test_email_unsubscribe_candidates.py:38`
- `tests/test_email_unsubscribe_candidates.py:49`
- `tests/test_email_unsubscribe_candidates.py:77`
- `tests/test_email_unsubscribe_candidates.py:78`

## `_unsubscribe_candidate_dedupe_key` — function, line 650
- **called from:**
- `mcp_servers/email_server.py:635`
- `routes/email_routes.py:666`

## `_dedupe_unsubscribe_candidates` — function, line 663
- **called from:**
- `mcp_servers/email_server.py:702`
- `routes/email_routes.py:2573`
- `tests/test_email_unsubscribe_candidates.py:81`

## `_group_uid_fetch_records` — function, line 691
- **called from:**
- `routes/email_routes.py:2071`
- `routes/email_routes.py:2882`
- `routes/email_routes.py:2891`
- `tests/test_email_gmail_fetch_flags.py:40`
- `tests/test_email_gmail_fetch_flags.py:53`
- `tests/test_email_gmail_fetch_flags.py:62`
- `tests/test_email_gmail_fetch_flags.py:68`
- `tests/test_email_gmail_fetch_flags.py:69`
- `tests/test_email_gmail_fetch_flags.py:71`

## `_account_cache_key` — function, line 723
- **called from:**
- `routes/email_routes.py:790`
- `routes/email_routes.py:831`
- `routes/email_routes.py:903`
- `routes/email_routes.py:1058`
- `routes/email_routes.py:1117`
- `routes/email_routes.py:1128`
- `routes/email_routes.py:1144`
- `routes/email_routes.py:1149`
- `routes/email_routes.py:1168`
- `routes/email_routes.py:1206`
- `routes/email_routes.py:1231`
- `routes/email_routes.py:1271`
- `routes/email_routes.py:1946`
- `routes/email_routes.py:2431`

## `_parse_email_list_record` — function, line 727
- **called from:**
- `routes/email_routes.py:2113`
- `routes/email_routes.py:2892`

## `_email_index_rows` — function, line 776
- **called from:**
- `routes/email_routes.py:2056`
- `routes/email_routes.py:2863`
- `tests/test_email_owner_scope.py:253`
- `tests/test_email_owner_scope.py:260`
- `tests/test_email_owner_scope.py:265`

## `_email_index_list` — function, line 822
- **called from:**
- `routes/email_routes.py:2346`

## `_email_index_search` — function, line 898
- **called from:**
- `routes/email_routes.py:2796`

## `_email_search_terms` — function, line 989
- **called from:**
- `routes/email_routes.py:913`
- `routes/email_routes.py:1034`

## `_imap_or_many` — function, line 1024
- **called from:**
- `routes/email_routes.py:1043`

## `_email_imap_search_criteria` — function, line 1033
- **called from:**
- `routes/email_routes.py:2834`

## `_email_index_upsert` — function, line 1047
- **called from:**
- `routes/email_routes.py:2117`
- `routes/email_routes.py:2903`
- `tests/test_email_owner_scope.py:232`

## `_email_index_update_flags` — function, line 1111
- **called from:**
- `routes/email_routes.py:3028`
- `routes/email_routes.py:3168`
- `routes/email_routes.py:3740`
- `routes/email_routes.py:3757`
- `routes/email_routes.py:3772`
- `routes/email_routes.py:3996`
- `routes/email_routes.py:4012`
- `routes/email_routes.py:4656`
- `tests/test_email_owner_scope.py:258`
- `tests/test_email_owner_scope.py:259`

## `_email_index_delete` — function, line 1137
- **called from:**
- `routes/email_routes.py:2661`
- `routes/email_routes.py:2711`
- `routes/email_routes.py:3789`
- `routes/email_routes.py:3804`
- `routes/email_routes.py:3820`
- `routes/email_routes.py:3910`
- `tests/test_email_owner_scope.py:264`

## `_email_preview_cache_get` — function, line 1158
- **called from:**
- `routes/email_routes.py:3208`

## `_email_preview_cache_put` — function, line 1184
- **called from:**
- `routes/email_routes.py:3224`

## `_email_attachment_meta_cache_get` — function, line 1221
- **called from:**
- `routes/email_routes.py:3012`
- `routes/email_routes.py:3282`

## `_email_attachment_meta_cache_put` — function, line 1255
- **called from:**
- `routes/email_routes.py:3043`
- `routes/email_routes.py:3294`

## `_smtp_ready` — function, line 1286
- **called from:**
- `mcp_servers/email_server.py:1318`
- `mcp_servers/email_server.py:1325`
- `mcp_servers/email_server.py:1333`
- `routes/email_routes.py:1301`
- `routes/email_routes.py:1317`
- `routes/note/note_routes.py:314`
- `routes/note/note_routes.py:327`
- `tests/test_email_oauth.py:103`
- `tests/test_email_oauth.py:115`
- `tests/test_email_oauth.py:127`
- `tests/test_email_oauth.py:134`

## `_resolve_send_config` — function, line 1292
- **called from:**
- `mcp_servers/email_server.py:1488`
- `routes/email_routes.py:2644`
- `routes/email_routes.py:4256`
- `routes/email_routes.py:4528`
- `src/task_scheduler.py:1829`

## `_store_email_flag` — function, line 1326
- **called from:**
- `routes/email_routes.py:3738`
- `routes/email_routes.py:3755`
- `routes/email_routes.py:3770`
- `routes/email_routes.py:3817`
- `routes/email_routes.py:3994`
- `routes/email_routes.py:4010`
- `routes/email_routes.py:4655`
- `tests/test_email_uid_no_seqno_fallback.py:67`
- `tests/test_email_uid_no_seqno_fallback.py:79`

## `_move_email_message` — function, line 1338
- **called from:**
- `routes/email_routes.py:2659`
- `routes/email_routes.py:2709`
- `routes/email_routes.py:3787`
- `routes/email_routes.py:3802`
- `routes/email_routes.py:3908`
- `tests/test_email_uid_no_seqno_fallback.py:73`
- `tests/test_email_uid_no_seqno_fallback.py:86`

## `_apply_odysseus_headers` — function, line 1359
- **called from:**
- `routes/email_routes.py:2652`
- `routes/email_routes.py:4274`
- `routes/email_routes.py:4559`

## `_normalize_addr_field` — function, line 1367
- **called from:**
- `routes/email_routes.py:4265`
- `routes/email_routes.py:4266`
- `routes/email_routes.py:4267`
- `routes/email_routes.py:4543`
- `routes/email_routes.py:4544`
- `routes/email_routes.py:4545`

## `_envelope_recipients` — function, line 1381
- **called from:**
- `routes/email_routes.py:4287`
- `routes/email_routes.py:4578`
- `tests/test_email_envelope_recipients.py:13`
- `tests/test_email_envelope_recipients.py:17`
- `tests/test_email_envelope_recipients.py:21`
- `tests/test_email_envelope_recipients.py:26`

## `_md_to_email_html` — function, line 1395
- **called from:**
- `routes/email_routes.py:4281`
- `routes/email_routes.py:4569`

## `_inline` — function, line 1403
- **called from:**
- `routes/email_routes.py:1423`
- `routes/email_routes.py:1427`
- `routes/email_routes.py:1431`
- `routes/email_routes.py:1435`

## `_EmailHtmlSanitizer` — class, line 1448
- **called from:**
- `routes/email_routes.py:1501`

## `_EmailHtmlSanitizer.__init__` — method, line 1454
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

## `_EmailHtmlSanitizer.handle_starttag` — method, line 1459
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_EmailHtmlSanitizer.handle_startendtag` — method, line 1479
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_EmailHtmlSanitizer.handle_endtag` — method, line 1483
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_EmailHtmlSanitizer.handle_data` — method, line 1492
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_sanitize_email_html` — function, line 1498
- **called from:**
- `routes/email_routes.py:4568`
- `routes/email_routes.py:4735`

## `setup_email_routes` — function, line 1513
- **called from:**
- `app.py:862`
- `tests/test_email_account_default_serialization.py:49`
- `tests/test_email_account_port_validation.py:43`
- `tests/test_email_imap_timeout.py:118`
- `tests/test_email_oauth.py:268`
- `tests/test_email_oauth.py:436`
- `tests/test_email_oauth.py:849`
- `tests/test_email_oauth.py:901`
- `tests/test_email_owner_scope.py:298`
- `tests/test_email_owner_scope.py:377`
- `tests/test_email_owner_scope.py:461`
- `tests/test_email_owner_scope.py:519`
- `tests/test_email_owner_scope.py:567`
- `tests/test_email_read_mark_seen.py:95`
- `tests/test_email_read_mark_seen.py:125`
- `tests/test_email_read_mark_seen.py:162`
- `tests/test_email_read_mark_seen.py:189`
- `tests/test_email_read_mark_seen.py:214`
- `tests/test_email_read_mark_seen.py:237`
- `tests/test_email_read_mark_seen.py:260`
- `tests/test_email_summary_llm.py:227`
- `tests/test_email_summary_llm.py:298`
- `tests/test_email_test_connection_oauth.py:75`
- `tests/test_email_test_connection_oauth.py:128`
- `tests/test_email_test_connection_oauth.py:173`
- `tests/test_email_test_connection_oauth.py:222`
- `tests/test_email_test_connection_oauth.py:260`
- `tests/test_email_test_connection_oauth.py:317`
- `tests/test_email_test_connection_oauth.py:393`
- `tests/test_schedule_email_offset_normalization.py:34`

## `_pooled_connect` — function, line 1547
- **called from:**
- `routes/email_routes.py:1859`

## `_pooled_release` — function, line 1581
- **called from:**
- `routes/email_routes.py:2265`

## `_list_cache_key` — function, line 1591
- **called from:**
- `routes/email_routes.py:2375`

## `_read_cache_key` — function, line 1594
- **called from:**
- `routes/chat_routes.py:1295`
- `routes/email_routes.py:3190`
- `routes/email_routes.py:3248`

## `_list_cache_get` — function, line 1600
- **called from:**
- `routes/email_routes.py:2377`

## `_list_cache_put` — function, line 1608
- **called from:**
- `routes/email_routes.py:2399`

## `_folder_cache_get` — function, line 1615
- **called from:**
- `routes/email_routes.py:3926`

## `_folder_cache_get_stale` — function, line 1625
- **called from:**
- `routes/email_routes.py:3934`
- `routes/email_routes.py:3971`

## `_folder_cache_put` — function, line 1629
- **called from:**
- `routes/email_routes.py:3967`

## `_invalidate_list_cache` — function, line 1635
- **called from:**
- `routes/email_routes.py:2662`
- `routes/email_routes.py:2718`
- `routes/email_routes.py:3741`
- `routes/email_routes.py:3758`
- `routes/email_routes.py:3773`
- `routes/email_routes.py:3790`
- `routes/email_routes.py:3805`
- `routes/email_routes.py:3821`
- `routes/email_routes.py:3896`
- `routes/email_routes.py:3911`
- `routes/email_routes.py:3998`
- `routes/email_routes.py:4013`
- `routes/email_routes.py:4658`

## `_update_list_cache_seen` — function, line 1652
- **called from:**
- `routes/email_routes.py:3029`
- `routes/email_routes.py:3169`

## `_read_cache_get` — function, line 1674
- **called from:**
- `routes/chat_routes.py:1296`
- `routes/email_routes.py:3191`
- `routes/email_routes.py:3249`
- `routes/email_routes.py:3261`

## `_read_cache_put` — function, line 1682
- **called from:**
- `routes/email_routes.py:3210`
- `routes/email_routes.py:3222`
- `routes/email_routes.py:3267`

## `_fixture_email_file` — function, line 1705
- **called from:**
- `mcp_servers/email_server.py:829`
- `mcp_servers/email_server.py:874`
- `routes/email_routes.py:1709`
- `routes/email_routes.py:1712`

## `_fixture_email_enabled` — function, line 1708
- **called from:**
- `mcp_servers/email_server.py:896`
- `mcp_servers/email_server.py:931`
- `mcp_servers/email_server.py:946`
- `mcp_servers/email_server.py:954`
- `routes/email_routes.py:1773`
- `routes/email_routes.py:1807`
- `routes/email_routes.py:2596`
- `routes/email_routes.py:3924`

## `_fixture_email_rows` — function, line 1711
- **called from:**
- `mcp_servers/email_server.py:900`
- `mcp_servers/email_server.py:942`
- `mcp_servers/email_server.py:958`
- `routes/email_routes.py:1777`
- `routes/email_routes.py:1811`
- `routes/email_routes.py:2426`

## `_fixture_email_record` — function, line 1732
- **called from:**
- `mcp_servers/email_server.py:890`
- `routes/email_routes.py:1728`

## `_fixture_email_list` — function, line 1772
- **called from:**
- `routes/email_routes.py:2342`
- `routes/email_routes.py:2422`

## `_fixture_email_read` — function, line 1806
- **called from:**
- `routes/email_routes.py:3187`

## `_list_emails_sync` — function, line 1843
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_imap_search_quote` — function, line 1985
- **called from:**
- `routes/email_routes.py:1039`
- `routes/email_routes.py:1991`
- `routes/email_routes.py:2293`

## `_related_thread_attachments_sync` — function, line 2267
- **called from:**
- `routes/email_routes.py:3033`

## `list_emails` — function (async), line 2327
- **route:** `GET /list`
- decorator: `router.get("/list")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unread_state` — function (async), line 2410
- **route:** `GET /unread-state`
- decorator: `router.get("/unread-state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unflag_spam` — function (async), line 2484
- **route:** `POST /{uid}/unflag-spam`
- decorator: `router.post("/{uid}/unflag-spam")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_unsubscribe_spam_cache` — function, line 2500
- **called from:**
- `routes/email_routes.py:2529`

## `_scan_unsubscribe_candidates_sync` — function, line 2525
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_uid_sort_value` — function, line 2567
- **called from:**
- `routes/email_routes.py:2574`

## `scan_unsubscribe_candidates` — function (async), line 2586
- **route:** `GET /unsubscribe/scan`
- decorator: `router.get("/unsubscribe/scan")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `execute_unsubscribe` — function, line 2605
- **route:** `POST /unsubscribe/execute`
- decorator: `router.post("/unsubscribe/execute")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_unsubscribe_candidates` — function, line 2678
- **route:** `POST /unsubscribe/cleanup`
- decorator: `router.post("/unsubscribe/cleanup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_contacts` — function (async), line 2725
- **route:** `GET /contacts`
- decorator: `router.get("/contacts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_emails` — function, line 2773
- **route:** `GET /search`
- decorator: `router.get("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_read_email_sync` — function, line 2923
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_mark_email_seen_sync` — function, line 3160
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_email_by_uid` — function (async), line 3176
- **route:** `GET /read/{uid}`
- decorator: `router.get("/read/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_schedule_recent_email_warm` — function, line 3227
- **called from:**
- `routes/email_routes.py:2379`
- `routes/email_routes.py:2398`

## `_warm` — function (async), line 3258
- **called from:**
- `routes/email_routes.py:3275`

## `list_attachments` — function (async), line 3280
- **route:** `GET /attachments/{uid}`
- decorator: `router.get("/attachments/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_attachment` — function (async), line 3301
- **route:** `GET /attachment/{uid}/{index}`
- decorator: `router.get("/attachment/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_all_attachments` — function (async), line 3328
- **route:** `GET /attachments-download/{uid}`
- decorator: `router.get("/attachments-download/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `inline_image` — function (async), line 3381
- **route:** `GET /inline-image/{uid}`
- decorator: `router.get("/inline-image/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `attachment_as_doc` — function, line 3432
- **route:** `POST /attachment-as-doc/{uid}/{index}`
- decorator: `router.post("/attachment-as-doc/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_tag_doc_with_source` — function, line 3475
- **called from:**
- `routes/email_routes.py:3537`
- `routes/email_routes.py:3620`

## `_resolve_doc_session` — function, line 3501
- **called from:**
- `routes/email_routes.py:3516`

## `_create_markdown_doc` — function, line 3518
- **called from:**
- `routes/email_routes.py:3653`
- `routes/email_routes.py:3693`
- `routes/email_routes.py:3702`

## `_attached_email_markdown` — function, line 3540
- **called from:**
- `routes/email_routes.py:3649`

## `_attachment_bytes_from_msg` — function, line 3625
- **called from:**
- `routes/email_routes.py:3649`

## `get_attachment_path` — function (async), line 3711
- **route:** `POST /attachment-path/{uid}/{index}`
- decorator: `router.post("/attachment-path/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_unread` — function (async), line 3733
- **route:** `POST /mark-unread/{uid}`
- decorator: `router.post("/mark-unread/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `flag_email` — function (async), line 3748
- **route:** `POST /flag/{uid}`
- decorator: `router.post("/flag/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_read` — function (async), line 3765
- **route:** `POST /mark-read/{uid}`
- decorator: `router.post("/mark-read/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `archive_email` — function, line 3782
- **route:** `POST /archive/{uid}`
- decorator: `router.post("/archive/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email` — function (async), line 3797
- **route:** `DELETE /delete/{uid}`
- decorator: `router.delete("/delete/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email_permanent` — function (async), line 3812
- **route:** `DELETE /delete-permanent/{uid}`
- decorator: `router.delete("/delete-permanent/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_odysseus_reminder_emails` — function (async), line 3828
- **route:** `DELETE /odysseus/reminders`
- decorator: `router.delete("/odysseus/reminders")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_search_quote` — function, line 3847
- **called from:**
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3874`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`

## `_search_uids` — function, line 3850
- **called from:**
- `mcp_servers/email_server.py:2854`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`

## `move_email` — function (async), line 3903
- **route:** `POST /move/{uid}`
- decorator: `router.post("/move/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_folders` — function (async), line 3918
- **route:** `GET /folders`
- decorator: `router.get("/folders")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_list_folders_sync` — function, line 3946
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_answered` — function (async), line 3989
- **route:** `POST /mark-answered/{uid}`
- decorator: `router.post("/mark-answered/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_answered` — function (async), line 4005
- **route:** `POST /clear-answered/{uid}`
- decorator: `router.post("/clear-answered/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compose_upload` — function (async), line 4020
- **route:** `POST /compose-upload`
- decorator: `router.post("/compose-upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_safe_compose_filename` — function, line 4042
- **called from:**
- `routes/email_routes.py:4049`
- `routes/email_routes.py:4062`
- `routes/email_routes.py:4096`
- `routes/email_routes.py:4111`

## `_stage_compose_bytes` — function, line 4046
- **called from:**
- `routes/email_routes.py:4130`
- `routes/email_routes.py:4182`

## `_stage_compose_file` — function, line 4056
- **called from:**
- `routes/email_routes.py:4129`

## `_load_odysseus_attachment_source` — function, line 4069
- **called from:**
- `routes/email_routes.py:4127`
- `routes/email_routes.py:4173`

## `compose_from_odysseus` — function (async), line 4116
- **route:** `POST /compose-from-odysseus`
- decorator: `router.post("/compose-from-odysseus")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compose_from_odysseus_zip` — function (async), line 4140
- **route:** `POST /compose-from-odysseus-zip`
- decorator: `router.post("/compose-from-odysseus-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unique_name` — function, line 4155
- **called from:**
- `routes/email_routes.py:4174`

## `compose_from_attachment` — function (async), line 4192
- **route:** `POST /compose-from-attachment/{uid}/{index}`
- decorator: `router.post("/compose-from-attachment/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_compose_upload` — function (async), line 4232
- **route:** `DELETE /compose-upload/{token}`
- decorator: `router.delete("/compose-upload/{token}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_send_email_sync` — function (async), line 4245
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `schedule_email` — function (async), line 4294
- **route:** `POST /schedule`
- decorator: `router.post("/schedule")`
- **called from:**
- `tests/test_email_owner_scope.py:467`
- `tests/test_email_owner_scope.py:471`

## `list_scheduled` — function (async), line 4360
- **route:** `GET /scheduled`
- decorator: `router.get("/scheduled")`
- **called from:**
- `tests/test_email_owner_scope.py:479`
- `tests/test_email_owner_scope.py:480`
- `tests/test_email_owner_scope.py:486`
- `tests/test_email_owner_scope.py:490`

## `cancel_scheduled` — function (async), line 4383
- **route:** `DELETE /scheduled/{sid}`
- decorator: `router.delete("/scheduled/{sid}")`
- **called from:**
- `tests/test_email_owner_scope.py:485`
- `tests/test_email_owner_scope.py:489`

## `list_pending_agent_drafts` — function (async), line 4407
- **route:** `GET /pending`
- decorator: `router.get("/pending")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `approve_agent_draft` — function (async), line 4426
- **route:** `POST /pending/{sid}/approve`
- decorator: `router.post("/pending/{sid}/approve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cancel_agent_draft` — function (async), line 4450
- **route:** `DELETE /pending/{sid}`
- decorator: `router.delete("/pending/{sid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `resolve_contact` — function (async), line 4471
- **route:** `GET /resolve-contact`
- decorator: `router.get("/resolve-contact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `send_email` — function (async), line 4519
- **route:** `POST /send`
- decorator: `router.post("/send")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_deliver` — function, line 4604
- **called from:**
- `src/webhook_manager.py:385`
- `src/webhook_manager.py:390`
- `tests/test_webhook_dns_rebinding_pin.py:149`
- `tests/test_webhook_ssrf_resilience.py:117`

## `save_draft` — function (async), line 4723
- **route:** `POST /draft`
- decorator: `router.post("/draft")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_do_append` — function, line 4758
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `extract_writing_style` — function (async), line 4775
- **route:** `POST /extract-style`
- decorator: `router.post("/extract-style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_gather_samples` — function, line 4789
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `summarize_email` — function (async), line 4884
- **route:** `POST /summarize`
- decorator: `router.post("/summarize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_atts` — function, line 4910
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `translate_email` — function (async), line 5001
- **route:** `POST /translate`
- decorator: `router.post("/translate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_add` — function, line 5051
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:1832`
- `mcp_servers/email_server.py:1836`
- `mcp_servers/email_server.py:1844`
- `routes/email_routes.py:5059`
- `routes/email_routes.py:5063`
- `routes/email_routes.py:5067`
- `routes/email_routes.py:5342`
- `routes/email_routes.py:5347`
- `routes/email_routes.py:5353`
- `routes/email_routes.py:5358`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `static/js/emailLibrary.js:3632`
- `static/js/emailLibrary.js:3635`
- `static/js/emailLibrary.js:3647`

## `ai_reply` — function (async), line 5148
- **route:** `POST /ai-reply`
- decorator: `router.post("/ai-reply")`
- **called from:**
- `tests/test_email_owner_scope.py:301`

## `_add` — function, line 5335
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:1832`
- `mcp_servers/email_server.py:1836`
- `mcp_servers/email_server.py:1844`
- `routes/email_routes.py:5059`
- `routes/email_routes.py:5063`
- `routes/email_routes.py:5067`
- `routes/email_routes.py:5342`
- `routes/email_routes.py:5347`
- `routes/email_routes.py:5353`
- `routes/email_routes.py:5358`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `static/js/emailLibrary.js:3632`
- `static/js/emailLibrary.js:3635`
- `static/js/emailLibrary.js:3647`

## `get_writing_style` — function (async), line 5442
- **route:** `GET /style`
- decorator: `router.get("/style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_writing_style` — function (async), line 5453
- **route:** `PUT /style`
- decorator: `router.put("/style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_email_config` — function (async), line 5467
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_email_config` — function (async), line 5510
- **route:** `PUT /config`
- decorator: `router.put("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_email_urgency_state` — function (async), line 5583
- **route:** `GET /urgency-state`
- decorator: `router.get("/urgency-state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_email_accounts` — function (async), line 5605
- **route:** `GET /accounts`
- decorator: `router.get("/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_email_account` — function (async), line 5649
- **route:** `POST /accounts`
- decorator: `router.post("/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_email_account` — function (async), line 5704
- **route:** `PUT /accounts/{account_id}`
- decorator: `router.put("/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email_account` — function (async), line 5742
- **route:** `DELETE /accounts/{account_id}`
- decorator: `router.delete("/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `test_account_config` — function (async), line 5781
- **route:** `POST /accounts/test`
- decorator: `router.post("/accounts/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_google_token` — function, line 5861
- **called from:**
- `routes/email_routes.py:5900`
- `routes/email_routes.py:5962`

## `set_default_account` — function (async), line 5987
- **route:** `POST /accounts/{account_id}/set-default`
- decorator: `router.post("/accounts/{account_id}/set-default")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `google_oauth_authorize` — function (async), line 6010
- **route:** `GET /oauth/google/authorize`
- decorator: `router.get("/oauth/google/authorize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `google_oauth_callback` — function (async), line 6034
- **route:** `GET /oauth/google/callback`
- decorator: `router.get("/oauth/google/callback")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
