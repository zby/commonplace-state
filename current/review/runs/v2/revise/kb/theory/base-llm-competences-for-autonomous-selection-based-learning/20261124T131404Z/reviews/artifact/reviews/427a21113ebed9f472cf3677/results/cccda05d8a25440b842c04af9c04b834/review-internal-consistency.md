---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - three irreducible semantic competences remain on the frozen base LLM
  reason: '''Irreducible'' sits uneasily with the Scope statement that offloadable
    sub-tasks move out of the LLM column and new bottlenecks can be added. Read as
    a hypothesis of irreducibility, the two are compatible. Read literally, ''irreducible''
    conflicts with the stated revisability. This is likely drift that needs author
    confirmation, not a contradiction.'
  level: info
- scope: passage
  quotes:
  - routing and loading the relevant artifacts
  reason: The opening assigns routing of relevant artifacts to harness code. The note
    also says semantic work stays on the model. Choosing which uncodified artifact
    is relevant to a novel case is meaning-dependent, so the note's two columns may
    overlap here. This is an ambiguity that needs confirmation, not a contradiction.
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
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/427a21113ebed9f472cf3677/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: cccda05d8a25440b842c04af9c04b834
completed-at: '2026-11-24T13:17:58Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/outputs/review-internal-consistency.md
raw-output-sha256: 090c593ae4227dfa9d404ab0e77b447ad95b7ea690296fdf015ed0a86a11f0fd
format: 2
---

# Review

## Summary

The sections agree. The opening, competence list, store-maintenance paragraph, independence paragraph, empirical illustration, Scope and Open Questions all treat the split as a working hypothesis. All of them place mechanical work in harness code and semantic work on the frozen model. The human-assisted bootstrap is explicitly temporary, so it does not contradict the autonomy framing. The description matches the body. Two terms are close to drift: "irreducible" against the revisability clause, and harness-side "routing" against the semantic residue. Neither is an outright contradiction.
