---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: dc859c7284fe4a7d95df019fdb2a8b5d
completed-at: '2026-11-16T17:36:29Z'
findings:
- scope: passage
  quotes:
  - 'The kind of test depends on the claim: an observation for an empirical claim,
    a derivation for a formal one, a check against the source for a source-derived
    one.'
  reason: This three-way list of test kinds is never used again in the argument; no
    later section depends on telling observation, derivation and source check apart.
    It is a single explanatory sentence, not a separate structure, and it does keep
    'test' from being read as empirical only. That makes it minor extra vocabulary
    rather than decoration that misleads.
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/5a8789bfb3f80b2a82bf6ddf/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/5a8789bfb3f80b2a82bf6ddf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/dc859c7284fe4a7d95df019fdb2a8b5d/outputs/review-framework-decoration.md
raw-output-sha256: 559478ac8d8467d2ebbadad116547114777b59d8ee274f30da41ad7d8f9fe14c
---

# Review

## Summary

The note's one framework is the three-question split into truth, test record and fit, and it is load-bearing. The body has no tables, notation or equations.

## Structures checked

- **Three questions: truth, test record, fit.** Each later section works on one pair of these. The sections are test record vs truth, test record vs fit, fit vs test record, the interaction between fit and test, and how a contradiction is repaired using both. The final scope boundary says the questions are separate but correlated, which relies on all three being named. Replacing the split with one sentence would lose the pairwise distinctions that organize the argument.
- **Fit criteria: relevance, scope and level, agreement, operational change.** These are used again. The failure cases under "A good test record does not make a claim fit" cover irrelevance, duplication, wrong level, mismatched scope and detail that changes no inference. "Fit is not an independent test" relies on agreement with the other claims. The Scope section names the same dimensions when it says fit has no single scale.
- **Independence condition on tests.** A test counts only if its outcome could have gone against the claim and it does not presuppose the theory. This becomes the decision rule in "Fit is not an independent test". It is load-bearing.
- **Kinds of test.** This list is not used later, as recorded in the info finding.
