# `static/js/streamingRenderer.js` — definitions & call sites

12 definitions (regex-based, best-effort).
**Exports:** `createStreamRenderer`

## `createStreamRenderer` — function, line 29
- **called from:**
- `static/js/chat.js:719`
- `static/js/chat.js:3077`
- `static/js/chat.js:3128`
- `static/js/chat.js:5689`
- `static/js/streamingRenderer.js:29`

## `start` — function, line 38
- **called from:**
- `app.py:1218`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `routes/chat_helpers.py:1149`
- `routes/chat_helpers.py:1150`
- `routes/chat_helpers.py:1151`
- `routes/chat_routes.py:3068`
- `routes/cookbook_routes.py:3678`
- `routes/email_helpers.py:273`
- `routes/email_routes.py:1003`
- `routes/model_routes.py:1537`
- `routes/skills_routes.py:849`
- `scripts/add_hwfit_models.py:64`
- `services/hwfit/hf_discovery.py:115`
- `services/search/content.py:720`
- `services/search/content.py:720`
- `src/agent_tools/document_tools.py:205`
- `src/agent_tools/filesystem_tools.py:864`
- `src/agent_tools/filesystem_tools.py:865`
- `src/agent_tools/filesystem_tools.py:954`
- `src/llm_core.py:346`
- `src/pdf_form_doc.py:86`
- `src/text_helpers.py:110`
- `src/text_helpers.py:111`
- `src/tool_parsing.py:595`
- `src/tool_parsing.py:762`
- `src/tool_parsing.py:785`
- `src/tool_parsing.py:1211`
- `src/tool_parsing.py:1211`
- `src/tool_parsing.py:1245`
- `src/tool_parsing.py:1272`
- `src/tool_parsing.py:1344`
- `src/visual_report.py:1706`
- `src/visual_report.py:1709`
- `tests/markdown_browser_check.py:32`
- `tests/markdown_screenshot.py:57`
- `tests/test_agent_thread_dot_alignment_css.py:35`
- `tests/test_app_config_shared_fetch_js.py:210`
- `tests/test_app_config_shared_fetch_js.py:210`
- `tests/test_app_config_shared_fetch_js.py:212`
- `tests/test_atomic_io.py:114`
- `tests/test_atomic_io.py:115`
- `tests/test_auth_config_lock_concurrency.py:185`
- `tests/test_auth_config_lock_concurrency.py:234`
- `tests/test_auth_config_lock_concurrency.py:235`
- `tests/test_caldav_redirect_hardening.py:65`
- `tests/test_caldav_redirect_hardening.py:66`
- `tests/test_calendar_default_transaction.py:287`
- `tests/test_calendar_default_transaction.py:288`
- `tests/test_compare_stop_disconnect_poll.py:105`
- `tests/test_compare_stop_disconnect_poll.py:135`
- `tests/test_compare_stop_disconnect_poll.py:167`
- `tests/test_compare_stop_disconnect_poll.py:180`
- `tests/test_compare_stop_disconnect_poll.py:186`
- `tests/test_compare_stop_disconnect_poll.py:200`
- `tests/test_compare_stop_disconnect_poll.py:206`
- `tests/test_compare_stop_disconnect_poll.py:227`
- `tests/test_compare_stop_disconnect_poll.py:229`
- `tests/test_compare_stop_disconnect_poll.py:262`
- … +98 more (grep the name in repo)

## `highlight` — function, line 45
- **called from:**
- `static/js/documentLibrary.js:784`
- `static/js/documentLibrary.js:963`
- `static/js/streamingRenderer.js:45`
- `static/js/streamingRenderer.js:58`
- `static/js/streamingRenderer.js:137`

## `clearTail` — function, line 49
- **called from:**
- `static/js/streamingRenderer.js:49`
- `static/js/streamingRenderer.js:70`
- `static/js/streamingRenderer.js:86`
- `static/js/streamingRenderer.js:191`

