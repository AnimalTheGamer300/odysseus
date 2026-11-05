# `src/cleanup_service.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_utcnow` — function, line 9
- **called from:**
- `src/cleanup_service.py:86`
- `src/cleanup_service.py:101`
- `src/cleanup_service.py:127`
- `src/cleanup_service.py:235`
- `src/cleanup_service.py:236`
- `src/task_scheduler.py:181`
- `src/task_scheduler.py:186`
- `src/task_scheduler.py:493`
- `src/task_scheduler.py:511`
- `src/task_scheduler.py:514`
- `src/task_scheduler.py:516`
- `src/task_scheduler.py:520`
- `src/task_scheduler.py:534`
- `src/task_scheduler.py:610`
- `src/task_scheduler.py:631`
- `src/task_scheduler.py:836`
- `src/task_scheduler.py:848`
- `src/task_scheduler.py:896`
- `src/task_scheduler.py:953`
- `src/task_scheduler.py:955`
- `src/task_scheduler.py:981`
- `src/task_scheduler.py:996`
- `src/task_scheduler.py:999`
- `src/task_scheduler.py:1022`
- `src/task_scheduler.py:1031`
- `src/task_scheduler.py:1094`
- `src/task_scheduler.py:1129`
- `src/task_scheduler.py:1130`
- `src/task_scheduler.py:1135`
- `src/task_scheduler.py:1151`
- `src/task_scheduler.py:1154`
- `src/task_scheduler.py:1163`
- `src/task_scheduler.py:1251`
- `src/task_scheduler.py:1256`
- `src/task_scheduler.py:1261`
- `src/task_scheduler.py:1286`
- `src/task_scheduler.py:1291`
- `src/task_scheduler.py:1292`
- `src/task_scheduler.py:1496`
- `src/task_scheduler.py:1499`
- `src/task_scheduler.py:1503`
- `src/task_scheduler.py:1710`
- `src/task_scheduler.py:1711`
- `src/task_scheduler.py:1890`
- `src/task_scheduler.py:1891`
- `src/task_scheduler.py:1940`
- `src/task_scheduler.py:1948`
- `src/task_scheduler.py:2290`
- `src/task_scheduler.py:2291`
- `src/task_scheduler.py:2624`
- `src/task_scheduler.py:2652`
- `src/task_scheduler.py:2687`
- `src/task_scheduler.py:2705`
- `src/task_scheduler.py:2845`
- `src/task_scheduler.py:2846`
- `src/webhook_manager.py:418`
- `src/webhook_manager.py:432`
- `src/webhook_manager.py:441`
- `tests/test_cleanup_service_utcnow.py:13`
- `tests/test_cleanup_service_utcnow.py:23`
- … +2 more (grep the name in repo)

## `CleanupConfig` — class, line 18
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_apply_owner_filter` — function, line 28
- **called from:**
- `src/cleanup_service.py:51`
- `src/cleanup_service.py:96`
- `src/cleanup_service.py:141`
- `src/cleanup_service.py:180`
- `src/cleanup_service.py:250`
- `src/cleanup_service.py:269`

## `_message_count_subquery` — function, line 40
- **called from:**
- `src/cleanup_service.py:142`
- `src/cleanup_service.py:251`

## `_recent_session_ids` — function, line 48
- **called from:**
- `src/cleanup_service.py:134`
- `src/cleanup_service.py:262`

## `_supports_delete_returning` — function, line 55
- **called from:**
- `src/cleanup_service.py:181`

## `archive_inactive_sessions` — function (async), line 75
- **called from:**
- `src/cleanup_service.py:345`

## `cleanup_old_sessions` — function (async), line 116
- **called from:**
- `src/cleanup_service.py:350`

## `get_cleanup_preview` — function (async), line 225
- **called from:**
- `routes/cleanup/cleanup_routes.py:32`

## `cleanup_sessions` — function (async), line 329
- **called from:**
- `routes/cleanup/cleanup_routes.py:50`
