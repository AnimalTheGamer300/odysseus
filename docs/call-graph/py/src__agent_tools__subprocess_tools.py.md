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
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)

## `PythonTool` — class, line 359
- **called from:**
- `src/agent_tools/__init__.py:40`

## `PythonTool.execute` — method (async), line 360
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:502`
- `core/database.py:895`
- `core/database.py:898`
- `core/database.py:901`
- `core/database.py:913`
- `core/database.py:936`
- `core/database.py:939`
- `core/database.py:960`
- `core/database.py:963`
- `core/database.py:964`
- `core/database.py:984`
- `core/database.py:987`
- `core/database.py:1007`
- `core/database.py:1010`
- `core/database.py:1037`
- `core/database.py:1040`
- `core/database.py:1041`
- `core/database.py:1062`
- `core/database.py:1065`
- `core/database.py:1066`
- `core/database.py:1087`
- `core/database.py:1090`
- `core/database.py:1110`
- `core/database.py:1113`
- `core/database.py:1115`
- `core/database.py:1117`
- `core/database.py:1119`
- `core/database.py:1138`
- `core/database.py:1141`
- `core/database.py:1161`
- `core/database.py:1164`
- `core/database.py:1185`
- `core/database.py:1188`
- `core/database.py:1207`
- `core/database.py:1210`
- `core/database.py:1230`
- `core/database.py:1233`
- `core/database.py:1235`
- `core/database.py:1237`
- `core/database.py:1239`
- `core/database.py:1241`
- `core/database.py:1243`
- `core/database.py:1262`
- `core/database.py:1265`
- `core/database.py:1285`
- `core/database.py:1288`
- `core/database.py:1308`
- `core/database.py:1311`
- `core/database.py:1312`
- `core/database.py:1332`
- `core/database.py:1335`
- `core/database.py:1336`
- `core/database.py:1368`
- `core/database.py:1370`
- `core/database.py:1396`
- `core/database.py:1398`
- … +332 more (grep the name in repo)
