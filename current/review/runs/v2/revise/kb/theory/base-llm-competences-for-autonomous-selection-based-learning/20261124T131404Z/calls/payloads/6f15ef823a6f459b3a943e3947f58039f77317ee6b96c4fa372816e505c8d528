---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/theory/COLLECTION.md
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 2853d9852e734b45b9cf2119940d79ca
completed-at: '2026-11-24T13:16:52Z'
findings:
- scope: passage
  quotes:
  - This split is a **working hypothesis**, not an established impossibility result.
  reason: The contract's 'Don't defend against objections you've already closed' convention
    names this exact pattern ('a hypothesis to be tested, not a definitional truth')
    as padding. The conjectural force is already declared in the description and in
    the bolded opening 'Working hypothesis.', so restating it with a 'not an established
    ...' contrast in Scope pre-empts a misreading that the earlier text has already
    ruled out. The second sentence of the bullet, which names how the column can change,
    is the part worth keeping.
  level: warn
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: 'The contract treats qualifiers in the title, description, opening claim
    and main proof as obligations. ''Irreducible'' is not argued in the body, and
    Scope withdraws it: any sub-task shown to be offloadable ''moves out of the LLM
    column''. The title''s hedges (''may offload much of'') run the other way and
    leave the offloading half of the claim close to vacuous. The claim should be stated
    at the strength the argument supports, for example ''three semantic competences
    that harness code does not yet supply'', with the offloading claim given a stated
    boundary or kept to the listed functions.'
  level: warn
- scope: passage
  quotes:
  - 'evidenced-by: weak-model lines produced no held-out harness gains under a loop
    that lifted stronger models (bounded to one benchmark and loop)'
  reason: Under 'Origin is not corroboration', an evidenced-by context phrase must
    either say what the claim risked (for corroboration) or say that the evidence
    qualifies or bounds the claim. This phrase reports a result and its limit but
    does not say which role it plays. The body calls it an 'illustration', and the
    source supports only a base-model floor, not the three-competence split. The phrase
    could say directly that the evidence bounds or illustrates the floor claim rather
    than corroborating the split.
  level: info
contract: verdict
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/2853d9852e734b45b9cf2119940d79ca/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/2b9e74a902ea5fafb7e63eda/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/2853d9852e734b45b9cf2119940d79ca/outputs/review.md
raw-output-sha256: cf47d59e6d44c144cb947fdd288fadc9139699f4bf90da412b19c4a672227b42
---

# Review

The note belongs in `kb/theory/`. Once its named elements (harness code, a frozen base LLM, a selection-based learning loop) are scoped, it still makes a claim about the design space: how the work of an autonomous selection loop divides between harness code and the base model. It does not record a Commonplace selection. The description and the bolded opening both declare its conjectural force, and an Open Questions section names the remaining gaps, as the hypothesis convention requires.

The outbound links follow the collection's conventions. Each footer entry uses a label from the table with a valid destination: `defined-in` points to `theory/definitions`, `grounds` and `extends` stay within theory, and `evidenced-by` points to a tracked ingest. The inline links use connective framing ('Following', 'yet'). There are no links into `kb/work/` and no links to snapshots. Source grounding stays well inside the bound: there is one unquoted tracked source, and it is cited in a body sentence, not only in the footer.

Two conventions go unmet, so the outcome is warn. First, the Scope bullet repeats the hypothesis status in the defensive form that the contract specifically calls padding. Second, the claim's qualifiers do not match the argument. 'Irreducible' is stronger than the body supports, and Scope takes it back. The title's 'may ... much' is weaker than the note's actual commitment. A smaller point is that the `evidenced-by` context phrase does not say whether the source corroborates the claim or only bounds it.
