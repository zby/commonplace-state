---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: e6c44a5d053c40b889fc04e430cca4c7
completed-at: '2026-11-21T19:26:59Z'
findings: []
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/8906369a907679cf8c3cfb8e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/outputs/review-redundant-restatement.md
raw-output-sha256: 155021b654890ae206912dcfba9c273c4088bca836cd199505fb69dbf091c514
---

# Review

## Summary

I checked the first paragraph of each section and the last paragraph before
each heading.

**Section openings.** Each one either is a one-sentence transition or
introduces new content:

- "One change followed through": a one-sentence transition into the example.
- "Deliberative learning versus training weights": introduces the definition.
- "Proof, formula, judgment": asks a new question about why earlier systems
  stalled.
- "Compatible with the Bitter Lesson": introduces the objection.
- "What counts as learned …": defines the success verdict.

None of these openings can be deleted without losing the section's starting
point.

**Section closings.** None previews the next section's content:

- The three-things summary that closes the example draws conclusions from the
  example. It does not preview the definition that follows.
- The costs paragraph adds new material.
- The bet paragraph that closes the precedent section is followed by the Bitter
  Lesson objection, not by a re-development of the bet.
- The bootstrap condition is new content.

The bet paragraph repeats the introduction's thesis. That repetition is not at
a section boundary, and it develops the thesis's requirements instead of
restating it. It falls outside this gate.
