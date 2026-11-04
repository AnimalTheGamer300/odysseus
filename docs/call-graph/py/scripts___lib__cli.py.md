# `scripts/_lib/cli.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `quiet_logs` — function, line 48
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `emit` — function, line 61
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fail` — function, line 75
- **called from:**
- `scripts/_lib/cli.py:121`
- `tests/test_agent_bash_windows.py:24`
- `tests/test_agent_bash_windows.py:46`
- `tests/test_agent_bash_windows.py:83`
- `tests/test_agent_bash_windows.py:120`
- `tests/test_cookbook_docker_access.py:101`
- `tests/test_foreground_model_routing.py:1083`
- `tests/test_foreground_model_routing.py:1176`
- `tests/test_foreground_model_routing.py:1641`
- `tests/test_foreground_model_routing.py:1834`
- `tests/test_foreground_model_routing.py:1983`
- `tests/test_foreground_model_routing.py:1988`
- `tests/test_foreground_model_routing.py:2012`
- `tests/test_foreground_model_routing.py:2058`
- `tests/test_foreground_model_routing.py:2090`
- `tests/test_foreground_model_routing.py:2206`
- `tests/test_llm_core_fallback.py:1375`
- `tests/test_personal_upload_privilege.py:68`
- `tests/test_task_scheduler_cache.py:29`
- `tests/test_task_scheduler_cache.py:66`
- `tests/test_task_scheduler_cache.py:84`
- `tests/test_tts_service_enforce_cache_limit.py:94`
- `static/js/cookbookSchedule.js:203`
- `static/js/cookbookSchedule.js:208`
- `static/js/cookbookSchedule.js:211`
- `static/js/cookbookSchedule.js:284`
- `static/js/cookbookSchedule.js:371`

## `common_parser` — function, line 84
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `run` — function, line 99
- **called from:**
- `app.py:1312`
- `core/platform_compat.py:124`
- `core/platform_compat.py:406`
- `core/platform_compat.py:447`
- `launcher.py:114`
- `launcher.py:149`
- `mcp_servers/email_server.py:2906`
- `mcp_servers/email_server.py:2912`
- `mcp_servers/email_server.py:2912`
- `mcp_servers/image_gen_server.py:180`
- `mcp_servers/image_gen_server.py:184`
- `mcp_servers/image_gen_server.py:184`
- `mcp_servers/memory_server.py:281`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/memory_server.py:285`
- `mcp_servers/rag_server.py:156`
- `mcp_servers/rag_server.py:160`
- `mcp_servers/rag_server.py:160`
- `routes/cookbook_routes.py:1627`
- `routes/cookbook_routes.py:3720`
- `routes/cookbook_routes.py:3733`
- `routes/cookbook_routes.py:3744`
- `routes/cookbook_routes.py:3805`
- `routes/cookbook_routes.py:4271`
- `routes/cookbook_routes.py:4273`
- `routes/cookbook_routes.py:4294`
- `routes/cookbook_routes.py:4296`
- `routes/cookbook_routes.py:4457`
- `routes/cookbook_routes.py:4467`
- `routes/hwfit_routes.py:128`
- `scripts/diffusion_server.py:1506`
- `scripts/dump_agent_prompt.py:415`
- `scripts/mlx_image_server.py:207`
- `scripts/mlx_image_server.py:281`
- `scripts/mlx_image_server.py:379`
- `scripts/mlx_image_server.py:466`
- `scripts/pr_blocker_audit.py:253`
- `services/hwfit/hardware.py:45`
- `src/builtin_mcp.py:293`
- `src/document_processor.py:548`
- `src/document_processor.py:616`
- `src/endpoint_resolver.py:184`
- `src/event_bus.py:43`
- `src/model_discovery.py:49`
- `tests/run_focus.py:321`
- `tests/run_order_report.py:152`
- `tests/test_admin_tools_registry.py:44`
- `tests/test_admin_tools_registry.py:56`
- `tests/test_agent_round_model_provenance_ui.py:35`
- `tests/test_agent_rounds_exhausted.py:18`
- `tests/test_agent_state_dir_confinement.py:126`
- `tests/test_agent_state_dir_confinement.py:129`
- `tests/test_agent_state_dir_confinement.py:132`
- `tests/test_agent_state_dir_confinement.py:450`
- `tests/test_agent_state_dir_confinement.py:453`
- `tests/test_agent_state_dir_confinement.py:474`
- `tests/test_agent_state_dir_confinement.py:477`
- `tests/test_agent_state_dir_confinement.py:609`
- `tests/test_agent_state_dir_confinement.py:629`
- `tests/test_agent_state_dir_confinement.py:689`
- … +546 more (grep the name in repo)
