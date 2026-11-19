---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Adoption here means entering a live behavioral path on which later operation depends,
    as distinguished by [operative change](./definitions/operative-change.md).
  reason: The core claim turns on what 'adoption' and 'enters use' mean, but the note
    defines adoption only at the end of the second section, after the claim and both
    cases have already relied on it. Moving this sentence up to follow the opening
    paragraph, or folding it into it, would help the claim's key term without adding
    apparatus. The core claim is still easy to find.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/07eafe96dc40bbee88b9f3fd/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/07eafe96dc40bbee88b9f3fd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 12a999b3c6ea4a278d71b44f3cd27d47
completed-at: '2026-11-17T07:21:43Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/12a999b3c6ea4a278d71b44f3cd27d47/outputs/review.md
raw-output-sha256: a99ef9f5aa332a7d4c32fc187ed3a07ec5ee793f8178da53fbca67bacfcf110f
format: 2
---

# Review

## Summary

The note's strongest claim in one sentence: an evaluator whose judgment controls whether a change is adopted is part of what determines the resulting system, while an evaluator who only assesses a change after adoption does not, through that assessment, determine the adoption; the difference lies in what the judgment controls, not in who makes it.

The title states this claim, and the first body paragraph states it plainly, right after a single supplement line. The second paragraph gives its consequence: it bears on how contributions to an improvement are attributed. Later material stays subordinate to it:

- The two hypothetical cases illustrate the contrast directly, and their closing paragraph restates it ("Only the first verdict controls the adoption being examined").
- "One episode can contain both roles" heads off the obvious objection that a single episode can do both, and keeps the reader on the claim.
- The Scope bullets bound the claim without competing with it.

No setup, analogy or terminology comes before the claim. The one shape issue is minor: the definition of adoption, which is the claim's key term, comes late, after the material that depends on it. That is recorded as an info finding. The core claim is easy to recover after one reading, so the result is PASS.
