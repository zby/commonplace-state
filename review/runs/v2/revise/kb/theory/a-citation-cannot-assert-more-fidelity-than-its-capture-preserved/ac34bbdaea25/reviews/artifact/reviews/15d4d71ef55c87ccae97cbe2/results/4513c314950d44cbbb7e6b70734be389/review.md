---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The layering is not a design choice — [a framework rule with a boundary-preserving
    rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md),
    and no rival capture design drops the layering while preserving the commitments
    the framework has already made.
  reason: 'The section that supplies the claim''s premise opens with related-note
    machinery (the inherited-constraint test) before the plain causes: finite context
    and copyright. Starting with those causes and folding the rival-design argument
    into a trailing clause would make the premise more memorable. The core claim stays
    findable, so this is only a memorability issue.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/15d4d71ef55c87ccae97cbe2/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/15d4d71ef55c87ccae97cbe2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 4513c314950d44cbbb7e6b70734be389
completed-at: '2026-11-16T22:10:18Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/4513c314950d44cbbb7e6b70734be389/outputs/review.md
raw-output-sha256: f4dca999d86225e13d48333475aa799292a21c740f255929f0151aeefeef128b
format: 2
---

# Review

## Summary

The note's strongest claim, in one sentence, is this: a citation's fidelity is fixed when the source is captured, no later notation or check can raise it, and only re-capture can. The title states this claim, and the first paragraph restates it plainly with "non-increasing" and "only re-capture". The note keeps the claim prominent from the start.

Later material stays subordinate to the claim. The fidelity/authority paragraph heads off a likely misreading against a neighbouring note, and it ends on a concrete contrast. "Capture is layered" gives the premise. "Why notation cannot repair it" gives the mechanism. The locator corollary and the Scope section follow from the claim and set its limits. Each section's heading says how it relates to the claim.

One passage is slightly obscured. The layering section opens with a link-and-argument clause about inherited constraints and boundary-preserving rivals, and only then gives the concrete causes: finite context windows and copyright. The fix is to lead with those causes. This does not hide the core claim, so the outcome is PASS with one INFO finding.

There is also a possible revision target, though it is not a defect. The Scope section's "provenance quality is decided *before any note is written*" is an easy-to-remember operational form of the claim. The note could echo it closer to the opening if the author wants readers to retain it.
