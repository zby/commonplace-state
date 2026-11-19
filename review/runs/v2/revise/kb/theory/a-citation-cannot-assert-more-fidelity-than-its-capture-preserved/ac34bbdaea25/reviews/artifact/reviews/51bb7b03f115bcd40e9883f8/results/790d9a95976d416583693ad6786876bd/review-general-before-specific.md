---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/structural/general-before-specific.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/structural/general-before-specific.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/51bb7b03f115bcd40e9883f8/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/51bb7b03f115bcd40e9883f8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 790d9a95976d416583693ad6786876bd
completed-at: '2026-11-16T22:09:51Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/790d9a95976d416583693ad6786876bd/outputs/review-general-before-specific.md
raw-output-sha256: 6da3ece8bffeb070053693bc1f72bce5e65acbcf77f69f3ec9f7edd6dfcd8519
format: 2
---

# Review

## Summary

The sections run from the general claim to its consequences and limits; no adjacent pair puts a specific case before the rule it exemplifies.

The section sequence is: the untitled opening (the general bound and the fidelity/authority distinction), "Capture is layered because it is forced to be", "Why notation cannot repair it", "Corollary: a locator must carry the layer, not just the span", "Scope" and "Open Questions".

- Opening → layering: the general bound comes first; the layering section explains why capture loses fidelity.
- Layering → notation: the second section argues that downstream notation cannot raise the bound. Its link to the more general "history has one chance to become checkable" rule appears inside the section as a cross-note connection. No later section states that rule, so the ordering is not inverted.
- Notation → corollary: the corollary is an explicitly derived specific consequence and correctly follows the argument it depends on.
- Corollary → Scope: Scope qualifies the claim's boundaries after the claim is stated, which is the expected order.
- Scope → Open Questions: these are open questions, not a general rule.
