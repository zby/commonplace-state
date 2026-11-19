---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The central claim follows largely from the note''s own definitions: fit
    is relative to the theory''s problem and test record is relative to independent
    tests. Its empirical exposure therefore lies in whether the listed counterexample
    kinds actually occur and whether the definitions are useful, rather than in an
    observation that could contradict the claim directly. The mechanism is present
    and hard to vary, but its constraint is mostly conceptual.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/b923f1580efa4cad0db8d48b/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/b923f1580efa4cad0db8d48b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 5fe4f6eb46b546179c20385ffc39bbac
completed-at: '2026-11-16T17:39:10Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/5fe4f6eb46b546179c20385ffc39bbac/outputs/review-explanatory-reach.md
raw-output-sha256: d90117e607dbed2f562a70a57019793d75ce6c5a7f50924490205cc38b0a6669
format: 2
---

# Review

## Summary

The note explains why its central claim holds instead of only recording it. A test record concerns a claim's relation to tests that could have refuted it. Fit concerns what the theory is for: its problem, the scope and level of the decisions it guides, redundancy with other claims, and operational effect. Because the two depend on different inputs, a value on one does not fix the value on the other. The note names concrete ways they come apart: a well-tested claim can be redundant, at the wrong level or irrelevant, and a false claim can fit because neighbouring claims already assume it.

Varying a premise changes the conclusion. If fit were defined as survival of tests, or if tests were allowed to presuppose the theory, the separation would collapse. The note blocks that collapse with an explicit criterion: agreement counts as a test only when the claim could have failed. The statement in Scope that the questions are not statistically independent clarifies the claim and does not protect it from counterexamples, since it concedes a correlation the central claim does not deny. There is no ad-hoc accommodation.
