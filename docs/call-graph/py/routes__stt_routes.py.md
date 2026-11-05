# `routes/stt_routes.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `setup_stt_routes` — function, line 12
- **called from:**
- `app.py:842`

## `get_stt_stats` — function (async), line 17
- **route:** `GET /stats`
- decorator: `router.get("/stats")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `transcribe_audio` — function (async), line 26
- **route:** `POST /transcribe`
- decorator: `router.post("/transcribe")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
