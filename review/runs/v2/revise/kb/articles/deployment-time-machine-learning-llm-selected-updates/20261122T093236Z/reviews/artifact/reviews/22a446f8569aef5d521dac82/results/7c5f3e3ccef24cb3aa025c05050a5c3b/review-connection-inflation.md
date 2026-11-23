---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/22a446f8569aef5d521dac82/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 7c5f3e3ccef24cb3aa025c05050a5c3b
completed-at: '2026-11-22T09:33:39Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/7c5f3e3ccef24cb3aa025c05050a5c3b/outputs/review-connection-inflation.md
raw-output-sha256: c8b45fa27eafe757179093c06c66e6d200e14a7e6e15db5e4f2938e807c4b14c
format: 2
---

# Review

## Summary

The article has no Relevant Notes footer; its closing "Where to go next" list plays that role, so each entry was checked against the body's inline use. Every entry adds navigational context or a target absent from the body.

## Entries

- **Testing Autonomous Selection-Based Learning.** The body links it as the place that "sets those comparisons out". The entry adds that the article also proposes a first experiment, which tells a reader why to open it next. The overlap is real but not complete.
- **The definition (selection-based learning).** The body cites it only for the one defining condition. The entry adds what the full definition contains: what a claim must name, and boundary cases such as triggers and direct updates.
- **Single-loop and double-loop learning.** The body never links this definition, so the entry is new navigation.
- **Necessary preference can guide improvement without a global measure.** The body uses it inline for "robust comparison". The entry adds that the note covers how to decide open comparisons and states Commonplace's declared objective, which the body does not say.
- **Reversibility can favor a change by limiting future loss.** The body links it inline. The entry adds a pairing relation to the necessary-preference note.
- **Companion drafts (theory-builder articles).** The body does not link any of them, and the entry explains their status and the narrower *theory builder* framing.

No entry both repeats a body link and restates the same relationship without new information.
