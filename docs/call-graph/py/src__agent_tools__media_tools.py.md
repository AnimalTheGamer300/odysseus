# `src/agent_tools/media_tools.py` — definitions & call sites

24 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_video_encode_args` — function, line 28
- **called from:**
- `src/agent_tools/media_tools.py:1777`
- `src/agent_tools/media_tools.py:1782`

## `_parse_seconds` — function, line 71
- **called from:**
- `src/agent_tools/media_tools.py:130`
- `src/agent_tools/media_tools.py:1092`
- `src/agent_tools/media_tools.py:2180`
- `src/agent_tools/media_tools.py:2182`
- `tests/test_inspect_media_tool.py:47`
- `tests/test_inspect_media_tool.py:48`
- `tests/test_inspect_media_tool.py:49`
- `tests/test_inspect_media_tool.py:50`
- `tests/test_inspect_media_tool.py:51`
- `tests/test_inspect_media_tool.py:55`

## `_parse_video_position` — function, line 111
- **called from:**
- `src/agent_tools/media_tools.py:1088`
- `src/agent_tools/media_tools.py:1098`
- `src/agent_tools/media_tools.py:1320`
- `src/agent_tools/media_tools.py:1323`
- `src/agent_tools/media_tools.py:1374`
- `src/agent_tools/media_tools.py:1377`
- `src/agent_tools/media_tools.py:1436`
- `src/agent_tools/media_tools.py:1673`
- `src/agent_tools/media_tools.py:1883`
- `tests/test_inspect_media_percent_ranges.py:14`
- `tests/test_inspect_media_percent_ranges.py:15`
- `tests/test_inspect_media_percent_ranges.py:18`
- `tests/test_inspect_media_tool.py:56`
- `tests/test_inspect_media_tool.py:57`
- `tests/test_inspect_media_tool.py:58`

## `_format_seconds` — function, line 133
- **called from:**
- `src/agent_tools/media_tools.py:391`
- `src/agent_tools/media_tools.py:1113`
- `src/agent_tools/media_tools.py:1114`
- `src/agent_tools/media_tools.py:1115`
- `src/agent_tools/media_tools.py:1333`
- `src/agent_tools/media_tools.py:1334`
- `src/agent_tools/media_tools.py:1335`
- `src/agent_tools/media_tools.py:1442`
- `src/agent_tools/media_tools.py:1443`
- `src/agent_tools/media_tools.py:1529`
- `src/agent_tools/media_tools.py:1825`
- `src/agent_tools/media_tools.py:1826`
- `src/agent_tools/media_tools.py:1829`
- `src/agent_tools/media_tools.py:1830`
- `src/agent_tools/media_tools.py:1833`
- `src/agent_tools/media_tools.py:1858`
- `src/agent_tools/media_tools.py:1860`
- `src/agent_tools/media_tools.py:2028`
- `src/agent_tools/media_tools.py:2030`
- `src/agent_tools/media_tools.py:2030`
- `src/agent_tools/media_tools.py:2075`
- `src/agent_tools/media_tools.py:2080`
- `src/agent_tools/media_tools.py:2084`
- `src/agent_tools/media_tools.py:2084`
- `src/agent_tools/media_tools.py:2090`
- `src/agent_tools/media_tools.py:2090`
- `src/agent_tools/media_tools.py:2287`
- `src/agent_tools/media_tools.py:2287`

## `_resolve_workspace_path` — function, line 141
- **called from:**
- `src/agent_tools/media_tools.py:196`
- `src/agent_tools/media_tools.py:795`
- `src/agent_tools/media_tools.py:1431`
- `src/agent_tools/media_tools.py:1595`
- `src/agent_tools/media_tools.py:1817`
- `src/agent_tools/media_tools.py:2149`
- `src/agent_tools/web_tools.py:2578`
- `src/agent_tools/web_tools.py:2588`
- `src/agent_tools/web_tools_prewave3.py:2611`
- `src/agent_tools/web_tools_prewave3.py:2621`
- `src/agent_tools/web_tools_prewave3.py:2890`
- `tests/test_private_browser_tool.py:44`
- `tests/test_resource_identity.py:105`

## `_resolve_media_path` — function, line 195
- **called from:**
- `src/agent_tools/media_tools.py:461`
- `src/agent_tools/media_tools.py:772`
- `src/agent_tools/media_tools.py:2135`
- `tests/test_inspect_media_tool.py:855`

## `_run` — function, line 203
- **called from:**
- `services/hwfit/hardware.py:87`
- `services/hwfit/hardware.py:94`
- `services/hwfit/hardware.py:108`
- `services/hwfit/hardware.py:110`
- `services/hwfit/hardware.py:211`
- `services/hwfit/hardware.py:221`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:237`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:293`
- `services/hwfit/hardware.py:294`
- `services/hwfit/hardware.py:323`
- `services/hwfit/hardware.py:325`
- `services/hwfit/hardware.py:338`
- `services/hwfit/hardware.py:341`
- `services/hwfit/hardware.py:376`
- `services/hwfit/hardware.py:378`
- `services/hwfit/hardware.py:393`
- `services/hwfit/hardware.py:422`
- `services/hwfit/hardware.py:466`
- `services/hwfit/hardware.py:491`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:503`
- `services/hwfit/hardware.py:531`
- `services/hwfit/hardware.py:549`
- `services/hwfit/hardware.py:554`
- `services/hwfit/hardware.py:557`
- `services/hwfit/hardware.py:562`
- `services/hwfit/hardware.py:635`
- `services/research/research_handler.py:102`
- `services/search/providers.py:268`
- `services/search/providers.py:281`
- `services/search/providers.py:290`
- `services/search/providers.py:298`
- `src/research_handler.py:421`
- `tests/test_agent_evidence_loop.py:128`
- `tests/test_agent_evidence_loop.py:140`
- `tests/test_agent_evidence_loop.py:152`
- `tests/test_agent_evidence_loop.py:163`
- `tests/test_agent_evidence_loop.py:189`
- `tests/test_agent_evidence_loop.py:222`
- `tests/test_agent_evidence_loop.py:262`
- `tests/test_agent_evidence_loop.py:304`
- `tests/test_agent_evidence_loop.py:356`
- `tests/test_agent_evidence_loop.py:399`
- `tests/test_agent_evidence_loop.py:439`
- `tests/test_agent_evidence_loop.py:461`
- `tests/test_agent_evidence_loop.py:627`
- `tests/test_agent_evidence_loop.py:649`
- `tests/test_agent_evidence_loop.py:677`
- `tests/test_agent_evidence_loop.py:715`
- `tests/test_agent_rounds_exhausted.py:24`
- `tests/test_agent_runtime_context.py:28`
- `tests/test_app_config_shared_fetch_js.py:89`
- `tests/test_app_config_shared_fetch_js.py:107`
- `tests/test_app_config_shared_fetch_js.py:125`
- `tests/test_app_config_shared_fetch_js.py:144`
- `tests/test_app_config_shared_fetch_js.py:163`
- `tests/test_app_config_shared_fetch_js.py:188`
- `tests/test_app_config_shared_fetch_js.py:277`
- … +208 more (grep the name in repo)

