---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/structural/compound-bullet.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/structural/compound-bullet.md
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: b1e59a3182a04202a4248788318061b4
completed-at: '2026-11-25T05:25:13Z'
findings:
- scope: passage
  quotes:
  - An unconfirmed conjecture in `kb/log.md` is that thoroughness pressure paired
    with superficial length pressure produces both failures at once
  reason: 'The brevity-pressure bullet, about 150 words long, first makes a sourced
    claim: length pressure makes wording denser without cutting content. It then adds
    a separate, unconfirmed conjecture from the log: thoroughness pressure combined
    with length pressure produces bloat and encoding distortion together. The conjecture
    is a second claim with a different evidential status. It could stand as its own
    bullet, but here it sits after two long quotations, where a reader scanning the
    list is likely to miss it.'
  level: warn
- scope: passage
  quotes:
  - At the code–prose boundary,
  reason: 'The first Current answer bullet pairs the executor-determinability principle
    with a separate code–prose finding: direct access to live source made exact-fact
    documentation copies unnecessary. Both fit the lead-in, which names the executor
    and live source, so the bullet reads as one rule with two applications rather
    than as two unrelated points. Splitting it would make the evidence-backed second
    half easier to scan, but the bullet still works as written.'
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b1e59a3182a04202a4248788318061b4/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/17f9f6f3b4ecfb331fa23dcc/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b1e59a3182a04202a4248788318061b4/outputs/review-compound-bullet.md
raw-output-sha256: c400f18a4f411bb4b0c9f211b228bfe8cb2cc28a0165c9f2211a568fc4254adb
---

# Review

## Summary

Most long bullets develop one point with supporting detail. Examples are the reverse-compression bullet, which backs its claim with rewrite evidence, the cheap-adoption bullet and the agent-additive-bias bullet. The bias bullet's two questions, why the bias exists and how to counter it, are tied together by its own reasoning: different causes call for different countermeasures.

The brevity-pressure bullet in Unsettled is the clear case of a compound bullet. Its sourced finding and its unconfirmed log conjecture are independent claims with different evidential status. The conjecture comes after long verbatim quotations, so a reader scanning the list is likely to miss it. The first Current answer bullet is a milder case, because its lead-in already covers both halves.
