---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - hosted providers' output filters on mass verbatim reproduction add a third barrier,
    but that one is provider-contingent rather than inherited
  reason: This caveat names a third barrier and then sets it aside as non-inherited,
    so it adds nothing to the support route for forced layering, which rests on context
    limits and copyright. It could shrink to a short aside or be dropped. It may still
    be worth a few words because it heads off the objection that provider filters
    were overlooked.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/detail-overhang.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/detail-overhang.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/e840664cdac25e21e2a1f5c4/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/e840664cdac25e21e2a1f5c4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: e35f0ad067db4e528439aebc559918a6
completed-at: '2026-11-16T22:10:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/e35f0ad067db4e528439aebc559918a6/outputs/review.md
raw-output-sha256: 1650508081f9872e61ade22fb978c13b4628b213dd739427061a10d5a2fe5901
format: 2
---

# Review

## Summary

Detail is mostly proportional to its argumentative role. The note is compact. Each section does one job: the layering, why notation cannot raise fidelity, the locator corollary and the scope boundary. The examples are short.

## Details checked

- **Authority versus fidelity paragraph.** It is long for an opening caveat, but it does not overhang. A linked note asserts the complementary claim that authority is earned after capture. Without the explicit distinction, a reader could take this note to contradict that one. The two closing contrast sentences, about a verified rule on a second-hand passage and an unverified verbatim quote, show that the two axes are independent. That makes the composition memorable without starting a second thesis. This PASS is recorded to prevent a likely false positive.
- **Layer bullets.** The two parenthetical examples in the second-hand bullet are brief and make an unfamiliar category concrete. They are proportional.
- **Provider-filter caveat.** This is the one detail whose length exceeds its work; see the finding. It is only one clause, so the result is INFO rather than WARN.
- **"Why notation cannot repair it."** Each step in this section carries an inference: the mechanical derivation rule, substring match versus judgment, and the stronger trust signal. It is not padding.
- **Scope and evidence footer.** The lossless-source boundary sets a real condition on the claim. The ADR 046 figures give the evidence in one sentence. Both are proportional.
