---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Separating them lets a human-assisted bootstrap identify which competence currently
    binds: people temporarily supply the missing semantic step while transfer tests
    check each kind of decision on its own.'
  reason: 'The bootstrap procedure is a practical use of the split, not support for
    it. The preceding two sentences already justify separating the competences by
    showing that they fail independently. The bootstrap sentence adds an operational
    method with its own claims (people can supply the missing step; transfer tests
    can isolate each decision kind) that would need separate evidence. It is compact
    and shows why the split matters to a builder, so it is not a clear removal. Its
    better home is unclear: possibly the first open question, or a separate note on
    bootstrapping an autonomous loop.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/9f5c8879202f4849902675196efd1047/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/030f2e6bac785c33f2fc3b6f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 9f5c8879202f4849902675196efd1047
completed-at: '2026-11-24T13:16:47Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/9f5c8879202f4849902675196efd1047/outputs/review.md
raw-output-sha256: e39dee9ac785d116f377b52f82316f7bd3392dbe1cace2be92949f521980d681
format: 2
---

# Review

## Summary

The main claim is that harness code can take over much of an autonomous selection-based learning loop, leaving three semantic competences on the frozen base LLM. Most side material directly supports it.

- The three bullets on enforcement, evidence capture and store bookkeeping set up the claim by naming what harness code offloads.
- The paragraph on store-level maintenance and criterion revision is a boundary condition. It explains why these do not form a fourth competence, which the note needs if it claims there are exactly three.
- The independent-failure paragraph supports treating the competences as distinct rather than as one capability.
- The Harness Evolution illustration is bounded evidence for a base-model floor, and the note scopes it as one benchmark and loop.
- The Scope section and Open Questions limit the hypothesis; they do not branch from it.

One sentence is a mild branch. The human-assisted bootstrap is a downstream use of the split, not a premise for it. It is short and gives the split practical weight, so it can stay for now. If the note grows, it is the first candidate to demote into an open question or move to a separate note.
