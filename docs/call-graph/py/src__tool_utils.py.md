# `src/tool_utils.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_mcp_manager` — function, line 20
- **called from:**
- `app.py:835`

## `get_mcp_manager` — function, line 25
- **called from:**
- `routes/task/task_routes.py:1003`
- `scripts/dump_agent_prompt.py:391`
- `src/agent_loop.py:4042`
- `src/agent_tools/admin_tools.py:228`
- `src/agent_tools/admin_tools.py:275`
- `src/agent_tools/admin_tools.py:299`
- `src/agent_tools/admin_tools.py:313`
- `src/agent_tools/admin_tools.py:357`
- `src/task_scheduler.py:1448`
- `src/task_scheduler.py:2193`
- `src/tool_execution.py:529`
- `src/tool_execution.py:706`
- `src/tool_execution.py:1313`
- `src/tool_execution.py:1356`

## `set_upload_handler` — function, line 34
- **called from:**
- `src/app_initializer.py:96`

## `get_upload_handler` — function, line 40
- **called from:**
- `src/agent_tools/document_tools.py:14`
- `src/tools/calendar.py:419`
- `src/tools/calendar.py:488`
- `src/tools/notes.py:204`
- `src/tools/notes.py:253`

## `_truncate` — function, line 47
- **called from:**
- `src/agent_tools/filesystem_tools.py:570`
- `src/agent_tools/filesystem_tools.py:677`
- `src/agent_tools/filesystem_tools.py:1026`
- `src/agent_tools/subprocess_tools.py:321`
- `src/agent_tools/subprocess_tools.py:322`
- `src/agent_tools/subprocess_tools.py:330`
- `src/agent_tools/subprocess_tools.py:351`
- `src/agent_tools/subprocess_tools.py:351`
- `src/agent_tools/subprocess_tools.py:356`
- `src/agent_tools/subprocess_tools.py:377`
- `src/agent_tools/subprocess_tools.py:377`
- `src/agent_tools/subprocess_tools.py:382`
- `src/tool_utils.py:97`
- `tests/test_agent_loop_tool_output_truncation.py:15`
- `tests/test_agent_loop_tool_output_truncation.py:21`
- `tests/test_agent_loop_tool_output_truncation.py:31`
- `tests/test_agent_loop_tool_output_truncation.py:38`
- `tests/test_agent_loop_tool_output_truncation.py:43`
- `tests/test_agent_tools_truncate_nonstring.py:11`
- `tests/test_agent_tools_truncate_nonstring.py:12`
- `tests/test_agent_tools_truncate_nonstring.py:13`
- `tests/test_agent_tools_truncate_nonstring.py:17`
- `tests/test_agent_tools_truncate_nonstring.py:22`
- `tests/test_agent_tools_truncate_nonstring.py:23`
- `tests/test_mcp_common_truncate.py:10`
- `tests/test_mcp_common_truncate.py:11`
- `tests/test_mcp_common_truncate.py:15`
- `tests/test_mcp_common_truncate.py:16`

## `truncate_tool_output` — function, line 75
- **called from:**
- `src/agent_loop.py:5183`
- `src/agent_loop.py:5263`
- `src/agent_loop.py:6555`
- `src/agent_loop.py:6559`
- `src/agent_loop.py:6563`
- `src/agent_loop.py:6565`
- `src/agent_loop.py:6567`
- `src/agent_loop.py:6577`

## `_parse_tool_args` — function, line 106
- **called from:**
- `src/agent_tools/admin_tools.py:26`
- `src/agent_tools/admin_tools.py:221`
- `src/agent_tools/admin_tools.py:377`
- `src/agent_tools/admin_tools.py:449`
- `src/agent_tools/admin_tools.py:501`
- `src/agent_tools/document_tools.py:782`
- `src/tools/calendar.py:35`
- `src/tools/contacts.py:19`
- `src/tools/contacts.py:87`
- `src/tools/cookbook.py:610`
- `src/tools/cookbook.py:678`
- `src/tools/cookbook.py:993`
- `src/tools/cookbook.py:1020`
- `src/tools/cookbook.py:1173`
- `src/tools/cookbook.py:1192`
- `src/tools/cookbook.py:1249`
- `src/tools/cookbook.py:1459`
- `src/tools/cookbook.py:1547`
- `src/tools/image.py:24`
- `src/tools/image.py:169`
- `src/tools/notes.py:26`
- `src/tools/research.py:24`
- `src/tools/research.py:103`
- `src/tools/system.py:45`
- `src/tools/system.py:281`
- `src/tools/system.py:614`
- `src/tools/vault.py:50`
- `src/tools/vault.py:95`
- `src/tools/vault.py:153`
- `tests/test_admin_tools_registry.py:72`
- `tests/test_admin_tools_registry.py:74`
- `tests/test_admin_tools_registry.py:77`
- `tests/test_admin_tools_registry.py:78`
- `tests/test_admin_tools_registry.py:79`
