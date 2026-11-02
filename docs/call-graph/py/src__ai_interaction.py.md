# `src/ai_interaction.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_session_manager` — function, line 45
- **called from:**
- `src/app_initializer.py:93`

## `get_session_manager` — function, line 53
- **called from:**
- `routes/model_routes.py:2643`
- `src/agent_jobs.py:282`
- `src/agent_tools/session_tools.py:29`
- `src/agent_tools/session_tools.py:82`
- `src/agent_tools/session_tools.py:169`
- `src/agent_tools/session_tools.py:256`
- `src/bg_monitor.py:99`

## `set_memory_manager` — function, line 58
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_rag_manager` — function, line 64
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_resolve_model` — function, line 78
- **called from:**
- `routes/skills_routes.py:1132`
- `src/ai_interaction.py:1026`
- `src/ai_interaction.py:1030`
- `src/ai_interaction.py:1230`
- `src/ai_interaction.py:1234`
- `src/ai_interaction.py:1500`
- `src/ai_interaction.py:1504`
- `src/document_processor.py:321`
- `src/document_processor.py:332`

## `_json_list` — function, line 102
- **called from:**
- `src/ai_interaction.py:182`
- `src/ai_interaction.py:182`
- `tests/cli/test_mcp_cli_json.py:9`
- `tests/cli/test_mcp_cli_json.py:10`
- `tests/cli/test_mcp_cli_json.py:11`

## `_image_like` — function, line 111
- **called from:**
- `src/ai_interaction.py:200`

## `stream_ai_tool` — function (async), line 214
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_pipeline` — function (async), line 221
- **called from:**
- `src/ai_interaction.py:1730`
- `tests/test_resolve_model_offloaded.py:37`
- `tests/test_resolve_model_offloaded.py:38`
- `tests/test_resolve_model_offloaded.py:57`

## `do_manage_memory` — function (async), line 341
- **called from:**
- `src/ai_interaction.py:1735`
- `tests/test_memory_store_unreadable_no_wipe.py:200`

## `do_manage_rag` — function (async), line 525
- **called from:**
- `tests/test_rag_remove_directory_scope.py:156`

## `do_ui_control` — function (async), line 616
- **called from:**
- `src/ai_interaction.py:1740`
- `tests/test_ui_control_rag_toggle.py:15`
- `tests/test_ui_control_rag_toggle.py:23`
- `tests/test_ui_control_rag_toggle.py:30`
- `tests/test_ui_control_rag_toggle.py:35`

## `do_generate_image` — function (async), line 940
- **called from:**
- `routes/chat_routes.py:2146`
- `tests/test_ai_image_url_safety.py:71`
- `tests/test_ai_image_url_safety.py:98`

## `_resolve_image_model` — function (async), line 1023
- **called from:**
- `src/ai_interaction.py:1036`

## `_call` — function, line 1024
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_integration_api_call_ssrf.py:62`
- `tests/test_integration_api_call_ssrf.py:75`
- `tests/test_integration_api_call_ssrf.py:85`
- `tests/test_integration_api_call_ssrf.py:95`
- `tests/test_integration_api_call_ssrf.py:101`
- `tests/test_integrations_api_call_truncation.py:159`
- `tests/test_integrations_api_call_truncation.py:180`
- `tests/test_integrations_api_call_truncation.py:200`
- `tests/test_integrations_api_call_truncation.py:226`
- `tests/test_integrations_api_call_truncation.py:243`
- `tests/test_llm_core_async_mistral_content.py:45`
- `tests/test_llm_core_async_mistral_content.py:60`
- `tests/test_llm_core_async_mistral_content.py:70`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_to_gallery` — function, line 1109
- **called from:**
- `src/ai_interaction.py:1140`
- `src/ai_interaction.py:1160`

## `do_edit_image` — function (async), line 1188
- **called from:**
- `routes/chat_routes.py:2136`
- `src/tool_execution.py:1284`

## `_call` — function, line 1228
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_integration_api_call_ssrf.py:62`
- `tests/test_integration_api_call_ssrf.py:75`
- `tests/test_integration_api_call_ssrf.py:85`
- `tests/test_integration_api_call_ssrf.py:95`
- `tests/test_integration_api_call_ssrf.py:101`
- `tests/test_integrations_api_call_truncation.py:159`
- `tests/test_integrations_api_call_truncation.py:180`
- `tests/test_integrations_api_call_truncation.py:200`
- `tests/test_integrations_api_call_truncation.py:226`
- `tests/test_integrations_api_call_truncation.py:243`
- `tests/test_llm_core_async_mistral_content.py:45`
- `tests/test_llm_core_async_mistral_content.py:60`
- `tests/test_llm_core_async_mistral_content.py:70`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_edited_image_to_gallery` — function, line 1257
- **called from:**
- `src/ai_interaction.py:1284`
- `src/ai_interaction.py:1554`

## `_save_image_bytes` — function, line 1279
- **called from:**
- `src/ai_interaction.py:1330`
- `src/ai_interaction.py:1424`
- `src/ai_interaction.py:1436`
- `src/ai_interaction.py:1597`
- `src/ai_interaction.py:1688`
- `src/ai_interaction.py:1700`

## `_try_local_img2img_fallback` — function (async), line 1286
- **called from:**
- `src/ai_interaction.py:1398`
- `src/ai_interaction.py:1665`

## `_poll_progress` — function (async), line 1353
- **called from:**
- `src/ai_interaction.py:1372`
- `src/ai_interaction.py:1639`

## `do_edit_image` — function (async), line 1458
- **called from:**
- `routes/chat_routes.py:2136`
- `src/tool_execution.py:1284`

## `_call` — function, line 1498
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_integration_api_call_ssrf.py:62`
- `tests/test_integration_api_call_ssrf.py:75`
- `tests/test_integration_api_call_ssrf.py:85`
- `tests/test_integration_api_call_ssrf.py:95`
- `tests/test_integration_api_call_ssrf.py:101`
- `tests/test_integrations_api_call_truncation.py:159`
- `tests/test_integrations_api_call_truncation.py:180`
- `tests/test_integrations_api_call_truncation.py:200`
- `tests/test_integrations_api_call_truncation.py:226`
- `tests/test_integrations_api_call_truncation.py:243`
- `tests/test_llm_core_async_mistral_content.py:45`
- `tests/test_llm_core_async_mistral_content.py:60`
- `tests/test_llm_core_async_mistral_content.py:70`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_edited_image_to_gallery` — function, line 1527
- **called from:**
- `src/ai_interaction.py:1284`
- `src/ai_interaction.py:1554`

## `_save_image_bytes` — function, line 1549
- **called from:**
- `src/ai_interaction.py:1330`
- `src/ai_interaction.py:1424`
- `src/ai_interaction.py:1436`
- `src/ai_interaction.py:1597`
- `src/ai_interaction.py:1688`
- `src/ai_interaction.py:1700`

## `_try_local_img2img_fallback` — function (async), line 1556
- **called from:**
- `src/ai_interaction.py:1398`
- `src/ai_interaction.py:1665`

## `_poll_progress` — function (async), line 1620
- **called from:**
- `src/ai_interaction.py:1372`
- `src/ai_interaction.py:1639`

## `dispatch_ai_tool` — function (async), line 1723
- **called from:**
- `src/ai_interaction.py:217`
- `src/tool_execution.py:1215`
- `tests/test_ai_interaction_owner_scope.py:60`
