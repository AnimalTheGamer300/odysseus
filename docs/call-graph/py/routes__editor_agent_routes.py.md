# `routes/editor_agent_routes.py` — definitions & call sites

63 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_normalize_ai_step` — function, line 143
- **called from:**
- `routes/editor_agent_routes.py:259`

## `_normalize_ask_user` — function, line 199
- **called from:**
- `routes/editor_agent_routes.py:238`
- `routes/editor_agent_routes.py:250`

## `_validate_plan` — function, line 227
- **called from:**
- `routes/editor_agent_routes.py:1216`
- `tests/test_agent_editor_routes.py:1723`
- `tests/test_agent_editor_routes.py:1728`
- `tests/test_agent_editor_routes.py:1737`
- `tests/test_agent_editor_routes.py:1742`
- `tests/test_agent_editor_routes.py:1746`
- `tests/test_agent_editor_routes.py:1751`
- `tests/test_agent_editor_routes.py:1756`
- `tests/test_agent_editor_routes.py:1763`
- `tests/test_agent_editor_routes.py:1767`
- `tests/test_agent_editor_routes.py:1768`
- `tests/test_agent_editor_routes.py:1769`
- `tests/test_agent_editor_routes.py:1773`
- `tests/test_agent_editor_routes.py:1777`
- `tests/test_agent_editor_routes.py:1781`

## `_is_text_request` — function, line 381
- **called from:**
- `routes/editor_agent_routes.py:417`
- `routes/editor_agent_routes.py:838`
- `routes/editor_agent_routes.py:938`
- `routes/editor_agent_routes.py:1075`
- `routes/editor_agent_routes.py:1077`

## `_format_target` — function, line 385
- **called from:**
- `routes/editor_agent_routes.py:417`
- `routes/editor_agent_routes.py:805`
- `routes/editor_agent_routes.py:924`
- `routes/editor_agent_routes.py:928`

## `_extend_requested` — function, line 398
- **called from:**
- `routes/editor_agent_routes.py:813`
- `routes/editor_agent_routes.py:931`

## `_generative_kind` — function, line 406
- **called from:**
- `routes/editor_agent_routes.py:703`
- `routes/editor_agent_routes.py:1168`
- `routes/editor_agent_routes.py:1176`
- `routes/editor_agent_routes.py:1765`
- `tests/test_agent_editor_routes.py:500`
- `tests/test_agent_editor_routes.py:515`
- `tests/test_agent_editor_routes.py:1621`
- `tests/test_agent_editor_routes.py:1643`
- `tests/test_agent_editor_routes.py:1644`
- `tests/test_editor_planner_routing.py:141`
- `tests/test_editor_planner_routing.py:145`
- `tests/test_photo_editor_family.py:244`
- `tests/test_photo_editor_family.py:245`
- `tests/test_photo_editor_family.py:246`
- `tests/test_photo_editor_family.py:247`
- `tests/test_photo_editor_family.py:248`
- `tests/test_photo_editor_family.py:249`
- `tests/test_photo_editor_family.py:251`
- `tests/test_photo_editor_family.py:252`
- `tests/test_photo_editor_family.py:253`
- `tests/test_photo_editor_family.py:254`
- `tests/test_photo_editor_family.py:255`
- `tests/test_photo_editor_style_guide.py:320`
- `tests/test_photo_editor_style_guide.py:347`
- `tests/test_photo_editor_style_guide.py:348`

## `_is_new_image_request` — function, line 467
- **called from:**
- `routes/editor_agent_routes.py:421`
- `routes/editor_agent_routes.py:441`
- `routes/editor_agent_routes.py:620`
- `tests/test_editor_planner_routing.py:142`
- `tests/test_editor_planner_routing.py:144`

## `_instruction_prompt` — function, line 474
- **called from:**
- `routes/editor_agent_routes.py:497`
- `routes/editor_agent_routes.py:627`
- `routes/editor_agent_routes.py:638`

## `_restyle_prompt` — function, line 487
- **called from:**
- `routes/editor_agent_routes.py:615`

## `_generative_mode` — function, line 500
- **called from:**
- `routes/editor_agent_routes.py:631`
- `routes/editor_agent_routes.py:670`
- `tests/test_agent_editor_routes.py:476`
- `tests/test_photo_editor_family.py:274`
- `tests/test_photo_editor_family.py:276`
- `tests/test_photo_editor_family.py:277`
- `tests/test_photo_editor_family.py:278`

## `_removal_prompt` — function, line 513
- **called from:**
- `routes/editor_agent_routes.py:635`

## `_scene_prompt` — function, line 575
- **called from:**
- `routes/editor_agent_routes.py:637`

## `_generative_step` — function, line 608
- **called from:**
- `routes/editor_agent_routes.py:687`
- `tests/test_agent_editor_routes.py:519`
- `tests/test_agent_editor_routes.py:529`
- `tests/test_agent_editor_routes.py:533`
- `tests/test_photo_editor_family.py:261`
- `tests/test_photo_editor_family.py:262`
- `tests/test_photo_editor_family.py:264`
- `tests/test_photo_editor_family.py:265`
- `tests/test_photo_editor_family.py:267`

## `_selection_step_for` — function, line 661
- **called from:**
- `routes/editor_agent_routes.py:684`

## `_generative_steps` — function, line 681
- **called from:**
- `routes/editor_agent_routes.py:714`
- `routes/editor_agent_routes.py:719`
- `routes/editor_agent_routes.py:1183`
- `tests/test_agent_editor_routes.py:462`
- `tests/test_agent_editor_routes.py:467`
- `tests/test_agent_editor_routes.py:470`
- `tests/test_agent_editor_routes.py:473`
- `tests/test_agent_editor_routes.py:478`
- `tests/test_agent_editor_routes.py:685`
- `tests/test_agent_editor_routes.py:699`

## `_plan_uses_ai_content` — function, line 691
- **called from:**
- `routes/editor_agent_routes.py:718`
- `routes/editor_agent_routes.py:1511`
- `routes/editor_agent_routes.py:1829`
- `routes/editor_agent_routes.py:1832`

## `_ensure_generative` — function, line 695
- **called from:**
- `routes/editor_agent_routes.py:1493`
- `routes/editor_agent_routes.py:1779`
- `tests/test_agent_editor_routes.py:502`
- `tests/test_agent_editor_routes.py:712`
- `tests/test_photo_editor_family.py:285`
- `tests/test_photo_editor_family.py:291`
- `tests/test_photo_editor_family.py:295`

## `_image_provider_available` — function, line 723
- **called from:**
- `routes/editor_agent_routes.py:1476`
- `routes/editor_agent_routes.py:1766`

## `_state_dims` — function, line 732
- **called from:**
- `routes/editor_agent_routes.py:808`
- `routes/editor_agent_routes.py:1060`

## `_title_text` — function, line 751
- **called from:**
- `routes/editor_agent_routes.py:794`

## `_crop_rect_for_aspect` — function, line 761
- **called from:**
- `routes/editor_agent_routes.py:828`

## `_extend_dims` — function, line 781
- **called from:**
- `routes/editor_agent_routes.py:814`

## `_plan_text_steps` — function, line 793
- **called from:**
- `routes/editor_agent_routes.py:839`
- `routes/editor_agent_routes.py:939`

## `_plan_format_steps` — function, line 804
- **called from:**
- `routes/editor_agent_routes.py:925`
- `tests/test_agent_editor_routes.py:536`
- `tests/test_agent_editor_routes.py:543`

## `_plan_psd_steps` — function, line 843
- **called from:**
- `routes/editor_agent_routes.py:936`

## `_is_background_removal_intent` — function, line 849
- **called from:**
- `routes/editor_agent_routes.py:916`
- `tests/test_editor_generation_model_routing.py:262`
- `tests/test_editor_generation_model_routing.py:263`
- `tests/test_editor_generation_model_routing.py:264`
- `tests/test_editor_generation_model_routing.py:265`
- `tests/test_editor_generation_model_routing.py:266`
- `tests/test_editor_generation_model_routing.py:267`
- `tests/test_editor_generation_model_routing.py:268`
- `tests/test_editor_generation_model_routing.py:269`
- `tests/test_editor_generation_model_routing.py:272`
- `tests/test_editor_generation_model_routing.py:273`
- `tests/test_editor_generation_model_routing.py:274`
- `tests/test_editor_generation_model_routing.py:275`
- `tests/test_editor_generation_model_routing.py:276`
- `tests/test_editor_generation_model_routing.py:277`
- `tests/test_editor_generation_model_routing.py:278`
- `tests/test_editor_generation_model_routing.py:279`
- `tests/test_editor_generation_model_routing.py:280`
- `tests/test_editor_generation_model_routing.py:281`
- `tests/test_editor_generation_model_routing.py:287`
- `tests/test_editor_generation_model_routing.py:293`

## `_plan_special` — function, line 907
- **called from:**
- `routes/editor_agent_routes.py:1476`
- `routes/editor_agent_routes.py:1769`
- `tests/test_editor_layer_scoped_actions_browser.py:315`
- `tests/test_editor_planner_routing.py:47`
- `tests/test_photo_editor_style_guide.py:309`
- `tests/test_photo_editor_style_guide.py:321`
- `tests/test_photo_editor_style_guide.py:331`
- `tests/test_photo_editor_style_guide.py:335`
- `tests/test_photo_editor_style_guide.py:342`
- `tests/test_photo_editor_style_guide.py:424`

## `_step_op_signature` — function, line 960
- **called from:**
- `routes/editor_agent_routes.py:1012`
- `routes/editor_agent_routes.py:1030`

## `_reply_from_ops` — function, line 1008
- **called from:**
- `routes/editor_agent_routes.py:1076`

## `_reply_matches_ops` — function, line 1023
- **called from:**
- `routes/editor_agent_routes.py:1075`

## `_verified_reply` — function, line 1040
- **called from:**
- `routes/editor_agent_routes.py:1950`
- `tests/test_photo_editor_style_guide.py:352`
- `tests/test_photo_editor_style_guide.py:361`

## `set_editor_planner` — function, line 1084
- **called from:**
- `routes/editor_agent_routes.py:1363`
- `tests/test_agent_editor_routes.py:21`
- `tests/test_agent_editor_routes.py:23`
- `tests/test_agent_editor_routes.py:35`
- `tests/test_agent_editor_routes.py:54`
- `tests/test_agent_editor_routes.py:75`
- `tests/test_agent_editor_routes.py:81`
- `tests/test_agent_editor_routes.py:89`
- `tests/test_agent_editor_routes.py:103`
- `tests/test_agent_editor_routes.py:109`
- `tests/test_agent_editor_routes.py:120`
- `tests/test_agent_editor_routes.py:134`
- `tests/test_agent_editor_routes.py:185`
- `tests/test_agent_editor_routes.py:214`
- `tests/test_agent_editor_routes.py:254`
- `tests/test_agent_editor_routes.py:276`
- `tests/test_agent_editor_routes.py:371`
- `tests/test_agent_editor_routes.py:397`
- `tests/test_agent_editor_routes.py:663`
- `tests/test_agent_editor_routes.py:677`
- `tests/test_agent_editor_routes.py:744`
- `tests/test_agent_editor_routes.py:1033`
- `tests/test_agent_editor_routes.py:1075`
- `tests/test_agent_editor_routes.py:1348`
- `tests/test_agent_editor_routes.py:1392`
- `tests/test_agent_editor_routes.py:1405`
- `tests/test_agent_editor_routes.py:1508`
- `tests/test_agent_editor_routes.py:1585`
- `tests/test_agent_editor_routes.py:1598`
- `tests/test_agent_editor_routes.py:1630`
- `tests/test_agent_editor_routes.py:1649`
- `tests/test_agent_editor_routes.py:1668`
- `tests/test_agent_editor_routes.py:1684`
- `tests/test_agent_editor_routes.py:1697`
- `tests/test_agent_editor_routes.py:1787`
- `tests/test_agent_editor_routes.py:1795`
- `tests/test_agent_editor_routes.py:1809`
- `tests/test_agent_editor_routes.py:1826`
- `tests/test_agent_editor_routes.py:1845`
- `tests/test_editor_generation_model_routing.py:33`
- `tests/test_editor_generation_model_routing.py:50`
- `tests/test_editor_generation_model_routing.py:73`
- `tests/test_editor_generation_model_routing.py:89`
- `tests/test_editor_generation_model_routing.py:208`
- `tests/test_editor_generation_model_routing.py:254`
- `tests/test_editor_generation_model_routing.py:340`
- `tests/test_editor_generation_model_routing.py:351`
- `tests/test_editor_generation_model_routing.py:394`
- `tests/test_editor_generation_model_routing.py:405`
- `tests/test_editor_generation_model_routing.py:448`
- `tests/test_editor_generation_model_routing.py:456`
- `tests/test_editor_planner_routing.py:33`
- `tests/test_editor_planner_routing.py:35`
- `tests/test_editor_planner_routing.py:149`
- `tests/test_editor_planner_routing.py:158`
- `tests/test_editor_planner_routing.py:167`
- `tests/test_photo_editor_family.py:125`
- `tests/test_photo_editor_family.py:142`
- `tests/test_photo_editor_family.py:348`
- `tests/test_photo_editor_family.py:373`
- … +8 more (grep the name in repo)

## `_plan_is_generic_tone_only` — function, line 1149
- **called from:**
- `routes/editor_agent_routes.py:1166`

## `_unsure_plan` — function, line 1155
- **called from:**
- `routes/editor_agent_routes.py:1502`
- `routes/editor_agent_routes.py:1792`

## `_fallback_plan` — function, line 1175
- **called from:**
- `routes/editor_agent_routes.py:1529`
- `routes/editor_agent_routes.py:1760`
- `tests/test_editor_planner_routing.py:51`
- `tests/test_editor_planner_routing.py:108`
- `tests/test_photo_editor_family.py:301`
- `tests/test_photo_editor_family.py:304`
- `tests/test_photo_editor_family.py:307`

## `_parse_plan` — function, line 1196
- **called from:**
- `routes/editor_agent_routes.py:1466`
- `routes/editor_agent_routes.py:1753`
- `tests/test_photo_editor_style_guide.py:177`

## `_normalize_steps` — function, line 1219
- **called from:**
- `routes/editor_agent_routes.py:1538`
- `tests/test_agent_editor_routes.py:143`
- `tests/test_agent_editor_routes.py:144`

## `_json_object` — function (async), line 1238
- **called from:**
- `routes/editor_agent_routes.py:1431`
- `routes/editor_agent_routes.py:1536`
- `routes/editor_agent_routes.py:1604`
- `routes/editor_agent_routes.py:1628`
- `routes/editor_agent_routes.py:1697`
- `routes/editor_agent_routes.py:2088`
- `routes/gallery/gallery_routes.py:338`
- `routes/gallery/gallery_routes.py:3017`

## `_prompt` — function, line 1248
- **called from:**
- `routes/editor_agent_routes.py:1432`
- `routes/editor_agent_routes.py:1704`
- `routes/editor_agent_routes.py:2092`

## `_bridge_timeout` — function, line 1255
- **called from:**
- `routes/editor_agent_routes.py:1540`
- `routes/editor_agent_routes.py:1630`

## `_is_admin` — function, line 1265
- **called from:**
- `routes/editor_agent_routes.py:1985`
- `routes/editor_agent_routes.py:2052`
- `routes/task/task_routes.py:443`
- `routes/task/task_routes.py:1100`

## `_user` — function, line 1319
- **called from:**
- `routes/editor_agent_routes.py:1430`
- `routes/editor_agent_routes.py:1535`
- `routes/editor_agent_routes.py:1582`
- `routes/editor_agent_routes.py:1603`
- `routes/editor_agent_routes.py:1627`
- `routes/editor_agent_routes.py:1696`
- `routes/editor_agent_routes.py:1984`
- `routes/editor_agent_routes.py:2051`
- `routes/editor_agent_routes.py:2087`

## `_default_editor_planner` — function (async), line 1340
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_editor_agent_routes` — function, line 1359
- **called from:**
- `app.py:864`
- `tests/test_agent_editor_routes.py:29`
- `tests/test_agent_editor_routes.py:187`
- `tests/test_agent_editor_routes.py:777`
- `tests/test_agent_editor_routes.py:869`
- `tests/test_agent_editor_routes.py:896`
- `tests/test_agent_editor_routes.py:1032`
- `tests/test_agent_editor_routes.py:1052`
- `tests/test_agent_editor_routes.py:1135`
- `tests/test_editor_generation_model_routing.py:39`
- `tests/test_editor_generation_model_routing.py:76`
- `tests/test_editor_generation_model_routing.py:182`
- `tests/test_editor_generation_model_routing.py:338`
- `tests/test_editor_generation_model_routing.py:392`
- `tests/test_editor_generation_model_routing.py:445`
- `tests/test_editor_model_discovery.py:60`
- `tests/test_editor_model_discovery.py:98`
- `tests/test_editor_model_discovery.py:133`
- `tests/test_editor_model_discovery.py:187`
- `tests/test_editor_model_discovery.py:230`
- `tests/test_editor_model_discovery.py:250`
- `tests/test_editor_model_discovery.py:290`
- `tests/test_editor_model_discovery.py:307`
- `tests/test_editor_model_discovery.py:345`
- `tests/test_editor_model_discovery.py:365`
- `tests/test_editor_model_discovery.py:388`
- `tests/test_editor_planner_routing.py:41`
- `tests/test_editor_planner_ssrf_authorization.py:75`
- `tests/test_editor_planner_ssrf_authorization.py:114`
- `tests/test_editor_planner_ssrf_authorization.py:322`
- `tests/test_editor_planner_ssrf_authorization.py:384`
- `tests/test_editor_planner_ssrf_authorization.py:432`
- `tests/test_photo_editor_family.py:128`
- `tests/test_photo_editor_family.py:336`
- `tests/test_photo_editor_style_guide.py:43`

