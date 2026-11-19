# Assessment: Removing approval waits can leave required human evaluation in place

**Proposed purpose (the operator named none):** Agents and maintainers deciding whether to remove a human approval wait from a KB procedure should be able to tell whether the change only removes a wait or also automates or retires a required evaluation task, and should report which.

No write brief was supplied, so the plan's `must-keep` lists the divergence items below in full.

## What reads well

The two paired cases (required approval, optional assessment) make the three-way split concrete. The definitional paragraph turns them into a test the reader can apply.

## Sentence a hostile reviewer attacks first

"Calling the whole process automated would conceal an omitted task." All three depth 1 reports converge on it or its premise. It holds only if the process specification is still in force after the wait that enforced it is gone. The note never states that condition.

## Ranked changes

1. **Cut the third statement of the necessity caveat.** Cost: one sentence. Pass: `fix-strategy-taxonomy` for the marginal-value-redundancy finding (depth 4). The sentence "This example establishes a gap against the specification, not that skipping review causes harm." repeats a disclaimer the lead and the definition paragraph already make. The compression synthesis reaches the same conclusion. Removing it puts the reader's attention on the wait/requirement distinction, which is what the purpose needs. The cut changes no claim, and the paragraph's point still ends at the omitted task. The adjacent sentence has an open claim question (below). The fix must change only the cut sentence and leave "Calling the whole process automated would conceal an omitted task." untouched.

No other pass is recommended. The note is compact. Branch-bloat and core-claim-obscured found nothing. Its terms are ordinary words, so `abstractions` and `plain-wording` have nothing clear to do. The title is a claim that the body supports, so `opening-and-title` has nothing clear to do either. The remaining issues are claim questions, which the passes cannot fix.

## Overclaims: support or divergence

- "A claim of full automation must say which tasks it preserves and which requirements it retires." **Divergence**: this is the note's normative contribution. Keep it. Whether to scope it to wider-process claims is a claim question below.
- "Whether a specified task is useful or necessary is a separate question." **Divergence**: the synthesis leaves open whether this belongs among the headline commitments. Keep it in the lead unless the operator decides otherwise.
- "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." **Divergence**: a separate point from the necessity caveat. The synthesis says to keep it.
- "Calling the whole process automated would conceal an omitted task." **Support**: it may be narrowed. It has an open claim question, so no pass touches it.

## Stale qualifications

None found. The Scope bullets qualify terms the body still uses, and the link to the factory-claim note matches its use.

## Claim questions for the operator

1. **The authority of the process specification after enforcement is gone** (defect that one or two sentences would correct). Passages: the lead's "Adoption may proceed without a person while the process specification still assigns monitoring or later revision decisions to one." and the weekly-review example's "Calling the whole process automated would conceal an omitted task." Case: a specification still assigns a weekly review that nobody has done for a year and nobody treats as binding. Then automating adoption conceals nothing, but the note's test reports an omitted task. Under the note's wording, "required" can be read either as "the written text assigns it" or as "the process owner still holds someone accountable for it", and the two readings classify that case differently. Proposed fix: one sentence stating the condition, for example that the specification is the one currently endorsed, or that a person is still accountable for the task. Optionally, add that the reporting duty holds on either reading: a live requirement is an undone task, and a lapsed one must be reported as retired. Reports: `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/critique-note.md`, `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/premise-decomposition-gate.md`, `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/composition-friction-gate.md`.
2. **Different evidence standards for waits and requirements** (defect that one or two sentences would correct). Passage: the second Scope bullet, "A habitual wait for human input can block automation even without a written rule. It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement." The note recognizes waits from practice and requirements only from text, and gives no reason. Case: a maintainer usually samples changes on Fridays, with no written rule. The note's test cannot say whether skipping that review leaves an unfulfilled requirement or skips optional assessment. "To remove" also adds a normative conclusion the definitions do not supply. Proposed fix: either give the reason (a requirement is a normative commitment, not a behaviour) or say how unwritten requirements are identified. Alternatively, limit the note to processes with an explicit specification. Reports: same three as item 1.
3. **Scope of the opening "must"** (defect that one sentence would correct, borderline choice). Passage: "A claim of full automation must say which tasks it preserves and which requirements it retires." against the later "A claim about automated adoption alone need not include monitoring or revision." If "full automation" is read as automation of adoption, the two statements conflict. If it is read as the wider process, they are consistent. Proposed fix: say in the lead that the duty applies to claims about the wider process. Reports: `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/composition-friction-gate.md`, `kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/premise-decomposition-gate.md`.

None of these needs a rewrite or restructuring. Each is a sentence-level claim edit, so the run does not stop. The role report shows no dependents, so these changes reach no linking file.

## Findings not acted on

- marginal-value-redundancy INFO, "This distinguishes human work within the process from optional assessment of its results…": INFO level only. The clause marks the boundary with the linked factory-claim note, and the reviewer is unsure whether it should go.
- Synthesis: folding the lead's necessity caveat into the definition paragraph. This is a choice the synthesis leaves to the author. The lead's version is kept (must-keep). Only the post-example sentence is cut.
- Synthesis: the anticipatory list of fates in the Required approval case, and the restating clause before the factory-claim link. Below the synthesis's own threshold.
- Critique: no comparison with human-in-the-loop versus human-on-the-loop (supervisory control). Extension: the claim stands without it, and the purpose does not ask for related work.
- Critique: mixed cases enforced by a deadline or an escalation. Extension: further cases the purpose does not ask for.
- Premise decomposition: domains where "fully automated" has a conventional scope. This is absorbed into claim question 3 and not acted on separately.
