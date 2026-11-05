# `static/js/emailLibrary/settingsPage.js` — definitions & call sites

38 definitions (regex-based, best-effort).
**Exports:** `_EMAIL_SETTINGS_ICON`, `_bindEmailSettingsPageControls`, `_disableInlineImages`, `_emailCleanupSettingsHtml`, `_emailDisplaySettingsHtml`, `_emailSettingsAccountSelectHtml`, `_emailSettingsFormHtml`, `_emailSettingsLoadingHtml`, `_emailWritingStyleHtml`, `_fetchEmailSettingsConfig`, `_fetchEmailWritingStyle`, `_hideEmailSettingsPage`, `_isAutoReplyActiveForCurrentAccount`, `_readEmailInlineImagesPreference`, `_showEmailSettingsPage`, `_syncAutoReplyCalendarEvent`, `_syncEmailAutoReplyTitle`, `_syncEmailSettingsAccountPicker`

## `_emailInlineImagesStorageKey` — function, line 36
- **called from:**
- `static/js/emailLibrary/settingsPage.js:36`
- `static/js/emailLibrary/settingsPage.js:42`
- `static/js/emailLibrary/settingsPage.js:51`

## `_readEmailInlineImagesPreference` — function, line 40
- **called from:**
- `static/js/emailLibrary/index.js:2406`
- `static/js/emailLibrary/index.js:3125`
- `static/js/emailLibrary/index.js:3150`
- `static/js/emailLibrary/index.js:3211`
- `static/js/emailLibrary/settingsPage.js:40`

## `_writeEmailInlineImagesPreference` — function, line 49
- **called from:**
- `static/js/emailLibrary/settingsPage.js:49`
- `static/js/emailLibrary/settingsPage.js:57`
- `static/js/emailLibrary/settingsPage.js:268`
- `static/js/emailLibrary/settingsPage.js:658`
- `static/js/emailLibrary/settingsPage.js:673`

## `_disableInlineImages` — function, line 55
- **called from:**
- `static/js/emailLibrary/bodyRender.js:390`
- `static/js/emailLibrary/settingsPage.js:55`

## `_setEmailSaveIcon` — function, line 81
- **called from:**
- `static/js/emailLibrary/settingsPage.js:81`
- `static/js/emailLibrary/settingsPage.js:704`
- `static/js/emailLibrary/settingsPage.js:746`
- `static/js/emailLibrary/settingsPage.js:754`
- `static/js/emailLibrary/settingsPage.js:793`
- `static/js/emailLibrary/settingsPage.js:812`
- `static/js/emailLibrary/settingsPage.js:814`

## `_normalizeAutoReplyConfig` — function, line 90
- **called from:**
- `static/js/emailLibrary/settingsPage.js:90`
- `static/js/emailLibrary/settingsPage.js:238`
- `static/js/emailLibrary/settingsPage.js:266`

## `_autoReplyDateValue` — function, line 107
- **called from:**
- `static/js/emailLibrary/settingsPage.js:107`
- `static/js/emailLibrary/settingsPage.js:148`
- `static/js/emailLibrary/settingsPage.js:149`
- `static/js/emailLibrary/settingsPage.js:161`
- `static/js/emailLibrary/settingsPage.js:162`
- `static/js/emailLibrary/settingsPage.js:242`
- `static/js/emailLibrary/settingsPage.js:243`
- `static/js/emailLibrary/settingsPage.js:322`
- `static/js/emailLibrary/settingsPage.js:323`

## `_todayDateInputValue` — function, line 113
- **called from:**
- `static/js/emailLibrary/settingsPage.js:113`
- `static/js/emailLibrary/settingsPage.js:148`
- `static/js/emailLibrary/settingsPage.js:161`
- `static/js/emailLibrary/settingsPage.js:684`

