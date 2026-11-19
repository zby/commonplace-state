---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: The opening paragraph states the automation-claim requirement that the closing
    paragraph of 'Name the process being automated' states again in fuller form. The
    overlap is one sentence, not a whole section, so it does not inflate the section
    count.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/c90bdf108241fb2b354daa27/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/c90bdf108241fb2b354daa27/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: 6fb5b78d26b04bfbbc6f3a9906799888
completed-at: '2026-11-17T13:06:54Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/6fb5b78d26b04bfbbc6f3a9906799888/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 50ac930c74d8847f02dadfeb8424b1d8e70304c1ac06d58c349e85c774c5a417
format: 2
---

# Review

## Summary

The note has an untitled opening and three headed sections: "The same activity can perform different roles", "Name the process being automated" and "Scope". It makes at least three distinct non-obvious claims:

1. A blocking wait, an unfulfilled specified task and optional assessment are different conditions. Removing a wait is not the same as removing a specified evaluation task.
2. Calling an activity evaluation does not tell you which of these roles it plays. Both a non-binding recommendation that execution waits for and human-authored acceptance rules applied by a program show this.
3. A claim that the wider process is automated must separate tasks that are performed automatically from tasks that are no longer required. This includes dependencies that apply to the revision process but not to the earlier adoption, and the point that retiring a review changes requirements rather than automating the review.

The opening states claim 1. Each of the two headed sections develops a different claim. "Scope" gives two boundary conditions: influence that does not create a stop, and a habitual wait with no written rule. Neither is stated elsewhere. Every section adds substance, so the sections do not outnumber the claims plus the support units that need separate treatment.
