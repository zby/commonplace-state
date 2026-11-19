# Assessment: A better-factory claim compares operative states under an antecedent assessment relation

**Proposed purpose (no operator purpose was given):** Agents and maintainers who design or evaluate self-revising factories should be able to tell, on one read, what an auditable improvement claim compares and which requirements must be fixed before development, without working through caveats the note repeats.

**What reads well:** The predecessor / candidate / operative-successor terms and the three hypothetical cases (retention without improvement, improvement without learning, learning) separate this claim from its neighbours concretely and precisely.

**Sentence a hostile reviewer would attack first:** "Prior declaration prevents that form of post-hoc selection." Selection survives a prior declaration in at least three ways. The assessor can choose the successor's measurement boundary after development. The assessor can make several declarations and report only the one that passes. And an assessor who declares after a candidate has been staged already knows the result (report-2 and report-1).

## Ranked changes

1. **State each boundary once, and lead with the two-component relation.** The note says four times that a declared comparison need not track real quality: in the opening, at the end of the relation section, and in Scope bullets 1 and 2. It separates adoption control from the comparison three times: in the relata section, the improvement section and Scope bullet 5. It repeats the non-regression scope in its own paragraph, and the preserved-path condition again in the last Scope bullet. The opening names the claim's slots without filling them. Planned change: put "non-regression on the predecessor's prior capabilities, with thresholds for permitted degradation, plus a declared gain on a named dimension" into the opening. Fold the threshold gloss into the two-component sentence and drop the separate paragraph. Keep one quality-tracking caveat and one adoption-versus-judgment statement. Cut the trailing preserved-path sentence and the opaque "a description cannot change…" clause. Keep the Scope bullets that add new limits: the retrospective criterion, the retirement-permitting relation, and the generalization's first sentence. *Cost:* one structural pass over the opening, the relation section and Scope. *Pass:* `readability-and-flow` (it answers finding-3 and finding-4 and the synthesis, report-4, items 1 and 2).
2. **Cut the learning-evidence branch to one clause.** The paragraph "The third case requires evidence of that contribution…" explains how to establish learning, which is a different claim. Keep one clause saying that a passed comparison does not identify the experience link, and keep the link to the experiment note. That link has a `grounds` entry in Relevant Notes, and code checks that link targets survive. Keep the three cases and the closing rule. *Cost:* one paragraph, in the same pass as item 1. *Pass:* `readability-and-flow` (finding-3, report-4 item 3).
3. **Gloss the entry terms.** Add a short appositive for "software factory" at its first mention. Explain "open production family" as the unbounded range of production tasks the factory may face, wherever the surviving quality caveat uses it. *Cost:* two short glosses. *Pass:* `fix-strategy-taxonomy` on finding-1.
4. **Fix the opening's attachment ambiguity.** "a retained change to its reusable machinery that later work depends on" reads as though later work depends on the machinery. The intended condition is that later work depends on the change. *Cost:* a reorder within one clause. *Pass:* `fix-strategy-taxonomy` on finding-8, at depth 5. If item 1 rewrites the opening, the pass checks the new wording or ends `no-change`.
5. **Split the 48-word deployed-system sentence.** Make the fixed-weights consequence its own sentence. *Cost:* one sentence. *Pass:* `fix-strategy-taxonomy` on finding-7.
6. **Replace "audit-proof".** The idiom can be read as "immune to audit". Use "auditable" or "antecedently declared, auditable". This matches the opening's wording and does not change the claim. *Cost:* one word. *Pass:* `fix-strategy-taxonomy` on finding-5.

## Overclaim candidates (support or divergence)

- "Prior declaration prevents that form of post-hoc selection." **Support**: it may be narrowed. The narrowing is open as a claim question (below), so no pass touches it.
- "a retained change can degrade the factory as easily as improve it" (report-3). **Support**: "can degrade the factory" is enough for the argument. This is left as a claim question, because it changes a stated comparison.
- **Divergence (must keep):**
  - A discarded candidate never enters the comparison.
  - Antecedence guards auditability and is not constitutive of improvement. The factory-learning note relies on this, per report-5.
  - An independently supplied retrospective criterion can ground a legitimate improvement claim.
  - The two-component relation is the shape this framework declares, not the only declarable one.
  - A comparison judges the adopted states; whether an evaluator controlled adoption is a separate causal question. The removing-approval-waits note relies on this.
  - Non-regression preserves a factory-development path only when that path is in the checked scope. The closing-path note relies on this.
  - Holding model weights fixed does not put the comparison out of reach.

