# `services/shell/service.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ShellResult` — class, line 11
- decorator: `dataclass`
- **called from:**
- `services/shell/service.py:67`
- `services/shell/service.py:79`
- `services/shell/service.py:86`

## `ShellService` — class, line 19
- **called from:**
- `tests/test_shell_service.py:51`

## `ShellService.__init__` — method, line 29
- **called from:**
- `core/exceptions.py:8`
- `core/exceptions.py:15`
- `core/exceptions.py:22`
- `core/exceptions.py:29`
- `routes/email_routes.py:1455`
- `src/builtin_actions.py:428`
- `src/outbound_fetch.py:220`
- `tests/test_agent_state_dir_confinement.py:648`
- `tests/test_calendar_default_transaction.py:456`
- `tests/test_chat_attachment_picker.py:10`
- `tests/test_deep_research_extraction_controls.py:14`
- `tests/test_embedding_lanes.py:257`
- `tests/test_embedding_lanes.py:284`
- `tests/test_integrations_store_shape.py:46`
- `tests/test_retired_settings_interfaces.py:30`
- `tests/test_upload_handler_atomicity.py:42`
- `tests/test_upload_multifile.py:154`
- `static/js/cookbookDownload.js:148`

## `ShellService.execute` — method (async), line 34
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

## `ShellService.stream` — method (async), line 88
- **called from:**
- `src/llm_core.py:3043`
- `src/llm_core.py:3164`
- `src/llm_core.py:3263`
- `src/llm_core.py:3468`
- `src/outbound_fetch.py:297`
- `tests/test_compare_stop_disconnect_poll.py:200`
- `tests/test_compare_stop_disconnect_poll.py:206`
- `tests/test_shell_service.py:52`
- `tests/test_web_fetch_size_caps.py:56`
- `tests/test_web_fetch_size_caps.py:63`
- `static/js/chat.js:341`
- `static/js/sessions.js:2214`
- `static/js/sessions.js:2793`

## `ShellService._reader` — method (async), line 113
- **called from:**
- `routes/shell_routes.py:1061`
- `routes/shell_routes.py:1062`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `src/agent_tools/subprocess_tools.py:246`
- `src/agent_tools/subprocess_tools.py:247`
