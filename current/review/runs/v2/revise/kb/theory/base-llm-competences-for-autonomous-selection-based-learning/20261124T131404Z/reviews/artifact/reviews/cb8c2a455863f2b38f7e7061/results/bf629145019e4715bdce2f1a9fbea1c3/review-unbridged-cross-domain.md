---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Even within one benchmark and loop, an inadequate base model can block outer-loop
    learning before the store itself saturates.
  reason: 'The cited result comes from a fixed-task planning benchmark with a parsing
    scorer, while the note''s argument concerns open-ended work in which new failure
    modes keep arriving. The source and target domains share the relevant mechanism:
    a frozen-weight loop that selects edits to a harness store. The note also limits
    the citation to an illustration of a base-model floor within that one benchmark
    and loop, not evidence for the three-competence split. Stating that the shared
    mechanism is the frozen-weight store-editing loop would make the bridge explicit,
    but the transfer as worded is not overclaimed.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/cb8c2a455863f2b38f7e7061/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: bf629145019e4715bdce2f1a9fbea1c3
completed-at: '2026-11-24T13:15:30Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 498a54e21dc6bb135af906ca346062d5d6beec04bc2d1e802b32f01833a787ce
format: 2
---

# Review

The note cites one empirical result: the Harness Evolution study. Its domain is a harness-evolution loop over small models on one planning benchmark. That loop is a frozen-weight selection loop over a store of prompts, lessons and tools, so it is an instance of the note's argument domain rather than a different domain. The note claims only that a base-model floor exists in that setting and explicitly limits the claim to one benchmark and loop. It does not use the result to show which of the three competences binds. No unbridged transfer remains.
