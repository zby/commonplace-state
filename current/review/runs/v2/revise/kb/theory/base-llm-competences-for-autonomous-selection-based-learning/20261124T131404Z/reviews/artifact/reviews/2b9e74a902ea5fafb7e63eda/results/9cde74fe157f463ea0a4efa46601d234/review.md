---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - three irreducible semantic competences remain on the frozen base LLM
  reason: The collection treats qualifiers in the opening claim as obligations. 'Irreducible'
    is the strongest qualifier in the thesis, but the argument does not support it.
    The cited premise (semantic work can be relocated but not eliminated) establishes
    that some semantic residue remains. It does not establish that these three competences
    are each irreducible. The note's own Scope also says any sub-task shown to be
    offloadable leaves the LLM column. Drop the qualifier, or state the irreducibility
    as the conjectured part and name what would refute it.
  level: warn
- scope: passage
  quotes:
  - 'evidenced-by: weak-model lines produced no held-out harness gains under a loop
    that lifted stronger models (bounded to one benchmark and loop)'
  reason: Under 'Origin is not corroboration', an evidenced-by context phrase must
    either say what the claim risked and how the evidence relates in time to the claim
    (corroboration) or say that the evidence qualifies or bounds the claim. This phrase
    only describes the finding and limits the evidence's own scope. The body calls
    the source an 'illustration' of a base-model floor, which supports at most the
    existence of a floor and not the three-competence split. The phrase should say
    it qualifies or bounds the floor premise, or the link should be relabelled if
    the claim was abstracted from this source.
  level: warn
- scope: passage
  quotes:
  - not an established impossibility result
  reason: The opening already declares the note a working hypothesis twice. Restating
    this in Scope as 'a working hypothesis, not an established impossibility result'
    matches the pattern the contract calls padding against an objection that is already
    closed. The rest of the bullet, which says what would move items in or out of
    the LLM column, is a useful named boundary and should stay.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/theory/COLLECTION.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/9cde74fe157f463ea0a4efa46601d234/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/2b9e74a902ea5fafb7e63eda/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 9cde74fe157f463ea0a4efa46601d234
completed-at: '2026-11-24T13:16:51Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/9cde74fe157f463ea0a4efa46601d234/outputs/review.md
raw-output-sha256: fa3a1c3210717e525c0ad9abbee75006fb2c3b317010e652e5825bf2c3d5f603
format: 2
---

# Review

## Summary

Placement in `kb/theory/` is correct. Apart from scoping, the note makes a contestable claim about the design space: harness code can take over loop bookkeeping, enforcement and replay, while three semantic competences stay on a frozen base LLM. It names no Commonplace-specific choice that would need recoverable scoping, so it does not collapse into a record of what Commonplace selected. Its conjectural force is visible in the description, the opening and the Scope section, as the "Hypotheses stay recognizable in prose" convention requires. The claim reads as universal, conditioned on open-ended work, and the necessary/not-sufficient boundary is stated in Scope. Real gaps sit in Open Questions rather than being hedged into the claim.

Link practice mostly conforms. Inline links carry connectives ("Following", "yet"). Footer entries use labels from the table with suitable destinations: `defined-in` for definitions, `grounds` and `extends` for theory notes, and `evidenced-by` for the source ingest. The note links to no `kb/work/` path and no snapshot. It cites one tracked source without a quotation, well under the unquoted-source limit of five, and hosts that source in a body sentence rather than only in the footer.

Two conventions are partly unmet:

1. **Qualifier obligation.** The "irreducible" qualifier in the thesis is stronger than the argument and conflicts with the note's own Scope.
2. **Origin is not corroboration.** The `evidenced-by` footer phrase neither states a risked test nor says that the source qualifies or bounds the claim.

A minor redundant hedge in Scope is noted as info.
