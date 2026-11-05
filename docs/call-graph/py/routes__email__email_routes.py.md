# `routes/email/email_routes.py` — definitions & call sites

214 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_check_mail_host` — function, line 91
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_normalized_mail_host` — function, line 102
- **called from:**
- `routes/email/email_routes.py:7607`
- `routes/email/email_routes.py:7649`

## `_google_oauth_imap_transport_allowed` — function, line 107
- **called from:**
- `routes/email/email_routes.py:7609`

## `_google_oauth_smtp_transport_allowed` — function, line 111
- **called from:**
- `routes/email/email_routes.py:7654`

## `_email_style_key` — function, line 114
- **called from:**
- `routes/email/email_routes.py:119`
- `routes/email/email_routes.py:129`
- `routes/email/email_routes.py:143`
- `routes/email/email_routes.py:153`
- `routes/email/email_routes.py:183`
- `routes/email/email_routes.py:192`

## `_get_email_writing_style_for_account` — function, line 118
- **called from:**
- `routes/email/email_routes.py:6931`
- `routes/email/email_routes.py:7220`

## `_set_email_writing_style_for_account` — function, line 128
- **called from:**
- `routes/email/email_routes.py:6574`
- `routes/email/email_routes.py:7232`

## `_get_email_view_inline_images` — function, line 141
- **called from:**
- `routes/email/email_routes.py:7273`

## `_set_email_view_inline_images` — function, line 152
- **called from:**
- `routes/email/email_routes.py:7312`

## `_get_auto_reply_settings_for_account` — function, line 182
- **called from:**
- `routes/email/email_routes.py:193`
- `routes/email/email_routes.py:7258`

## `_set_auto_reply_settings_for_account` — function, line 191
- **called from:**
- `routes/email/email_routes.py:7313`

## `_safe_attachment_zip_name` — function, line 218
- **called from:**
- `routes/email/email_routes.py:4192`
- `routes/email/email_routes.py:4203`
- `routes/email/email_routes.py:4250`
- `routes/email/email_routes.py:4251`
- `routes/email/email_routes.py:4343`
- `routes/email/email_routes.py:4394`
- `routes/email/email_routes.py:4731`
- `routes/email/email_routes.py:5790`

## `_coerce_port` — function, line 226
- **called from:**
- `routes/email/email_routes.py:7436`
- `routes/email/email_routes.py:7439`
- `routes/email/email_routes.py:7509`
- `routes/email/email_routes.py:7580`
- `routes/email/email_routes.py:7646`
- `tests/test_email_account_port_validation.py:22`
- `tests/test_email_account_port_validation.py:23`
- `tests/test_email_account_port_validation.py:28`
- `tests/test_email_account_port_validation.py:29`
- `tests/test_email_account_port_validation.py:34`

## `_lock_email_account_owner_mutation` — function, line 241
- **called from:**
- `routes/email/email_routes.py:283`
- `routes/email/email_routes.py:7321`
- `routes/email/email_routes.py:7449`

## `_email_account_owner_scope` — function, line 248
- **called from:**
- `routes/email/email_routes.py:7323`
- `routes/email/email_routes.py:7349`
- `routes/email/email_routes.py:7476`
- `routes/email/email_routes.py:7555`
- `routes/email/email_routes.py:7797`

## `_discover_email_account_mutation_scope` — function, line 258
- **called from:**
- `routes/email/email_routes.py:7532`
- `routes/email/email_routes.py:7788`

## `_lock_and_reload_email_account` — function, line 277
- **called from:**
- `routes/email/email_routes.py:7536`
- `routes/email/email_routes.py:7792`

## `_email_tag_owner_aliases` — function, line 299
- **called from:**
- `routes/email/email_routes.py:334`

## `_email_tag_owner_clause` — function, line 333
- **called from:**
- `routes/email/email_routes.py:383`
- `routes/email/email_routes.py:2445`
- `routes/email/email_routes.py:2589`
- `routes/email/email_routes.py:2647`
- `routes/email/email_routes.py:2698`
- `routes/email/email_routes.py:3107`
- `routes/email/email_routes.py:3125`
- `routes/email/email_routes.py:3505`
- `tests/test_email_owner_scope.py:26`
- `tests/test_email_owner_scope.py:42`

## `_email_tag_account_clause` — function, line 343
- **called from:**
- `routes/email/email_routes.py:384`
- `routes/email/email_routes.py:2446`
- `routes/email/email_routes.py:2590`
- `routes/email/email_routes.py:2648`
- `routes/email/email_routes.py:2699`
- `routes/email/email_routes.py:3126`

## `_sanitize_visible_email_tags` — function, line 357
- **called from:**
- `routes/email/email_routes.py:2172`
- `routes/email/email_routes.py:2502`
- `routes/email/email_routes.py:2602`
- `routes/email/email_routes.py:2663`
- `routes/email/email_routes.py:2685`
- `routes/email/email_routes.py:2724`
- `routes/email/email_routes.py:2734`

## `_hide_unlinked_calendar_tags` — function, line 372
- **called from:**
- `routes/email/email_routes.py:2767`
- `routes/email/email_routes.py:2923`
- `routes/email/email_routes.py:2996`

## `_clear_done_response_tags` — function, line 380
- **called from:**
- `routes/email/email_routes.py:5631`
- `routes/email/email_routes.py:6314`

## `_record_email_received_events` — function, line 408
- **called from:**
- `routes/email/email_routes.py:3015`

## `_run_away_reply_check` — function (async), line 464
- **called from:**
- `routes/email/email_routes.py:477`

## `_folder_name_from_list_line` — function, line 484
- **called from:**
- `mcp_servers/email_server.py:495`
- `mcp_servers/email_server.py:507`
- `routes/email/email_routes.py:497`
- `routes/email/email_routes.py:519`

## `_list_imap_folders` — function, line 492
- **called from:**
- `routes/email/email_routes.py:505`
- `routes/email/email_routes.py:5307`
- `routes/email/email_routes.py:5370`

## `_resolve_mail_folder` — function, line 503
- **called from:**
- `routes/email/email_routes.py:1495`
- `routes/email/email_routes.py:1517`
- `routes/email/email_routes.py:2389`
- `routes/email/email_routes.py:3622`
- `routes/email/email_routes.py:3756`
- `routes/email/email_routes.py:5302`
- `routes/email/email_routes.py:5367`

## `_mail_folder_role_hint` — function, line 538
- **called from:**
- `routes/email/email_routes.py:2389`
- `routes/email/email_routes.py:3622`
- `routes/email/email_routes.py:3757`

## `_folder_role_from_name` — function, line 555
- **called from:**
- `mcp_servers/email_server.py:3286`
- `mcp_servers/email_server.py:3376`
- `routes/email/email_routes.py:1495`
- `routes/email/email_routes.py:1517`

