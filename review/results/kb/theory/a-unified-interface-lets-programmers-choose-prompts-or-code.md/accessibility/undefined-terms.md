---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 2507e629a34445439219d3dc27929d21
completed-at: '2026-11-20T11:10:04Z'
findings:
- scope: passage
  quotes:
  - Call boundaries must enforce schemas before codification
  reason: First body mention of the active vocabulary term 'codification' has neither
    an inline gloss nor a link; the link and the terse gloss 'changing medium' arrive
    only later in 'Why this matters for constraining'. A reader can partly infer the
    meaning from the preceding prompt-to-code bullet, but the gate requires a gloss
    and link at first meaningful mention. Gloss it here (e.g. moving a rule from a
    prompt into code) and link the definition.
  level: warn
- scope: passage
  quotes:
  - brittle proxy theory
  reason: '''Proxy theory'' reads as KB-specific phrasing and is not defined. The
    clause ''that fails on edge cases or distribution shift'' gives enough context
    to infer roughly what it means (a coded rule that approximates the real task),
    so the barrier is minor.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2507e629a34445439219d3dc27929d21/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/7924916eea42702c8c51b162/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2507e629a34445439219d3dc27929d21/outputs/review-undefined-terms.md
raw-output-sha256: 96ab4e1f91fb9805223ac718d763b6d30b6aac2ce5e0371644c3a076003e00fc
---

# Review

## Summary

Most technical terms are introduced with enough local context. Information hiding is defined in the opening paragraph. llm-do's callable namespace is described where it is introduced. Relaxing is glossed as "regaining generality". The spec-mining link follows a sentence that describes the activity. Constraining is linked and paired with "narrowing the interpretation space". Execution regime becomes clear through the contrast with ordinary code-to-code swaps.

The main gap is codification. It is an active vocabulary term, and its first body use, in the practical-consequence paragraph, is bare. Its link and a brief gloss appear only ten lines later, so the definition comes after the sentence that depends on it.
