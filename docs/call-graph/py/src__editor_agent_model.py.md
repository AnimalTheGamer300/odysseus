# `src/editor_agent_model.py` — definitions & call sites

29 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_setting` — function, line 55
- **called from:**
- `src/editor_agent_model.py:66`
- `src/editor_agent_model.py:78`
- `src/editor_agent_model.py:82`
- `src/editor_agent_model.py:86`

## `local_bases` — function, line 65
- **called from:**
- `src/editor_agent_model.py:318`
- `src/editor_agent_model.py:366`
- `src/editor_agent_model.py:375`
- `src/editor_agent_model.py:417`
- `src/editor_agent_model.py:424`
- `src/editor_agent_model.py:567`
- `src/editor_agent_model.py:613`
- `src/editor_agent_model.py:649`
- `src/editor_agent_model.py:713`
- `tests/test_editor_agent_model_resolution.py:43`

## `local_model` — function, line 77
- **called from:**
- `routes/editor_agent_routes.py:1439`
- `routes/editor_agent_routes.py:1470`
- `routes/editor_agent_routes.py:1472`
- `routes/editor_agent_routes.py:1728`
- `routes/editor_agent_routes.py:1757`
- `routes/editor_agent_routes.py:1759`
- `src/editor_agent_model.py:277`
- `src/editor_agent_model.py:323`
- `src/editor_agent_model.py:323`
- `src/editor_agent_model.py:371`
- `src/editor_agent_model.py:379`
- `src/editor_agent_model.py:418`
- `src/editor_agent_model.py:423`
- `src/editor_agent_model.py:426`
- `src/editor_agent_model.py:568`
- `src/editor_agent_model.py:650`

## `caption_base` — function, line 81
- **called from:**
- `src/editor_agent_model.py:274`
- `src/editor_agent_model.py:717`
- `tests/test_editor_agent_model_resolution.py:70`

## `caption_model` — function, line 85
- **called from:**
- `src/editor_agent_model.py:277`

## `set_override` — function, line 99
- **called from:**
- `routes/editor_agent_routes.py:1456`
- `routes/editor_agent_routes.py:1743`

## `get_override` — function, line 103
- **called from:**
- `routes/editor_agent_routes.py:1349`

## `set_last_model` — function, line 107
- **called from:**
- `routes/editor_agent_routes.py:1355`
- `routes/editor_agent_routes.py:1457`
- `routes/editor_agent_routes.py:1744`

## `get_last_model` — function, line 111
- **called from:**
- `routes/editor_agent_routes.py:1465`
- `routes/editor_agent_routes.py:1752`

## `_chat_url` — function, line 115
- **called from:**
- `src/editor_agent_model.py:204`

## `_split_override` — function, line 122
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_has_image` — function, line 131
- **called from:**
- `src/editor_agent_model.py:609`
- `tests/test_agent_editor_routes.py:1447`
- `tests/test_agent_editor_routes.py:1448`
- `tests/test_agent_editor_routes.py:1468`

## `_first_image` — function, line 141
- **called from:**
- `src/editor_agent_model.py:611`

## `_strip_images` — function, line 153
- **called from:**
- `src/editor_agent_model.py:610`

## `_with_caption` — function, line 169
- **called from:**
- `src/editor_agent_model.py:628`

## `_post_chat` — function (async), line 179
- **called from:**
- `src/editor_agent_model.py:278`
- `src/editor_agent_model.py:332`
- `src/editor_agent_model.py:621`
- `src/editor_agent_model.py:627`
- `src/editor_agent_model.py:633`

## `_served_models` — function (async), line 220
- **called from:**
- `src/editor_agent_model.py:252`

## `_resolve_model` — function (async), line 243
- **called from:**
- `services/skills/model_selection.py:41`
- `services/skills/model_selection.py:70`
- `src/ai_interaction.py:1352`
- `src/ai_interaction.py:1356`
- `src/ai_interaction.py:1360`
- `src/ai_interaction.py:1596`
- `src/ai_interaction.py:1600`
- `src/ai_interaction.py:1604`
- `src/ai_interaction.py:1948`
- `src/ai_interaction.py:1952`
- `src/document_processor.py:427`
- `src/document_processor.py:438`
- `src/editor_agent_model.py:277`
- `src/editor_agent_model.py:323`
- `tests/test_editor_agent_model_resolution.py:17`
- `tests/test_editor_agent_model_resolution.py:24`
- `tests/test_editor_agent_model_resolution.py:25`
- `tests/test_editor_agent_model_resolution.py:31`
- `tests/test_editor_agent_model_resolution.py:38`

## `caption_image` — function (async), line 262
- **called from:**
- `src/editor_agent_model.py:625`
- `tests/test_editor_agent_model_resolution.py:71`
- `tests/test_editor_agent_model_resolution.py:81`

## `_parse_self_check` — function, line 285
- **called from:**
- `src/editor_agent_model.py:336`

## `self_check` — function (async), line 296
- **called from:**
- `routes/editor_agent_routes.py:2089`
- `tests/test_editor_agent_model_resolution.py:52`
- `tests/test_editor_agent_model_resolution.py:82`

## `_resolve_override_candidate` — function, line 342
- **called from:**
- `src/editor_agent_model.py:420`
- `src/editor_agent_model.py:583`

## `_candidates` — function, line 565
- **called from:**
- `src/editor_agent_model.py:614`
- `tests/test_agent_editor_routes.py:1433`
- `tests/test_editor_agent_model_resolution.py:90`
- `tests/test_editor_agent_model_resolution.py:91`
- `tests/test_editor_planner_ssrf_authorization.py:127`
- `tests/test_editor_planner_ssrf_authorization.py:147`
- `tests/test_editor_planner_ssrf_authorization.py:170`
- `tests/test_editor_planner_ssrf_authorization.py:180`
- `tests/test_editor_planner_ssrf_authorization.py:200`
- `tests/test_editor_planner_ssrf_authorization.py:205`
- `tests/test_editor_planner_ssrf_authorization.py:237`
- `tests/test_editor_planner_ssrf_authorization.py:242`
- `tests/test_editor_planner_ssrf_authorization.py:267`
- `tests/test_editor_planner_ssrf_authorization.py:293`
- `tests/test_editor_planner_ssrf_authorization.py:298`
- `tests/test_editor_planner_ssrf_authorization.py:312`
- `tests/test_editor_planner_ssrf_authorization.py:358`
- `tests/test_editor_planner_ssrf_authorization.py:362`
- `tests/test_editor_planner_ssrf_authorization.py:436`
- `tests/test_editor_planner_ssrf_authorization.py:441`

## `plan_with_editor_agent` — function (async), line 593
- **called from:**
- `routes/editor_agent_routes.py:1348`
- `tests/test_agent_editor_routes.py:1457`
- `tests/test_agent_editor_routes.py:1480`
- `tests/test_agent_editor_routes.py:1502`
- `tests/test_agent_editor_routes.py:1874`

## `list_editor_agent_models` — function (async), line 641
- **called from:**
- `routes/editor_agent_routes.py:2054`
- `tests/test_agent_editor_routes.py:1385`

## `probe_models` — function, line 703
- **called from:**
- `src/editor_agent_model.py:714`
- `src/editor_agent_model.py:719`

## `_probe_worker` — function, line 712
- **called from:**
- `tests/test_editor_agent_model_resolution.py:80`

## `startup_probe` — function, line 723
- **called from:**
- `routes/editor_agent_routes.py:2070`

## `probe_status` — function, line 731
- **called from:**
- `routes/editor_agent_routes.py:2068`
- `routes/editor_agent_routes.py:2071`
