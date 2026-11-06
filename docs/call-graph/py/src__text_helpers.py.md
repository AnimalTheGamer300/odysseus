# `src/text_helpers.py` — definitions & call sites

7 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_strip_reasoning_prose` — function, line 70
- **called from:**
- `src/text_helpers.py:188`

## `_sub_delimited` — function, line 92
- **called from:**
- `src/text_helpers.py:135`
- `src/text_helpers.py:138`
- `src/text_helpers.py:180`
- `src/text_helpers.py:209`

## `normalize_thinking_markup` — function, line 117
- **called from:**
- `routes/chat_helpers.py:1668`
- `routes/chat_helpers.py:1800`
- `src/text_helpers.py:173`
- `tests/test_redos_llm_parsers.py:43`
- `tests/test_redos_llm_parsers.py:56`

## `_replace_gemma_thought` — function, line 130
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `strip_think` — function, line 146
- **called from:**
- `routes/calendar_routes.py:1879`
- `routes/chat_helpers.py:689`
- `routes/chat_helpers.py:784`
- `routes/session_routes.py:863`
- `services/memory/memory_extractor.py:956`
- `src/builtin_actions.py:736`
- `src/research_utils.py:23`
- `src/task_scheduler.py:1825`
- `src/text_helpers.py:195`
- `tests/test_redos_llm_parsers.py:42`
- `tests/test_redos_llm_parsers.py:48`
- `tests/test_redos_llm_parsers.py:168`
- `tests/test_redos_llm_parsers.py:169`
- `tests/test_redos_llm_parsers.py:170`
- `tests/test_redos_llm_parsers.py:171`
- `tests/test_redos_llm_parsers.py:172`
- `tests/test_strip_reasoning_prose_dataloss.py:12`
- `tests/test_strip_reasoning_prose_dataloss.py:19`
- `tests/test_strip_reasoning_prose_dataloss.py:25`
- `tests/test_strip_think.py:6`
- `tests/test_strip_think.py:7`
- `tests/test_strip_think.py:8`
- `tests/test_strip_think.py:11`
- `tests/test_strip_think.py:12`
- `tests/test_strip_think.py:15`
- `tests/test_strip_think.py:16`
- `tests/test_strip_think.py:19`
- `tests/test_strip_think.py:22`
- `tests/test_strip_think.py:25`
- `tests/test_strip_think.py:29`
- `tests/test_strip_think.py:34`
- `tests/test_strip_think.py:39`
- `tests/test_strip_think.py:44`

## `strip_thinking` — function, line 194
- **called from:**
- `routes/chat_routes.py:5781`
- `src/background_tool_jobs.py:162`
- `src/deep_research.py:640`
- `src/deep_research.py:1758`
- `src/research_handler.py:181`
- `src/research_handler.py:208`
- `src/research_handler.py:1081`
- `src/research_handler.py:1135`
- `src/task_scheduler.py:2312`
- `src/visual_report.py:2750`
- `tests/test_research_utils.py:9`
- `tests/test_research_utils.py:13`
- `tests/test_research_utils.py:17`
- `tests/test_research_utils.py:23`
- `tests/test_research_utils.py:28`
- `tests/test_research_utils.py:33`
- `tests/test_research_utils.py:36`
- `tests/test_research_utils.py:40`
- `tests/test_research_utils.py:44`
- `tests/test_research_utils.py:50`

## `strip_closed_think_blocks` — function, line 202
- **called from:**
- `services/memory/memory_extractor.py:1047`
- `services/skills/evaluation.py:55`
- `services/skills/evaluation.py:297`
- `services/skills/evaluation.py:392`
- `services/skills/evaluation.py:453`
- `tests/test_redos_residual_python.py:45`
