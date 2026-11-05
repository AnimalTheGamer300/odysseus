# `routes/tts_routes.py` — definitions & call sites

5 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `TTSRequest` — class, line 13
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_tts_routes` — function, line 17
- **called from:**
- `app.py:836`

## `get_tts_stats` — function (async), line 22
- **route:** `GET /stats`
- decorator: `router.get("/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `synthesize_speech` — function (async), line 31
- **route:** `POST /synthesize`
- decorator: `router.post("/synthesize")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `clear_tts_cache` — function (async), line 78
- **route:** `POST /clear-cache`
- decorator: `router.post("/clear-cache")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
