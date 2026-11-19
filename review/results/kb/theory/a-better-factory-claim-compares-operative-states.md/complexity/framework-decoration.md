---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: b782e79a95b2475dbf75ec62dfa4555d
completed-at: '2026-11-18T00:18:26Z'
findings:
- scope: passage
  quotes:
  - Three terms keep the comparison's endpoints straight.
  reason: 'The three-term vocabulary (predecessor, candidate, operative successor)
    is close to sentence-sized, but every term is used later: candidate drives the
    construction-event exclusion and the staging-evidence distinction, while predecessor
    and successor anchor the relation. It is load-bearing, if lightly formalized.'
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/c666018fa46ef3beb8b2e1c4/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/c666018fa46ef3beb8b2e1c4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/b782e79a95b2475dbf75ec62dfa4555d/outputs/review-framework-decoration.md
raw-output-sha256: ee2078a31baf7e7c5882785966d531ffcf890708a5013a37543d44053a824206
---

# Review

## Summary

The note uses three structures. I checked each one by deleting it and rereading the passage.

- **Predecessor / candidate / operative successor.** Each term does work. Candidate exclusion supports the inference that a better-factory claim cannot be read off a construction event. The operative-successor definition carries the installed-and-depended-on condition and the measurement-boundary variant. One sentence could carry the distinctions, but the structure adds no vocabulary that the argument leaves unused. Recorded as info.
- **Two-component relation (non-regression plus declared improvement).** This is load-bearing. Non-regression scope drives the factory-development preservation consequence. The Scope section uses the two-component shape to say when that consequence stops following, namely relations that permit capability retirement.
- **Retention without improvement / improvement without learning / learning.** These are discriminative cases. Each separates claims that the note says are independent. The third case supports the inference that learning needs causal-contribution evidence from a with/without contrast. No case goes unused.

The note contains no notation or equations. No structure fails the test.
