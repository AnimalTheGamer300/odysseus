# `src/ai_interaction.py` — definitions & call sites

37 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `set_session_manager` — function, line 46
- **called from:**
- `src/app_initializer.py:93`

## `get_session_manager` — function, line 54
- **called from:**
- `routes/model_routes.py:3025`
- `src/agent_jobs.py:282`
- `src/agent_tools/session_tools.py:29`
- `src/agent_tools/session_tools.py:96`
- `src/agent_tools/session_tools.py:184`
- `src/agent_tools/session_tools.py:277`
- `src/bg_monitor.py:135`

## `set_memory_manager` — function, line 59
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `set_rag_manager` — function, line 65
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_resolve_model` — function, line 79
- **called from:**
- `services/skills/model_selection.py:41`
- `services/skills/model_selection.py:70`
- `src/ai_interaction.py:1352`
- `src/ai_interaction.py:1356`
- `src/ai_interaction.py:1360`
- `src/ai_interaction.py:1596`
- `src/ai_interaction.py:1600`
- `src/ai_interaction.py:1604`
- `src/ai_interaction.py:1948`
- `src/ai_interaction.py:1952`
- `src/document_processor.py:427`
- `src/document_processor.py:438`
- `src/editor_agent_model.py:277`
- `src/editor_agent_model.py:323`
- `tests/test_editor_agent_model_resolution.py:17`
- `tests/test_editor_agent_model_resolution.py:24`
- `tests/test_editor_agent_model_resolution.py:25`
- `tests/test_editor_agent_model_resolution.py:31`
- `tests/test_editor_agent_model_resolution.py:38`

## `_json_list` — function, line 103
- **called from:**
- `src/ai_interaction.py:185`
- `src/ai_interaction.py:187`
- `tests/cli/test_mcp_cli_json.py:9`
- `tests/cli/test_mcp_cli_json.py:10`
- `tests/cli/test_mcp_cli_json.py:11`

## `_image_like` — function, line 112
- **called from:**
- `src/ai_interaction.py:206`

## `stream_ai_tool` — function (async), line 220
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `do_pipeline` — function (async), line 227
- **called from:**
- `src/ai_interaction.py:2178`
- `tests/test_resolve_model_offloaded.py:37`
- `tests/test_resolve_model_offloaded.py:38`
- `tests/test_resolve_model_offloaded.py:57`

## `_manage_memory_lines` — function, line 347
- **called from:**
- `src/agent_runtime/owned_resources.py:386`
- `src/ai_interaction.py:407`
- `tests/test_manage_memory_json_contract.py:8`

## `do_manage_memory` — function (async), line 385
- **called from:**
- `src/ai_interaction.py:2183`
- `tests/test_manage_memory_blank_id.py:23`
- `tests/test_manage_memory_blank_id.py:49`
- `tests/test_memory_store_unreadable_no_wipe.py:200`

## `do_manage_rag` — function (async), line 610
- **called from:**
- `tests/test_rag_remove_directory_scope.py:156`

## `do_ui_control` — function (async), line 701
- **called from:**
- `src/ai_interaction.py:2188`
- `tests/test_ui_control_rag_toggle.py:26`
- `tests/test_ui_control_rag_toggle.py:43`
- `tests/test_ui_control_rag_toggle.py:51`
- `tests/test_ui_control_rag_toggle.py:58`
- `tests/test_ui_control_rag_toggle.py:63`
- `tests/test_ui_control_rag_toggle.py:68`
- `tests/test_ui_control_rag_toggle.py:75`
- `tests/test_ui_control_rag_toggle.py:84`
- `tests/test_ui_control_rag_toggle.py:92`
- `tests/test_ui_control_rag_toggle.py:103`
- `tests/test_ui_control_rag_toggle.py:104`
- `tests/test_ui_control_rag_toggle.py:123`
- `tests/test_ui_control_rag_toggle.py:132`
- `tests/test_ui_control_rag_toggle.py:136`
- `tests/test_ui_control_rag_toggle.py:140`
- `tests/test_ui_control_rag_toggle.py:146`
- `tests/test_ui_control_rag_toggle.py:154`

## `image_editing_provider_available` — function, line 1175
- **called from:**
- `routes/editor_agent_routes.py:727`
- `src/agent_tools/editor_tools.py:49`
- `tests/test_editor_generation_model_routing.py:318`
- `tests/test_editor_generation_model_routing.py:373`
- `tests/test_photo_editor_family.py:324`

## `_uses_openrouter_chat_images` — function, line 1208
- **called from:**
- `routes/gallery/gallery_routes.py:1927`
- `routes/gallery/gallery_routes.py:1960`
- `src/ai_interaction.py:1389`
- `src/ai_interaction.py:1800`
- `src/ai_interaction.py:1862`

## `_chat_image_results` — function, line 1214
- **called from:**
- `routes/gallery/gallery_routes.py:1961`
- `src/ai_interaction.py:1460`
- `src/ai_interaction.py:1861`

## `_image_response_error` — function, line 1229
- **called from:**
- `routes/gallery/gallery_routes.py:1957`
- `src/ai_interaction.py:1457`
- `src/ai_interaction.py:1858`

## `do_generate_image` — function (async), line 1241
- **called from:**
- `routes/chat_routes.py:4441`
- `routes/gallery/gallery_routes.py:2666`
- `src/agent_tools/editor_tools.py:664`
- `src/tool_execution.py:2286`
- `tests/test_ai_image_url_safety.py:71`
- `tests/test_ai_image_url_safety.py:98`
- `tests/test_editor_generation_model_routing.py:321`
- `tests/test_editor_generation_model_routing.py:376`
- `tests/test_image_provider_transport.py:22`
- `tests/test_image_provider_transport.py:32`
- `tests/test_image_provider_transport.py:45`
- `tests/test_image_provider_transport.py:61`
- `tests/test_image_provider_transport.py:127`
- `tests/test_image_provider_transport.py:201`
- `tests/test_image_provider_transport.py:217`
- `tests/test_image_provider_transport.py:228`
- `tests/test_image_provider_transport.py:242`
- `tests/test_image_quality_defaults.py:57`
- `tests/test_image_quality_defaults.py:62`

## `get_user_setting` — function, line 1283
- **called from:**
- `src/ai_interaction.py:1186`
- `src/ai_interaction.py:1290`
- `src/ai_interaction.py:1295`
- `src/ai_interaction.py:1297`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1588`
- `src/editor_agent_model.py:679`
- `src/editor_image_settings.py:10`
- `src/editor_image_settings.py:11`
- `src/endpoint_resolver.py:467`
- `src/endpoint_resolver.py:714`
- `src/utility_effort.py:36`
- `src/utility_effort.py:46`
- `tests/test_editor_generation_model_routing.py:315`
- `tests/test_editor_generation_model_routing.py:370`
- `tests/test_editor_generation_model_routing.py:424`
- `tests/test_editor_generation_model_routing.py:500`

