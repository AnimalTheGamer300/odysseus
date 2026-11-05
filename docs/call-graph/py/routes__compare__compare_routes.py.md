# `routes/compare/compare_routes.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_owned_endpoint_by_url` — function, line 22
- **called from:**
- `routes/compare/compare_routes.py:152`
- `tests/test_compare_endpoint_owner_scope.py:70`

## `_owned_endpoint_by_id` — function, line 42
- **called from:**
- `routes/compare/compare_routes.py:134`

## `RecordVoteRequest` — class, line 60
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `setup_compare_routes` — function, line 67
- **called from:**
- `app.py:899`
- `tests/test_endpoint_owner_scope_followup.py:24`

## `start_comparison` — function, line 71
- **route:** `POST /start`
- decorator: `router.post("/start")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `vote_comparison` — function, line 238
- **route:** `POST /{comp_id}/vote`
- decorator: `router.post("/{comp_id}/vote")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `record_comparison` — function, line 284
- **route:** `POST /record`
- decorator: `router.post("/record")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `list_comparisons` — function, line 321
- **route:** `GET /history`
- decorator: `router.get("/history")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `delete_comparison` — function, line 347
- **route:** `DELETE /{comp_id}`
- decorator: `router.delete("/{comp_id}")`
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_
