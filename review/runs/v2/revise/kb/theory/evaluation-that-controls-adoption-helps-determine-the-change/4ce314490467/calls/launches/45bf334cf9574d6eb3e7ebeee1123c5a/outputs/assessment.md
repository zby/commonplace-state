# Assessment: Removing approval waits can leave required human evaluation in place

**Proposed purpose (the operator named none):** An agent or maintainer about to remove a human approval stop from a KB or agent process should be able to tell, for each human evaluation task, whether the change automates it, retires it or leaves it required but undone, and should report a claim of automation accordingly.

**Decision: stop.** The highest-value change is a correction to the note's classification, not a text pass. The passes do not change claims, so none is recommended now.

## Why the run stops

The note's normative claim asks a full-automation claim to split each human task into "preserved" and "retired". Two sentences carry this as a closed partition, and three depth 1 reports independently show that it is not closed:

1. "Removing that stop requires deciding whether its check can be automated or is unnecessary." The composition-friction report (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/composition-friction-gate.md`) shows a third option: move the check out of the blocking path and keep it as a non-blocking specified task. The note's own weekly-review example is that option. As stated, the sentence is wrong.
2. "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." The premise-decomposition report (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/premise-decomposition-gate.md`) names substitution (the review replaced by metric-triggered rollback) and partial automation (machine triage, human confirms flagged cases). Neither is automation or retirement of the original task. It also names deferred blocking (a review that becomes a wait after a deadline), which breaks the silent premise that "blocking dependency" and "unfulfilled requirement" are disjoint.
3. "Calling the whole process automated would conceal an omitted task." The friction report notes that this needs a stated meaning of "automated" that the note never gives. The critique report (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/critique-note.md`) adds that "required" rests on an unexplained authority of the written specification, and the premise report adds that processes with no written specification (habitual tasks, as distinct from habitual waits) cannot be sorted.

Each repair is local in the reports' judgment, but each one adds or corrects a claim: a third exit route for a check, named substitution and partial-automation cases, a definition of "automated", a ground for "required" and a scope boundary for unspecified processes. Passes cannot make these changes. Text a rewrite will replace is not worth a pass.

Route: `commonplace-review run rewrite kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md --commission FILE`, with the commission prepared with `cp-skill-write-multistage`.

**Dependents.** The role report (`kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/role`) finds one dependent, `kb/theory/README.md`, which cites the title and glosses the three-way distinction. The proposed corrections keep that distinction, so the gloss should survive. A title change or a file relocation (below) would reach the README's link and link text.

## Ranked changes (for the rewrite commission, not for passes now)

1. **Close or open the partition of how a required check leaves the blocking path** (automate, retire, relocate to a non-blocking task, substitute, split). Cost: one to three sentences plus a revised required-approval paragraph. Pass: none; claim change, rewrite route.
2. **State what "automated" means for a whole-process claim and what makes a specified task "required"** (its output feeds a later decision, or an owner would treat its omission as a defect; otherwise it is a stale requirement to retire explicitly). Cost: two sentences. Pass: none; claim change.
3. **Add scope boundaries for deferred or conditional blocking and for processes without a written specification.** Cost: two Scope bullets. Pass: none; claim change.
4. **State the necessity disclaimer once** (opening or Scope) and end the other three passages at their positive point. Cost: three local cuts. Pass: `fix-strategy-taxonomy` on finding-1, or `readability-and-flow`. Deferred until after the rewrite, because the rewrite will touch two of the four passages.
5. **Move or cut the positioning paragraph** (causal-credit clause and the operative-states link) so the definitions lead into the cases. Cost: one paragraph moved. Pass: `readability-and-flow`. Deferred for the same reason.
6. **Replace "Conversely"**, which presents an independent point as an inverse. Cost: one word. Pass: parent-context swap. Deferred.

**Sentence a hostile reviewer would attack first:** "Removing that stop requires deciding whether its check can be automated or is unnecessary." The note's own weekly-review example is a counterexample.

**What reads well:** The paired required-approval and optional-assessment cases show the same activity (examining results and forming a verdict) in two roles, which makes the wait/requirement distinction concrete without argument.

## Candidate overclaims

- "A claim of full automation must say which tasks it preserves and which requirements it retires." **Divergence**: the note's central normative claim; must be kept (its partition may be extended).
- "The process depends on human intervention even if the maintainer always approves." **Divergence**: the structural point the routine-approvals link rests on; held under the premise hunt.
- "Removing that stop requires deciding whether its check can be automated or is unnecessary." **Support**; wrong as stated and must be corrected, not merely narrowed.
- "Calling the whole process automated would conceal an omitted task." **Support**; may be narrowed by stating the meaning of "automated".
- Title, "can leave required human evaluation in place". **Support**; modal and instantiated, but the critique shows "required" claims more than the note defends until the ground for "required" is stated.

## Stale qualifications (claim questions for the operator, not passes)

- **File slug.** `evaluation-that-controls-adoption-helps-determine-the-change` states a different claim (evaluation helps determine the change) from the title, and the body explicitly sets aside causal credit. Proposal: relocate the file to a slug matching the title, as its own `commonplace-relocate-*` commit; this reaches `kb/theory/README.md`.
- **Causal-credit clause.** "rather than deciding who deserves causal credit for an improvement" rules out a reading nothing in the current note invites; it appears to be a remnant of the claim the slug still names. Decide whether to keep it (if readers of the operative-states note bring that question) or cut it.

## Findings not acted on

- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/compression-bundle/marginal-value-redundancy.md` (warn, depth 4): the repeated necessity disclaimer. Valid and of clear value, but not planned now because the run stops for a claim correction that will rewrite two of the four passages it names. Plan it as a `fix-strategy-taxonomy` entry, or fold it into the rewrite commission. Its info-level item (the causal-credit clause) is listed above as a stale qualification.
