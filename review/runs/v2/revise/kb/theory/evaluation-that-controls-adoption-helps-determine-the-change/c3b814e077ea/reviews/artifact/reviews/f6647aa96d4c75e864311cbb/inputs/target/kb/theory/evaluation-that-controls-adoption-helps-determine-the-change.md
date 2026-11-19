---
description: "Distinguishes required human evaluation from optional assessment: adoption can run unattended while monitoring or subsequent revision still requires a person"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# Removing approval waits can leave required human evaluation in place

A system that adopts changes without waiting for approval can still require human evaluation to monitor those changes or decide subsequent revisions. Removing the wait automates adoption, not necessarily the wider process. Human assessment that only observes results need not create either dependency.

The distinction is relative to the process being automated and its stated requirements. Human evaluation remains a dependency when omitting it either prevents that process from proceeding in practice or leaves an evaluation task specified by those requirements undone. Execution continuing without a person establishes only the absence of a blocking step.

This distinguishes an operating dependency from an assessment of results, rather than deciding who deserves causal credit for an improvement. It complements [the comparison of a system before and after an adopted change](./a-better-factory-claim-compares-operative-states.md): a judgment that the system improved does not by itself show whether human evaluation was required to operate it.

## The same activity can perform different roles

Consider two hypothetical cases involving a new written procedure for an agent.

**Required approval.** An agent proposes the instruction, a maintainer examines test results, and the agent adopts it only after approval. The process depends on human intervention even if the maintainer always approves. Removing that stop requires deciding whether its check can be automated or is unnecessary; [routine approvals do not establish that human judgment is dispensable](./routine-approvals-do-not-show-that-human-judgment-is-dispensable.md).

**Optional assessment.** The agent adopts the instruction under its existing rules. A week later, a maintainer examines the results to assess whether it helped. This is an optional study: neither adoption nor a required monitoring or revision task depends on it.

Both cases involve examining results and forming a verdict. What matters is whether the operating process depends on the human activity, not whether the activity is called evaluation. A non-binding recommendation still creates a dependency if the agent must wait for it. Conversely, a program can apply human-authored acceptance rules without requiring a new human judgment for each change.

## Name the process being automated

Suppose adoption is automatic, but the operating requirements assign a maintainer a weekly sample review and rollback of harmful changes. Adoption continues if the maintainer does nothing, but the required monitoring task goes undone. The process including that task is not fully automated, even though no individual adoption waits for review.

The same distinction applies to subsequent revisions. If the next revision requires the maintainer's assessment, that assessment is a dependency of the revision process, though not of the earlier adoption. Using an optional study's available findings does not itself require future studies. Making a new human assessment a condition of each revision does.

A claim about automated adoption alone need not include monitoring or revision; a claim about the wider process must account for them. Identifying these dependencies does not establish that each specified task is useful or adequate. Removing an unnecessary requirement may be justified, but it changes the process being automated; simply skipping the task does not fulfill the existing requirement.

## Scope

- The distinction concerns required human intervention, not every human influence. Anticipated assessment can shape proposals without creating a human stop.
- A habitual wait for human input can block automation even without a written rule. It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement.