## `_run_video_probe` — function (async), line 213
- **called from:**
- `src/agent_tools/media_tools.py:1054`
- `src/agent_tools/media_tools.py:1065`
- `src/agent_tools/media_tools.py:2221`

## `_scene_change_timestamps` — function (async), line 221
- **called from:**
- `src/agent_tools/media_tools.py:1930`

## `_motion_score_timestamps` — function (async), line 250
- **called from:**
- `src/agent_tools/media_tools.py:1940`

## `_bounded_scene_sample` — function, line 288
- **called from:**
- `src/agent_tools/media_tools.py:1933`

## `_bounded_motion_sample` — function, line 328
- **called from:**
- `src/agent_tools/media_tools.py:1943`

## `_pack_overview_contact_sheets` — function, line 362
- **called from:**
- `src/agent_tools/media_tools.py:2021`

## `_model_frame_dimension` — function, line 404
- **called from:**
- `src/agent_tools/media_tools.py:877`
- `src/agent_tools/media_tools.py:1122`

## `ExtractTextTool` — class, line 424
- **called from:**
- `src/agent_tools/__init__.py:50`
- `src/agent_tools/media_tools.py:917`
- `tests/test_extract_text_tool.py:35`
- `tests/test_extract_text_tool.py:36`
- `tests/test_extract_text_tool.py:37`
- `tests/test_extract_text_tool.py:38`
- `tests/test_extract_text_tool.py:39`
- `tests/test_extract_text_tool.py:64`
- `tests/test_extract_text_tool.py:65`
- `tests/test_extract_text_tool.py:79`
- `tests/test_extract_text_tool.py:82`
- `tests/test_extract_text_tool.py:111`

## `ExtractTextTool.execute` — method (async), line 427
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

