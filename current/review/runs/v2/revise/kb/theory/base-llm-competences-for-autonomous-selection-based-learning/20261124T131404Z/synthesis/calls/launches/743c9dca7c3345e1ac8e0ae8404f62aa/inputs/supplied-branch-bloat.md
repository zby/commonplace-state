---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 1af422c939fd477db742a5dc2b879315
completed-at: '2026-11-24T13:16:47Z'
findings:
- scope: passage
  quotes:
  - 'Separating them lets a human-assisted bootstrap identify which competence currently
    binds: people temporarily supply the missing semantic step while transfer tests
    check each kind of decision on its own.'
  reason: 'The human-assisted bootstrap procedure is an application of the three-way
    split, not support for it. The preceding sentence already justifies separating
    the competences: they can fail independently. The bootstrap sentence adds a method
    (people supply the missing step; transfer tests check each decision kind) that
    the note does not develop or ground, so it adds attack surface. It is compact
    and plausibly useful. It could be cut to the independence point, or moved to an
    open question or a note about bootstrapping. The best destination is unclear.'
  level: info
contract: verdict
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1af422c939fd477db742a5dc2b879315/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/030f2e6bac785c33f2fc3b6f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1af422c939fd477db742a5dc2b879315/outputs/review.md
raw-output-sha256: 50a769cf5ec5b38eb0c53136ff7fe1dd05cebc3a1b975240430ab444ae405275
---

# Review

## Summary

The main claim is that harness code can take over much of an autonomous selection-based learning loop, which leaves three semantic competences on the frozen base LLM. Almost all of the side material supports that claim where it sits.

- **The three harness bullets and the remark about code-writing LLMs** say what gets offloaded. Without them, the "much of the loop" half of the claim has no content.
- **The criterion-revision paragraph** sets a boundary. It explains why store maintenance and double-loop revision do not add a fourth competence. That protects the count in the title.
- **The independence paragraph** explains why the competences are listed as three rather than one general semantic capacity. Only its last sentence, about the bootstrap procedure, goes beyond what the argument needs. That sentence is recorded as an INFO finding.
- **The harness-evolution ceiling illustration** is stated narrowly and supports the premise that a base-model floor exists even when the store can be updated.
- **The Scope and Open Questions sections** limit the hypothesis and frame what to measure next. They do not open new claims.

No branch competes strongly enough with the main claim to need removal.
