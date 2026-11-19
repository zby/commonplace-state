---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Three held results give it its economic form."
      - "is the same for every kind"
    reason: "The opening presents three 'held results' as the explanatory case. The first two cite theory notes. The third claims that the conversion machinery is the same for every kind of knowledge work. It has no citation, and it is close to the universality the conjecture is meant to test. The authoring instructions ask the opening to distinguish current facts from explanatory conjectures. They also ask that a transferable truth-apt claim live in kb/theory/ and be cited through a rests-on edge. This claim is labelled as held, but it is neither grounded nor marked as conjecture."
    level: warn
  - scope: passage
    quotes:
      - "Second kind first, extract later."
    reason: "The Feasibility and commitment scope clause asks, for each candidate presented as adoptable, for a feasibility argument or witness, its unresolved obstacles, and what adoption would commit consumers to and how readily it could be reversed. The proposal says option 2 is expected to be chosen. It names one risk (bespoke additions entrenching) but gives no feasibility witness: no second kind is identified, and the nearest prepared run is still KB building. It also does not say what adopting option 1 or 2 commits consumers to, or what reversing either option would disturb. The Forces section discusses entrenchment in general terms but does not tie it to the options."
    level: warn
  - scope: passage
    quotes:
      - "The trigger for an adoption decision is the first completed second-kind run with the comparison recorded."
    reason: "The adoption criteria are evidence for or against the conjecture, not criteria for adopting one of the three design options. Producing that evidence requires already running a second kind on the machinery, which is in effect option 2 (or option 1). The proposal does not say which option the trigger decides or which option yields the qualifying run. It also does not say what result would select option 1 over option 2. The clause asks the proposal to name what must be observed, built or decided for an option to be adopted, and what result would change the selection. It also asks that a deferred choice name the option that remains feasible in the meantime and any waiting costs. Those mappings are missing."
    level: warn
outcome: warn
---

# Review

## Summary

The note is a recognizable design proposal and meets most of the type's authoring instructions:

- **Proposal markers.** The description leads with "Proposal:". A dated current-state anchor separates shipped facts from the proposal and correctly marks the refinement interface as unpromoted.
- **No adoption decision.** The proposal explicitly declines to choose among its options.
- **Option space.** It is inspectable. It has three materially different routes, and the third (no shared layer) works as the rival the conjecture must beat.
- **Universality axis.** The axis is declared, and transferable premises are cited as rests-on notes.
- **Operativity and warrant.** The section states honestly that there is no consumer yet, names the delivery channel, and reuses the ablation proposal's oracle instead of adding one.

## Unmet instructions

The gaps concern how the options connect to feasibility and adoption:

- **Explanatory case.** One of the three "held results" is an uncited universality claim, presented as fact rather than conjecture.
- **Feasibility and commitment scope.** The options get only brief cost remarks. None of them, including the one the note expects to be chosen, gets a feasibility witness or a statement of what adoption would commit consumers to and how reversible it would be.
- **Adoption criteria.** The criteria test the overarching conjecture, not a selection among the options. The proposal never says which option the second-kind run would come from or which option the triggered decision would adopt.

These are specific instructions left unmet within a proposal that conforms overall, so the outcome is WARN rather than FAIL.
