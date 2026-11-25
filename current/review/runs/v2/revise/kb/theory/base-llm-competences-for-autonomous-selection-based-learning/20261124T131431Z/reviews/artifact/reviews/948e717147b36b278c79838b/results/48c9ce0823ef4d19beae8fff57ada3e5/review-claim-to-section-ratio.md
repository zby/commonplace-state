---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/48c9ce0823ef4d19beae8fff57ada3e5/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/948e717147b36b278c79838b/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 48c9ce0823ef4d19beae8fff57ada3e5
completed-at: '2026-11-24T13:15:24Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/48c9ce0823ef4d19beae8fff57ada3e5/outputs/review-claim-to-section-ratio.md
raw-output-sha256: d75650165a4942ba8fdd53c1c0dfa81f2ba55303b26a5ef64fd1992c2a3e3825
format: 2
---

# Review

The note has three sections: an untitled lead body, `## Scope` and `## Open Questions`. The lead body carries several distinct non-obvious claims:

1. Harness code can take over enforcement, evidence capture and replay, and store bookkeeping, so the frozen model need not track them.
2. Three semantic competences remain on the frozen base LLM in open-ended work: interpreting uncodified text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs.
3. Store-level maintenance and criterion revision need no separate competence; they reduce to competences 2 and 3 applied to the store.
4. The competences fail independently at different thresholds, so a human-assisted bootstrap can identify the binding one.
5. A bounded empirical case shows that a weak base model can block outer-loop learning before the store saturates.

`## Scope` carries boundary conditions: the split is a revisable working hypothesis, and the competences are necessary but not sufficient. `## Open Questions` states two unresolved points that the body does not restate. No section repeats the framing of another. Five or more claims share three sections, so sections do not outnumber claims.
