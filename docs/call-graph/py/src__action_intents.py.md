# `src/action_intents.py` — definitions & call sites

3 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `ToolIntent` — class, line 16
- decorator: `dataclass(frozen=True)`
- **called from:**
- `routes/chat_routes.py:1459`
- `src/action_intents.py:148`
- `src/action_intents.py:150`
- `src/action_intents.py:153`
- `src/action_intents.py:154`

## `classify_tool_intent` — function, line 145
- **called from:**
- `src/action_intents.py:164`
- `tests/test_action_intents.py:6`
- `tests/test_action_intents.py:56`
- `tests/test_action_intents.py:68`
- `tests/test_action_intents.py:77`
- `tests/test_action_intents.py:83`
- `tests/test_action_intents.py:84`
- `tests/test_action_intents.py:85`
- `tests/test_chat_route_tool_policy.py:233`
- `tests/test_chat_route_tool_policy.py:247`

## `message_needs_tools` — function, line 157
- **called from:**
- `tests/test_action_intents.py:5`
- `tests/test_action_intents.py:12`
- `tests/test_action_intents.py:13`
- `tests/test_action_intents.py:14`
- `tests/test_action_intents.py:15`
- `tests/test_action_intents.py:16`
- `tests/test_action_intents.py:17`
- `tests/test_action_intents.py:18`
- `tests/test_action_intents.py:21`
- `tests/test_action_intents.py:27`
- `tests/test_action_intents.py:28`
- `tests/test_action_intents.py:29`
- `tests/test_action_intents.py:30`
- `tests/test_action_intents.py:31`
- `tests/test_action_intents.py:35`
- `tests/test_action_intents.py:36`
- `tests/test_action_intents.py:37`
- `tests/test_action_intents.py:41`
- `tests/test_action_intents.py:42`
- `tests/test_action_intents.py:43`
- `tests/test_action_intents.py:44`
- `tests/test_action_intents.py:48`
- `tests/test_action_intents.py:49`
- `tests/test_action_intents.py:53`
- `tests/test_action_intents.py:54`
- `tests/test_action_intents.py:55`
- `tests/test_action_intents.py:74`
- `tests/test_action_intents.py:75`
- `tests/test_action_intents.py:76`
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
