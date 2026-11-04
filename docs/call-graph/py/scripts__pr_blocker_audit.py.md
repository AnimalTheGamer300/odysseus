# `scripts/pr_blocker_audit.py` — definitions & call sites

74 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `PullRequest` — class, line 97
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/pr_blocker_audit.py:284`

## `ScoredPullRequest` — class, line 110
- decorator: `dataclass(frozen=True)`
- **called from:**
- `scripts/pr_blocker_audit.py:495`

## `ProgressReporter` — class, line 116
- **called from:**
- `scripts/pr_blocker_audit.py:165`
- `scripts/pr_blocker_audit.py:196`
- `scripts/pr_blocker_audit.py:1031`

## `ProgressReporter.__init__` — method, line 117
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

## `ProgressReporter.phase` — method, line 122
- **called from:**
- `scripts/pr_blocker_audit.py:172`
- `scripts/pr_blocker_audit.py:203`

## `ProgressReporter.update` — method, line 127
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

## `ProgressReporter.finish_line` — method, line 141
- **called from:**
- `scripts/pr_blocker_audit.py:149`

## `ProgressReporter.summary` — method, line 147
- **called from:**
- `scripts/pr_blocker_audit.py:235`
- `static/js/emailLibrary.js:7511`

## `load_json_file` — function, line 154
- **called from:**
- `scripts/pr_blocker_audit.py:1029`

## `fetch_live_prs` — function, line 164
- **called from:**
- `scripts/pr_blocker_audit.py:1032`
- `tests/test_pr_blocker_audit.py:105`
- `tests/test_pr_blocker_audit.py:122`
- `tests/test_pr_blocker_audit.py:139`
- `tests/test_pr_blocker_audit.py:155`
- `tests/test_pr_blocker_audit.py:182`
- `tests/test_pr_blocker_audit.py:201`

## `_limit_payload` — function, line 184
- **called from:**
- `scripts/pr_blocker_audit.py:178`

## `_fill_missing_live_files` — function, line 195
- **called from:**
- `scripts/pr_blocker_audit.py:181`

## `_fetch_live_pr_files` — function, line 246
- **called from:**
- `scripts/pr_blocker_audit.py:221`

## `_run_gh_json` — function, line 252
- **called from:**
- `scripts/pr_blocker_audit.py:174`
- `scripts/pr_blocker_audit.py:177`
- `scripts/pr_blocker_audit.py:248`

## `normalize_prs` — function, line 262
- **called from:**
- `scripts/pr_blocker_audit.py:1033`
- `tests/test_pr_blocker_audit.py:24`
- `tests/test_pr_blocker_audit.py:48`
- `tests/test_pr_blocker_audit.py:69`
- `tests/test_pr_blocker_audit.py:84`
- `tests/test_pr_blocker_audit.py:106`
- `tests/test_pr_blocker_audit.py:123`
- `tests/test_pr_blocker_audit.py:470`
- `tests/test_pr_blocker_audit.py:483`
- `tests/test_pr_blocker_audit.py:498`
- `tests/test_pr_blocker_audit.py:526`
- `tests/test_pr_blocker_audit.py:551`
- `tests/test_pr_blocker_audit.py:561`
- `tests/test_pr_blocker_audit.py:581`
- `tests/test_pr_blocker_audit.py:597`
- `tests/test_pr_blocker_audit.py:613`
- `tests/test_pr_blocker_audit.py:639`
- `tests/test_pr_blocker_audit.py:650`
- `tests/test_pr_blocker_audit.py:670`
- `tests/test_pr_blocker_audit.py:688`
- `tests/test_pr_blocker_audit.py:933`

## `missing_file_metadata_count` — function, line 271
- **called from:**
- `scripts/pr_blocker_audit.py:659`
- `scripts/pr_blocker_audit.py:724`
- `scripts/pr_blocker_audit.py:757`
- `scripts/pr_blocker_audit.py:1034`

## `missing_metadata_warning` — function, line 275
- **called from:**
- `scripts/pr_blocker_audit.py:1036`

## `normalize_pr` — function, line 280
- **called from:**
- `scripts/pr_blocker_audit.py:268`

## `_extract_files` — function, line 297
- **called from:**
- `scripts/pr_blocker_audit.py:209`
- `scripts/pr_blocker_audit.py:249`
- `scripts/pr_blocker_audit.py:281`

## `_extract_author` — function, line 311
- **called from:**
- `scripts/pr_blocker_audit.py:287`

## `_safe_int` — function, line 318
- **called from:**
- `scripts/pr_blocker_audit.py:208`
- `scripts/pr_blocker_audit.py:285`

## `classify_areas` — function, line 325
- **called from:**
- `scripts/pr_blocker_audit.py:283`
- `tests/test_pr_blocker_audit.py:394`
- `tests/test_pr_blocker_audit.py:403`
- `tests/test_pr_blocker_audit.py:412`
- `tests/test_pr_blocker_audit.py:420`
- `tests/test_pr_blocker_audit.py:428`
- `tests/test_pr_blocker_audit.py:436`
- `tests/test_pr_blocker_audit.py:448`
- `tests/test_pr_blocker_audit.py:459`

## `is_docs_tooling_only` — function, line 343
- **called from:**
- `scripts/pr_blocker_audit.py:332`

## `is_docs_tooling_path` — function, line 348
- **called from:**
- `scripts/pr_blocker_audit.py:345`

## `title_strongly_indicates_docs_tooling` — function, line 361
- **called from:**
- `scripts/pr_blocker_audit.py:332`

## `title_has_keyword` — function, line 377
- **called from:**
- `scripts/pr_blocker_audit.py:338`

## `hot_files` — function, line 384
- **called from:**
- `scripts/pr_blocker_audit.py:655`
- `scripts/pr_blocker_audit.py:720`
- `scripts/pr_blocker_audit.py:753`
- `tests/test_pr_blocker_audit.py:478`

## `overlap_clusters` — function, line 393
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `score_prs` — function, line 425
- **called from:**
- `scripts/pr_blocker_audit.py:654`
- `scripts/pr_blocker_audit.py:719`
- `scripts/pr_blocker_audit.py:752`
- `tests/test_pr_blocker_audit.py:518`
- `tests/test_pr_blocker_audit.py:543`
- `tests/test_pr_blocker_audit.py:641`

## `score_pr` — function, line 432
- **called from:**
- `scripts/pr_blocker_audit.py:428`
- `tests/test_pr_blocker_audit.py:572`
- `tests/test_pr_blocker_audit.py:573`

## `direct_auth_token_signal` — function, line 498
- **called from:**
- `scripts/pr_blocker_audit.py:441`

## `days_since` — function, line 513
- **called from:**
- `scripts/pr_blocker_audit.py:487`

## `reference_time` — function, line 520
- **called from:**
- `scripts/pr_blocker_audit.py:426`

## `parse_datetime` — function, line 527
- **called from:**
- `scripts/pr_blocker_audit.py:514`
- `scripts/pr_blocker_audit.py:521`

## `duplicate_candidates` — function, line 539
- **called from:**
- `scripts/pr_blocker_audit.py:657`
- `scripts/pr_blocker_audit.py:722`
- `scripts/pr_blocker_audit.py:755`
- `tests/test_pr_blocker_audit.py:491`

## `_looks_similar` — function, line 550
- **called from:**
- `scripts/pr_blocker_audit.py:544`

## `_groups_from_matches` — function, line 560
- **called from:**
- `scripts/pr_blocker_audit.py:547`

## `words` — function, line 579
- **called from:**
- `scripts/pr_blocker_audit.py:362`
- `scripts/pr_blocker_audit.py:381`
- `scripts/pr_blocker_audit.py:584`

## `title_keywords` — function, line 583
- **called from:**
- `scripts/pr_blocker_audit.py:556`
- `scripts/pr_blocker_audit.py:556`

## `locked_areas` — function, line 587
- **called from:**
- `scripts/pr_blocker_audit.py:656`
- `scripts/pr_blocker_audit.py:721`
- `scripts/pr_blocker_audit.py:754`
- `tests/test_pr_blocker_audit.py:641`

## `_locked_area_priority` — function, line 615
- **called from:**
- `scripts/pr_blocker_audit.py:598`

## `_locked_area_why` — function, line 621
- **called from:**
- `scripts/pr_blocker_audit.py:599`

## `_summarize_files` — function, line 627
- **called from:**
- `scripts/pr_blocker_audit.py:605`

## `_priority_rank` — function, line 634
- **called from:**
- `scripts/pr_blocker_audit.py:612`

## `safer_areas` — function, line 638
- **called from:**
- `scripts/pr_blocker_audit.py:709`
- `scripts/pr_blocker_audit.py:745`
- `scripts/pr_blocker_audit.py:795`

## `build_structured_report` — function, line 652
- **called from:**
- `scripts/pr_blocker_audit.py:714`

## `render_json` — function, line 713
- **called from:**
- `scripts/pr_blocker_audit.py:1040`
- `tests/test_pr_blocker_audit.py:934`
- `tests/test_pr_blocker_audit.py:935`

## `render_markdown` — function, line 717
- **called from:**
- `scripts/pr_blocker_audit.py:1042`
- `tests/test_pr_blocker_audit.py:583`
- `tests/test_pr_blocker_audit.py:604`
- `tests/test_pr_blocker_audit.py:691`

## `render_terminal` — function, line 750
- **called from:**
- `scripts/pr_blocker_audit.py:1038`
- `tests/test_pr_blocker_audit.py:605`
- `tests/test_pr_blocker_audit.py:617`
- `tests/test_pr_blocker_audit.py:657`
- `tests/test_pr_blocker_audit.py:658`
- `tests/test_pr_blocker_audit.py:678`
- `tests/test_pr_blocker_audit.py:690`

## `_terminal_hot_rows` — function, line 800
- **called from:**
- `scripts/pr_blocker_audit.py:778`

## `_terminal_duplicate_rows` — function, line 810
- **called from:**
- `scripts/pr_blocker_audit.py:793`

## `colorize` — function, line 821
- **called from:**
- `scripts/pr_blocker_audit.py:760`
- `scripts/pr_blocker_audit.py:766`
- `scripts/pr_blocker_audit.py:770`
- `scripts/pr_blocker_audit.py:773`
- `scripts/pr_blocker_audit.py:777`
- `scripts/pr_blocker_audit.py:779`
- `scripts/pr_blocker_audit.py:780`
- `scripts/pr_blocker_audit.py:784`
- `scripts/pr_blocker_audit.py:788`
- `scripts/pr_blocker_audit.py:792`
- `scripts/pr_blocker_audit.py:794`
- `scripts/pr_blocker_audit.py:806`

## `priority_color` — function, line 828
- **called from:**
- `scripts/pr_blocker_audit.py:770`

## `hot_count_color` — function, line 832
- **called from:**
- `scripts/pr_blocker_audit.py:806`

## `merge_state_color` — function, line 836
- **called from:**
- `scripts/pr_blocker_audit.py:784`

## `should_use_color` — function, line 845
- **called from:**
- `scripts/pr_blocker_audit.py:1038`
- `tests/test_pr_blocker_audit.py:730`
- `tests/test_pr_blocker_audit.py:733`
- `tests/test_pr_blocker_audit.py:744`
- `tests/test_pr_blocker_audit.py:745`

## `should_show_progress` — function, line 861
- **called from:**
- `scripts/pr_blocker_audit.py:1031`

## `enable_windows_vt_mode` — function, line 871
- **called from:**
- `scripts/pr_blocker_audit.py:850`
- `scripts/pr_blocker_audit.py:857`

## `_cluster_summary` — function, line 887
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_overlap_driver_summary` — function, line 896
- **called from:**
- `scripts/pr_blocker_audit.py:665`
- `scripts/pr_blocker_audit.py:731`
- `scripts/pr_blocker_audit.py:764`

