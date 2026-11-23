---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the full definition, including what a claim must name and boundary cases such
    as triggers and direct updates. A companion definition covers
  reason: This navigation bullet points to two separate destinations. The first is
    the selection-based learning definition. The second is the single-loop and double-loop
    definition, added as a trailing sentence. Each could stand as its own bullet.
    A reader scanning for the single-loop/double-loop definition will likely miss
    it, because the bullet's lead link names only the first destination.
  level: warn
- scope: passage
  quotes:
  - and Commonplace's declared objective; paired with
  reason: The bullet attaches a second note (reversibility) after a semicolon. Here
    the pairing is defensible because the reversibility note continues the 'how to
    decide when the comparison is open' point. It is borderline rather than a clear
    second idea, but the second link is still hidden at the end of a long item.
  level: info
- scope: passage
  quotes:
  - and the bet stated here is about the comparison, not about how good the proposals
    are.
  reason: The hazard bullet ends with a separate scope statement about what the bet
    covers. That statement explains why weak proposals remain a hazard outside the
    bet, so it reads as elaboration rather than a fully independent claim. It could
    still be split if the scope disclaimer should stand out.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7dd49d5a42f4de5923b4f56a88374fd/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/241375a2730a45b7464ee3da/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: c7dd49d5a42f4de5923b4f56a88374fd
completed-at: '2026-11-22T09:34:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c7dd49d5a42f4de5923b4f56a88374fd/outputs/review-compound-bullet.md
raw-output-sha256: e541f3606550ca54290dae0234c7ba58098c7858b018f646213ee69664815c43
format: 2
---

# Review

## Summary

I checked every bullet and numbered item of roughly 30 words or more. The
two numbered empirical-check items each develop one criterion with a supporting
remark. Four of the hazard bullets each state one hazard with its mechanism.
The "Companion drafts" bullet groups three related drafts under one
explanation, which counts as one idea.

One navigation bullet clearly combines two pointers that could be listed
separately, so the outcome is warn. Two other items have a trailing second
element. Each is closely tied to its lead idea, so both are recorded as info.
