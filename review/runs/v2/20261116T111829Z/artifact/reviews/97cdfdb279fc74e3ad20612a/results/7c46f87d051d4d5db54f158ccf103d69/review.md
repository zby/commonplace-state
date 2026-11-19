---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Three held results give it its economic form.
  - is the same for every kind
  reason: The opening presents three 'held results' as the explanatory case. The first
    two cite theory notes. The third claims that the conversion machinery is the same
    for every kind of knowledge work. It has no citation, and it is close to the universality
    the conjecture is meant to test. The authoring instructions ask the opening to
    distinguish current facts from explanatory conjectures. They also ask that a transferable
    truth-apt claim live in kb/theory/ and be cited through a rests-on edge. This
    claim is labelled as held, but it is neither grounded nor marked as conjecture.
  level: warn
- scope: passage
  quotes:
  - Second kind first, extract later.
  reason: 'The Feasibility and commitment scope clause asks, for each candidate presented
    as adoptable, for a feasibility argument or witness, its unresolved obstacles,
    and what adoption would commit consumers to and how readily it could be reversed.
    The proposal says option 2 is expected to be chosen. It names one risk (bespoke
    additions entrenching) but gives no feasibility witness: no second kind is identified,
    and the nearest prepared run is still KB building. It also does not say what adopting
    option 1 or 2 commits consumers to, or what reversing either option would disturb.
    The Forces section discusses entrenchment in general terms but does not tie it
    to the options.'
  level: warn
- scope: passage
  quotes:
  - The trigger for an adoption decision is the first completed second-kind run with
    the comparison recorded.
  reason: The adoption criteria are evidence for or against the conjecture, not criteria
    for adopting one of the three design options. Producing that evidence requires
    already running a second kind on the machinery, which is in effect option 2 (or
    option 1). The proposal does not say which option the trigger decides or which
    option yields the qualifying run. It also does not say what result would select
    option 1 over option 2. The clause asks the proposal to name what must be observed,
    built or decided for an option to be adopted, and what result would change the
    selection. It also asks that a deferred choice name the option that remains feasible
    in the meantime and any waiting costs. Those mappings are missing.
  level: warn
outcome: warn
description: Retained verdict review of kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
  against kb/reference/types/design-proposal.md
contract: verdict
note: kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
criterion: kb/reference/types/design-proposal.md
note-sha256: 756b823f38fd3e59583f849f7dff5410799fdfe37375cc6e92a6873c008573d1
criterion-sha256: cb161c022ae205bf81d8b35b5d00de450b06c8cd9a601042372941957d94b9e9
target-sha256: 756b823f38fd3e59583f849f7dff5410799fdfe37375cc6e92a6873c008573d1
target-capture: kb/reports/state/review/runs/v2/20261116T111829Z/artifact/reviews/97cdfdb279fc74e3ad20612a/inputs/target/kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
observation: kb/reports/state/review/runs/v2/20261116T111829Z/artifact/reviews/97cdfdb279fc74e3ad20612a/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T111829Z
launch: 7c46f87d051d4d5db54f158ccf103d69
completed-at: '2026-11-16T11:19:19Z'
raw-output: kb/reports/state/review/runs/v2/20261116T111829Z/calls/launches/7c46f87d051d4d5db54f158ccf103d69/outputs/review.md
raw-output-sha256: 0ea33d0a0cd60818e449f8d5078cf023911133ca5168dbe614544a647e771525
format: 2
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
