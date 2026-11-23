---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "# A unified interface lets programmers choose prompts or code without changing callers"
    reason: "The writing shape asks the title to be the strongest compressed handle. The body's distinctive contribution is that the shared interface leaks asymmetrically in the two swap directions, so interface parity alone is not enough for safe swapping. The title states only the call-site-invariance half, and the description is what carries the asymmetric-leak claim. The title still works as a handle, so this is advisory."
    level: info
  - scope: passage
    quotes:
      - "This friction would likely discourage incremental refactoring and push toward big-bang rewrites. That effect is an expectation, not an observed result."
    reason: "This sentence states a limit on the claim (an unobserved expectation) in the body rather than under the `## Scope` heading. The instruction asks for limits to sit under that heading. The limit stays beside its claim, so this is a minor placement point rather than an unmet instruction."
    level: info
outcome: pass
---

# Review

The note does what the `note` type spec's authoring instructions ask.

- **Main claim near the top.** The opening paragraph states the claim: one interface hides whether a prompt or code implements an operation, and the abstraction leaks asymmetrically. The mechanism follows straight after.
- **Links to adjacent notes.** Inline links (the English account of prompting, constraining, codification, spec mining, relaxing and typed callables) support traversal at the points where they matter. The footer gives each link a relation label and a reason.
- **Design rationale, not procedure.** Prescriptive sentences such as enforcing schemas before codification are consequences of the argument. They are not step-by-step procedure, so they belong in a note.
- **Limits under `## Scope`.** The note has a `## Scope` section with three concrete limits: call invariance is not behavioral invariance, structural signature changes need adapters, and swapping back to prompts needs latency and cost headroom at the call site. These are narrow enough that a rescoping edit could change them without rewriting the claim.
- **Template shape.** The note follows the template: a prose title, a freeform analysis, Scope, Open Questions and a Relevant Notes footer.

The two INFO findings are advisory. The title compresses only half of the note's contribution. One expectation-level caveat sits in the body instead of under Scope. Neither is an unmet instruction.
