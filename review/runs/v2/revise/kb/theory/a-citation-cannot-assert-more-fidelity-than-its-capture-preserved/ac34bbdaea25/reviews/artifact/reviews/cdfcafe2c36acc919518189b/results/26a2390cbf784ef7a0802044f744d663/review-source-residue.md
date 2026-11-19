---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - verification requires going back to the authoritative artifact (the sibling PDF)
  reason: The note claims generality over any captured long source, but this parenthetical
    assumes the evidence corpus's arrangement, in which every snapshot sits beside
    an authoritative PDF. It is stated as part of the general definition of the paraphrase
    layer, not as an example. Generalize it ("the authoritative artifact, e.g. the
    original PDF") or drop the parenthetical.
  level: warn
- scope: passage
  quotes:
  - a court restating a complaint; a news article quoting an order whose original
    is no longer served
  reason: These legal-domain cases come from the casebook corpus, but they appear
    in parentheses as illustrations of second-hand capture. They are framed as examples
    and do not overcommit the claim.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/cdfcafe2c36acc919518189b/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/cdfcafe2c36acc919518189b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 26a2390cbf784ef7a0802044f744d663
completed-at: '2026-11-16T22:09:35Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/26a2390cbf784ef7a0802044f744d663/outputs/review-source-residue.md
raw-output-sha256: c7414d9c94f2599442ba9ae631e0efb857a8eb1f43a81404b92aa57cb65e4756
format: 2
---

# Review

## Summary

The title and opening frame the claim generally: for any citation of a captured source, fidelity is bounded by the capture layer. The body mostly keeps that generality. It speaks of snapshots, layers, locators and authoritative artifacts. It ties the limits to general conditions (finite context, copyright) and names the provider-specific output filters as contingent.

One residue remains from the source setting. The paraphrase-layer bullet equates the authoritative artifact with "the sibling PDF". That is the casebook corpus's storage convention, presented as if it were part of the general mechanism. It is the only unframed narrowing, so the outcome is WARN. The legal second-hand examples are explicitly framed as illustrations and are recorded only as info.
