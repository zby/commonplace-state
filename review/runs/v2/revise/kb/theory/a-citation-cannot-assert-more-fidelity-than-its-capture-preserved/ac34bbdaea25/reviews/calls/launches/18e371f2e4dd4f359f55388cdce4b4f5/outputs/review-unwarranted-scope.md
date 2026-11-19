---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A long source cannot be captured verbatim into markdown at full fidelity, because the consumer's context window is finite and because copyright forces trims."
    reason: "The description and section heading claim that layering is forced for every framework 'whose consumer is an LLM and whose sources are real documents'. The two premises cover only part of that class. A finite context window limits what a consumer reads at once, not what the snapshot stores, since a full verbatim snapshot can be read in chunks. Copyright forces trims only for sources whose licence forbids full reproduction, and long public-domain or openly licensed documents are outside that. The note states no transfer relation from the premises' domain (long, reproduction-restricted sources stored under a single-read budget) to the claimed class. The surplus is not marked conjectural, and the rival-absence claim that would close the gap is asserted without a presented search."
    level: warn
  - scope: passage
    quotes:
      - "The claim bites exactly where capture is lossy, which is to say wherever the sources are long."
    reason: "The Scope section equates 'lossy' with 'long'. Under the note's own premises, however, lossiness also requires a reproduction restriction or a storage constraint. That makes the boundary statement broader than the support, since it includes long, freely reproducible sources. It is a supporting claim, but it defines the area of reliance the note invites."
    level: info
outcome: warn
---

# Review

**Claimed scope.** Two scopes are in play. (1) Citations to lossy captures can assert no more fidelity than the capture preserved, and no downstream notation, locator or gate can raise it. (2) Per the description and the layering section, capture is necessarily layered for any LLM-consumer framework over real documents.

**Presented support.** Claim 1 is derived from the layer definitions and the derived-copy rule's mechanical-derivation precondition. Its exercised domain matches its claimed domain: wherever a passage lacks a mechanical rule back to its source, notation cannot supply one. The Scope section correctly withdraws the claim for lossless sources. Claim 1 passes.

Claim 2 is derived from two premises, a finite context window and copyright trims, plus an unreported rival search, and is backed by one corpus observation (ADR 046's casebook run). Those premises hold for long sources under reproduction restrictions and for designs that store only what one read can consume. The claim is phrased for all frameworks with an LLM consumer and real sources. The note neither argues why the premises reach freely licensed long sources or chunked full-text snapshots, nor marks that reach as conjecture. Because claim 2 appears in the description and frames the note, this is a WARN rather than INFO.
