# Assessment: Removing approval waits can leave required human evaluation in place

**Proposed purpose (operator named none):** A builder of an agent-operated KB who removes an approval wait should be able to tell which human evaluation tasks their process still depends on, so that they do not claim the wider process is "fully automated" when only adoption is.

**Decision: stop. No passes are planned.** The depth 1 critique proposes changing the note's claim, not its wording. The passes do not change claims, so the text they would polish is likely to be replaced.

## Why the run stops

The critique (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/critique-note.md`, attack outcome "partially lands") proposes changing what the note claims:

1. Split the dependency definition into two named relations: a *blocking* dependency (the process cannot proceed without the person) and an *obligation* dependency (the process runs, but a specified task goes undone). Then say which one the title asserts. As an alternative, it proposes limiting the claim to compliance with stated requirements. Either option changes the note's central definition and the scope of its headline.
2. Rename the file to match the title. The filename `evaluation-that-controls-adoption-helps-determine-the-change` names a causal-credit claim that the body explicitly sets aside ("rather than deciding who deserves causal credit for an improvement").

The other depth 1 reports point the same way. The composition-friction report ranks the definition sentence as the thinnest joint. Its "For the human" item asks the operator to decide whether "required" means "the process specifies it" or "the process cannot work properly without it". The premise-decomposition report finds the criterion under-inclusive: it misses tacit quality dependencies and tacit non-blocking expectations, and it gives an unclear verdict on revision loops fed only by optional studies. It proposes new Scope qualifications. These add claims, which passes may not do. The synthesis proposes restructuring: lead with the weekly-review case or merge the two case sections. It says the author must first choose which framing leads, the title's scope-of-automation framing or the description's required-versus-optional framing. That choice is also a claim decision.

**Role report check:** Only `kb/theory/README.md` links to the note. Its index entry repeats the title and glosses the distinction (automated adoption vs. required human monitoring or revision vs. optional assessment). The proposals do not come from a term that a dependent uses in another sense. However, if the rewrite changes the title or the central distinction, that index entry must change with it (role report run directory: `kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/role`). A file rename also has to be committed alone with `commonplace-relocate-*`.

**Route:** `commonplace-review run rewrite kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md --commission FILE`, with the commission prepared using `cp-skill-write-multistage`. Its decisions: which dependency relation(s) the title asserts; whether quality-only reliance and tacit expectations are excluded in Scope or handled; which framing leads; the filename.

## Ranked changes (for the rewrite commission, not for passes)

1. **Separate blocking from obligation dependency, and state which one the headline uses.** Cost: claim rewrite of the definition paragraph, the "Name the process" section, the title and the description. Route: rewrite. Highest value: it removes the "true by stipulation" objection, which is the attack most likely to make a builder discount the note.
2. **Give the weekly-review case an operational consequence, or mark it as showing only the obligation case.** Example consequence: harmful changes accumulate with no rollback. Cost: one paragraph. Route: rewrite, because it changes what the example shows.
3. **Bring the "does not establish that each specified task is useful or adequate" concession into the opening, and add what a builder does differently.** The builder action is to declare which required tasks a "fully automated" claim covers. Cost: two sentences. Route: rewrite (it adds a claim).
4. **Put the case that exemplifies the title first, or merge the case sections into one contrast set.** Cost: structural reorder. Route: rewrite, or readability-and-flow after the framing is decided.
5. **Draw the line between using findings and depending on assessment for a revision loop whose only input is study findings.** Cost: one or two sentences. Route: rewrite (it changes the claim's boundary).
6. **Rename the file to match the title.** Cost: a relocation commit, plus the README link. Route: `commonplace-relocate-*`, committed alone.
7. Add a Relevant Notes footer for the two inline links. Cost: small. Route: a separate operator edit, not a pass.

**Sentence a hostile reviewer attacks first:** "Human evaluation remains a dependency when omitting it either prevents that process from proceeding in practice or leaves an evaluation task specified by those requirements undone." Its second disjunct makes the headline true by definition.

**What reads well:** The required-approval versus optional-assessment pair shows clearly that the same examining activity can be a blocking dependency or an optional study, and the "always approves" point holds up under every review.

## Candidate overclaims: support or divergence

- "The process depends on human intervention even if the maintainer always approves." **Divergence: keep.** It blocks the "always approves, so dispensable" inference, and all reviews say it holds.
- "Execution continuing without a person establishes only the absence of a blocking step." **Divergence: keep.** The note's distinctive inference limit; it holds in two reviews.
- "Removing the wait automates adoption, not necessarily the wider process." **Divergence: keep.** It is the headline claim in its safe "not necessarily" form.
- "Using an optional study's available findings does not itself require future studies." **Support: may be narrowed.** Two reports show that it conflicts with the first disjunct when studies are revision's sole input.
- "It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement." **Support: may be narrowed.** "To remove" presumes that the wait does no evaluation work, which pulls against the routine-approvals link.

## Stale qualifications (claim questions for the operator)

- The filename names a causal-credit claim ("helps determine the change") that the body disclaims. This is a stale identifier, not a pass item.
- The description says monitoring or revision "still requires a person". Under the note's own definition, that holds only in the obligation sense unless a blocking case is shown. It repeats the definitional equivocation at the retrieval surface.

## Findings not acted on

- All depth 1 findings: not acted on by passes, because the run stops for the claim-level proposal above. They feed the rewrite commission instead.
- Synthesis sentence-level folds (two closing caveats, the "Execution continuing…" sentence, the claim-scoping sentence): the synthesis itself put them below threshold, and the text may be rewritten.
- Role report: it reports no untaken recommendations and no duplication, so there is nothing to act on beyond the README reach noted above.
- No stored `warn`/`fail` results and no earlier decisions were supplied.
