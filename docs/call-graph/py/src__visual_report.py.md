# `src/visual_report.py` — definitions & call sites

25 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_autolink_urls` — function, line 57
- **called from:**
- `src/visual_report.py:81`
- `tests/test_visual_report_nonstring.py:11`
- `tests/test_visual_report_nonstring.py:17`

## `_md_to_html` — function, line 72
- **called from:**
- `src/visual_report.py:2771`
- `tests/test_security_regressions.py:1230`
- `tests/test_security_regressions.py:1248`
- `tests/test_visual_report_math.py:17`
- `tests/test_visual_report_math.py:31`
- `tests/test_visual_report_math.py:37`
- `tests/test_visual_report_math.py:43`
- `tests/test_visual_report_math.py:49`
- `tests/test_visual_report_math.py:73`

## `_extract_headings` — function, line 107
- **called from:**
- `src/visual_report.py:2773`
- `tests/test_visual_report_nonstring.py:12`
- `tests/test_visual_report_nonstring.py:13`
- `tests/test_visual_report_nonstring.py:18`
- `tests/test_visual_report_slug_unique.py:14`
- `tests/test_visual_report_toc_code_fence.py:17`
- `tests/test_visual_report_toc_code_fence.py:22`
- `tests/test_visual_report_toc_code_fence.py:27`

## `_plain_heading_text` — function, line 121
- **called from:**
- `src/visual_report.py:152`
- `src/visual_report.py:158`

## `_make_slug` — function, line 131
- **called from:**
- `src/visual_report.py:155`
- `src/visual_report.py:160`

## `_apply_heading_ids` — function, line 164
- **called from:**
- `src/visual_report.py:2774`

## `_wrap_report_sections` — function, line 202
- **called from:**
- `src/visual_report.py:2841`

## `_extract_research_trace` — function, line 220
- **called from:**
- `src/visual_report.py:2844`

## `_inject_images` — function, line 241
- **called from:**
- `src/visual_report.py:2843`

## `_source_evidence_summary` — function, line 291
- **called from:**
- `src/visual_report.py:2908`
- `tests/test_visual_report.py:60`

## `_standard_visual_variant` — function, line 1853
- **called from:**
- `src/visual_report.py:2995`
- `tests/test_visual_research_mode.py:64`
- `tests/test_visual_research_mode.py:65`

## `_category_css` — function, line 1858
- **called from:**
- `src/visual_report.py:3051`

## `_extract_report_title` — function, line 2450
- **called from:**
- `src/visual_report.py:2754`

## `_is_icon_or_logo_url` — function, line 2483
- **called from:**
- `src/visual_report.py:2795`
- `tests/test_visual_report_icon_url.py:14`
- `tests/test_visual_report_icon_url.py:15`
- `tests/test_visual_report_icon_url.py:16`
- `tests/test_visual_report_icon_url.py:20`
- `tests/test_visual_report_icon_url.py:21`
- `tests/test_visual_report_icon_url.py:22`
- `tests/test_visual_report_icon_url.py:23`
- `tests/test_visual_report_icon_url.py:24`
- `tests/test_visual_report_icon_url.py:28`
- `tests/test_visual_report_icon_url.py:29`

## `_sanitize_visual_html` — function, line 2506
- **called from:**
- `src/visual_report.py:2550`

## `_extract_visual_html` — function, line 2543
- **called from:**
- `src/visual_report.py:2766`

## `replace` — function, line 2547
- **called from:**
- `app.py:1066`
- `app.py:1074`
- `core/atomic_io.py:78`
- `core/atomic_io.py:99`
- `core/database.py:25`
- `core/database.py:948`
- `core/database.py:989`
- `core/database.py:1011`
- `core/database.py:1033`
- `core/database.py:1054`
- `core/database.py:1079`
- `core/database.py:1103`
- `core/database.py:1127`
- `core/database.py:1150`
- `core/database.py:1180`
- `core/database.py:1205`
- `core/database.py:1230`
- `core/database.py:1253`
- `core/database.py:1281`
- `core/database.py:1304`
- `core/database.py:1328`
- `core/database.py:1352`
- `core/database.py:1374`
- `core/database.py:1417`
- `core/database.py:1449`
- `core/database.py:1472`
- `core/database.py:1495`
- `core/database.py:1531`
- `core/database.py:1555`
- `core/database.py:1578`
- `core/database.py:1614`
- `core/database.py:1642`
- `core/database.py:1676`
- `core/database.py:1697`
- `core/database.py:2543`
- `core/database.py:2674`
- `core/database.py:2797`
- `core/database.py:2823`
- `core/database.py:2849`
- `core/database.py:2874`
- `core/database.py:2899`
- `core/database.py:2926`
- `core/database.py:2947`
- `core/database.py:3042`
- `core/platform_compat.py:344`
- `core/session_manager.py:77`
- `core/session_manager.py:78`
- `core/session_manager.py:746`
- `core/session_manager.py:749`
- `core/session_manager.py:1146`
- `mcp_servers/email_server.py:53`
- `mcp_servers/email_server.py:53`
- `mcp_servers/email_server.py:1148`
- `mcp_servers/email_server.py:1402`
- `mcp_servers/email_server.py:1461`
- `mcp_servers/email_server.py:1465`
- `mcp_servers/email_server.py:1764`
- `mcp_servers/email_server.py:1768`
- `mcp_servers/email_server.py:1902`
- `mcp_servers/email_server.py:2086`
- … +1611 more (grep the name in repo)

## `_diagram_text_lines` — function, line 2572
- **called from:**
- `src/visual_report.py:2688`
- `src/visual_report.py:2698`
- `src/visual_report.py:2699`

## `_svg_text` — function, line 2597
- **called from:**
- `src/visual_report.py:2688`
- `src/visual_report.py:2698`
- `src/visual_report.py:2699`

## `_render_visual_diagram` — function, line 2607
- **called from:**
- `src/visual_report.py:2726`

## `_extract_visual_diagrams` — function, line 2715
- **called from:**
- `src/visual_report.py:2770`

## `replace` — function, line 2719
- **called from:**
- `app.py:1066`
- `app.py:1074`
- `core/atomic_io.py:78`
- `core/atomic_io.py:99`
- `core/database.py:25`
- `core/database.py:948`
- `core/database.py:989`
- `core/database.py:1011`
- `core/database.py:1033`
- `core/database.py:1054`
- `core/database.py:1079`
- `core/database.py:1103`
- `core/database.py:1127`
- `core/database.py:1150`
- `core/database.py:1180`
- `core/database.py:1205`
- `core/database.py:1230`
- `core/database.py:1253`
- `core/database.py:1281`
- `core/database.py:1304`
- `core/database.py:1328`
- `core/database.py:1352`
- `core/database.py:1374`
- `core/database.py:1417`
- `core/database.py:1449`
- `core/database.py:1472`
- `core/database.py:1495`
- `core/database.py:1531`
- `core/database.py:1555`
- `core/database.py:1578`
- `core/database.py:1614`
- `core/database.py:1642`
- `core/database.py:1676`
- `core/database.py:1697`
- `core/database.py:2543`
- `core/database.py:2674`
- `core/database.py:2797`
- `core/database.py:2823`
- `core/database.py:2849`
- `core/database.py:2874`
- `core/database.py:2899`
- `core/database.py:2926`
- `core/database.py:2947`
- `core/database.py:3042`
- `core/platform_compat.py:344`
- `core/session_manager.py:77`
- `core/session_manager.py:78`
- `core/session_manager.py:746`
- `core/session_manager.py:749`
- `core/session_manager.py:1146`
- `mcp_servers/email_server.py:53`
- `mcp_servers/email_server.py:53`
- `mcp_servers/email_server.py:1148`
- `mcp_servers/email_server.py:1402`
- `mcp_servers/email_server.py:1461`
- `mcp_servers/email_server.py:1465`
- `mcp_servers/email_server.py:1764`
- `mcp_servers/email_server.py:1768`
- `mcp_servers/email_server.py:1902`
- `mcp_servers/email_server.py:2086`
- … +1611 more (grep the name in repo)

## `generate_visual_report` — function, line 2736
- **called from:**
- `routes/document/document_routes.py:688`
- `src/research_handler.py:888`
- `tests/test_security_regressions.py:1265`
- `tests/test_security_regressions.py:1276`
- `tests/test_visual_report.py:19`
- `tests/test_visual_report.py:71`
- `tests/test_visual_report.py:91`
- `tests/test_visual_report.py:111`
- `tests/test_visual_report.py:157`
- `tests/test_visual_report.py:180`
- `tests/test_visual_report.py:210`
- `tests/test_visual_report.py:251`
- `tests/test_visual_report.py:285`
- `tests/test_visual_report.py:312`
- `tests/test_visual_report.py:313`
- `tests/test_visual_report_math.py:60`
- `tests/test_visual_report_math_browser.py:27`
- `tests/test_visual_report_mobile_toolbar.py:21`

## `_json_for_script` — function, line 3061
- **called from:**
- `src/visual_report.py:3057`
- `src/visual_report.py:3073`

## `json_dumps_str` — function, line 3071
- **called from:**
- `src/visual_report.py:3056`
