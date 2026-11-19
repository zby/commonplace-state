---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 7a48b8a809bd40d0a95d3a653572ef86
completed-at: '2026-11-17T07:22:19Z'
findings:
- scope: passage
  quotes:
  - This distinction concerns the causal role of a particular judgment. It does not
    establish that a later evaluator had no other influence on the system.
  reason: The first Scope bullet repeats a boundary the note has already drawn. The
    cases section already says the later assessment 'could still cause a future revision
    or a rollback' and that this 'would give it a causal role in a different transition'.
    That earlier passage is more concrete. The bullet adds no new boundary case, so
    deleting it loses nothing. Cut it; if the general wording is wanted, fold 'other
    influence' into the earlier sentence.
  level: warn
- scope: passage
  quotes:
  - human approval does not remove the need to justify the assessment
  reason: Defensive redundancy. The bullet opens with 'Approval does not establish
    quality', which already entails that approval does not replace a justified assessment.
    The closing clause restates the bullet's own opening and admits nothing new. The
    test-optimization sentence before it brings in a separate Goodhart concern, so
    ending on the restatement also leaves the bullet's job unclear. Cut the trailing
    clause, and keep the test-gaming point only if it bears on the selection/assessment
    distinction.
  level: warn
- scope: passage
  quotes:
  - A human approval required for adoption is part of the process that selected the
    revision. A later human assessment is not evidence of that same contribution to
    selection.
  reason: 'These two sentences restate the opening paragraph''s contrast with ''human''
    added. The worked cases then give the same contrast again in concrete form. The
    paragraph''s first sentence does work because it names the use: attributing a
    system''s improvement. It is unclear whether the human-specific restatement adds
    uptake, since the opening already says the role does not depend on whether a person
    or a program judges. Consider keeping the use sentence and letting the cases carry
    the contrast.'
  level: info
contract: verdict
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/9b7fef079868a383f871d2e8/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/9b7fef079868a383f871d2e8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/7a48b8a809bd40d0a95d3a653572ef86/outputs/review.md
raw-output-sha256: 1a977e13a424c11d5157280fea69ec18bc22825c89069faa48243a1560e75f3d
---

# Review

Most of the note earns its space. The opening claim, the two worked cases, the account of one episode containing both roles, and the paragraph that anchors "adoption" to operative change each do distinct work. The hypothetical-case disclaimer is a short provenance mark, not a hedge. The "Calling the whole episode an evaluation" and "A different description cannot turn required approval" sentences look similar but do different jobs. The first is about lumping two judgments together. The second is about relabeling a required approval, which is the core claim in the note's description. Both pass.

The redundancy is in the Scope section. Its first bullet restates the later-assessment boundary that the cases section already states more concretely. Its third bullet ends with a clause its own opening already entails. Removing both makes Scope shorter, and Scope still carries its real boundary: participation in selection does not settle whether the evaluator belongs to the learner. The second paragraph's human-specific restatement is a borderline case. It is noted as INFO rather than WARN because it sits next to the note's statement of why the distinction matters.
