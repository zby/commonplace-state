---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 0d803fab7d78498584be07f131ac550c
completed-at: '2026-11-18T16:03:05Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5d480d0ab97ec10bbe86573c/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/5d480d0ab97ec10bbe86573c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/0d803fab7d78498584be07f131ac550c/outputs/review-clause-packing.md
raw-output-sha256: 25bf7ed30b17a97b1550e6aec9ab88c48e31534c929e3b8b5c111149f4ae4654
---

# Review

No body sentence reaches the roughly 40-word threshold with more than two or three independent concepts. The longest candidates were checked for count and distance:

- The opening question ("given a quoted span, a resolved source text and a normalization rule, does the span occur in that text, once or once inside a stated range?") front-loads its three givens before the question, so only one dependency is open at a time.
- "A checksum against a recorded capture, with explicit name pairing between citation and file, binds the compared bytes to that capture" separates subject from verb with one interrupting phrase. That is a single long dependency, which the gate tolerates; the semicolon contrast that follows is short.
- "Judging support is costlier and noisier, so it cannot simply block the way a wording check does, and how reliably it detects out-of-context use is unmeasured" carries three short ideas in sequence without nested dependencies.
- The sentences on current-byte checking, silent fallback and semantic hops each carry two ideas joined by one contrast or consequence.

No sentence needs reordering or splitting under this gate.
