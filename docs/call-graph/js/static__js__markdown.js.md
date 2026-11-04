# `static/js/markdown.js` — definitions & call sites

56 definitions (regex-based, best-effort).
**Exports:** `createCollapsible`, `default`, `ensureKatex`, `ensureMermaid`, `extractThinkingBlocks`, `hasUnclosedThinkTag`, `mdToHtml`, `neutralizeStrayThinkTags`, `normalizeThinkingMarkup`, `processWithThinking`, `renderContent`, `renderMath`, `renderMermaid`, `restoreThinkTags`, `sanitizeAllowedHtml`, `squashOutsideCode`, `startsWithReasoningPrefix`, `svgifyEmoji`, `tableReplyFloor`

## `decodeMathSource` — function, line 53
- **called from:**
- `static/js/markdown.js:53`
- `static/js/markdown.js:1080`

## `_loadScript` — function, line 61
- **called from:**
- `static/js/markdown.js:61`
- `static/js/markdown.js:88`
- `static/js/markdown.js:104`

## `_loadStylesheet` — function, line 71
- **called from:**
- `static/js/markdown.js:71`
- `static/js/markdown.js:104`

## `ensureMermaid` — function, line 87
- **called from:**
- `static/js/markdown.js:87`
- `static/js/markdown.js:1309`

## `ensureKatex` — function, line 103
- **called from:**
- `static/js/markdown.js:103`
- `static/js/markdown.js:128`
- `static/js/markdown.js:1329`

## `_scheduleMathFlush` — function, line 123
- **called from:**
- `static/js/markdown.js:123`
- `static/js/markdown.js:1120`

## `safeLinkUrl` — function, line 134
- **called from:**
- `static/js/markdown.js:134`
- `static/js/markdown.js:151`
- `static/js/markdown.js:161`

## `linkHtml` — function, line 150
- **called from:**
- `static/js/markdown.js:150`
- `static/js/markdown.js:1023`
- `static/js/markdown.js:1030`
- `static/js/markdown.js:1046`

## `imageHtml` — function, line 160
- **called from:**
- `static/js/markdown.js:160`
- `static/js/markdown.js:1017`

## `_isModelEndpointUrl` — function, line 168
- **called from:**
- `static/js/markdown.js:168`
- `static/js/markdown.js:1503`
- `static/js/markdown.js:1518`

## `_compactUrlSchemeValue` — function, line 207
- **called from:**
- `static/js/emailLibrary/utils.js:61`
- `static/js/emailLibrary/utils.js:66`
- `static/js/emailLibrary/utils.js:216`
- `static/js/markdown.js:207`
- `static/js/markdown.js:212`
- `static/js/markdown.js:239`

## `_isDangerousUrl` — function, line 211
- **called from:**
- `static/js/emailLibrary/utils.js:65`
- `static/js/emailLibrary/utils.js:71`
- `static/js/emailLibrary/utils.js:199`
- `static/js/markdown.js:211`
- `static/js/markdown.js:216`
- `static/js/markdown.js:248`

## `_isDangerousSrcset` — function, line 215
- **called from:**
- `static/js/emailLibrary/utils.js:70`
- `static/js/emailLibrary/utils.js:199`
- `static/js/markdown.js:215`
- `static/js/markdown.js:248`

## `_cleanAllowedHtmlOnce` — function, line 219
- **called from:**
- `static/js/markdown.js:219`
- `static/js/markdown.js:267`

## `sanitizeAllowedHtml` — function, line 257
- **called from:**
- `static/js/document.js:2481`
- `static/js/document.js:2497`
- `static/js/markdown.js:257`
- `static/js/markdown.js:1054`
- `static/js/markdown.js:1062`

## `neutralizeStrayThinkTags` — function, line 277
- **called from:**
- `static/js/chat.js:3317`
- `static/js/chat.js:5785`
- `static/js/chat.js:7510`
- `static/js/chatRenderer.js:2633`
- `static/js/chatRenderer.js:2920`
- `static/js/markdown.js:277`
- `static/js/markdown.js:401`

