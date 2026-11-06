# `static/js/markdown.js` — definitions & call sites

71 definitions (regex-based, best-effort).
**Exports:** `createCollapsible`, `default`, `ensureKatex`, `ensureMermaid`, `extractThinkingBlocks`, `hasUnclosedThinkTag`, `mdToHtml`, `neutralizeStrayThinkTags`, `normalizeThinkingMarkup`, `processWithThinking`, `renderContent`, `renderMath`, `renderMermaid`, `restoreThinkTags`, `sanitizeAllowedHtml`, `squashOutsideCode`, `startsWithReasoningPrefix`, `svgifyEmoji`

## `decodeMathSource` — function, line 53
- **called from:**
- `static/js/markdown.js:53`
- `static/js/markdown.js:1385`

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
- `static/js/markdown.js:1606`

## `ensureKatex` — function, line 103
- **called from:**
- `static/js/markdown.js:103`
- `static/js/markdown.js:128`
- `static/js/markdown.js:1626`

## `_scheduleMathFlush` — function, line 123
- **called from:**
- `static/js/markdown.js:123`
- `static/js/markdown.js:1425`

## `safeLinkUrl` — function, line 134
- **called from:**
- `static/js/markdown.js:134`
- `static/js/markdown.js:151`

## `linkHtml` — function, line 150
- **called from:**
- `static/js/markdown.js:150`
- `static/js/markdown.js:1329`
- `static/js/markdown.js:1336`
- `static/js/markdown.js:1352`

## `linkifyPlainEmailUidLines` — function, line 160
- **called from:**
- `static/js/markdown.js:160`
- `static/js/markdown.js:1309`

## `linkifyRawEmailToolBlocks` — function, line 173
- **called from:**
- `static/js/markdown.js:173`
- `static/js/markdown.js:1307`

## `linkifyRawEmailReadBlocks` — function, line 198
- **called from:**
- `static/js/markdown.js:198`
- `static/js/markdown.js:1308`

## `linkifyRawCookbookLists` — function, line 216
- **called from:**
- `static/js/markdown.js:216`
- `static/js/markdown.js:1310`

## `linkifyPlainSkillLists` — function, line 235
- **called from:**
- `static/js/markdown.js:235`
- `static/js/markdown.js:1311`

## `flattenLegacyNoteMoreDetails` — function, line 255
- **called from:**
- `static/js/markdown.js:255`
- `static/js/markdown.js:1173`

## `extractMoreListPayloads` — function, line 264
- **called from:**
- `static/js/markdown.js:264`
- `static/js/markdown.js:1173`

## `moreListPayloadFromHref` — function, line 291
- **called from:**
- `static/js/markdown.js:291`
- `static/js/markdown.js:1714`

## `imageHtml` — function, line 304
- **called from:**
- `static/js/markdown.js:304`
- `static/js/markdown.js:1322`

## `_bindChatImageFallback` — function, line 335
- **called from:**
- `static/js/markdown.js:302`
- `static/js/markdown.js:335`
- `static/js/markdown.js:350`

## `wrapOf` — arrow, line 337
- **called from:**
- `static/js/markdown.js:342`
- `static/js/markdown.js:346`

## `_isModelEndpointUrl` — function, line 352
- **called from:**
- `static/js/markdown.js:352`
- `static/js/markdown.js:1840`
- `static/js/markdown.js:1855`

## `_compactUrlSchemeValue` — function, line 391
- **called from:**
- `static/js/emailLibrary/utils.js:61`
- `static/js/emailLibrary/utils.js:66`
- `static/js/emailLibrary/utils.js:224`
- `static/js/markdown.js:391`
- `static/js/markdown.js:396`
- `static/js/markdown.js:423`

## `_isDangerousUrl` — function, line 395
- **called from:**
- `static/js/emailLibrary/utils.js:65`
- `static/js/emailLibrary/utils.js:71`
- `static/js/emailLibrary/utils.js:207`
- `static/js/markdown.js:395`
- `static/js/markdown.js:400`
- `static/js/markdown.js:432`

## `_isDangerousSrcset` — function, line 399
- **called from:**
- `static/js/emailLibrary/utils.js:70`
- `static/js/emailLibrary/utils.js:207`
- `static/js/markdown.js:399`
- `static/js/markdown.js:432`

## `_cleanAllowedHtmlOnce` — function, line 403
- **called from:**
- `static/js/markdown.js:403`
- `static/js/markdown.js:451`

