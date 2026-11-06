# `src/report_math.py` — definitions & call sites

12 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_placeholder` — function, line 20
- **called from:**
- `src/report_math.py:57`
- `src/report_math.py:78`

## `_HtmlContext` — class, line 28
- **called from:**
- `src/report_math.py:47`

## `_HtmlContext.__init__` — method, line 30
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

## `_HtmlContext.handle_starttag` — method, line 34
- **called from:**
- `src/agent_tools/document_tools.py:768`

## `_HtmlContext.handle_endtag` — method, line 38
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_InlineMath` — class, line 43
- **called from:**
- `src/report_math.py:84`
- `src/report_math.py:86`

## `_InlineMath.handleMatch` — method, line 44
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_DisplayMath` — class, line 60
- **called from:**
- `src/report_math.py:87`

## `_DisplayMath.test` — method, line 61
- **called from:**
- `tests/test_endpoint_registered_authority.py:342`
- `tests/test_endpoint_registered_authority.py:362`
- `tests/test_endpoint_registered_authority.py:387`
- `tests/test_endpoint_registered_authority.py:404`
- `tests/test_endpoint_registered_authority.py:414`
- `static/app.js:375`
- `static/app.js:3026`
- `static/app.js:3242`
- `static/js/a11y.js:74`
- `static/js/actionMenuOrder.js:21`
- `static/js/admin.js:468`
- `static/js/admin.js:469`
- `static/js/admin.js:470`
- `static/js/admin.js:474`
- `static/js/admin.js:1861`
- `static/js/admin.js:1902`
- `static/js/admin.js:2015`
- `static/js/admin.js:2029`
- `static/js/backgroundToolJobs.js:34`
- `static/js/calendar.js:92`
- `static/js/calendar.js:92`
- `static/js/calendar.js:3102`
- `static/js/calendar.js:3714`
- `static/js/calendar.js:4094`
- `static/js/calendar.js:4105`
- `static/js/calendar.js:4176`
- `static/js/calendar.js:4182`
- `static/js/calendar.js:4349`
- `static/js/calendar.js:4483`
- `static/js/calendar/utils.js:170`
- `static/js/censor.js:205`
- `static/js/censor.js:215`
- `static/js/censor.js:227`
- `static/js/censor.js:242`
- `static/js/censor.js:260`
- `static/js/chat.js:134`
- `static/js/chat.js:165`
- `static/js/chat.js:214`
- `static/js/chat.js:228`
- `static/js/chat.js:297`
- `static/js/chat.js:1273`
- `static/js/chat.js:1273`
- `static/js/chat.js:1433`
- `static/js/chat.js:1433`
- `static/js/chat.js:2235`
- `static/js/chat.js:2237`
- `static/js/chat.js:2237`
- `static/js/chat.js:2849`
- `static/js/chat.js:3048`
- `static/js/chat.js:3331`
- `static/js/chat.js:3332`
- `static/js/chat.js:3333`
- `static/js/chat.js:3333`
- `static/js/chat.js:3338`
- `static/js/chat.js:3915`
- `static/js/chat.js:3932`
- `static/js/chat.js:4410`
- `static/js/chat.js:4413`
- `static/js/chat.js:4414`
- `static/js/chat.js:4415`
- … +815 more (grep the name in repo)

## `_DisplayMath.run` — method, line 64
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

## `ReportMathExtension` — class, line 81
- **called from:**
- `src/visual_report.py:84`

## `ReportMathExtension.extendMarkdown` — method, line 82
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
