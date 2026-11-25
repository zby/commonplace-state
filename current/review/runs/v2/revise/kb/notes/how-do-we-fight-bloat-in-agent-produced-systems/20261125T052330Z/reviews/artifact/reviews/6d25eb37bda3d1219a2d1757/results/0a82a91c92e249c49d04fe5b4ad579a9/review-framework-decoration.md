---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Bloat in these mixed systems compounds through three channels:'
  reason: The three-channel taxonomy (context and routing cost, maintenance and drift
    load, recursive exposure) is never named again in Current answer or Unsettled.
    Each channel still states a distinct causal mechanism, and the channels jointly
    justify why the query stays open, so the list is not decorative. It does, however,
    introduce categories that the rest of the argument does not explicitly use.
  level: info
- scope: passage
  quotes:
  - five partial mechanisms across prose, structure, and the code–prose boundary
  reason: The three domains (prose, structure, code–prose boundary) are not used to
    organize or classify the five mechanisms that follow. The framing is harmless,
    but it does no work beyond the bullets.
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0a82a91c92e249c49d04fe5b4ad579a9/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/6d25eb37bda3d1219a2d1757/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 0a82a91c92e249c49d04fe5b4ad579a9
completed-at: '2026-11-25T05:24:27Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0a82a91c92e249c49d04fe5b4ad579a9/outputs/review-framework-decoration.md
raw-output-sha256: 45710d75951612b0ba553ba19eb628f89ce86fa63f1d55f72d4c4f5d3abbb5ae
format: 2
---

# Review

## Summary

The note has no tables, notation or equations. Its structures are bulleted lists: the three cost channels, the five current mechanisms and the six unsettled problems.

The mechanism and unsettled lists are load-bearing. Each item names a distinct mechanism, gives its warrant or failure condition, and cites separate evidence. One sentence could not replace either list without losing decision-relevant distinctions.

The three-channel taxonomy in Stakes carries distinct mechanisms: attention cost, reconciliation cost and recursive anchoring. The later sections do not refer back to it, so it slightly over-structures the motivation. That is a minor issue, not a decorative framework. The domain triple in the Current answer lead-in also has no further role. Both are recorded as info.
