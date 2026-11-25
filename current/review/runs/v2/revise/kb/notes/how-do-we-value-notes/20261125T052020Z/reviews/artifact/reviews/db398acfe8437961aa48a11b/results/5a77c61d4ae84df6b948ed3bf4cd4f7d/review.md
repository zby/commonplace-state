---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This query stays open as long as candidate selection relies on ad-hoc judgment
    rather than a tested valuation practice; it would narrow or retire once Commonplace
    adopts and validates an explicit selection mechanism.
  reason: The collection's purpose says 'No further work or promotion is expected'
    of a note and sends 'material that still serves an investigation' to kb/work/.
    This passage and the whole Unsettled section explicitly expect further work and
    eventual narrowing or retirement. The Current answer is usable as written for
    a recognizable occasion (deciding whether a note is worth keeping), so the placement
    is defensible, but the note's standing-query framing conflicts with the contract's
    'finished' expectation. Either the contract should admit standing queries whose
    answer is kept current, or the note should frame its open items as known limits
    of a finished answer rather than as an ongoing investigation.
  level: warn
- scope: passage
  quotes:
  - Structural validation, source grounding, and critique gates check validity more
    strongly than anything checks learning value or reader update.
  reason: The Quality section asks notes to link to the evidence for factual examples.
    This is a factual comparison about Commonplace's current gates, but it links no
    instruction, reference or retained report that shows the asymmetry; the adjacent
    link supports only the general conjecture about weakly discriminated qualities.
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/notes/COLLECTION.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/notes/COLLECTION.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion-sha256: 4e28fa28099a5eceaece18aa0d3c0e610964838c3b0acd8ed5ca0591717bbb60
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/5a77c61d4ae84df6b948ed3bf4cd4f7d/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/db398acfe8437961aa48a11b/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 5a77c61d4ae84df6b948ed3bf4cd4f7d
completed-at: '2026-11-25T05:23:05Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/5a77c61d4ae84df6b948ed3bf4cd4f7d/outputs/review.md
raw-output-sha256: b931e950a040b01d0ba70147dac1b0b662fbb38f2a6e98009d30198ab175c0c6
format: 2
---

# Review

## Summary

The note mostly follows the notes collection's conventions. Its title is the question a reader would look up. Its description distinguishes it from the theory notes it draws on by naming its use: judging whether to keep or select a note as autonomous production grows. The body stands without any producing conversation or workshop. It links to existing theory for each lens instead of reconstructing the arguments, which the Quality section asks for.

Outbound links fit the contract's table. The `see-also` footer entries point to theory notes as companions or fuller arguments. The single `evidenced-by` entry points to a reference definition, which is a permitted destination. Inline links to `kb/reference/link-vocabulary.md` and other theory notes serve the reader directly.

The convention that is not fully met is the collection's expectation that a note is a finished piece with no further work expected. The note calls itself a standing query that stays open and expects to narrow or retire. Its Unsettled section lists open research problems, which the contract would route to `kb/work/`. Its Current answer is a usable reply for a recognizable occasion, so this is a WARN rather than a wrong-placement FAIL. The tension needs a decision: either amend the contract to admit standing queries, or reframe the open items as stated limits of a finished answer.
