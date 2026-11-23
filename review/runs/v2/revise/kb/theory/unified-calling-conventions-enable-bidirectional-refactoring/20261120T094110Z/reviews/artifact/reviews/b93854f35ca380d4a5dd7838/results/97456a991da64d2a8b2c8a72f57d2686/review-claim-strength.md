---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: a5d6bbe51674a1b1da0fe05d349fd8079e8ed28089a3aac0f9a2502b70c4d8e3
criterion-sha256: 8e4666d11f54dfcb2ef8de2c1942bb8fa7d77bd1fb54fec00bb5794bf4642367
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/b93854f35ca380d4a5dd7838/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 97456a991da64d2a8b2c8a72f57d2686
completed-at: '2026-11-20T09:41:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/outputs/review-claim-strength.md
raw-output-sha256: a31db2761dd36951d752f1dd67f7d31a8e8473a368f585c6f420282ab9fd8f65
format: 2
---

# Review

## Summary

The title "Unified calling conventions enable bidirectional refactoring between neural and symbolic" makes a contestable claim. An informed practitioner could argue the opposite: matching a call signature does not make an LLM-backed component and a Python function interchangeable. Nondeterminism, cost, latency and failure modes differ, so swapping implementations behind one name might still force changes at call sites or in callers' error handling. Someone could also argue that the main barrier to moving the boundary is behavioural equivalence, not interface shape. Because a knowledgeable reader could dispute the title, it is not a truism.

The claim also goes beyond the familiar point that a stable interface hides its implementation. It says that a shared convention makes movement possible in both directions (codifying and relaxing) and makes each move a local operation. That is the non-obvious point the note sets out to establish.
