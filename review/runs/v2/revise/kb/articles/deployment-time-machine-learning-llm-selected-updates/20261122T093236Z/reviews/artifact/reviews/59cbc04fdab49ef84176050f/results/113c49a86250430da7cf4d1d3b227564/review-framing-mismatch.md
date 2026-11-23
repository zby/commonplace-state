---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Unlike proof-gated switches, empirical admission admits harmful changes
  reason: 'The contrast presents harmful admission as specific to empirical admission.
    The mechanism is that the last filter''s false positives become operative. That
    mechanism also covers proof-gated admission whenever the formalization is inadequate,
    and the article says so earlier (''under an inadequate formalization, a proved
    switch need not deliver what its user wanted''). The framing excludes a case the
    mechanism covers. Contrast instead on what each filter can certify, for example:
    proof-gated admission excludes changes harmful under its axioms; empirical admission
    certifies nothing beyond its observed evidence.'
  level: warn
- scope: passage
  quotes:
  - Training or fine-tuning runs
  reason: The table row presents the timing of updates as separating gradient training
    from selection over a readable store. Weight updates can also run online during
    deployment (the linked deployment-time adaptation note says so). The paragraph
    below qualifies 'deployment time' for the readable-store column, but not this
    column's restriction. This emphasizes the typical case rather than excluding the
    other outright.
  level: info
- scope: passage
  quotes:
  - on a task already near the model's effective context limit, extra prompt text
    can tip a correct answer into rework
  reason: Context cost is framed as a near-limit effect, while the stated cost is
    diffuse load on every task. The preceding clause ('every unrelated task also loads
    that extra line') keeps the general case, so this only emphasizes the most visible
    instance.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/59cbc04fdab49ef84176050f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 113c49a86250430da7cf4d1d3b227564
completed-at: '2026-11-22T09:37:43Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/outputs/review-framing-mismatch.md
raw-output-sha256: 0b841a0087fe0004be42c8311d024d771374924c02f2c1ce5265d73c445d62f6
format: 2
---

# Review

## Summary

Most mechanism statements are framed at the right generality: direct versus
selected updates, credit assignment without a chain rule, operative dependence,
open verdicts under necessary preference, and the Bitter Lesson's production-
method axis. One hazard bullet frames false-positive retention as unique to
empirical admission. The article's own Gödel machine paragraph shows that the
mechanism reaches proof-gated admission too, so that framing earns a warning.
Two other framings emphasize a typical case without excluding others.