## `_subscribe` — function, line 1374
- **called from:**
- `routes/editor_agent_routes.py:1586`

## `_unsubscribe` — function, line 1385
- **called from:**
- `routes/editor_agent_routes.py:1596`

## `_broadcast` — function, line 1392
- **called from:**
- `routes/editor_agent_routes.py:1549`
- `routes/editor_agent_routes.py:1920`
- `routes/editor_agent_routes.py:1941`

## `_expire_command` — function, line 1409
- **called from:**
- `routes/editor_agent_routes.py:1565`
- `routes/editor_agent_routes.py:1928`
- `routes/editor_agent_routes.py:1948`

## `_scoped` — function, line 1421
- **called from:**
- `routes/editor_agent_routes.py:1537`
- `routes/editor_agent_routes.py:1583`
- `routes/editor_agent_routes.py:1720`

## `_scope_label` — function, line 1425
- **called from:**
- `routes/editor_agent_routes.py:1574`
- `routes/editor_agent_routes.py:1722`
- `routes/editor_agent_routes.py:1895`

## `plan` — function (async), line 1429
- **route:** `POST /api/editor/plan`
- decorator: `router.post("/api/editor/plan")`
- **called from:**
- `static/js/admin.js:2718`
- `static/js/chat.js:5868`
- `static/js/editor/nl-edit.js:130`
- `static/js/galleryEditor.js:2693`

