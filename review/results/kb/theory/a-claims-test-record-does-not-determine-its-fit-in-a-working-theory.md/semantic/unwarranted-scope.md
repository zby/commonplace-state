---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: b6a23a58fe6291a871cc12a8dd183c09f9904c44bdd8940e94ff885dd50d8f36
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
outcome: pass
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
  - A claim that has survived every test so far is still a conjecture.
  reason: This supporting claim covers every claim kind the note admits, including
    formal claims tested by derivation. Its support is Popper's account of empirical
    corroboration, which is relative to accepted basic statements. The note gives
    no transfer relation from empirical corroboration to formal derivations or source
    checks. This is a non-central overreach.
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/f4bb83601b693c6db82539c6/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/f4bb83601b693c6db82539c6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/5fe4f6eb46b546179c20385ffc39bbac/outputs/review-unwarranted-scope.md
raw-output-sha256: 436e6020482ae8ad99308b28525d673131dde5c7fb08be92faae0cea6b0beed7
---

# Review

## Summary

**Claimed scope.** Any claim in any working theory: its test record does not fix its fit, and its fit counts as a test only where the claim could have failed.

**Support.** The note offers a conceptual derivation from its own definitions of the three questions, of independence and of fit. It names concrete ways in which test record and fit come apart: irrelevance, redundancy, wrong level or scope, maintenance cost without inferential effect, and fit produced by shared assumptions. It cites Popper for the distinction between truth and corroboration, and for the requirement that corroborating evidence come from attempts to refute.

**Exercised domain.** The derivation holds wherever its definitions apply. The definitions are stated for working theories in general and do not depend on a particular system. The central claim therefore matches its exercised domain. The Scope section also marks what the note does not settle: fit has no single scale, objectives and authority lie outside tests, and the questions are correlated.

The only overreach is in a supporting claim. The "still a conjecture" rule is grounded in Popper's account of empirical corroboration but is applied to every kind of claim the note lists, including formal ones (INFO).
