---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/structural/compound-bullet.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/review-gates/structural/compound-bullet.md
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 326e79289f244bd5adc1f6080d20368b
completed-at: '2026-11-19T13:27:11Z'
findings:
- scope: passage
  quotes:
  - The account reports equally demanding interruptions; it does not isolate whether
    worker behavior or a workflow that turns every stop into an immediate ping made
    interruption the default.
  reason: 'The uncalibrated-escalation bullet states the failure mode and gives its
    quoted evidence. It then ends with a separate evidential caveat: the source cannot
    tell worker behavior apart from a workflow that pings on every stop. That caveat
    could stand as its own claim, and it comes after two long quotations, where a
    scanning reader may miss it. It does qualify the bullet''s own evidence, though,
    and it mirrors the preceding paragraph''s point about defaults, so it reads as
    bounded elaboration rather than a buried second point.'
  level: info
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/326e79289f244bd5adc1f6080d20368b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/de2f984a811e980298fa6449/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/326e79289f244bd5adc1f6080d20368b/outputs/review-compound-bullet.md
raw-output-sha256: 7bd22847dc2c451779fd3cedf5f93f42cb35b649ac41a0b327d2ade30eedbffd
---

# Review

I checked each body bullet longer than about 30 words.

- The **earnest low-value tangents** and **local over-specification** bullets each state one mechanism and give supporting evidence or a link.
- In the two-view split, numbered item 1 describes the narrow-deep execution role. It covers what the worker receives and what it returns, which are two sides of one role. Item 2 describes the wide-shallow triage role in the same way.
- The three illustration bullets each name one mechanism and what it separates. The ADR 138 bullet lists the three unbundled decisions as elaboration of one example.
- The residual-friction bullets each give one friction and its mechanism.
- Each Scope bullet states one boundary. Some add its contrapositive ("On a small, single-thread task...") or a contrasting non-case ("Purely intrinsic local checks..."). In each case the addition explains the same boundary rather than making an independent point.
- The Relevant Notes bullets are a link, a relation label and a single gloss each.

Only the uncalibrated-escalation bullet comes close to the failure mode. The finding above records it at info level only.
