---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
findings: []
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/6cb72caa3094475bd7c2125c/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/6cb72caa3094475bd7c2125c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-source-residue.md
raw-output-sha256: 4395eab80d2072eef273574c5b7b88eb5e3c2e5f32e61f5ac916b8849dc9c3b4
---

# Review

The title states a general relativity claim. The opening immediately scopes the note to "a knowledge base written and reviewed by agents" and then to "Commonplace's grounding check". The note explains this narrowing: the unit of cost is clear for that check and "would need its own unit for any other check". The Scope section repeats the boundary.

The narrower-domain vocabulary is therefore framed as the declared case, not as leakage. This includes verbatim-quote validation, ADRs, retained quotes and snapshot-required marks. The mathematical-proof vocabulary from Descartes and Lamport ("chains", "proof step", "geometers") appears only inside passages explicitly presented as precedents and marked as analogy. No unframed domain-specific framing overcommits the general claim.
