---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A claim of full automation must say which tasks it preserves and which requirements
    it retires.
  reason: '''Preserves'' could mean tasks still performed, now automatically, or tasks
    still assigned to a person. The second reading would conflict with calling the
    process fully automated. The later sentence ''distinguish tasks performed automatically
    from tasks no longer required'' mostly resolves this toward the first reading,
    so the ambiguity is probably not material.'
  level: info
- scope: passage
  quotes:
  - Suppose adoption is automatic, but the process specification assigns a maintainer
    a weekly sample review
  reason: The note does not say whether 'process specification' means only written
    rules or also established expectations that nobody wrote down. The Scope section
    settles the unwritten case for waits but not for non-blocking tasks. An unwritten
    but expected review would count as a retired requirement under the broader reading
    but not under the narrower one. The reviewer cannot show that this changes the
    note's central inference.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 7e280ea5c281cae159c80c9c759469682e1da1250b68065aa914ca6cabedf4ab
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/688592fec124e30cee3decf3/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/artifact/reviews/688592fec124e30cee3decf3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews
launch: eff9412d238b43238712971432930665
completed-at: '2026-11-17T13:08:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/reviews/calls/launches/eff9412d238b43238712971432930665/outputs/review-underspecified-assertions.md
raw-output-sha256: 40e4b766f9891ff8907a07488300a9764907da7982d505761b4329245e6301a7
format: 2
---

# Review

The note's load-bearing assertions are its definitions: an actual wait is a blocking dependency, and a specified task can go undone while execution continues. Its recommendations are that a full-automation claim must name the tasks it preserves and the requirements it retires, and that retiring a review is a change in requirements rather than automation. Its boundaries are that the claim concerns required intervention, not every influence, and that habitual waits count as waits.

The definitions state their criteria: whether execution waits for a person, and whether the specification assigns the task. The worked cases supply the operational consequence of each. The paragraph on subsequent revisions resolves when an optional study turns into a dependency: when a new human assessment is made a condition of each revision.

Two possible ambiguities remain. One is what "preserves" means. The other is whether an unwritten expectation counts as part of the specification. Neither is shown to change the note's truth conditions or recommendation enough to reach WARN.
