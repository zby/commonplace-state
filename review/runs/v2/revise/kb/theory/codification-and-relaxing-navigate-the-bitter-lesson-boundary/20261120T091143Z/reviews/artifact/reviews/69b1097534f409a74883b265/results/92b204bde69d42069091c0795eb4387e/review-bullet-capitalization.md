---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - fixed artifacts split into exact specs and proxy theories
  - the verifiability gradient
  - constraining and extraction can trade generality for reliability, speed, or cost
  reason: Several Relevant Notes items open with lowercase link text while the first
    item in the same list opens with a capitalized link title. Lowercase link text
    that names a target note is a deliberate citation form, so this is not a failure,
    but the list is internally inconsistent.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/structural/bullet-capitalization.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/structural/bullet-capitalization.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 807dce0e67e2aaa4a5e7f81b62364e3707ffb2c46eae078cdbed121a53531660
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/92b204bde69d42069091c0795eb4387e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/69b1097534f409a74883b265/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 92b204bde69d42069091c0795eb4387e
completed-at: '2026-11-20T09:13:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/92b204bde69d42069091c0795eb4387e/outputs/review-bullet-capitalization.md
raw-output-sha256: 56ad9aa6b7927e69e6750eea8bddb177fffdf8e7b55f92ec8ff720d631e703a1
format: 2
---

# Review

## Summary

The body's prose bullets all start with a capital letter: the two bolded regime items, the three numbered heuristics, and the two Sources entries. The only lowercase openings are in the Relevant Notes footer. Each of those items opens with link text that names its target note. That is a deliberately lowercase citation form, which the gate's test exempts. The one observation is that the footer mixes styles: the first item capitalizes its link title and the later items do not. This is recorded as INFO only.
