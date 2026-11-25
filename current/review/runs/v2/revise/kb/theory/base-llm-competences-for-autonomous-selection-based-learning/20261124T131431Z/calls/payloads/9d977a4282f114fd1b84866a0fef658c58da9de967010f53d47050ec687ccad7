# Assessment: base-llm-competences-for-autonomous-selection-based-learning

**Proposed purpose (operator named none):** For agents and maintainers designing a fixed-weight selection-based learning loop: see which loop functions harness code can take over, which three semantic competences the frozen base LLM must still supply, and that this split is a revisable working hypothesis.

**Outcome: stop before any pass.** The highest-value changes are claim corrections, not text passes. The one dependent's relied-on idea, the "base-model floor", needs one of them. Details are under "Why this run stops".

## What reads well

The three competences are distinct and concrete. Each has a one-sentence job description and a link to the note that develops it. The harness-side list is grouped into three plainly named jobs.

## Sentence a hostile reviewer attacks first

"A bounded empirical illustration of a base-model floor appears in [Harness Evolution Hits a Ceiling] …, where the three weakest tested models produced no held-out gains under the same harness-evolution loop that improved stronger models."

According to the linked ingest, a frontier proposer (Kimi K3) did the diagnosing and proposing, and fixed judge thresholds did the accepting. The weak models were only task executors. The cited floor is therefore an executor's object-level capability floor. It is not a floor in any of the three loop competences the note names. The ingest also retains no quotes, so the use cannot be checked against source text (grounding-alignment `fail`). The next target is "three irreducible semantic competences remain on the frozen base LLM": both "irreducible" and "on the frozen base LLM" go beyond the grounding note, which allows semantic work to move to another processor.

## Ranked changes (highest value against the purpose first)

1. **Recast or drop the Harness Evolution illustration** (2 sentences plus the footer `evidenced-by` phrase). Say whether it shows an executor floor, and whether that floor is in scope, or drop it as support. Retain grounding quotes if the paragraph stays. *Cost:* a claim decision that also touches the dependent article. *Route:* claim correction (no pass owns it); then `cp-skill-ground` for quotes.
2. **Resolve "irreducible" and state why the remainder sits on the base LLM.** Choose "not offloadable in principle" or "not yet shown offloadable". Add the boundary condition, for example a single frozen model as the only semantic processor inside the autonomous boundary. *Cost:* one clause plus one word. *Route:* claim correction.
3. **Hedge or make testable "These three competences can fail independently and sit at different capability thresholds."** Name the dissociation that would support it and the single-factor outcome that would collapse it, or mark it as a conjecture. *Cost:* one sentence. *Route:* claim correction.
4. **Bound the criterion-revision reduction.** Competence 3 judges "against stated commitments", so it covers revision only in the KB's double-loop sense, where the declared objective stays fixed. Consolidation without a triggering failure may need competence 2 widened. *Cost:* one or two sentences. *Route:* claim correction.
5. **Place relevance selection explicitly.** "Routing and loading the relevant artifacts" sits on the harness side, but in open-ended work deciding relevance depends on meaning. *Cost:* one clause. *Route:* claim correction.
6. **Fold the bridge sentence after the harness bullets** (marginal-value finding 2; synthesis opportunity 1; anthropomorphic "in its head"). *Cost:* one sentence. *Pass:* readability-and-flow. This is deferred: the tool-building clause has its own THIN joint, because it assumes competence 2, and the claim decisions above may reshape it.
7. **Cut the defensive "not an established impossibility result" from Scope and keep the revision rule** (marginal-value finding 1; COLLECTION finding 1). *Cost:* one clause. *Pass:* readability-and-flow. This is deferred: it depends on how item 2 resolves "irreducible".
8. **Gloss "selection-based learning" and "scheduler–LLM separation" in the opening, and reframe the diagnostic-richness link as an evidence property** (undefined-terms; misleading-link-text). *Cost:* two glosses and one link reframe. *Pass:* opening-and-title, or fix-level edits. This is deferred: the scheduler gloss bears on the stretched-scope warning in item 5.
9. **Sharpen the description to name the three competences** (description-discrimination). *Cost:* one line. This is deferred until the claim strength settles.

## Overclaims: support or divergence

- "harness code can take over much of the loop's machinery": **divergence**, keep. This is half the thesis, and the dependent relies on it.
- "three … semantic competences remain on the frozen base LLM" (the three named competences): **divergence**, keep. The dependent restates them by name.
- "irreducible": **support**, may be narrowed.
- "Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning.": **divergence**, keep. The dependent relies on necessary-not-sufficient. The undefined "clearing" threshold is a claim question.
- "store-level maintenance and criterion revision do not require a separate model competence": **divergence**, keep. It may gain a boundary condition.
- "These three competences can fail independently and sit at different capability thresholds.": **support**, may be hedged.
- "an inadequate base model can block outer-loop learning before the store itself saturates": **support**, may be narrowed or dropped.

## Stale qualifications

