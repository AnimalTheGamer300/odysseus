# `src/cleanup_service.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow` — function, line 9
- **called from:**
- `src/cleanup_service.py:51`
- `src/cleanup_service.py:66`
- `src/cleanup_service.py:92`
- `src/cleanup_service.py:171`
- `src/cleanup_service.py:172`
- `src/task_scheduler.py:142`
- `src/task_scheduler.py:147`
- `src/task_scheduler.py:403`
- `src/task_scheduler.py:424`
- `src/task_scheduler.py:470`
- `src/task_scheduler.py:491`
- `src/task_scheduler.py:693`
- `src/task_scheduler.py:705`
- `src/task_scheduler.py:752`
- `src/task_scheduler.py:807`
- `src/task_scheduler.py:809`
- `src/task_scheduler.py:835`
- `src/task_scheduler.py:850`
- `src/task_scheduler.py:853`
- `src/task_scheduler.py:876`
- `src/task_scheduler.py:885`
- `src/task_scheduler.py:948`
- `src/task_scheduler.py:971`
- `src/task_scheduler.py:972`
- `src/task_scheduler.py:974`
- `src/task_scheduler.py:979`
- `src/task_scheduler.py:996`
- `src/task_scheduler.py:997`
- `src/task_scheduler.py:1002`
- `src/task_scheduler.py:1018`
- `src/task_scheduler.py:1021`
- `src/task_scheduler.py:1030`
- `src/task_scheduler.py:1118`
- `src/task_scheduler.py:1123`
- `src/task_scheduler.py:1128`
- `src/task_scheduler.py:1153`
- `src/task_scheduler.py:1158`
- `src/task_scheduler.py:1159`
- `src/task_scheduler.py:1342`
- `src/task_scheduler.py:1345`
- `src/task_scheduler.py:1349`
- `src/task_scheduler.py:1550`
- `src/task_scheduler.py:1551`
- `src/task_scheduler.py:1728`
- `src/task_scheduler.py:1729`
- `src/task_scheduler.py:1778`
- `src/task_scheduler.py:1786`
- `src/task_scheduler.py:2096`
- `src/task_scheduler.py:2097`
- `src/task_scheduler.py:2421`
- `src/task_scheduler.py:2456`
- `src/task_scheduler.py:2473`
- `src/task_scheduler.py:2612`
- `src/task_scheduler.py:2613`
- `src/webhook_manager.py:418`
- `src/webhook_manager.py:432`
- `src/webhook_manager.py:441`
- `tests/test_cleanup_service_utcnow.py:13`
- `tests/test_cleanup_service_utcnow.py:23`
- `tests/test_cleanup_service_utcnow.py:25`
- … +1 more (grep the name in repo)

## `CleanupConfig` — class, line 18
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apply_owner_filter` — function, line 28
- **called from:**
- `src/cleanup_service.py:61`
- `src/cleanup_service.py:100`
- `src/cleanup_service.py:110`
- `src/cleanup_service.py:186`
- `src/cleanup_service.py:198`
- `src/cleanup_service.py:208`

## `archive_inactive_sessions` — function (async), line 40
- **called from:**
- `src/cleanup_service.py:284`

## `cleanup_old_sessions` — function (async), line 81
- **called from:**
- `src/cleanup_service.py:289`

## `get_cleanup_preview` — function (async), line 161
- **called from:**
- `routes/cleanup/cleanup_routes.py:32`

## `cleanup_sessions` — function (async), line 268
- **called from:**
- `routes/cleanup/cleanup_routes.py:50`
