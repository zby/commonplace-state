---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Harness code may offload much of a selection loop, leaving three base LLM competences
  reason: 'The modal "may" softens the first clause toward a possibility claim, but
    the contestable content sits in the main predicate: that the residue after offloading
    is exactly three base-LLM competences. An informed reader could argue the harness
    offloads little, or that more, fewer or different competences remain. The hedge
    matches the note''s declared working-hypothesis status rather than hiding a truism.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: 6a55a7da08cc048516968bc1585e42d1ae84de609542823eeb090628ab7aff46
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1ebc4d6655fb4afbba43b5d1c07168c8/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/6306c54dc806e78c04737e71/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 1ebc4d6655fb4afbba43b5d1c07168c8
completed-at: '2026-11-24T13:15:22Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1ebc4d6655fb4afbba43b5d1c07168c8/outputs/review-claim-strength.md
raw-output-sha256: c7e20cbf36b08c71c9e33be69d5cf31f96200d34c6b1c82db6747a22d0c7211d
format: 2
---

# Review

## Summary

The title is contestable. "Harness code may offload much of a selection loop" alone would be close to uncontroversial. The title's commitment comes from "leaving three base LLM competences": a specific claim about what cannot be offloaded and how many residual competences there are. Someone informed could reasonably argue that diagnosis and judgment can largely move into harness code, or that the remaining work does not split into three separable competences. The title states the hard point in its predicate instead of presupposing it in its subject, so the presupposed-claim pattern does not apply.
