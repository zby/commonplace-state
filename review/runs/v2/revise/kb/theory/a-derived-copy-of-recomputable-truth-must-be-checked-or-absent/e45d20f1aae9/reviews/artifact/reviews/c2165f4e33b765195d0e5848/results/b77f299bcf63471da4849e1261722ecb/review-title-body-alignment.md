---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - mechanically recomputable from a ground-truth source
  reason: The body limits the rule to copies that can be re-derived mechanically and
    checked deterministically (Level A). It says that judgment-level dependent artifacts,
    such as natural-language summaries or instructions derived from sources, are not
    forbidden and stay under managed staleness. The H1 relies on the word 'recomputable'
    alone to carry that limit. A reader might count an LLM-regenerated summary as
    'recomputable'. The body excludes that case, so the alignment holds, but the qualifier
    'mechanically' lives only in the body. This is a minor precision point, not drift.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: d216c06478befd5bb5127bbf823c381c19d11c7fa554be37842181529ed0ce4c
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/c2165f4e33b765195d0e5848/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/c2165f4e33b765195d0e5848/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: b77f299bcf63471da4849e1261722ecb
completed-at: '2026-11-16T22:18:10Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/b77f299bcf63471da4849e1261722ecb/outputs/review-title-body-alignment.md
raw-output-sha256: 27b2b2ed43983170db68d89db98d7a4a55cfcf8928a9d368f5edf5411c698bf0
format: 2
---

# Review

## Summary

The body supports the title's claim. It names exactly two valid states for a derived copy: checked (a validator re-derives the copy and fails on mismatch) or absent (deleted, or replaced by a live read). It justifies the excluded middle through the asymmetry between a bounded recomputation and silent, unbounded wrongness. It also states the preconditions for "checked" and gives instances in four states of application. The scope section, the preconditions and the consequences all keep to the title's subject, derived copies of recomputable truth. The section on what enforcement buys argues that checked copies beat omission, which refines the title's disjunction rather than drifting from it. There is no claim drift or material scope drift.
