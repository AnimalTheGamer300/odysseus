# `src/research_utils.py` — definitions & call sites

2 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `strip_thinking` — function, line 12
- **called from:**
- `routes/chat_routes.py:5762`
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

## `is_low_quality` — function, line 62
- **called from:**
- `services/research/research_handler.py:194`
- `services/research/research_handler.py:364`
- `src/deep_research.py:1388`
- `src/research_handler.py:662`
- `src/research_handler.py:685`
- `tests/test_research_utils.py:57`
- `tests/test_research_utils.py:60`
- `tests/test_research_utils.py:63`
- `tests/test_research_utils.py:66`
- `tests/test_research_utils.py:69`
- `tests/test_research_utils.py:72`
- `tests/test_research_utils.py:75`
- `tests/test_research_utils.py:78`
- `tests/test_research_utils.py:81`
- `tests/test_research_utils.py:87`
- `tests/test_research_utils.py:90`
- `tests/test_research_utils.py:93`
- `tests/test_research_utils.py:97`
- `tests/test_research_utils_low_quality_nonstring.py:9`
- `tests/test_research_utils_low_quality_nonstring.py:10`
- `tests/test_research_utils_low_quality_nonstring.py:11`
- `tests/test_research_utils_low_quality_nonstring.py:15`
- `tests/test_research_utils_low_quality_nonstring.py:16`