## `sanitizeAllowedHtml` — function, line 441
- **called from:**
- `static/js/document.js:3570`
- `static/js/document.js:3602`
- `static/js/document.js:3623`
- `static/js/document.js:3639`
- `static/js/document.js:4157`
- `static/js/document.js:16165`
- `static/js/document.js:16250`
- `static/js/markdown.js:441`
- `static/js/markdown.js:1359`
- `static/js/markdown.js:1367`

## `neutralizeStrayThinkTags` — function, line 461
- **called from:**
- `static/js/chat.js:4836`
- `static/js/chatRenderer.js:3319`
- `static/js/chatRenderer.js:3645`
- `static/js/markdown.js:461`
- `static/js/markdown.js:585`

## `esc` — arrow, line 491
- **called from:**
- `static/js/admin.js:28`
- `static/js/admin.js:28`
- `static/js/admin.js:86`
- `static/js/admin.js:88`
- `static/js/admin.js:93`
- `static/js/admin.js:94`
- `static/js/admin.js:96`
- `static/js/admin.js:114`
- `static/js/admin.js:125`
- `static/js/admin.js:138`
- `static/js/admin.js:139`
- `static/js/admin.js:143`
- `static/js/admin.js:330`
- `static/js/admin.js:331`
- `static/js/admin.js:332`
- `static/js/admin.js:648`
- `static/js/admin.js:651`
- `static/js/admin.js:655`
- `static/js/admin.js:680`
- `static/js/admin.js:769`
- `static/js/admin.js:769`
- `static/js/admin.js:771`
- `static/js/admin.js:773`
- `static/js/admin.js:777`
- `static/js/admin.js:777`
- `static/js/admin.js:836`
- `static/js/admin.js:836`
- `static/js/admin.js:838`
- `static/js/admin.js:840`
- `static/js/admin.js:841`
- `static/js/admin.js:915`
- `static/js/admin.js:1072`
- `static/js/admin.js:1073`
- `static/js/admin.js:1077`
- `static/js/admin.js:1077`
- `static/js/admin.js:1078`
- `static/js/admin.js:1078`
- `static/js/admin.js:1080`
- `static/js/admin.js:1094`
- `static/js/admin.js:1094`
- `static/js/admin.js:1094`
- `static/js/admin.js:1097`
- `static/js/admin.js:1097`
- `static/js/admin.js:1099`
- `static/js/admin.js:1099`
- `static/js/admin.js:1099`
- `static/js/admin.js:1380`
- `static/js/admin.js:1385`
- `static/js/admin.js:1428`
- `static/js/admin.js:1428`
- `static/js/admin.js:1430`
- `static/js/admin.js:1432`
- `static/js/admin.js:1436`
- `static/js/admin.js:1436`
- `static/js/admin.js:1551`
- `static/js/admin.js:1554`
- `static/js/admin.js:1557`
- `static/js/admin.js:1557`
- `static/js/admin.js:1915`
- `static/js/admin.js:2802`
- … +576 more (grep the name in repo)

## `restoreThinkTags` — function, line 560
- **called from:**
- `static/js/chat.js:4405`
- `static/js/markdown.js:560`
- `static/js/markdown.js:748`
- `static/js/markdown.js:749`

## `hasUnclosedThinkTag` — function, line 566
- **called from:**
- `static/js/chat.js:4511`
- `static/js/markdown.js:566`
- `static/js/markdown.js:707`

## `startsWithReasoningPrefix` — function, line 577
- **called from:**
- `static/js/chat.js:4912`
- `static/js/chat.js:6186`
- `static/js/liveThinkingThrottle.js:105`
- `static/js/markdown.js:577`
- `static/js/markdown.js:609`

## `normalizeThinkingMarkup` — function, line 581
- **called from:**
- `static/js/chat.js:1621`
- `static/js/chat.js:3704`
- `static/js/chat.js:4144`
- `static/js/chat.js:4152`
- `static/js/chat.js:4368`
- `static/js/chat.js:4399`
- `static/js/chat.js:4442`
- `static/js/chat.js:4452`
- `static/js/chat.js:4895`
- `static/js/chat.js:7363`
- `static/js/chat.js:9263`
- `static/js/chatRenderer.js:3245`
- `static/js/markdown.js:567`
- `static/js/markdown.js:581`
- `static/js/markdown.js:605`

## `normalizePlainThinking` — function, line 603
- **called from:**
- `static/js/markdown.js:603`
- `static/js/markdown.js:667`

