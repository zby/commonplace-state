---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A workflow that bundles all three manufactures urgency even when the worker's local judgment is sound."
    reason: "Body composability: the unbundling of stop, retention and operator-action decisions is a second claim, with its own refuter, beside the title's conflict claim. A note citing this one only for the isolation/prioritization conflict also imports the unbundling claim. The description announces the split, and the section follows from the conflict, so this is a candidate for extraction if other notes start citing the unbundling alone. It is not a breach of the convention now."
    level: info
outcome: pass
---

# Review

## Summary

The note conforms to the `kb/theory/` collection contract.

**Placement.** The intended contribution is a design-space claim: under bounded effective context and a competing workload that does not fit beside task context, isolating a worker for focus removes the comparison set that global prioritization needs. Scoping the named Commonplace mechanisms (deferred traversal logging, ADR 138, the unresolved frontier) leaves the claim intact. The note labels them as "local design examples, not corroboration", so they serve as illustration and do not form the intended contribution. The note is not a record of Commonplace selections, a procedure or a design proposal.

**Explanatory-reach and claim formulation.** The note declares its claim mode in a named line ("Claim mode: universal") and states the conditions and what would refute it. That meets the modality convention. The boundaries the argument depends on (bounded context, combined state exceeding the window) are in the claim. Other limits are in `## Scope`: relational versus intrinsic checks, and allocation versus objective choice. Real gaps are named in `## Open Questions` rather than hedged. The note separates the mechanism (missing comparison set) from the failure direction (workflow defaults), which predicts how the conclusion changes when a premise changes. Defensive padding is minimal.

**Origin is not corroboration.** The Nostalgebraist source is linked `abstracted-from` with "origin, not corroboration". The body reports what that account does not isolate. The Scope section says that neither the account nor the Commonplace mechanisms give a controlled comparison. No `evidenced-by` edge claims corroboration.

**Outbound links.** Every footer label suits its destination under the contract's table. `grounds`, `extends`, `contrasts`, `mechanism` and `enables` point to theory notes. `defined-in` points to `reference/definitions/`. `abstracted-from` points to a tracked ingest in `sources/`. Each footer entry has a context phrase that states the reader need. The ADR 138 link is inline and has prose explaining its role. The note does not link into `kb/work/` or into a snapshot.

**Source grounding.** The note cites one tracked source. It cites that source in the body, and each verbatim quotation has its own citation immediately after it. This is well within the five-source unquoted limit.

The one INFO finding concerns body composability. It is recorded for future splitting and does not count against conformance.
