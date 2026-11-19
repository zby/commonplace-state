---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
findings:
- scope: passage
  quotes:
  - is the state that is installed and that later production and factory development
    depend on
  reason: A partial or staged rollout (a canary installed for a fraction of production,
    or a successor installed on some family members but not others) sits between candidate
    and operative successor. The stated criterion — installed and depended on — can
    classify it, but only by choosing a measurement boundary the note mentions solely
    for continuously revised systems. Coverage is possible but strained.
  level: info
- scope: passage
  quotes:
  - is the factory state current when the comparison is declared
  reason: The simplest instance, the first installation of a factory, has no predecessor
    state with prior capabilities. The framework appears to exclude it from better-factory
    claims, which is reasonable, but the note does not say so. Non-regression would
    then be vacuous rather than inapplicable.
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b5d2e1578a2e7bf5a51034dd/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b5d2e1578a2e7bf5a51034dd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 931830f35ef859381d31d28fb539d3561ee3656cb029d1bcaf18a214c7140a78
---

# Review

The note builds three small frameworks: a three-term vocabulary for the comparison's endpoints (predecessor, candidate, operative successor); a two-component assessment relation (non-regression plus a declared improvement); and a three-case contrast (retention without improvement, improvement without learning, learning).

Boundary cases tested:

- **Continuously revised system.** This case is handled explicitly: the successor is the operative state at a named measurement boundary.
- **Installed then rolled back.** The linked operative-change definition counts a change as operative while it holds. The successor at the measurement boundary maps cleanly.
- **Deliberate retirement of capability.** Non-regression would fail this case. The Scope section handles it explicitly as an alternative declarable relation.
- **Improvement solely in cost or latency.** This maps to "at least one named production dimension".
- **Change that improves only against a different objective.** The note handles this explicitly: it need not pass the declared comparison.
- **Experience-derived change bundled with other changes.** The learning case defers to the experimental-contrast requirement, which covers this.
- **Staged or partial rollout, and first-ever factory.** Each maps only with strain; recorded as INFO.

The three-case contrast is not meant to be exhaustive. It separates three claims, and its length fits that role. No case clearly falls outside the claimed coverage.
