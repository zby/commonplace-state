---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The title invites reliance over knowledge bases in general, but the presented
    mechanisms are Commonplace's own. The note's link from that general claim to Commonplace's
    mechanisms is the opening premise that any KB reader alternates between broad
    and narrow views; a derivation from that premise would cover every KB where it
    holds. The premise is asserted, not argued, so the reach to other KBs is gestured
    at rather than articulated. The surplus is also softened by the explicit 'qualitative
    design criterion, not yet a metric' framing and by task-relativity.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
contract: verdict
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
note-sha256: 0519683dd2a2ad488108c956b1c1a59791f57be492893178645772a263c8257f
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/f326720d7f21a2fea0605bdc/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/f326720d7f21a2fea0605bdc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:03Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-unwarranted-scope.md
raw-output-sha256: 6dadc1bace8c1f4d6eb5980b98363098acb21c6e3a4567b81a31252bf02adbe5
format: 2
---

# Review

## Summary

**Claimed scope:** knowledge bases generally should make task-relevant switches between broad and detailed views cheap in both directions.

**Presented support:**

- a derivation from the opening premise that readers alternate between broad and narrow views;
- inherited results from linked notes, namely title-as-claim traversal, the differing metadata needs of search and link-following, pointer trade-offs, and recognition's dependence on co-presence;
- an inventory of Commonplace mechanisms that show the views and transitions concretely.

**Exercised domain:** Commonplace's surfaces, plus whatever the alternation premise covers.

The general scope is carried by the stated premise and the mechanism, not by the Commonplace examples alone. A transfer relation is therefore present, though the premise itself is not argued (INFO). The note also limits its own reliance. It is a qualitative criterion with no metric or threshold, it is relative to the task and the available operations, and its Open questions cover measurement. With these limits, the invited reliance does not clearly exceed what the note supports. No WARN applies.
