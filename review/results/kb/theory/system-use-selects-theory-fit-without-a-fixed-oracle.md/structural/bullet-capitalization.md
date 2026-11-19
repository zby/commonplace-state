---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/structural/bullet-capitalization.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/structural/bullet-capitalization.md
criterion-sha256: 807dce0e67e2aaa4a5e7f81b62364e3707ffb2c46eae078cdbed121a53531660
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 9a3dadef070b47feafc46aa3d3260d94
completed-at: '2026-11-16T18:56:07Z'
findings:
- scope: passage
  quotes:
  - changes proposal, diagnosis, branch allocation, or recovery rather than merely
    being cited;
  reason: The six lowercase bullets after 'including whether a claim:' are grammatical
    completions of that lead-in sentence, punctuated with semicolons and a final 'and'.
    Lowercase is the deliberate form for such run-in lists, so this is not the gate's
    failure mode.
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/6f1dc6b3185e60a624d36618/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/6f1dc6b3185e60a624d36618/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/9a3dadef070b47feafc46aa3d3260d94/outputs/review-bullet-capitalization.md
raw-output-sha256: 37e542ee1410cbff998ab8fd9ba787134c12fba40868f684ffff934e0054ff8e
---

# Review

The note has three bullet lists. The Scope and Open Questions bullets all begin with a capital letter or with a quoted capitalized word ("Initial").

The list under "including whether a claim:" begins each item in lowercase. Each item completes the lead-in sentence ("whether a claim changes…", "whether a claim yields…"), and the items end with semicolons and a closing "and". The list is one sentence split into items, so lowercase is the deliberate form. The gate's test skips deliberately lowercase forms. No bullet begins in lowercase where a standalone fragment should be capitalized.