## Stale qualifications

- The description says "the predecessor's **declared** prior capabilities", but the body says "prior capabilities". Report-3 shows that the two readings differ: all capabilities, including latent ones, versus only the listed ones.
- The Relevant Notes entry for the self-improvement note says this note *applies* "the indexed and antecedent conditions". The body says it **adds** prior declaration to independent specifiability, so "applies" misstates what is inherited.
- The `> TODO!` line about "software house" sits in the body. The rename would reach the tag head, the factory-learning note and the closing-path note (report-5). It is a terminology decision for the operator, not a pass.

## Claim questions for the operator

1. **Title scope (defect, corrected by one word).** The H1 says that every better-factory claim compares states under an antecedent relation. Scope bullet 3 says that a retrospective criterion can ground a legitimate improvement claim. Read literally, both cannot hold. Proposed title: "An auditable better-factory claim compares operative states under an antecedent assessment relation". This also changes the file name, and the tag head and the factory-learning note cite this note. Sources: finding-2 (`kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/frontmatter/title-body-alignment.md`), report-2, report-3. Passes are scoped away from the H1.
2. **"Antecedent" names two conditions (defect: two readings).** The linked self-improvement note uses *antecedent* for a constitutive condition. This note uses it for temporal prior declaration and says antecedence "is not constitutive of improvement". Under one reading, the note denies its grounding note. Under the other, it adds a distinct condition under the same name. Correction: use "prior declaration" in the Scope bullet and fix the footer's "applies". The title and the heading use the term too, and the factory-learning note relies on the Scope bullet. Source: finding-6 (`…/semantic/conceptual-role-conflation.md`), report-5 run directory `kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/role`. Passes are scoped away from that bullet and from the footer entry.
3. **Selection survives prior declaration (defect, corrected by one or two sentences).** The cases are listed in this question's opening and come from report-2 (`kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/kb/instructions/critique-note.md`) and report-1 (`…/kb/instructions/composition-friction-gate.md`). Possible corrections:
   - Narrow "Prior declaration prevents that form of post-hoc selection" to selection within one declaration, or require that every declared comparison be reported.
   - Require the measurement boundary, or the rule that selects it, to be part of the declaration.
   - Specify whether "declared while only the predecessor exists" excludes staged candidate results.

   Passes are scoped away from these three sentences.
4. **Baseline timing (extension or defect, unclear; treated as a choice, no defect shown).** The predecessor is "current when the comparison is declared". An assessor who chooses when to declare therefore chooses the baseline (report-2). The fix could be a clause in the predecessor definition or in the first Open Question.
5. **Retention symmetry (choice, no defect shown).** Weaken "as easily as improve it" to "can degrade" (report-3).
6. **"Prior capabilities" versus "declared prior capabilities"** (the stale qualification above). The operator should say which reading the framework takes (report-3).
7. **The software-house TODO.** The operator should decide whether the rename happens. If it does, apply it as its own commit, together with its dependents.

## Findings and proposals not acted on

- finding-2 (title-body alignment): routed to claim question 1. A title change is not a pass.
- finding-6 (conceptual-role conflation): routed to claim question 2. The fix changes a term a dependent relies on.
- Report-3's points on the whole production environment and on comparable predecessor measurement (environment drift): **extensions**. The first Open Question already names baseline and comparable conditions, and the purpose does not ask for that coverage.
- Report-1's point that the prior-capabilities scope is "thin": an **extension**. The second Open Question already concedes checkability.
- Report-1's point that "therefore … different relata" is thin: an **extension**. The relata section argues the point. This is not recommended, because item 1 may restructure the opening anyway.
- Report-5's note that the removing-approval-waits dependent reads the adoption bullet in an "operate" sense: this concerns the dependent's wording, not this artifact. The adoption-versus-judgment statement is kept.
- `plain-wording`, `abstractions` and `opening-and-title` are not recommended. Apart from the findings planned above, no wording or term problem has clear value, and the title change is a claim question.
