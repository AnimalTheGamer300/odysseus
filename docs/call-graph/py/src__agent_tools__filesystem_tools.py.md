# `src/agent_tools/filesystem_tools.py` — definitions & call sites

37 definitions. Callers = static call sites (`name(` / `.name(`) across the whole app scope (incl. tests).

## `_glob_to_regex` — function, line 23
- **called from:**
- `src/agent_tools/filesystem_tools.py:60`
- `src/agent_tools/filesystem_tools.py:631`

## `_python_grep_worker` — function, line 48
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `within` — function, line 74
- **called from:**
- `src/agent_tools/filesystem_tools.py:86`
- `src/agent_tools/filesystem_tools.py:86`

## `safe_file` — function, line 82
- **called from:**
- `src/agent_tools/filesystem_tools.py:121`

## `walk_files` — function, line 104
- **called from:**
- `src/agent_tools/filesystem_tools.py:118`

## `_unified_diff` — function, line 154
- **called from:**
- `src/agent_tools/filesystem_tools.py:237`
- `src/agent_tools/filesystem_tools.py:336`
- `src/agent_tools/filesystem_tools.py:402`

## `EditFileTool` — class, line 182
- **called from:**
- `src/agent_tools/__init__.py:45`
- `tests/test_edit_file.py:64`
- `tests/test_edit_file.py:75`
- `tests/test_edit_file.py:84`
- `tests/test_edit_file.py:87`
- `tests/test_edit_file.py:94`

## `EditFileTool.execute` — method (async), line 183
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `EditFileTool._apply` — method, line 204
- **called from:**
- `static/js/markdown.js:1469`
- `static/js/markdown.js:1473`
- `static/js/theme.js:719`

## `ReadFileTool` — class, line 242
- **called from:**
- `src/agent_tools/__init__.py:43`

## `ReadFileTool.execute` — method (async), line 243
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `ReadFileTool._read` — method, line 260
- **called from:**
- `services/hwfit/hardware.py:246`
- `services/hwfit/hardware.py:253`
- `services/hwfit/hardware.py:254`
- `services/hwfit/hardware.py:255`
- `services/hwfit/hardware.py:266`
- `tests/test_cookbook_dependency_completion_regression.py:12`
- `tests/test_cookbook_dependency_completion_regression.py:20`
- `tests/test_cookbook_dependency_completion_regression.py:34`
- `tests/test_cookbook_dependency_completion_regression.py:49`
- `tests/test_cookbook_dependency_completion_regression.py:60`
- `tests/test_cookbook_dependency_completion_regression.py:78`
- `tests/test_cookbook_dependency_completion_regression.py:92`
- `tests/test_cookbook_dependency_completion_regression.py:102`
- `tests/test_cookbook_dependency_completion_regression.py:108`

## `WriteFileTool` — class, line 292
- **called from:**
- `src/agent_tools/__init__.py:44`

## `WriteFileTool.execute` — method (async), line 293
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `WriteFileTool._write` — method, line 318
- **called from:**
- `tests/test_focused_test_guidance.py:110`
- `tests/test_focused_test_guidance.py:116`
- `tests/test_focused_test_guidance.py:122`
- `tests/test_personal_index_hidden_dirs.py:23`
- `tests/test_personal_index_hidden_dirs.py:24`
- `tests/test_personal_index_hidden_dirs.py:25`
- `tests/test_personal_index_hidden_dirs.py:26`
- `tests/test_personal_index_hidden_dirs.py:27`
- `tests/test_personal_index_hidden_dirs.py:28`
- `tests/test_personal_index_hidden_dirs.py:29`
- `tests/test_personal_index_hidden_dirs.py:34`
- `tests/test_personal_index_hidden_dirs.py:35`
- `tests/test_personal_index_hidden_dirs.py:36`
- `tests/test_personal_index_hidden_dirs.py:43`
- `tests/test_personal_index_hidden_dirs.py:44`
- `tests/test_personal_index_hidden_dirs.py:45`
- `tests/test_personal_index_hidden_dirs.py:52`
- `tests/test_personal_index_hidden_dirs.py:53`
- `tests/test_personal_index_hidden_dirs.py:61`
- `tests/test_personal_index_hidden_dirs.py:62`
- `tests/test_rag_index_hidden_dirs.py:36`
- `tests/test_rag_index_hidden_dirs.py:37`
- `tests/test_rag_index_hidden_dirs.py:38`
- `tests/test_rag_index_hidden_dirs.py:39`
- `tests/test_rag_index_hidden_dirs.py:40`
- `tests/test_rag_index_hidden_dirs.py:41`
- `tests/test_rag_index_hidden_dirs.py:42`
- `tests/test_rag_index_hidden_dirs.py:54`
- `tests/test_rag_index_hidden_dirs.py:55`
- `tests/test_rag_index_hidden_dirs.py:56`
- `tests/test_rag_index_hidden_dirs.py:70`
- `tests/test_rag_index_hidden_dirs.py:71`
- `tests/test_tidy_research_owner_scope.py:59`
- `tests/test_tidy_research_owner_scope.py:68`
- `tests/test_tidy_research_owner_scope.py:69`
- `tests/test_tidy_research_owner_scope.py:90`
- `tests/test_tidy_research_owner_scope.py:101`
- `tests/test_tidy_research_owner_scope.py:102`
- `tests/test_tidy_research_owner_scope.py:124`
- `tests/test_tidy_research_owner_scope.py:125`
- `tests/test_tidy_research_owner_scope.py:136`
- `tests/test_tidy_research_owner_scope.py:137`
- `tests/test_tidy_research_owner_scope.py:150`
- `tests/test_tidy_research_owner_scope.py:151`

