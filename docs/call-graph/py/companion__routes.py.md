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
- `app.py:887`
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
- `app.py:485`
- `app.py:487`
- `app.py:572`
- `app.py:574`
- `app.py:613`
- `app.py:763`
- `app.py:837`
- `app.py:844`
- `app.py:854`
- `app.py:1034`
- `app.py:1048`
- `app.py:1101`
- `app.py:1118`
- `app.py:1126`
- `app.py:1209`
- `app.py:1220`
- `app.py:1278`
- `app.py:1281`
- `app.py:1303`
- `core/auth.py:128`
- `core/auth.py:131`
- `core/auth.py:147`
- `core/auth.py:183`
- `core/auth.py:217`
- `core/auth.py:282`
- `core/auth.py:311`
- `core/auth.py:331`
- `core/auth.py:363`
- `core/auth.py:402`
- `core/auth.py:465`
- `core/auth.py:523`
- `core/auth.py:545`
- `core/auth.py:561`
- `core/database.py:918`
- `core/database.py:941`
- `core/database.py:966`
- `core/database.py:989`
- `core/database.py:1012`
- `core/database.py:1043`
- `core/database.py:1068`
- `core/database.py:1092`
- `core/database.py:1143`
- `core/database.py:1166`
- `core/database.py:1212`
- `core/database.py:1267`
- `core/database.py:1290`
- `core/database.py:1314`
- `core/database.py:1338`
- `core/database.py:1372`
- `core/database.py:1401`
- `core/database.py:1471`
- `core/database.py:1497`
- `core/database.py:1529`
- `core/database.py:1555`
- `core/database.py:1569`
- `core/database.py:1588`
- `core/database.py:1624`
- `core/database.py:1667`
- `core/database.py:1698`
- `core/database.py:1710`
- … +491 more (grep the name in repo)

## `models` — function, line 110
- **route:** `GET /models`
- decorator: `router.get("/models")`
- **called from:**
- `static/js/chatRenderer.js:2625`
- `static/js/compare/models.js:65`
- `static/js/compare/selector.js:403`
- `static/js/cookbook-deps-recipes.js:71`
- `static/js/cookbook-deps-recipes.js:79`
- `static/js/cookbook.js:2704`
- `static/js/cookbookRunning.js:4080`
- `static/js/cookbookServe.js:1718`
- `static/js/markdown.js:517`
- `static/js/providers.js:38`
- `static/js/settings.js:737`

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
