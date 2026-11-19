---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 1fcb6fe423b6419ba77c67a498edd3eb
completed-at: '2026-11-16T17:38:18Z'
findings:
- scope: passage
  quotes:
  - 'A claim fits a working theory when the theory handles its problem better with
    the claim than without it: the claim is relevant to that problem, is stated at
    the scope and level the theory''s decisions need, agrees with the other retained
    claims, and changes explanation, prediction, search or modification when used.'
  reason: About 50 words with a definition followed by four coordinated conditions.
    The colon-and-list structure keeps it readable, so it is not overloaded, but it
    is the densest sentence in the note. If it grows further, end the definition at
    the colon and give the four conditions as their own sentence.
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/e9542d561da1aef274e373cf/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/e9542d561da1aef274e373cf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/1fcb6fe423b6419ba77c67a498edd3eb/outputs/review-clause-packing.md
raw-output-sha256: c2cbabd4583d014ceece2af632c62017aacf6acdd08d2d24cda34d8c6290b3e6
---

# Review

## Summary

Most sentences in the note are short and carry one point each. Only a few pass roughly 40 words. These are the "Does it fit?" definition, the Popper sentence in "A test record is not truth" and the §82 sentence in "Fit is not an independent test". Each holds at most a main claim plus one contrast or consequence, or a parallel list after a colon. The reader never has to keep two long dependencies open at once.

No subject is separated from its verb by a long interrupting clause. In "A claim that repeatedly fails to predict, to guide recovery or to transfer has not been refuted by that alone", the interrupting list is short and parallel, so the distance is tolerable.

The only note is an info finding on the fit definition. It is dense but well structured.
