# `src/tool_utils.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_mcp_manager` — function, line 20
- **called from:**
- `app.py:919`
- `scripts/ody_eval_email_fixture.py:61`
- `scripts/ody_eval_email_fixture.py:65`
- `tests/test_local_mcp_capabilities.py:72`
- `tests/test_local_mcp_capabilities.py:76`
- `tests/test_local_mcp_capabilities.py:600`
- `tests/test_local_mcp_capabilities.py:667`
- `tests/test_local_mcp_capabilities.py:695`
- `tests/test_local_mcp_capabilities.py:723`
- `tests/test_local_mcp_capabilities.py:873`
- `tests/test_local_mcp_capabilities.py:925`
- `tests/test_local_mcp_capabilities.py:996`
- `tests/test_product_turn_contract_route.py:31`
- `tests/test_product_turn_contract_route.py:36`
- `tests/test_product_turn_contract_route.py:63`

## `get_mcp_manager` — function, line 25
- **called from:**
- `routes/chat_routes.py:3842`
- `routes/task/task_routes.py:1075`
- `scripts/dump_agent_prompt.py:391`
- `scripts/ody_eval_email_fixture.py:36`
- `src/agent_loop.py:21466`
- `src/agent_loop.py:21880`
- `src/agent_runtime/authority.py:390`
- `src/agent_runtime/authority.py:506`
- `src/agent_runtime/remote_resources.py:134`
- `src/agent_tools/admin_tools.py:242`
- `src/agent_tools/admin_tools.py:289`
- `src/agent_tools/admin_tools.py:313`
- `src/agent_tools/admin_tools.py:327`
- `src/agent_tools/admin_tools.py:371`
- `src/task_scheduler.py:1602`
- `src/task_scheduler.py:2388`
- `src/tool_capabilities.py:382`
- `src/tool_capabilities.py:389`
- `src/tool_execution.py:1276`
- `src/tool_execution.py:1488`
- `src/tool_execution.py:2497`
- `src/tool_execution.py:2544`
- `tests/test_local_mcp_capabilities.py:228`
- `tests/test_local_mcp_capabilities.py:410`
- `tests/test_local_mcp_capabilities.py:436`
- `tests/test_local_mcp_capabilities.py:512`
- `tests/test_local_mcp_capabilities.py:748`
- `tests/test_local_mcp_capabilities.py:774`
- `tests/test_product_turn_contract_route.py:21`
- `tests/test_product_turn_contract_route.py:33`

## `set_upload_handler` — function, line 34
- **called from:**
- `src/app_initializer.py:96`

## `get_upload_handler` — function, line 40
- **called from:**
- `src/agent_runtime/owned_resources.py:86`
- `src/agent_runtime/resources.py:114`
- `src/agent_tools/document_tools.py:49`
- `src/agent_tools/media_tools.py:453`
- `src/clean_agent_preview.py:4050`
- `src/tools/calendar.py:602`
- `src/tools/calendar.py:701`
- `src/tools/image.py:120`
- `src/tools/notes.py:378`
- `src/tools/notes.py:450`

## `_truncate` — function, line 47
- **called from:**
- `src/agent_loop.py:22618`
- `src/agent_loop.py:26272`
- `src/agent_loop.py:26394`
- `src/agent_loop.py:27274`
- `src/agent_loop.py:27295`
- `src/agent_loop.py:27474`
- `src/agent_loop.py:27493`
- `src/agent_loop.py:27597`
- `src/agent_loop.py:27615`
- `src/agent_loop.py:27906`
- `src/agent_loop.py:27977`
- `src/agent_loop.py:34665`
- `src/agent_loop.py:34868`
- `src/agent_loop.py:34872`
- `src/agent_loop.py:34876`
- `src/agent_loop.py:35990`
- `src/agent_loop.py:36006`
- `src/agent_loop.py:38394`
- `src/agent_loop.py:38421`
- `src/agent_tools/filesystem_tools.py:838`
- `src/agent_tools/filesystem_tools.py:945`
- `src/agent_tools/filesystem_tools.py:1351`
- `src/agent_tools/subprocess_tools.py:589`
- `src/agent_tools/subprocess_tools.py:590`
- `src/agent_tools/subprocess_tools.py:593`
- `src/agent_tools/subprocess_tools.py:594`
- `src/agent_tools/subprocess_tools.py:598`
- `src/agent_tools/subprocess_tools.py:599`
- `src/agent_tools/subprocess_tools.py:603`
- `src/agent_tools/subprocess_tools.py:804`
- `src/agent_tools/subprocess_tools.py:829`
- `src/tool_execution.py:2656`
- `src/tool_execution.py:2735`
- `src/tool_utils.py:97`
- `tests/test_agent_loop_tool_output_truncation.py:16`
- `tests/test_agent_loop_tool_output_truncation.py:22`
- `tests/test_agent_loop_tool_output_truncation.py:32`
- `tests/test_agent_loop_tool_output_truncation.py:39`
- `tests/test_agent_loop_tool_output_truncation.py:44`
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
- `src/agent_loop.py:34878`
- `src/agent_loop.py:34880`
- `src/agent_loop.py:34894`

## `_parse_tool_args` — function, line 106
- **called from:**
- `scripts/eval_odysseus_app_route_smoke.py:138`
- `scripts/eval_odysseus_everyday_live_hard.py:287`
- `scripts/eval_odysseus_live_hard_examples.py:303`
- `src/agent_runtime/owned_resources.py:22`
- `src/agent_tools/admin_tools.py:26`
- `src/agent_tools/admin_tools.py:235`
- `src/agent_tools/admin_tools.py:391`
- `src/agent_tools/admin_tools.py:463`
- `src/agent_tools/admin_tools.py:515`
- `src/agent_tools/document_tools.py:1089`
- `src/tools/calendar.py:113`
- `src/tools/contacts.py:19`
- `src/tools/contacts.py:87`
- `src/tools/cookbook.py:739`
- `src/tools/cookbook.py:809`
- `src/tools/cookbook.py:1317`
- `src/tools/cookbook.py:1344`
- `src/tools/cookbook.py:1497`
- `src/tools/cookbook.py:1519`
- `src/tools/cookbook.py:1620`
- `src/tools/cookbook.py:1847`
- `src/tools/cookbook.py:1952`
- `src/tools/image.py:29`
- `src/tools/image.py:103`
- `src/tools/notes.py:40`
- `src/tools/research.py:25`
- `src/tools/research.py:117`
- `src/tools/system.py:45`
- `src/tools/system.py:355`
- `src/tools/system.py:836`
- `src/tools/vault.py:50`
- `src/tools/vault.py:99`
- `src/tools/vault.py:157`
- `tests/test_admin_tools_registry.py:72`
- `tests/test_admin_tools_registry.py:74`
- `tests/test_admin_tools_registry.py:77`
- `tests/test_admin_tools_registry.py:78`
- `tests/test_admin_tools_registry.py:79`
