---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The initial human scaffolding must serve as a launchpad that computation comes
    to supply and revise, not a permanent ceiling of hand-crafted rules.
  reason: 'Intended meaning: the hand-written instructions, types and gates are only
    a starting point, and automated learning must come to produce and revise their
    content instead of leaving them as a fixed upper limit. ''Launchpad'' suggests
    something left behind once the launch is over, but the sentence itself says computation
    will ''supply and revise'' the scaffolding rather than leave it. The image therefore
    conflicts with the literal claim and makes the reader reconcile the two. The previous
    sentence already states the condition literally (''only if automated learning
    outgrows that starting point''). Literal replacement: ''The initial hand-written
    scaffolding must be a starting point whose content automated learning comes to
    supply and revise, not a permanent limit set by hand-crafted rules.'' This removes
    the contradictory implication that the scaffolding is discarded.'
  level: warn
outcome: warn
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/2301a99d229fa8469e715284/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: e6c44a5d053c40b889fc04e430cca4c7
completed-at: '2026-11-21T19:26:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/outputs/review-mannered-prose.md
raw-output-sha256: ec4f6294fef091199b6de3d4fa6c4cb3910347d383cb21e53089c9161c6305a2
format: 2
---

# Review

## Summary

The article mostly uses literal or conventional wording. I checked the
following and kept them:

- "judge slot" is precise shorthand for a role the article defines.
- "sits on the computation side of the Bitter Lesson" uses a mapping the
  section explains.
- "belong on the ledger" is a conventional accounting idiom.
- "hard-oracle extreme" names an end of a spectrum the section lays out.
- "throwback" and "invert the order of proof" are familiar idioms whose
  meaning is clear in context.

One local instance meets the test: "launchpad". Its implication that the
scaffolding is left behind conflicts with the sentence's own literal clause
("supply and revise"). The literal form is at least as clear. This is a single
instance, not a pervasive pattern, so the outcome is WARN.