## `esc` — arrow, line 307
- **called from:**
- `static/js/admin.js:20`
- `static/js/admin.js:20`
- `static/js/admin.js:53`
- `static/js/admin.js:55`
- `static/js/admin.js:60`
- `static/js/admin.js:61`
- `static/js/admin.js:62`
- `static/js/admin.js:80`
- `static/js/admin.js:91`
- `static/js/admin.js:104`
- `static/js/admin.js:105`
- `static/js/admin.js:109`
- `static/js/admin.js:273`
- `static/js/admin.js:274`
- `static/js/admin.js:275`
- `static/js/admin.js:525`
- `static/js/admin.js:532`
- `static/js/admin.js:534`
- `static/js/admin.js:545`
- `static/js/admin.js:545`
- `static/js/admin.js:674`
- `static/js/admin.js:679`
- `static/js/admin.js:719`
- `static/js/admin.js:719`
- `static/js/admin.js:720`
- `static/js/admin.js:722`
- `static/js/admin.js:1022`
- `static/js/admin.js:1200`
- `static/js/admin.js:1203`
- `static/js/admin.js:1206`
- `static/js/admin.js:1933`
- `static/js/admin.js:1948`
- `static/js/admin.js:1949`
- `static/js/admin.js:1951`
- `static/js/admin.js:1953`
- `static/js/admin.js:2081`
- `static/js/admin.js:2156`
- `static/js/admin.js:2157`
- `static/js/admin.js:2158`
- `static/js/admin.js:2158`
- `static/js/admin.js:2390`
- `static/js/admin.js:2417`
- `static/js/admin.js:2417`
- `static/js/admin.js:2417`
- `static/js/admin.js:2436`
- `static/js/admin.js:2436`
- `static/js/admin.js:2436`
- `static/js/admin.js:2542`
- `static/js/admin.js:2543`
- `static/js/admin.js:2544`
- `static/js/admin.js:2545`
- `static/js/admin.js:2545`
- `static/js/admin.js:2558`
- `static/js/admin.js:2561`
- `static/js/admin.js:2561`
- `static/js/admin.js:2562`
- `static/js/admin.js:2563`
- `static/js/admin.js:2566`
- `static/js/admin.js:2567`
- `static/js/admin.js:2569`
- … +443 more (grep the name in repo)

## `restoreThinkTags` — function, line 376
- **called from:**
- `static/js/chat.js:3021`
- `static/js/markdown.js:376`
- `static/js/markdown.js:612`
- `static/js/markdown.js:613`

## `hasUnclosedThinkTag` — function, line 382
- **called from:**
- `static/js/chat.js:3099`
- `static/js/markdown.js:382`
- `static/js/markdown.js:571`

## `startsWithReasoningPrefix` — function, line 393
- **called from:**
- `static/js/chat.js:3395`
- `static/js/chat.js:4579`
- `static/js/liveThinkingThrottle.js:105`
- `static/js/markdown.js:393`
- `static/js/markdown.js:456`

## `normalizeThinkingMarkup` — function, line 397
- **called from:**
- `static/js/chat.js:741`
- `static/js/chat.js:2775`
- `static/js/chat.js:2783`
- `static/js/chat.js:2984`
- `static/js/chat.js:3015`
- `static/js/chat.js:3035`
- `static/js/chat.js:3095`
- `static/js/chat.js:3378`
- `static/js/chat.js:5694`
- `static/js/chat.js:7650`
- `static/js/markdown.js:383`
- `static/js/markdown.js:397`
- `static/js/markdown.js:452`

## `tableReplyFloor` — function, line 429
- **called from:**
- `static/js/chat.js:4584`
- `static/js/markdown.js:429`
- `static/js/markdown.js:475`
- `static/js/markdown.js:483`
- `static/js/markdown.js:502`
- `static/js/markdown.js:513`

## `normalizePlainThinking` — function, line 450
- **called from:**
- `static/js/markdown.js:450`
- `static/js/markdown.js:531`

