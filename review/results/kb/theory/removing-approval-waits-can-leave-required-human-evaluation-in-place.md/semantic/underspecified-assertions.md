---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: d155a6ea644e43e9abfa39b7f9c0a531
completed-at: '2026-11-18T16:03:42Z'
findings:
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: '''Preserves'' could mean the tasks kept as human work, or the tasks whose
    function is kept by any means, including automated replacement. Taken alone, the
    two readings set different reporting obligations. The later paragraph resolves
    this by requiring the account to say ''what work still requires a person and what
    changed'' and listing moved, automated, replaced and retired checks. The ambiguity
    is therefore resolved in context and is not material.'
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/4792ef4bd86bd2a6428b9c0a/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/4792ef4bd86bd2a6428b9c0a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/d155a6ea644e43e9abfa39b7f9c0a531/outputs/review-underspecified-assertions.md
raw-output-sha256: 5a9a6415e63dd3454dbda5387a7e640a857ea4af0ce402ffcdfa302485dc4053
---

# Review

## Summary

The load-bearing assertions are the opening distinction, the definitions of actual wait, unfulfilled requirement and optional assessment, the classification of the two cases, the weekly-review gap, the revision-dependency rule, the reporting obligation, and the Scope boundaries. Each one names its mechanism (execution waits, or the specification assigns the task) and its scope (adoption versus the wider process including monitoring and revision).

The note supplies the clarifications that would otherwise be missing:

- It states which process a full-automation claim concerns: "A claim about automated adoption alone need not include monitoring or revision."
- It says what the weekly-review example establishes: a gap against the specification, not harm.
- It says what turns an optional study into a revision dependency: "Making a new human assessment a condition of each revision does."

The only candidate ambiguity, "preserves", is resolved by the nearby context and recorded as INFO.
