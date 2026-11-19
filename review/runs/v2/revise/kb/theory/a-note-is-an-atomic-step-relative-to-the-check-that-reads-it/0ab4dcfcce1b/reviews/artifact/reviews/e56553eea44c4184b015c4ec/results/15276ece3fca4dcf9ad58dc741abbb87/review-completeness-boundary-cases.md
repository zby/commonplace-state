---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Links to other notes are also not sources in this sense
  reason: 'The source/non-source split covers ingests (quoted, unquoted, snapshot-required)
    and linked notes, but not other linked artifacts the note itself relies on as
    evidence: ADRs and the retained report under kb/reports/retained/. Those map onto
    the ''linked note'' branch only if they carry a claim title and their own grounding
    review, which the note does not state. Coverage is possible but strained.'
  level: info
- scope: passage
  quotes:
  - A source that has been quoted verbatim is not one of them.
  reason: 'The unit is defined per source (quoted vs unquoted), but the mechanism
    is per cited claim: a source quoted for one claim and cited without a quote for
    another in the same note falls between the two categories. The finding-step mechanism
    resolves it (it counts for the unquoted use), but the stated unit does not.'
  level: info
- scope: passage
  quotes:
  - because three candidates are available and they justify different values
  reason: The three-way enumeration of what kind of number N is (degradation point,
    smallest no-miss count, convention) is presented as exhaustive without argument;
    an adjacent candidate such as a cost budget for the author or a value derived
    from the co-loading bound is not considered. The enumeration's argumentative role
    is only to eliminate two options, so this is strained rather than broken.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e56553eea44c4184b015c4ec/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e56553eea44c4184b015c4ec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 410bcee74c0af6f503bb4ec2cda23cf8146b7883597b4a93b25c1ff1ae6bac56
format: 2
---

# Review

The note's frameworks are the two bounds (co-loading and checking), the classification of linked material for the grounding check's cost (quoted source, unquoted source, snapshot-required source, linked note), and the three candidate kinds of N.

The two-bound framework holds at its boundaries: the note supplies both a case satisfying co-loading but not checking (the eight multi-source notes) and the converse case, and it says where the bounds couple. The linked-material classification handles the simplest case (one quoted source), the extreme case (claims needing a whole snapshot) and the joint-support case. It is strained at two adjacent cases. Linked artifacts that are neither notes nor sources, such as ADRs and retained reports, are not placed. A source used both quoted and unquoted is also not placed, because the unit is stated per source while the mechanism is per claim. The enumeration of N kinds is not argued exhaustive, but it only needs to eliminate two alternatives. None of these cases clearly falls outside the claimed coverage, so the gate passes with informational findings.
