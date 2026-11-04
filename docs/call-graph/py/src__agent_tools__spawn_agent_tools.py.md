# `src/agent_tools/spawn_agent_tools.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_parse_args` — function, line 61
- **called from:**
- `src/agent_tools/spawn_agent_tools.py:268`
- `tests/test_spawn_agent.py:46`
- `tests/test_spawn_agent.py:50`
- `tests/test_spawn_agent.py:53`

## `_headers_for_endpoint` — function, line 78
- **called from:**
- `src/agent_tools/spawn_agent_tools.py:117`

## `_resolve_subagent_model` — function (async), line 99
- **called from:**
- `src/agent_jobs.py:150`
- `src/agent_tools/spawn_agent_tools.py:149`

## `run_subagent` — function (async), line 121
- **called from:**
- `src/agent_jobs.py:214`
- `src/agent_tools/spawn_agent_tools.py:292`
- `tests/test_spawn_agent.py:72`
- `tests/test_spawn_agent.py:87`
- `tests/test_spawn_agent.py:132`

## `SpawnAgentTool` — class, line 266
- **called from:**
- `src/agent_tools/__init__.py:62`
- `tests/test_spawn_agent.py:182`
- `tests/test_spawn_agent.py:200`

## `SpawnAgentTool.execute` — method (async), line 267
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

## `CheckAgentsTool` — class, line 307
- **called from:**
- `src/agent_tools/__init__.py:63`
- `tests/test_spawn_agent.py:212`
- `tests/test_spawn_agent.py:215`

## `CheckAgentsTool.execute` — method (async), line 310
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
