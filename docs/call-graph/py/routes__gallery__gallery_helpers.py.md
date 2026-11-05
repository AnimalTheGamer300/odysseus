# `routes/gallery/gallery_helpers.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `GalleryPatch` — class, line 21
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_extract_exif` — function, line 29
- **called from:**
- `routes/gallery/gallery_routes.py:910`

## `_to_deg` — function, line 74
- **called from:**
- `routes/gallery/gallery_helpers.py:78`
- `routes/gallery/gallery_helpers.py:79`

## `_image_to_dict` — function, line 96
- **called from:**
- `routes/gallery/gallery_routes.py:1305`
- `routes/gallery/gallery_routes.py:1446`
- `routes/gallery/gallery_routes.py:1489`

## `_owner_filter` — function, line 125
- **called from:**
- `routes/gallery/gallery_routes.py:1166`
- `routes/gallery/gallery_routes.py:1199`
- `routes/gallery/gallery_routes.py:1212`
- `routes/gallery/gallery_routes.py:1222`
- `routes/gallery/gallery_routes.py:1328`
- `routes/gallery/gallery_routes.py:1335`
- `routes/gallery/gallery_routes.py:1340`
- `routes/gallery/gallery_routes.py:1347`
- `routes/gallery/gallery_routes.py:1390`
- `routes/gallery/gallery_routes.py:1391`
- `routes/gallery/gallery_routes.py:1392`
- `routes/gallery/gallery_routes.py:1420`
- `routes/gallery/gallery_routes.py:1564`
- `routes/gallery/gallery_routes.py:1589`
- `routes/gallery/gallery_routes.py:1616`
- `src/session_search.py:240`
- `src/session_search.py:278`
- `tests/test_gallery_owner_filter_single_user.py:41`
- `tests/test_gallery_owner_filter_single_user.py:51`
- `tests/test_gallery_owner_filter_single_user.py:52`
- `tests/test_gallery_owner_filter_single_user.py:62`
- `tests/test_null_owner_gates.py:150`
- `tests/test_null_owner_gates.py:159`
- `tests/test_null_owner_gates.py:167`

## `_human_size` — function, line 140
- **called from:**
- `routes/gallery/gallery_routes.py:1400`
