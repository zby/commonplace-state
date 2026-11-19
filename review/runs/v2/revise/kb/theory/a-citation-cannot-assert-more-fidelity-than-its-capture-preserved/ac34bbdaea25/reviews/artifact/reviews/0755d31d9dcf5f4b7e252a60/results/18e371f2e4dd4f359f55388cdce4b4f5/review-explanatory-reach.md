---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The only operation that raises fidelity is re-capture.
  reason: The note never defines 're-capture', and the Scope section counts 'return
    to the authoritative artifact and quote-mine it' as one. So any downstream operation
    that consults the original, such as a review gate reading the sibling PDF, can
    be relabelled re-capture rather than counted as a counterexample to 'no review
    gate can promote a passage'. This leaves the non-increase claim close to definitional
    at its boundary. The core mechanism (paraphrase has no mechanical derivation rule
    back to its source) is real, but its exclusion of downstream promotion is protected
    by the elastic term rather than constrained by it.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/0755d31d9dcf5f4b7e252a60/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/0755d31d9dcf5f4b7e252a60/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-explanatory-reach.md
raw-output-sha256: f40f34ffab39127b2d105bb33c0300b4cf07eec1ece8650e90a153b836eca85b
format: 2
---

# Review

The central claim is that a citation cannot assert more fidelity than its capture preserved. The note offers a mechanism for it. A verbatim quote has a mechanical derivation rule back to the snapshot: substring match. A paraphrase has none, so no notation can make a paraphrase checkable as source text. Marking it verbatim only attaches a stronger trust signal to an unchecked copy.

Variation test: change the premise that capture is lossy and the conclusion moves. The Scope section shows this directly. With a lossless short source, the layers collapse and the bound becomes vacuous. Change the premise that paraphrase lacks a derivation rule, for example by imagining a mechanical paraphrase-to-source check, and the "notation cannot repair it" conclusion would fail. The argument therefore constrains the conclusion and is not merely adaptive.

Falsifiability: a downstream operation that raises a passage's provenance grade without consulting the original would contradict the claim. That gives the claim content. The INFO finding notes that "re-capture" is broad enough to absorb operations that do consult the original. This thins the boundary but leaves the mechanism standing.

No ad-hoc escape hatches beyond that were found. The Scope section narrows the claim through a stated premise change, not a protective exception.
