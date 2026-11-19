---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 8a50c381505d456c8bee5240864437ff
completed-at: '2026-11-16T18:55:47Z'
findings: []
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/0ef14e09cf214cb02939e6c1/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/0ef14e09cf214cb02939e6c1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/8a50c381505d456c8bee5240864437ff/outputs/review-jargon-persistence.md
raw-output-sha256: 1984a35d51476347fb25bf81ed379339cb569b9d549b75c844e9420a60c2ceb4
---

# Review

The note's recurring framework terms are "theory fit", "selection environment" and "fixed oracle". Each recurs several times, but later uses carry local context rather than relying on a single early definition.

"Theory fit" is grounded in the opening paragraph (claims that fit poorly together or fail to help the system reason, modify or recover), and later uses sit inside sentences that restate what fit is about, such as "Fit is exposed through a portfolio of consequences" and the Scope bullet contrasting it with "a claim's independent test record". Its qualifier carries meaning that plain "fit" would not recover, so the gate's qualifier exception also applies.

"Selection environment" is introduced with a gloss (claims earn provisional standing by changing consequential work and surviving consequences of use). Later uses such as "an **initial** selection environment, not a final authority" and "make the selection environment less self-sealing" are readable from their own sentences.

"Fixed oracle" is paraphrased in the second paragraph as "automatic evaluator fully decides", and later uses ("No one item is a complete oracle", "complete global evaluator") keep that evaluator sense visible. No term loses its grounding through repetition.