## `ApplyPatchTool` — class, line 342
- **called from:**
- `src/agent_tools/__init__.py:46`

## `ApplyPatchTool.execute` — method (async), line 343
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `_parse_agent_patch` — function, line 428
- **called from:**
- `src/agent_tools/filesystem_tools.py:366`

## `_apply_patch_hunks` — function, line 490
- **called from:**
- `src/agent_tools/filesystem_tools.py:389`

## `LsTool` — class, line 517
- **called from:**
- `src/agent_tools/__init__.py:48`
- `tests/test_agent_state_dir_confinement.py:126`
- `tests/test_agent_state_dir_confinement.py:609`

## `LsTool.execute` — method (async), line 518
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `LsTool._ls` — method, line 538
- **called from:**
- `routes/email_pollers.py:1175`

## `GlobTool` — class, line 572
- **called from:**
- `src/agent_tools/__init__.py:49`
- `tests/test_agent_state_dir_confinement.py:129`
- `tests/test_agent_state_dir_confinement.py:450`
- `tests/test_agent_state_dir_confinement.py:474`

## `GlobTool.execute` — method (async), line 573
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `GlobTool._glob` — method, line 599
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `GrepTool` — class, line 679
- **called from:**
- `src/agent_tools/__init__.py:50`
- `tests/test_agent_state_dir_confinement.py:132`
- `tests/test_agent_state_dir_confinement.py:453`
- `tests/test_agent_state_dir_confinement.py:477`
- `tests/test_agent_state_dir_confinement.py:629`
- `tests/test_agent_state_dir_confinement.py:689`
- `tests/test_agent_state_dir_confinement.py:711`
- `tests/test_agent_state_dir_confinement.py:739`
- `tests/test_agent_state_dir_confinement.py:764`
- `tests/test_agent_state_dir_confinement.py:785`
- `tests/test_agent_state_dir_confinement.py:839`
- `tests/test_agent_state_dir_confinement.py:879`
- `tests/test_agent_state_dir_confinement.py:883`
- `tests/test_agent_state_dir_confinement.py:898`
- `tests/test_agent_state_dir_confinement.py:942`
- `tests/test_agent_state_dir_confinement.py:961`
- `tests/test_agent_state_dir_confinement.py:984`
- `tests/test_agent_state_dir_confinement.py:1039`

## `GrepTool.execute` — method (async), line 680
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)

## `GrepTool._grep` — method, line 715
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `GrepTool.is_top_level_safe` — method, line 728
- **called from:**
- `src/agent_tools/filesystem_tools.py:775`

## `GrepTool.safe_targets` — method, line 741
- **called from:**
- `src/agent_tools/filesystem_tools.py:785`

## `GrepTool.parse_rg_result` — method, line 793
- **called from:**
- `src/agent_tools/filesystem_tools.py:881`

## `GrepTool.run_rg` — method, line 812
- **called from:**
- `src/agent_tools/filesystem_tools.py:907`
- `src/agent_tools/filesystem_tools.py:928`

## `GrepTool.enqueue_stdout` — method, line 830
- **called from:**
- `src/agent_tools/filesystem_tools.py:845`
- `src/agent_tools/filesystem_tools.py:848`

## `GrepTool.read_stdout` — method, line 841
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `GrepTool.read_stderr` — method, line 850
- **called from:**
_no local callers found (framework-called, dynamic, or dead — check before deleting)_

## `GetWorkspaceTool` — class, line 1028
- **called from:**
- `src/agent_tools/__init__.py:56`

## `GetWorkspaceTool.execute` — method (async), line 1031
- **called from:**
- `core/database.py:146`
- `core/database.py:151`
- `core/database.py:158`
- `core/database.py:160`
- `core/database.py:509`
- `core/database.py:902`
- `core/database.py:905`
- `core/database.py:908`
- `core/database.py:920`
- `core/database.py:947`
- `core/database.py:950`
- `core/database.py:951`
- `core/database.py:974`
- `core/database.py:977`
- `core/database.py:998`
- `core/database.py:1001`
- `core/database.py:1002`
- `core/database.py:1022`
- `core/database.py:1025`
- `core/database.py:1045`
- `core/database.py:1048`
- `core/database.py:1075`
- `core/database.py:1078`
- `core/database.py:1079`
- `core/database.py:1100`
- `core/database.py:1103`
- `core/database.py:1104`
- `core/database.py:1125`
- `core/database.py:1128`
- `core/database.py:1148`
- `core/database.py:1151`
- `core/database.py:1153`
- `core/database.py:1155`
- `core/database.py:1157`
- `core/database.py:1176`
- `core/database.py:1179`
- `core/database.py:1199`
- `core/database.py:1202`
- `core/database.py:1223`
- `core/database.py:1226`
- `core/database.py:1245`
- `core/database.py:1248`
- `core/database.py:1268`
- `core/database.py:1271`
- `core/database.py:1273`
- `core/database.py:1275`
- `core/database.py:1277`
- `core/database.py:1279`
- `core/database.py:1281`
- `core/database.py:1300`
- `core/database.py:1303`
- `core/database.py:1323`
- `core/database.py:1326`
- `core/database.py:1346`
- `core/database.py:1349`
- `core/database.py:1350`
- `core/database.py:1370`
- `core/database.py:1373`
- `core/database.py:1374`
- `core/database.py:1406`
- … +335 more (grep the name in repo)
