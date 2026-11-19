---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: e2ca83dfc9ae43cca4524ed4feca96f4
completed-at: '2026-11-17T07:21:17Z'
findings:
- scope: passage
  quotes:
  - A test available to the proposing system can be optimized without improving the
    capability it is meant to assess; human approval does not remove the need to justify
    the assessment.
  reason: 'This sentence adds a separate mechanism: a proposing system can optimize
    against an available test (a Goodhart-style failure). That mechanism needs its
    own evidence, and it does not bound the note''s claim about which judgment controls
    adoption. The bullet''s first two sentences already state the needed boundary:
    approval does not establish quality. Delete the sentence or rehome it in a note
    on test gaming or evaluator independence.'
  level: warn
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/71eb50e937bd2976a55df961/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/71eb50e937bd2976a55df961/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/e2ca83dfc9ae43cca4524ed4feca96f4/outputs/review.md
raw-output-sha256: 3503b40db108043f99c48e998408c25b2422eae14d8b2898a81d6f25eedd1c60
---

# Review

The main claim is that a judgment helps determine a change when it controls whether the change enters use. Assessment after adoption does not, through that assessment alone, contribute to selecting the change. What matters is the judgment's causal role, not whether a person or program makes it.

Most of the side material supports that claim in its current place:

- The two hypothetical cases are the note's central contrast.
- The remark that a later assessment could cause a future rollback limits the claim to the transition under examination.
- "One episode can contain both roles" blocks the redescription move named in the description.
- The definition of adoption, with its link to operative change, fixes the term the claim depends on.
- The first two Scope bullets are boundary conditions. The second also motivates the single open question.
- The first two sentences of the third bullet ("Approval does not establish quality…") are also a boundary condition. They stop readers from treating selection as endorsement.

The final sentence of that bullet is the one branch that needs action. It introduces test optimization by the proposing system. That is a different failure mechanism, with its own evidence requirements, and the note neither defends it nor needs it. Here it widens the attack surface and shifts the reader's attention from causal role to evaluation validity. Removing it leaves the boundary condition intact.
