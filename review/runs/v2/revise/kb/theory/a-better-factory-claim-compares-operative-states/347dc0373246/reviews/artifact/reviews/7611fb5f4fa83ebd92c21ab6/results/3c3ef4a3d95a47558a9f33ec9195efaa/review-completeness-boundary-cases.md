---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Four declarations make a better-factory claim determinate
  reason: 'The four-declaration list (compared states, relation, successor route,
    evaluator location) is presented as sufficient for determinacy, but the operative
    successor is defined through the linked operative-change definition, which is
    horizon-relative. A successor installed, measured and rolled back shortly after
    strains the list: whether it counts as the operative successor depends on a horizon
    the four declarations do not name. The note''s own text also invokes a ''declared
    family'' and a learner boundary as further declarations. Coverage is possible
    if these are read into the existing four, but the mapping is strained.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/7611fb5f4fa83ebd92c21ab6/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/7611fb5f4fa83ebd92c21ab6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 3c3ef4a3d95a47558a9f33ec9195efaa
completed-at: '2026-11-16T22:00:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/3c3ef4a3d95a47558a9f33ec9195efaa/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 1cd31887d0cd3bb85c8d0d34d02f0299de45991b273fc074968b8f38c0dc0557
format: 2
---

# Review

## Summary

The note builds three frameworks: the four declarations, the two routes to a successor, and the two-part assessment relation. I tested each against boundary cases.

- **Simplest instance.** One retained change, measured after installation. This maps cleanly onto measurement over snapshots, which explicitly allows "a single retained change".
- **Mixed route.** A candidate is staged, admitted, then measured again after installation. The Scope section says the routes are a reading of an episode rather than a partition of processes, so the case is covered by declaration.
- **Candidate never depended on.** A candidate passes staging but is never used. The operative-successor definition excludes it, so it is covered.
- **Empty prior scope.** A first factory has no predecessor capability. Non-regression is vacuous and the target component carries the claim, which is consistent with the framework.
- **Retirement of prior capability.** A successor deliberately drops an unsafe capability. The Scope section covers this as an alternative declarable relation.
- **Short-lived successor.** A successor is installed and then rolled back. This strains the four-declaration list because operativity depends on a horizon the list does not name; see the finding.

The frameworks hold at their stated boundaries. The only strain is the claim that exactly four declarations make the comparison determinate.
