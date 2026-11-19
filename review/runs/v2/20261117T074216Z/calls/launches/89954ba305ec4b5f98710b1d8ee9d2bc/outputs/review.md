---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the first requires a person for the process to proceed"
    reason: "The note gives two tests for the operating-dependency side: the system 'must wait for' the evaluation, and the process 'requires a person' to proceed. A veto window (the change is adopted automatically unless a maintainer objects within a set period) sits between the two cases. The system waits, but it proceeds without any person acting. The tests therefore disagree. The monitoring paragraph's 'monitoring on which the process relies' test can classify this case, but only by inference. Coverage is possible but strained. One sentence naming default-adopt or veto-window review, and saying which test governs, would remove the ambiguity."
    level: info
outcome: pass
---

# Review

## Summary

The note sets up a two-way distinction. Human evaluation that adoption depends on (an operating dependency) is set against assessment that only measures adopted results. I tested this distinction against boundary cases taken from the note's own framing. Most cases map cleanly, and the note already handles several boundary cases explicitly. One in-between case, the veto window, is only strained, so this is an INFO finding and the outcome is pass.

## Grounding definition

The note grounds the distinction in two places. The opening paragraph names the operating side: "must wait for before adopting" and "requires a person for the process to proceed". The monitoring paragraph widens the test to dependence after adoption: "monitoring on which the process relies".

## Boundary cases tested

- **Simplest instances:** required approval and non-blocking assessment. The note's two worked cases map cleanly.
- **Approval that always passes:** the maintainer always approves. The note covers this explicitly: it is still a dependency. It also cross-links routine approvals.
- **Non-binding recommendation the agent waits for:** covered explicitly as a dependency.
- **Human-authored rules applied by a program:** covered explicitly as not needing a new judgment for each change.
- **Automated adoption with required monitoring and rollback:** covered explicitly as a dependency that has moved downstream rather than disappeared.
- **Anticipated assessment that shapes proposals:** covered in Scope as influence without a stop.
- **Bypassed required check:** covered in Scope.
- **Veto window, or adopt-unless-objected:** this case falls between the enumerated cases. See the finding. The "relies on" test can classify it, but the note does not name the case.
- **Sampled or risk-gated approval, where only some changes wait for a human:** the test applies to each change and maps cleanly. The process depends on a person for the gated subset.

## Weight

The distinction is binary and short, and its argumentative role justifies it. Adding a category is not warranted. At most, one clarifying sentence is needed.
