---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The only operation that raises fidelity is re-capture."
    reason: "The note never defines 're-capture', and the Scope section counts 'return to the authoritative artifact and quote-mine it' as one. So any downstream operation that consults the original, such as a review gate reading the sibling PDF, can be relabelled re-capture rather than counted as a counterexample to 'no review gate can promote a passage'. This leaves the non-increase claim close to definitional at its boundary. The core mechanism (paraphrase has no mechanical derivation rule back to its source) is real, but its exclusion of downstream promotion is protected by the elastic term rather than constrained by it."
    level: info
outcome: pass
---

# Review

The central claim is that a citation cannot assert more fidelity than its capture preserved. The note offers a mechanism for it. A verbatim quote has a mechanical derivation rule back to the snapshot: substring match. A paraphrase has none, so no notation can make a paraphrase checkable as source text. Marking it verbatim only attaches a stronger trust signal to an unchecked copy.

Variation test: change the premise that capture is lossy and the conclusion moves. The Scope section shows this directly. With a lossless short source, the layers collapse and the bound becomes vacuous. Change the premise that paraphrase lacks a derivation rule, for example by imagining a mechanical paraphrase-to-source check, and the "notation cannot repair it" conclusion would fail. The argument therefore constrains the conclusion and is not merely adaptive.

Falsifiability: a downstream operation that raises a passage's provenance grade without consulting the original would contradict the claim. That gives the claim content. The INFO finding notes that "re-capture" is broad enough to absorb operations that do consult the original. This thins the boundary but leaves the mechanism standing.

No ad-hoc escape hatches beyond that were found. The Scope section narrows the claim through a stated premise change, not a protective exception.
