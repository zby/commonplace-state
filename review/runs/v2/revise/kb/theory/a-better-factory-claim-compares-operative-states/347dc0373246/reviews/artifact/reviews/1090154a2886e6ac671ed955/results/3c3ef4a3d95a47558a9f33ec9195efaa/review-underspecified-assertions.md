---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '**exceed a specified target** on at least one named production dimension'
  reason: Two readings fit. (a) The target is a margin over the predecessor's level,
    so the successor must outperform the predecessor on that dimension. (b) The target
    is an absolute level declared in advance, so the successor passes if it clears
    it even when the predecessor already did. The unresolved choice is the comparison
    baseline. Under (b), a successor identical to the predecessor on every dimension
    passes a 'better-factory' comparison when the predecessor already met the target.
    Under (a), it fails. The choice changes when the claim is true and whether passing
    establishes improvement at all.
  level: warn
- scope: passage
  quotes:
  - just not this audit-proof one
  reason: '''Audit-proof'' could mean robust under audit, which is the intended reading
    given the opening''s ''auditable'', or shielded from audit. Context favours the
    first reading, so the ambiguity is probably immaterial.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/1090154a2886e6ac671ed955/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/1090154a2886e6ac671ed955/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 3c3ef4a3d95a47558a9f33ec9195efaa
completed-at: '2026-11-16T22:00:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/3c3ef4a3d95a47558a9f33ec9195efaa/outputs/review-underspecified-assertions.md
raw-output-sha256: b86d2b1a38c174abba76e7437bc9e5fba15720606ae35451f954e3779b361ed1
format: 2
---

# Review

## Summary

Most load-bearing assertions are resolved in context.

- **Predecessor's prior scope.** The note glosses it as "what that state could already do". The open question about specifying it for open-ended families is flagged honestly as unresolved.
- **The two routes.** Each is defined by where the evaluation sits on the causal path.
- **Learner boundary versus evaluator location.** The note says what each declares.

**Target component.** The second component of the assessment relation leaves its baseline unstated. That choice decides whether passing the comparison implies the successor is better than the predecessor, which is the note's own claim; see the warning finding.
