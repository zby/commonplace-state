---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
note-sha256: 1b0b5eaeee5248af37617d4526756460a4a101df5725794b117143cd4b9cc8c2
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/8e0eb26a9e3f15d6ed2d5c7b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 97456a991da64d2a8b2c8a72f57d2686
completed-at: '2026-11-20T09:42:00Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/outputs/review-description-discrimination.md
raw-output-sha256: 89014142d6cf174a081d0dd430d5cd3f81228184fa2be264718d675067a6c8cc
format: 2
---

# Review

## Summary

The description does more than paraphrase the title. It adds:

- **Implication:** components can move "without changing call sites", which states concretely what "bidirectional refactoring" buys.
- **Mechanism:** "name-based dispatch over a hybrid VM" names how the shared convention is achieved.
- **Context:** llm-do is the demonstrating system, which separates this note from abstract notes on constraining or codification and from other system comparisons.

An agent choosing among nearby notes on codification, relaxing or typed callables could pick this one from the description alone.