## `extractThinkingBlocks` — function, line 527
- **called from:**
- `static/js/chat.js:2785`
- `static/js/chat.js:3039`
- `static/js/chat.js:4563`
- `static/js/chat.js:4663`
- `static/js/chatRenderer.js:1116`
- `static/js/chatRenderer.js:2615`
- `static/js/chatRenderer.js:2926`
- `static/js/markdown.js:527`
- `static/js/markdown.js:747`

## `createThinkingSection` — function, line 621
- **called from:**
- `static/js/markdown.js:621`
- `static/js/markdown.js:756`

## `createTaskCompletedMarker` — function, line 644
- **called from:**
- `static/js/markdown.js:644`
- `static/js/markdown.js:761`
- `static/js/markdown.js:765`

## `_emojiCodepoints` — function, line 666
- **called from:**
- `static/js/markdown.js:666`
- `static/js/markdown.js:674`

## `_emojiImg` — function, line 673
- **called from:**
- `static/js/markdown.js:673`
- `static/js/markdown.js:686`

## `_svgifyText` — function, line 682
- **called from:**
- `static/js/markdown.js:682`
- `static/js/markdown.js:722`

## `_useSvgEmoji` — function, line 691
- **called from:**
- `static/js/markdown.js:691`
- `static/js/markdown.js:701`
- `static/js/markdown.js:768`
- `static/js/markdown.js:1261`

## `svgifyEmoji` — function, line 700
- **called from:**
- `static/js/chatRenderer.js:2395`
- `static/js/markdown.js:700`
- `static/js/markdown.js:768`
- `static/js/markdown.js:1261`

## `createCollapsible` — function, line 733
- **called from:**
- `static/js/markdown.js:733`

## `processWithThinking` — function, line 746
- **called from:**
- `static/js/chat.js:720`
- `static/js/chat.js:1567`
- `static/js/chat.js:2994`
- `static/js/chat.js:3129`
- `static/js/chat.js:4631`
- `static/js/chat.js:4667`
- `static/js/chat.js:4785`
- `static/js/chat.js:5690`
- `static/js/chat.js:7077`
- `static/js/chat.js:7234`
- `static/js/chat.js:7511`
- `static/js/chat.js:7515`
- `static/js/chat.js:7632`
- `static/js/chat.js:7668`
- `static/js/chatRenderer.js:2694`
- `static/js/chatRenderer.js:2928`
- `static/js/chatRenderer.js:2933`
- `static/js/chatRenderer.js:2965`
- `static/js/chatRenderer.js:3022`
- `static/js/compare/stream.js:268`
- `static/js/compare/stream.js:355`
- `static/js/compare/stream.js:511`
- `static/js/compare/stream.js:649`
- `static/js/compare/stream.js:789`
- `static/js/group.js:884`
- `static/js/group.js:900`
- `static/js/group.js:949`
- `static/js/markdown.js:746`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2683`

## `_listItem` — function, line 777
- **called from:**
- `static/js/markdown.js:777`
- `static/js/markdown.js:813`
- `static/js/markdown.js:818`
- `static/js/markdown.js:850`

## `_listItemHtml` — function, line 788
- **called from:**
- `static/js/markdown.js:788`
- `static/js/markdown.js:839`

## `_collectList` — function, line 800
- **called from:**
- `static/js/markdown.js:800`
- `static/js/markdown.js:833`
- `static/js/markdown.js:852`

## `_buildNestedLists` — function, line 845
- **called from:**
- `static/js/markdown.js:845`
- `static/js/markdown.js:1196`

## `_buildNestedQuotes` — function, line 859
- **called from:**
- `static/js/markdown.js:859`
- `static/js/markdown.js:1205`

## `mdToHtml` — function, line 896
- **called from:**
- `static/js/chat.js:746`
- `static/js/chat.js:2843`
- `static/js/chat.js:3078`
- `static/js/chat.js:4611`
- `static/js/document.js:2486`
- `static/js/document.js:9702`
- `static/js/document.js:9733`
- `static/js/document.js:9881`
- `static/js/documentLibrary.js:1996`
- `static/js/documentLibrary.js:2965`
- `static/js/markdown.js:115`
- `static/js/markdown.js:637`
- `static/js/markdown.js:742`
- `static/js/markdown.js:764`
- `static/js/markdown.js:896`
- `static/js/markdown.js:1322`
- `static/js/markdown.js:1323`
- `static/js/tasks.js:2451`

## `pushMath` — arrow, line 1079
- **called from:**
- `static/js/markdown.js:1096`
- `static/js/markdown.js:1101`
- `static/js/markdown.js:1108`
- `static/js/markdown.js:1117`

## `squashOutsideCode` — function, line 1267
- **called from:**
- `static/js/chat.js:720`
- `static/js/chat.js:746`
- `static/js/chat.js:1568`
- `static/js/chat.js:2994`
- `static/js/chat.js:3078`
- `static/js/chat.js:3129`
- `static/js/chat.js:4611`
- `static/js/chat.js:4631`
- `static/js/chat.js:4786`
- `static/js/chat.js:5690`
- `static/js/chat.js:7078`
- `static/js/chat.js:7235`
- `static/js/chat.js:7515`
- `static/js/chat.js:7633`
- `static/js/chat.js:7669`
- `static/js/chatRenderer.js:2694`
- `static/js/chatRenderer.js:2860`
- `static/js/chatRenderer.js:3022`
- `static/js/compare/stream.js:269`
- `static/js/compare/stream.js:356`
- `static/js/compare/stream.js:512`
- `static/js/compare/stream.js:650`
- `static/js/compare/stream.js:790`
- `static/js/group.js:885`
- `static/js/group.js:901`
- `static/js/group.js:950`
- `static/js/markdown.js:1267`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2683`

