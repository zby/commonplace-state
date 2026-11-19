---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/43c7e571fe5fc517cd70e938/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/43c7e571fe5fc517cd70e938/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 26a2390cbf784ef7a0802044f744d663
completed-at: '2026-11-16T22:09:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/26a2390cbf784ef7a0802044f744d663/outputs/review-unbridged-cross-domain.md
raw-output-sha256: ae1205f624fe12f256b431e624fff3c4be2bc28706c18ce4ed966772ccd5de4e
format: 2
---

# Review

## Summary

The note cites one empirical result: the verbatim-quote checker run over a casebook corpus, reported through ADR 046. The source domain is citations in an agent-operated markdown KB checked against retained snapshots. That is also the note's argument domain: citation fidelity for KB claims that cite captured sources. The legal subject matter of the casebooks does not create a domain gap, because the checked mechanism does not depend on it. That mechanism is substring matching of `verbatim`-marked quotes against a snapshot.

The other supports are links to KB theory notes (the derived-copy rule, "history has one chance to become checkable", the inherited-constraint test). These are arguments within the same domain, not imported empirical results. No cross-domain transfer needs a bridge.
