---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/complexity/framework-decoration.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a9173c3ee1b847eab4323e4d4cabd507
completed-at: '2026-11-25T05:22:07Z'
findings:
- scope: passage
  quotes:
  - (reader update, subroutine reuse, demand-root coverage, counterfactual use, maintenance
    cost)
  reason: The list of dimensions to combine does not line up with the five lenses
    in Current answer. It drops admission/answerability, validity-versus-value and
    structural proxies, and it introduces 'demand-root coverage' and 'subroutine reuse'
    without defining them. The mismatch is minor, but readers can't tell whether this
    is a second taxonomy or a restatement of the first.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a9173c3ee1b847eab4323e4d4cabd507/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/3e7975c5d99d9ed12fdeee64/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a9173c3ee1b847eab4323e4d4cabd507/outputs/review-framework-decoration.md
raw-output-sha256: 3f5a8337d598e468412d1164b519dfa9047b7981f638c39705b0abe7c6a08627
---

# Review

## Summary

The note's only framework-like structure is the five-lens list in Current answer. That list does real work, so it is not decoration. Each lens names a different test: an admission contract, validity versus value, reader update against a cheaper alternative, counterfactual effect in live work, and structural ranking proxies. The lenses also differ in when they can be observed. The Unsettled section depends on these differences. The asymmetric-pressure item contrasts the validity checks with the learning-value and reader-update lenses. The cold-start item contrasts the lenses usable at admission with the inbound-link and counterfactual-use signals, which only appear after retention. A single sentence such as "Commonplace uses several partial criteria" would lose those contrasts.

The note has no notation, equations or formal decompositions. The one minor inconsistency is that the list of dimensions to combine uses vocabulary that differs from the five lenses. It is recorded as an info finding.