## `extractThinkingBlocks` — function, line 663
- **called from:**
- `static/js/chat.js:4154`
- `static/js/chat.js:4456`
- `static/js/chat.js:6170`
- `static/js/chat.js:6259`
- `static/js/chatRenderer.js:1584`
- `static/js/chatRenderer.js:3245`
- `static/js/chatRenderer.js:3301`
- `static/js/chatRenderer.js:3651`
- `static/js/markdown.js:663`
- `static/js/markdown.js:885`

## `createThinkingSection` — function, line 757
- **called from:**
- `static/js/markdown.js:757`
- `static/js/markdown.js:894`

## `createTaskCompletedMarker` — function, line 780
- **called from:**
- `static/js/markdown.js:780`
- `static/js/markdown.js:899`
- `static/js/markdown.js:903`

## `_emojiCodepoints` — function, line 802
- **called from:**
- `static/js/markdown.js:802`
- `static/js/markdown.js:810`

## `_emojiImg` — function, line 809
- **called from:**
- `static/js/markdown.js:809`
- `static/js/markdown.js:822`

## `_svgifyText` — function, line 818
- **called from:**
- `static/js/markdown.js:818`
- `static/js/markdown.js:858`

## `_useSvgEmoji` — function, line 827
- **called from:**
- `static/js/markdown.js:827`
- `static/js/markdown.js:837`
- `static/js/markdown.js:906`
- `static/js/markdown.js:1558`

## `svgifyEmoji` — function, line 836
- **called from:**
- `static/js/chatRenderer.js:2974`
- `static/js/chatRenderer.js:3050`
- `static/js/markdown.js:836`
- `static/js/markdown.js:906`
- `static/js/markdown.js:1558`

## `createCollapsible` — function, line 869
- **called from:**
- `static/js/chatRenderer.js:3524`
- `static/js/markdown.js:869`

