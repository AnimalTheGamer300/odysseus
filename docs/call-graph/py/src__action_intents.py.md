# `src/action_intents.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolIntent` — class, line 16
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/chat_routes.py:3191`
- `src/action_intents.py:194`
- `src/action_intents.py:196`
- `src/action_intents.py:199`
- `src/action_intents.py:200`

## `classify_tool_intent` — function, line 191
- **called from:**
- `src/action_intents.py:210`
- `src/turn_contract.py:4302`
- `tests/test_action_intents.py:6`
- `tests/test_action_intents.py:57`
- `tests/test_action_intents.py:61`
- `tests/test_action_intents.py:68`
- `tests/test_action_intents.py:82`
- `tests/test_action_intents.py:93`
- `tests/test_action_intents.py:96`
- `tests/test_action_intents.py:112`
- `tests/test_action_intents.py:132`
- `tests/test_action_intents.py:146`
- `tests/test_action_intents.py:152`
- `tests/test_action_intents.py:153`
- `tests/test_action_intents.py:154`
- `tests/test_action_intents_calendar.py:5`
- `tests/test_action_intents_calendar.py:12`
- `tests/test_action_intents_calendar.py:19`
- `tests/test_chat_route_tool_policy.py:607`
- `tests/test_chat_route_tool_policy.py:638`

## `message_needs_tools` — function, line 203
- **called from:**
- `tests/test_action_intents.py:5`
- `tests/test_action_intents.py:12`
- `tests/test_action_intents.py:13`
- `tests/test_action_intents.py:14`
- `tests/test_action_intents.py:15`
- `tests/test_action_intents.py:16`
- `tests/test_action_intents.py:17`
- `tests/test_action_intents.py:18`
- `tests/test_action_intents.py:19`
- `tests/test_action_intents.py:22`
- `tests/test_action_intents.py:28`
- `tests/test_action_intents.py:29`
- `tests/test_action_intents.py:30`
- `tests/test_action_intents.py:31`
- `tests/test_action_intents.py:32`
- `tests/test_action_intents.py:36`
- `tests/test_action_intents.py:37`
- `tests/test_action_intents.py:38`
- `tests/test_action_intents.py:42`
- `tests/test_action_intents.py:43`
- `tests/test_action_intents.py:44`
- `tests/test_action_intents.py:45`
- `tests/test_action_intents.py:49`
- `tests/test_action_intents.py:50`
- `tests/test_action_intents.py:54`
- `tests/test_action_intents.py:55`
- `tests/test_action_intents.py:56`
- `tests/test_action_intents.py:118`
- `tests/test_action_intents.py:119`
- `tests/test_action_intents.py:138`
- `tests/test_action_intents.py:139`
- `tests/test_action_intents.py:143`
- `tests/test_action_intents.py:144`
- `tests/test_action_intents.py:145`
- `tests/test_action_intents_shell_verbs.py:16`
- `tests/test_action_intents_shell_verbs.py:17`
- `tests/test_action_intents_shell_verbs.py:18`
- `tests/test_action_intents_shell_verbs.py:22`
- `tests/test_action_intents_shell_verbs.py:23`
- `tests/test_action_intents_shell_verbs.py:27`
- `tests/test_action_intents_shell_verbs.py:28`
- `tests/test_action_intents_shell_verbs.py:29`
- `tests/test_action_intents_shell_verbs.py:30`
- `tests/test_action_intents_shell_verbs.py:34`
- `tests/test_action_intents_shell_verbs.py:35`
