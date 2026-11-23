---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - That sequence establishes three things.
  - the system adapted across tasks at deployment time without changing a single model
    weight
  reason: 'The routing-line sequence is introduced as a supposition (''Suppose agents
    repeatedly misfile...''). It is a constructed illustration, and the note does
    not report it as an observed episode. The summary then says the sequence ''establishes''
    three things and states the first in the register of an observation: ''the system
    adapted''. The note never says who the judge and reviewer are in the example.
    If they are LLM components, the illustration depicts the bet succeeding, which
    the note elsewhere marks as unproven (''no completed end-to-end automated run'').
    A constructed example can show that the paradigm is coherent. It cannot establish
    that adaptation occurred. The wording lets illustrative support read as evidence.'
  level: warn
- scope: passage
  quotes:
  - why did earlier AI systems not turn it into a general machine learning paradigm
  reason: 'The section frames the precedents as an answer to this question. It implies
    a historical explanation: earlier systems stalled because of how they decided
    whether to keep a change. That explanation is never stated as a hypothesis or
    supported. The causal reading is recoverable only as an implication of the framing,
    so its status takes effortful reading to assign.'
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 633d1cb13e9347e80c3c0f113b3d287e57c3358cb491657a0053c853021455a6
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/956564d3fab6ab509e65242d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-epistemic-status-blur.md
raw-output-sha256: afa70b06b4050265c4e4ac487f2e33ce1a5637241554e2b362809e68a5ec559d
format: 2
---

# Review

## Summary

The note's central conjecture is well marked. 'Our empirical bet', 'We bet', 'Consistency is part of the bet' and the explicit current-state paragraph ('no completed end-to-end automated run') keep the LLM-judgment claim recoverable as a hypothesis. Its falsification condition is stated.

Several other claims are recognizably derived or definitional rather than empirical. These include the decision-analysis material, the definition of selection-based learning and the condition that the Bitter Lesson compatibility depends on. The reported findings from the harness-evolution study are attributed and qualified ('stayed within noise').

The main blur is the worked example. A supposed sequence is summarized as having 'established' that a system adapted at deployment time. Illustrative support is thereby presented as if it were an observation.
