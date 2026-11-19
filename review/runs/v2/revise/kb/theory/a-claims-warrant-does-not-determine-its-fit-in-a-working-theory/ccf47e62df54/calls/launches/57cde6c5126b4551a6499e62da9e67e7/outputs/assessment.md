# Assessment: A claim's warrant does not determine its fit in a working theory

**Purpose (as given):** Make the note clear and correct for a KB maintainer reading it for the first time.

**Decision: stop.** The highest-value changes against "correct" are claim decisions, not text passes. Two depth 1 reports propose changing the note's central claim: either narrow the symmetric "neither evaluation determines the other" to apparent or operational fit, or restate it as "warrant is necessary but not sufficient for fit". The operator must decide which claim the note makes before any pass is worth its read. No passes are listed.

## What reads well

The second paragraph's concrete list of ways a warranted claim can fit poorly (irrelevance, duplication, wrong abstraction level, maintenance cost without changed inference) settles the title's direction on its own; every report that tested it found that it holds.

## Sentence a hostile reviewer would attack first

"Theory fit is therefore relational: it concerns how warranted claims compose into an operative explanatory structure, not whether each claim passes its independent warrant test in isolation."

This is the note's only positive account of fit. Its "therefore" follows from premises about where a contradiction can be repaired, not about what fit is. It also defines fit over *warranted* claims, which makes warrant a precondition of genuine fit. That contradicts the symmetric claim in Scope ("neither evaluation determines the other") and leaves the fit-does-not-imply-warrant direction resting on the word "apparent". The composition-friction and premise-decomposition reports both rank this first.

## Ranked changes (highest value against the purpose first)

1. **Decide whether an unwarranted claim can have genuine fit, or only apparent fit.** Cost: one claim decision, then one or two sentences in paragraph 4 and the Scope section. This needs an operator decision, not a pass. Under one answer, line 16 drops "warranted" and the symmetric claim stands. Under the other, the central claim becomes "warrant is necessary but not sufficient for fit", and the title and the Scope bullet change with it. Sources: `kb/reports/state/review/results/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md/kb/instructions/premise-decomposition-gate.md` (first finding; it proposes narrowing the symmetric claim to apparent or operational fit) and `kb/reports/state/review/results/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md/kb/instructions/composition-friction-gate.md` (filter and top joint). **This is the proposal that sets `stop`.**
2. **State the rule that separates evidence exchange from substitution.** Cost: one added sentence, but it is a new claim. As written, "silently" is the only boundary. The note can be read as asymmetric: failure in use counts against warrant, success never counts for it. The critique proposes a rule: use counts toward warrant to the degree that the demand could have exposed the claim and was not shaped by assuming it. Adding a rule is a claim change that no pass may make. Sources: finding-4 (`semantic/underspecified-assertions`, depth 2), critique-note report, composition-friction report.
3. **Say what "independent" warrant is independent of.** Cost: one clause, a claim clarification. Without it the separation appears to assume atomist epistemology, and the confirmation-holist objection lands. The critique proposes: independent of the particular purpose-relative working theory under evaluation, not of all background knowledge. Source: critique-note report.
4. **Bound the procedural-claims case.** Cost: one clause, or a scope narrowing. For procedural claims, the only warrant may be "it produced the outcome in this system". That evidence is fit evidence, so the two questions may not separate there. Either limit the commitment to claims whose warrant has a standard external to the system, or say how procedural warrant stays separate. Source: premise-decomposition report, second finding.
5. **Retitle to match the settled claim.** Cost: title and filename change; `opening-and-title` (depth 6) or a fix-strategy entry for finding-1. The H1 states one direction, while the body and Scope state two. The right title depends on change 1, so this waits on that decision. Source: finding-1 (`frontmatter/title-body-alignment`).
6. **Move the contradiction paragraph after the substitution section and tie it to the distinction.** Cost: paragraph reorder plus one bridging sentence; `readability-and-flow`. As written, the repair-option list reads as ordinary confirmation holism. The synthesis also offers moving the repair options to a separate note on contradiction as a revision signal. Sources: synthesis opportunity 1, composition-friction (THIN joint), critique constructive finding 3. This waits on change 1, because the paragraph holds the sentence change 1 rewrites.
7. **Compress the Scope section to its real boundaries.** Cost: two bullet cuts and two folds; `fix-strategy-taxonomy` on finding-2, or `readability-and-flow`. Fold "procedural" into the opening list of warrant kinds. Fold the non-independence point into the first sentence of the inform-not-substitute section. Cut the closing restatement in paragraph 2. This waits on changes 1 and 4: the statistical-independence bullet states the symmetric claim, and the warrant bullet is where the procedural question sits. Sources: finding-2, synthesis opportunity 2.
8. **Remove the "the knowledge base" residue.** Cost: one phrase; `fix-strategy-taxonomy` on finding-3. If change 7 folds the warrant bullet away, the phrase goes with it.

