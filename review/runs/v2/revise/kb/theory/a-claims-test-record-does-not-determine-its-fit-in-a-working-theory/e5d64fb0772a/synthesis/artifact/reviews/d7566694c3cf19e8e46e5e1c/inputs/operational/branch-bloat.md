---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 3d0e9350e5af46b088f1dc00bb0c49bb
completed-at: '2026-11-16T17:37:47Z'
findings:
- scope: passage
  quotes:
  - When a well-tested new claim contradicts the working theory, logic says only that
    the claims cannot all be kept.
  reason: 'The contradiction section develops a related mechanism: a contradiction
    does not settle which claim to give up. That mechanism needs its own grounding,
    and the note does not cite one for it. It partly supports the title, because it
    shows that a good test record does not decide what the theory keeps. But the main
    claim stands without it: the three standings are separate, and agreement counts
    as a test only where the claim could have failed. The section adds attack surface
    and could be compressed to one sentence in ''The two kinds of evidence inform
    each other'' or rehomed as its own note. Its best destination is unclear, so this
    is INFO.'
  level: info
- scope: passage
  quotes:
  - This note uses "test record" where it earlier used "warrant".
  reason: This terminology-history paragraph is side material about the note's revision,
    not about its claim. Its one useful clause, that truth and support must be kept
    apart, is already made by the definitions above it and by the next section. This
    is mainly a change-history matter, at the edge of this gate's lens, so it is recorded
    as INFO rather than WARN.
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/20312f9b48c5e93b34cd58e1/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/20312f9b48c5e93b34cd58e1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/3d0e9350e5af46b088f1dc00bb0c49bb/outputs/review.md
raw-output-sha256: c291c494fddc24c25aee018159d81970e181ee04f45ac6f2d7a6d27ca30954bb
---

# Review

## Summary

The main claim is that truth, test record and fit are separate standings, and that fit counts as an independent test only where the claim could have failed. Most of the side material directly strengthens that claim:

- The truth-versus-record section and the fit-is-not-a-test section are the core argument.
- "The two kinds of evidence inform each other" is a concession and boundary. It stops readers from concluding that fit and testing are unrelated.
- The Scope bullets are boundary conditions. The last one explicitly blocks the reading that the standings are statistically independent.

Two passages are weaker:

- **The contradiction section** is a separate mechanism. It is about underdetermined repair, not the separation of the three standings. It could be shortened into the preceding section or rehomed.
- **The paragraph about the earlier "warrant" wording** is revision history inside the note body.

Neither passage obscures the central point enough to require action, so the result is PASS with INFO findings.
