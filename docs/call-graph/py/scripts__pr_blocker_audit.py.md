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

## `ProgressReporter.phase` — method, line 122
- **called from:**
- `scripts/pr_blocker_audit.py:172`
- `scripts/pr_blocker_audit.py:203`
- `static/js/markdown.js:334`

## `ProgressReporter.update` — method, line 127
- **called from:**
- `app.py:487`
- `app.py:1336`
- `app.py:1356`
- `core/database.py:3084`
- `core/session_manager.py:989`
- `routes/auth_routes.py:474`
- `routes/auth_routes.py:487`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:919`
- `routes/chat_helpers.py:1062`
- `routes/chat_helpers.py:1079`
- `routes/chat_helpers.py:1096`
- `routes/chat_routes.py:1442`
- `routes/chat_routes.py:1493`
- `routes/chat_routes.py:3580`
- `routes/chat_routes.py:3639`
- `routes/chat_routes.py:3651`
- `routes/chat_routes.py:3669`
- `routes/chat_routes.py:3685`
- `routes/chat_routes.py:3687`
- `routes/chat_routes.py:3690`
- `routes/chat_routes.py:3692`
- `routes/chat_routes.py:3694`
- `routes/chat_routes.py:3697`
- `routes/chat_routes.py:3705`
- `routes/chat_routes.py:3713`
- `routes/chat_routes.py:3717`
- `routes/chat_routes.py:3721`
- `routes/chat_routes.py:3732`
- `routes/chat_routes.py:3735`
- `routes/chat_routes.py:3742`
- `routes/chat_routes.py:3826`
- `routes/chat_routes.py:3835`
- `routes/chat_routes.py:3839`
- `routes/chat_routes.py:4025`
- `routes/chat_routes.py:4439`
- `routes/chat_routes.py:4680`
- `routes/chat_routes.py:4699`
- `routes/chat_routes.py:5001`
- `routes/chat_routes.py:5005`
- `routes/cookbook_routes.py:3264`
- `routes/cookbook_routes.py:3268`
- `routes/cookbook_routes.py:3271`
- `routes/cookbook_routes.py:3386`
- `routes/cookbook_routes.py:4121`
- `routes/device_flow.py:156`
- `routes/email/email_pollers.py:969`
- `routes/email/email_routes.py:187`
- `routes/email/email_routes.py:1307`
- `routes/email/email_routes.py:2526`
- `routes/email/email_routes.py:2872`
- `routes/email/email_routes.py:4906`
- `routes/email/email_routes.py:4976`
- `routes/email/email_routes.py:5502`
- `routes/email/email_routes.py:5503`
- `routes/email/email_routes.py:5506`
- `routes/email/email_routes.py:5511`
- `routes/email/email_routes.py:6640`
- … +548 more (grep the name in repo)

## `ProgressReporter.finish_line` — method, line 141
- **called from:**
- `scripts/pr_blocker_audit.py:149`

## `ProgressReporter.summary` — method, line 147
- **called from:**
- `scripts/pr_blocker_audit.py:235`
- `tests/test_agent_trace.py:47`
- `tests/test_agent_trace.py:150`
- `tests/test_agent_trace.py:158`
- `tests/test_agent_trace.py:180`
- `static/js/emailLibrary/reader.js:643`

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
- `src/agent_loop.py:19019`
- `src/agent_loop.py:19020`
- `static/js/editor/look-recipes.js:30`

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
- `scripts/ref_parity_audit.py:577`
- `tests/test_pr_blocker_audit.py:934`
- `tests/test_pr_blocker_audit.py:935`

## `render_markdown` — function, line 717
- **called from:**
- `scripts/pr_blocker_audit.py:1042`
- `scripts/ref_parity_audit.py:577`
- `tests/test_pr_blocker_audit.py:583`
- `tests/test_pr_blocker_audit.py:604`
- `tests/test_pr_blocker_audit.py:691`
- `tests/test_ref_parity_audit.py:298`

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
- `scripts/generate_env_reference.py:1156`
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
- `scripts/eval_odysseus_contextual_tool_use.py:935`
- `scripts/eval_odysseus_contextual_tool_use.py:938`
- `scripts/pr_blocker_audit.py:1043`

## `build_parser` — function, line 1007
- **called from:**
- `scripts/pr_blocker_audit.py:1025`
- `scripts/ref_parity_audit.py:556`
- `tests/run_focus.py:299`
- `tests/run_order_report.py:137`
- `tests/test_pr_blocker_audit.py:239`
- `tests/test_pr_blocker_audit.py:960`
- `tests/test_ref_parity_audit.py:351`

## `main` — function, line 1024
- **called from:**
- `integrations/claude/skills/odysseus/scripts/odysseus_api.py:218`
- `integrations/codex/scripts/odysseus_api.py:218`
- `scripts/add_hwfit_models.py:512`
- `scripts/agent_migration_manifest.py:635`
- `scripts/analyze_odysseus_eval_targets.py:180`
- `scripts/assemble_sft_clean_corpus.py:74`
- `scripts/audit_c5_benchmark_evidence.py:1637`
- `scripts/audit_email_sft_with_deepseek.py:323`
- `scripts/audit_historical_tool_routing.py:121`
- `scripts/audit_sft_corpus_with_deepseek.py:344`
- `scripts/audit_typo_tool_routing.py:99`
- `scripts/backfill_model_release_dates.py:136`
- `scripts/build_frontend.py:148`
- `scripts/build_historical_harness_queue.py:333`
- `scripts/build_odysseus_everyday_deepseek_heldout_cases.py:274`
- `scripts/build_odysseus_everyday_deepseek_heldout_v3_cases.py:353`
- `scripts/build_odysseus_realistic_web_synthesis_rows.py:361`
- `scripts/build_odysseus_search_teacher_edited_rows.py:267`
- `scripts/build_odysseus_sft_repair_manifest.py:230`
- `scripts/build_odysseus_tool_efficiency_sft_slice.py:447`
- `scripts/build_odysseus_v54_live_gap_teacher_sft.py:557`
- `scripts/build_odysseus_v55_web_synthesis_teacher_sft.py:519`
- `scripts/build_odysseus_v56_broad_web_teacher_sft.py:551`
- `scripts/build_odysseus_v61_app_route_web_rows.py:394`
- `scripts/build_odysseus_v62_teacher_trace_web_rows.py:288`
- `scripts/build_odysseus_web_teacher_sft.py:500`
- `scripts/build_odysseus_web_v53_repair_sft.py:483`
- `scripts/build_sft_environment_inventories.py:97`
- `scripts/build_sft_expansion_manifest.py:161`
- `scripts/build_sft_expansion_splits.py:110`
- `scripts/build_v66_calendar_heldout_cases.py:113`
- `scripts/check_brotli.py:122`
- `scripts/check_ca_trust.py:180`
- `scripts/claim_ownerless.py:106`
- `scripts/cook_sft_alex_conversations.py:298`
- `scripts/css_snapshot.py:295`
- `scripts/curate_public_search_seed_cases.py:324`
- `scripts/curate_sft_trace_run.py:178`
- `scripts/demo_email/seed_demo_emails.py:394`
- `scripts/dump_agent_prompt.py:545`
- `scripts/eval_ajax_basic_tools.py:71`
- `scripts/eval_exact_file_routing.py:202`
- `scripts/eval_followup_domain_continuity.py:209`
- `scripts/eval_odysseus_app_route_smoke.py:400`
- `scripts/eval_odysseus_contextual_tool_use.py:944`
- `scripts/eval_odysseus_crud.py:925`
- `scripts/eval_odysseus_everyday_live_hard.py:590`
- `scripts/eval_odysseus_live_hard_direct.py:261`
- `scripts/eval_odysseus_live_hard_examples.py:468`
- `scripts/eval_odysseus_tool_use.py:1490`
- `scripts/eval_qwen35_document_shape_direct.py:303`
- `scripts/eval_qwen35_implicit_memory.py:279`
- `scripts/eval_qwen35_tool_router_extended.py:571`
- `scripts/filter_sft_seed_hygiene.py:90`
- `scripts/generate_env_reference.py:1270`
- `scripts/generate_sft_environment_expansion.py:399`
- `scripts/generate_sft_flow_variants_with_kimi.py:211`
- `scripts/hf_download.py:182`
- `scripts/import_from_vllm_recipes.py:348`
- `scripts/index_documents.py:117`
- … +139 more (grep the name in repo)
