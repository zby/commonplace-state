---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: e7e7788b7ea190c885bef64d9c8f6ed445f02c6f4af354b813adc8b21b8868bc
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: d51ce59f0332424cab54d61772dd1184
completed-at: '2026-11-20T09:12:20Z'
findings:
- scope: passage
  quotes:
  - 'This note concerns the code-extraction case: committing an interpreted rule to
    a script, executable test, schema, or validator whose behavior can be inspected
    and checked at acceptable cost.'
  - The replacement can itself be codified by adoption; what relaxing reverses is
    the extraction, not symbolic membership.
  reason: 'Scope drift. The H1 names codification in general as one of the two navigating
    moves. The body narrows that move to code extraction: committing an interpreted
    rule to an inspectable script, test, schema or validator. It also states that
    codification by adoption, such as adopting a model package, falls outside this
    case. Relaxing is defined as reversing the extraction, not codification. The bet
    section is headed ''Every code-extraction codification is a bet''. What the body
    now establishes is that code extraction and relaxing navigate the bitter lesson
    boundary. Because the body declares a different scope, the title''s unqualified
    ''Codification'' is broader than what the body argues. Qualifying the title, for
    example with ''Code extraction and relaxing ...'', would align it.'
  level: warn
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/d51ce59f0332424cab54d61772dd1184/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/fb296f0a132c1c5826360c86/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/d51ce59f0332424cab54d61772dd1184/outputs/review-title-body-alignment.md
raw-output-sha256: a8b879ffda37b33e0181e771961f2546e72c1629e75ef01786847237f68926e2
---

# Review

## Summary

The body supports the title's central claim. The bitter lesson boundary between the arithmetic and vision-feature regimes cannot be identified in advance. Practical systems therefore commit structure, treat each commitment as a bet, and relax it when scale makes a general replacement viable. The trade-off section, the bidirectional trajectory, the bet framing, spec mining, relaxing signals and the working heuristics all serve that navigation claim, so there is no claim drift.

The mismatch is in scope. After revision, the body explicitly limits itself to the code-extraction case of codification. It excludes codification by adoption, and it defines relaxing as reversing an extraction. The H1 still says "Codification" without qualification, so it promises a broader scope than the body covers. The finding gives the narrower claim the body now establishes, so the title can be corrected to match.
