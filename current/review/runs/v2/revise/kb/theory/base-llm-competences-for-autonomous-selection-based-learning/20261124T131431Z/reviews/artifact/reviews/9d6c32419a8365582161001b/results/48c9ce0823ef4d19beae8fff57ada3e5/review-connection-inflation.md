---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'grounds: why harness offloading narrows the base-LLM floor without eliminating
    it'
  reason: The body already cites this note inline at the point where it argues that
    semantic work is relocated rather than eliminated. The footer adds the typed `grounds`
    relation but little framing beyond the body's use. This entry is near the inflation
    threshold but not over it.
  level: info
- scope: passage
  quotes:
  - 'evidenced-by: weak-model lines produced no held-out harness gains under a loop
    that lifted stronger models (bounded to one benchmark and loop)'
  reason: 'The footer gloss restates the body''s paragraph about this source almost
    exactly: weakest models, no held-out gains, the same loop improved stronger models,
    one benchmark and loop. Its only addition is the typed `evidenced-by` edge. That
    edge keeps the entry from being inflated under the gate''s second question, but
    the context phrase could be shortened.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/48c9ce0823ef4d19beae8fff57ada3e5/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/9d6c32419a8365582161001b/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 48c9ce0823ef4d19beae8fff57ada3e5
completed-at: '2026-11-24T13:15:24Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/48c9ce0823ef4d19beae8fff57ada3e5/outputs/review-connection-inflation.md
raw-output-sha256: df2bc06569486299f7519fef77ac6d123c2c97822f3d9686c686027c5378d9f9
format: 2
---

# Review

Each of the eight footer entries also appears inline in the body, which the gate says is not inflation by itself. Every entry adds a typed relation (`defined-in`, `grounds`, `extends`, `evidenced-by`), so none fails the gate's second question.

Several entries add framing that the body's inline use lacks. The scheduler–LLM entry names the other side of the split, which keeps semantic interpretation on the model. The on-balance judgment entry says the target also covers how to test an LLM selector. The diagnostic-richness entry describes how the evidence interface interacts with competence 2. The operative-change entry states the failure condition for competence 1. The single-loop/double-loop entry ties criterion revision to competences 2 and 3.

Two entries mostly restate the body's framing; the info findings record them. Neither is flagged as inflated, because the typed relation is navigational information the inline citation does not carry.
