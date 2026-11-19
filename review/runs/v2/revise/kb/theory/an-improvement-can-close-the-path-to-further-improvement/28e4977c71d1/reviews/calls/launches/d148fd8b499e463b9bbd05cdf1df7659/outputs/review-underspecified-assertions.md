---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "If that scope includes the ability to revise the system's improvement machinery"
    reason: "This assertion states what a non-regression scope must include, and it allows two materially different readings. Reading A: the scope must include the first-order capability to produce and install another revision of the system, the capability the example agent loses. Reading B: the scope must include the second-order capability to revise the improvement machinery itself, such as editing the revision workflow or the evaluator. The unresolved choice is the scope of the checked capability. The choice changes what a declared comparison must test: whether another revision can still be carried through to use, or whether the revision workflow itself stays revisable. It also changes whether the example's successor fails. The surrounding text (\"the revision capability\", \"the only applicable revision path\") leans toward Reading A, but the explicit object \"improvement machinery\" supports Reading B."
    level: warn
outcome: warn
---

# Review

Most load-bearing assertions are exact.

- **The worked example.** It names the workflow, the change and the lost route.
- **The replacement condition.** It requires a replacement to "carry another revision through to use".
- **The Scope entries.** They state the system boundary and alternative paths.

The note's operative recommendation is the sentence that says what non-regression must check. That sentence leaves the object of the checked capability unresolved between producing another revision and revising the improvement machinery. The two readings call for different checks in a declared comparison, so the difference is material.
