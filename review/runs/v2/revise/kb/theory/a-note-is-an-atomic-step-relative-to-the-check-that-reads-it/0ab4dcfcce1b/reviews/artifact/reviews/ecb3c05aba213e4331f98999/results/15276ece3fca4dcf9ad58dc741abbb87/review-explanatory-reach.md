---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - An artifact-side bound does not have that failure mode, because a conforming artifact
    fits by construction
  reason: This sub-argument assumes that a validator can decide conformance mechanically.
    However, the note's unit (the unquoted source) depends on whether a source's support
    for a claim is carried by a quotation, and deciding that is partly a judgment.
    The mechanism for why the artifact-side bound avoids silent failure is plausible
    but not yet constrained enough to show the count is mechanically decidable.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/ecb3c05aba213e4331f98999/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/ecb3c05aba213e4331f98999/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-explanatory-reach.md
raw-output-sha256: a928da3ac57ae2b14c5d5da41a668c6675c07b218f645ee8fa02f7905896cbbe
format: 2
---

# Review

The central claim is that a note's atomicity is relative to the check applied to it, and that for the grounding check the unit of cost is the unquoted source. The note gives a mechanism for this: the grounding check's cost is the work of finding the supporting passage in each artifact. A verbatim quote moves that finding step into a substring validator, so a quoted source no longer adds to that cost, while a snapshot-required source still adds its full cost.

The mechanism is hard to vary. If the validator is removed, quoting no longer discharges the finding step, and the note says so in Scope. If the cost is counted in links or bytes, the multi-source single-claim examples stop separating the two bounds. The claim is also falsifiable. A grounding check whose cost did not fall when sources were quoted, or a corpus where the two bounds never diverged, would count against it. The note does not add escape hatches. Occurrence-versus-representativeness and snapshot-required claims are stated as priced limits, with their consequence for the count. The supporting sub-argument that an artifact-side bound fails loudly is thinner, as noted.
