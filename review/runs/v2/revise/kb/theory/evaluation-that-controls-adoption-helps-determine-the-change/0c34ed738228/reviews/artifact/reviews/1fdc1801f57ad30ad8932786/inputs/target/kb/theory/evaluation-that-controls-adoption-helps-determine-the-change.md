---
description: "Distinguishes approval that selects a system revision from assessment after adoption; one episode can contain both, but describing it differently cannot remove an evaluator's causal contribution"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# Evaluation that controls adoption helps determine the change

> Supplement to the adoption-versus-measurement distinction in [the better-factory comparison](./a-better-factory-claim-compares-operative-states.md).

An evaluator who controls whether a proposed change enters use helps determine which system results. An evaluator who only assesses an already-adopted change does not, through that assessment alone, determine its adoption. The difference is what the judgment controls, not whether a person or a program makes it.

This matters when deciding whose contributions explain a system's improvement. A human approval required for adoption is part of the process that selected the revision. A later human assessment is not evidence of that same contribution to selection.

## The same activity can perform different roles

Consider an agent that proposes a new KB instruction. These are hypothetical cases, not reports of observed behavior.

**Approval before adoption.** The agent proposes the instruction, a maintainer examines test results, and the agent adopts it only after the maintainer approves. The maintainer's judgment helps select the instruction that enters use. An account of how this change was selected must include that judgment.

**Assessment after adoption.** The agent adopts the instruction under its existing rules. A week later, the maintainer examines the results and concludes that the instruction helped. This judgment assesses an existing change; it did not decide whether that instruction entered use.

Both cases involve reading results and forming a verdict. Only the first verdict controls the adoption being examined. The later assessment could still cause a future revision or a rollback. That would give it a causal role in a different transition.

## One episode can contain both roles

A maintainer might approve a proposed instruction and later assess its effects in use. The episode then contains both selection and assessment. Calling the whole episode an evaluation does not identify which judgment did which work.

The account must name the change and the decision being examined. Whether approval was required for that adoption is a fact about the process. A different description cannot turn required approval into assessment after adoption.

Adoption here means entering a live behavioral path on which later operation depends, as distinguished by [operative change](./definitions/operative-change.md). A favorable assessment of a proposal that is never adopted does not establish an improvement of the deployed system.

## Scope

- This distinction concerns the causal role of a particular judgment. It does not establish that a later evaluator had no other influence on the system.
- Participation in selection does not by itself determine whether the evaluator counts as part of the learner. That depends on the declared system boundary. An externally supplied selection judgment must still be acknowledged as a contribution.
- Approval does not establish quality. An evaluator can select a harmful revision, just as a later assessment can misjudge its effects. A test available to the proposing system can be optimized without improving the capability it is meant to assess; human approval does not remove the need to justify the assessment.

## Open Questions

- How should an improvement claim report externally supplied adoption judgments when the evaluator is outside its declared learner boundary?
