---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A test available to the proposing system can be optimized without improving the capability it is meant to assess; human approval does not remove the need to justify the assessment."
    reason: "This sentence adds a separate mechanism: a proposing system can optimize against an available test (a Goodhart-style failure). That mechanism needs its own evidence, and it does not bound the note's claim about which judgment controls adoption. The bullet's first two sentences already state the needed boundary: approval does not establish quality. Delete the sentence or rehome it in a note on test gaming or evaluator independence."
    level: warn
outcome: warn
---

# Review

The main claim is that a judgment helps determine a change when it controls whether the change enters use. Assessment after adoption does not, through that assessment alone, contribute to selecting the change. What matters is the judgment's causal role, not whether a person or program makes it.

Most of the side material supports that claim in its current place:

- The two hypothetical cases are the note's central contrast.
- The remark that a later assessment could cause a future rollback limits the claim to the transition under examination.
- "One episode can contain both roles" blocks the redescription move named in the description.
- The definition of adoption, with its link to operative change, fixes the term the claim depends on.
- The first two Scope bullets are boundary conditions. The second also motivates the single open question.
- The first two sentences of the third bullet ("Approval does not establish quality…") are also a boundary condition. They stop readers from treating selection as endorsement.

The final sentence of that bullet is the one branch that needs action. It introduces test optimization by the proposing system. That is a different failure mechanism, with its own evidence requirements, and the note neither defends it nor needs it. Here it widens the attack surface and shifts the reader's attention from causal role to evaluation validity. Removing it leaves the boundary condition intact.
