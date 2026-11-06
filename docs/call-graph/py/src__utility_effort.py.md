# `src/utility_effort.py` — definitions & call sites

9 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `utility_routes` — function, line 18
- **called from:**
- `src/utility_effort.py:83`

## `configured_effort` — function, line 32
- **called from:**
- `src/utility_effort.py:82`
- `src/utility_effort.py:116`
- `src/utility_effort.py:139`

## `fallback_route_efforts` — function, line 39
- **called from:**
- `src/utility_effort.py:73`
- `src/utility_effort.py:141`

## `effort_for_route` — function, line 71
- **called from:**
- `src/utility_effort.py:119`
- `src/utility_effort.py:147`
- `tests/test_utility_reasoning_effort.py:467`
- `tests/test_utility_reasoning_effort.py:468`

## `session_effort` — function, line 90
- **called from:**
- `src/utility_effort.py:122`

## `_is_session_route` — function, line 98
- **called from:**
- `src/utility_effort.py:123`

## `effort_for_call` — function, line 108
- **called from:**
- `routes/chat_helpers.py:774`
- `routes/email/email_helpers.py:462`
- `routes/email/email_routes.py:6566`
- `routes/history/history_routes.py:1548`
- `routes/memory/memory_routes.py:274`
- `routes/memory/memory_routes.py:473`
- `routes/session_routes.py:1399`
- `routes/session_routes.py:1594`
- `services/memory/memory_extractor.py:693`
- `services/memory/memory_extractor.py:951`
- `services/memory/memory_extractor.py:1039`
- `services/memory/skill_extractor.py:208`
- `src/context_compactor.py:798`
- `tests/test_utility_reasoning_effort.py:206`
- `tests/test_utility_reasoning_effort.py:207`
- `tests/test_utility_reasoning_effort.py:212`
- `tests/test_utility_reasoning_effort.py:213`
- `tests/test_utility_reasoning_effort.py:217`
- `tests/test_utility_reasoning_effort.py:219`
- `tests/test_utility_reasoning_effort.py:223`
- `tests/test_utility_reasoning_effort.py:224`
- `tests/test_utility_reasoning_effort.py:228`
- `tests/test_utility_reasoning_effort.py:229`
- `tests/test_utility_reasoning_effort.py:233`
- `tests/test_utility_reasoning_effort.py:238`
- `tests/test_utility_reasoning_effort.py:242`
- `tests/test_utility_reasoning_effort.py:247`
- `tests/test_utility_reasoning_effort.py:251`
- `tests/test_utility_reasoning_effort.py:259`

## `candidate_effort_factory` — function, line 132
- **called from:**
- `routes/email/email_routes.py:6802`
- `src/task_endpoint.py:111`
- `tests/test_utility_reasoning_effort.py:239`
- `tests/test_utility_reasoning_effort.py:243`
- `tests/test_utility_reasoning_effort.py:439`
- `tests/test_utility_reasoning_effort.py:441`
- `tests/test_utility_reasoning_effort.py:444`
- `tests/test_utility_reasoning_effort.py:465`

## `factory` — function, line 146
- **called from:**
- `tests/test_admin_listing_authorization.py:63`
- `tests/test_background_tool_jobs.py:16`
- `tests/test_calendar_default_transaction.py:79`
- `tests/test_calendar_default_transaction.py:180`
- `tests/test_calendar_default_transaction.py:225`
- `tests/test_calendar_default_transaction.py:251`
- `tests/test_calendar_default_transaction.py:295`
- `tests/test_calendar_default_transaction.py:499`
- `tests/test_calendar_default_transaction.py:511`
- `tests/test_calendar_default_transaction.py:526`
- `tests/test_chat_document_owner_context.py:58`
- `tests/test_chat_document_owner_context.py:94`
- `tests/test_chat_document_owner_context.py:115`
- `tests/test_chat_helpers.py:511`
- `tests/test_chat_helpers.py:565`
- `tests/test_chat_helpers.py:602`
- `tests/test_chat_image_preservation.py:20`
- `tests/test_chat_image_preservation.py:32`
- `tests/test_chat_image_preservation.py:48`
- `tests/test_chat_tidy_content_preservation.py:60`
- `tests/test_chat_tidy_content_preservation.py:75`
- `tests/test_chat_tidy_content_preservation.py:79`
- `tests/test_chat_tidy_content_preservation.py:90`
- `tests/test_chat_tidy_content_preservation.py:107`
- `tests/test_chat_tidy_content_preservation.py:120`
- `tests/test_chat_tidy_content_preservation.py:146`
- `tests/test_chatgpt_session_binding.py:26`
- `tests/test_chatgpt_session_binding.py:49`
- `tests/test_chatgpt_session_binding.py:65`
- `tests/test_chatgpt_session_binding.py:79`
- `tests/test_chatgpt_session_binding.py:92`
- `tests/test_chatgpt_session_binding.py:103`
- `tests/test_chatgpt_session_binding.py:130`
- `tests/test_chatgpt_subscription_device_flow_multi_account.py:174`
- `tests/test_chatgpt_subscription_usage.py:26`
- `tests/test_cleanup_transcript_preservation.py:36`
- `tests/test_cleanup_transcript_preservation.py:67`
- `tests/test_cleanup_transcript_preservation.py:79`
- `tests/test_cleanup_transcript_preservation.py:91`
- `tests/test_cleanup_transcript_preservation.py:107`
- `tests/test_cleanup_transcript_preservation.py:115`
- `tests/test_cleanup_transcript_preservation.py:128`
- `tests/test_cleanup_transcript_preservation.py:157`
- `tests/test_cleanup_transcript_preservation.py:166`
- `tests/test_cleanup_transcript_preservation.py:206`
- `tests/test_cleanup_transcript_preservation.py:224`
- `tests/test_cleanup_transcript_preservation.py:233`
- `tests/test_cleanup_transcript_preservation.py:260`
- `tests/test_cleanup_transcript_preservation.py:276`
- `tests/test_cleanup_transcript_preservation.py:306`
- `tests/test_cleanup_transcript_preservation.py:318`
- `tests/test_cleanup_transcript_preservation.py:358`
- `tests/test_cleanup_transcript_preservation.py:375`
- `tests/test_cookbook_endpoint_registration.py:75`
- `tests/test_cookbook_endpoint_registration.py:474`
- `tests/test_cost_tracking.py:142`
- `tests/test_cost_tracking.py:158`
- `tests/test_cost_tracking.py:176`
- `tests/test_cost_tracking.py:187`
- `tests/test_default_chat_model_filter.py:36`
- … +50 more (grep the name in repo)
