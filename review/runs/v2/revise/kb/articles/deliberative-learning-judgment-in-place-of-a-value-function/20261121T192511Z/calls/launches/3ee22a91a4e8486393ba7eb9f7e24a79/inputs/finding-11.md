---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
note-sha256: 135b98e5c97638f9c99a605f2b718690401271eaab4b9328f0777fdf0ac8dc5e
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a494636333e44e6fab547975bb757825
completed-at: '2026-11-21T19:30:12Z'
findings:
- scope: passage
  quotes:
  - That sequence establishes three things.
  reason: 'The routing-line case is a constructed illustration (''Suppose agents repeatedly
    misfile...''). Its outcomes are narrated in the indicative: ''On later tasks,
    the new line directs proposal writes accurately''. The article then says the sequence
    ''establishes'' three things. The first, ''the system adapted across tasks at
    deployment time without changing a single model weight'', reads as an observed
    result. Later the article reports no completed end-to-end automated run. A hypothetical
    lends the confidence of evidence to claims it only illustrates.'
  level: warn
- scope: passage
  quotes:
  - three precedents shows that the bottleneck was always
  reason: That earlier systems failed to become a general paradigm because of what
    played the value-function role is the article's own historical-causal construction.
    It rests on three selectively described cases, yet 'shows' and 'always' assert
    it as established. The article's own EURISKO account also cites brittleness and
    human intervention, so the construction needs proposing language.
  level: warn
- scope: passage
  quotes:
  - its own data located the stall in what the proposer was not shown
  reason: The parenthetical observation that the scorer saw a failure mode the proposer
    never received is reported data. The article says the data 'located the stall',
    which presents a causal explanation of the stall as if the observation established
    it. A mechanism inherits the confidence of the observation proposed to explain
    it.
  level: warn
- scope: passage
  quotes:
  - the system sits on the computation side of the Bitter Lesson
  reason: This sentence and the following one about what additional compute buys are
    written declaratively. They belong to the bet that the opening states, which includes
    scaling with computation compatible with the Bitter Lesson, and the 'strict condition'
    follows immediately. Their status is recoverable, but only by tracing back to
    the opening.
  level: info
contract: verdict
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/7989fe2870731906726997e5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/outputs/review-epistemic-status-blur.md
raw-output-sha256: ad6a759c9cc25bd970158ec3ee5ac6708bf4ec74f16c76db18376ba22b0b76ae
---

# Review

The article handles its main conjecture well. The bet is labelled as a bet
twice and set apart from the definitional first level. Its own section
reports the lack of end-to-end evidence and states a failure condition.

The blur sits in the supporting moves:

- The constructed routing-line example is said to "establish" conclusions,
  one of which reads as an observed deployment result.
- The diagnosis that the value-function role was "always" the bottleneck is
  the article's interpretive construction, but it is presented as shown.
- The rereading of the Harness Evolution study promotes an observation about
  what the proposer saw into a located cause of the stall.

In each case, a reader can no longer tell illustration or hypothesis from
reported finding.
