# Assessment: Harness code may offload much of a selection loop, leaving three base LLM competences

## Proposed purpose

The operator named no purpose, so this assessment works under this one: agents and maintainers deciding how to divide an autonomous fixed-weight learning loop between harness code and the model should see which jobs code can take, which three semantic competences stay on the model, and how settled that split and its evidence are.

## What reads well

The note has a clean two-part structure: grouped harness jobs, then three numbered competences, each with a condition and a link to the note that develops it. The one dependent article relies on that structure.

## Sentence a hostile reviewer would attack first

"Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates." It is offered as an illustration of the note's floor. In the cited paper, however, a separate frontier proposer did the diagnosis and proposals. The weak models were only task executors. So the case shows an executor-capability floor, not a floor in the competences the note names (see claim question A).

## Ranked changes

1. **Gloss two load-bearing first mentions.** Give "selection-based learning" a gloss at its first meaningful mention, and say what scheduler–LLM separation separates. Cost: two short clauses. Pass: `fix-strategy-taxonomy` on `accessibility/undefined-terms`, limited to those two items. "Transfer tests" and "outer-loop learning" sit in passages with open claim questions (D and A), so they are excluded.
2. **Remove the restatement around the offload list and the duplicated status label.** Cut the sentence that repeats the three bullets, but keep the point that a code-writing LLM can build further harness tools. This also removes the "in its head" idiom flagged by `prose/anthropomorphic-framing`. Cut the defensive "not an established impossibility result" clause and the third "working hypothesis" label from Scope bullet 1. Keep its revision rule. Cost: two sentences shortened. Pass: `fix-strategy-taxonomy` on `compression-bundle/marginal-value-redundancy`. This covers synthesis opportunity 1 and the first item of the `kb/theory/COLLECTION` finding.
3. **Restate the diagnostic-richness link as a relation.** The inline link reads as the name of competence 2. The link's target defines diagnostic richness as the evidence available to the proposer, which is separate from the proposer's capability. Cost: one parenthetical. Pass: `fix-strategy-taxonomy` on `sentence/misleading-link-text`.
4. **Make the description discriminate.** Name the three competences, or what the harness takes over, so an agent can choose this note over the scheduler–LLM separation and relocation notes. Cost: one frontmatter line. Pass: `fix-strategy-taxonomy` on `frontmatter/description-discrimination`.

Order by depth: 3, 4, 5, 6.

## Overclaim candidates: support or divergence

- "harness code can take over much of the loop's machinery": **support** and may be narrowed, for example to the mechanical part of routing (see claim question F).
- "three irreducible semantic competences remain on the frozen base LLM": **support** in its word "irreducible" and in placing the competences on the frozen base LLM; both may be narrowed (claim question B). **Divergence** in its core: in open-ended work, semantic competences remain that harness code does not supply, and these are the three named ones.
- "These three competences can fail independently and sit at different capability thresholds": **support**; it may be hedged (claim question D).
- "Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning": **divergence**, kept; the dependent article relies on it. Its threshold is claim question E.
- "store-level maintenance and criterion revision do not require a separate model competence": **divergence** in intent; its reduction argument is claim question C.

## Claim questions for the operator

Passes are kept away from each passage below.

