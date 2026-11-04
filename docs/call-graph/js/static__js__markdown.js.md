# `static/js/markdown.js` — definitions & call sites

55 definitions (regex-based, best-effort).
**Exports:** `createCollapsible`, `default`, `ensureKatex`, `ensureMermaid`, `extractThinkingBlocks`, `hasUnclosedThinkTag`, `mdToHtml`, `neutralizeStrayThinkTags`, `normalizeThinkingMarkup`, `processWithThinking`, `renderContent`, `renderMath`, `renderMermaid`, `restoreThinkTags`, `sanitizeAllowedHtml`, `squashOutsideCode`, `startsWithReasoningPrefix`, `svgifyEmoji`

## `decodeMathSource` — function, line 53
- **called from:**
- `static/js/markdown.js:53`
- `static/js/markdown.js:1032`

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
- `static/js/markdown.js:1248`

## `ensureKatex` — function, line 103
- **called from:**
- `static/js/markdown.js:103`
- `static/js/markdown.js:128`
- `static/js/markdown.js:1268`

## `_scheduleMathFlush` — function, line 123
- **called from:**
- `static/js/markdown.js:123`
- `static/js/markdown.js:1072`

## `safeLinkUrl` — function, line 134
- **called from:**
- `static/js/markdown.js:134`
- `static/js/markdown.js:151`
- `static/js/markdown.js:161`

## `linkHtml` — function, line 150
- **called from:**
- `static/js/markdown.js:150`
- `static/js/markdown.js:975`
- `static/js/markdown.js:982`
- `static/js/markdown.js:998`

## `imageHtml` — function, line 160
- **called from:**
- `static/js/markdown.js:160`
- `static/js/markdown.js:969`

## `_isModelEndpointUrl` — function, line 168
- **called from:**
- `static/js/markdown.js:168`
- `static/js/markdown.js:1433`
- `static/js/markdown.js:1448`

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
- `static/js/markdown.js:1006`
- `static/js/markdown.js:1014`

## `neutralizeStrayThinkTags` — function, line 277
- **called from:**
- `static/js/chat.js:3309`
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
- `static/js/chat.js:3013`
- `static/js/markdown.js:376`
- `static/js/markdown.js:564`
- `static/js/markdown.js:565`

## `hasUnclosedThinkTag` — function, line 382
- **called from:**
- `static/js/chat.js:3091`
- `static/js/markdown.js:382`
- `static/js/markdown.js:523`

## `startsWithReasoningPrefix` — function, line 393
- **called from:**
- `static/js/chat.js:3387`
- `static/js/chat.js:4571`
- `static/js/liveThinkingThrottle.js:105`
- `static/js/markdown.js:393`
- `static/js/markdown.js:425`

## `normalizeThinkingMarkup` — function, line 397
- **called from:**
- `static/js/chat.js:740`
- `static/js/chat.js:2767`
- `static/js/chat.js:2775`
- `static/js/chat.js:2976`
- `static/js/chat.js:3007`
- `static/js/chat.js:3027`
- `static/js/chat.js:3087`
- `static/js/chat.js:3370`
- `static/js/chat.js:5697`
- `static/js/chat.js:7489`
- `static/js/markdown.js:383`
- `static/js/markdown.js:397`
- `static/js/markdown.js:421`

## `normalizePlainThinking` — function, line 419
- **called from:**
- `static/js/markdown.js:419`
- `static/js/markdown.js:483`

## `extractThinkingBlocks` — function, line 479
- **called from:**
- `static/js/chat.js:2777`
- `static/js/chat.js:3031`
- `static/js/chat.js:4555`
- `static/js/chat.js:4644`
- `static/js/chatRenderer.js:1116`
- `static/js/chatRenderer.js:2615`
- `static/js/chatRenderer.js:2926`
- `static/js/markdown.js:479`
- `static/js/markdown.js:699`

## `createThinkingSection` — function, line 573
- **called from:**
- `static/js/markdown.js:573`
- `static/js/markdown.js:708`

## `createTaskCompletedMarker` — function, line 596
- **called from:**
- `static/js/markdown.js:596`
- `static/js/markdown.js:713`
- `static/js/markdown.js:717`

## `_emojiCodepoints` — function, line 618
- **called from:**
- `static/js/markdown.js:618`
- `static/js/markdown.js:626`

## `_emojiImg` — function, line 625
- **called from:**
- `static/js/markdown.js:625`
- `static/js/markdown.js:638`

## `_svgifyText` — function, line 634
- **called from:**
- `static/js/markdown.js:634`
- `static/js/markdown.js:674`

## `_useSvgEmoji` — function, line 643
- **called from:**
- `static/js/markdown.js:643`
- `static/js/markdown.js:653`
- `static/js/markdown.js:720`
- `static/js/markdown.js:1200`

## `svgifyEmoji` — function, line 652
- **called from:**
- `static/js/chatRenderer.js:2395`
- `static/js/markdown.js:652`
- `static/js/markdown.js:720`
- `static/js/markdown.js:1200`

## `createCollapsible` — function, line 685
- **called from:**
- `static/js/markdown.js:685`

