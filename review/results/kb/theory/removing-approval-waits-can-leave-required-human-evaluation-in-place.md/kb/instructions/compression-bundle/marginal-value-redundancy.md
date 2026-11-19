---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: 6f2678952bd046c08c020059be0ae91c
completed-at: '2026-11-18T16:03:14Z'
findings:
- scope: passage
  quotes:
  - This example establishes a gap against the specification, not that skipping review
    causes harm.
  reason: Defensive redundancy. The opening paragraph already says usefulness or necessity
    is a separate question. The second paragraph already says an unfulfilled requirement
    is 'not by itself evidence that the system would fail or degrade without the task.'
    This sentence makes the same disclaimer a third time and adds nothing new. Cut
    it; the paragraph's point ends at 'would conceal an omitted task.'
  level: warn
- scope: passage
  quotes:
  - This distinguishes human work within the process from optional assessment of its
    results, rather than deciding who deserves causal credit for an improvement.
  reason: The first clause repeats the distinction that the previous sentence ('Optional
    assessment creates neither...') has just drawn. Only the causal-credit contrast
    and the link to the before/after comparison do new work. It may be better to fold
    the contrast into the linking sentence, but it serves as a boundary with the linked
    note, so the reviewer is unsure whether the clause should go.
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/d8a50108ab9c57a1771816ce/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/d8a50108ab9c57a1771816ce/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/6f2678952bd046c08c020059be0ae91c/outputs/review.md
raw-output-sha256: 9b6c4bd4c9db341ce5d31a4fe11243d8892e8b0fc2866b45282ff3c33778a141
---

# Review

## Summary

Most of the note earns its space. The two hypothetical cases make the distinction concrete. The closing paragraph of the first section adds new boundary cases: a non-binding recommendation that still blocks, and human-authored rules applied without a new judgment. "Name the process being automated" adds the subsequent-revision case and lists the kinds of change, which turns the opening claim into a reporting rule. The Scope bullets add boundary cases the body does not cover: anticipated influence and habitual unwritten waits.

The main problem is that the necessity caveat appears several times. The note says a specified task is not evidence of necessity in the lead, in the mechanism paragraph and in the closing sentence about retiring a review. Each of those places has a job. The sentence after the weekly-review example repeats the caveat with no new job. Under this gate's defensive-redundancy rule, it should be cut. A smaller restatement near the start of the third paragraph is flagged INFO as a possible fold.
