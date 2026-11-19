---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The bound does not fix its own N"
    reason: "N appears here for the first time and is never defined. The heading (\"What kind of number a step size is\") lets the reader guess that N is the step-size limit, but not what it counts: unquoted sources per note, artifacts opened, or something else. The note uses no formal arguments, so plain language such as \"the maximum number of unquoted sources a note may cite\" would serve better than the symbol."
    level: warn
  - scope: passage
    quotes:
      - "Does not decide N, a validator rule that would enforce it"
    reason: "N is reused in Scope and in the Lamport paragraph (\"any particular N\"). Each of these sentences only makes sense if the reader has inferred N's meaning from the earlier section. Replacing the symbol with a plain-language phrase throughout would remove the dependency."
    level: info
outcome: warn
---

# Review

## Summary

The note's only formal notation is the variable N, which names the step-size limit in the section "What kind of number a step size is", in the Lamport paragraph and in Scope. It is not given a local definition. The reader has to infer from the heading and the earlier argument that N counts unquoted sources per note. Since the note makes no equation or pseudocode argument, the gate prefers plain language over the symbol.

The inline code markers `verbatim` and `(snapshot required)` are not opaque notation: each is explained in its own sentence (substring match against the linked file; a source with no bounded passage that counts fully against the step).
