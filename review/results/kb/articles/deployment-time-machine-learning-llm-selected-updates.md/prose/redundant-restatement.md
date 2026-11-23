---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b4e70f5925ff4ae894d0f33589d060fa
completed-at: '2026-11-22T09:34:30Z'
findings:
- scope: passage
  quotes:
  - 'one condition: a change to what the system retains for its later work is'
  reason: 'This section''s opening paragraph restates the definition of selection-based
    learning that the introduction already gave (''learning through proposed changes
    that are evaluated and can be rejected''). It then adds new detail: evaluation
    need not be a separate stage, rejection is its own event, and the measure may
    be fixed or a comparison. The introduction gives setup and this section gives
    the fuller statement, so the overlap is intentional reinforcement at a different
    structural position.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/ed238768f3178e9378010c59/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b4e70f5925ff4ae894d0f33589d060fa/outputs/review-redundant-restatement.md
raw-output-sha256: 5b1733c0b5cdd172d8987bfc84bb78f13322ec83ce99b94310e81721a6f85027
---

# Review

## Summary

Section openings:

- "One change followed through" opens with a one-sentence transition.
- "Selection-based learning versus direct gradient training" re-grounds the
  introduction's definition, then extends it. Deleting the paragraph would
  remove content the section depends on.
- "Proof, formula, judgment" opens with a framing question that the section
  answers.
- "Compatible with the Bitter Lesson" opens with the objection it then
  rebuts.
- "Whether a change improved the system" briefly recalls that the term carries
  no success condition, then defines how improvement is judged.

Closing paragraphs: none of the paragraphs before a heading previews or
enumerates what the next section develops.

The introduction's statement of the bet is repeated in the "Proof, formula,
judgment" section. That repetition falls mid-section, not at a boundary, so
this gate does not cover it.