## `_uid_bytes` — function, line 566
- **called from:**
- `routes/email/email_routes.py:572`
- `routes/email/email_routes.py:584`
- `routes/email/email_routes.py:594`
- `routes/email/email_routes.py:635`
- `routes/email/email_routes.py:1490`
- `routes/email/email_routes.py:1502`
- `routes/email/email_routes.py:1505`
- `routes/email/email_routes.py:1508`
- `routes/email/email_routes.py:1520`
- `routes/email/email_routes.py:1523`
- `routes/email/email_routes.py:3826`
- `routes/email/email_routes.py:3975`
- `routes/email/email_routes.py:5384`
- `routes/email/email_routes.py:5386`
- `routes/email/email_routes.py:5394`
- `routes/email/email_routes.py:5414`
- `routes/email/email_routes.py:5433`

## `_uid_exists` — function, line 570
- **called from:**
- `routes/email/email_routes.py:611`
- `routes/email/email_routes.py:1487`
- `routes/email/email_routes.py:1500`
- `routes/email/email_routes.py:1518`
- `routes/email/email_routes.py:5381`

## `_uid_has_deleted_flag` — function, line 591
- **called from:**
- `routes/email/email_routes.py:5392`

## `_resolve_current_email_uid` — function, line 608
- **called from:**
- `routes/email/email_routes.py:5291`
- `tests/test_review_email_delete_lookup.py:12`
- `tests/test_review_email_delete_lookup.py:19`
- `tests/test_review_email_delete_lookup.py:25`
- `tests/test_review_email_delete_lookup.py:32`
- `tests/test_review_email_delete_lookup.py:38`

## `_imap_uid_search` — function, line 630
- **called from:**
- `routes/email/email_routes.py:617`
- `routes/email/email_routes.py:2405`
- `routes/email/email_routes.py:2408`
- `routes/email/email_routes.py:2410`
- `routes/email/email_routes.py:2413`
- `routes/email/email_routes.py:2418`
- `routes/email/email_routes.py:2427`
- `routes/email/email_routes.py:2433`
- `routes/email/email_routes.py:2524`
- `routes/email/email_routes.py:2535`
- `routes/email/email_routes.py:2537`
- `routes/email/email_routes.py:2552`
- `routes/email/email_routes.py:2854`
- `routes/email/email_routes.py:3160`
- `routes/email/email_routes.py:3260`
- `routes/email/email_routes.py:3633`

## `_imap_uid_fetch` — function, line 634
- **called from:**
- `routes/email/email_routes.py:2622`
- `routes/email/email_routes.py:2861`
- `routes/email/email_routes.py:3182`
- `routes/email/email_routes.py:3194`
- `routes/email/email_routes.py:3273`
- `routes/email/email_routes.py:3329`
- `routes/email/email_routes.py:3671`
- `routes/email/email_routes.py:3781`
- `routes/email/email_routes.py:4109`
- `routes/email/email_routes.py:4141`
- `routes/email/email_routes.py:4168`
- `routes/email/email_routes.py:4304`
- `routes/email/email_routes.py:4471`
- `routes/email/email_routes.py:4500`
- `routes/email/email_routes.py:4600`
- `routes/email/email_routes.py:4680`
- `routes/email/email_routes.py:4773`
- `routes/email/email_routes.py:4825`
- `routes/email/email_routes.py:5186`
- `routes/email/email_routes.py:5841`
- `routes/email/email_routes.py:6614`

## `_imap_search_quote` — function, line 638
- **called from:**
- `routes/email/email_routes.py:617`
- `routes/email/email_routes.py:1166`
- `routes/email/email_routes.py:2524`
- `routes/email/email_routes.py:2854`
- `routes/email/email_routes.py:3260`

## `_message_id_chain` — function, line 642
- **called from:**
- `routes/email/email_routes.py:2839`

## `_uid_from_fetch_meta` — function, line 653
- **called from:**
- `mcp_servers/email_server.py:803`
- `mcp_servers/email_server.py:1751`
- `routes/email/email_routes.py:852`
- `routes/email/email_routes.py:3204`
- `routes/email/email_routes.py:3277`
- `routes/email/email_routes.py:4310`
- `routes/email/email_routes.py:4487`
- `routes/email/email_routes.py:4503`
- `routes/email/email_routes.py:4621`
- `routes/email/email_routes.py:4687`
- `tests/test_email_gmail_fetch_flags.py:43`
- `tests/test_email_gmail_fetch_flags.py:47`
- `tests/test_email_library_bulk_actions.py:762`
- `tests/test_email_library_bulk_actions.py:767`
- `tests/test_email_library_bulk_actions.py:780`
- `tests/test_email_library_bulk_actions.py:784`
- `tests/test_email_library_bulk_actions.py:786`
- `tests/test_email_library_bulk_actions.py:791`
- `tests/test_email_library_bulk_actions.py:793`
- `tests/test_email_library_bulk_actions.py:795`

## `_size_from_fetch_meta` — function, line 658
- **called from:**
- `routes/email/email_routes.py:4489`
- `routes/email/email_routes.py:4623`
- `tests/test_email_library_bulk_actions.py:763`
- `tests/test_email_library_bulk_actions.py:768`
- `tests/test_email_library_bulk_actions.py:781`
- `tests/test_email_library_bulk_actions.py:785`
- `tests/test_email_library_bulk_actions.py:787`
- `tests/test_email_library_bulk_actions.py:788`
- `tests/test_email_library_bulk_actions.py:792`
- `tests/test_email_library_bulk_actions.py:794`
- `tests/test_email_library_bulk_actions.py:796`

## `_parse_list_unsubscribe_header` — function, line 663
- **called from:**
- `mcp_servers/email_server.py:615`
- `routes/email/email_routes.py:721`
- `tests/test_email_unsubscribe_candidates.py:11`

## `_email_unsubscribe_candidate_from_msg` — function, line 714
- **called from:**
- `mcp_servers/email_server.py:668`
- `mcp_servers/email_server.py:810`
- `mcp_servers/email_server.py:881`
- `routes/email/email_routes.py:3213`
- `routes/email/email_routes.py:3284`
- `routes/email/email_routes.py:3338`
- `tests/test_email_unsubscribe_candidates.py:38`
- `tests/test_email_unsubscribe_candidates.py:49`
- `tests/test_email_unsubscribe_candidates.py:77`
- `tests/test_email_unsubscribe_candidates.py:78`

## `_unsubscribe_candidate_dedupe_key` — function, line 767
- **called from:**
- `mcp_servers/email_server.py:692`
- `routes/email/email_routes.py:788`

## `_dedupe_unsubscribe_candidates` — function, line 785
- **called from:**
- `mcp_servers/email_server.py:730`
- `mcp_servers/email_server.py:814`
- `routes/email/email_routes.py:3222`
- `tests/test_email_unsubscribe_candidates.py:81`
- `tests/test_email_unsubscribe_candidates.py:104`