## `bridge_command` — function (async), line 1534
- **route:** `POST /api/editor/bridge/command`
- decorator: `router.post("/api/editor/bridge/command")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `bridge_events` — function (async), line 1581
- **route:** `GET /api/editor/bridge/events`
- decorator: `router.get("/api/editor/bridge/events")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `gen` — function (async), line 1585
- **called from:**
- `routes/editor_agent_routes.py:1598`
- `tests/test_compare_stop_disconnect_poll.py:82`

## `bridge_result` — function (async), line 1602
- **route:** `POST /api/editor/bridge/result`
- decorator: `router.post("/api/editor/bridge/result")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `bridge_await` — function (async), line 1626
- **route:** `POST /api/editor/bridge/await`
- decorator: `router.post("/api/editor/bridge/await")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_scoped_editor_tools` — function, line 1666
- **called from:**
- `routes/editor_agent_routes.py:1719`

## `editor_agent` — function (async), line 1688
- **route:** `POST /api/editor/agent`
- decorator: `router.post("/api/editor/agent")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `style_guide_route` — function (async), line 1968
- **route:** `GET /api/editor/style-guide`
- decorator: `router.get("/api/editor/style-guide")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `editor_image_models` — function (async), line 1977
- **route:** `GET /api/editor/image-models`
- decorator: `router.get("/api/editor/image-models")`
- **called from:**
- `routes/editor_agent_routes.py:1714`
- `routes/gallery/gallery_routes.py:1792`
- `routes/gallery/gallery_routes.py:2661`
- `tests/test_editor_generation_model_routing.py:121`
- `tests/test_editor_generation_model_routing.py:140`
- `tests/test_editor_generation_model_routing.py:144`
- `tests/test_editor_generation_model_routing.py:151`
- `tests/test_editor_generation_model_routing.py:159`
- `tests/test_editor_generation_model_routing.py:163`

## `editor_agent_models` — function (async), line 2041
- **route:** `GET /api/editor/agent-models`
- decorator: `router.get("/api/editor/agent-models")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `editor_self_check` — function (async), line 2079
- **route:** `POST /api/editor/self-check`
- decorator: `router.post("/api/editor/self-check")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
