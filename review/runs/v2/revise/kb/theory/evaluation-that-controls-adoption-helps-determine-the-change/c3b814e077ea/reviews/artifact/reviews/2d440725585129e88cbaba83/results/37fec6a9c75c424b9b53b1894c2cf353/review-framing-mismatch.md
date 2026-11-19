---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 32c9c946ad8092a20aa5d4cfe1aa0e58bc5f9bfe61100f236c18efc78f6c479b
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/2d440725585129e88cbaba83/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/2d440725585129e88cbaba83/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: 37fec6a9c75c424b9b53b1894c2cf353
completed-at: '2026-11-17T07:55:08Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/37fec6a9c75c424b9b53b1894c2cf353/outputs/review-framing-mismatch.md
raw-output-sha256: eb873cc36a91e3e808d6523181b036454d899a0a84c42407a65c32a24a17bd21
format: 2
---

# Review

## Summary

The note gives one criterion for a human-evaluation dependency: omitting the evaluation either stops the process in practice or leaves a specified evaluation task undone. Its explanatory sentences frame their claims at the generality of that criterion.

- "Removing the wait automates adoption, not necessarily the wider process" frames the mechanism as being relative to the process, which is what the criterion defines.
- "Execution continuing without a person establishes only the absence of a blocking step" names only the first branch of the criterion, and it does so on purpose, to show that this branch alone is insufficient evidence.
- "What matters is whether the operating process depends on the human activity, not whether the activity is called evaluation" correctly locates the mechanism in dependency rather than in a label, and the next two sentences apply that both ways.
- The Scope bullet on habitual waits fits the "in practice" branch, and it correctly declines to treat such a wait as evidence for the requirement branch.

The worked examples use a maintainer and an agent instruction, but they are explicitly hypothetical illustrations, and the general claim is stated about "a system" and "the process being automated". No framing excludes cases that the mechanism covers.
