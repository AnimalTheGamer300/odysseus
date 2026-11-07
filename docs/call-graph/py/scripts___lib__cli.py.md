# `scripts/_lib/cli.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `quiet_logs` — function, line 48
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `emit` — function, line 61
- **called from:**
- `scripts/eval_exact_file_routing.py:170`
- `scripts/eval_exact_file_routing.py:184`
- `src/containment.py:992`
- `src/containment.py:998`
- `src/email_reply_stream.py:26`
- `src/email_reply_stream.py:42`
- `src/email_reply_stream.py:48`
- `static/js/editor/brush-engine.js:24`

## `fail` — function, line 75
- **called from:**
- `scripts/_lib/cli.py:121`
- `tests/conftest.py:297`
- `tests/test_agent_bash_windows.py:30`
- `tests/test_agent_bash_windows.py:121`
- `tests/test_agent_bash_windows.py:164`
- `tests/test_agent_bash_windows.py:196`
- `tests/test_agent_editor_routes.py:1074`
- `tests/test_agent_editor_routes.py:1216`
- `tests/test_agent_tmux_retirement.py:19`
- `tests/test_agent_tmux_retirement.py:107`
- `tests/test_background_containment.py:45`
- `tests/test_background_containment.py:94`
- `tests/test_background_containment.py:133`
- `tests/test_background_containment.py:160`
- `tests/test_background_resource_identity.py:73`
- `tests/test_background_resource_identity.py:93`
- `tests/test_background_resource_identity.py:117`
- `tests/test_background_resource_identity.py:212`
- `tests/test_background_resource_identity.py:231`
- `tests/test_background_resource_identity.py:255`
- `tests/test_browser_identity_transport.py:118`
- `tests/test_browser_lifecycle.py:178`
- `tests/test_browser_resource_identity.py:71`
- `tests/test_browser_resource_identity.py:126`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:177`
- `tests/test_chatgpt_zero_native_tools.py:196`
- `tests/test_containment_enforcement.py:57`
- `tests/test_containment_enforcement.py:80`
- `tests/test_containment_enforcement.py:182`
- `tests/test_containment_enforcement.py:186`
- `tests/test_cookbook_cache_scan_isolation.py:58`
- `tests/test_cookbook_docker_access.py:108`
- `tests/test_editor_layer_scoped_actions_browser.py:17`
- `tests/test_effect_resource_bindings.py:315`
- `tests/test_email_task_intent.py:139`
- `tests/test_foreground_model_routing.py:1137`
- `tests/test_foreground_model_routing.py:1230`
- `tests/test_foreground_model_routing.py:1695`
- `tests/test_foreground_model_routing.py:1918`
- `tests/test_foreground_model_routing.py:2067`
- `tests/test_foreground_model_routing.py:2072`
- `tests/test_foreground_model_routing.py:2096`
- `tests/test_foreground_model_routing.py:2142`
- `tests/test_foreground_model_routing.py:2174`
- `tests/test_foreground_model_routing.py:2290`
- `tests/test_image_creation_routing.py:139`
- `tests/test_llm_core_fallback.py:1631`
- `tests/test_native_execution_containment.py:51`
- `tests/test_native_execution_containment.py:142`
- `tests/test_orphan_reaping.py:121`
- `tests/test_orphan_reaping.py:156`
- `tests/test_orphan_reaping.py:187`
- `tests/test_orphan_reaping.py:198`
- `tests/test_orphan_reaping.py:215`
- `tests/test_orphan_reaping.py:254`
- `tests/test_orphan_reaping.py:321`
- `tests/test_orphan_reaping.py:351`
- `tests/test_pdf_cmyk_image_analysis.py:83`
- `tests/test_personal_upload_privilege.py:68`
- `tests/test_preview_drafting_recovery.py:77`
- … +51 more (grep the name in repo)

## `common_parser` — function, line 84
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run` — function, line 99
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
