---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/compression-bundle/detail-overhang.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 53523469b20f4c61aa0fedd39fae71f6
completed-at: '2026-11-25T05:23:35Z'
findings:
- scope: passage
  quotes:
  - what Commonplace's reader-need labels (`grounds`, `mechanism`, `defined-in`, `evidenced-by`
    in [link vocabulary](../reference/link-vocabulary.md)) already express
  reason: 'The root-questions bullet is the longest item in Unsettled, and this aside
    enumerates four link labels to make a point that a short link to the link vocabulary
    could make. The bullet''s job is to name the gap: there are no query-centred root
    notes from which value could propagate. The list of labels gives the reader no
    step toward that gap. It could shrink to ''what typed reader-need links already
    express'' with the link kept. It is flagged only as INFO because the concrete
    labels do show the reader what ''sub-question'' means in Commonplace terms.'
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/53523469b20f4c61aa0fedd39fae71f6/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/c352112b26ca262c9a51d426/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/53523469b20f4c61aa0fedd39fae71f6/outputs/review.md
raw-output-sha256: ab4cb65676b11d5458f0a596b4a3fe559d441a780ccc4adf7fe02049d4f93125
---

# Review

## Summary

Overall, the detail in this note is in proportion to the work it does. The note is a standing query: Stakes, Current answer and Unsettled. Each section stays compact.

- **Stakes.** The inline gloss of explanatory-reach and the examples of collection-specific bars do one job: they show that collection goals exist but do not rank notes. The maintenance-cost sentence carries the urgency premise in one line.
- **Current answer.** Each of the five lenses is one bullet, and each bullet glosses its linked theory in a clause or two. The "Validity separate from value" bullet links two notes, but the second adds a different distinction: test record versus theory fit. It is not repetition.
- **Unsettled.** Most bullets state the gap and its consequence briefly. The root-questions bullet runs longer than the others. Most of that length explains the orphan and closed-loop failure modes, and those are what make the gap concrete. The only part worth trimming is the list of link labels, recorded above as INFO.

Compressing further would mostly remove the short glosses that let a reader act on the query without opening every linked note.