## `_group_uid_fetch_records` — function, line 813
- **called from:**
- `routes/email/email_routes.py:2630`
- `routes/email/email_routes.py:3202`
- `routes/email/email_routes.py:3276`
- `routes/email/email_routes.py:3679`
- `routes/email/email_routes.py:3688`
- `routes/email/email_routes.py:4309`
- `routes/email/email_routes.py:4502`
- `routes/email/email_routes.py:4686`
- `tests/test_email_gmail_fetch_flags.py:40`
- `tests/test_email_gmail_fetch_flags.py:53`
- `tests/test_email_gmail_fetch_flags.py:62`
- `tests/test_email_gmail_fetch_flags.py:68`
- `tests/test_email_gmail_fetch_flags.py:69`
- `tests/test_email_gmail_fetch_flags.py:71`

## `_account_cache_key` — function, line 845
- **called from:**
- `routes/email/email_routes.py:916`
- `routes/email/email_routes.py:957`
- `routes/email/email_routes.py:1029`
- `routes/email/email_routes.py:1188`
- `routes/email/email_routes.py:1247`
- `routes/email/email_routes.py:1258`
- `routes/email/email_routes.py:1274`
- `routes/email/email_routes.py:1279`
- `routes/email/email_routes.py:1298`
- `routes/email/email_routes.py:1336`
- `routes/email/email_routes.py:1361`
- `routes/email/email_routes.py:1404`
- `routes/email/email_routes.py:1430`
- `routes/email/email_routes.py:2479`
- `routes/email/email_routes.py:3051`

## `_parse_email_list_record` — function, line 849
- **called from:**
- `routes/email/email_routes.py:2672`
- `routes/email/email_routes.py:3689`
- `tests/test_email_attachment_search.py:60`

## `_email_index_rows` — function, line 902
- **called from:**
- `routes/email/email_routes.py:2615`
- `routes/email/email_routes.py:3660`
- `tests/test_email_owner_scope.py:253`
- `tests/test_email_owner_scope.py:260`
- `tests/test_email_owner_scope.py:265`

## `_email_index_list` — function, line 948
- **called from:**
- `routes/email/email_routes.py:2919`
- `routes/email/email_routes.py:2976`
- `tests/test_email_list_stale_while_revalidate.py:205`
- `tests/test_email_list_stale_while_revalidate.py:245`

## `_email_index_search` — function, line 1024
- **called from:**
- `routes/email/email_routes.py:3584`
- `tests/test_email_attachment_search.py:28`

## `_email_search_terms` — function, line 1116
- **called from:**
- `mcp_servers/email_server.py:2114`
- `routes/email/email_routes.py:1039`
- `routes/email/email_routes.py:1161`

## `_imap_or_many` — function, line 1151
- **called from:**
- `routes/email/email_routes.py:1173`

## `_email_imap_search_criteria` — function, line 1160
- **called from:**
- `routes/email/email_routes.py:3631`
- `tests/test_email_attachment_search.py:78`

## `_email_index_upsert` — function, line 1177
- **called from:**
- `routes/email/email_routes.py:2678`
- `routes/email/email_routes.py:3702`
- `tests/test_email_list_stale_while_revalidate.py:156`
- `tests/test_email_list_stale_while_revalidate.py:218`
- `tests/test_email_owner_scope.py:232`

## `_email_index_update_flags` — function, line 1241
- **called from:**
- `routes/email/email_routes.py:1949`
- `tests/test_email_owner_scope.py:258`
- `tests/test_email_owner_scope.py:259`

## `_email_index_delete` — function, line 1267
- **called from:**
- `routes/email/email_routes.py:1954`
- `tests/test_email_owner_scope.py:264`

## `_email_preview_cache_get` — function, line 1288
- **called from:**
- `routes/email/email_routes.py:4022`

## `_email_preview_cache_put` — function, line 1314
- **called from:**
- `routes/email/email_routes.py:4038`

## `_email_attachment_meta_cache_get` — function, line 1351
- **called from:**
- `routes/email/email_routes.py:3823`
- `routes/email/email_routes.py:4099`

## `_email_attachment_meta_cache_put` — function, line 1385
- **called from:**
- `routes/email/email_routes.py:3853`
- `routes/email/email_routes.py:4104`
- `routes/email/email_routes.py:4115`
- `tests/test_email_attachment_search.py:150`
- `tests/test_email_attachment_search.py:153`

## `_smtp_ready` — function, line 1442
- **called from:**
- `mcp_servers/email_server.py:2509`
- `mcp_servers/email_server.py:2516`
- `mcp_servers/email_server.py:2524`
- `routes/email/email_routes.py:1457`
- `routes/email/email_routes.py:1473`
- `routes/note/note_routes.py:317`
- `routes/note/note_routes.py:330`
- `tests/test_email_oauth.py:103`
- `tests/test_email_oauth.py:115`
- `tests/test_email_oauth.py:127`
- `tests/test_email_oauth.py:134`

## `_resolve_send_config` — function, line 1448
- **called from:**
- `mcp_servers/email_server.py:2679`
- `routes/email/email_routes.py:3348`
- `routes/email/email_routes.py:5890`
- `routes/email/email_routes.py:6162`
- `src/task_scheduler.py:1991`

## `_store_email_flag` — function, line 1482
- **called from:**
- `routes/email/email_routes.py:3380`
- `routes/email/email_routes.py:5208`
- `routes/email/email_routes.py:5228`
- `routes/email/email_routes.py:5246`
- `routes/email/email_routes.py:5332`
- `routes/email/email_routes.py:5628`
- `routes/email/email_routes.py:5644`
- `routes/email/email_routes.py:6312`
- `routes/email/email_routes.py:6353`
- `routes/email/email_routes.py:6453`
- `tests/test_email_uid_no_seqno_fallback.py:67`
- `tests/test_email_uid_no_seqno_fallback.py:79`

## `_move_email_message` — function, line 1494
- **called from:**
- `routes/email/email_routes.py:3365`
- `routes/email/email_routes.py:3378`
- `routes/email/email_routes.py:3461`
- `routes/email/email_routes.py:5266`
- `routes/email/email_routes.py:5314`
- `routes/email/email_routes.py:5542`
- `tests/test_email_uid_no_seqno_fallback.py:73`
- `tests/test_email_uid_no_seqno_fallback.py:86`

## `_copy_and_delete_email_message` — function, line 1515
- **called from:**
- `routes/email/email_routes.py:3459`

## `_apply_odysseus_headers` — function, line 1530
- **called from:**
- `routes/email/email_routes.py:3356`
- `routes/email/email_routes.py:5908`
- `routes/email/email_routes.py:6205`

