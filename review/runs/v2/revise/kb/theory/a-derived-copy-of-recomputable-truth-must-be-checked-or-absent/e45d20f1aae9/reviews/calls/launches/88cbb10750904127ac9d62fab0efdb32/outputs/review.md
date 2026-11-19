---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky. An unenforced copy is always one missed edit away from the catastrophic state, with nothing watching."
    reason: "This closing paragraph restates the asymmetry the preceding paragraph already set out (one bounded recomputation vs. silent, unbounded wrongness, already announced as 'the rule rides entirely on that'). Its one new job is the 'forbidden rather than merely risky' stance. Fold that phrase into the end of the previous paragraph and drop the recap and the 'one missed edit away' sentence."
    level: warn
  - scope: passage
    quotes:
      - "Machine-followable suffices; human visibility is not required once the validator carries the interrupt."
    reason: "This repeats the earlier statement that the validator is the edit-time surface and 'lineage only needs to sit where a machine can follow it, not where a human will see it.' The precondition is fully stated by its first two sentences. Keep the point in only one place."
    level: warn
  - scope: passage
    quotes:
      - "A checkable claim is enforced as a check or not asserted at all."
    reason: "The bullet's closing sentence restates its own opening imperative ('Never write the unenforced natural-language version of a checkable claim') and adds nothing to it. Cut it."
    level: warn
  - scope: passage
    quotes:
      - "applied not only to caches but to every derived copy of recomputable truth"
    reason: "Defensive redundancy: calling the rule 'the general form' of the cache maxim already means it reaches beyond caches. The trailing clause restates that. Cut it, or merge the maxim into the opening or the asymmetry section, where it would frame the rule instead of sitting alone after the instances."
    level: warn
outcome: warn
---

# Review

The note's main structure earns its space. The opening rule, the regime boundary (managed staleness vs. Level A enforcement), the third class from enforcement, the four preconditions and the four instances each do separate work. The instances section is not a recap. It maps the instances onto distinct application states and supports the claim that the rule generalizes.

The redundancy is local. Two closing restatements repeat the openings of their own units: the asymmetry section's second paragraph and the "never write" bullet. One point appears twice, in two sections: lineage needs only to be machine-followable. The final cache-maxim line ends with a clause that its own "general form" phrase already entails. Each fix is a cut or a fold of a few words. None removes an argument step.

Non-obvious passes. The "Checked copies degrade gracefully" bullet echoes the asymmetry but adds the lifecycle-exit consequence, so it passes. The amortization remark in instance 1 applies precondition 4 to a concrete case instead of restating it, so it also passes.