- **A. The Harness Evolution paragraph and its footer entry (defect, about two sentences).**
  - **The case.** In the linked ingest (`kb/sources/harness-evolution-ceiling-weight-training.ingest.md`), the proposer that diagnosed failures and proposed edits was a separate frontier model. The weak Qwen/Gemma models were task executors. Their harness gains raised delivery, but the freed trajectories ended in F4, the class for a delivered plan that is poor. The ingest also notes that "too weak" is confounded with the paper's own rule, and that the paper places the ceiling in the loop's evidence package.
  - **Two readings.** In the first, the case is a floor on the loop competences 1–3. In the second, it is a floor on executor or object-level capability. The paragraph supports both, and they lead a reader to different conclusions about what binds.
  - **Reports.** `kb/instructions/critique-note` and `kb/instructions/premise-decomposition-gate` (paths under `kb/workflow-state/data/current/review/results/kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md/kb/instructions/`).
  - **Grounding.** `semantic/grounding-alignment` fails because the ingest retains no quotes. Grounding the claim with `cp-skill-ground` belongs with this question.
  - **Dependent.** The role report marks this sentence PARTLY SUPPLIED for `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`. Recasting it should be checked against the article's "Below that competence floor…" passage.
  - **Deferred findings.** `accessibility/unidentified-references` (naming Tian et al.'s 2026 arXiv preprint) and the "outer-loop learning" item of `accessibility/undefined-terms` wait on this decision.
- **B. "irreducible … on the frozen base LLM" (defect, one or two words or a boundary clause).**
  - **Two readings of "irreducible".** It can mean "cannot be offloaded now" or "cannot be offloaded in principle". The Scope revision rule withdraws the second reading.
  - **Unstated boundary.** The grounding relocation note allows semantic work to move to another processor, such as a human, a second model or a verifier. The note does not state why the work stays on this model, for example because one frozen model is the only semantic processor inside the autonomous boundary.
  - **Reports.** The critique, the composition friction gate, the synthesis and `kb/theory/COLLECTION`.
  - **Dependent.** The dependent article uses this exact phrase as link text at its line 225, so a change of wording needs a matching edit there.
- **C. The criterion-revision reduction (defect or extension; one or two sentences).**
  - **The problem.** Competence 3 judges "against stated commitments", while criterion revision changes those commitments. Competence 2 starts from a failure, but consolidating prose rules need not.
  - **Possible fixes.** Either state the KB's narrower double-loop sense, in which the declared objective stays fixed, or widen competence 2 to cover synthesis without a triggering failure.
  - **Reports.** The critique, the composition friction gate and the premise decomposition gate.
  - **Deferred finding.** The `sentence/clause-packing` finding sits in this sentence and waits on this decision.
- **D. "These three competences can fail independently and sit at different capability thresholds" (defect in epistemic status, one sentence).** The note states this sentence as fact. Its only support is one hypothetical dissociation, and the bootstrap use depends on it. A rival view holds that model capabilities vary mainly along one general factor. Either hedge the sentence as a conjecture or name the dissociation that would test it. Reports: `semantic/epistemic-status-blur` and the critique. The "transfer tests" gloss waits on this decision.
- **E. "Clearing these competences" (two readings, one clause).**
  - **Two readings.** "Clearing" can mean having some ability in each competence, or reliability enough to keep pace with novel failures without human repair.
  - **Scope of necessity.** The premise decomposition shows that necessity holds only where no fixed scorer settles selection.
  - **Reports.** `semantic/underspecified-assertions` and the premise decomposition gate.
  - **Dependent.** The dependent article relies on the necessary-not-sufficient claim. A threshold qualification leaves that claim intact.
- **F. Routing and loading "the relevant artifacts" on the harness side (defect, one phrase).**
  - **The problem.** In open-ended work, judging relevance for a new case depends on meaning, and none of the three competences names it. The scheduler–LLM separation note grounds bookkeeping and defined transitions, not relevance selection.
  - **Fix.** Either limit the bullet to mechanical routing or assign the relevance judgment to a competence.
  - **Reports.** `semantic/completeness-boundary-cases`, the warn item of `semantic/grounding-alignment`, and the premise decomposition gate.
- **Choices, no defect shown.**
  - **Exploration and task selection as a possible fourth competence** (premise decomposition gate). The Scope rule already allows additions, so this is an extension or choice; it is not ranked first.
  - **A per-role floor across several models instead of one base model** (premise decomposition gate). This is a choice that overlaps B; it is not ranked first.

No stop. Each defect above can be corrected by narrowing a phrase or adding a boundary clause. The thesis and the argument's order stand.

## Stale qualifications

- The footer entry for Harness Evolution, "evidenced-by: weak-model lines produced no held-out harness gains under a loop that lifted stronger models", has the same executor-versus-loop ambiguity as the body (A). Per `kb/theory/COLLECTION`, it also does not say whether the evidence corroborates the claim or only bounds it.
- The footer entry for Diagnostic richness ("how the harness's evidence interface interacts with competence 2") is already correct. Only the inline link misleads, and change 3 fixes it.

## Findings not acted on

- `accessibility/unidentified-references`: the paragraph is under claim question A and may be recast.
- `kb/theory/COLLECTION`: item 1 is covered by the marginal-value fix. Item 2 is claim question B. Item 3 is in the footer and belongs with A.
- `prose/anthropomorphic-framing`: the marginal-value fix removes the sentence that contains "in its head". If the fix keeps that clause, apply the literal wording "carry … in its context" in the same entry.
- `semantic/completeness-boundary-cases`: claim question F.
- `semantic/epistemic-status-blur`: claim question D.
- `semantic/grounding-alignment` (fail): claim questions A and F; grounding by `cp-skill-ground`.
- `semantic/underspecified-assertions`: claim question E.
- `sentence/clause-packing`: the sentence is under claim question C.
- `accessibility/undefined-terms`, the "transfer tests" and "outer-loop learning" items: under claim questions D and A. The info items ("diagnostic richness", "criterion revision") are covered by change 3 or sit under C.
- Synthesis opportunity 2 (state the status once): the label cut is covered by change 2. The "irreducible" meaning is claim question B.
- Critique secondary objection (the ablations credit capability-granting components, not enforcement): this is an extension that bears on the offload list. The purpose does not ask for it.
- Composition friction gate, the THIN tool-building joint: the premise decomposition finds that it HOLDS, because tool building falls under competence 2. The marginal-value fix keeps that point, so the matter is left to the operator.
