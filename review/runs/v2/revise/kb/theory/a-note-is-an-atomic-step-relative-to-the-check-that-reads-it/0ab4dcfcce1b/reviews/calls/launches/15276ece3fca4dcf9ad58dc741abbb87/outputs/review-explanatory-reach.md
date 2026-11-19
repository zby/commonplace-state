---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "An artifact-side bound does not have that failure mode, because a conforming artifact fits by construction"
    reason: "This sub-argument assumes that a validator can decide conformance mechanically. However, the note's unit (the unquoted source) depends on whether a source's support for a claim is carried by a quotation, and deciding that is partly a judgment. The mechanism for why the artifact-side bound avoids silent failure is plausible but not yet constrained enough to show the count is mechanically decidable."
    level: info
outcome: pass
---

# Review

The central claim is that a note's atomicity is relative to the check applied to it, and that for the grounding check the unit of cost is the unquoted source. The note gives a mechanism for this: the grounding check's cost is the work of finding the supporting passage in each artifact. A verbatim quote moves that finding step into a substring validator, so a quoted source no longer adds to that cost, while a snapshot-required source still adds its full cost.

The mechanism is hard to vary. If the validator is removed, quoting no longer discharges the finding step, and the note says so in Scope. If the cost is counted in links or bytes, the multi-source single-claim examples stop separating the two bounds. The claim is also falsifiable. A grounding check whose cost did not fall when sources were quoted, or a corpus where the two bounds never diverged, would count against it. The note does not add escape hatches. Occurrence-versus-representativeness and snapshot-required claims are stated as priced limits, with their consequence for the count. The supporting sub-argument that an artifact-side bound fails loudly is thinner, as noted.
