---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - separates trustworthiness from whether a candidate earns its maintenance burden
  reason: 'The body already links this note and states the same relationship: a note
    can be grounded and coherent yet too redundant or narrow to justify its maintenance
    cost. The footer''s untyped see-also label adds no relationship semantics, and
    its gloss adds no framing beyond the body.'
  level: warn
- scope: passage
  quotes:
  - defines substantive writing value relative to the reader's prior and existing
    KB
  reason: The body already links this note and says it asks what change the note warrants
    relative to the intended reader and existing KB. The see-also footer entry repeats
    that framing without adding a typed relationship or new navigational context.
  level: warn
- scope: passage
  quotes:
  - candidate structural and review signals for ranking notes as the corpus grows
  reason: The body already links this note for ranking at scale and lists the structural
    and review signals. The see-also footer entry restates that use and adds neither
    a typed relationship nor new context.
  level: warn
- scope: passage
  quotes:
  - counterfactual use in live work as a selection signal when no fixed oracle exists
  reason: 'The body''s Counterfactual use bullet already links this note and states
    the same relationship: where no fixed oracle exists, counterfactual effect in
    live work serves as a selection signal. The see-also footer entry nearly paraphrases
    the body.'
  level: warn
- scope: passage
  quotes:
  - Commonplace's admission invariant naming referent, asserted property, and revision
    trigger
  reason: The gloss repeats the body's Admission bullet, which lists referent, correctness
    or currency property, and revision trigger. The entry does carry a typed relation
    (evidenced-by), so under the gate's second question it is not counted as inflated.
    The type is questionable, though, because a definition is not evidence for the
    note's claims. Retyping or removing the entry would make the footer clearer.
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a9173c3ee1b847eab4323e4d4cabd507/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/9eb544ffab8a84490525dedc/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a9173c3ee1b847eab4323e4d4cabd507
completed-at: '2026-11-25T05:22:07Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a9173c3ee1b847eab4323e4d4cabd507/outputs/review-connection-inflation.md
raw-output-sha256: 9b523290e8ba129f40d57d52b0ca0062ee8f88a87cff94f934627624caf00e86
format: 2
---

# Review

## Summary

All five footer entries point to notes the body already links inline. Four use the untyped `see-also` label. Each of their glosses restates the relationship the body already sets out in its lens bullet, so they fail both questions in the gate's test. The fifth entry, Answerability, carries a typed relation. That passes the second question, even though its gloss repeats the body and the `evidenced-by` type fits a definition poorly.

The footer currently adds almost nothing that the body's inline links don't already give a reader. It would earn its place if it pointed to notes the body does not cite, such as the maintenance-capacity, test-record, improvement or underselection notes, or if it used typed relations that say how each target bears on this query.
