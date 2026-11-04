# `src/agent_tools/subprocess_tools.py` — definitions & call sites

18 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_create_bash_subprocess` — function (async), line 20
- **called from:**
- `src/agent_tools/subprocess_tools.py:336`
- `tests/test_agent_bash_windows.py:29`
- `tests/test_agent_bash_windows.py:52`
- `tests/test_agent_bash_windows.py:125`

## `_tmux_session_name` — function, line 41
- **called from:**
- `src/agent_tools/subprocess_tools.py:142`
- `src/agent_tools/subprocess_tools.py:323`
- `src/agent_tools/subprocess_tools.py:332`

## `_run_exec` — function (async), line 46
- **called from:**
- `src/agent_tools/subprocess_tools.py:68`
- `src/agent_tools/subprocess_tools.py:73`
- `src/agent_tools/subprocess_tools.py:82`
- `src/agent_tools/subprocess_tools.py:83`
- `src/agent_tools/subprocess_tools.py:88`
- `src/agent_tools/subprocess_tools.py:90`
- `src/agent_tools/subprocess_tools.py:103`
- `src/agent_tools/subprocess_tools.py:179`

## `_tmux_has_session` — function (async), line 67
- **called from:**
- `src/agent_tools/subprocess_tools.py:87`
- `src/agent_tools/subprocess_tools.py:101`

## `_tmux_capture` — function (async), line 72
- **called from:**
- `src/agent_tools/subprocess_tools.py:160`

## `_tmux_send_line` — function (async), line 80
- **called from:**
- `src/agent_tools/subprocess_tools.py:155`

## `_ensure_tmux_session` — function (async), line 86
- **called from:**
- `src/agent_tools/subprocess_tools.py:143`

## `_output_after_marker` — function, line 106
- **called from:**
- `src/agent_tools/subprocess_tools.py:161`

## `_extract_marker_rc` — function, line 123
- **called from:**
- `src/agent_tools/subprocess_tools.py:174`

## `_run_tmux_bash` — function (async), line 133
- **called from:**
- `src/agent_tools/subprocess_tools.py:309`

## `_clean_tmux_command_output` — function, line 187
- **called from:**
- `src/agent_tools/subprocess_tools.py:175`
- `src/agent_tools/subprocess_tools.py:182`

## `_run_subprocess_streaming` — function (async), line 208
- **called from:**
- `src/agent_tools/subprocess_tools.py:345`
- `src/agent_tools/subprocess_tools.py:371`

## `_reader` — function (async), line 219
- **called from:**
- `routes/shell_routes.py:1061`
- `routes/shell_routes.py:1062`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `src/agent_tools/subprocess_tools.py:246`
- `src/agent_tools/subprocess_tools.py:247`

## `_progress_emitter` — function (async), line 233
- **called from:**
- `src/agent_tools/subprocess_tools.py:248`

## `BashTool` — class, line 297
- **called from:**
- `src/agent_tools/__init__.py:39`
- `tests/test_agent_bash_windows.py:60`
- `tests/test_agent_bash_windows.py:97`

## `BashTool.execute` — method (async), line 298
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `PythonTool` — class, line 359
- **called from:**
- `src/agent_tools/__init__.py:40`

## `PythonTool.execute` — method (async), line 360
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)
