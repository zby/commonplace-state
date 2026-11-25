---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - keep genuinely contested or under-evidenced comparisons open, and recognize when
    an existing check is misleading
  reason: Competence 3 joins weighing trade-offs, keeping under-evidenced comparisons
    open, and recognizing that an existing check misleads. The last part could stand
    alone as a claim about check failure. The bold label names both halves, and the
    note counts exactly three competences, so splitting the item would change the
    claim. This is a borderline compound, not a buried second point.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/1c0a7c49c6a741fbaac55e35c3f53a13/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/2b2f8ab5ea1dfa1ae4c05d49/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 1c0a7c49c6a741fbaac55e35c3f53a13
completed-at: '2026-11-24T13:16:07Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/1c0a7c49c6a741fbaac55e35c3f53a13/outputs/review-compound-bullet.md
raw-output-sha256: 9b3fa21e74fe808fa96991d4118c192a321c1ad856f0f8b1ff6af904abd75b16
format: 2
---

# Review

## Summary

Several items are longer than 30 words: the three harness-function bullets, the three numbered competences and the first Scope bullet. Each develops one idea.

The harness-function bullets list example tasks under one label. Competences 1 and 2 each state one competence and its supporting detail. Competence 2's bold label joins diagnosis and candidate synthesis, but the sentence presents them as one step that runs from a trace to remedies. The first Scope bullet says that the split is a working hypothesis. It then explains how the hypothesis can be revised in either direction. That second sentence elaborates the first claim; it does not add a separate point.

Competence 3 is the closest case, as the finding explains. It stays at INFO because the note intentionally bundles these parts into one competence that it counts.
