---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a494636333e44e6fab547975bb757825
completed-at: '2026-11-21T19:30:11Z'
findings:
- scope: passage
  quotes:
  - Deployment time, taking effect on the next task that reads the store
  reason: The comparison table makes update timing a structural axis, with deployment
    time for deliberative learning and training runs for weights. The article's own
    two-condition definition has no timing condition, and two boundary cases fall
    outside the row. First, online weight updates made during deployment are weight
    training at deployment time. Second, a team editing its handbook or code by judgment
    before a release is deliberative learning outside deployment. The intro itself
    counts the handbook team as a precedent. The row describes the Commonplace deployment,
    not the paradigm contrast it claims to draw.
  level: warn
- scope: passage
  quotes:
  - the bet fails—and weights-only continual learning wins those domains
  reason: 'The failure clause names two outcomes: the bet holds, or weights-only continual
    learning wins. Other outcomes fit the article''s own material. Both approaches
    could fail in a domain. A human judge could still make deliberative learning viable
    there. The approaches could also combine: the cited Harness Evolution study reports
    adapters that stack with an evolved harness. The bet''s failure does not imply
    the weights-only alternative.'
  level: warn
- scope: passage
  quotes:
  - Inspecting traces to edit, narrow, or revert specific entries while keeping the
    rest
  reason: The table presents targeted, trace-based correction as the deliberative
    side of the contrast. The simplest deliberative learner is a one-shot admission
    gate that never revises earlier edits. It meets both conditions but has no such
    correction, and the linked definition treats correction as a separate property.
    The article's 'Where to go next' points to this distinction, so the boundary is
    recoverable. The table cell still strains it.
  level: info
- scope: passage
  quotes:
  - four hazards can defeat it
  reason: 'Search omission is an adjacent failure outside the list: the loop never
    proposes the edit worth having, and no judge can recover that. Retrieval misses
    are another; the earlier cost paragraph names them, but the hazard list does not.
    The list is not presented as exhaustive, so coverage is strained rather than broken.'
  level: info
- scope: passage
  quotes:
  - Looking at three precedents shows that the bottleneck was always
  reason: The precedent ladder of proof, fixed formula and on-balance judgment classifies
    systems by what fills the value-function role. The EURISKO rung sits on a different
    axis, criterion revision. Human on-balance judges, such as the software teams
    named in the intro, are the obvious precedent for the top rung, yet the ladder
    omits them. The mapping is possible but strained.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/7981cece45014b5df1ab98d8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 4a66ee158a804dec54e90fc68d2b441751350d78477f68830735bf0ac79c6a82
---

# Review

The article sets up three frameworks:

- the two membership conditions with the weight-training comparison table;
- the precedent ladder of proof, formula, changing heuristics and judgment;
- the evaluation apparatus: the learned verdict, the two-part check, the four
  hazards and the failure condition.

The two conditions handle their boundary cases well. Direct updates, readable
tabular tables, triggers and automatic logging are placed explicitly, and the
fixed-criterion limiting case is named.

The comparison table is the weak point. Its timing row does not follow from
the definition. Online weight training and pre-release deliberative editing
both fall outside the row. The correction row describes a property that some
members lack.

The closing failure condition treats a failed bet as a win for weights-only
learning. It leaves out mixed, hybrid and human-judge outcomes, and the
article's own cited evidence points to some of these.

The remaining findings are INFO: the hazard list and the precedent ladder are
illustrative rather than claimed to be complete. None calls for adding
categories. Narrowing the timing row and the failure clause would close the
gaps.
