---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Direct memory fails when it becomes generic capture rather than a role-specific artifact."
    reason: "Tested against boundary cases, the failure-mode framing is strained. A role-specific artifact that duplicates or contradicts an existing memory, or that hardens a lesson the agent wrongly judged stable from a single episode, is neither generic capture nor clearly one of the listed examples. The section's own examples (a findable-but-accurate note, a misleading instruction, a fossilized check) are also role-specific artifacts. They are coverable only if 'fails when' is read as one sufficient condition rather than as the failure space. The section does not claim to be exhaustive, so coverage is possible but strained."
    level: info
outcome: pass
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
