---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 26a2390cbf784ef7a0802044f744d663
completed-at: '2026-11-16T22:09:35Z'
findings:
- scope: passage
  quotes:
  - In that regime a structured span locator earns its keep
  reason: 'Literal meaning: in that regime a structured span locator is worth its
    cost or is the appropriate design. `Earns its keep` adds a deservingness connotation
    that the note neither uses nor supports, and it is the gate''s own fail example.
    Replace with "In that regime a structured span locator is the appropriate design"
    (or "is justified"). This removes the idiom without losing precision.'
  level: warn
- scope: passage
  quotes:
  - Change the premise and the conclusion moves, which is where the claim earns its
    boundaries.
  reason: 'Literal meaning: the claim''s boundaries are where its premise stops holding.
    `Earns its boundaries` adds deservingness and makes the reader translate a figure
    that adds no contrast or mechanism. Replace with "The claim''s scope ends where
    its premise fails." This removes that reading effort and the unused connotation.'
  level: warn
- scope: passage
  quotes:
  - The claim bites exactly where capture is lossy
  reason: 'Literal meaning: the claim applies, or has practical consequences, only
    where capture is lossy. `Bites` is a mild conventional idiom, but "The claim applies
    exactly where capture is lossy" is as short and clearer. This is minor; it is
    recorded for completeness alongside the other scope-section idioms.'
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/7691b6f3dd684c3f3cff2486/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/7691b6f3dd684c3f3cff2486/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/26a2390cbf784ef7a0802044f744d663/outputs/review-mannered-prose.md
raw-output-sha256: 0a99d4aa3a99d53d8d09e5385423b6a67e5bcf01fbac38cbb7dc79fa7bce4741
---

# Review

## Summary

Most of the note's figurative wording has a function. The *spent* / *earned* pairing in the opening ("is spent at capture and never replenished" versus authority "earned by post-capture work") sharpens a real contrast between fidelity and authority that the paragraph goes on to use: "capture sets a ceiling" and "earn authority beneath it". *Ceiling* names an upper bound precisely. The *debt* language in the scope section ("the debt is fixed at ingest … repaid deliberately") maps onto the note's mechanism: an unpreserved verbatim layer is a deficit that only re-capture removes. Those figures are kept.

The failures cluster in the Scope section. There, two uses of *earns* ("earns its boundaries", "earns its keep") add a deservingness connotation that the note does not establish. They state ideas that literal wording states at least as clearly. Both are local, so the outcome is WARN, not FAIL.
