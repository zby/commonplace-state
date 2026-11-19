---
description: "Distinguishes human evaluation needed for a system to proceed from assessment that only measures its results; the distinction identifies human stops that automation must address"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# Evaluation required for adoption is part of the operating process

Human evaluation that a system must wait for before adopting a change is part of its operating process. Human assessment that only measures an already-adopted change need not be. The difference matters for automation: the first requires a person for the process to proceed; the second can observe a process that runs without one.

This distinguishes an operating dependency from an assessment of results, rather than deciding who deserves causal credit for an improvement. It complements [the comparison of a system before and after an adopted change](./a-better-factory-claim-compares-operative-states.md): a judgment that the system improved does not by itself show whether human evaluation was required to operate it.

## The same activity can perform different roles

Consider two hypothetical cases involving a new KB instruction.

**Required approval.** An agent proposes the instruction, a maintainer examines test results, and the agent adopts it only after approval. The process depends on human intervention even if the maintainer always approves. Removing that stop requires deciding whether its check can be automated or is unnecessary; [routine approvals do not establish that human judgment is dispensable](./routine-approvals-do-not-show-that-human-judgment-is-dispensable.md).

**Non-blocking assessment.** The agent adopts the instruction under its existing rules. A week later, a maintainer examines the results to assess whether it helped. The process neither waited for that assessment nor relies on it to continue. That assessment creates no human stop in adoption.

Both cases involve examining results and forming a verdict. What matters is whether the operating process depends on the human activity, not whether the activity is called evaluation. A non-binding recommendation still creates a dependency if the agent must wait for it. Conversely, a program can apply human-authored acceptance rules without requiring a new human judgment for each change.

## Name the process being automated

An episode can contain both required approval and later assessment. Describing the whole episode as evaluation obscures which human activities the system needs.

Adoption can also be automated while continued operation depends on human monitoring and rollback. If a maintainer must inspect each adopted instruction and reverse harmful changes, the broader process still requires human work. Moving the check after adoption has not eliminated that dependency. Optional observation is different from monitoring on which the process relies.

## Scope

- The distinction concerns required human intervention, not every human influence. Anticipated assessment can shape proposals without creating a human stop.
- A written approval requirement and actual execution can differ. Bypassing a required check is not evidence that its function has been automated or is unnecessary.
- Removing a stop does not establish that the resulting changes are good. Whether a check is adequate, and whether a change improves the system, remain separate questions.
