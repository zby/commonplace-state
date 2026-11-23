---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'But without a unified interface, each codification step is a breaking change:
    call sites must be updated, prompt structure must change, the agent''s view of
    available operations shifts. This friction discourages incremental refactoring
    and pushes toward big-bang rewrites.'
  reason: 'This is an empirical-sounding causal claim about what friction does to
    development practice (''discourages incremental refactoring'', ''pushes toward
    big-bang rewrites''). It is stated in the same declarative register as the design
    description, but the note presents no observation and cites no evidence for it.
    It also overstates the derivation: without a unified interface a codification
    step changes call sites, but ''each ... is a breaking change'' asserts this universally.'
  level: warn
- scope: passage
  quotes:
  - 'With unified calling, the progression is smooth:'
  reason: 'The progression is a constructed scenario: the `sanitize_filename` steps
    are hypothetical, and the observation step (''the agent consistently lowercases...'')
    reads like a report. The note presents the scenario as an established outcome
    (''is smooth'', ''the call site doesn''t change''). Nothing shows whether llm-do
    users actually followed this progression, or whether it is a design-level derivation.
    Support for llm-do''s architecture (shared namespace, name dispatch) is thereby
    presented as support for the experienced smoothness of refactoring.'
  level: warn
- scope: passage
  quotes:
  - Each link can be independently refactored without disturbing the rest.
  reason: This derived consequence holds only when interfaces are preserved, yet it
    reads as an established property of the architecture. The status is recoverable
    as a derivation from the stated premise, but only by effortful reading.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: cead3a2ab3223a39a27d524d121b933c37329874d980e453c9124a146044e75a
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/994c6f577d4f3563ba070ca9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-epistemic-status-blur.md
raw-output-sha256: e561ec6d00f84c7193c9ce72feef406401dedb755b3ca0e8af5f115275e40e5f
format: 2
---

# Review

The note mixes three kinds of claim:

- A reported design: llm-do's shared namespace, `.agent` files, name-based dispatch and imperative scheduler.
- A derived consequence: a shared interface means callers need not change.
- Proposed or empirical claims about development practice: friction pushes toward big-bang rewrites, and the progression is smooth.

The design description and the derivation are presented at an appropriate status. The practice-level claims are not. They carry the same declarative confidence as the design description, although the note offers no observation of refactoring episodes, and the worked progression is a constructed scenario written as if it had been observed. Support for "llm-do has this architecture" thus spreads to "refactoring with it is smooth".

The Open Questions section marks scale, debugging and language transfer as open. That correctly hedges those claims but leaves the flagged ones untouched.
