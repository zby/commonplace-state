---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews
launch: 56a8a531464847629382b1e7312d9dd8
completed-at: '2026-11-17T13:16:03Z'
findings:
- scope: passage
  quotes:
  - This distinguishes human work within the process from optional assessment of its
    results, rather than deciding who deserves causal credit for an improvement.
  reason: This positioning paragraph sits between the claim and the examples that
    carry it. It reframes the distinction as work versus optional assessment, rules
    out a question about causal credit that the reader has not raised, and links to
    a neighbouring note. The core claim stays findable, but this related-note material
    delays the cases. Folding the link into the Optional assessment case or a closing
    line would keep the opening focused on the wait-versus-task distinction.
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/b2eb42bef99857e31130bb0e/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/artifact/reviews/b2eb42bef99857e31130bb0e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/reviews/calls/launches/56a8a531464847629382b1e7312d9dd8/outputs/review.md
raw-output-sha256: 649a12832b47fcd876adc440e15607f154ed3ff1515e27e9b1086f8ae505e4e3
---

# Review

## Summary

The core claim is easy to find. The note opens with it and keeps later material in support of it.

Restated in one sentence: removing a human approval wait differs from removing a specified human evaluation task, so a claim of full automation must say which required tasks remain and which were retired. The title states the first half. The opening sentence states it plainly, and the third sentence of the opening paragraph states the consequence for automation claims. The second paragraph defines the two terms needed (blocking dependency versus unfulfilled requirement). "The same activity can perform different roles" illustrates the distinction with two cases. "Name the process being automated" applies it to the automation claim. Scope bounds it. Each section serves the opening claim.

The one shape issue is minor. The third opening paragraph places scoping and related-note material before the examples. Its contrast with "optional assessment" also introduces a third category early, which the frontmatter description also foregrounds. This makes the claim slightly less memorable, but it does not hide it, so this is INFO rather than WARN.
