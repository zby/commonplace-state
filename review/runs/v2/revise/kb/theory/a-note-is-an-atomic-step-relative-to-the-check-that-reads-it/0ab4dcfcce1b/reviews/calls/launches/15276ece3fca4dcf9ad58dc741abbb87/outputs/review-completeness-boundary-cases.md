---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Links to other notes are also not sources in this sense"
    reason: "The source/non-source split covers ingests (quoted, unquoted, snapshot-required) and linked notes, but not other linked artifacts the note itself relies on as evidence: ADRs and the retained report under kb/reports/retained/. Those map onto the 'linked note' branch only if they carry a claim title and their own grounding review, which the note does not state. Coverage is possible but strained."
    level: info
  - scope: passage
    quotes:
      - "A source that has been quoted verbatim is not one of them."
    reason: "The unit is defined per source (quoted vs unquoted), but the mechanism is per cited claim: a source quoted for one claim and cited without a quote for another in the same note falls between the two categories. The finding-step mechanism resolves it (it counts for the unquoted use), but the stated unit does not."
    level: info
  - scope: passage
    quotes:
      - "because three candidates are available and they justify different values"
    reason: "The three-way enumeration of what kind of number N is (degradation point, smallest no-miss count, convention) is presented as exhaustive without argument; an adjacent candidate such as a cost budget for the author or a value derived from the co-loading bound is not considered. The enumeration's argumentative role is only to eliminate two options, so this is strained rather than broken."
    level: info
outcome: pass
---

# Review

The note's frameworks are the two bounds (co-loading and checking), the classification of linked material for the grounding check's cost (quoted source, unquoted source, snapshot-required source, linked note), and the three candidate kinds of N.

The two-bound framework holds at its boundaries: the note supplies both a case satisfying co-loading but not checking (the eight multi-source notes) and the converse case, and it says where the bounds couple. The linked-material classification handles the simplest case (one quoted source), the extreme case (claims needing a whole snapshot) and the joint-support case. It is strained at two adjacent cases. Linked artifacts that are neither notes nor sources, such as ADRs and retained reports, are not placed. A source used both quoted and unquoted is also not placed, because the unit is stated per source while the mechanism is per claim. The enumeration of N kinds is not argued exhaustive, but it only needs to eliminate two alternatives. None of these cases clearly falls outside the claimed coverage, so the gate passes with informational findings.
