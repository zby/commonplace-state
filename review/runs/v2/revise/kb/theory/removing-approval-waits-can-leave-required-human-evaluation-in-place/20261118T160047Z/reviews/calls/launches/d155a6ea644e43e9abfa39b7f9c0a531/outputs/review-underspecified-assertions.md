---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A claim of full automation must say which tasks it preserves and which requirements it retires."
    reason: "'Preserves' could mean the tasks kept as human work, or the tasks whose function is kept by any means, including automated replacement. Taken alone, the two readings set different reporting obligations. The later paragraph resolves this by requiring the account to say 'what work still requires a person and what changed' and listing moved, automated, replaced and retired checks. The ambiguity is therefore resolved in context and is not material."
    level: info
outcome: pass
---

# Review

## Summary

The load-bearing assertions are the opening distinction, the definitions of actual wait, unfulfilled requirement and optional assessment, the classification of the two cases, the weekly-review gap, the revision-dependency rule, the reporting obligation, and the Scope boundaries. Each one names its mechanism (execution waits, or the specification assigns the task) and its scope (adoption versus the wider process including monitoring and revision).

The note supplies the clarifications that would otherwise be missing:

- It states which process a full-automation claim concerns: "A claim about automated adoption alone need not include monitoring or revision."
- It says what the weekly-review example establishes: a gap against the specification, not harm.
- It says what turns an optional study into a revision dependency: "Making a new human assessment a condition of each revision does."

The only candidate ambiguity, "preserves", is resolved by the nearby context and recorded as INFO.
