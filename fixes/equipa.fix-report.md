## Fix Report: equipa

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Completeness | boundary-case-acknowledged | Reframed the promotion ladder as mostly typed rows across stages and moved rubric scores/evolution into evaluation artifacts | fixed |
| 2 | Grounding | scope-narrowed | Changed the SIMBA claim to `lessons_learned` rows and added the current `simba_generated`/`simba` source-label caveat | fixed |
| 3 | Internal consistency | scope-narrowed | Split the core harness role set from the broader benchmark role table in the role-catalog sentence | fixed |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Completeness):** "The ladder framing says EQUIPA keeps distinct tables and scripts for each compilation level, but boundary cases do not map cleanly."
- **#2 (Grounding):** "The SIMBA grounding is too strong" and "There is no `simba_rules` table; SIMBA uses `lessons_learned`."
- **#3 (Internal consistency):** "The role benchmarking discussion shifts terms" and "Those are not the same set."

### Deferred items
- (none)

### New patterns
- (none)
