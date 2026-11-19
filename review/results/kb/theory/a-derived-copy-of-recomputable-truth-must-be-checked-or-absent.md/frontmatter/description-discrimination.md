---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c6bc1cabfa9b3bb239157a2bf369985593cb36e9e78af74fe7b23e30b4acd14f
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: b77f299bcf63471da4849e1261722ecb
completed-at: '2026-11-16T22:18:10Z'
findings:
- scope: document
  quotes: []
  reason: The description mostly restates the title. It expands 'derived copy of recomputable
    truth' to 'a copy of information recomputable from a ground-truth source', 'checked'
    to 'machine-checked against that source', and 'absent' to 'not exist'. It then
    states the excluded middle ('hand-maintained-and-trusted is forbidden'), which
    the title already implies. It does not give the mechanism (an absent copy costs
    one bounded recomputation, while a false copy causes silent, unbounded wrongness).
    It also omits the scope boundary (the rule applies only where verification is
    a deterministic Level A check; judgment-level dependencies stay under managed
    staleness) and the implication (omission is the fallback when a copy cannot be
    checked). Any of these would help an agent choose this note over neighbouring
    lineage and staleness notes.
  level: warn
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/082cf21546aebbc1c941bbbe/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/082cf21546aebbc1c941bbbe/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/b77f299bcf63471da4849e1261722ecb/outputs/review-description-discrimination.md
raw-output-sha256: 56999f1a2007815302be08d5cfcc449bec3c6e93f3b281a6ea2ba1764fa25768
---

# Review

## Summary

The description adds a little: "machine-checked" makes "checked" precise, and it names the forbidden state. Most of it is still a paraphrase of the title. In a short result list next to the lineage, make-like staleness and compiled-view notes, it would not show what this note specifically argues: the asymmetry between the cost of an absent copy and the cost of a false one, and the limit of the rule to mechanically derivable copies. Replacing part of the paraphrase with that mechanism or scope would make the description discriminate.