## `_normalize_addr_field` — function, line 1538
- **called from:**
- `routes/email/email_routes.py:5899`
- `routes/email/email_routes.py:5900`
- `routes/email/email_routes.py:5901`
- `routes/email/email_routes.py:6185`
- `routes/email/email_routes.py:6186`
- `routes/email/email_routes.py:6187`

## `_envelope_recipients` — function, line 1552
- **called from:**
- `routes/email/email_routes.py:5921`
- `routes/email/email_routes.py:6224`
- `tests/test_email_envelope_recipients.py:13`
- `tests/test_email_envelope_recipients.py:17`
- `tests/test_email_envelope_recipients.py:21`
- `tests/test_email_envelope_recipients.py:26`

## `_md_links_to_html` — function, line 1569
- **called from:**
- `routes/email/email_routes.py:1619`
- `tests/test_redos_residual_python.py:81`

## `_md_to_email_html` — function, line 1604
- **called from:**
- `routes/email/email_routes.py:5915`
- `routes/email/email_routes.py:6215`
- `tests/test_redos_residual_python.py:97`

## `_inline` — function, line 1612
- **called from:**
- `routes/email/email_routes.py:1632`
- `routes/email/email_routes.py:1636`
- `routes/email/email_routes.py:1640`
- `routes/email/email_routes.py:1644`

## `_EmailHtmlSanitizer` — class, line 1657
- **called from:**
- `routes/email/email_routes.py:1710`

## `_EmailHtmlSanitizer.__init__` — method, line 1663
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

## `_EmailHtmlSanitizer.handle_starttag` — method, line 1668
- **called from:**
- `src/agent_tools/document_tools.py:768`

## `_EmailHtmlSanitizer.handle_startendtag` — method, line 1688
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_EmailHtmlSanitizer.handle_endtag` — method, line 1692
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_EmailHtmlSanitizer.handle_data` — method, line 1701
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_sanitize_email_html` — function, line 1707
- **called from:**
- `routes/email/email_routes.py:6214`
- `routes/email/email_routes.py:6404`

## `setup_email_routes` — function, line 1722
- **called from:**
- `app.py:946`
- `tests/test_codeql_python_residual_closure.py:438`
- `tests/test_codeql_python_residual_closure.py:490`
- `tests/test_codeql_python_residual_followup.py:185`
- `tests/test_codeql_python_residual_followup.py:251`
- `tests/test_email_account_default_serialization.py:49`
- `tests/test_email_account_host_ssrf.py:131`
- `tests/test_email_account_host_ssrf.py:152`
- `tests/test_email_account_host_ssrf.py:168`
- `tests/test_email_account_host_ssrf.py:182`
- `tests/test_email_account_host_ssrf.py:201`
- `tests/test_email_account_host_ssrf.py:216`
- `tests/test_email_account_host_ssrf.py:242`
- `tests/test_email_account_host_ssrf.py:261`
- `tests/test_email_account_host_ssrf.py:299`
- `tests/test_email_account_host_ssrf.py:427`
- `tests/test_email_account_host_ssrf.py:505`
- `tests/test_email_account_port_validation.py:43`
- `tests/test_email_bulk_delete_safety.py:110`
- `tests/test_email_fixture_reply_account.py:16`
- `tests/test_email_fixture_reply_account.py:35`
- `tests/test_email_imap_timeout.py:118`
- `tests/test_email_library_bulk_actions.py:322`
- `tests/test_email_library_bulk_actions.py:461`
- `tests/test_email_library_bulk_actions.py:507`
- `tests/test_email_library_bulk_actions.py:540`
- `tests/test_email_list_stale_while_revalidate.py:17`
- `tests/test_email_list_stale_while_revalidate.py:192`
- `tests/test_email_list_stale_while_revalidate.py:239`
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
- `tests/test_email_summary_llm.py:271`
- `tests/test_email_summary_llm.py:342`
- `tests/test_email_test_connection_oauth.py:75`
- `tests/test_email_test_connection_oauth.py:128`
- `tests/test_email_test_connection_oauth.py:173`
- `tests/test_email_test_connection_oauth.py:222`
- `tests/test_email_test_connection_oauth.py:260`
- `tests/test_email_test_connection_oauth.py:317`
- `tests/test_email_test_connection_oauth.py:393`
- `tests/test_schedule_email_offset_normalization.py:34`

## `_pooled_connect` — function, line 1756
- **called from:**
- `routes/email/email_routes.py:2385`

## `_pooled_release` — function, line 1790
- **called from:**
- `routes/email/email_routes.py:2826`

## `_invalidate_imap_pool` — function, line 1800
- **called from:**
- `routes/email/email_routes.py:2951`

## `_list_cache_key` — function, line 1821
- **called from:**
- `routes/email/email_routes.py:2948`

## `_read_cache_key` — function, line 1824
- **called from:**
- `routes/chat_routes.py:2929`
- `routes/email/email_routes.py:4004`
- `routes/email/email_routes.py:4062`

## `_list_cache_get` — function, line 1837
- **called from:**
- `routes/email/email_routes.py:2953`

## `_list_stale_get` — function, line 1846
- **called from:**
- `routes/email/email_routes.py:2973`
- `routes/email/email_routes.py:2998`

## `_list_stale_put` — function, line 1850
- **called from:**
- `routes/email/email_routes.py:1862`

## `_list_cache_put` — function, line 1858
- **called from:**
- `routes/email/email_routes.py:1886`
- `routes/email/email_routes.py:3019`

## `_schedule_list_refresh` — function, line 1867
- **called from:**
- `routes/email/email_routes.py:3001`

## `_run` — function, line 1879
- **called from:**
- `services/hwfit/hardware.py:87`
- `services/hwfit/hardware.py:94`
- `services/hwfit/hardware.py:108`
- `services/hwfit/hardware.py:110`
- `services/hwfit/hardware.py:211`
- `services/hwfit/hardware.py:221`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:294`
- `services/hwfit/hardware.py:323`
- `services/hwfit/hardware.py:325`
- `services/hwfit/hardware.py:338`
- `services/hwfit/hardware.py:341`
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`
- `services/hwfit/hardware.py:393`
- `services/hwfit/hardware.py:422`
- `services/hwfit/hardware.py:466`
- `services/hwfit/hardware.py:491`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:549`
- `services/hwfit/hardware.py:554`
- `services/hwfit/hardware.py:557`
- `services/hwfit/hardware.py:562`
- `services/hwfit/hardware.py:635`
- `services/research/research_handler.py:102`
- `services/search/providers.py:268`
- `services/search/providers.py:281`
- `services/search/providers.py:290`
- `services/search/providers.py:298`
- `src/research_handler.py:421`
- `tests/test_agent_evidence_loop.py:128`
- `tests/test_agent_evidence_loop.py:140`
- `tests/test_agent_evidence_loop.py:152`
- `tests/test_agent_evidence_loop.py:163`
- `tests/test_agent_evidence_loop.py:189`
- `tests/test_agent_evidence_loop.py:222`
- `tests/test_agent_evidence_loop.py:262`
- `tests/test_agent_evidence_loop.py:304`
- `tests/test_agent_evidence_loop.py:356`
- `tests/test_agent_evidence_loop.py:399`
- `tests/test_agent_evidence_loop.py:439`
- `tests/test_agent_evidence_loop.py:461`
- `tests/test_agent_evidence_loop.py:627`
- `tests/test_agent_evidence_loop.py:649`
- `tests/test_agent_evidence_loop.py:677`
- `tests/test_agent_evidence_loop.py:715`
- `tests/test_agent_rounds_exhausted.py:24`
- `tests/test_agent_runtime_context.py:28`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- … +208 more (grep the name in repo)

