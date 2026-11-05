# `companion/routes.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `token_owner` — function, line 31
- **called from:**
- `companion/routes.py:105`
- `companion/routes.py:126`
- `tests/test_companion_readonly.py:160`
- `tests/test_companion_readonly.py:165`
- `tests/test_companion_readonly.py:170`

## `owner_can_see` — function, line 44
- **called from:**
- `companion/routes.py:142`
- `tests/test_companion_readonly.py:176`
- `tests/test_companion_readonly.py:181`
- `tests/test_companion_readonly.py:186`
- `tests/test_companion_readonly.py:190`
- `tests/test_companion_readonly.py:191`
- `tests/test_companion_readonly.py:197`
- `tests/test_companion_readonly.py:198`

## `require_models_scope` — function, line 56
- **called from:**
- `companion/routes.py:120`

## `mint_pairing_token` — function, line 68
- **called from:**
- `companion/routes.py:209`
- `tests/test_companion_pairing.py:104`
- `tests/test_companion_pairing.py:112`

## `setup_companion_routes` — function, line 82
- **called from:**
- `app.py:972`
- `tests/test_companion_pairing.py:259`
- `tests/test_companion_pairing.py:269`
- `tests/test_companion_readonly.py:121`

## `ping` — function, line 86
- **route:** `GET /ping`
- decorator: `router.get("/ping")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `info` — function, line 98
- **route:** `GET /info`
- decorator: `router.get("/info")`
- **called from:**
- `app.py:526`
- `app.py:528`
- `app.py:650`
- `app.py:652`
- `app.py:691`
- `app.py:843`
- `app.py:921`
- `app.py:928`
- `app.py:938`
- `app.py:1198`
- `app.py:1212`
- `app.py:1271`
- `app.py:1285`
- `app.py:1302`
- `app.py:1310`
- `app.py:1382`
- `app.py:1401`
- `app.py:1412`
- `app.py:1453`
- `app.py:1456`
- `app.py:1490`
- `core/auth.py:146`
- `core/auth.py:149`
- `core/auth.py:165`
- `core/auth.py:201`
- `core/auth.py:235`
- `core/auth.py:300`
- `core/auth.py:329`
- `core/auth.py:349`
- `core/auth.py:381`
- `core/auth.py:429`
- `core/auth.py:474`
- `core/auth.py:503`
- `core/auth.py:516`
- `core/auth.py:574`
- `core/auth.py:596`
- `core/auth.py:612`
- `core/database.py:977`
- `core/database.py:999`
- `core/database.py:1021`
- `core/database.py:1043`
- `core/database.py:1090`
- `core/database.py:1115`
- `core/database.py:1138`
- `core/database.py:1161`
- `core/database.py:1192`
- `core/database.py:1217`
- `core/database.py:1241`
- `core/database.py:1292`
- `core/database.py:1315`
- `core/database.py:1339`
- `core/database.py:1385`
- `core/database.py:1460`
- `core/database.py:1483`
- `core/database.py:1506`
- `core/database.py:1543`
- `core/database.py:1566`
- `core/database.py:1590`
- `core/database.py:1624`
- `core/database.py:1653`
- … +820 more (grep the name in repo)

## `models` — function, line 110
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
- `static/js/admin.js:680`
- `static/js/admin.js:685`
- `static/js/chatRenderer.js:3311`
- `static/js/compare/models.js:65`
- `static/js/compare/selector.js:403`
- `static/js/cookbook-deps-recipes.js:71`
- `static/js/cookbook-deps-recipes.js:79`
- `static/js/cookbook.js:2838`
- `static/js/cookbookRunning.js:4157`
- `static/js/cookbookServe.js:1762`
- `static/js/editor/ai-models.js:253`
- `static/js/markdown.js:701`
- `static/js/providers.js:38`
- `static/js/settings.js:741`

## `pair_page` — function, line 169
- **route:** `GET /pair`
- decorator: `router.get("/pair")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `pair_create` — function, line 196
- **route:** `POST /pair`
- decorator: `router.post("/pair")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
