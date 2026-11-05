# `src/editor_style_guide.py` — definitions & call sites

27 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_adj` — function, line 134
- **called from:**
- `src/editor_style_guide.py:184`
- `src/editor_style_guide.py:185`
- `src/editor_style_guide.py:186`
- `src/editor_style_guide.py:223`
- `src/editor_style_guide.py:230`
- `src/editor_style_guide.py:237`
- `src/editor_style_guide.py:252`
- `src/editor_style_guide.py:262`
- `src/editor_style_guide.py:401`
- `src/editor_style_guide.py:402`
- `src/editor_style_guide.py:403`
- `src/editor_style_guide.py:412`
- `src/editor_style_guide.py:413`
- `src/editor_style_guide.py:414`
- `src/editor_style_guide.py:425`
- `src/editor_style_guide.py:426`
- `src/editor_style_guide.py:427`

## `_filter` — function, line 138
- **called from:**
- `src/editor_style_guide.py:187`
- `src/editor_style_guide.py:253`
- `src/editor_style_guide.py:254`
- `src/editor_style_guide.py:268`
- `src/editor_style_guide.py:415`
- `src/editor_style_guide.py:428`

## `match` — function, line 306
- **called from:**
- `app.py:336`
- `core/platform_compat.py:346`
- `routes/_validators.py:15`
- `routes/auth_routes.py:897`
- `routes/calendar_routes.py:425`
- `routes/calendar_routes.py:435`
- `routes/calendar_routes.py:448`
- `routes/calendar_routes.py:458`
- `routes/calendar_routes.py:546`
- `routes/calendar_routes.py:561`
- `routes/calendar_routes.py:577`
- `routes/calendar_routes.py:591`
- `routes/calendar_routes.py:604`
- `routes/chat_helpers.py:43`
- `routes/chat_helpers.py:146`
- `routes/chat_helpers.py:148`
- `routes/chat_helpers.py:560`
- `routes/chat_helpers.py:1681`
- `routes/chat_helpers.py:1695`
- `routes/chat_helpers.py:1704`
- `routes/chat_helpers.py:1721`
- `routes/chat_helpers.py:1732`
- `routes/chat_helpers.py:1809`
- `routes/chat_helpers.py:1825`
- `routes/chat_helpers.py:1854`
- `routes/chat_routes.py:307`
- `routes/cookbook_helpers.py:59`
- `routes/cookbook_helpers.py:67`
- `routes/cookbook_helpers.py:75`
- `routes/cookbook_helpers.py:75`
- `routes/cookbook_helpers.py:75`
- `routes/cookbook_helpers.py:83`
- `routes/cookbook_helpers.py:91`
- `routes/cookbook_helpers.py:120`
- `routes/cookbook_helpers.py:120`
- `routes/cookbook_helpers.py:167`
- `routes/cookbook_helpers.py:688`
- `routes/cookbook_helpers.py:694`
- `routes/cookbook_helpers.py:731`
- `routes/cookbook_helpers.py:776`
- `routes/cookbook_routes.py:527`
- `routes/cookbook_routes.py:528`
- `routes/cookbook_routes.py:606`
- `routes/cookbook_routes.py:607`
- `routes/cookbook_routes.py:3634`
- `routes/cookbook_routes.py:4263`
- `routes/document/document_helpers.py:215`
- `routes/document/document_routes.py:757`
- `routes/document/document_routes.py:1137`
- `routes/email/email_helpers.py:507`
- `routes/email/email_pollers.py:842`
- `routes/email/email_routes.py:834`
- `routes/email/email_routes.py:1590`
- `routes/email/email_routes.py:1625`
- `routes/email/email_routes.py:1626`
- `routes/email/email_routes.py:1627`
- `routes/email/email_routes.py:1680`
- `routes/email/email_routes.py:3610`
- `routes/emoji_routes.py:78`
- `routes/note/note_routes.py:285`
- … +550 more (grep the name in repo)

## `is_ambiguous` — function, line 315
- **called from:**
- `src/editor_style_guide.py:359`
- `tests/test_photo_editor_style_guide.py:123`
- `tests/test_photo_editor_style_guide.py:125`

## `ask_user_plan` — function, line 324
- **called from:**
- `routes/editor_agent_routes.py:1172`
- `routes/editor_agent_routes.py:1193`
- `src/editor_style_guide.py:360`

## `has_concrete_intent` — function, line 338
- **called from:**
- `routes/editor_agent_routes.py:1170`

## `fallback_plan` — function, line 350
- **called from:**
- `routes/editor_agent_routes.py:1185`
- `tests/test_photo_editor_style_guide.py:62`
- `tests/test_photo_editor_style_guide.py:80`
- `tests/test_photo_editor_style_guide.py:86`
- `tests/test_photo_editor_style_guide.py:92`
- `tests/test_photo_editor_style_guide.py:99`
- `tests/test_photo_editor_style_guide.py:102`
- `tests/test_photo_editor_style_guide.py:107`
- `tests/test_photo_editor_style_guide.py:117`
- `tests/test_photo_editor_style_guide.py:226`
- `tests/test_photo_editor_style_guide.py:239`

## `color_for_name` — function, line 380
- **called from:**
- `src/editor_style_guide.py:585`
- `src/editor_style_guide.py:589`
- `src/editor_style_guide.py:591`
- `src/editor_style_guide.py:651`
- `src/editor_style_guide.py:670`
- `tests/test_photo_editor_style_guide.py:496`

## `look_plan` — function, line 454
- **called from:**
- `src/editor_style_guide.py:345`
- `src/editor_style_guide.py:638`
- `tests/test_photo_editor_style_guide.py:595`
- `tests/test_photo_editor_style_guide.py:606`
- `tests/test_photo_editor_style_guide.py:622`

## `_hex_rgb01` — function, line 496
- **called from:**
- `src/editor_style_guide.py:507`
- `src/editor_style_guide.py:538`

## `_hue_degrees` — function, line 506
- **called from:**
- `src/editor_style_guide.py:525`
- `src/editor_style_guide.py:526`
- `src/editor_style_guide.py:602`

## `_hue_delta` — function, line 524
- **called from:**
- `src/editor_style_guide.py:601`

## `_is_chromatic` — function, line 532
- **called from:**
- `src/editor_style_guide.py:600`

## `_recolor_object_phrase` — function, line 545
- **called from:**
- `src/editor_style_guide.py:592`
- `tests/test_photo_editor_style_guide.py:22`
- `tests/test_photo_editor_style_guide.py:29`
- `tests/test_photo_editor_style_guide.py:30`

## `recolor_plan` — function, line 566
- **called from:**
- `routes/editor_agent_routes.py:921`
- `routes/editor_agent_routes.py:1510`
- `src/editor_style_guide.py:345`
- `src/editor_style_guide.py:641`
- `tests/test_photo_editor_style_guide.py:491`
- `tests/test_photo_editor_style_guide.py:503`
- `tests/test_photo_editor_style_guide.py:511`
- `tests/test_photo_editor_style_guide.py:518`
- `tests/test_photo_editor_style_guide.py:566`
- `tests/test_photo_editor_style_guide.py:573`
- `tests/test_photo_editor_style_guide.py:586`

## `structural_plan` — function, line 630
- **called from:**
- `routes/editor_agent_routes.py:947`
- `src/editor_style_guide.py:345`
- `tests/test_photo_editor_style_guide.py:414`
- `tests/test_photo_editor_style_guide.py:443`
- `tests/test_photo_editor_style_guide.py:448`
- `tests/test_photo_editor_style_guide.py:450`
- `tests/test_photo_editor_style_guide.py:452`
- `tests/test_photo_editor_style_guide.py:454`
- `tests/test_photo_editor_style_guide.py:456`
- `tests/test_photo_editor_style_guide.py:458`
- `tests/test_photo_editor_style_guide.py:460`
- `tests/test_photo_editor_style_guide.py:614`
- `tests/test_photo_editor_style_guide.py:616`

## `_is_global_lift` — function, line 742
- **called from:**
- `src/editor_style_guide.py:811`
- `src/editor_style_guide.py:862`
- `src/editor_style_guide.py:875`

## `_is_shadows_highlights` — function, line 762
- **called from:**
- `src/editor_style_guide.py:815`

## `_is_masked_recolor` — function, line 769
- **called from:**
- `src/editor_style_guide.py:871`

## `_is_whole_image_adjustment` — function, line 785
- **called from:**
- `src/editor_style_guide.py:875`

## `collapse_global_lifts` — function, line 799
- **called from:**
- `src/editor_style_guide.py:853`
- `tests/test_photo_editor_style_guide.py:138`
- `tests/test_photo_editor_style_guide.py:148`
- `tests/test_photo_editor_style_guide.py:159`
- `tests/test_photo_editor_style_guide.py:165`

## `_clone` — function, line 842
- **called from:**
- `src/editor_style_guide.py:908`

## `enforce_guards` — function, line 846
- **called from:**
- `routes/editor_agent_routes.py:263`
- `routes/editor_agent_routes.py:1187`
- `routes/editor_agent_routes.py:1482`
- `routes/editor_agent_routes.py:1499`
- `routes/editor_agent_routes.py:1515`
- `routes/editor_agent_routes.py:1773`
- `routes/editor_agent_routes.py:1780`
- `src/editor_style_guide.py:357`
- `tests/test_photo_editor_style_guide.py:271`
- `tests/test_photo_editor_style_guide.py:279`
- `tests/test_photo_editor_style_guide.py:533`
- `tests/test_photo_editor_style_guide.py:550`
- `tests/test_photo_editor_style_guide.py:561`

## `strengthen` — function, line 881
- **called from:**
- `routes/editor_agent_routes.py:1486`
- `routes/editor_agent_routes.py:1761`
- `tests/test_photo_editor_style_guide.py:257`
- `tests/test_photo_editor_style_guide.py:262`

## `_step_signature` — function, line 912
- **called from:**
- `src/editor_style_guide.py:905`
- `src/editor_style_guide.py:906`

## `guidance` — function, line 926
- **called from:**
- `routes/editor_agent_routes.py:104`
- `src/editor_style_guide.py:1107`
- `tests/test_photo_editor_style_guide.py:218`
- `tests/test_photo_editor_style_guide.py:219`
- `tests/test_photo_editor_style_guide.py:300`

## `as_json` — function, line 1032
- **called from:**
- `routes/editor_agent_routes.py:1974`
- `tests/test_photo_editor_style_guide.py:384`
- `tests/test_photo_editor_style_guide.py:475`
- `tests/test_photo_editor_style_guide.py:649`
