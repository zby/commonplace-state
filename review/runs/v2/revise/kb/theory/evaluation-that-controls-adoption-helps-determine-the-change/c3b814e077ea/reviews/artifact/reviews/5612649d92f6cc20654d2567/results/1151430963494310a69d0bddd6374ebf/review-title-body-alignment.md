---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Besides supporting the title''s claim, the body spends much of its length
    on a criterion: human activity is an operating dependency when omitting it blocks
    the process or leaves a required task undone, and is optional assessment otherwise.
    The title covers the consequence (required evaluation can remain after the wait
    is removed) but not this criterion. That is acceptable compression, not drift;
    if the title is revised, it could signal the required-versus-optional distinction.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 659f02d5e20334786517749c67b3273fe4d42cb5cd154819bf1efc3e855776c6
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/5612649d92f6cc20654d2567/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/5612649d92f6cc20654d2567/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: 1151430963494310a69d0bddd6374ebf
completed-at: '2026-11-17T07:54:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/1151430963494310a69d0bddd6374ebf/outputs/review-title-body-alignment.md
raw-output-sha256: adef84975ec65c0c645f3ecdb850d92f7faa5d02cc04d674fccde558c62e9bb2
format: 2
---

# Review

## Summary

The body supports the H1 claim directly. The opening states that a system adopting changes without approval "can still require human evaluation to monitor those changes or decide subsequent revisions". The "Name the process being automated" section gives a concrete case: a weekly sample review and rollback remain required after automatic adoption. The scope matches. The title says "can leave", and the body likewise treats the remaining requirement as possible, depending on the process's stated requirements, not inevitable.

The required-approval and optional-assessment cases, and the Scope list, develop the criterion that tells required evaluation from optional assessment. This is the supporting mechanism for the title's "required", not a different claim. The finding above is informational. The filename slug differs from the H1, but under this gate the slug is not tested.
