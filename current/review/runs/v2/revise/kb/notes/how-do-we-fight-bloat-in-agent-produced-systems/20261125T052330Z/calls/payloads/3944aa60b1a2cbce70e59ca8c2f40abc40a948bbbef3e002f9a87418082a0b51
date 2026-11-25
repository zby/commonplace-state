---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 8db905baf3094b5185b9d357cb80ec16
completed-at: '2026-11-25T05:26:40Z'
findings:
- scope: passage
  quotes:
  - cutting six candidate pages by 53 percent and retiring two
  reason: 'The evidence summary leaves the population relation open. Reading (a):
    the 53 percent reduction covers six pages, one of which was retired, plus one
    further retired page, for seven in total. Reading (b): six pages were cut by 53
    percent and two further pages were retired outright, implying eight pages and
    a larger effect. The sentence does not say whether the retired pages are inside
    the six. The choice changes the size of the evidence for source access eliminating
    exact-fact prose; reading (b) overstates the reduction relative to (a).'
  level: warn
- scope: passage
  quotes:
  - keeps both code and natural-language bloat bounded under sustained autonomous
    production
  reason: The retirement condition does not say what 'bounded' is measured against,
    such as artifact count, context cost, maintenance backlog or a declared quality
    bound, or over what timeframe 'sustained' holds. Different choices would change
    when the query retires. The open Unsettled bullet on separating useful redundancy
    from bloat partly explains why no measure is given, so the ambiguity is acknowledged
    rather than hidden.
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/c8b484481c9ffd89e9bddf99/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/outputs/review-underspecified-assertions.md
raw-output-sha256: 4c0c89addf9f5291593b86d9bcae49faf1a6c50991d56f9552c3a6c8d552b0dd
---

# Review

## Summary

Most load-bearing assertions resolve their mechanism in context. The three cost channels each state their causal route. Each Current-answer bullet names the mechanism its linked note supplies. The Unsettled bullets state what is missing rather than asserting a settled claim. The additive-bias bullet's heading ("biased toward adding") settles that the comparison is against what would be appropriate, not a raw count of additions.

One evidence summary is materially ambiguous: "cutting six candidate pages by 53 percent and retiring two" can be read as seven or eight pages, which changes how large the reported reduction is. The retirement condition's "bounded" lacks a measure, but the note openly treats that measure as an unsettled problem, so it is reported as INFO.