## `ExtractTextTool._extract_pdf_pages` — method, line 477
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `InspectMediaTool` — class, line 531
- **called from:**
- `src/agent_tools/__init__.py:49`
- `tests/test_extract_text_tool.py:133`
- `tests/test_extract_text_tool.py:134`
- `tests/test_inspect_media_percent_ranges.py:33`
- `tests/test_inspect_media_probe_recovery.py:55`
- `tests/test_inspect_media_tool.py:82`
- `tests/test_inspect_media_tool.py:104`
- `tests/test_inspect_media_tool.py:111`
- `tests/test_inspect_media_tool.py:131`
- `tests/test_inspect_media_tool.py:138`
- `tests/test_inspect_media_tool.py:155`
- `tests/test_inspect_media_tool.py:159`
- `tests/test_inspect_media_tool.py:184`
- `tests/test_inspect_media_tool.py:205`
- `tests/test_inspect_media_tool.py:212`
- `tests/test_inspect_media_tool.py:232`
- `tests/test_inspect_media_tool.py:260`
- `tests/test_inspect_media_tool.py:277`
- `tests/test_inspect_media_tool.py:298`
- `tests/test_inspect_media_tool.py:312`
- `tests/test_inspect_media_tool.py:325`
- `tests/test_inspect_media_tool.py:339`
- `tests/test_inspect_media_tool.py:354`
- `tests/test_inspect_media_tool.py:368`
- `tests/test_inspect_media_tool.py:383`
- `tests/test_inspect_media_tool.py:397`
- `tests/test_inspect_media_tool.py:410`
- `tests/test_inspect_media_tool.py:423`
- `tests/test_inspect_media_tool.py:437`
- `tests/test_inspect_media_tool.py:442`
- `tests/test_inspect_media_tool.py:447`
- `tests/test_inspect_media_tool.py:478`
- `tests/test_inspect_media_tool.py:483`
- `tests/test_inspect_media_tool.py:487`
- `tests/test_inspect_media_tool.py:514`
- `tests/test_inspect_media_tool.py:530`
- `tests/test_inspect_media_tool.py:562`
- `tests/test_inspect_media_tool.py:591`
- `tests/test_inspect_media_tool.py:614`
- `tests/test_inspect_media_tool.py:620`
- `tests/test_inspect_media_tool.py:649`
- `tests/test_inspect_media_tool.py:665`
- `tests/test_inspect_media_tool.py:689`
- `tests/test_inspect_media_tool.py:710`
- `tests/test_inspect_media_tool.py:715`
- `tests/test_inspect_media_tool.py:721`
- `tests/test_inspect_media_tool.py:726`
- `tests/test_inspect_media_tool.py:773`
- `tests/test_inspect_media_tool.py:796`
- `tests/test_inspect_media_tool.py:821`
- `tests/test_inspect_media_tool.py:839`
- `tests/test_inspect_media_tool.py:865`
- `tests/test_inspect_media_tool.py:885`
- `tests/test_inspect_media_tool.py:919`
- `tests/test_inspect_media_tool.py:943`
- `tests/test_inspect_media_tool.py:967`
- `tests/test_inspect_media_tool.py:994`
- `tests/test_inspect_media_tool.py:1015`
- `tests/test_inspect_media_tool.py:1041`
- `tests/test_inspect_media_tool.py:1066`
- … +25 more (grep the name in repo)

## `InspectMediaTool.execute` — method (async), line 534
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

## `InspectMediaTool._render_template` — method, line 1395
- **called from:**
- `src/agent_tools/media_tools.py:1410`

## `TranscribeMediaTool` — class, line 2124
- **called from:**
- `src/agent_tools/__init__.py:51`
- `tests/test_inspect_media_tool.py:1689`
- `tests/test_inspect_media_tool.py:1729`
- `tests/test_inspect_media_tool.py:1762`
- `tests/test_inspect_media_tool.py:1797`
- `tests/test_inspect_media_tool.py:1848`
- `tests/test_inspect_media_tool.py:1867`
- `tests/test_inspect_media_tool.py:1883`
- `tests/test_inspect_media_tool.py:1928`
- `tests/test_inspect_media_tool.py:1931`
- `tests/test_inspect_media_tool.py:1959`

## `TranscribeMediaTool.execute` — method (async), line 2127
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

## `TranscribeMediaTool._transcribe` — method, line 2251
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `TranscribeMediaTool._subtitle_time` — method, line 2309
- **called from:**
- `src/agent_tools/media_tools.py:2318`
- `src/agent_tools/media_tools.py:2318`
