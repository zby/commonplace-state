---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A non-binding recommendation still creates a dependency if the agent must wait for it."
    reason: "The title restricts the claim to 'approval' waits, but the mechanism (execution control versus specification) uses no property of approval. The body itself counts waits for non-binding recommendations and habitual waits for human input as actual waits. Deleting 'approval' ('Removing human waits can leave required human evaluation in place') leaves the argument unchanged. The narrowing is probably intentional domain framing, since approval stops are the motivating case and the linked routine-approvals note uses the same framing, so this is INFO rather than WARN."
    level: info
outcome: pass
---

# Review

## Summary

Qualifiers in the title, description, and opening are *approval* (wait), *required* (evaluation), and *human*.

- **Required** is load-bearing. The note's central contrast is between required evaluation and optional assessment. Without it, the claim would sweep in optional studies, which the note explicitly says create neither a dependency nor a requirement.
- **Human** is load-bearing for the note's purpose. The argument concerns claims of automation: whether a person is still needed. A program applying human-authored rules is explicitly excluded from requiring "a new human judgment for each change."
- **Approval** is not used by the mechanism, and the body generalizes past it (see the INFO finding). Because approval stops are the evident motivating domain, the narrowing reads as intentional framing rather than an unnecessary assumption inherited by readers. It does not warrant WARN.
