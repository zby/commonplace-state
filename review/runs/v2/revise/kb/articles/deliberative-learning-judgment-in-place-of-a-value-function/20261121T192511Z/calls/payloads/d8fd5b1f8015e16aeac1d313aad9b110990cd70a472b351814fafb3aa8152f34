---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: 0639a8d235bbdf791feaa2f1eae21d28a4131c0fe56e0a15fefe51fa524835cf
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/synthesis
launch: 7af52ce228c64935a22d9a85bfab5e8d
completed-at: '2026-11-21T19:32:54Z'
findings:
- scope: passage
  quotes:
  - putting a fixed-weight language model in the judge slot turns deliberative learning
    into an automated machine learning paradigm
  reason: 'The article states its second-level bet twice, and the two versions differ.
    The opening calls it an automated machine learning paradigm and attaches a five-capability
    list that ends in the Bitter Lesson. The bold sentence at the end of ''Proof,
    formula, judgment'' commits to something narrower and more testable: autonomous
    double-loop learning with targeted correction where no fixed criterion is adequate.
    The first-level claim in the opening also shares its paragraph with a gloss on
    compatible value functions, a novelty concession and a no-guarantee caveat. A
    reader can''t tell which version of the bet the evidence section tests. Direction:
    cut each opening claim paragraph to its main sentence and one caveat, and state
    the bet once in the opening in the form the article intends to test. Leave the
    capability list, the precedents and the compatible-value-function gloss to the
    sections that already develop them.'
- scope: passage
  quotes:
  - In real engineering and knowledge work, gains and losses fall on different tasks
  reason: 'On-balance judgment gives the article its title, but it enters as the fourth
    item in a run of historical precedents, under the same bold-label format as the
    Gödel machine, PRODIGY and EURISKO. It isn''t a precedent: it is the article''s
    proposal and the turn toward the bet. The paragraph also holds a stray rule about
    when to investigate an unknown, which the article never uses. The ''every reasonable
    measure'' formulation appears in three places: the opening gloss, this paragraph
    and the ''learned'' definition. A reader can''t easily see that the precedent
    sequence exists to motivate this slot, or where the concept is actually defined.
    Direction: mark the paragraph explicitly as the step the precedents lead to (for
    example its own lead-in or subsection), make it the one place on-balance judgment
    is defined, drop the value-of-information sentence, and have the opening and the
    evidence section point back to it.'
- scope: document
  quotes: []
  reason: 'In ''Deliberative learning versus training weights'', the comparison table
    is followed by a ''three payoffs'' paragraph that restates three of its rows,
    which the routing-line recap has already made concrete. The cost ledger that follows
    anticipates the four-hazard list in the final section: unfaithful rationales appear
    in both, and the faithfulness link appears only in the earlier one. The reader
    meets the same advantages twice and the same risk twice, and the comparison section
    ends up longer than its contrast needs. Direction: let the table carry the payoffs,
    moving the two links into its cells or into one sentence that introduces the costs.
    Keep the costs as limits on the form itself, and let the hazards section be the
    single home for the threats to the LLM-judge bet.'
contract: report
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/synthesis/calls/launches/7af52ce228c64935a22d9a85bfab5e8d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/synthesis/artifact/reviews/851501536899cc7cf909b7ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/synthesis/calls/launches/7af52ce228c64935a22d9a85bfab5e8d/outputs/review.md
raw-output-sha256: ffb1231d8f1409166396c3711a0b4185778b6f047740bae05fdaf930c7f34d1b
---

# Simplification synthesis: Deliberative Learning: Judgment in Place of a Value Function

## Opportunities

### 1. State each level of the thesis once, in the form the article tests

- Location: opening, the two paragraphs beginning "This article makes a two-level claim" and "Second, and this is our empirical bet". These should be compared with the bold sentence "We bet that a fixed-weight language model can fill the judge slot autonomously, running double-loop deliberative learning with targeted correction for work where no fixed criterion is adequate" in "Proof, formula, judgment: where the bet enters".
- Combines: core-claim-obscured (both INFO findings: the crowded first-level paragraph and the diverging second-level formulations).
- Preserve or decide: the two formulations of the bet make materially different commitments. "An automated machine learning paradigm" that scales with computation is a broad framing claim. "Autonomous double-loop learning with targeted correction where no fixed criterion is adequate" is a narrower and falsifiable capability claim, and the evidence section's two-part test and failure condition match it. The author must choose which one the article commits to, or keep both with an explicit relation, such as the narrow claim as the test of the broad one. That choice should not be settled as a compression edit. Keep the RL-style "no built-in guarantee" caveat beside the first-level claim, because the "What counts as learned" section depends on it. One possible resolution is to open with the later bold sentence and move the Bitter Lesson clause to the section about it.

### 2. Give on-balance judgment its own role as the point the precedents lead to

- Location: "Proof, formula, judgment: where the bet enters", the paragraph headed "**On-balance judgment.**". Related occurrences of the concept are the opening gloss "deciding edits without selecting one scalar weighting from the many value functions compatible with the goal" and the definition of "learned" under "What counts as learned".
- Combines: branch-bloat WARN and detail-overhang WARN (the unused sentence "An unknown is worth investigating only if a plausible answer could reverse the choice"), and core-claim-obscured INFO (the compatible-value-function gloss in the opening). The format problem, with the proposal presented as a fourth precedent, is cross-cutting.
- Preserve or decide: keep the on-balance judgment that *admits* a change separate from the verdict that a change was *learned*. Both use "every reasonable measure", but the first is a decision made on present evidence and the second is a retrospective counterfactual comparison with the change taken out. Merging them would erase the article's point that "letting a change stand while its verdict is open is a decision, not a demonstrated gain". Also keep the open-verdict-plus-reversibility clause, because it connects back to the routing-line example. The author must decide whether the paragraph stays in the precedent section with an explicit lead-in or becomes its own subsection placed just before the bet.

### 3. Let the table carry the payoffs and give each risk one home

- Location: "Deliberative learning versus training weights", from "Three payoffs follow directly" through the cost-ledger paragraph. The hazard bullet "*Unfaithful rationales.*" is under "Material limits and failure modes".
- Combines: marginal-value-redundancy WARN (the payoffs paragraph restates the table) and INFO (unfaithful rationales stated twice). The detail-overhang INFO on the "weighs nothing" naming aside comes from the same section, but it is local and does not change this direction.
- Preserve or decide: the payoffs paragraph carries two links, persistent deployment-time adaptation and inspectability as a property of form, plus one extra claim, inspection "by other agents at volumes people could not read". Each must find a new home or be dropped deliberately. The costs paragraph and the hazards list have different scopes. The costs belong to legible stores in general, whatever fills the judge slot. The hazards threaten the LLM-judge bet specifically. Keep that distinction when deciding where faithfulness lives. The closing falsification condition names "unfaithful rationales", so the hazard bullet must stay at least as a named item.