## `_resolve_image_model` — function (async), line 1345
- **called from:**
- `src/ai_interaction.py:1366`

## `_call` — function, line 1346
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_email_list_stale_while_revalidate.py:47`
- `tests/test_email_list_stale_while_revalidate.py:81`
- `tests/test_email_list_stale_while_revalidate.py:127`
- `tests/test_email_list_stale_while_revalidate.py:140`
- `tests/test_email_list_stale_while_revalidate.py:141`
- `tests/test_email_list_stale_while_revalidate.py:196`
- `tests/test_email_list_stale_while_revalidate.py:242`
- `tests/test_email_list_stale_while_revalidate.py:244`
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
- `tests/test_manage_settings_denylist_hard.py:46`
- `tests/test_manage_settings_denylist_hard.py:54`
- `tests/test_manage_settings_denylist_hard.py:62`
- `tests/test_manage_settings_denylist_hard.py:68`
- `tests/test_manage_settings_denylist_hard.py:77`
- `tests/test_manage_settings_denylist_hard.py:91`
- `tests/test_manage_settings_denylist_hard.py:101`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_to_gallery` — function, line 1471
- **called from:**
- `src/ai_interaction.py:1505`

## `_store_image` — function, line 1494
- **called from:**
- `src/ai_interaction.py:1509`
- `src/ai_interaction.py:1523`

## `do_edit_image` — function (async), line 1551
- **called from:**
- `routes/chat_routes.py:4431`
- `src/tool_execution.py:2468`
- `tests/test_edit_image_tool.py:82`
- `tests/test_edit_image_tool.py:107`
- `tests/test_edit_image_tool.py:117`
- `tests/test_edit_image_tool.py:140`
- `tests/test_edit_image_tool.py:144`
- `tests/test_edit_image_tool.py:169`
- `tests/test_edit_image_tool.py:172`
- `tests/test_edit_image_tool.py:175`
- `tests/test_edit_image_tool.py:187`
- `tests/test_image_provider_transport.py:41`
- `tests/test_image_provider_transport.py:122`
- `tests/test_image_provider_transport.py:165`
- `tests/test_image_provider_transport.py:190`
- `tests/test_image_provider_transport.py:215`
- `tests/test_image_provider_transport.py:240`
- `tests/test_image_provider_transport.py:254`
- `tests/test_image_quality_defaults.py:69`

