---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Caller (agent or code) ──▶ ticket_classifier ──▶ binding"
    reason: "The ASCII flow diagram restates the preceding sentence, in which the programmer binds a name such as `ticket_classifier` to either a prompt-backed agent or a Python function. Deleting the diagram loses no category, decision rule or inference, and it supports no prediction. The same route already survives as one sentence."
    level: warn
outcome: warn
---

# Review

## Summary

The note has four structures. Only one is decorative.

- **ASCII binding diagram (The mechanism).** Decorative; see the finding. It shows one name resolving to one of two implementations, which the prose above it already says in one sentence. It adds no information about the run-level binding choice or the declared-argument scoping. Those appear only in prose.
- **Two-direction leak list.** Load-bearing. Each direction names a distinct caller type and a distinct failure mechanism, and the next paragraph derives two separate prescriptions from them. Merging the two into one sentence would lose the asymmetry, which is the note's central claim.
- **Three-move taxonomy (refactoring, prototyping, relaxing).** Load-bearing. The note uses the distinction for an inference: only the first move preserves behavior, yet all three stay local to the binding. The categories also map onto linked definitions (codification, relaxing) rather than adding vocabulary the argument never uses.
- **Scope bullets.** Each bullet states a boundary condition that limits the main claim. None adds categories that go unused.

Delete the diagram, or replace it with something prose cannot carry, such as where run-level binding resolution happens.
