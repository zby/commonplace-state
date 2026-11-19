---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

The note makes two attributions to linked targets; both resolve and both match.

- "This is a choice within the trade-off between checking cost and reliance risk" identifies the fail-on-mismatch choice as an instance of the linked note's title claim. The target (`checking-retained-results-trades-cost-against-reliance-risk.md`) states that how often to check depends on check cost relative to the risk of relying on stale or wrong content, and its completeness-mark section says an inexpensive, defined check makes enforcement attractive. The note's further qualification — reuse of the check's result accepts the risk of changes since it ran — matches the target's "assurance dates from the last check".
- "ADR 046 judges such false mismatches worse than no check" matches ADR 046's Consequences: an under-normalized checker "would produce false mismatches on correct quotes, which is worse than no check". The casebook-corpus attribution (mismatches dominated by editorial omission, bracketed substitution and case changes) matches ADR 046's prototype-run paragraph.

ADR 073 and ADR 094 are cited by number without links; they are citations of decisions rather than concept identifications, and the reading scope does not extend to unlinked files, so they were not checked under this gate.
