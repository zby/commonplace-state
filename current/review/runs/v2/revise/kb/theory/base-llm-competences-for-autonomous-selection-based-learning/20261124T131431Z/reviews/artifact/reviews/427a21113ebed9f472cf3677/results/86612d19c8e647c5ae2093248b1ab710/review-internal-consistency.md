---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - three irreducible semantic competences remain
  reason: '''Irreducible'' conflicts mildly with the Scope section, which says any
    sub-task shown to be reliably offloadable moves out of the LLM column. It also
    conflicts with the later use of ''reduces to competences 2 and 3'' in a different
    sense. Because ''irreducible'' sits under ''our working hypothesis'', this is
    likely wording drift rather than contradiction, but a human should confirm which
    sense is intended.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/86612d19c8e647c5ae2093248b1ab710/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/427a21113ebed9f472cf3677/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 86612d19c8e647c5ae2093248b1ab710
completed-at: '2026-11-24T13:18:10Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/86612d19c8e647c5ae2093248b1ab710/outputs/review-internal-consistency.md
raw-output-sha256: 5bb5c159acf183c5cc7b78234f32ba589a5b10e9b587fe353efa79ee23ccb56f
format: 2
---

# Review

## Summary

The title, description, opening and Scope agree. All four present the split as a working hypothesis in which harness code takes much of the loop and three semantic competences remain on the model. The harness list (detecting bloat, staleness and regressions) and the store-maintenance paragraph (semantic conflicts and criterion revision go to competences 2 and 3) divide the work consistently. Autonomous operation and the human-assisted bootstrap do not conflict: the Scope says the competences are necessary for autonomous operation, and the bootstrap paragraph covers the period before they are met. The Harness Evolution paragraph is bounded as an illustration and agrees with the "base-model floor" in the Open Questions.

The only drift is the word "irreducible", noted as INFO.