## `_folder_cache_get` — function, line 1900
- **called from:**
- `routes/email/email_routes.py:5560`

## `_folder_cache_get_stale` — function, line 1910
- **called from:**
- `routes/email/email_routes.py:5568`
- `routes/email/email_routes.py:5605`

## `_folder_cache_put` — function, line 1914
- **called from:**
- `routes/email/email_routes.py:5601`

## `_invalidate_list_cache` — function, line 1920
- **called from:**
- `routes/email/email_routes.py:1950`
- `routes/email/email_routes.py:1955`
- `routes/email/email_routes.py:2950`
- `routes/email/email_routes.py:3368`
- `routes/email/email_routes.py:3385`
- `routes/email/email_routes.py:3473`
- `routes/email/email_routes.py:5211`
- `routes/email/email_routes.py:5231`
- `routes/email/email_routes.py:5249`
- `routes/email/email_routes.py:5269`
- `routes/email/email_routes.py:5300`
- `routes/email/email_routes.py:5320`
- `routes/email/email_routes.py:5336`
- `routes/email/email_routes.py:5454`
- `routes/email/email_routes.py:5456`
- `routes/email/email_routes.py:5527`
- `routes/email/email_routes.py:5545`
- `routes/email/email_routes.py:5632`
- `routes/email/email_routes.py:5647`
- `routes/email/email_routes.py:6315`

## `_index_update_flags` — function, line 1947
- **called from:**
- `routes/email/email_routes.py:3839`
- `routes/email/email_routes.py:3978`
- `routes/email/email_routes.py:5210`
- `routes/email/email_routes.py:5230`
- `routes/email/email_routes.py:5248`
- `routes/email/email_routes.py:5630`
- `routes/email/email_routes.py:5646`
- `routes/email/email_routes.py:6313`

## `_index_delete` — function, line 1952
- **called from:**
- `routes/email/email_routes.py:3367`
- `routes/email/email_routes.py:3384`
- `routes/email/email_routes.py:3466`
- `routes/email/email_routes.py:5268`
- `routes/email/email_routes.py:5299`
- `routes/email/email_routes.py:5317`
- `routes/email/email_routes.py:5319`
- `routes/email/email_routes.py:5335`
- `routes/email/email_routes.py:5403`
- `routes/email/email_routes.py:5425`
- `routes/email/email_routes.py:5544`

