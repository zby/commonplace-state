---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - harness code can supply much of an autonomous selection-based learning loop, leaving
    three conjectured semantic competences on the frozen base LLM
  reason: '''Frozen'' does little visible work in the argument. The offloading mechanism
    and the semantic-relocation argument would place the same three competences on
    a model whose weights also change. Freezing matters mainly to the ''base-model
    floor'' framing: the competences must already be present, not learned. Whether
    that boundary is load-bearing is unclear.'
  level: info
- scope: document
  quotes: []
  reason: The claim is scoped to LLMs. The relocation argument might apply to any
    fixed semantic processor, but the note is plainly about LLM harnesses, so this
    is intentional domain scoping.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: 65eb6e50ebf86671e73830336dd77216ac6bc4d37b1e89d6318d431fed96442b
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/53f391d66a56fae2d2cce319/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: cccda05d8a25440b842c04af9c04b834
completed-at: '2026-11-24T13:17:58Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: 82c932e5b185fffab158b070b0fef96b6254f1364ee24860487d1110859c9e4a
format: 2
---

# Review

## Summary

The main qualifiers do work. "Autonomous" matters because the note contrasts it with a human-assisted bootstrap in which people supply the missing semantic step. Without autonomy, nothing forces the competences onto the model. "Open-ended work," where new failure modes keep arriving, is what keeps semantic work from being codified away. "Selection-based learning" maps onto competences 2 (proposal) and 3 (selection). "Harness code" names the offloading channel. "Frozen" is the only qualifier whose load is unclear, and it may protect the floor framing. No qualifier clearly narrows the central claim without support.
