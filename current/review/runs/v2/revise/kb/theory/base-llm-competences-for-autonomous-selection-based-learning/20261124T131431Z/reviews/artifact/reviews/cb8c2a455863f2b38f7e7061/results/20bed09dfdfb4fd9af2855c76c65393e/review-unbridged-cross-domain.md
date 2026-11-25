---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/20bed09dfdfb4fd9af2855c76c65393e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/cb8c2a455863f2b38f7e7061/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 20bed09dfdfb4fd9af2855c76c65393e
completed-at: '2026-11-24T13:15:56Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/20bed09dfdfb4fd9af2855c76c65393e/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 6a7ba58b5b164b3233f2c0319223768454638e2d6e77d508d9792467cdadf272
format: 2
---

# Review

## Summary

The note cites one empirical result: weak models gained nothing on held-out tasks under a harness-evolution loop that improved stronger models. The source domain, a self-evolving harness that updates prompts, lessons and tools around a fixed model, is an instance of the note's argument domain, an autonomous selection-based learning loop that updates a store around a frozen base LLM. No domain transfer is needed for the claim the evidence is used to support: that an inadequate base model can block outer-loop learning.

The note limits the transfer it does make. It calls the result "a bounded empirical illustration of a base-model floor" and confines it to "one benchmark and loop". It does not claim that the result confirms the specific three-competence split, or that it generalizes to the open-ended software and KB maintenance settings named in the open questions. No bridge is missing.
