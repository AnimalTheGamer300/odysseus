# `src/agent_tools/spawn_agent_tools.py` — definitions & call sites

8 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_parse_args` — function, line 61
- **called from:**
- `src/agent_tools/spawn_agent_tools.py:268`
- `src/agent_tools/web_tools.py:1950`
- `src/agent_tools/web_tools_prewave3.py:1954`
- `src/agent_tools/web_tools_prewave3.py:2825`
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
- `tests/test_spawn_agent.py:182`
- `tests/test_spawn_agent.py:200`

## `SpawnAgentTool.execute` — method (async), line 267
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

## `CheckAgentsTool` — class, line 307
- **called from:**
- `tests/test_spawn_agent.py:212`
- `tests/test_spawn_agent.py:215`

## `CheckAgentsTool.execute` — method (async), line 310
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
