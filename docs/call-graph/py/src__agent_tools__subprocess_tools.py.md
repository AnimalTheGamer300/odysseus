# `src/agent_tools/subprocess_tools.py` — definitions & call sites

30 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_ffmpeg_unicode_drawtext_needs_fontfile` — function, line 35
- **called from:**
- `src/agent_tools/subprocess_tools.py:641`

## `_resolve_fontfile_for_text` — function, line 53
- **called from:**
- `src/agent_tools/subprocess_tools.py:642`

## `_cancel_host_shell_bridge_request` — function (async), line 76
- **called from:**
- `src/agent_tools/subprocess_tools.py:791`
- `tests/test_tool_execution_bridge_security.py:126`
- `tests/test_tool_execution_bridge_security.py:157`
- `tests/test_tool_execution_bridge_security.py:222`
- `tests/test_tool_execution_bridge_security.py:314`

## `find_bash` — function, line 94
- **called from:**
- `core/platform_compat.py:281`
- `core/platform_compat.py:311`
- `routes/cookbook_routes.py:880`
- `routes/shell_routes.py:649`
- `routes/shell_routes.py:1109`
- `src/agent_tools/subprocess_tools.py:112`
- `src/builtin_actions.py:911`
- `src/builtin_actions.py:927`
- `src/builtin_actions.py:928`
- `src/builtin_actions.py:937`
- `src/builtin_actions.py:938`
- `src/containment.py:928`
- `tests/test_cookbook_dependency_completion_regression.py:644`
- `tests/test_cookbook_helpers.py:808`
- `tests/test_platform_compat.py:34`
- `tests/test_platform_compat.py:48`
- `tests/test_platform_compat.py:62`
- `tests/test_platform_compat.py:78`

## `_create_bash_subprocess` — function (async), line 104
- **called from:**
- `tests/test_agent_bash_windows.py:35`
- `tests/test_agent_bash_windows.py:61`
- `tests/test_agent_bash_windows.py:84`
- `tests/test_agent_bash_windows.py:127`
- `tests/test_agent_bash_windows.py:201`

## `_host_shell_requires_detach` — function, line 131
- **called from:**
- `src/agent_tools/subprocess_tools.py:158`
- `src/agent_tools/subprocess_tools.py:721`
- `src/tool_execution.py:405`
- `tests/test_host_shell_polling.py:45`
- `tests/test_host_shell_polling.py:49`
- `tests/test_host_shell_polling.py:50`
- `tests/test_host_shell_polling.py:54`

## `_host_shell_should_auto_poll` — function, line 155
- **called from:**
- `src/agent_tools/subprocess_tools.py:748`
- `src/tool_execution.py:398`
- `tests/test_host_shell_polling.py:58`
- `tests/test_host_shell_polling.py:59`

## `_docker_default_gateway_ips` — function, line 166
- **called from:**
- `src/agent_tools/subprocess_tools.py:210`

## `_is_private_bridge_ip` — function, line 184
- **called from:**
- `src/agent_tools/subprocess_tools.py:211`

## `is_host_shell_bridge_url_allowed` — function, line 203
- **called from:**
- `routes/chat_routes.py:806`
- `src/agent_loop.py:9496`
- `src/agent_loop.py:9542`
- `src/agent_tools/subprocess_tools.py:79`
- `src/agent_tools/subprocess_tools.py:689`
- `src/tool_execution.py:162`
- `src/tool_execution.py:235`
- `src/tool_execution.py:305`
- `src/tool_execution.py:333`
- `tests/test_client_tool_routing.py:1215`
- `tests/test_client_tool_routing.py:1216`
- `tests/test_client_tool_routing.py:1217`
- `tests/test_client_tool_routing.py:1218`
- `tests/test_client_tool_routing.py:1219`
- `tests/test_client_tool_routing.py:1222`
- `tests/test_client_tool_routing.py:1224`
- `tests/test_client_tool_routing.py:1225`
- `tests/test_client_tool_routing.py:1226`
- `tests/test_client_tool_routing.py:1227`
- `tests/test_client_tool_routing.py:1228`
- `tests/test_client_tool_routing.py:1229`
- `tests/test_review_regressions.py:704`
- `tests/test_review_regressions.py:707`

## `host_shell_bridge_endpoint_url` — function, line 221
- **called from:**
- `src/agent_tools/subprocess_tools.py:81`
- `src/agent_tools/subprocess_tools.py:693`
- `src/tool_execution.py:141`

## `_replace_workspace_alias` — function, line 227
- **called from:**
- `src/agent_tools/subprocess_tools.py:438`
- `src/agent_tools/subprocess_tools.py:544`
- `src/agent_tools/subprocess_tools.py:546`
- `src/bg_jobs.py:115`
- `tests/test_agent_bash_tmux_env.py:9`

## `_namespace_visible_without_bind` — function, line 251
- **called from:**
- `src/agent_tools/subprocess_tools.py:267`
- `src/agent_tools/subprocess_tools.py:470`

## `_namespace_dir_chain` — function, line 259
- **called from:**
- `tests/test_execution_filesystem_boundary.py:119`
- `tests/test_execution_filesystem_boundary.py:120`
- `tests/test_execution_filesystem_boundary.py:121`
- `tests/test_execution_filesystem_boundary.py:124`

## `_isolated_tmp_dir` — function, line 280
- **called from:**
- `src/agent_tools/subprocess_tools.py:661`
- `src/agent_tools/subprocess_tools.py:938`
- `tests/test_execution_filesystem_boundary.py:292`
- `tests/test_execution_filesystem_boundary.py:307`

## `_execution_boundary` — function, line 298
- **called from:**
- `src/agent_tools/subprocess_tools.py:405`

## `_filesystem_boundary_block` — function, line 357
- **called from:**
- `src/agent_tools/subprocess_tools.py:415`
- `src/agent_tools/subprocess_tools.py:439`

## `_contained_command` — function, line 381
- **called from:**
- `tests/test_execution_filesystem_boundary.py:165`
- `tests/test_execution_filesystem_boundary.py:185`
- `tests/test_execution_filesystem_boundary.py:198`
- `tests/test_execution_filesystem_boundary.py:219`
- `tests/test_execution_filesystem_boundary.py:235`

## `_wrap_workspace_namespace` — function, line 446
- **called from:**
- `src/agent_tools/subprocess_tools.py:406`
- `tests/test_agent_bash_tmux_env.py:20`
- `tests/test_execution_filesystem_boundary.py:62`
- `tests/test_workspace_artifact_tool_floor.py:2261`
- `tests/test_workspace_artifact_tool_floor.py:2288`
- `tests/test_workspace_artifact_tool_floor.py:2291`
- `tests/test_workspace_artifact_tool_floor.py:2312`

## `_owned_spec` — function, line 503
- **called from:**
- `src/agent_runtime/process_resources.py:61`
- `src/agent_tools/subprocess_tools.py:534`
- `src/agent_tools/subprocess_tools.py:710`
- `src/bg_jobs.py:110`
- `tests/test_containment_enforcement.py:92`
- `tests/test_containment_enforcement.py:294`
- `tests/test_containment_enforcement.py:324`

## `_run_owned_command` — function (async), line 519
- **called from:**
- `src/agent_tools/subprocess_tools.py:663`
- `src/agent_tools/subprocess_tools.py:948`
- `src/builtin_actions.py:898`

## `BashTool` — class, line 607
- **called from:**
- `src/agent_tools/__init__.py:40`
- `tests/test_agent_bash_tmux_env.py:39`
- `tests/test_agent_bash_tmux_env.py:64`
- `tests/test_agent_bash_tmux_env.py:84`
- `tests/test_agent_bash_tmux_env.py:108`
- `tests/test_agent_bash_windows.py:102`
- `tests/test_agent_bash_windows.py:139`
- `tests/test_agent_bash_windows.py:168`
- `tests/test_agent_tmux_retirement.py:22`
- `tests/test_containment_enforcement.py:242`
- `tests/test_containment_enforcement.py:264`
- `tests/test_native_execution_containment.py:35`
- `tests/test_native_execution_containment.py:53`
- `tests/test_native_execution_containment.py:62`
- `tests/test_native_execution_containment.py:171`
- `tests/test_native_execution_containment.py:183`
- `tests/test_native_execution_containment.py:193`
- `tests/test_native_execution_containment.py:196`
- `tests/test_preview_execution_evidence.py:17`
- `tests/test_production_external_bridge.py:188`
- `tests/test_runtime_resource_integration.py:57`
- `tests/test_runtime_resource_integration.py:64`
- `tests/test_runtime_resource_integration.py:76`
- `tests/test_wave3_launch_cost_lifecycle.py:66`
- `tests/test_wave3_launch_cost_lifecycle.py:69`
- `tests/test_workspace_artifact_tool_floor.py:2338`
- `tests/test_workspace_artifact_tool_floor.py:2343`

## `BashTool.execute` — method (async), line 608
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `HostShellTool` — class, line 665
- **called from:**
- `src/agent_tools/__init__.py:41`
- `tests/test_host_shell_polling.py:94`
- `tests/test_host_shell_polling.py:142`
- `tests/test_host_shell_polling.py:186`
- `tests/test_production_external_bridge.py:54`
- `tests/test_production_external_bridge.py:92`
- `tests/test_tool_execution_bridge_security.py:153`
- `tests/test_tool_execution_bridge_security.py:250`
- `tests/test_tool_execution_bridge_security.py:316`

## `HostShellTool.execute` — method (async), line 666
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)

## `_python_child_runtime_failure` — function, line 839
- **called from:**
- `src/agent_tools/subprocess_tools.py:596`

## `_python_with_visible_final_expression` — function, line 855
- **called from:**
- `src/agent_tools/subprocess_tools.py:942`

## `_python_with_configured_import_paths` — function, line 900
- **called from:**
- `src/agent_tools/subprocess_tools.py:941`
- `tests/test_python_tool_import_paths.py:6`
- `tests/test_python_tool_import_paths.py:10`

## `PythonTool` — class, line 909
- **called from:**
- `src/agent_tools/__init__.py:42`
- `tests/test_containment_enforcement.py:106`
- `tests/test_containment_enforcement.py:201`
- `tests/test_containment_enforcement.py:283`
- `tests/test_containment_enforcement.py:355`
- `tests/test_native_execution_containment.py:132`
- `tests/test_native_execution_containment.py:144`
- `tests/test_native_execution_containment.py:152`
- `tests/test_workspace_artifact_tool_floor.py:2152`
- `tests/test_workspace_artifact_tool_floor.py:2157`
- `tests/test_workspace_artifact_tool_floor.py:2162`
- `tests/test_workspace_artifact_tool_floor.py:2173`
- `tests/test_workspace_artifact_tool_floor.py:2186`
- `tests/test_workspace_artifact_tool_floor.py:2198`
- `tests/test_workspace_artifact_tool_floor.py:2201`
- `tests/test_workspace_artifact_tool_floor.py:2243`

## `PythonTool.execute` — method (async), line 910
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:539`
- `core/database.py:954`
- `core/database.py:957`
- `core/database.py:960`
- `core/database.py:972`
- `core/database.py:995`
- `core/database.py:997`
- `core/database.py:1017`
- `core/database.py:1019`
- `core/database.py:1039`
- `core/database.py:1041`
- `core/database.py:1060`
- `core/database.py:1068`
- `core/database.py:1085`
- `core/database.py:1088`
- `core/database.py:1109`
- `core/database.py:1112`
- `core/database.py:1113`
- `core/database.py:1133`
- `core/database.py:1136`
- `core/database.py:1156`
- `core/database.py:1159`
- `core/database.py:1186`
- `core/database.py:1189`
- `core/database.py:1190`
- `core/database.py:1211`
- `core/database.py:1214`
- `core/database.py:1215`
- `core/database.py:1236`
- `core/database.py:1239`
- `core/database.py:1259`
- `core/database.py:1262`
- `core/database.py:1264`
- `core/database.py:1266`
- `core/database.py:1268`
- `core/database.py:1287`
- `core/database.py:1290`
- `core/database.py:1310`
- `core/database.py:1313`
- `core/database.py:1334`
- `core/database.py:1337`
- `core/database.py:1358`
- `core/database.py:1361`
- `core/database.py:1380`
- `core/database.py:1383`
- `core/database.py:1406`
- `core/database.py:1423`
- `core/database.py:1426`
- `core/database.py:1428`
- `core/database.py:1430`
- `core/database.py:1432`
- `core/database.py:1434`
- `core/database.py:1436`
- `core/database.py:1455`
- `core/database.py:1458`
- `core/database.py:1478`
- … +725 more (grep the name in repo)