## `renderContent` — function, line 1288
- **called from:**
- `static/js/chatRenderer.js:2575`
- `static/js/markdown.js:1288`
- `static/js/research/panel.js:1133`

## `renderMermaid` — function, line 1304
- **called from:**
- `static/js/chat.js:4684`
- `static/js/chatRenderer.js:2784`
- `static/js/chatRenderer.js:3126`
- `static/js/document.js:9889`
- `static/js/group.js:953`
- `static/js/markdown.js:1304`
- `static/js/slashCommands.js:454`

## `renderMath` — function, line 1325
- **called from:**
- `static/js/document.js:9743`
- `static/js/document.js:9745`
- `static/js/markdown.js:22`
- `static/js/markdown.js:129`
- `static/js/markdown.js:1076`
- `static/js/markdown.js:1325`

## `_loadExpandedSet` — function, line 1379
- **called from:**
- `static/js/markdown.js:1379`
- `static/js/markdown.js:1435`
- `static/js/markdown.js:1452`

## `_saveExpandedSet` — function, line 1383
- **called from:**
- `static/js/markdown.js:1383`
- `static/js/markdown.js:1438`

## `_hashThinkingContent` — function, line 1391
- **called from:**
- `static/js/markdown.js:1391`
- `static/js/markdown.js:1433`
- `static/js/markdown.js:1458`

## `_setThinkingExpanded` — function, line 1401
- **called from:**
- `static/js/markdown.js:1401`
- `static/js/markdown.js:1430`
- `static/js/markdown.js:1463`

## `_watchThinking` — function, line 1443
- **called from:**
- `static/js/markdown.js:1443`

## `_apply` — arrow, line 1446
- **called from:**
- `static/js/markdown.js:1469`
- `static/js/markdown.js:1473`
- `static/js/theme.js:719`

## `start` — arrow, line 1466
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

## `_endpointNameFromUrl` — function, line 1485
- **called from:**
- `static/js/markdown.js:1485`
- `static/js/markdown.js:1535`
- `static/js/markdown.js:1543`
- `static/js/markdown.js:1564`

## `_appendEndpointAddButtons` — function, line 1494
- **called from:**
- `static/js/markdown.js:1494`
- `static/js/markdown.js:1587`
- `static/js/markdown.js:1591`

## `_registerEndpointFromButton` — function, line 1516
- **called from:**
- `static/js/markdown.js:1516`
- `static/js/markdown.js:1581`

## `_watchModelEndpointLinks` — function, line 1572
- **called from:**
- `static/js/markdown.js:1572`

## `start` — arrow, line 1584
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
