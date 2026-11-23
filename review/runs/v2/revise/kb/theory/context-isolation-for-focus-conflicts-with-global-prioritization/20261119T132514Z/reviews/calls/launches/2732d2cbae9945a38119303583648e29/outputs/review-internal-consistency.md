---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "deciding how much effort a local branch deserves relative to other work, when to stop or defer it"
      - "a local execution judgment the isolated worker can make"
    reason: "The opening defines global prioritization to include 'when to stop or defer' a branch, a decision the isolated worker 'cannot reliably make'. The unbundled-decisions list then calls 'This run should stop' a local execution judgment the isolated worker can make. The residual-friction section adds that stopping is still bounded by a compressed proxy of global priority ('when to stop digging'). The reconciling distinction, stopping because a local or injected stop condition is met versus stopping because other work matters more, is not stated at either site. As written, the two passages assign the same decision to opposite sides of the split."
    level: warn
outcome: warn
---

# Review

## Claims checked

- **Opening.** Isolation removes the live comparison set. Global prioritization covers effort, stopping or deferral, and escalation. Isolated workers keep local technical judgment.
- **Failure section.** Missing context explains indiscrimination, and defaults set its direction. Static rules cannot supply live relative scale.
- **Split section.**
  - The worker receives injected stop conditions and does not judge global urgency.
  - Triage compares compressed summaries.
  - There are three unbundled decisions.
- **Residual friction.** Within-episode choices, including when to stop digging, remain local but are bounded by a compressed proxy of global priority.
- **Scope.** The conflict needs bounded context and a non-fitting workload, and it applies to relational prioritization only.

## Assessment

Most claims cohere:

- The claim-mode conditions match the Scope section.
- The "narrower than lacking judgment" paragraph matches the worker's role in the split.
- The default-direction argument matches the escalation bullet's caveat.
- The illustrations-not-corroboration framing is consistent across the split and Scope sections.

The one contradiction is where the stopping decision sits (see finding). Point 1 of the split ("local stop conditions from outside") and the residual-friction bullet hint at a reconciliation, but the triad states it without that qualification.
