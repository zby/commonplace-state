---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 7c0e6973430767ada1017279b0e9567ecaf500f2a7ed8b3bee8ed0f57ac7594d
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/d6e4371b023e06b4202ebcfd/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/artifact/reviews/d6e4371b023e06b4202ebcfd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews
launch: c241a278060046ea9c226fc96c458dd9
completed-at: '2026-11-18T16:02:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/reviews/calls/launches/c241a278060046ea9c226fc96c458dd9/outputs/review.md
raw-output-sha256: ac8c627b2b0963a6c8a743ec4508de7a5ca3e10056d2d01187faffb8af2ea0a7
format: 2
---

# Review

## Summary

The main claim is that removing a human approval wait differs from removing a specified evaluation task. A claim of full automation must therefore say which tasks it keeps and which requirements it retires. Optional assessment is neither a wait nor a requirement. No part of the note works as a branch that competes with this claim.

## Side material checked

- **Comparison with the factory-claim note.** This paragraph sets a boundary. It separates the distinction from questions of causal credit and from judgments that the system improved. That limits how far the claim reaches, so it stays.
- **Non-binding recommendation and human-authored acceptance rules.** These two contrasts say what makes an activity a dependency: execution waiting for it, not the label "evaluation." They are boundary cases for the central distinction.
- **Subsequent revisions.** This paragraph applies the same wait/requirement distinction to the revision process. The opening paragraph already commits to "monitoring or later revision decisions," so this is part of the stated argument, not an extension.
- **Ways a check can change.** The list of ways a check can change (moved, automated, replaced, retired) is what the note asks a full-automation claim to state. Retiring a review "is a change in requirements, not automation of that review." This directly supports the main claim.
- **Scope bullets.** Both bullets set boundaries. Anticipated influence is not a stop. A habitual wait is a real wait but does not show a requirement. Each one prevents a likely overextension of the claim.

None of these needs a different kind of evidence or introduces a separate hypothesis, analogy or prediction. Each one sets up the main argument, supplies a premise or sets a boundary, so nothing should be removed, demoted or moved elsewhere.
