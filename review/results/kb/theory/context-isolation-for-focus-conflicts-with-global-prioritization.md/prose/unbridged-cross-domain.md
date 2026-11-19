---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 3d6f8665a9b04e2c816a2b4805122f0c
completed-at: '2026-11-19T13:26:47Z'
findings: []
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/740e88bba3f753ddffef62e2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 2872e4fe5afdee96d69524a28905a09d1bee6a824d5ae7ee6706868b8ec12299
---

# Review

## Summary

The note's only cited empirical material is the practitioner account of coding
agents, together with the Anthropic write-up quoted within it. The argument's
domain is agent systems under bounded context generally. Coding agents are a
subset of that domain, not a separate domain, and the note does not use the
account as evidence that transfers to other kinds of agents:

- It says the account "motivated this analysis".
- It names a confound the account cannot resolve: worker behavior versus a
  workflow that pings on every stop.
- The Scope section says that neither the account nor the Commonplace
  mechanisms provide a controlled comparison. The footer labels the source
  "origin, not corroboration".

The claim rests on a structural argument about which information is present in
a bounded window, not on transferred results.

The comparison between a human specialist and a stateless agent is a contrast
that explains why the failure arises in agents. It does not import a finding
from human cognition. The babysitting image belongs to the quoted source and is
not offered as a mechanism the note relies on.
