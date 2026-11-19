# Assessment: Checking retained results trades cost against reliance risk

**Proposed purpose (the operator named none):** An agent or maintainer deciding whether and how often to check a retained derived result in a KB should be able to read the trade-off in one pass. They should see why a stop-authorizing result such as the completeness mark warrants a defined check while a candidate-only result such as a connect report can be reused, and which conditions a mechanical check needs.

## What reads well

The two worked examples, a result that authorizes stopping and a result offered only as candidates, make an abstract trade-off concrete, and every caveat sits beside the claim it limits.

## Sentence a hostile reviewer would attack first

"The absence of a known change is evidence of freshness only if every relevant change reaches the checker." The premise-decomposition report defeats it with a counterexample: if a hook reports most changes but misses some, seeing no reported change is still weak evidence of freshness. The section heading ("does not establish freshness") and its last line state the defensible version. This is a claim question (below), so no pass touches it.

## Ranked changes

1. **Remove the garden path in the opening paragraph** (finding 6, parsing ambiguity). The clause-shaped link text "frontloading spares execution context" acts as the subject of a reduced relative clause, so "argues for results" first reads as the note advocating results. This is the note's first paragraph, so every reader meets it. Cost: one sentence split. Pass: `fix-strategy-taxonomy` on `sentence/parsing-ambiguity`.
2. **Split the overloaded suppression sentence** (finding 4, clause packing). One sentence carries the hidden-error claim, the nested stop-and-suppress mechanism and the identity with the indexes note. Split it at "which is how" and keep every relation. The consumption-channel note quotes "the copy suppresses the search that would have exposed what it misses", so that wording must stay. Cost: one sentence split. Pass: `fix-strategy-taxonomy` on `sentence/clause-packing`.
3. **Correct the stale link text for the recompute note** (finding 5, misleading link text). The link text still shows the target's former title, "inverts the … default". I confirmed the target's H1 is now "LLM recompute cost shifts the store-vs-recompute balance", so the link text promises a stronger claim than the target makes. The annotation should say that the target shifts the balance, not that it makes retention worth keeping by default. Cost: one link line. Pass: `fix-strategy-taxonomy` on `sentence/misleading-link-text`.
4. **Gloss "tag head" and "participating collections" at first mention** (finding 1, undefined terms). The mark section's scope depends on both terms. A short inline gloss helps a reader from outside Commonplace and costs a KB reader nothing. Cost: two short clauses. Pass: `fix-strategy-taxonomy` on `accessibility/undefined-terms`. The INFO item on "the validator" is not acted on.
5. **Cut two of the three redundancies** (finding 3, marginal-value redundancy):
   - the recap sentence in the freshness section ("Even the enforced mark can be stale …");
   - the restated conditionality in the Scope bullet ("The suppression mechanism is conditional."), keeping its prevalence disclaimer.

   Cost: two deletions. Pass: `fix-strategy-taxonomy` on `kb/instructions/compression-bundle/marginal-value-redundancy`, scoped to those two units. The third item stays (see below).

No `readability-and-flow`, `plain-wording`, `abstractions` or `opening-and-title` pass is recommended. The remaining structural proposals are choices I do not rank first, and the title change is a claim question.

## Divergence and support (must keep)

These sentences take a stance a reader could contest, and dependents rely on them. They are divergence and must be kept:

- "Accepting some risk between checks can be right, provided it is an explicit choice rather than a hidden consequence of trusting the copy." ADR 068 and the decisions-bind proposal rely on it.
- "These conditions make a check possible and worth relying on, not free or current." The validation contract relies on it.
- The four numbered mechanical-check conditions, in their order and numbering. ADR 046, the validation contract and the commitment note cite them by number.
- "Testing or centralizing a validator lowers the cost of assurance but does not prove the validator correct." ADR 046 relies on it.
- "This requires that the consumer actually stops and that the suppressed search would find more task-relevant material." This is the stated condition on the suppression mechanism.
- "Assurance dates from the last check."

Support that could be narrowed: "so one production is amortized over many uses" holds only for results that are reused and costly to derive (premise decomposition). Narrowing it is a claim question, not a pass.

