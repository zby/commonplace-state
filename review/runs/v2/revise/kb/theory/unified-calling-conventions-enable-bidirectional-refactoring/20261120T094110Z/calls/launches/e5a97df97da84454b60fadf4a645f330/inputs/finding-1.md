---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/accessibility/unidentified-references.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/accessibility/unidentified-references.md
criterion-sha256: 422847c587793f494bfa140e10c46772cc1decaf72d3a611ec83daa39da288c3
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 3eb26f9df34f411faf101251b0454a5c
completed-at: '2026-11-20T09:42:07Z'
findings:
- scope: passage
  quotes:
  - implements this through a hybrid VM where agents
  reason: The note introduces llm-do by linking to its repository and then describing
    its mechanism, without saying what kind of thing it is. A reader can infer that
    it is software that runs agents and tools, but the note never identifies it as,
    for example, a framework or runtime for composing LLM agents with Python tools.
    The link does not replace an inline identification. The author should add a short
    gloss on first mention and should say who made it only if the author can state
    that.
  level: warn
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/36bf1df07a36fcb407f8d9df/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/outputs/review-unidentified-references.md
raw-output-sha256: 2fc3d15dbea49b11fe0fc92d147b1e73bb2f96b388ec31b2187206ce1ee21e70
---

# Review

## Summary

One proper noun, llm-do, is the note's central example, but its first mention does not identify it.

The other named systems are identified. LangGraph and CrewAI are introduced as "declarative agent frameworks". Python and YAML are standard technology names. llm-do is introduced only through a link and through the mechanism it implements. Readers must infer what kind of system it is from the hybrid-VM description that follows. Adding a short type gloss on first mention would resolve this.
