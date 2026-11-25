---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"
    reason: "The note gives a mechanism for why some semantic work remains on the model: mechanical work moves into code, and semantic work can be relocated but not eliminated. It gives no mechanism for why the remainder divides into these three competences. Splitting competence 2 into diagnosis and synthesis, or merging competences 2 and 3, leaves the supporting argument unchanged. The count in the title is therefore easy to vary."
    level: warn
  - scope: passage
    quotes:
      - "Any sub-task shown to be reliably offloadable to harness code moves out of the LLM column, and concrete bottlenecks discovered in practice can add to it"
    reason: "The list can shrink when sub-tasks prove offloadable and grow when new bottlenecks appear. This revisability lets any observation be absorbed without falsifying the claim that 'three irreducible' competences remain, and it does not sharpen the explanation of why these three. That is ad-hoc accommodation of the enumerated claim. The general claim that some semantic floor remains is still falsifiable."
    level: warn
  - scope: passage
    quotes:
      - "spotting semantic conflicts between prose rules, refactoring them into a cleaner abstraction, or proposing a revised check reduces to competences 2 and 3 applied to the store and its criteria"
    reason: "The reduction of store maintenance and criterion revision to competences 2 and 3 is asserted rather than explained. It protects the three-item count without saying what makes those activities instances of diagnosis and trade-off judgment."
    level: info
outcome: warn
---

# Review

## Summary

The note's broad claim has a real mechanism. Harness code can absorb bookkeeping, replay and enforcement through the scheduler–LLM error-correction asymmetry. Because semantic work cannot be eliminated, some meaning-dependent work stays on the frozen model in open-ended settings. That part is constrained: a demonstration that harness code reliably handles novel diagnosis, for example, would contradict it.

The title's specific claim, that harness offloading leaves *three* competences, is not constrained in the same way. Nothing ties the semantic residue to the three-way split instead of to another partition. The Scope clause lets members move in or out, so no observation can count against the enumeration. The independent-failure paragraph gives a reason to separate the competences: they can fail independently. That reason motivates diagnosis but does not derive the boundaries.
