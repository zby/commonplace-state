---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - both are prices already paid elsewhere in the system
  reason: 'Literal meaning: both limits already apply to verbatim quotation wherever
    Commonplace uses it, so this note introduces no new limitation. The cost-accounting
    image adds a location (''elsewhere'') and a settled transaction (''already paid'')
    that the note never identifies, so the reader must guess where the payment was
    made. Replacement: ''both are limits Commonplace already accepts for verbatim
    quotation generally''. This removes the unlocated ''elsewhere'' and the implication
    of a specific prior trade-off.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/4afbcd47fd6cc23e73585fc6/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/4afbcd47fd6cc23e73585fc6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-mannered-prose.md
raw-output-sha256: 1b9bba89ef8c25cea08cb00c13c6111781c700751c06448300c2b5d19cd8236e
format: 2
---

# Review

The note mostly states its claims literally. Several economic idioms ("costs a trip to the source", "the audit the bound buys", "quoting spends against the co-loading bound") pass. They match the note's explicit cost framing: the grounding check is analysed by what it costs a reviewer. "Spends against" also names the real coupling the next sentence states. "Whether a finding was sitting behind it" is a conventional spatial figure for unread material and is clear.

One phrase fails the test. "Prices already paid elsewhere in the system" introduces an unlocated payment that the surrounding text does not resolve. The literal version is at least as clear and shorter in effect. This is a single local instance, so the result is WARN.
