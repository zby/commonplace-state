---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - accretion below the gains it finds
  - weights-only continual learning wins those domains
  reason: 'This is the article''s falsification condition, and it is load-bearing.
    Three choices remain open. (1) Comparison basis: ''below the gains'' can mean
    net gain under an aggregate score, or the on-balance standard the article defines,
    where every reasonable measure must agree. (2) Baseline: the gains can be measured
    against no learning, against a human judge in the same loop, or against weight
    training. (3) Scope: ''those domains'' can mean the domains tested in the controlled
    runs or all ''work where no fixed criterion is adequate''. Each choice changes
    which experiment falsifies the bet and what follows from it. Only a comparison
    against weight training could license the conclusion that ''weights-only continual
    learning wins''.'
  level: warn
- scope: passage
  quotes:
  - the system sits on the computation side of the Bitter Lesson
  reason: Two mechanisms fit this sentence. (a) The system counts as computation-based
    because its judge is a model produced by large-scale training. (b) It counts because
    the store's content is produced through search and selection by computation. The
    next paragraph's bootstrap condition points toward (b) but is framed as an added
    condition. The difference is plausibly material, but context largely resolves
    it.
  level: info
- scope: passage
  quotes:
  - must score higher across reasonable measures of the declared work
  reason: '''Across reasonable measures'' can mean every reasonable measure or an
    aggregate over them. Two paragraphs earlier, the definition of ''learned'' says
    ''across every reasonable measure'', which resolves the reading in context.'
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/907aecbeaa49824b25b53a4b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a494636333e44e6fab547975bb757825
completed-at: '2026-11-21T19:30:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/outputs/review-underspecified-assertions.md
raw-output-sha256: c57ecec68fc6d41680f70874db75433011213a5ade3151b81fe37955d764fafe
format: 2
---

# Review

Most load-bearing assertions are well specified. The learned verdict names
its alternative, horizon and standard. The routing-line example resolves its
evaluative terms into concrete outcomes. The operative-dependence check names
its intervention.

The exception is the closing falsification condition, which carries
the article's empirical commitment. It leaves three choices open: how costs
and gains are compared, which baseline the gains are measured against, and
which domains the verdict covers. Different choices yield different
experiments. Only some of them would support the stated conclusion that
weights-only learning wins.

Two other possible ambiguities are resolved by nearby context and are
recorded as INFO.
