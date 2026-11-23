---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 16b1a9e3052e425f8bb2307f87992ba0
completed-at: '2026-11-21T19:27:21Z'
findings:
- scope: passage
  quotes:
  - Before stating the paradigm abstractly, follow a single edit through a deployed
    agent system
  reason: 'The section ''One change followed through'' is a worked case: one routing
    line, its narrowing, and a revision to the review check. It comes before ''Deliberative
    learning versus training weights'', which states the general definition and contrast.
    The case exemplifies the definition; it does not qualify or contradict it. Under
    the gate''s tiebreaker, an exemplifying case placed before its general rule is
    WARN. The ordering is deliberate, and the introduction gives a one-sentence gloss
    of deliberative learning first, so the reader is not left without the rule. Still,
    the full definition arrives only after the case. If the example-first order is
    meant to stay, this warning records a known choice rather than an error.'
  level: warn
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/16b1a9e3052e425f8bb2307f87992ba0/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/e24b9185222840b856a4b17b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/16b1a9e3052e425f8bb2307f87992ba0/outputs/review-general-before-specific.md
raw-output-sha256: 2be97ef612a956390461537e1c4e1ce602da67a26766b8eb046c67848a6f21ac
---

# Review

## Summary

The article has six sections after the introduction. I checked each adjacent pair.

- **One change followed through → Deliberative learning versus training weights.** A specific case comes before the general definition it illustrates. The case exemplifies the rule rather than qualifying it, so the gate's tiebreaker gives WARN. The article says this order is deliberate ("Before stating the paradigm abstractly…"), and the introduction already defines the term in one sentence. This lowers the cost to the reader but does not change what the gate's test finds.
- **Deliberative learning versus training weights → Proof, formula, judgment.** General comes before the specific precedents (Gödel machine, PRODIGY, EURISKO). This order is correct.
- **Proof, formula, judgment → Compatible with the Bitter Lesson.** Each section makes a different argument; neither is a case of the other.
- **Compatible with the Bitter Lesson → What counts as learned, current evidence, and limits.** These are separate concerns with no general/specific relation.
- **What counts as learned… → Where to go next.** A navigation section, so there is no general/specific relation.

Only the first pair fails the test.
