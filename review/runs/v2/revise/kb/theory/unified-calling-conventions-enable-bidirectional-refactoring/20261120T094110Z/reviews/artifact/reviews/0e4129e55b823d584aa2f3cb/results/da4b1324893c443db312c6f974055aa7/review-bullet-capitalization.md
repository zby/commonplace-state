---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '[constraining](./definitions/constraining.md) — the mechanism that unified calling
    makes frictionless'
  - '[codification](./definitions/codification.md) — the phase transition from neural
    to symbolic'
  reason: These footer bullets begin with lowercase link text for registered terms.
    The lowercase mirrors the definition file names and works as an identifier-style
    label, so it is defensible, but it is inconsistent with sibling footer bullets
    that use capitalized titles such as "[Prompting changes failure diagnosis...]".
    Capitalizing the term or using the definition titles would make the list uniform.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/structural/bullet-capitalization.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/structural/bullet-capitalization.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: 807dce0e67e2aaa4a5e7f81b62364e3707ffb2c46eae078cdbed121a53531660
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/da4b1324893c443db312c6f974055aa7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/0e4129e55b823d584aa2f3cb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: da4b1324893c443db312c6f974055aa7
completed-at: '2026-11-20T09:43:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/da4b1324893c443db312c6f974055aa7/outputs/review-bullet-capitalization.md
raw-output-sha256: 9170798ccbe0f2ff708d3440c6c08343ae67c77a2f3e382b9327110ec074303e
format: 2
---

# Review

The Open Questions bullets and numbered steps all begin with capital letters. In the Relevant Notes footer, the bullets that begin with `spec-mining-as-codification`, `instructions-are-typed-callables` and `operational-signals-that-a-component-is-a-relaxing-candidate` use file-slug identifiers as link text. Those are deliberately lowercase forms, so the gate exempts them. The `constraining` and `codification` bullets are borderline. They are ordinary words rather than slugs, but they match the registered term and file names. They are recorded as INFO rather than a failure.