## `pad` — arrow, line 115
- **called from:**
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/modalManager.js:716`

## `_autoReplyCalendarKey` — function, line 122
- **called from:**
- `static/js/emailLibrary/settingsPage.js:122`
- `static/js/emailLibrary/settingsPage.js:128`
- `static/js/emailLibrary/settingsPage.js:134`
- `static/js/emailLibrary/settingsPage.js:135`

## `_readAutoReplyCalendarUid` — function, line 126
- **called from:**
- `static/js/emailLibrary/settingsPage.js:126`
- `static/js/emailLibrary/settingsPage.js:184`

## `_writeAutoReplyCalendarUid` — function, line 131
- **called from:**
- `static/js/emailLibrary/settingsPage.js:131`
- `static/js/emailLibrary/settingsPage.js:199`
- `static/js/emailLibrary/settingsPage.js:206`
- `static/js/emailLibrary/settingsPage.js:214`
- `static/js/emailLibrary/settingsPage.js:222`

## `_addLocalCalendarDays` — function, line 139
- **called from:**
- `static/js/emailLibrary/settingsPage.js:139`
- `static/js/emailLibrary/settingsPage.js:154`

## `pad` — arrow, line 143
- **called from:**
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/calendar.js:3787`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:6976`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/document.js:7000`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1249`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailInbox.js:1286`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:340`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/aiReply.js:401`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:116`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/emailLibrary/settingsPage.js:144`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/features/notes/domain/recurrence.js:69`
- `static/js/modalManager.js:716`

## `_autoReplyCalendarPayload` — function, line 147
- **called from:**
- `static/js/emailLibrary/settingsPage.js:147`
- `static/js/emailLibrary/settingsPage.js:203`

## `_findAutoReplyCalendarEventUids` — function, line 160
- **called from:**
- `static/js/emailLibrary/settingsPage.js:160`
- `static/js/emailLibrary/settingsPage.js:194`
- `static/js/emailLibrary/settingsPage.js:205`

## `_syncAutoReplyCalendarEventNow` — function, line 181
- **called from:**
- `static/js/emailLibrary/settingsPage.js:181`
- `static/js/emailLibrary/settingsPage.js:230`

## `request` — arrow, line 186
- **called from:**
- `routes/calendar_routes.py:1185`
- `routes/calendar_routes.py:1197`
- `routes/contacts/contacts_routes.py:376`
- `src/integrations.py:634`
- `src/tools/system.py:933`
- `tests/smoke/test_documents_rag_smoke.py:55`
- `tests/test_admin_listing_authorization.py:135`
- `tests/test_admin_routes_auth_disabled.py:215`
- `tests/test_caldav_redirect_hardening.py:82`
- `tests/test_caldav_redirect_hardening.py:98`
- `tests/test_caldav_redirect_hardening.py:112`
- `tests/test_caldav_redirect_hardening.py:115`
- `tests/test_review_20260923_fixes.py:512`
- `tests/test_skills_audit_characterization.py:467`
- `tests/test_skills_audit_characterization.py:468`
- `tests/test_skills_audit_services.py:83`
- `tests/test_skills_audit_services.py:136`
- `tests/test_skills_audit_services.py:340`
- `tests/test_skills_audit_services.py:361`
- `tests/test_skills_audit_services.py:373`
- `tests/test_skills_audit_services.py:385`
- `tests/test_wave3_local_control.py:47`
- `tests/test_wave3_local_control.py:60`
- `tests/test_wave3_local_control.py:63`
- `tests/test_wave3_local_control.py:243`
- `static/js/chat.js:2907`
- `static/js/chatRenderer.js:1493`
- `static/js/editor/nl-edit.js:78`
- `static/js/editor/nl-edit.js:82`
- `static/js/emailLibrary/settingsPage.js:196`
- `static/js/emailLibrary/settingsPage.js:209`
- `static/js/emailLibrary/settingsPage.js:217`
- `static/js/features/notes/infrastructure/http.js:5`
- `static/js/features/notes/infrastructure/http.js:10`
- `static/js/features/notes/infrastructure/http.js:15`
- `static/js/features/notes/infrastructure/http.js:20`
- `static/js/features/notes/infrastructure/http.js:21`
- `static/js/features/notes/infrastructure/http.js:22`
- `static/js/features/notes/infrastructure/http.js:24`
- `static/js/features/notes/infrastructure/http.js:25`
- `static/js/features/notes/infrastructure/http.js:26`
- `static/js/features/notes/infrastructure/http.js:27`
- `static/js/galleryEditor.js:691`
- `static/js/galleryEditor.js:1855`
- `static/js/galleryEditor.js:1898`
- `static/js/galleryEditor.js:2717`

## `_syncAutoReplyCalendarEvent` — function, line 226
- **called from:**
- `static/js/emailLibrary/index.js:3327`
- `static/js/emailLibrary/settingsPage.js:226`
- `static/js/emailLibrary/settingsPage.js:566`
- `static/js/emailLibrary/settingsPage.js:589`
- `static/js/emailLibrary/settingsPage.js:737`

## `_isAutoReplyActiveForCurrentAccount` — function, line 237
- **called from:**
- `static/js/emailLibrary/index.js:3324`
- `static/js/emailLibrary/index.js:4977`
- `static/js/emailLibrary/settingsPage.js:237`
- `static/js/emailLibrary/settingsPage.js:562`
- `static/js/emailLibrary/settingsPage.js:585`
- `static/js/emailLibrary/settingsPage.js:749`
- `static/js/emailLibrary/settingsPage.js:772`

## `_syncEmailAutoReplyTitle` — function, line 249
- **called from:**
- `static/js/emailLibrary/index.js:2552`
- `static/js/emailLibrary/index.js:3326`
- `static/js/emailLibrary/index.js:4968`
- `static/js/emailLibrary/index.js:4983`
- `static/js/emailLibrary/settingsPage.js:249`
- `static/js/emailLibrary/settingsPage.js:564`
- `static/js/emailLibrary/settingsPage.js:587`
- `static/js/emailLibrary/settingsPage.js:751`
- `static/js/emailLibrary/settingsPage.js:781`

## `_fetchEmailSettingsConfig` — function, line 261
- **called from:**
- `static/js/emailLibrary/index.js:3317`
- `static/js/emailLibrary/index.js:4971`
- `static/js/emailLibrary/settingsPage.js:261`
- `static/js/emailLibrary/settingsPage.js:553`
- `static/js/emailLibrary/settingsPage.js:581`

## `_fetchEmailWritingStyle` — function, line 272
- **called from:**
- `static/js/emailLibrary/index.js:3318`
- `static/js/emailLibrary/settingsPage.js:272`
- `static/js/emailLibrary/settingsPage.js:554`
- `static/js/emailLibrary/settingsPage.js:582`

## `_emailSettingsLoadingHtml` — function, line 281
- **called from:**
- `static/js/emailLibrary/index.js:3309`
- `static/js/emailLibrary/settingsPage.js:281`
- `static/js/emailLibrary/settingsPage.js:539`
- `static/js/emailLibrary/settingsPage.js:578`

## `_emailSettingsFormHtml` — function, line 295
- **called from:**
- `static/js/emailLibrary/index.js:3323`
- `static/js/emailLibrary/settingsPage.js:295`
- `static/js/emailLibrary/settingsPage.js:560`
- `static/js/emailLibrary/settingsPage.js:584`

## `_emailCleanupSettingsHtml` — function, line 352
- **called from:**
- `static/js/emailLibrary/index.js:3322`
- `static/js/emailLibrary/settingsPage.js:352`
- `static/js/emailLibrary/settingsPage.js:560`
- `static/js/emailLibrary/settingsPage.js:584`

## `_emailDisplaySettingsHtml` — function, line 385
- **called from:**
- `static/js/emailLibrary/index.js:3321`
- `static/js/emailLibrary/settingsPage.js:385`
- `static/js/emailLibrary/settingsPage.js:560`
- `static/js/emailLibrary/settingsPage.js:584`

## `_emailSettingsAccountSelectHtml` — function, line 426
- **called from:**
- `static/js/emailLibrary/index.js:3314`
- `static/js/emailLibrary/settingsPage.js:426`
- `static/js/emailLibrary/settingsPage.js:547`

## `_syncEmailSettingsAccountPicker` — function, line 460
- **called from:**
- `static/js/emailLibrary/index.js:3350`
- `static/js/emailLibrary/settingsPage.js:460`
- `static/js/emailLibrary/settingsPage.js:571`
- `static/js/emailLibrary/settingsPage.js:606`

## `_emailWritingStyleHtml` — function, line 491
- **called from:**
- `static/js/emailLibrary/index.js:3320`
- `static/js/emailLibrary/settingsPage.js:491`
- `static/js/emailLibrary/settingsPage.js:560`
- `static/js/emailLibrary/settingsPage.js:584`

## `_showEmailSettingsPage` — function, line 521
- **called from:**
- `static/js/emailLibrary/index.js:3376`
- `static/js/emailLibrary/settingsPage.js:521`

## `_bindEmailSettingsPageControls` — function, line 620
- **called from:**
- `static/js/emailLibrary/index.js:3338`
- `static/js/emailLibrary/settingsPage.js:590`
- `static/js/emailLibrary/settingsPage.js:617`
- `static/js/emailLibrary/settingsPage.js:620`

## `syncDisplayTagsState` — arrow, line 627
- **called from:**
- `static/js/emailLibrary/settingsPage.js:641`
- `static/js/emailLibrary/settingsPage.js:643`

## `syncInlineImagesState` — arrow, line 645
- **called from:**
- `static/js/emailLibrary/settingsPage.js:659`
- `static/js/emailLibrary/settingsPage.js:675`
- `static/js/emailLibrary/settingsPage.js:680`

## `seedAutoReplyStartDate` — arrow, line 683
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `syncEnabledState` — arrow, line 692
- **called from:**
- `static/js/emailLibrary/settingsPage.js:768`
- `static/js/emailLibrary/settingsPage.js:785`

## `saveAutoReplySettings` — arrow, line 700
- **called from:**
- `static/js/emailLibrary/settingsPage.js:783`
- `static/js/emailLibrary/settingsPage.js:787`

## `_hideEmailSettingsPage` — function, line 870
- **called from:**
- `static/js/emailLibrary/index.js:3000`
- `static/js/emailLibrary/index.js:3067`
- `static/js/emailLibrary/settingsPage.js:870`
