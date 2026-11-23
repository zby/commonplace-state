---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution
    is algorithmically determined. In the vision-feature regime, the bet is risky:
    the spec is a theory, and scale may reveal a better path.'
  reason: INFO. Near the start of the bet section, this re-explains the arithmetic/vision-feature
    split that the previous section's two bullets already set out. It is setup reframed
    in bet terms rather than a second thesis statement, and its final sentence (the
    blurry zone) adds new content. So this is a weak signal, not a deletable paragraph.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/fcf36d84931b09bbd765172a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 15c0d28c726a474283672c97c466d84d
completed-at: '2026-11-20T09:13:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-redundant-restatement.md
raw-output-sha256: 58615baa04bb69f71a1f11a4d87e179e22e9ed65e172d78327ad6ed7782836c9
format: 2
---

# Review

## Summary

Section openings: the first section opens by defining the code-extraction scope of codification, which is new material. The bet section opens with the bet thesis itself, which is new; it repeats the code-extraction framing in only one clause. The heuristics section opens directly with heuristic 1. None of these opening paragraphs could be deleted without losing the section's own contribution.

Paragraphs before headings: the trajectory paragraph before the bet section and the induction-bias paragraph before the heuristics do not preview the following sections.

The only overlap is the bet section's second paragraph, which restates the regime contrast in bet language (INFO).