## `freeze` — function, line 55
- **called from:**
- `static/js/emailLibrary.js:2491`
- `static/js/emailLibrary.js:5385`
- `static/js/emailLibrary/utils.js:33`
- `static/js/settings/registry.js:9`
- `static/js/settings/registry.js:13`
- `static/js/settings/registry.js:17`
- `static/js/settings/registry.js:21`
- `static/js/settings/registry.js:46`
- `static/js/streamingRenderer.js:55`
- `static/js/streamingRenderer.js:169`
- `static/js/streamingRenderer.js:194`

## `renderTail` — function, line 63
- **called from:**
- `static/js/streamingRenderer.js:63`
- `static/js/streamingRenderer.js:174`

## `appendOpenFence` — function, line 84
- **called from:**
- `static/js/streamingRenderer.js:66`
- `static/js/streamingRenderer.js:84`

## `that` — class, line 106
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `fadeNewText` — function, line 109
- **called from:**
- `static/js/streamingRenderer.js:77`
- `static/js/streamingRenderer.js:109`

## `fullRender` — function, line 135
- **called from:**
- `static/js/streamingRenderer.js:135`
- `static/js/streamingRenderer.js:151`
- `static/js/streamingRenderer.js:178`
- `static/js/streamingRenderer.js:201`

## `update` — function, line 148
- **called from:**
- `app.py:335`
- `app.py:446`
- `app.py:1152`
- `app.py:1172`
- `core/database.py:2770`
- `core/session_manager.py:606`
- `core/session_manager.py:1087`
- `routes/auth_routes.py:424`
- `routes/auth_routes.py:437`
- `routes/backup_routes.py:197`
- `routes/backup_routes.py:204`
- `routes/backup_routes.py:212`
- `routes/chat_helpers.py:451`
- `routes/chat_helpers.py:556`
- `routes/chat_helpers.py:564`
- `routes/chat_routes.py:246`
- `routes/chat_routes.py:297`
- `routes/chat_routes.py:1681`
- `routes/chat_routes.py:1691`
- `routes/chat_routes.py:1703`
- `routes/chat_routes.py:1721`
- `routes/chat_routes.py:1736`
- `routes/chat_routes.py:1738`
- `routes/chat_routes.py:1740`
- `routes/chat_routes.py:1744`
- `routes/chat_routes.py:1754`
- `routes/chat_routes.py:1762`
- `routes/chat_routes.py:1766`
- `routes/chat_routes.py:1770`
- `routes/chat_routes.py:1781`
- `routes/chat_routes.py:1784`
- `routes/chat_routes.py:1791`
- `routes/chat_routes.py:2163`
- `routes/chat_routes.py:2401`
- `routes/chat_routes.py:2420`
- `routes/cookbook_routes.py:3385`
- `routes/cookbook_routes.py:3389`
- `routes/cookbook_routes.py:3392`
- `routes/cookbook_routes.py:3507`
- `routes/cookbook_routes.py:4215`
- `routes/device_flow.py:156`
- `routes/email_pollers.py:786`
- `routes/email_routes.py:145`
- `routes/email_routes.py:1177`
- `routes/email_routes.py:1993`
- `routes/email_routes.py:2311`
- `routes/email_routes.py:3524`
- `routes/email_routes.py:3871`
- `routes/email_routes.py:3872`
- `routes/email_routes.py:3875`
- `routes/email_routes.py:3880`
- `routes/email_routes.py:4939`
- `routes/email_routes.py:5571`
- `routes/email_routes.py:5695`
- `routes/email_routes.py:6000`
- `routes/gallery/gallery_routes.py:2170`
- `routes/gallery/gallery_routes.py:2189`
- `routes/gallery/gallery_routes.py:2208`
- `routes/gallery/gallery_routes.py:2310`
- `routes/history/history_routes.py:707`
- … +205 more (grep the name in repo)

## `finalize` — function, line 187
- **called from:**
- `static/js/chat.js:845`
- `static/js/streamingRenderer.js:157`
- `static/js/streamingRenderer.js:187`
