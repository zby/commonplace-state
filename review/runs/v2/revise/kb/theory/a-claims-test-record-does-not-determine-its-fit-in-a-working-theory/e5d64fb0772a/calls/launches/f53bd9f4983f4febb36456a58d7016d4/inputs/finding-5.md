---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 5fe4f6eb46b546179c20385ffc39bbac
completed-at: '2026-11-16T17:39:10Z'
findings:
- scope: passage
  quotes:
  - A test is independent when its outcome could have gone against the claim and does
    not presuppose the working theory.
  - What decides is whether the use could have gone against the claim, not where the
    evidence was produced.
  reason: 'The opening defines independence by two joint conditions: the outcome could
    have gone against the claim, and the test does not presuppose the working theory.
    The ''Fit is not an independent test'' section, like the description, then says
    one condition alone decides: whether the use could have gone against the claim.
    A use inside the working theory is the case most likely to presuppose that theory.
    Under the opening definition such a use is excluded even when it could have failed;
    under the later sentence it counts as a test. The definition of the note''s central
    term drifts between sections.'
  level: warn
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/844ec84f19283101752c8f9b/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/844ec84f19283101752c8f9b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/5fe4f6eb46b546179c20385ffc39bbac/outputs/review-internal-consistency.md
raw-output-sha256: 0fa6defe1c5836a1300341e1e1980239af4d34fe7209b282d006b65a1f75de3c
---

# Review

## Summary

Most sections agree with one another:

- The opening says no answer settles another. The Scope says the questions are not statistically independent. The note reconciles these explicitly by distinguishing logical non-determination from correlation.
- The fit definition requires agreement with the other retained claims. The contradiction section allows a well-tested contradicting claim to force revision elsewhere. These are consistent, because the note presents repair as a decision that weighs both standings.
- "Neither may be substituted for the other" is consistent with the earlier sections.

The one inconsistency is the definition of an independent test. The opening gives two conditions. The later section and the description give one, which changes whether use inside the theory can count as an independent test.
