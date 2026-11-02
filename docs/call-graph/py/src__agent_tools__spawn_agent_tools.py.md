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