## `get_user_setting` — function, line 1582
- **called from:**
- `src/ai_interaction.py:1186`
- `src/ai_interaction.py:1290`
- `src/ai_interaction.py:1295`
- `src/ai_interaction.py:1297`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1586`
- `src/ai_interaction.py:1588`
- `src/editor_agent_model.py:679`
- `src/editor_image_settings.py:10`
- `src/editor_image_settings.py:11`
- `src/endpoint_resolver.py:467`
- `src/endpoint_resolver.py:714`
- `src/utility_effort.py:36`
- `src/utility_effort.py:46`
- `tests/test_editor_generation_model_routing.py:315`
- `tests/test_editor_generation_model_routing.py:370`
- `tests/test_editor_generation_model_routing.py:424`
- `tests/test_editor_generation_model_routing.py:500`

## `_call` — function, line 1594
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_email_list_stale_while_revalidate.py:47`
- `tests/test_email_list_stale_while_revalidate.py:81`
- `tests/test_email_list_stale_while_revalidate.py:127`
- `tests/test_email_list_stale_while_revalidate.py:140`
- `tests/test_email_list_stale_while_revalidate.py:141`
- `tests/test_email_list_stale_while_revalidate.py:196`
- `tests/test_email_list_stale_while_revalidate.py:242`
- `tests/test_email_list_stale_while_revalidate.py:244`
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
- `tests/test_manage_settings_denylist_hard.py:46`
- `tests/test_manage_settings_denylist_hard.py:54`
- `tests/test_manage_settings_denylist_hard.py:62`
- `tests/test_manage_settings_denylist_hard.py:68`
- `tests/test_manage_settings_denylist_hard.py:77`
- `tests/test_manage_settings_denylist_hard.py:91`
- `tests/test_manage_settings_denylist_hard.py:101`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_edited_image_to_gallery` — function, line 1643
- **called from:**
- `src/ai_interaction.py:1681`
- `src/ai_interaction.py:2002`

## `_save_image_bytes` — function, line 1665
- **called from:**
- `src/ai_interaction.py:1727`
- `src/ai_interaction.py:1872`
- `src/ai_interaction.py:1884`
- `src/ai_interaction.py:2045`
- `src/ai_interaction.py:2136`
- `src/ai_interaction.py:2148`

## `_try_local_img2img_fallback` — function (async), line 1683
- **called from:**
- `src/ai_interaction.py:1841`
- `src/ai_interaction.py:2113`

## `_poll_progress` — function (async), line 1750
- **called from:**
- `src/ai_interaction.py:1769`
- `src/ai_interaction.py:2087`

## `do_edit_image` — function (async), line 1906
- **called from:**
- `routes/chat_routes.py:4431`
- `src/tool_execution.py:2468`
- `tests/test_edit_image_tool.py:82`
- `tests/test_edit_image_tool.py:107`
- `tests/test_edit_image_tool.py:117`
- `tests/test_edit_image_tool.py:140`
- `tests/test_edit_image_tool.py:144`
- `tests/test_edit_image_tool.py:169`
- `tests/test_edit_image_tool.py:172`
- `tests/test_edit_image_tool.py:175`
- `tests/test_edit_image_tool.py:187`
- `tests/test_image_provider_transport.py:41`
- `tests/test_image_provider_transport.py:122`
- `tests/test_image_provider_transport.py:165`
- `tests/test_image_provider_transport.py:190`
- `tests/test_image_provider_transport.py:215`
- `tests/test_image_provider_transport.py:240`
- `tests/test_image_provider_transport.py:254`
- `tests/test_image_quality_defaults.py:69`

## `_call` — function, line 1946
- **called from:**
- `tests/test_contacts_import_nonstring.py:26`
- `tests/test_contacts_import_nonstring.py:32`
- `tests/test_contacts_import_nonstring.py:37`
- `tests/test_email_list_stale_while_revalidate.py:47`
- `tests/test_email_list_stale_while_revalidate.py:81`
- `tests/test_email_list_stale_while_revalidate.py:127`
- `tests/test_email_list_stale_while_revalidate.py:140`
- `tests/test_email_list_stale_while_revalidate.py:141`
- `tests/test_email_list_stale_while_revalidate.py:196`
- `tests/test_email_list_stale_while_revalidate.py:242`
- `tests/test_email_list_stale_while_revalidate.py:244`
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
- `tests/test_manage_settings_denylist_hard.py:46`
- `tests/test_manage_settings_denylist_hard.py:54`
- `tests/test_manage_settings_denylist_hard.py:62`
- `tests/test_manage_settings_denylist_hard.py:68`
- `tests/test_manage_settings_denylist_hard.py:77`
- `tests/test_manage_settings_denylist_hard.py:91`
- `tests/test_manage_settings_denylist_hard.py:101`
- `tests/test_rag_server_directory_nonstring.py:22`
- `tests/test_rag_server_directory_nonstring.py:27`

## `_save_edited_image_to_gallery` — function, line 1975
- **called from:**
- `src/ai_interaction.py:1681`
- `src/ai_interaction.py:2002`

## `_save_image_bytes` — function, line 1997
- **called from:**
- `src/ai_interaction.py:1727`
- `src/ai_interaction.py:1872`
- `src/ai_interaction.py:1884`
- `src/ai_interaction.py:2045`
- `src/ai_interaction.py:2136`
- `src/ai_interaction.py:2148`

## `_try_local_img2img_fallback` — function (async), line 2004
- **called from:**
- `src/ai_interaction.py:1841`
- `src/ai_interaction.py:2113`

## `_poll_progress` — function (async), line 2068
- **called from:**
- `src/ai_interaction.py:1769`
- `src/ai_interaction.py:2087`

## `dispatch_ai_tool` — function (async), line 2171
- **called from:**
- `src/ai_interaction.py:223`
- `src/tool_execution.py:2397`
- `tests/test_ai_interaction_owner_scope.py:60`
