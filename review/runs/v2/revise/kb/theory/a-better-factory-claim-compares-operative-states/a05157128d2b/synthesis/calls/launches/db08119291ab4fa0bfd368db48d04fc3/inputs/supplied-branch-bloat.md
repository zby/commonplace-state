---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3716e46b3a2745bf818526d3d0a1022e
completed-at: '2026-11-18T00:19:41Z'
findings:
- scope: passage
  quotes:
  - The third case requires evidence of that contribution, not just the sequence of
    a failure, a retained instruction and better results. Comparing otherwise equivalent
    runs with and without the retained instruction tests its contribution, because
    [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).
  reason: 'This paragraph explains how to identify learning: how to show that an experience-derived
    change causally contributed to an improvement. The note''s main claim is about
    the relata and the antecedent relation of a better-factory claim. The note only
    needs the boundary that improvement and learning are separate claims. The first
    two hypothetical cases and the sentence ''the experience-to-change link distinguishes
    learning'' already state that boundary. The evidence method for learning needs
    different support (experimental contrast) and belongs in the factory-learning
    note, which owns the experience-to-change link. Recommend cutting this paragraph
    to at most one clause or moving it to that note. The Learning bullet could also
    be shortened to the bare causal condition.'
  level: warn
- scope: passage
  quotes:
  - Internal controls on what the factory retains govern adoption, but do not by themselves
    establish that the adopted state passes the declared comparison.
  - Whether an evaluator also controlled adoption is a separate causal question; a
    description cannot change whether its judgment was required for installation.
  reason: 'Two asides bring in a separate topic: what controls adoption, meaning which
    evaluator or retention control decided installation. Each one partly bounds the
    claim, since judging adopted states is not the same as gating adoption. But the
    topic appears in two places, it is not developed, and the second sentence (''a
    description cannot change...'') answers an objection the note never raises. Their
    destination is unclear. Merge them into one Scope boundary, or move the adoption-control
    question to whichever note treats evaluator authority.'
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/95e3c202163a38d5c54b0d63/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/95e3c202163a38d5c54b0d63/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3716e46b3a2745bf818526d3d0a1022e/outputs/review.md
raw-output-sha256: 7e6efa3b2b5a207bf7b2c403ea8651bf901c6faa2fbcc4ff3101f46e89c64530
---

# Review

## Summary

The main claim is that a better-factory claim compares two operative states: a predecessor and an installed successor. It uses an assessment relation declared before development. That relation combines non-regression over the predecessor's prior capabilities with a declared improvement. Most side material supports this claim. Several parts stay in place:

- The candidate/successor distinction.
- The whole-production-environment paragraph, which bounds the relata.
- The factory-development preservation consequence, which the description and Scope list tie to the non-regression scope.
- The Scope boundaries.

The retention/improvement/learning section starts as a useful contrast: retention without improvement, and improvement without learning, separate this claim from its neighbours. It then branches into how to establish learning. The with/without-instruction experiment paragraph is about identifying a causal contribution, not about comparing states. It needs different evidence and makes the note more open to attack without strengthening the main claim. That paragraph is the WARN: cut it or move it to the factory-learning note.

A smaller branch on adoption control appears twice. Its destination is unclear, so it gets INFO.