## `processWithThinking` — function, line 884
- **called from:**
- `static/js/chat.js:1600`
- `static/js/chat.js:2588`
- `static/js/chat.js:3704`
- `static/js/chat.js:4378`
- `static/js/chat.js:4543`
- `static/js/chat.js:6227`
- `static/js/chat.js:6263`
- `static/js/chat.js:6378`
- `static/js/chat.js:7369`
- `static/js/chat.js:8771`
- `static/js/chat.js:8926`
- `static/js/chat.js:9134`
- `static/js/chat.js:9245`
- `static/js/chat.js:9281`
- `static/js/chatRenderer.js:352`
- `static/js/chatRenderer.js:3380`
- `static/js/chatRenderer.js:3653`
- `static/js/chatRenderer.js:3692`
- `static/js/chatRenderer.js:3762`
- `static/js/compare/stream.js:324`
- `static/js/compare/stream.js:414`
- `static/js/compare/stream.js:559`
- `static/js/compare/stream.js:698`
- `static/js/compare/stream.js:864`
- `static/js/group.js:886`
- `static/js/group.js:902`
- `static/js/group.js:951`
- `static/js/markdown.js:884`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2819`

## `_listItem` — function, line 915
- **called from:**
- `static/js/markdown.js:915`
- `static/js/markdown.js:951`
- `static/js/markdown.js:956`
- `static/js/markdown.js:988`

## `_listItemHtml` — function, line 926
- **called from:**
- `static/js/markdown.js:926`
- `static/js/markdown.js:977`

## `_collectList` — function, line 938
- **called from:**
- `static/js/markdown.js:938`
- `static/js/markdown.js:971`
- `static/js/markdown.js:990`

## `_buildNestedLists` — function, line 983
- **called from:**
- `static/js/markdown.js:983`
- `static/js/markdown.js:1488`

## `_buildNestedQuotes` — function, line 997
- **called from:**
- `static/js/markdown.js:997`
- `static/js/markdown.js:1497`

## `svgThemeCss` — function, line 1034
- **called from:**
- `static/js/markdown.js:1034`
- `static/js/markdown.js:1107`

## `safeColor` — arrow, line 1059
- **called from:**
- `static/js/markdown.js:1069`

## `renderSvgSandbox` — function, line 1073
- **called from:**
- `static/js/markdown.js:1073`
- `static/js/markdown.js:1194`
- `static/js/markdown.js:1269`

## `decodeSvgTitleEntities` — arrow, line 1082
- **called from:**
- `static/js/markdown.js:1103`

## `replaceRawSvgBlocks` — function, line 1111
- **called from:**
- `static/js/markdown.js:1111`
- `static/js/markdown.js:1267`

## `isTagBoundary` — arrow, line 1117
- **called from:**
- `static/js/markdown.js:1120`
- `static/js/markdown.js:1133`
- `static/js/markdown.js:1144`

## `mdToHtml` — function, line 1167
- **called from:**
- `static/js/chat.js:1626`
- `static/js/chat.js:4228`
- `static/js/chat.js:4495`
- `static/js/chat.js:6207`
- `static/js/chat.js:7370`
- `static/js/document.js:3605`
- `static/js/document.js:3628`
- `static/js/document.js:15395`
- `static/js/document.js:15484`
- `static/js/document.js:16170`
- `static/js/documentLibrary.js:2217`
- `static/js/documentLibrary.js:3030`
- `static/js/markdown.js:115`
- `static/js/markdown.js:773`
- `static/js/markdown.js:880`
- `static/js/markdown.js:902`
- `static/js/markdown.js:1167`
- `static/js/markdown.js:1619`
- `static/js/markdown.js:1620`
- `static/js/markdown.js:1745`
- `static/js/tasks.js:2569`

## `pushMath` — arrow, line 1384
- **called from:**
- `static/js/markdown.js:1401`
- `static/js/markdown.js:1406`
- `static/js/markdown.js:1413`
- `static/js/markdown.js:1422`

## `squashOutsideCode` — function, line 1564
- **called from:**
- `static/js/chat.js:1600`
- `static/js/chat.js:1626`
- `static/js/chat.js:2589`
- `static/js/chat.js:3704`
- `static/js/chat.js:4378`
- `static/js/chat.js:4495`
- `static/js/chat.js:4543`
- `static/js/chat.js:6207`
- `static/js/chat.js:6227`
- `static/js/chat.js:6379`
- `static/js/chat.js:7367`
- `static/js/chat.js:8772`
- `static/js/chat.js:8927`
- `static/js/chat.js:9134`
- `static/js/chat.js:9246`
- `static/js/chat.js:9282`
- `static/js/chatRenderer.js:3380`
- `static/js/chatRenderer.js:3583`
- `static/js/chatRenderer.js:3762`
- `static/js/compare/stream.js:325`
- `static/js/compare/stream.js:415`
- `static/js/compare/stream.js:560`
- `static/js/compare/stream.js:699`
- `static/js/compare/stream.js:865`
- `static/js/group.js:887`
- `static/js/group.js:903`
- `static/js/group.js:952`
- `static/js/markdown.js:1564`
- `static/js/slashCommands.js:453`
- `static/js/tasks.js:2819`

## `renderContent` — function, line 1585
- **called from:**
- `static/js/chatRenderer.js:3223`
- `static/js/chatRenderer.js:3226`
- `static/js/markdown.js:1585`
- `static/js/research/panel.js:1643`

## `renderMermaid` — function, line 1601
- **called from:**
- `static/js/chat.js:6280`
- `static/js/chatRenderer.js:3481`
- `static/js/chatRenderer.js:3866`
- `static/js/document.js:16178`
- `static/js/group.js:955`
- `static/js/markdown.js:1601`
- `static/js/slashCommands.js:454`

## `renderMath` — function, line 1622
- **called from:**
- `static/js/document.js:15513`
- `static/js/markdown.js:22`
- `static/js/markdown.js:129`
- `static/js/markdown.js:1381`
- `static/js/markdown.js:1622`

## `_loadExpandedSet` — function, line 1675
- **called from:**
- `static/js/markdown.js:1675`
- `static/js/markdown.js:1772`
- `static/js/markdown.js:1789`

## `_saveExpandedSet` — function, line 1679
- **called from:**
- `static/js/markdown.js:1679`
- `static/js/markdown.js:1775`

## `_hashThinkingContent` — function, line 1687
- **called from:**
- `static/js/markdown.js:1687`
- `static/js/markdown.js:1770`
- `static/js/markdown.js:1795`

## `_setThinkingExpanded` — function, line 1697
- **called from:**
- `static/js/markdown.js:1697`
- `static/js/markdown.js:1767`
- `static/js/markdown.js:1800`

## `_watchThinking` — function, line 1780
- **called from:**
- `static/js/markdown.js:1780`

## `_apply` — arrow, line 1783
- **called from:**
- `static/js/markdown.js:1806`
- `static/js/markdown.js:1810`
- `static/js/theme.js:775`

## `start` — arrow, line 1803
- **called from:**
- `app.py:1410`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `mcp_servers/email_server.py:2023`
- `routes/auth_routes.py:895`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:1714`
- `routes/chat_helpers.py:1777`
- `routes/chat_helpers.py:1778`
- `routes/chat_helpers.py:1779`
- `routes/chat_routes.py:5541`
- `routes/cookbook_routes.py:3584`
- `routes/email/email_helpers.py:399`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1596`
- `routes/email/email_routes.py:1898`
- `routes/model_routes.py:1666`
- `scripts/add_hwfit_models.py:117`
- `scripts/css_snapshot.py:211`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:411`
- `services/search/core.py:800`
- `services/skills/evaluation.py:463`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:245`
- `src/agent_evidence.py:308`
- `src/agent_loop.py:1143`
- `src/agent_loop.py:2639`
- `src/agent_loop.py:2644`
- `src/agent_loop.py:2652`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:3180`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9169`
- `src/agent_loop.py:12041`
- `src/agent_loop.py:12044`
- `src/agent_loop.py:14160`
- `src/agent_loop.py:14164`
- `src/agent_runtime/completion.py:90`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:94`
- `src/agent_tools/document_tools.py:240`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:431`
- `src/agent_tools/document_tools.py:729`
- `src/agent_tools/document_tools.py:734`
- `src/agent_tools/document_tools.py:898`
- `src/agent_tools/filesystem_tools.py:1153`
- `src/agent_tools/filesystem_tools.py:1154`
- `src/agent_tools/filesystem_tools.py:1266`
- `src/agent_tools/web_tools.py:954`
- `src/agent_tools/web_tools.py:975`
- `src/agent_tools/web_tools.py:978`
- `src/agent_tools/web_tools_prewave3.py:958`
- … +213 more (grep the name in repo)

## `_endpointNameFromUrl` — function, line 1822
- **called from:**
- `static/js/markdown.js:1822`
- `static/js/markdown.js:1872`
- `static/js/markdown.js:1880`
- `static/js/markdown.js:1901`

## `_appendEndpointAddButtons` — function, line 1831
- **called from:**
- `static/js/markdown.js:1831`
- `static/js/markdown.js:1924`
- `static/js/markdown.js:1928`

## `_registerEndpointFromButton` — function, line 1853
- **called from:**
- `static/js/markdown.js:1853`
- `static/js/markdown.js:1918`

## `_watchModelEndpointLinks` — function, line 1909
- **called from:**
- `static/js/markdown.js:1909`

## `start` — arrow, line 1921
- **called from:**
- `app.py:1410`
- `launcher.py:73`
- `launcher.py:145`
- `launcher.py:147`
- `mcp_servers/email_server.py:2023`
- `routes/auth_routes.py:895`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:94`
- `routes/chat_helpers.py:1714`
- `routes/chat_helpers.py:1777`
- `routes/chat_helpers.py:1778`
- `routes/chat_helpers.py:1779`
- `routes/chat_routes.py:5541`
- `routes/cookbook_routes.py:3584`
- `routes/email/email_helpers.py:399`
- `routes/email/email_routes.py:1130`
- `routes/email/email_routes.py:1596`
- `routes/email/email_routes.py:1898`
- `routes/model_routes.py:1666`
- `scripts/add_hwfit_models.py:117`
- `scripts/css_snapshot.py:211`
- `services/hwfit/hf_discovery.py:115`
- `services/search/core.py:411`
- `services/search/core.py:800`
- `services/skills/evaluation.py:463`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:225`
- `src/agent_evidence.py:245`
- `src/agent_evidence.py:308`
- `src/agent_loop.py:1143`
- `src/agent_loop.py:2639`
- `src/agent_loop.py:2644`
- `src/agent_loop.py:2652`
- `src/agent_loop.py:2653`
- `src/agent_loop.py:3180`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9123`
- `src/agent_loop.py:9169`
- `src/agent_loop.py:12041`
- `src/agent_loop.py:12044`
- `src/agent_loop.py:14160`
- `src/agent_loop.py:14164`
- `src/agent_runtime/completion.py:90`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:93`
- `src/agent_runtime/completion.py:94`
- `src/agent_tools/document_tools.py:240`
- `src/agent_tools/document_tools.py:384`
- `src/agent_tools/document_tools.py:431`
- `src/agent_tools/document_tools.py:729`
- `src/agent_tools/document_tools.py:734`
- `src/agent_tools/document_tools.py:898`
- `src/agent_tools/filesystem_tools.py:1153`
- `src/agent_tools/filesystem_tools.py:1154`
- `src/agent_tools/filesystem_tools.py:1266`
- `src/agent_tools/web_tools.py:954`
- `src/agent_tools/web_tools.py:975`
- `src/agent_tools/web_tools.py:978`
- `src/agent_tools/web_tools_prewave3.py:958`
- … +213 more (grep the name in repo)
