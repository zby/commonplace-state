---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 8bfc809941a747bdbe0657a1a1c6c3f6
completed-at: '2026-11-17T07:20:34Z'
findings:
- scope: passage
  quotes:
  - Participation in selection does not by itself determine whether the evaluator
    counts as part of the learner. That depends on the declared system boundary.
  reason: '"The learner" and "declared system boundary" are used as if the reader
    already knows them. They are not glossed, and nothing earlier in the note introduces
    the idea that an improvement claim names a learning system with a declared boundary.
    Without that idea, a first-time reader cannot tell what being "part of the learner"
    would mean or who declares the boundary. Add a short inline gloss, such as "the
    system credited with learning, whose extent the improvement claim declares", and
    link the source note if one exists. The open question''s "declared learner boundary"
    depends on the same unexplained concept.'
  level: warn
- scope: passage
  quotes:
  - Supplement to the adoption-versus-measurement distinction in [the better-factory
    comparison]
  reason: '"The better-factory comparison" names a KB-internal argument and gives
    no hint of what it compares. The body can be read without it, so the cost is low.
    A few words saying what that note claims would still tell the reader whether to
    follow the link.'
  level: info
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/420ceb63b44830c3676b9c54/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/420ceb63b44830c3676b9c54/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/8bfc809941a747bdbe0657a1a1c6c3f6/outputs/review-undefined-terms.md
raw-output-sha256: 9adf6fd7da4ce5fbdcd98823487cc574cdef2e52a9e083a9ac45cefe658a6c3c
---

# Review

## Summary

The core vocabulary works for a first-time reader. The two worked cases define "approval before adoption" and "assessment after adoption" through what the evaluator controls. "Adoption" receives an inline gloss, "entering a live behavioral path on which later operation depends", next to its link to the operative-change definition, so the link is not doing the defining.

The gap is in the Scope section. "The learner" and its "declared system boundary" import a framework concept from elsewhere in the KB without saying what it is. This is the one place where the reader would have to know KB context to follow the sentence. The supplement pointer's "better-factory comparison" is opaque but has little effect on comprehension.