## `processWithThinking` — function, line 698
- **called from:**
- `static/js/chat.js:719`
- `static/js/chat.js:1566`
- `static/js/chat.js:2986`
- `static/js/chat.js:3121`
- `static/js/chat.js:4612`
- `static/js/chat.js:4648`
- `static/js/chat.js:4764`
- `static/js/chat.js:5693`
- `static/js/chat.js:6997`
- `static/js/chat.js:7152`
- `static/js/chat.js:7360`
- `static/js/chat.js:7471`
- `static/js/chat.js:7507`
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
- `static/js/markdown.js:698`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2683`

## `_listItem` — function, line 729
- **called from:**
- `static/js/markdown.js:729`
- `static/js/markdown.js:765`
- `static/js/markdown.js:770`
- `static/js/markdown.js:802`

## `_listItemHtml` — function, line 740
- **called from:**
- `static/js/markdown.js:740`
- `static/js/markdown.js:791`

## `_collectList` — function, line 752
- **called from:**
- `static/js/markdown.js:752`
- `static/js/markdown.js:785`
- `static/js/markdown.js:804`

## `_buildNestedLists` — function, line 797
- **called from:**
- `static/js/markdown.js:797`
- `static/js/markdown.js:1135`

## `_buildNestedQuotes` — function, line 811
- **called from:**
- `static/js/markdown.js:811`
- `static/js/markdown.js:1144`

## `mdToHtml` — function, line 848
- **called from:**
- `static/js/chat.js:745`
- `static/js/chat.js:2835`
- `static/js/chat.js:3070`
- `static/js/chat.js:4592`
- `static/js/document.js:2486`
- `static/js/document.js:9702`
- `static/js/document.js:9733`
- `static/js/document.js:9881`
- `static/js/documentLibrary.js:1956`
- `static/js/documentLibrary.js:2750`
- `static/js/markdown.js:115`
- `static/js/markdown.js:589`
- `static/js/markdown.js:694`
- `static/js/markdown.js:716`
- `static/js/markdown.js:848`
- `static/js/markdown.js:1261`
- `static/js/markdown.js:1262`
- `static/js/tasks.js:2451`

## `pushMath` — arrow, line 1031
- **called from:**
- `static/js/markdown.js:1048`
- `static/js/markdown.js:1053`
- `static/js/markdown.js:1060`
- `static/js/markdown.js:1069`

## `squashOutsideCode` — function, line 1206
- **called from:**
- `static/js/chat.js:719`
- `static/js/chat.js:745`
- `static/js/chat.js:1567`
- `static/js/chat.js:2986`
- `static/js/chat.js:3070`
- `static/js/chat.js:3121`
- `static/js/chat.js:4592`
- `static/js/chat.js:4612`
- `static/js/chat.js:4765`
- `static/js/chat.js:5693`
- `static/js/chat.js:6998`
- `static/js/chat.js:7153`
- `static/js/chat.js:7360`
- `static/js/chat.js:7472`
- `static/js/chat.js:7508`
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
- `static/js/markdown.js:1206`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2683`

## `renderContent` — function, line 1227
- **called from:**
- `static/js/chatRenderer.js:2575`
- `static/js/markdown.js:1227`
- `static/js/research/panel.js:1133`

## `renderMermaid` — function, line 1243
- **called from:**
- `static/js/chat.js:4665`
- `static/js/chatRenderer.js:2784`
- `static/js/chatRenderer.js:3126`
- `static/js/document.js:9889`
- `static/js/group.js:953`
- `static/js/markdown.js:1243`
- `static/js/slashCommands.js:454`

## `renderMath` — function, line 1264
- **called from:**
- `static/js/document.js:9743`
- `static/js/document.js:9745`
- `static/js/markdown.js:22`
- `static/js/markdown.js:129`
- `static/js/markdown.js:1028`
- `static/js/markdown.js:1264`

## `_loadExpandedSet` — function, line 1317
- **called from:**
- `static/js/markdown.js:1317`
- `static/js/markdown.js:1365`
- `static/js/markdown.js:1382`

## `_saveExpandedSet` — function, line 1321
- **called from:**
- `static/js/markdown.js:1321`
- `static/js/markdown.js:1368`

## `_hashThinkingContent` — function, line 1329
- **called from:**
- `static/js/markdown.js:1329`
- `static/js/markdown.js:1363`
- `static/js/markdown.js:1388`

## `_setThinkingExpanded` — function, line 1339
- **called from:**
- `static/js/markdown.js:1339`
- `static/js/markdown.js:1360`
- `static/js/markdown.js:1393`

## `_watchThinking` — function, line 1373
- **called from:**
- `static/js/markdown.js:1373`

## `_apply` — arrow, line 1376
- **called from:**
- `static/js/markdown.js:1399`
- `static/js/markdown.js:1403`
- `static/js/theme.js:719`

## `start` — arrow, line 1396
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
- `tests/test_compare_stop_disconnect_poll.py:266`
- `tests/test_compare_stop_disconnect_poll.py:276`
- … +95 more (grep the name in repo)

## `_endpointNameFromUrl` — function, line 1415
- **called from:**
- `static/js/markdown.js:1415`
- `static/js/markdown.js:1465`
- `static/js/markdown.js:1473`
- `static/js/markdown.js:1494`

## `_appendEndpointAddButtons` — function, line 1424
- **called from:**
- `static/js/markdown.js:1424`
- `static/js/markdown.js:1517`
- `static/js/markdown.js:1521`

## `_registerEndpointFromButton` — function, line 1446
- **called from:**
- `static/js/markdown.js:1446`
- `static/js/markdown.js:1511`

## `_watchModelEndpointLinks` — function, line 1502
- **called from:**
- `static/js/markdown.js:1502`

## `start` — arrow, line 1514
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
- `tests/test_compare_stop_disconnect_poll.py:266`
- `tests/test_compare_stop_disconnect_poll.py:276`
- … +95 more (grep the name in repo)
