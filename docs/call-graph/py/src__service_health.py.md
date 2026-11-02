# `src/service_health.py` — definitions & call sites

22 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_svc` — function, line 83
- **called from:**
- `src/service_health.py:195`
- `src/service_health.py:207`
- `src/service_health.py:209`
- `src/service_health.py:211`
- `src/service_health.py:235`
- `src/service_health.py:240`
- `src/service_health.py:249`
- `src/service_health.py:254`
- `src/service_health.py:280`
- `src/service_health.py:291`
- `src/service_health.py:293`
- `src/service_health.py:297`
- `src/service_health.py:313`
- `src/service_health.py:357`
- `src/service_health.py:396`
- `src/service_health.py:461`
- `src/service_health.py:464`
- `src/service_health.py:496`

## `_safe_url` — function, line 87
- **called from:**
- `src/service_health.py:241`
- `src/service_health.py:286`
- `src/service_health.py:362`
- `tests/test_service_health_collect.py:61`

## `_classify_error` — function, line 110
- **called from:**
- `src/service_health.py:176`
- `src/service_health.py:253`
- `src/service_health.py:296`
- `src/service_health.py:334`
- `src/service_health.py:371`
- `src/service_health.py:463`
- `tests/test_service_health_collect.py:72`
- `tests/test_service_health_collect.py:73`
- `tests/test_service_health_collect.py:74`
- `tests/test_service_health_collect.py:75`
- `tests/test_service_health_collect.py:76`
- `tests/test_service_health_collect.py:77`

## `_detail_for` — function, line 143
- **called from:**
- `src/service_health.py:254`
- `src/service_health.py:297`
- `src/service_health.py:461`
- `src/service_health.py:464`
- `src/service_health.py:496`

## `_http_get` — function, line 147
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_bounded_map` — function, line 153
- **called from:**
- `src/service_health.py:336`
- `src/service_health.py:376`

## `chromadb_health` — function, line 186
- **called from:**
- `src/service_health.py:482`
- `tests/test_app_initializer_memory_vector_degraded.py:69`
- `tests/test_app_initializer_memory_vector_degraded.py:70`
- `tests/test_app_initializer_memory_vector_degraded.py:71`
- `tests/test_service_health_chromadb.py:13`
- `tests/test_service_health_chromadb.py:19`
- `tests/test_service_health_chromadb.py:24`
- `tests/test_service_health_chromadb.py:29`
- `tests/test_service_health_chromadb.py:35`

## `_searxng_instance` — function, line 216
- **called from:**
- `src/service_health.py:238`

## `searxng_health` — function, line 225
- **called from:**
- `tests/test_service_health_search.py:18`
- `tests/test_service_health_search.py:23`
- `tests/test_service_health_search.py:35`
- `tests/test_service_health_search.py:44`
- `tests/test_service_health_search.py:52`
- `tests/test_service_health_search.py:60`
- `tests/test_service_health_search.py:73`

## `_ntfy_integration` — function, line 260
- **called from:**
- `src/service_health.py:278`
- `tests/test_reminder_ntfy_ssrf.py:69`
- `tests/test_reminder_ntfy_ssrf.py:84`
- `tests/test_reminder_ntfy_ssrf.py:100`
- `tests/test_reminder_ntfy_ssrf.py:111`

## `ntfy_health` — function, line 269
- **called from:**
- `tests/test_service_health_ntfy.py:22`
- `tests/test_service_health_ntfy.py:27`
- `tests/test_service_health_ntfy.py:40`
- `tests/test_service_health_ntfy.py:46`
- `tests/test_service_health_ntfy.py:60`

## `email_health` — function, line 303
- **called from:**
- `tests/test_service_health_email.py:22`
- `tests/test_service_health_email.py:26`
- `tests/test_service_health_email.py:36`
- `tests/test_service_health_email.py:41`
- `tests/test_service_health_email.py:46`
- `tests/test_service_health_email.py:51`
- `tests/test_service_health_email.py:58`
- `tests/test_service_health_email.py:76`

## `_label` — function, line 319
- **called from:**
- `src/service_health.py:323`
- `src/service_health.py:339`
- `src/service_health.py:365`
- `src/service_health.py:379`

## `_check` — function, line 322
- **called from:**
- `tests/test_companion_readonly.py:44`
- `tests/test_compare_endpoint_owner_scope.py:24`
- `tests/test_gallery_image_endpoint_owner_scope.py:19`
- `tests/test_null_owner_gates.py:236`
- `tests/test_research_endpoint_owner_scope.py:35`

## `providers_health` — function, line 346
- **called from:**
- `tests/test_service_health_providers.py:16`
- `tests/test_service_health_providers.py:20`
- `tests/test_service_health_providers.py:30`
- `tests/test_service_health_providers.py:35`
- `tests/test_service_health_providers.py:40`
- `tests/test_service_health_providers.py:48`
- `tests/test_service_health_providers.py:57`
- `tests/test_service_health_providers.py:75`
- `tests/test_service_health_providers.py:95`

## `_label` — function, line 361
- **called from:**
- `src/service_health.py:323`
- `src/service_health.py:339`
- `src/service_health.py:365`
- `src/service_health.py:379`

## `_check` — function, line 364
- **called from:**
- `tests/test_companion_readonly.py:44`
- `tests/test_compare_endpoint_owner_scope.py:24`
- `tests/test_gallery_image_endpoint_owner_scope.py:19`
- `tests/test_null_owner_gates.py:236`
- `tests/test_research_endpoint_owner_scope.py:35`

## `_rollup_items` — function, line 385
- **called from:**
- `src/service_health.py:341`
- `src/service_health.py:382`

## `_rollup` — function, line 401
- **called from:**
- `src/service_health.py:501`
- `tests/test_service_health_collect.py:19`
- `tests/test_service_health_collect.py:23`
- `tests/test_service_health_collect.py:27`

## `_gather_inputs` — function, line 410
- **called from:**
- `src/service_health.py:478`

## `_run_subsystem` — function (async), line 451
- **called from:**
- `src/service_health.py:486`
- `src/service_health.py:487`
- `src/service_health.py:488`
- `src/service_health.py:489`

## `collect_service_health` — function (async), line 467
- **called from:**
- `routes/diagnostics_routes.py:30`
- `tests/test_service_health_collect.py:42`
- `tests/test_service_health_collect.py:104`
- `tests/test_service_health_collect.py:133`
