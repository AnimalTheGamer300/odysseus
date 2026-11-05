# `scripts/ody_eval_email_fixture.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `FixtureEmailMcpManager` — class, line 16
- **called from:**
- `scripts/ody_eval_email_fixture.py:61`

## `FixtureEmailMcpManager.call_tool` — method (async), line 19
- **called from:**
- `mcp_servers/email_server.py:4038`
- `mcp_servers/image_gen_server.py:44`
- `mcp_servers/memory_server.py:143`
- `mcp_servers/rag_server.py:68`
- `src/mcp_manager.py:639`
- `src/task_scheduler.py:1628`
- `src/task_scheduler.py:2436`
- `src/tool_execution.py:1501`
- `src/tool_execution.py:2539`
- `src/tool_execution.py:2562`
- `tests/test_browser_lifecycle.py:332`
- `tests/test_email_search_folder_contract.py:24`
- `tests/test_generated_image_ownership.py:480`
- `tests/test_generated_image_ownership.py:488`
- `tests/test_image_quality_defaults.py:64`
- `tests/test_mcp_email_decode_header_spaces.py:99`
- `tests/test_mcp_email_decode_header_spaces.py:113`
- `tests/test_mcp_email_decode_header_spaces.py:127`
- `tests/test_mcp_email_decode_header_spaces.py:143`
- `tests/test_mcp_email_decode_header_spaces.py:156`
- `tests/test_mcp_email_decode_header_spaces.py:223`
- `tests/test_mcp_email_decode_header_spaces.py:241`
- `tests/test_mcp_email_decode_header_spaces.py:272`
- `tests/test_mcp_email_decode_header_spaces.py:327`
- `tests/test_mcp_email_search_dates.py:47`
- `tests/test_mcp_email_search_dates.py:77`
- `tests/test_mcp_email_search_dates.py:107`
- `tests/test_mcp_email_search_dates.py:129`
- `tests/test_mcp_email_search_dates.py:145`
- `tests/test_mcp_email_search_dates.py:158`
- `tests/test_mcp_email_search_dates.py:182`
- `tests/test_mcp_email_search_dates.py:210`
- `tests/test_mcp_email_search_error_transport.py:10`
- `tests/test_mcp_memory_owner_scope.py:22`
- `tests/test_memory_store_unreadable_no_wipe.py:218`
- `tests/test_memory_tool_contract.py:33`
- `tests/test_memory_tool_contract.py:42`
- `tests/test_rag_server_directory_nonstring.py:18`
- `tests/test_remote_resource_identity.py:177`
- `tests/test_remote_resource_identity.py:180`

## `email_fixture` — function, line 28
- decorator: `contextlib.contextmanager`
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:367`
- `scripts/eval_odysseus_everyday_live_hard.py:553`
- `scripts/eval_odysseus_live_hard_examples.py:420`
