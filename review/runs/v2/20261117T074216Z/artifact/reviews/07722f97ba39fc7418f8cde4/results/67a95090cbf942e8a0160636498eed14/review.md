---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Evaluation required for adoption is part of the operating process
  reason: The title comes close to being true by definition. If the system must wait
    for an evaluation before it adopts a change, that evaluation is already a step
    the process cannot run without, so calling it 'part of the operating process'
    restates the premise. An informed reader could only disagree by using a different
    meaning of 'operating process', for example by placing human gates under governance
    rather than operation. That is a dispute over terms, not a substantive counter-claim.
    The note's contestable points are elsewhere. First, the operating role depends
    on whether the process waits for the activity, not on whether the activity is
    called evaluation. Second, a gate that always approves is still a human stop.
    Third, moving a check after adoption does not remove the dependency when the process
    relies on monitoring and rollback. The title states none of these points.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: dd4b1cefbeff4310b0bcfefd2b787535ac93b72f067610861712e4e1656e62f7
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/07722f97ba39fc7418f8cde4/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/07722f97ba39fc7418f8cde4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: 67a95090cbf942e8a0160636498eed14
completed-at: '2026-11-17T07:42:50Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/67a95090cbf942e8a0160636498eed14/outputs/review.md
raw-output-sha256: eeb0ae575c3ea7cc159f2ab90b96bd753eeab4e1d3a43dfbdd1a79744402f329
format: 2
---

# Review

## Summary

The title is phrased as a claim, but it only weakly passes the test of whether an informed person could argue the opposite. "Required for adoption" already means the process cannot proceed without the evaluation. Saying that such an evaluation "is part of the operating process" therefore mostly repeats that meaning.

## Where the contestable content lies

The body makes points that someone could dispute:

- The same activity can block the process or merely assess its results. What counts is whether the process depends on the activity, not what the activity is called. For example, a non-binding recommendation still creates a dependency if the agent must wait for it.
- An approval step that always says yes is still a human stop. Observing routine approvals does not show that the step can be removed.
- Moving a check after adoption does not remove the human dependency if continued operation relies on monitoring and rollback.

These claims argue against a common practice: describing a system as self-improving when a human gate or required monitoring remains. Sharpening the title toward one of them would give it the claim strength the body already supports. One possible title is "Whether human evaluation blocks the process, not its name, determines whether automation depends on it." The criterion also allows a topical title, since the note presents itself as drawing a distinction ("Distinguishes human evaluation needed for a system to proceed from assessment that only measures its results").

## Why warn rather than fail

Unlike the criterion's fail examples, the title is not empty. It rules out the position that human evaluation sits outside the system and is only oversight, which some accounts of autonomous improvement take. Its weakness is closeness to a definition, not complete vacuity.
