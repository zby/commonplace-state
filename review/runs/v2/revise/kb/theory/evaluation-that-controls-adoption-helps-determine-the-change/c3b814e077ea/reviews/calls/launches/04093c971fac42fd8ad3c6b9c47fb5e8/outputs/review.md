---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Human evaluation remains a dependency when omitting it either prevents that process from proceeding in practice or leaves an evaluation task specified by those requirements undone."
    reason: "DOUBTFUL — (stated without modality, so read as the correct boundary for 'dependency') human evaluation is a dependency exactly when omitting it blocks the process in practice or leaves a requirement-specified evaluation task undone — under-inclusion: a process whose output quality silently relies on unrequired human review (e.g. a maintainer who informally catches harmful instructions; without them, adoption and revision keep proceeding but harmful changes accumulate) is sorted as having no human dependency, because degradation neither blocks progress nor leaves a written task undone. The note relativizes deliberately ('relative to the process being automated and its stated requirements') and its Scope excludes mere influence, so the cut is coherent, but a reader asking whether the human is dispensable gets 'not a dependency' for a case where removing the person changes outcomes. A qualification in Scope that the criterion tracks operating and specified dependencies, not quality dependencies, would close it — LOCAL — instance"
  - scope: passage
    quotes:
      - "Using an optional study's available findings does not itself require future studies."
    reason: "DOUBTFUL — (universal) consuming an optional study's findings does not by itself make future studies required — a revision loop whose only trigger or input is study findings stops proceeding when studies stop, so by the note's own first criterion ('prevents that process from proceeding in practice') the studies become a practical dependency of revision without any requirement being written. The word 'itself' saves the premise only if 'using findings' excludes making them the sole revision input; the note does not draw that line — LOCAL — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — (unstated, universal) the process's requirements are explicit enough to determine which evaluation tasks are 'specified', so the second dependency criterion can be applied — in agent-operated systems many expectations of human review are tacit and non-blocking ('someone should look at these occasionally'); the Scope bullet handles tacit blocking waits but not tacit non-blocking expectations, which the criterion can neither count as specified nor dismiss. The commitment survives for systems with written operating requirements; it needs a condition that the requirements be stated, or guidance for tacit ones — LOCAL — instance"
  - scope: passage
    quotes:
      - "Removing the wait automates adoption, not necessarily the wider process."
    reason: "HOLDS — (universal for the 'not necessarily' form) adoption and monitoring/revision are separable stages, so automating the gate on one does not automate the others — hunted for a process where removing the approval wait necessarily removes every other human task; continuous deployment with a mandated on-call review and rollback duty is an ordinary counter-case to that, confirming the premise."
  - scope: passage
    quotes:
      - "Execution continuing without a person establishes only the absence of a blocking step."
    reason: "HOLDS — observed unattended execution shows only that no step waits for a person — hunted for a case where continued execution also shows no required task is undone; it cannot, since an undone monitoring duty does not halt execution (the note's weekly sample review case), so the inference limit holds."
  - scope: passage
    quotes:
      - "What matters is whether the operating process depends on the human activity, not whether the activity is called evaluation."
    reason: "HOLDS — the role of a human activity is fixed by the process's dependence on it, not by the activity's type — hunted for an activity whose kind alone settles dependence; identical result-examination performs a gating role in one configuration and an optional study in another, as the two cases show, and the non-binding-but-awaited recommendation confirms that labels do not decide it."
  - scope: passage
    quotes:
      - "The process depends on human intervention even if the maintainer always approves."
    reason: "HOLDS — a required approval stop is a dependency regardless of its approval rate — hunted for a case where a never-rejecting approval is not a dependency; omitting it still halts adoption, so under the note's blocking criterion it remains one. Whether the stop is needed is a separate question the note routes to its linked note."
outcome: report
---

# Premise decomposition: Removing approval waits can leave required human evaluation in place

**Register:** claim
**Central commitment (one sentence):** Removing approval waits automates adoption but can leave human evaluation required for monitoring or revision, where "required" means that omitting it blocks the process in practice or leaves a task specified by the process's stated requirements undone.

## Premises and counterexamples

The title claim is existential ("can"), and the weekly sample-review example witnesses it directly, so the claim does not fail globally. The load-bearing content is the distinction the note uses to sort cases. That distinction rests on four premises: adoption is separable from monitoring and revision; unattended execution shows only that nothing blocks; the activity's role, not its type, settles dependence; and a two-part dependency criterion (practical blocking or a specified task) is the right boundary. The two cases and the subsequent-revision paragraph apply that criterion, and they assume that requirements are explicit enough to apply it.

The separability, inference-limit and role premises survive active hunts. The pressure falls on the criterion and its application. It under-includes tacit quality dependencies, has no clear treatment for tacit non-blocking expectations, and gives an unclear verdict on optional studies whose findings are the revision loop's only input. Each dent is repairable by a qualification in `## Scope`. None forces the commitment to be weakened.

## For the human

Look first at the dependency criterion: say in Scope whether "dependency" deliberately excludes quality-only reliance on unrequired human review, and how tacit, non-blocking expectations are treated.
