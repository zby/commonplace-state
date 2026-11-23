---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: da4b1324893c443db312c6f974055aa7
completed-at: '2026-11-20T09:43:01Z'
findings:
- scope: passage
  quotes:
  - '[llm-do](https://github.com/zby/llm-do) implements this through a hybrid VM'
  reason: '"The mechanism" is framed around one system (llm-do, proper nouns, `.agent`
    files). The following section, "Why this matters for constraining", gives the
    general argument: without a unified interface, codification is a breaking change.
    The llm-do section partly exemplifies that argument. However, the introduction
    already states the general rule, that a unified calling convention makes refactoring
    across the boundary local, before either section. The reader therefore meets the
    rule first. The order is defensible, but leading with the general rationale is
    a possible improvement.'
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/da4b1324893c443db312c6f974055aa7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/31cb4cfbe8416e98300ccfb6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/da4b1324893c443db312c6f974055aa7/outputs/review-general-before-specific.md
raw-output-sha256: 6cc8bc316329bebb67507448805dd9166947c88c8763eae6ac441e31e92febca
---

# Review

Adjacent section pairs:

- **The mechanism → Why this matters for constraining.** The first section is llm-do-specific. The second section is more general. Because the introduction already states the general claim, the llm-do section does not precede the first statement of the rule. It is recorded as INFO, not WARN.
- **Why this matters for constraining → The scheduler layer.** This pair moves from general to specific, which is the correct order.
- **The scheduler layer → The connection to typed callables.** The second section links llm-do to a separate theory note. It does not state the general rule that the scheduler exemplifies, so no reordering is indicated.
- **The connection to typed callables → Open Questions.** This pair is not a specific-to-general pair.
