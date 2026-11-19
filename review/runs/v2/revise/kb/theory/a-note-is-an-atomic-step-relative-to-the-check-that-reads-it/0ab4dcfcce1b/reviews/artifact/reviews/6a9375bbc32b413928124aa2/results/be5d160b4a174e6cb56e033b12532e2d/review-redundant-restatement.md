---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the unit — the unquoted source — is derived from that check's cost structure
  reason: 'The first Scope bullet restates the opening''s closing sentences: the rule
    is stated for the grounding check, and another check would need its own unit.
    One is setup and the other is a scope summary at a different structural position,
    so this is weak, intentional reinforcement.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/6a9375bbc32b413928124aa2/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/6a9375bbc32b413928124aa2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-redundant-restatement.md
raw-output-sha256: 0314187cf16898c83bb4f8a502760a7b7a60c2885e3fcc77026edc12dbb157bb
format: 2
---

# Review

Every section opens with its own contribution. "Placing the bound…" opens with the alternative placement. "Mechanism…" opens by defining what the grounding check asks. "The two bounds come apart…" opens with the corpus count. "What kind of number…" opens with the claim that the bound fixes N's kind but not its value. None of these first paragraphs can be deleted without losing content.

The last paragraph before "Placing the bound…" ends with a one-sentence preview that the note will treat the grounding check. That transition is acceptable. The paragraph before "The two bounds come apart…" makes the separate point about linked notes and does not preview the corpus section.

The Scope section repeats two points from the body: the grounding-check scope and the undecided N. It does so as boundary statements rather than a second argument, which the gate treats as INFO.
