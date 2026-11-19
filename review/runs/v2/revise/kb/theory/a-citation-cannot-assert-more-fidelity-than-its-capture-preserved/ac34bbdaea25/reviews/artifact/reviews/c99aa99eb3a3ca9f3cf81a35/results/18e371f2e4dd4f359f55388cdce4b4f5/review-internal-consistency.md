---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The one chance here is ingest, and what was not preserved verbatim then is permanently
    downgraded
  reason: '''One chance'' and ''permanently downgraded'' clash with the continuation
    ''recoverable only by returning to the authoritative artifact and capturing again''
    and with the opening ''The only operation that raises fidelity is re-capture''.
    A reader can reconcile them by reading ''permanently'' as ''for this capture'',
    but the summary-level wording claims more finality than the body allows.'
  level: info
- scope: passage
  quotes:
  - Two spans at the same file offset can differ in provenance quality by a full layer
  reason: The layer section places verbatim and paraphrase material in distinct regions
    of the snapshot (a verbatim block and a paraphrase summary). If 'file offset'
    means an offset in the snapshot, two spans from different regions cannot share
    it, so the corollary's example contradicts the structure described earlier. Under
    another reading, an offset into the authoritative source, there is no contradiction.
    This needs the author to confirm the intended reading.
  level: info
- scope: passage
  quotes:
  - the captured text is itself another party's restatement
  reason: Possible definition drift. The section heading and description present layers
    as products of forced, lossy capture. The second-hand layer, however, is defined
    by the source's provenance chain, which exists before capture. The opening says
    fidelity is 'spent at capture', but for second-hand material part of it was spent
    before capture.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/c99aa99eb3a3ca9f3cf81a35/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/c99aa99eb3a3ca9f3cf81a35/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-internal-consistency.md
raw-output-sha256: 7d1deda7f08ca7c12ba9d1dc7be247360ee78c2fdec55dc7a7d591629962fdf4
format: 2
---

# Review

Key claims by section:

- **Opening.** Fidelity is fixed at ingest and is non-increasing. Only re-capture raises it. Fidelity and authority move in opposite directions and compose as a ceiling plus earned weight.
- **Layering.** Capture is forced to be lossy for long sources, and the snapshot divides into verbatim, paraphrase and second-hand layers.
- **Notation.** Paraphrase has no mechanical derivation rule, so marking cannot raise its fidelity. The only repair is returning to the authoritative artifact.
- **Corollary.** Locators must encode the layer as well as position.
- **Scope.** Lossless short sources collapse the layers. Provenance quality is decided before writing.

No outright pairwise contradiction was found. The fidelity/authority distinction holds throughout, and the Scope section agrees with the corollary by placing the lossless case out of scope rather than in conflict.

Three tensions need the author's confirmation, and all are INFO. First, "permanently downgraded" sits beside "recoverable … capturing again". Second, the corollary's same-offset example sits uneasily with layers described as separate snapshot regions. Third, the second-hand layer does not fit the claim that the layers are produced by capture.
