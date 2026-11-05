# `src/agent_tools/bg_job_tools.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_age` — function, line 22
- **called from:**
- `src/agent_tools/bg_job_tools.py:62`
- `src/agent_tools/bg_job_tools.py:128`

## `_status_label` — function, line 34
- **called from:**
- `src/agent_tools/bg_job_tools.py:62`
- `src/agent_tools/bg_job_tools.py:117`
- `src/agent_tools/bg_job_tools.py:128`

## `job_lifecycle_facts` — function, line 47
- **called from:**
- `src/agent_tools/bg_job_tools.py:118`
- `src/agent_tools/bg_job_tools.py:124`
- `src/agent_tools/bg_job_tools.py:130`
- `src/bg_monitor.py:57`

## `_row` — function, line 60
- **called from:**
- `src/agent_runtime/owned_resources.py:237`
- `src/agent_runtime/owned_resources.py:311`
- `src/agent_runtime/owned_resources.py:341`
- `src/agent_runtime/owned_resources.py:370`
- `src/agent_tools/bg_job_tools.py:100`
- `src/fixture_email.py:133`
- `src/fixture_email.py:182`
- `tests/test_token_cache_atomic_swap.py:59`
- `tests/test_token_cache_atomic_swap.py:67`
- `tests/test_token_cache_atomic_swap.py:68`
- `tests/test_token_cache_atomic_swap.py:69`
- `tests/test_token_cache_atomic_swap.py:89`
- `tests/test_token_cache_atomic_swap.py:96`
- `tests/test_token_cache_atomic_swap.py:107`
- `tests/test_token_cache_atomic_swap.py:146`
- `tests/test_token_cache_atomic_swap.py:163`
- `tests/test_token_cache_atomic_swap.py:164`
- `tests/test_token_cache_atomic_swap.py:167`
- `tests/test_token_cache_atomic_swap.py:208`
- `tests/test_token_cache_atomic_swap.py:216`
- `tests/test_token_cache_atomic_swap.py:227`
- `tests/test_token_cache_atomic_swap.py:229`

## `ManageBgJobsTool` — class, line 65
- **called from:**
- `src/agent_tools/__init__.py:71`
- `tests/test_bg_job_tools.py:70`
- `tests/test_bg_job_tools.py:108`

## `ManageBgJobsTool.execute` — method (async), line 66
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