## Claim questions for the operator

- **Defect, one-sentence fix: freshness "only if".** Passage: "The absence of a known change is evidence of freshness only if every relevant change reaches the checker." Case: partial change notification still gives weak evidence of freshness. Possible repair: "establishes freshness only if". Reports: `kb/reports/state/review/results/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md/kb/instructions/premise-decomposition-gate.md` (DEFEATED) and `…/kb/instructions/composition-friction-gate.md`. Two dependents rely on this section's point. The repair keeps that point, but the operator should confirm it.
- **Defect, one-sentence fix (stale qualification): condition 3.** Passage: "The mark's contract supplies the first three; nothing in it establishes the fourth." Case: condition 3, a source available at check time, is a runtime fact that no contract can supply. The note itself says the validator reads the inputs "when they are supplied". Possible repair: "The mark's contract supplies the first two and names the inputs that condition 3 needs at check time; …". The validation contract cites conditions 2 and 3 by number, so the repair must keep the numbering. Report: `…/kb/instructions/composition-friction-gate.md`.
- **Choice, no defect shown: the title.** The claim-strength finding (`kb/reports/state/review/results/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md/frontmatter/claim-strength.md`) and the critique's secondary objection call the title near-truism. They propose sharpening it toward the stop-authorizing versus candidate-only contrast. The title reaches all 41 linkers, and four dependents already link under an older, stricter title. A rename is the operator's decision, with the dependents' link text alongside it.
- **Choice, no defect shown: trigger as a separate axis.** The critique (`…/kb/instructions/critique-note.md`, attack partially lands) proposes three changes:
  - restate the thesis as conditional on whether the dependency set can be tracked;
  - add check trigger (on change, on use, periodic) as a separate axis;
  - say whether the mark's between-validation window is a deliberate trade or comes from where the validator is invoked.

  This would change the thesis. I do not rank it first. The note's claim is qualitative and holds where dependency tracking is unsound, and its connect-report example already names dependency tracking as the difficulty. The operator may take it up as a rewrite.
- **Choice, no defect shown: restructuring.** The compression synthesis (`kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/synthesis`) proposes two moves: tie the mechanical-check section to the cost side (move it ahead of the examples, bridge it, or move it out), and lead with the claim, folding the freshness principle into the risk side. Moving the conditions out would break the numbered citations from ADR 046, the validation contract and the commitment note. The suggested bridge also adds a claim ("the connect report fails condition 1") that the note does not state. Both are the operator's decision.
- **Dependents outside this artifact.** The role report (`kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/role`) finds four dependents that link under the former title "A derived copy of recomputable truth must be checked or absent" and rely on a rule the note no longer states: `kb/agent-memory-systems/reviews/swamp.md`, plus the atomic-step-grounding, source-genre and tag-scope archived proposals. The passes edit only this note, so the operator decides whether those links change.

## Findings and proposals not acted on

- **Marginal-value redundancy, first item** ("This lets subsequent reads reuse the checked result."). Not cut. Two dependents rely on the explicit reuse point: the enforced tag-README note and the citation-fidelity note. The sentence costs one line.
- **Undefined terms, INFO item on "the validator".** It is INFO-level, and context resolves it.
- **Parsing ambiguity, INFO item on "it".** It is INFO-level. The fix-strategy worker may take it if it falls inside the rewritten sentence.
- **Claim strength (title).** Treated above as a claim question, not a pass.
- **Composition friction, "inexpensive" unsupported.** This is an extension: it asks for a cost comparison. The premise-decomposition report finds the premise holds (scan plus link lookup).
- **Composition friction, explicit-choice proviso thin; premise decomposition, check time must be visible.** Both are extensions: they ask for grounds or a mechanism behind a condition the note states. The purpose does not ask for that coverage.
- **Composition friction, connect-report reuse against an unbounded risk.** Extension. The note already concedes the risk is not zero.
- **Premise decomposition: amortization condition, immutable inputs, mandatory checks.** These are extensions or scope qualifications. Narrowing the amortization sentence is listed under support above.
- **Critique, verification cheaper than derivation not revisited for the mark.** Extension.
