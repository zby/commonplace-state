---
type: types/edit-result.md
outcome: changed
changes:
  - "Asymmetry section: rewrote the second paragraph's opening, which restated the first paragraph's bounded-versus-unbounded contrast, as a causal sentence that draws the conclusion."
  - "Where-the-rule-applies section: split the first paragraph so that the description of the managed-staleness machinery and the reason it stops at review are separate paragraphs."
  - "Deduplicated the caveat that lineage need only be machine-followable, not visible to a human: removed it from the regime paragraph and kept it in precondition 2, where the requirement is stated."
  - "Sentence-level edits (5): 'the rule rides entirely on that' became 'The rule rests on an asymmetry between the two failure modes'; 'Enforcement is the third class' became 'Enforcement adds a third class' (enforcement is not itself a class); 'Here' became 'In that class'; 'the regress' became 'the regress of unchecked claims'; the closing 'It is the general form' now names 'The rule' as its subject."
removed-links: []
---

# Report

Structural moves:

- Merged the restatement in the asymmetry section into one causal sentence ("Because one downside is bounded and recoverable and the other is silent and unbounded, …").
- Split the dense managed-staleness paragraph at its argument boundary: what the machinery does, then why it stops at review.
- Deduplicated the machine-followable/human-visibility caveat. The caveat now appears only in precondition 2. The regime paragraph keeps its claim that the interrupt-placement problem dissolves because the validator is the edit-time surface.

Sentence-level edits: 5.

No claims, examples, links or qualifications were removed. The opening already gives the sentence a reader would repeat (exactly two valid states, checked or absent), so nothing was moved there.

Noticed but not applied: the instances section says the four surfaces are "already enforced, stated but unenforced, resolved by omission, and not yet applied". It is unclear which list item each state maps to. For example, the byte-identical `AGENTS.md.template` copies are described without saying whether a check exists. Fixing the mapping would mean choosing between readings, so it was left and is flagged here.
