# `src/service_health.py` — definitions & call sites

23 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_svc` — function, line 97
- **called from:**
- `src/service_health.py:209`
- `src/service_health.py:221`
- `src/service_health.py:223`
- `src/service_health.py:225`
- `src/service_health.py:249`
- `src/service_health.py:254`
- `src/service_health.py:263`
- `src/service_health.py:268`
- `src/service_health.py:294`
- `src/service_health.py:305`
- `src/service_health.py:307`
- `src/service_health.py:311`
- `src/service_health.py:327`
- `src/service_health.py:371`
- `src/service_health.py:410`
- `src/service_health.py:483`
- `src/service_health.py:486`
- `src/service_health.py:500`
- `src/service_health.py:551`
- `tests/test_service_health_collect.py:263`

## `_safe_url` — function, line 101
- **called from:**
- `src/service_health.py:255`
- `src/service_health.py:300`
- `src/service_health.py:376`
- `tests/test_service_health_collect.py:61`

## `_classify_error` — function, line 124
- **called from:**
- `src/service_health.py:190`
- `src/service_health.py:267`
- `src/service_health.py:310`
- `src/service_health.py:348`
- `src/service_health.py:385`
- `src/service_health.py:442`
- `src/service_health.py:448`
- `src/service_health.py:454`
- `src/service_health.py:467`
- `src/service_health.py:485`
- `tests/test_service_health_collect.py:72`
- `tests/test_service_health_collect.py:73`
- `tests/test_service_health_collect.py:74`
- `tests/test_service_health_collect.py:75`
- `tests/test_service_health_collect.py:76`
- `tests/test_service_health_collect.py:77`

## `_detail_for` — function, line 157
- **called from:**
- `src/service_health.py:268`
- `src/service_health.py:311`
- `src/service_health.py:483`
- `src/service_health.py:486`
- `src/service_health.py:502`
- `src/service_health.py:551`

## `_http_get` — function, line 161
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_bounded_map` — function, line 167
- **called from:**
- `src/service_health.py:350`
- `src/service_health.py:390`

## `chromadb_health` — function, line 200
- **called from:**
- `src/service_health.py:526`
- `tests/test_app_initializer_memory_vector_degraded.py:69`
- `tests/test_app_initializer_memory_vector_degraded.py:70`
- `tests/test_app_initializer_memory_vector_degraded.py:71`
- `tests/test_service_health_chromadb.py:13`
- `tests/test_service_health_chromadb.py:19`
- `tests/test_service_health_chromadb.py:24`
- `tests/test_service_health_chromadb.py:29`
- `tests/test_service_health_chromadb.py:35`

## `_searxng_instance` — function, line 230
- **called from:**
- `src/service_health.py:252`

## `searxng_health` — function, line 239
- **called from:**
- `tests/test_service_health_search.py:18`
- `tests/test_service_health_search.py:23`
- `tests/test_service_health_search.py:35`
- `tests/test_service_health_search.py:44`
- `tests/test_service_health_search.py:52`
- `tests/test_service_health_search.py:60`
- `tests/test_service_health_search.py:73`

## `_ntfy_integration` — function, line 274
- **called from:**
- `src/service_health.py:292`
- `tests/test_reminder_ntfy_ssrf.py:69`
- `tests/test_reminder_ntfy_ssrf.py:84`
- `tests/test_reminder_ntfy_ssrf.py:100`
- `tests/test_reminder_ntfy_ssrf.py:111`

## `ntfy_health` — function, line 283
- **called from:**
- `tests/test_service_health_ntfy.py:22`
- `tests/test_service_health_ntfy.py:27`
- `tests/test_service_health_ntfy.py:40`
- `tests/test_service_health_ntfy.py:46`
- `tests/test_service_health_ntfy.py:60`

## `email_health` — function, line 317
- **called from:**
- `tests/test_service_health_email.py:22`
- `tests/test_service_health_email.py:26`
- `tests/test_service_health_email.py:36`
- `tests/test_service_health_email.py:41`
- `tests/test_service_health_email.py:46`
- `tests/test_service_health_email.py:51`
- `tests/test_service_health_email.py:58`
- `tests/test_service_health_email.py:76`

## `_label` — function, line 333
- **called from:**
- `src/agent_runtime/effects.py:441`
- `src/agent_runtime/effects.py:443`
- `src/agent_runtime/effects.py:444`
- `src/service_health.py:337`
- `src/service_health.py:353`
- `src/service_health.py:379`
- `src/service_health.py:393`

## `_check` — function, line 336
- **called from:**
- `tests/test_companion_readonly.py:44`
- `tests/test_compare_endpoint_owner_scope.py:24`
- `tests/test_gallery_image_endpoint_fallback.py:21`
- `tests/test_gallery_image_endpoint_owner_scope.py:19`
- `tests/test_null_owner_gates.py:236`
- `tests/test_research_endpoint_owner_scope.py:36`

## `providers_health` — function, line 360
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

## `_label` — function, line 375
- **called from:**
- `src/agent_runtime/effects.py:441`
- `src/agent_runtime/effects.py:443`
- `src/agent_runtime/effects.py:444`
- `src/service_health.py:337`
- `src/service_health.py:353`
- `src/service_health.py:379`
- `src/service_health.py:393`

## `_check` — function, line 378
- **called from:**
- `tests/test_companion_readonly.py:44`
- `tests/test_compare_endpoint_owner_scope.py:24`
- `tests/test_gallery_image_endpoint_fallback.py:21`
- `tests/test_gallery_image_endpoint_owner_scope.py:19`
- `tests/test_null_owner_gates.py:236`
- `tests/test_research_endpoint_owner_scope.py:36`

## `_rollup_items` — function, line 399
- **called from:**
- `src/service_health.py:355`
- `src/service_health.py:396`

## `_rollup` — function, line 415
- **called from:**
- `src/service_health.py:556`
- `tests/test_service_health_collect.py:19`
- `tests/test_service_health_collect.py:23`
- `tests/test_service_health_collect.py:27`

## `_gather_inputs` — function, line 424
- **called from:**
- `src/service_health.py:522`
- `tests/test_service_health_collect.py:164`
- `tests/test_service_health_collect.py:196`

## `_run_subsystem` — function (async), line 473
- **called from:**
- `src/service_health.py:545`

## `_source_unavailable` — function (async), line 489
- **called from:**
- `src/service_health.py:542`

## `collect_service_health` — function (async), line 507
- **called from:**
- `routes/diagnostics_routes.py:30`
- `tests/test_service_health_collect.py:42`
- `tests/test_service_health_collect.py:104`
- `tests/test_service_health_collect.py:133`
- `tests/test_service_health_collect.py:212`
- `tests/test_service_health_collect.py:234`
- `tests/test_service_health_collect.py:249`
- `tests/test_service_health_collect.py:275`
- `tests/test_service_health_collect.py:289`
- `tests/test_service_health_collect.py:305`
