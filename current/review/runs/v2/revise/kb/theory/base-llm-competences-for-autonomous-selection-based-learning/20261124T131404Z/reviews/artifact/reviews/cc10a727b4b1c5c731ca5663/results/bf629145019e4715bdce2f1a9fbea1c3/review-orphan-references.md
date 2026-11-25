---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - where the three weakest tested models produced no held-out gains under the same
    harness-evolution loop that improved stronger models
  reason: The claim is sourced with a link to the ingest, labelled a bounded illustration,
    and scoped to one benchmark and loop, which matches the ingest. The benchmark
    (DeepPlanning) and the model families are not named in the body, so a reader must
    follow the link to learn what "weakest" and "held-out" refer to. That is acceptable,
    but naming the benchmark would make the claim legible in place.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/prose/orphan-references.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/prose/orphan-references.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/cc10a727b4b1c5c731ca5663/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: bf629145019e4715bdce2f1a9fbea1c3
completed-at: '2026-11-24T13:15:30Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/outputs/review-orphan-references.md
raw-output-sha256: 6268f20eb9303b48d49c0f35c0c1b7b40b098e014217946e2212fc6bc6936e84
format: 2
---

# Review

The note contains one concrete empirical claim: the three weakest models in the Harness Evolution study gained nothing on held-out tasks. It links the source ingest, describes the result as a bounded illustration, and repeats the scope limit in the footer. The ingest supports the wording: it states that the three no-gain lines are also the three weakest models. No other figures, percentages or named studies appear. The numbered competences are labels, not data.
