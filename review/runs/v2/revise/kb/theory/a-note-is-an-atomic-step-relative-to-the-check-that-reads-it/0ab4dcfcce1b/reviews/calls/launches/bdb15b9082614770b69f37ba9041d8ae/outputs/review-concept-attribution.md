---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "which is an instance of the general rule that"
    reason: "The note calls check-relative atomicity an instance of the oracle-domain rule. The target's domain concept matches the gloss the note gives ('the range of candidates it can assess with the required confidence'). The target's rule, however, is about warranted evaluation autonomy in proposal-selection loops, and its Scope section restricts it to that pathway. The shared concept, a checker's domain, supports the identification, so this is not a mismatch. 'Applies the domain concept from' would state the relation more exactly than 'an instance of the general rule'."
    level: info
outcome: pass
---

# Review

I checked every sentence that identifies one of this note's concepts with a concept from a linked note:

- **Co-loading bound / short composable notes.** The target grounds note size in bounded context and in the number of co-loadable notes as the surface area for shared structure. The note reproduces this.
- **Atomicity relative to a check / oracle domain.** The match is acceptable; see the info finding.
- **The boundary of automation is the boundary of verification.** It is cited as the general dependence, which is the target's title claim.
- **Validated quote as a derived copy.** The target defines a checked copy as one a validator re-derives and fails on mismatch. ADR 046 makes the same identification for verbatim quotations, so the note's "applied to citation" matches.
- **Citation fidelity.** The target says that only re-capture raises fidelity. This matches "cannot be quoted into this route without returning to the source".
- **Linked notes are not sources.** The target's distinction between a grounding obligation and a representation obligation matches the note's use.
- **ADR 073 and `(snapshot required)`.** The ADR introduces retained verbatim quotes and a marked snapshot-required route. This matches.

The archived proposal *Exceeding a review budget splits the task* is named but not linked, so its attribution cannot be checked under this review's reading scope.
