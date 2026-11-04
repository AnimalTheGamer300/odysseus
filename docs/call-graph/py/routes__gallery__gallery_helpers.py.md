# `routes/gallery/gallery_helpers.py` — definitions & call sites

6 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `GalleryPatch` — class, line 21
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `_extract_exif` — function, line 29
- **called from:**
- `routes/gallery/gallery_routes.py:404`

## `_to_deg` — function, line 74
- **called from:**
- `routes/gallery/gallery_helpers.py:78`
- `routes/gallery/gallery_helpers.py:79`

## `_image_to_dict` — function, line 96
- **called from:**
- `routes/gallery/gallery_routes.py:795`
- `routes/gallery/gallery_routes.py:936`
- `routes/gallery/gallery_routes.py:979`

## `_owner_filter` — function, line 125
- **called from:**
- `routes/gallery/gallery_routes.py:660`
- `routes/gallery/gallery_routes.py:693`
- `routes/gallery/gallery_routes.py:706`
- `routes/gallery/gallery_routes.py:716`
- `routes/gallery/gallery_routes.py:818`
- `routes/gallery/gallery_routes.py:825`
- `routes/gallery/gallery_routes.py:830`
- `routes/gallery/gallery_routes.py:837`
- `routes/gallery/gallery_routes.py:880`
- `routes/gallery/gallery_routes.py:881`
- `routes/gallery/gallery_routes.py:882`
- `routes/gallery/gallery_routes.py:910`
- `routes/gallery/gallery_routes.py:1054`
- `routes/gallery/gallery_routes.py:1079`
- `routes/gallery/gallery_routes.py:1106`
- `src/session_search.py:214`
- `tests/test_gallery_owner_filter_single_user.py:41`
- `tests/test_gallery_owner_filter_single_user.py:51`
- `tests/test_gallery_owner_filter_single_user.py:52`
- `tests/test_gallery_owner_filter_single_user.py:62`
- `tests/test_null_owner_gates.py:150`
- `tests/test_null_owner_gates.py:159`
- `tests/test_null_owner_gates.py:167`

## `_human_size` — function, line 140
- **called from:**
- `routes/gallery/gallery_routes.py:890`
