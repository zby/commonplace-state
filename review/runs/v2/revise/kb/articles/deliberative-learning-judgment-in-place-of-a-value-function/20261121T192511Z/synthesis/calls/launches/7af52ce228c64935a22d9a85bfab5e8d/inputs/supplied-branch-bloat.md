---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 1a68e7dbbf77431fa0f5e6c254fc7776
completed-at: '2026-11-21T19:28:12Z'
findings:
- scope: passage
  quotes:
  - An unknown is worth investigating only if a plausible answer could reverse the
    choice.
  reason: 'This sentence states a value-of-information rule for when to investigate
    an unknown. The article never uses it: the on-balance paragraph goes from ''every
    reasonable measure favors it'' straight to open verdicts and reversibility, and
    no later section decides whether to investigate. It is a side claim imported from
    the source note. It adds a claim the reader must evaluate without serving either
    level of the thesis. Remove it; the linked on-balance note already holds it.'
  level: warn
- scope: passage
  quotes:
  - yet its own data located the stall in what the proposer was not shown (its scorer
    saw a failure mode in a quarter of runs that never reached the proposer), and
    its strongest gains came from editing a natural-language lessons file.
  reason: The reinterpretation of the Harness Evolution study does useful work as
    a reply to the weights-only rival, so it should not simply be cut. But the parenthetical
    statistic opens a second, evidence-hungry argument about the scorer–proposer information
    flow inside a section whose job is the production-method versus representational-form
    distinction. Consider compressing it to the conclusion and leaving the specifics
    to the linked ingest. Where the detail belongs is unclear, so this is info only.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/1a68e7dbbf77431fa0f5e6c254fc7776/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/9159b0114b46fba491dc0ad4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/1a68e7dbbf77431fa0f5e6c254fc7776/outputs/review.md
raw-output-sha256: 38550b7f2b77346cd830a1a079dc30f53d49d1456adc30a6e44da0907fbafc88
---

# Review

The article's main claim has two levels. First, deliberative learning, meaning rejectable edits to a readable, addressable store, is a distinct learning paradigm in which on-balance judgment replaces a value function. Second, it bets that a fixed-weight language model can fill the judge slot and that this approach fits the Bitter Lesson. The description explicitly commits the article to the weight-training contrast, the Bitter Lesson discussion and the empirical test. Those sections are therefore part of the main claim, not branches.

Most of the side material is needed:

- The routing-line example is the article's worked case, and later sections refer back to it.
- The costs paragraph and the four hazards set boundary conditions and limits on the bet.
- The Gödel machine, PRODIGY and EURISKO precedents support the claim that the bottleneck was "what played the value-function role."
- The bootstrap condition limits how far the Bitter Lesson compatibility claim reaches.
- The two-part test makes the bet falsifiable.
- The weights-only rival, Sutton/Javed plus the harness study, is a needed opponent concession and reply.

Two passages need attention. The value-of-information sentence in the on-balance paragraph is a stray rule that the argument never uses. It should be removed (WARN). The harness study's parenthetical statistic supports the reply to the rival, but it opens a sub-argument that could be compressed toward the linked ingest (INFO).
