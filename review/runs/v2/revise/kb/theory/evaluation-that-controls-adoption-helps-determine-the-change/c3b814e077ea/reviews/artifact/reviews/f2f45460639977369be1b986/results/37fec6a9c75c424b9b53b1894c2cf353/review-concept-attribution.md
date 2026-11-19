---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: 32c9c946ad8092a20aa5d4cfe1aa0e58bc5f9bfe61100f236c18efc78f6c479b
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/f2f45460639977369be1b986/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/f2f45460639977369be1b986/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: 37fec6a9c75c424b9b53b1894c2cf353
completed-at: '2026-11-17T07:55:08Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/37fec6a9c75c424b9b53b1894c2cf353/outputs/review-concept-attribution.md
raw-output-sha256: fa2c0f39753ec9bb52dec130487f165d472d30d0b036800e5d3918369f4033a4
format: 2
---

# Review

## Summary

The note makes two references to linked notes, and both targets resolve.

"It complements [the comparison of a system before and after an adopted change]" refers to `a-better-factory-claim-compares-operative-states.md`. That note's title claim compares the predecessor with the adopted operative successor. Its Scope says that a comparison "judges the adopted states" and that "whether an evaluator also controlled adoption is a separate causal question". That supports the note's statement that an improvement judgment does not by itself show whether human evaluation was required. The target is framed around software factories, but its last Scope bullet extends the construction to other systems that revise their reusable machinery. The difference is one of vocabulary, not substance.

The citation of [routine approvals do not establish that human judgment is dispensable] matches the target's title claim and opening paragraph: repeated approval does not show that a human check is unnecessary. The note uses this to support the point that removing an approval stop requires deciding whether its check can be automated or is unnecessary, and the target says the same thing about accounting for exceptional cases.

Neither reference identifies a concept in this note with a differently treated concept in the target.
