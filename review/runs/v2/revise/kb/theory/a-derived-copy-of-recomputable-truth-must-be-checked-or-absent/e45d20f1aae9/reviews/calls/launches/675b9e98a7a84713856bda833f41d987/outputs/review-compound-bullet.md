---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The sweep pattern is hand-authored, but it executes as a strict mechanical extraction"
    reason: "The `complete`-mark bullet makes two separable points. The first is that the mark is enforced: a validator re-derives membership and fails mismatches. The second, joined by `but` and a dash, is that the hand-authored sweep pattern does not reopen the regress because of precondition 4's amortization argument. That second point stands on its own as a claim about validator trust, and readers scanning the instance list are likely to miss it. It could be its own bullet or sentence, or move to precondition 4."
    level: warn
  - scope: passage
    quotes:
      - "A derivation rule that is itself a judgment call rather than a strict mechanical extraction does not meet this precondition"
    reason: "Precondition 4 argues that a central validator ends the regress through amortization. Its closing sentence adds a separate disqualifying condition: a validator whose derivation is a judgment call is the forbidden state moved down a layer. The two points are related, and the second can be read as the boundary of the first, so this is borderline. It is reported for awareness only."
    level: info
  - scope: passage
    quotes:
      - "currently resolved by omission (read the contract live)"
    reason: "The hot-path-skills bullet states its current state (omission) and then recommends enforcement as the dominant alternative. The bullet is short, and the recommendation follows from the current state, so this reads as one point with elaboration. It is noted only as a mild case."
    level: info
outcome: warn
---

# Review

Most long list items develop one idea with supporting detail. Examples are the Consequences bullets, the bullets for compiled views and duplicated build artifacts, and preconditions 1–3. Elaboration such as "Machine-followable suffices" or the ADR 025 and skill-edit examples supports the item's own claim and is not a second claim.

The clear case is the `complete`-mark instance bullet. After describing the enforced validator, it appends a separate argument about why a hand-authored sweep pattern is still acceptable. That argument concerns validator trust, and it repeats precondition 4. Embedded in an instance bullet, it gets lost when readers scan the list. Precondition 4 and the hot-path-skills bullet are borderline and recorded as INFO.
