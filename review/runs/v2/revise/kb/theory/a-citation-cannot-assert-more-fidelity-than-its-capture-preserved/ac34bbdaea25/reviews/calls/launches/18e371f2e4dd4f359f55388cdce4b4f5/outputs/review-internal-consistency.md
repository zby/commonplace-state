---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The one chance here is ingest, and what was not preserved verbatim then is permanently downgraded"
    reason: "'One chance' and 'permanently downgraded' clash with the continuation 'recoverable only by returning to the authoritative artifact and capturing again' and with the opening 'The only operation that raises fidelity is re-capture'. A reader can reconcile them by reading 'permanently' as 'for this capture', but the summary-level wording claims more finality than the body allows."
    level: info
  - scope: passage
    quotes:
      - "Two spans at the same file offset can differ in provenance quality by a full layer"
    reason: "The layer section places verbatim and paraphrase material in distinct regions of the snapshot (a verbatim block and a paraphrase summary). If 'file offset' means an offset in the snapshot, two spans from different regions cannot share it, so the corollary's example contradicts the structure described earlier. Under another reading, an offset into the authoritative source, there is no contradiction. This needs the author to confirm the intended reading."
    level: info
  - scope: passage
    quotes:
      - "the captured text is itself another party's restatement"
    reason: "Possible definition drift. The section heading and description present layers as products of forced, lossy capture. The second-hand layer, however, is defined by the source's provenance chain, which exists before capture. The opening says fidelity is 'spent at capture', but for second-hand material part of it was spent before capture."
    level: info
outcome: pass
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
