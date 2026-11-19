---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
findings:
- scope: passage
  quotes:
  - eight cite more than five distinct sources
  reason: '''Sources'' has two reasonable readings: (a) any distinct linked artifact,
    including notes, ADRs and reports; (b) cited source ingests only, and of those
    either all or only the unquoted ones. The note itself argues that linked notes
    are not sources and that quoted sources do not count against the step. The unresolved
    choice is the counting population. It is material: under (a) or under ''all ingests'',
    the conclusion that these eight notes are not atomic steps for the grounding check
    does not follow from the note''s own unit. Under ''unquoted ingests'' it does.
    The count of 344, the threshold of five and the date are also given without a
    method, so the evidence needed to support the assertion is unclear.'
  level: warn
- scope: passage
  quotes:
  - A verdict resting on fourteen artifacts costs as much to audit
  reason: This contrasts with 'three sources and six quoted passages'. It is unclear
    whether the three sources are unquoted, which would mean opening them, or the
    sources of the six quotes, which would mean opening nothing. The difference changes
    how far auditability actually differs between the two cases, but the surrounding
    paragraph makes the intended reading likely, so this is informational.
  level: info
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/c3d1f93f3654fedf810629fa/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/c3d1f93f3654fedf810629fa/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-underspecified-assertions.md
raw-output-sha256: f2e0bae9a8fa30715085ee008aba98f249565b79eb2925a6d7cfa1628946c3f2
---

# Review

Most load-bearing assertions are specific. The unit of cost is defined as the artifacts in which the reviewer must find the supporting passage. The experiment's numbers are given, the kind of number N is named while its value is left explicitly undecided, and the limits of quoting are stated with their consequence for the count.

The corpus paragraph is the one place where an unresolved choice changes the argument. It is the note's main evidence that the two bounds diverge in practice. Its count of "distinct sources" does not say which linked artifacts count, while the note's own mechanism makes that distinction decisive. Depending on the reading, the eight notes either support the claim that the bounds come apart or do not show it.
