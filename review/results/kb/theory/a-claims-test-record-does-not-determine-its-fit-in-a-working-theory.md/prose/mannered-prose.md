---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 0065be540a2840728201a22a480a5072
completed-at: '2026-11-16T17:36:51Z'
findings:
- scope: passage
  quotes:
  - but it has earned a new independent test
  reason: 'Literal meaning: repeated failures of fit are a reason to give the claim
    a new independent test. ''Earned'' adds deservingness, as though the claim were
    rewarded or penalised, and the note neither means nor supports that. ''But it
    should now get a new independent test'' is at least as clear and drops the connotation.'
  level: warn
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/88ab26ef9571ad5977bb1a56/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/88ab26ef9571ad5977bb1a56/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/0065be540a2840728201a22a480a5072/outputs/review-mannered-prose.md
raw-output-sha256: 6814bb8e4a2156ddfbd0dae79700224adcba750cb92d3484957e6e7802c8b8bf
---

# Review

The note is mostly literal. "Send a claim back for testing" and "locate a defect" are conventional and their connotations match what the note claims. "Agreement of this kind measures the theory's own assumptions" uses "measures" loosely, but it states a real contrast with independent testing and adds no misleading mechanism, so it is not flagged.

One phrase meets the test. "Has earned a new independent test" carries the same deservingness connotation that the gate's own example flags in "earns its keep". A literal phrasing is just as short.
