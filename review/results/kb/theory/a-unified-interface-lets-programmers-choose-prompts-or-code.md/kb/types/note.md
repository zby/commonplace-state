---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/types/note.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: b15473851bf04e13a7c12fcc3d7fa4bb
completed-at: '2026-11-20T11:10:29Z'
findings:
- scope: passage
  quotes:
  - '# A unified interface lets programmers choose prompts or code without changing
    callers'
  reason: The writing shape asks the title to be the strongest compressed handle.
    The body's distinctive contribution is that the shared interface leaks asymmetrically
    in the two swap directions, so interface parity alone is not enough for safe swapping.
    The title states only the call-site-invariance half, and the description is what
    carries the asymmetric-leak claim. The title still works as a handle, so this
    is advisory.
  level: info
- scope: passage
  quotes:
  - This friction would likely discourage incremental refactoring and push toward
    big-bang rewrites. That effect is an expectation, not an observed result.
  reason: This sentence states a limit on the claim (an unobserved expectation) in
    the body rather than under the `## Scope` heading. The instruction asks for limits
    to sit under that heading. The limit stays beside its claim, so this is a minor
    placement point rather than an unmet instruction.
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/b15473851bf04e13a7c12fcc3d7fa4bb/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/cd211ced30b98823ae846049/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/b15473851bf04e13a7c12fcc3d7fa4bb/outputs/review.md
raw-output-sha256: 57d9911956b7cd0ee1e9f39723287ab1eb0ff9c34c64ff076a97fafff41f9c42
---

# Review

The note does what the `note` type spec's authoring instructions ask.

- **Main claim near the top.** The opening paragraph states the claim: one interface hides whether a prompt or code implements an operation, and the abstraction leaks asymmetrically. The mechanism follows straight after.
- **Links to adjacent notes.** Inline links (the English account of prompting, constraining, codification, spec mining, relaxing and typed callables) support traversal at the points where they matter. The footer gives each link a relation label and a reason.
- **Design rationale, not procedure.** Prescriptive sentences such as enforcing schemas before codification are consequences of the argument. They are not step-by-step procedure, so they belong in a note.
- **Limits under `## Scope`.** The note has a `## Scope` section with three concrete limits: call invariance is not behavioral invariance, structural signature changes need adapters, and swapping back to prompts needs latency and cost headroom at the call site. These are narrow enough that a rescoping edit could change them without rewriting the claim.
- **Template shape.** The note follows the template: a prose title, a freeform analysis, Scope, Open Questions and a Relevant Notes footer.

The two INFO findings are advisory. The title compresses only half of the note's contribution. One expectation-level caveat sits in the body instead of under Scope. Neither is an unmet instruction.
