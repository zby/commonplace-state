---
type: types/edit-result.md
outcome: changed
changes:
- Narrowed 'The compatibility cost falls on identifiable callers' to losses like the
  removed getargspec that a team can find by testing dependencies before moving.
- Narrowed 'Those reasons can be checked independently of who offered them' to the
  factual parts of the reasons; the weighing of whose costs count cannot be checked
  that way.
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/narrow-overclaims.md
  on kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
format: 1
operation: kb/instructions/simplification-passes/narrow-overclaims.md
operation-sha256: fff83f2074936afa498432ab20d6f522624d8af329308aa5cdb1bd7f5cd99feb
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
input-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/calls/launches/055a0c47e3644da1a165f8eacf37c402/outputs/candidate.md
candidate-sha256: c2ca6d63a778da4948640a1d4fd36c6ea79d28df4eff3d219366f2430c69522a
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/artifact/edits/bce396d865f10e43ac6f04fa/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z
launch: 055a0c47e3644da1a165f8eacf37c402
completed-at: '2026-11-20T19:02:24Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/calls/launches/055a0c47e3644da1a165f8eacf37c402/outputs/result.md
raw-output-sha256: 01fbdc0990dc8c4907ee75afe6378e0c5f0f9389a97ecea4d19005b169fd5ce8
---

# Report

Two sentences changed, both within the supplied scope. No links, quoted spans, must-keep claims or relied-on terms were touched.

1. After the 3.11 table.
   - Before: "The compatibility cost falls on identifiable callers: for a particular application we can test its dependencies before deciding to move it."
   - After: "A loss like the removed `getargspec` can be found before moving: for a particular application we can test its dependencies before deciding to move it."
   - Evidence bounding it: the table records one compatibility loss, a removed interface that fails on call. A dependency test can find that kind of loss. The note has no evidence that every compatibility cost falls on callers who can be identified in advance.

2. Closing paragraph.
   - Before: "Those reasons can be checked independently of who offered them."
   - After: "The factual parts of those reasons, such as which work changed, can be checked independently of who offered them; the weighing of whose costs count cannot be checked that way."
   - Evidence bounding it: the note's own section "What analysis can settle" says analysis cannot supply the weights. The library-hours case says the same evidence supports different choices under different commitments. So only the factual reasons can be checked. The next sentence, which says the reasons make a judgment criticizable, stays unchanged and covers the weighing.

Noticed, not applied: nothing else outside the scope.
