---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Direct memory fails when it becomes generic capture rather than a role-specific
    artifact.
  reason: Tested against boundary cases, the failure-mode framing is strained. A role-specific
    artifact that duplicates or contradicts an existing memory, or that hardens a
    lesson the agent wrongly judged stable from a single episode, is neither generic
    capture nor clearly one of the listed examples. The section's own examples (a
    findable-but-accurate note, a misleading instruction, a fossilized check) are
    also role-specific artifacts. They are coverable only if 'fails when' is read
    as one sufficient condition rather than as the failure space. The section does
    not claim to be exhaustive, so coverage is possible but strained.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/agent-memory-requirements/create-memory-directly.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: fe3aada7aec4ce0d85e704be3bf70dc5d6242099ac82171dd77187fb75b4e33f
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/907eed36ae6db4e365dd1a69/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/907eed36ae6db4e365dd1a69/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 46f7e46ad52a4cef93827df87f98030b
completed-at: '2026-11-16T11:25:30Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/46f7e46ad52a4cef93827df87f98030b/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 897de78001d3a13df44dbb605f44604c9c3e2e3b512cbac9a5981886112fe02e
format: 2
---

# Review

## Summary

The note contains two enumerations: the Methods list of destination kinds and the Failure Modes section.

**Methods.** The grounding definition comes from the opening: direct creation applies when work reveals "a stable claim, procedure, policy, index entry, validation rule, or tool extension." I tested these boundary cases:

- Simplest instance: a single factual claim maps to notes.
- Extreme instance: a governed rule embedded in a work surface maps to the work-surface item.
- Between items: a user preference or a convention could go to notes or to instructions. Either placement is acceptable.
- Adjacent concept: fine-tuned weights fall outside direct creation. The note does not claim to cover distributed-parametric memory, so this is a scope boundary, not a gap.

The final Methods item lists write-time support (templates, validators, routing cues) rather than a destination. The preceding paragraph prepares the reader for that shift, so it does not break the list.

**Failure modes.** The framing sentence names one cause: generic capture. The boundary cases recorded in the finding sit awkwardly under that sentence. The section does not claim completeness, though, and its closing criterion ("good only when it becomes useful future context or useful future behavior") is broad enough to absorb them. The result is INFO, not WARN. Neither list is longer than its role warrants, so expanding it is not the obvious fix. Clarifying the scope of the framing sentence would suffice.
