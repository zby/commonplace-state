---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "branch allocation"
    reason: "\"Branch allocation\" appears only in this list item with no gloss; the note never says what branches are (search branches, candidate lines of work, code branches) or what allocating them means, so a reader without KB context cannot tell what consequence of fit this item names. Add a short gloss, e.g. which candidate lines of work receive effort."
    level: warn
  - scope: passage
    quotes:
      - "stronger mediation evidence"
    reason: "\"Mediation evidence\" is a technical term (evidence that the claim causally mediates the change in work) used without a gloss. The surrounding sentence about withholding, replacement or perturbation gives enough context to infer it, so this is minor; a brief parenthetical would make the contrast with \"operative fit\" and \"selection evidence\" explicit."
    level: info
outcome: warn
---

# Review

Most technical terms are glossed or inferable at first use. "Working theory" and "theory fit" are grounded by the opening paragraph; "fixed oracle" is paraphrased in the next paragraph as an automatic evaluator that fully decides fit; "selection environment" is explained in the same sentence that introduces it; "self-sealing", "held-out demands" and "read-back" are inferable from their sentences. No active vocabulary term from `AGENTS.md` is used in a technical sense in the body ("refinement path" uses bare refinement in its ordinary sense).

The one term a newcomer cannot recover is "branch allocation", which appears in the list of fit consequences without any context about what branches are. "Mediation evidence" is inferable but would benefit from a short gloss.
