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

## `ShellService.stream` — method (async), line 88
- **called from:**
- `src/llm_core.py:3075`
- `src/llm_core.py:3196`
- `src/llm_core.py:3295`
- `src/llm_core.py:3500`
- `src/outbound_fetch.py:297`
- `tests/test_compare_stop_disconnect_poll.py:200`
- `tests/test_compare_stop_disconnect_poll.py:206`
- `tests/test_shell_service.py:52`
- `tests/test_web_fetch_size_caps.py:56`
- `tests/test_web_fetch_size_caps.py:63`
- `static/js/chat.js:342`
- `static/js/sessions.js:2217`
- `static/js/sessions.js:2796`

## `ShellService._reader` — method (async), line 113
- **called from:**
- `routes/shell_routes.py:1061`
- `routes/shell_routes.py:1062`
- `services/shell/service.py:124`
- `services/shell/service.py:125`
- `src/agent_tools/subprocess_tools.py:246`
- `src/agent_tools/subprocess_tools.py:247`
