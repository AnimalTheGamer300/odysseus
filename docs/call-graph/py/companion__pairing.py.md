# `companion/pairing.py` — definitions & call sites

10 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_valid_companion_client_host` — function, line 40
- **called from:**
- `companion/pairing.py:104`

## `parse_companion_base_url` — function, line 70
- **called from:**
- `companion/pairing.py:119`
- `tests/test_companion_pairing.py:139`
- `tests/test_companion_pairing.py:207`

## `configured_companion_origin` — function, line 114
- **called from:**
- `companion/routes.py:204`

## `default_port` — function, line 122
- **called from:**
- `companion/routes.py:217`

## `lan_ip_candidates` — function, line 131
- **called from:**
- `companion/routes.py:215`

## `_add` — function, line 140
- **called from:**
- `companion/pairing.py:147`
- `companion/pairing.py:155`
- `mcp_servers/email_server.py:3079`
- `mcp_servers/email_server.py:3083`
- `mcp_servers/email_server.py:3091`
- `routes/email/email_routes.py:6761`
- `routes/email/email_routes.py:6765`
- `routes/email/email_routes.py:6769`
- `routes/email/email_routes.py:7089`
- `routes/email/email_routes.py:7094`
- `routes/email/email_routes.py:7100`
- `routes/email/email_routes.py:7105`
- `tests/test_manage_mcp_command_allowlist.py:125`
- `tests/test_manage_mcp_command_allowlist.py:143`
- `tests/test_manage_mcp_command_allowlist.py:160`
- `tests/test_notes_reminder_temporal_redos.py:47`
- `tests/test_notes_reminder_temporal_redos.py:53`
- `static/js/emailLibrary/index.js:3723`
- `static/js/emailLibrary/index.js:3726`
- `static/js/emailLibrary/index.js:3738`

## `find_admin_user` — function, line 162
- **called from:**
- `tests/test_companion_pairing.py:218`

## `mint_token` — function, line 182
- **called from:**
- `companion/routes.py:76`
- `tests/test_companion_pairing.py:88`

## `pairing_payload` — function, line 208
- **called from:**
- `companion/routes.py:218`
- `tests/test_companion_pairing.py:116`

## `pairing_qr_png_data_uri` — function, line 213
- **called from:**
- `companion/routes.py:219`