## `_update_list_cache_seen` — function, line 1957
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_read_cache_get` — function, line 2002
- **called from:**
- `routes/chat_routes.py:2930`
- `routes/email/email_routes.py:4005`
- `routes/email/email_routes.py:4063`
- `routes/email/email_routes.py:4075`

## `_read_cache_put` — function, line 2010
- **called from:**
- `routes/email/email_routes.py:4024`
- `routes/email/email_routes.py:4036`
- `routes/email/email_routes.py:4081`

## `_fixture_email_file` — function, line 2033
- **called from:**
- `mcp_servers/email_server.py:1119`
- `mcp_servers/email_server.py:1212`
- `mcp_servers/email_server.py:1237`
- `mcp_servers/email_server.py:1314`
- `mcp_servers/email_server.py:1551`
- `mcp_servers/email_server.py:3461`
- `routes/email/email_routes.py:2037`
- `routes/email/email_routes.py:2079`
- `routes/email/email_routes.py:2103`
- `routes/email/email_routes.py:2127`
- `routes/email/email_routes.py:2230`
- `routes/email/email_routes.py:2334`

## `_fixture_email_enabled` — function, line 2036
- **called from:**
- `mcp_servers/email_server.py:722`
- `mcp_servers/email_server.py:833`
- `mcp_servers/email_server.py:1252`
- `mcp_servers/email_server.py:1310`
- `mcp_servers/email_server.py:1422`
- `mcp_servers/email_server.py:1476`
- `mcp_servers/email_server.py:1495`
- `mcp_servers/email_server.py:1521`
- `mcp_servers/email_server.py:1547`
- `mcp_servers/email_server.py:2935`
- `mcp_servers/email_server.py:3189`
- `mcp_servers/email_server.py:3221`
- `mcp_servers/email_server.py:3264`
- `mcp_servers/email_server.py:3347`
- `mcp_servers/email_server.py:3460`
- `mcp_servers/email_server.py:4052`
- `mcp_servers/email_server.py:4090`
- `mcp_servers/email_server.py:4120`
- `mcp_servers/email_server.py:4140`
- `routes/email/email_routes.py:2075`
- `routes/email/email_routes.py:2220`
- `routes/email/email_routes.py:2288`
- `routes/email/email_routes.py:2332`
- `routes/email/email_routes.py:3300`
- `routes/email/email_routes.py:5280`
- `routes/email/email_routes.py:5558`

## `_fixture_folder_key` — function, line 2039
- **called from:**
- `mcp_servers/email_server.py:1136`
- `mcp_servers/email_server.py:1137`
- `mcp_servers/email_server.py:1169`
- `routes/email/email_routes.py:2052`
- `routes/email/email_routes.py:2053`

## `_fixture_folder_matches` — function, line 2051
- **called from:**
- `mcp_servers/email_server.py:1329`
- `mcp_servers/email_server.py:1484`
- `mcp_servers/email_server.py:1528`
- `mcp_servers/email_server.py:1570`
- `mcp_servers/email_server.py:3476`
- `routes/email/email_routes.py:2094`
- `routes/email/email_routes.py:2226`
- `routes/email/email_routes.py:2293`
- `routes/email/email_routes.py:2352`

## `_fixture_attachment_meta` — function, line 2058
- **called from:**
- `mcp_servers/email_server.py:1172`
- `routes/email/email_routes.py:2162`

## `_fixture_attachment_source` — function, line 2074
- **called from:**
- `mcp_servers/email_server.py:3534`
- `routes/email/email_routes.py:4124`
- `routes/email/email_routes.py:4281`
- `routes/email/email_routes.py:4427`
- `routes/email/email_routes.py:5173`

## `_fixture_email_rows` — function, line 2102
- **called from:**
- `mcp_servers/email_server.py:1257`
- `mcp_servers/email_server.py:1341`
- `mcp_servers/email_server.py:1483`
- `mcp_servers/email_server.py:1525`
- `routes/email/email_routes.py:2225`
- `routes/email/email_routes.py:2292`
- `routes/email/email_routes.py:3046`

## `_fixture_owner_has_rows` — function, line 2123
- **called from:**
- `mcp_servers/email_server.py:1478`
- `mcp_servers/email_server.py:1497`
- `mcp_servers/email_server.py:1523`
- `routes/email/email_routes.py:2077`
- `routes/email/email_routes.py:2222`
- `routes/email/email_routes.py:2290`

## `_fixture_email_record` — function, line 2141
- **called from:**
- `mcp_servers/email_server.py:1228`
- `mcp_servers/email_server.py:1572`
- `mcp_servers/email_server.py:3481`
- `routes/email/email_routes.py:2119`

## `_fixture_email_matches` — function, line 2203
- **called from:**
- `mcp_servers/email_server.py:1515`
- `routes/email/email_routes.py:2241`

## `_fixture_email_list` — function, line 2219
- **called from:**
- `routes/email/email_routes.py:2914`
- `routes/email/email_routes.py:3042`
- `routes/email/email_routes.py:3563`

## `_fixture_email_read` — function, line 2287
- **called from:**
- `routes/email/email_routes.py:3996`
- `routes/email/email_routes.py:4096`
- `routes/email/email_routes.py:4275`
- `routes/email/email_routes.py:4461`
- `routes/email/email_routes.py:4553`

## `_fixture_email_update` — function, line 2331
- **called from:**
- `routes/email/email_routes.py:5222`
- `routes/email/email_routes.py:5240`
- `routes/email/email_routes.py:5260`
- `routes/email/email_routes.py:5282`
- `routes/email/email_routes.py:5536`

## `_list_emails_sync` — function, line 2367
- **called from:**
- `routes/email/email_routes.py:1881`

## `_imap_search_quote` — function, line 2518
- **called from:**
- `routes/email/email_routes.py:617`
- `routes/email/email_routes.py:1166`
- `routes/email/email_routes.py:2524`
- `routes/email/email_routes.py:2854`
- `routes/email/email_routes.py:3260`

## `_related_thread_attachments_sync` — function, line 2828
- **called from:**
- `routes/email/email_routes.py:3843`

## `list_emails` — function (async), line 2888
- **route:** `GET /list`
- decorator: `router.get("/list")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unread_state` — function (async), line 3030
- **route:** `GET /unread-state`
- decorator: `router.get("/unread-state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unflag_spam` — function (async), line 3104
- **route:** `POST /{uid}/unflag-spam`
- decorator: `router.post("/{uid}/unflag-spam")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_unsubscribe_spam_cache` — function, line 3120
- **called from:**
- `routes/email/email_routes.py:3154`

## `_scan_unsubscribe_candidates_sync` — function, line 3145
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_uid_sort_value` — function, line 3216
- **called from:**
- `routes/email/email_routes.py:3223`

## `_unsubscribe_sender_uids_sync` — function, line 3236
- **called from:**
- `routes/email/email_routes.py:3430`

## `scan_unsubscribe_candidates` — function (async), line 3290
- **route:** `GET /unsubscribe/scan`
- decorator: `router.get("/unsubscribe/scan")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `execute_unsubscribe` — function, line 3309
- **route:** `POST /unsubscribe/execute`
- decorator: `router.post("/unsubscribe/execute")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cleanup_unsubscribe_candidates` — function, line 3404
- **route:** `POST /unsubscribe/cleanup`
- decorator: `router.post("/unsubscribe/cleanup")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_contacts` — function (async), line 3492
- **route:** `GET /contacts`
- decorator: `router.get("/contacts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `search_emails` — function, line 3540
- **route:** `GET /search`
- decorator: `router.get("/search")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_read_email_sync` — function, line 3722
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_mark_email_seen_sync` — function, line 3970
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `read_email_by_uid` — function (async), line 3985
- **route:** `GET /read/{uid}`
- decorator: `router.get("/read/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_schedule_recent_email_warm` — function, line 4041
- **called from:**
- `routes/email/email_routes.py:1888`
- `routes/email/email_routes.py:2955`
- `routes/email/email_routes.py:3016`

## `_warm` — function (async), line 4072
- **called from:**
- `routes/email/email_routes.py:4089`

## `list_attachments` — function (async), line 4094
- **route:** `GET /attachments/{uid}`
- decorator: `router.get("/attachments/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_attachment` — function (async), line 4122
- **route:** `GET /attachment/{uid}/{index}`
- decorator: `router.get("/attachment/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_all_attachments` — function (async), line 4163
- **route:** `GET /attachments-download/{uid}`
- decorator: `router.get("/attachments-download/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `download_bulk_attachments` — function (async), line 4216
- **route:** `POST /attachments-download-bulk`
- decorator: `router.post("/attachments-download-bulk")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_add_bytes` — function, line 4248
- **called from:**
- `routes/email/email_routes.py:4287`
- `routes/email/email_routes.py:4328`

## `download_bulk_messages` — function (async), line 4351
- **route:** `POST /messages-download-bulk`
- decorator: `router.post("/messages-download-bulk")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_email_filename` — function, line 4386
- **called from:**
- `routes/email/email_routes.py:4458`
- `routes/email/email_routes.py:4555`
- `routes/email/email_routes.py:4579`

## `_fixture_message_bytes` — function, line 4396
- **called from:**
- `routes/email/email_routes.py:4463`
- `routes/email/email_routes.py:4562`

## `_iter_spooled` — function, line 4734
- **called from:**
- `routes/email/email_routes.py:4746`

## `inline_image` — function (async), line 4759
- **route:** `GET /inline-image/{uid}`
- decorator: `router.get("/inline-image/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `attachment_as_doc` — function, line 4810
- **route:** `POST /attachment-as-doc/{uid}/{index}`
- decorator: `router.post("/attachment-as-doc/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_tag_doc_with_source` — function, line 4857
- **called from:**
- `routes/email/email_routes.py:4919`
- `routes/email/email_routes.py:5049`

## `_resolve_doc_session` — function, line 4883
- **called from:**
- `routes/email/email_routes.py:4898`

## `_create_markdown_doc` — function, line 4900
- **called from:**
- `routes/email/email_routes.py:5129`
- `routes/email/email_routes.py:5151`
- `routes/email/email_routes.py:5162`

## `_attached_email_markdown` — function, line 4922
- **called from:**
- `routes/email/email_routes.py:5125`

## `_store_pdf_upload` — function, line 4959
- **called from:**
- `routes/email/email_routes.py:5021`

## `_create_pdf_document_from_path` — function, line 5012
- **called from:**
- `routes/email/email_routes.py:5097`
- `routes/email/email_routes.py:5149`

## `_convert_docx_to_pdf` — function, line 5052
- **called from:**
- `routes/email/email_routes.py:5147`

## `_attachment_bytes_from_msg` — function, line 5101
- **called from:**
- `routes/email/email_routes.py:5125`

## `get_attachment_path` — function (async), line 5171
- **route:** `POST /attachment-path/{uid}/{index}`
- decorator: `router.post("/attachment-path/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_unread` — function (async), line 5203
- **route:** `POST /mark-unread/{uid}`
- decorator: `router.post("/mark-unread/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `flag_email` — function (async), line 5218
- **route:** `POST /flag/{uid}`
- decorator: `router.post("/flag/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_read` — function (async), line 5238
- **route:** `POST /mark-read/{uid}`
- decorator: `router.post("/mark-read/{uid}")`
- **called from:**
- `tests/test_email_list_stale_while_revalidate.py:199`
- `tests/test_email_list_stale_while_revalidate.py:243`

## `archive_email` — function, line 5258
- **route:** `POST /archive/{uid}`
- decorator: `router.post("/archive/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email` — function (async), line 5276
- **route:** `DELETE /delete/{uid}`
- decorator: `router.delete("/delete/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email_permanent` — function (async), line 5327
- **route:** `DELETE /delete-permanent/{uid}`
- decorator: `router.delete("/delete-permanent/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email_bulk` — function, line 5343
- **route:** `POST /delete-bulk`
- decorator: `router.post("/delete-bulk")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_odysseus_reminder_emails` — function (async), line 5459
- **route:** `DELETE /odysseus/reminders`
- decorator: `router.delete("/odysseus/reminders")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_search_quote` — function, line 5478
- **called from:**
- `routes/email/email_routes.py:5502`
- `routes/email/email_routes.py:5503`
- `routes/email/email_routes.py:5505`
- `routes/email/email_routes.py:5506`
- `routes/email/email_routes.py:5511`

## `_search_uids` — function, line 5481
- **called from:**
- `mcp_servers/email_server.py:4620`
- `routes/email/email_routes.py:5502`
- `routes/email/email_routes.py:5503`
- `routes/email/email_routes.py:5506`
- `routes/email/email_routes.py:5511`

## `move_email` — function (async), line 5534
- **route:** `POST /move/{uid}`
- decorator: `router.post("/move/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_folders` — function (async), line 5552
- **route:** `GET /folders`
- decorator: `router.get("/folders")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_list_folders_sync` — function, line 5580
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `mark_answered` — function (async), line 5623
- **route:** `POST /mark-answered/{uid}`
- decorator: `router.post("/mark-answered/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_answered` — function (async), line 5639
- **route:** `POST /clear-answered/{uid}`
- decorator: `router.post("/clear-answered/{uid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compose_upload` — function (async), line 5654
- **route:** `POST /compose-upload`
- decorator: `router.post("/compose-upload")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_safe_compose_filename` — function, line 5676
- **called from:**
- `routes/email/email_routes.py:5683`
- `routes/email/email_routes.py:5696`
- `routes/email/email_routes.py:5730`
- `routes/email/email_routes.py:5745`

## `_stage_compose_bytes` — function, line 5680
- **called from:**
- `routes/email/email_routes.py:5764`
- `routes/email/email_routes.py:5816`

## `_stage_compose_file` — function, line 5690
- **called from:**
- `routes/email/email_routes.py:5763`

## `_load_odysseus_attachment_source` — function, line 5703
- **called from:**
- `routes/email/email_routes.py:5761`
- `routes/email/email_routes.py:5807`

## `compose_from_odysseus` — function (async), line 5750
- **route:** `POST /compose-from-odysseus`
- decorator: `router.post("/compose-from-odysseus")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `compose_from_odysseus_zip` — function (async), line 5774
- **route:** `POST /compose-from-odysseus-zip`
- decorator: `router.post("/compose-from-odysseus-zip")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `unique_name` — function, line 5789
- **called from:**
- `routes/email/email_routes.py:5808`

## `compose_from_attachment` — function (async), line 5826
- **route:** `POST /compose-from-attachment/{uid}/{index}`
- decorator: `router.post("/compose-from-attachment/{uid}/{index}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_compose_upload` — function (async), line 5866
- **route:** `DELETE /compose-upload/{token}`
- decorator: `router.delete("/compose-upload/{token}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_send_email_sync` — function (async), line 5879
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `schedule_email` — function (async), line 5928
- **route:** `POST /schedule`
- decorator: `router.post("/schedule")`
- **called from:**
- `tests/test_email_owner_scope.py:467`
- `tests/test_email_owner_scope.py:471`

## `list_scheduled` — function (async), line 5994
- **route:** `GET /scheduled`
- decorator: `router.get("/scheduled")`
- **called from:**
- `tests/test_email_owner_scope.py:479`
- `tests/test_email_owner_scope.py:480`
- `tests/test_email_owner_scope.py:486`
- `tests/test_email_owner_scope.py:490`

## `cancel_scheduled` — function (async), line 6017
- **route:** `DELETE /scheduled/{sid}`
- decorator: `router.delete("/scheduled/{sid}")`
- **called from:**
- `tests/test_email_owner_scope.py:485`
- `tests/test_email_owner_scope.py:489`

## `list_pending_agent_drafts` — function (async), line 6041
- **route:** `GET /pending`
- decorator: `router.get("/pending")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `approve_agent_draft` — function (async), line 6060
- **route:** `POST /pending/{sid}/approve`
- decorator: `router.post("/pending/{sid}/approve")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `cancel_agent_draft` — function (async), line 6084
- **route:** `DELETE /pending/{sid}`
- decorator: `router.delete("/pending/{sid}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `resolve_contact` — function (async), line 6105
- **route:** `GET /resolve-contact`
- decorator: `router.get("/resolve-contact")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `send_email` — function (async), line 6153
- **route:** `POST /send`
- decorator: `router.post("/send")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_deliver` — function, line 6252
- **called from:**
- `src/webhook_manager.py:385`
- `src/webhook_manager.py:390`
- `tests/test_webhook_dns_rebinding_pin.py:149`
- `tests/test_webhook_ssrf_resilience.py:117`

## `save_draft` — function (async), line 6390
- **route:** `POST /draft`
- decorator: `router.post("/draft")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_do_append` — function, line 6432
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `extract_writing_style` — function (async), line 6471
- **route:** `POST /extract-style`
- decorator: `router.post("/extract-style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_gather_samples` — function, line 6485
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `summarize_email` — function (async), line 6585
- **route:** `POST /summarize`
- decorator: `router.post("/summarize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_fetch_atts` — function, line 6611
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `translate_email` — function (async), line 6703
- **route:** `POST /translate`
- decorator: `router.post("/translate")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_add` — function, line 6753
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:3079`
- `mcp_servers/email_server.py:3083`
- `mcp_servers/email_server.py:3091`
- `routes/email/email_routes.py:6761`
- `routes/email/email_routes.py:6765`
- `routes/email/email_routes.py:6769`
- `routes/email/email_routes.py:7089`
- `routes/email/email_routes.py:7094`
- `routes/email/email_routes.py:7100`
- `routes/email/email_routes.py:7105`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `tests/test_notes_reminder_temporal_redos.py:47`
- `tests/test_notes_reminder_temporal_redos.py:53`
- `static/js/emailLibrary/index.js:3723`
- `static/js/emailLibrary/index.js:3726`
- `static/js/emailLibrary/index.js:3738`

## `ai_reply` — function (async), line 6853
- **route:** `POST /ai-reply`
- decorator: `router.post("/ai-reply")`
- **called from:**
- `routes/email/email_routes.py:6859`
- `tests/test_email_owner_scope.py:301`

## `events` — function (async), line 6856
- **called from:**
- `routes/email/email_routes.py:6871`
- `scripts/eval_odysseus_crud.py:226`
- `static/js/chat.js:4735`
- `static/js/dragSort.js:212`
- `static/js/editor/layer-panel.js:138`
- `static/js/galleryEditor.js:10526`

## `run` — function (async), line 6858
- **called from:**
- `app.py:1228`
- `app.py:1530`
- `core/platform_compat.py:428`
- `core/platform_compat.py:469`
- `launcher.py:114`
- `launcher.py:149`
- `mcp_servers/email_server.py:4704`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/email_server.py:4710`
- `mcp_servers/image_gen_server.py:188`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/image_gen_server.py:192`
- `mcp_servers/memory_server.py:281`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/rag_server.py:156`
- `mcp_servers/rag_server.py:160`
- `mcp_servers/rag_server.py:160`
- `routes/cookbook_routes.py:1527`
- `routes/cookbook_routes.py:3626`
- `routes/cookbook_routes.py:3639`
- `routes/cookbook_routes.py:3650`
- `routes/cookbook_routes.py:3711`
- `routes/cookbook_routes.py:4177`
- `routes/cookbook_routes.py:4179`
- `routes/cookbook_routes.py:4201`
- `routes/cookbook_routes.py:4203`
- `routes/cookbook_routes.py:4368`
- `routes/cookbook_routes.py:4378`
- `routes/document/document_routes.py:489`
- `routes/email/email_routes.py:5062`
- `routes/email/email_routes.py:6861`
- `routes/hwfit_routes.py:147`
- `scripts/build_frontend.py:69`
- `scripts/build_frontend.py:70`
- `scripts/check_brotli.py:39`
- `scripts/css_snapshot.py:92`
- `scripts/css_snapshot.py:131`
- `scripts/diffusion_server.py:1506`
- `scripts/dump_agent_prompt.py:415`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_everyday_live_hard.py:586`
- `scripts/eval_odysseus_live_hard_examples.py:464`
- `scripts/eval_qwen_tool_groups_stream.py:276`
- `scripts/mlx_image_server.py:207`
- `scripts/mlx_image_server.py:281`
- `scripts/mlx_image_server.py:379`
- `scripts/mlx_image_server.py:466`
- `scripts/pr_blocker_audit.py:253`
- `scripts/probe_browser_budget.py:112`
- `scripts/probe_empty_search_recovery.py:90`
- `scripts/probe_fixed_search_evidence.py:81`
- `scripts/ref_parity_audit.py:142`
- `scripts/ref_parity_audit.py:232`
- `scripts/review_sft_environment_expansion.py:115`
- `scripts/run_odysseus_cases_chunked.py:107`
- `scripts/run_odysseus_search_teacher_pipeline.py:305`
- `scripts/run_odysseus_search_teacher_pipeline.py:412`
- `scripts/test_clean_tool_loop.py:209`
- … +1417 more (grep the name in repo)

## `_add` — function, line 7082
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:3079`
- `mcp_servers/email_server.py:3083`
- `mcp_servers/email_server.py:3091`
- `routes/email/email_routes.py:6761`
- `routes/email/email_routes.py:6765`
- `routes/email/email_routes.py:6769`
- `routes/email/email_routes.py:7089`
- `routes/email/email_routes.py:7094`
- `routes/email/email_routes.py:7100`
- `routes/email/email_routes.py:7105`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `tests/test_notes_reminder_temporal_redos.py:47`
- `tests/test_notes_reminder_temporal_redos.py:53`
- `static/js/emailLibrary/index.js:3723`
- `static/js/emailLibrary/index.js:3726`
- `static/js/emailLibrary/index.js:3738`

## `get_writing_style` — function (async), line 7212
- **route:** `GET /style`
- decorator: `router.get("/style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_writing_style` — function (async), line 7223
- **route:** `PUT /style`
- decorator: `router.put("/style")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_email_config` — function (async), line 7237
- **route:** `GET /config`
- decorator: `router.get("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_email_config` — function (async), line 7281
- **route:** `PUT /config`
- decorator: `router.put("/config")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `get_email_urgency_state` — function (async), line 7362
- **route:** `GET /urgency-state`
- decorator: `router.get("/urgency-state")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_email_accounts` — function (async), line 7384
- **route:** `GET /accounts`
- decorator: `router.get("/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `create_email_account` — function (async), line 7428
- **route:** `POST /accounts`
- decorator: `router.post("/accounts")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `update_email_account` — function (async), line 7488
- **route:** `PUT /accounts/{account_id}`
- decorator: `router.put("/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_email_account` — function (async), line 7531
- **route:** `DELETE /accounts/{account_id}`
- decorator: `router.delete("/accounts/{account_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_test_mail_connections` — function, line 7569
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_google_token` — function, line 7594
- **called from:**
- `routes/email/email_routes.py:7634`
- `routes/email/email_routes.py:7697`

## `test_account_config` — function (async), line 7722
- **route:** `POST /accounts/test`
- decorator: `router.post("/accounts/test")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_default_account` — function (async), line 7787
- **route:** `POST /accounts/{account_id}/set-default`
- decorator: `router.post("/accounts/{account_id}/set-default")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `google_oauth_authorize` — function (async), line 7810
- **route:** `GET /oauth/google/authorize`
- decorator: `router.get("/oauth/google/authorize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `google_oauth_callback` — function (async), line 7834
- **route:** `GET /oauth/google/callback`
- decorator: `router.get("/oauth/google/callback")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
