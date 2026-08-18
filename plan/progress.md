# Progress

## 2026-08-17

Stage: S1 Evidence + S4 Drafting.

Read project rules and section context, including `AGENTS.md`, review workflow files, section outlines, evidence matrix, chapter page, drafting board, and source pages for the 1.1 evidence pool.

Prepared local planning artifacts:

- `plan/project-overview.md`
- `plan/evidence-map.md`
- `plan/chapter-blueprints/1.1-blueprint.md`
- `plan/review/evidence-coverage.md`
- `plan/task-packets/rewrite-1.1.md`

### Capability-use audit

- Required skills: using-research-writing, paper-orchestration, evidence-driven-writing, literature-review, writing-core, verification.
- Skills actually used: using-research-writing, paper-orchestration, evidence-driven-writing, literature-review, writing-core, verification.
- Inputs consumed: project rules, review outline, detailed 1.1 logic, evidence package, evidence matrix, source pages for burden/guideline/closed-loop pilot evidence.
- Inputs not used and why: large raw `work/*.txt` files and full retrieval table were inspected at project level but not used as citable evidence because section 1.1 must use already admitted source pages and evidence matrix entries.
- Artifacts produced: evidence map, paragraph blueprint, evidence coverage, task packet, rewritten 1.1 evidence-package draft, updated chapter page and writing board.
- Verification run: `rg -n "1\\.1 完整草案 v3|1\\.1 v3 段落文献证据矩阵|dudysova-2024|结构性困境|临床疗效" ...`; `rg -n "首先|其次|最后|此外|另外|接下来|总之|值得注意的是|需要指出的是|重要的是|必须强调的是|显而易见|非常|极其|十分|相当|我认为|我觉得" ...`; plan artifact `Test-Path` checks. The style-check script referenced by the writing skill is not present in this repository.
- Remaining risk: the new text is marked `待校准`; per project workflow it still needs human calibration before moving into the confirmed integrated draft.

### Follow-up rewrite note

User requested a 250-300 Chinese-character version following "problem urgency -> paradigm defect -> technical route" and containing several specific claims. Rechecked the evidence package and found that symptom-level 30%-50%, sleep-insufficiency cross-system consequences, dose-response relationship, PSG one-night laboratory limitation, and CBT/drug/CPAP execution detached from monitoring are not directly supported by the current section evidence package.

Added `1.1 用户指定结构版 v4（证据受限，待补）` to `wiki/review/01-引言-1.1-P1-证据包.md`. It preserves the requested structure and phrasing while marking unsupported items as requiring direct evidence before entry into confirmed manuscript text.

Verification run: `rg -n "用户指定结构版 v4|系统性社会健康挑战|结构性困境——评估与治疗相互割裂|近年来，随着可穿戴生理传感与实时信号处理技术的成熟|待补直接证据|PSG|CPAP|剂量-反应" ...`; style forbidden-expression `rg` returned no matches.

### Follow-up citation-supported rewrite

Updated `wiki/review/01-引言-1.1-P1-证据包.md` again so `1.1 用户指定结构版 v4` is now a citation-supported version rather than a "待补" version. Removed unsupported manuscript claims about symptom-level 30%-50%, sleep-insufficiency cross-system outcomes and dose-response, PSG one-night laboratory limitation, and CBT/drug/CPAP detached monitoring. Added a v4 checklist and paragraph evidence matrix with source-page pointers for each sentence-level claim.

Verification run: inspected the v4 block; `rg` confirmed the v4 title, source links, and evidence matrix are present. Unsupported terms only remain in the checklist sentence explaining removed content. Style forbidden-expression `rg` returned no matches.

### Follow-up polish with research-writing-skill

Used `research-writing-skill` to polish `1.1 用户指定结构版 v4` while preserving evidence-supported claims, citations, and section logic. Added full forms for abbreviations at first use in the polished text, including OSA, RLS, REM, DSM, AHI, CBT-I, and AASM. Updated the v4 checklist and evidence matrix accordingly.

Added a new writing rule to `wiki/review/文献搜索策略_新版.md`: every abbreviation must be expanded at first occurrence in manuscript text, figure/table titles, notes, and the evidence matrix; updated the file date to 2026-08-17.

Verification run: `rg` confirmed the polished v4 block contains abbreviation full forms and source links; `rg` confirmed the new "术语与缩写" rule and `updated: 2026-08-17`; style forbidden-expression `rg` returned no matches.
