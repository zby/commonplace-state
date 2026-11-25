---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head
  reason: '"Keep track of ... in its head" attributes a human working memory to the
    model. The intended technical claim is about where state is held: budgets, traces
    and regression suites need not be carried in the model''s context window or reconstructed
    from its outputs across calls, because harness code stores and enforces them.
    A literal phrasing such as "the frozen model does not need to carry budgets, traces,
    or regression suites in its context" states the offloading mechanism the note
    argues for without implying internal mental bookkeeping.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/20bed09dfdfb4fd9af2855c76c65393e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/f318a48a0b65ea32d582e971/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 20bed09dfdfb4fd9af2855c76c65393e
completed-at: '2026-11-24T13:15:56Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/20bed09dfdfb4fd9af2855c76c65393e/outputs/review-anthropomorphic-framing.md
raw-output-sha256: e54d498cda68749e7fa3bdf188b99542f643d63f7bb53fff8b812ec237d81987
format: 2
---

# Review

## Summary

The note mostly describes model competences in behavioral, testable terms. "Interpreting unformalized text into action" is glossed as letting prose "govern its behavior under realistic context loads". "Diagnosing", "judging" and "recognizing missing evidence" name task functions whose outputs (diagnoses, candidate remedies, kept-open comparisons) can be checked. "Overclaiming certainty" describes produced output. These are the subject of the note, not stray cognitive attributions, so they are not flagged.

One idiom does import a mental-state picture: the model keeping track of things "in its head". The note's actual point is about relocating state from model context to harness code, and saying so directly would be more precise.