- The Scope bullet qualifies the split as "not an established impossibility result" and lets sub-tasks leave the LLM column. The body still says "irreducible". The qualification and the body word disagree.
- The footer's `evidenced-by` phrase reports the Harness Evolution result without saying whether it corroborates or only bounds the claim. The body calls it an "illustration" (COLLECTION, info).
- The inline diagnostic-richness link labels competence 2 with a term that its target defines as the evidence surface, which is separate from proposer capability. The footer states the relation correctly.

## Claim questions for the operator

1. **Harness Evolution illustration (defect, two readings).** Passage: the illustration paragraph and its footer entry. Reading A: "base-model floor" means the loop-operating model's competences, and the evidence would then misdescribe the source. Reading B: it means the executor's task capability, which lies outside the three competences. A reader concludes differently about what the floor consists of under each reading. Reports: `kb/workflow-state/data/current/review/results/kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md/kb/instructions/critique-note.md` and `kb/workflow-state/data/current/review/results/kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md/kb/instructions/premise-decomposition-gate.md`. This is coupled to the grounding-alignment `fail` (no retained quotes).
2. **"irreducible … remain on the frozen base LLM" (defect, two statements).** "irreducible" cannot hold alongside the Scope rule that offloadable sub-tasks leave the LLM column, unless it is read as provisional. "Remain on the frozen base LLM" also exceeds the grounding note, which allows another processor. A one-clause boundary condition and one word fix it. Reports: critique-note, composition-friction-gate, premise-decomposition-gate.
3. **Independence claim (defect: unmarked status).** It is stated as established, and its only example is hypothetical. Reports: critique-note, composition-friction-gate; finding `semantic/epistemic-status-blur`.
4. **Criterion-revision reduction (defect, case).** Revising a criterion changes the commitments that competence 3 judges against. Consolidation without a failure does not match competence 2 as worded. Reports: critique-note, composition-friction-gate, premise-decomposition-gate.
5. **Relevance routing on the harness side (defect, case).** In novel cases a relevance decision depends on meaning, yet neither column names it. Findings: `semantic/completeness-boundary-cases`, `semantic/grounding-alignment` (warn on the scheduler note's stretched scope).
6. **"Clearing" threshold (defect, two readings).** Reading A, non-zero ability, makes the necessity claim nearly trivial. Reading B, reliability at the rate of novel failures, makes it substantive. Finding: `semantic/underspecified-assertions`.
7. **Move the bootstrap method to the open question (choice, no defect shown).** Synthesis opportunity 3. It is not ranked first.
8. **Title strength (choice).** The COLLECTION review says "may offload much of" is weaker than the note's commitment. Changing the title is outside `repair-claim-title`, because the body's own strength is unsettled.

## Findings not acted on, with reasons

- `accessibility/undefined-terms` (selection-based learning, scheduler–LLM separation, transfer tests, outer-loop learning): deferred. "Transfer tests" and "outer-loop learning" sit in passages with open claim questions 3 and 1, and the scheduler gloss depends on question 5.
- `accessibility/unidentified-references`: deferred. It is the paragraph of question 1, and identifying the paper is moot if the paragraph is dropped.
- `frontmatter/description-discrimination`: deferred until claim strength settles.
- `compression-bundle/marginal-value-redundancy`: deferred (items 6 and 7 above).
- `kb/theory/COLLECTION`: its findings are claim questions 2 and 8 and the stale footer phrase.
- `prose/anthropomorphic-framing` ("in its head"): deferred. It sits in the bridge sentence that item 6 would fold.
- `semantic/completeness-boundary-cases`: claim question 5. The prioritization info item is an extension; the claim as scoped stands without it.
- `semantic/epistemic-status-blur`: claim question 3.
- `semantic/grounding-alignment` (fail): coupled to claim question 1. Retaining quotes for a use that may be dropped is premature.
- `semantic/underspecified-assertions`: claim question 6.
- `sentence/clause-packing`: deferred. The sentence is the criterion-revision reduction (question 4).
- `sentence/misleading-link-text`: deferred (item 8). It is a wording fix, but it falls inside competence 2, whose wording question 4 may widen.
- Extensions not recommended: exploration and task selection as a further competence (premise decomposition); role splitting across several models (premise decomposition; partly absorbed into question 2's boundary condition); the enforcement-components-within-noise point (critique, secondary).
- Choices not ranked first: question 7 (bootstrap relocation) and question 8 (title).

## Why this run stops

Two grounds apply together:

- **A dependent relies on the claim being changed.** The highest-value change is question 1, the recast or removal of the Harness Evolution illustration. The role report shows that `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` relies on the note's "base-model floor" and leans on this illustration for its below-floor sentence. Recasting it as an executor floor, or dropping it, changes what that article's "competence floor" rests on. The operator must decide the article's change too.
- **Too little text would survive.** Questions 2 to 6 sit in almost every paragraph: the harness list, the competence sentence, the reduction paragraph, the independence paragraph, the evidence paragraph and Scope. Passes scoped away from them would touch only text that the claim corrections are likely to rewrite.
