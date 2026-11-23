---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 7c5f3e3ccef24cb3aa025c05050a5c3b
completed-at: '2026-11-22T09:33:39Z'
findings:
- scope: passage
  quotes:
  - when at least one does
  reason: The necessary/possible distinction introduces the term 'possible' preference,
    but the argument uses only the necessary relation afterwards. The extra term is
    small and does not mislead, but nothing later depends on it.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/a7e1ac482d720d3c12de5def/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/outputs/review-framework-decoration.md
raw-output-sha256: 1985c40a913646dd3e6ae1b294e3510ed33b7f96590bd0ba0711089e8c6e5650
---

# Review

## Summary

The article's structures do work in its argument. One introduced term goes unused, recorded as an info finding.

## Structures checked

- **The five-row comparison table (gradient training vs selection over a readable store).** Each row is used later. The substrate and value-function rows carry the central contrast. The prose directly after the table takes up the "Deployment time" and "Inspectability" rows and adds their limits. The credit-assignment row returns as PRODIGY's targeted correction and as "credit assignment without a chain rule" in the Bitter Lesson section. One sentence could not keep the five contrasts and the hooks the later sections use.
- **The four-step admission sequence (formal proof, fixed formula, changing heuristics, robust comparison).** This is a progression, not a taxonomy kept for show. Each step names what the previous one could not do (ignore unprovable improvements; single-loop; needing a person to correct worth judgments), and the last step is where the bet enters. Deleting it would remove the argument for why the bet is new.
- **The necessary/possible preference vocabulary.** "Necessary" is load-bearing: it defines a robust comparison. "Possible" is introduced in the same sentence and never used again; see the finding.
- **The two-part empirical check (operative dependence, robust improvement).** These are two separate test conditions with different failure modes (an ignored file vs. passing only the admission check). They become the decision rule for testing the bet.
- **The five hazards list.** Three hazards are named again in the failure condition for the bet. "Judgment reliability" and "Weak proposals" are not reused there, but they set the bet's scope (the bet covers comparison, not proposal quality) rather than adding vocabulary for show.

The article contains no notation or equations.
