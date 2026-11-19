---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "an absence of that kind is a validator's result rather than a reviewer's finding"
    reason: "This frames the mechanism as the validator. The verbatim validator only checks quotations that are present: it resolves each `verbatim`-marked quote against its linked source. It cannot detect that a claim lacks a retained passage. The next sentence shows the real mechanism, which is counterfactual: had the author quoted the details, the validator would then have checked the quote. Detection therefore moves from the reviewer to authoring discipline, which the bound requires, plus the validator's check of whatever was quoted. As written, the sentence excludes the case that the absence goes unquoted and the validator says nothing."
    level: warn
  - scope: passage
    quotes:
      - "the bound is held by a validator that fails the note, not by a reviewer that stops reading"
    reason: "This presents the artifact-side bound as held by an existing validator, while the Scope section says the note does not decide N or 'a validator rule that would enforce it'. The mechanism is accurate for the proposed placement, but the present tense frames it as something already in force. Making the conditional explicit ('would be held') would match the scope."
    level: info
  - scope: passage
    quotes:
      - "Sizing a step to its checker rather than to the material is old."
    reason: "Descartes is introduced as a precedent for sizing to the checker, but the quoted precept sizes parts to 'its adequate solution', and the note itself concludes 'The parts are sized to the solution'. Only the evidence of simple links points implicitly to a checker. The next paragraph partly corrects this ('Lamport makes the checker explicit'). The lead sentence emphasizes checker-relativity more than the Descartes evidence carries."
    level: info
outcome: warn
---

# Review

Most of the note's mechanistic sentences identify their mechanism at the right level. Examples are the cost of the grounding check as the number of unquoted artifacts to search, a review-side budget failing silently, and the evidence from occurrence versus representativeness. The note also scopes itself to the grounding check and says the unit would need to be re-derived for any other check. That avoids the main generality risk for this gate.

The warning concerns the reinterpretation of the paired experiment. It assigns detection of a missing retained passage to the validator, but the validator only checks quotations that are present. Under an artifact-side bound, the absence is prevented when the author has to quote. It is not detected by a validator. The two info findings concern emphasis: present-tense wording for a validator that the Scope section says is undecided, and checker-relative framing for a Descartes quotation that sizes parts to the solution.
