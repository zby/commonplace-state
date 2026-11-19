---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: b6a23a58fe6291a871cc12a8dd183c09f9904c44bdd8940e94ff885dd50d8f36
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 5fe4f6eb46b546179c20385ffc39bbac
completed-at: '2026-11-16T17:39:10Z'
findings: []
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/6bb374c66b4af75ff29f41ae/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/6bb374c66b4af75ff29f41ae/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/5fe4f6eb46b546179c20385ffc39bbac/outputs/review-unearned-generality.md
raw-output-sha256: e25ec7d03156a4787627e44b2086dff97f017242826535b757ea970cce055780
---

# Review

## Summary

The central claim is stated in terms of "a claim", "test record" and "a working theory". Candidate concrete stand-ins would be "a KB note" and "a knowledge base". Downgrading to them changes the argument. The mechanism is that fit is relative to a theory's problem while a test record is relative to tests that could refute the claim. That mechanism does not depend on the claim being stored as a note. The note also argues its mechanism across several instance classes under the general term: empirical claims tested by observation, formal claims tested by derivation, and source-derived claims tested against the source. It treats system implementation, vocabulary and neighbouring claims as different things that a claim can be fitted to.

The general wording also forbids more. It rules out treating a claim's helpfulness to the system as evidence of its truth in any working theory, not only a KB, and it rules out retaining a claim solely on its test record. The abstraction sits at the load-bearing site, the claim and the theory, and is not spread across incidental nouns.
