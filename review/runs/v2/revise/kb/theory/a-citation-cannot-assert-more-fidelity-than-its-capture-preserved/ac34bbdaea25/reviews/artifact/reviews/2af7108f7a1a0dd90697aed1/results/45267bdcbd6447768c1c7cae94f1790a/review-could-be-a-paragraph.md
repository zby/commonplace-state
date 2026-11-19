---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/2af7108f7a1a0dd90697aed1/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/2af7108f7a1a0dd90697aed1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 45267bdcbd6447768c1c7cae94f1790a
completed-at: '2026-11-16T22:09:16Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/45267bdcbd6447768c1c7cae94f1790a/outputs/review-could-be-a-paragraph.md
raw-output-sha256: 07e0def74d2fa83a86c672e01461e35964201a5f24b22a254dd6850f13b12ec4
format: 2
---

# Review

## Summary

Collapsing the note into one paragraph would lose several separately load-bearing elements, so the multi-section structure is justified.

## What a one-paragraph version would lose

The headline ("fidelity is fixed at capture; only re-capture raises it") fits in a sentence, but the note does more than state it:

- **The fidelity/authority distinction.** It reconciles the claim with the linked note saying authority is earned after capture, and gives the composition rule (capture sets a ceiling; authority is earned beneath it). This is a non-obvious inference, not background.
- **Why the layering is forced.** Finite context and copyright are inherited constraints; provider output filters are flagged as contingent. This support path carries the claim that no rival design avoids the layers.
- **The mechanism for "notation cannot repair it".** A paraphrase has no mechanical derivation rule, so marking it `verbatim` produces a trusted hand-maintained copy with a stronger trust signal. This step turns a practical observation into a principled impossibility.
- **The locator corollary.** Two spans at the same offset can differ by a full layer, so a position-only locator is underspecified. This is a design consequence a reader would act on.
- **The boundary case.** For losslessly capturable sources the layers collapse and position becomes the binding constraint again, which also scopes the corollary.

A single paragraph could hold all of these only by compressing each into a clause, losing the inference steps and the boundary condition. The note is not over-complex for its content.