## Overclaim candidates: support or divergence

- "A warranted claim may fit poorly." (and the title's direction): **divergence, defend.** This is the note's contribution, and every report found that it holds.
- "Apparent fit does not imply warrant either.": **divergence, defend.** It holds as stated. The open question in change 1 concerns *genuine* fit, not this sentence.
- "The prohibition is substitution.": **divergence, defend.** This is the operational core. Change 2 would specify its boundary, not narrow it away.
- "Theory fit is therefore relational: it concerns how warranted claims compose…": **support.** It may be narrowed or restated, but only after the change 1 decision.
- "use a scope that does not match the decisions the theory must guide": **support.** The premise-decomposition report shows this item is mis-sorted, because over-application beyond a claim's scope is a warrant failure in use. It may be recast as "a scope narrower than the decisions require" or dropped.
- "Evidence for one question does not settle the other.": **support.** Prediction appears in both the fit and the warrant criteria, so the sentence needs a boundary where the criteria overlap (composition-friction report). It may be narrowed.

## Stale qualifications (claim questions for the operator, not passes)

- The Scope **Warrant** bullet justifies the broad sense by "claims in the knowledge base". The note's frame is any working theory, and the bullet's content already appears in the opening definition apart from "procedural".
- The last Scope bullet restates the claim as symmetric ("neither evaluation determines the other"). That contradicts line 16 and is broader than the title. Resolve it with change 1.
- The Scope bullet on objectives, commitments and grants of authority does not say whether these items have warrant in the note's broad sense or act only on fit (critique, synthesis).
- Relevant Notes omits `kb/theory/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md`, the sibling note that treats the evidence-exchange point the critique raises. The file exists.

## Findings not acted on, with reasons

All four stored findings are deferred by the stop. Each needs to wait for the claim decision:

- finding-1 (`frontmatter/title-body-alignment`, depth 6): the correct title depends on change 1. Retitling now could fix the wrong claim.
- finding-2 (`compression-bundle/marginal-value-redundancy`, depth 4): two of its cuts fall on the Scope bullets that changes 1 and 4 must settle first. The paragraph-2 restatement cut is safe but too small to justify a run on its own.
- finding-3 (`prose/source-residue`, depth 2): this is a one-phrase fix inside the warrant bullet, which change 7 may remove. The INFO item about "the system" is not acted on.
- finding-4 (`semantic/underspecified-assertions`, depth 2): resolving it means adding the exchange rule (change 2). That is a claim addition, not a narrowing or wording change.

## For the operator

Decide two things. First, can an unwarranted claim have genuine fit, or only apparent fit? Second, should the note state an explicit exchange rule, such as the critique's corroboration rule? After that, a replacement plan can run, in order: narrow-overclaims (scope-mismatch item, "Evidence for one question…"), fix-strategy-taxonomy on finding-3, readability-and-flow (move the contradiction paragraph, compress Scope per finding-2), then opening-and-title (finding-1).
