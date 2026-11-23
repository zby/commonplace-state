---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/accessibility/notation-opacity.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/review-gates/accessibility/notation-opacity.md
criterion-sha256: 1169b01cde2019fc32462be33de88364d0eebd8a030621ab4fd4143257dc17fe
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 5d4164f1498d4b17ab9a757ce8cd39e3
completed-at: '2026-11-20T09:13:05Z'
findings:
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
  - κ = 0.28 for CoT
  reason: The symbol κ comes from the Ebrahimi et al. paper. The note gives only its
    name, "sharing factor". It never says what is shared, what scale κ uses, or which
    direction means more sharing. A reader cannot tell whether κ ≈ 1 is good or bad,
    or why 0.28 shows that training diversity "actively hurts". The note uses κ in
    no formal argument. Replace the values with plain language, such as "transformers
    reuse little or nothing across sequence lengths, and chain-of-thought supervision
    makes this worse". Otherwise, define κ and its scale in one clause.
  level: warn
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/0799d301abcb8ef44692a6a4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/outputs/review-notation-opacity.md
raw-output-sha256: 502ed03deb9de28fc90a22bdd21a6cb6bcc51ee2c37eed4c6a20b8d5a06b46ba
---

# Review

The note has one piece of formal notation: the sharing factor κ in the induction-bias paragraph. The note does not define it, and it appears as bare values (κ ≈ 1, κ < 1, κ = 0.28). The next clause, "they learn length-specific solutions in isolation", suggests the intended reading. Still, the reader cannot work out from the note what the numbers measure or which direction is better. The paragraph contains no equations or derivations that need the symbol, so plain language is the better fix.

No other notation appears. The slash in "arithmetic/vision-feature boundary" is ordinary prose shorthand, not a variable.