## `_risk_summary` — function, line 902
- **called from:**
- `scripts/pr_blocker_audit.py:664`
- `scripts/pr_blocker_audit.py:732`

## `_target_summary` — function, line 908
- **called from:**
- `scripts/pr_blocker_audit.py:667`
- `scripts/pr_blocker_audit.py:733`
- `scripts/pr_blocker_audit.py:765`

## `_locked_rows` — function, line 917
- **called from:**
- `scripts/pr_blocker_audit.py:735`

## `_hot_rows` — function, line 932
- **called from:**
- `scripts/pr_blocker_audit.py:737`

## `_review_rows` — function, line 938
- **called from:**
- `scripts/pr_blocker_audit.py:741`

## `_duplicate_rows` — function, line 950
- **called from:**
- `scripts/pr_blocker_audit.py:743`

## `_table` — function, line 961
- **called from:**
- `scripts/pr_blocker_audit.py:735`
- `scripts/pr_blocker_audit.py:737`

## `_escape_cell` — function, line 970
- **called from:**
- `scripts/pr_blocker_audit.py:962`
- `scripts/pr_blocker_audit.py:966`

## `_format_pr_numbers` — function, line 974
- **called from:**
- `scripts/pr_blocker_audit.py:771`
- `scripts/pr_blocker_audit.py:806`
- `scripts/pr_blocker_audit.py:815`
- `scripts/pr_blocker_audit.py:892`
- `scripts/pr_blocker_audit.py:924`
- `scripts/pr_blocker_audit.py:935`
- `scripts/pr_blocker_audit.py:955`
- `tests/test_pr_blocker_audit.py:627`

## `shorten_text` — function, line 982
- **called from:**
- `scripts/pr_blocker_audit.py:786`
- `scripts/pr_blocker_audit.py:816`
- `scripts/pr_blocker_audit.py:913`
- `tests/test_pr_blocker_audit.py:692`

## `positive_int` — function, line 990
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `write_output` — function, line 1000
- **called from:**
- `scripts/pr_blocker_audit.py:1043`

## `build_parser` — function, line 1007
- **called from:**
- `scripts/pr_blocker_audit.py:1025`
- `tests/run_focus.py:299`
- `tests/run_order_report.py:137`
- `tests/test_pr_blocker_audit.py:239`
- `tests/test_pr_blocker_audit.py:960`

## `main` — function, line 1024
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
