---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:58Z'
findings:
- scope: passage
  quotes:
  - if neural and symbolic components present the same interface, callers don't need
    to know which they're talking to, and refactoring across the boundary becomes
    a local operation
  reason: 'The mechanism is present and constrains the conclusion: if the interface
    differs, callers must change. But the note never says what ''the same interface''
    includes for an LLM caller (name, argument schema, return type, the description
    text shown to the model). That leaves the mechanism somewhat thin, because it
    does not say which interface changes would break the guarantee.'
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/3bff9c17702ac5bf6ac26931/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-explanatory-reach.md
raw-output-sha256: 5925803e2353dcf89643498d09e2577c579d40982e9a76f1634ee6d282631dfb
---

# Review

The central claim is that unified calling conventions enable bidirectional refactoring between neural and symbolic components. The note explains why. When both kinds of component sit behind one interface and are resolved by name, a caller depends only on the name and the interface, so replacing the implementation does not reach the caller.

Varying a premise tests the explanation:

- **Remove interface unification** (separate tool and agent invocation paths). The conclusion changes: each codification step becomes a breaking change, as the note itself says.
- **Remove name-based dispatch** (direct object references). An LLM caller can no longer emit a reference that resolves to either kind, so the conclusion again fails.

The conclusion therefore depends on its premises.

The claim is falsifiable. Swapping an agent for a function under the same name and finding that the invoking prompt or callers had to change would contradict it. The Open Questions section raises real limits (scale, debugging) and does not shield the claim with escape hatches.

The mechanism is thin in one respect, so the result is PASS with INFO: the interface whose sameness carries the argument is not specified.
