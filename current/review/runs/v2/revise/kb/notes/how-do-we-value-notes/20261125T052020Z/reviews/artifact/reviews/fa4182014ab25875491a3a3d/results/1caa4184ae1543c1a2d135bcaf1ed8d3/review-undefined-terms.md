---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - propagate value from them down through answering notes and their subroutines
  reason: '"Subroutines" is applied to notes without explanation. A reader can guess
    that it means notes that answer sub-questions for an answering note, but nothing
    in the sentence says so, and the programming metaphor is not conventional for
    notes.'
  level: warn
- scope: passage
  quotes:
  - subroutine reuse, demand-root coverage
  reason: This list names two valuation signals that the note never defines. "Subroutine
    reuse" depends on the unexplained "subroutines" above. "Demand-root coverage"
    is new and only loosely connected to the earlier "root questions". A reader cannot
    tell what either signal measures.
  level: warn
- scope: passage
  quotes:
  - Where no fixed oracle decides theory fit
  reason: '"Fixed oracle" is borrowed from testing terminology and is not glossed.
    A short gloss, such as "a fixed test that decides whether a note fits the theory",
    would make the sentence readable without following the link.'
  level: info
- scope: passage
  quotes:
  - link-strength-weighted inbound links
  reason: '"Link strength" is not explained. A reader cannot tell what makes one link
    stronger than another without opening the linked quality-signal notes.'
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/1caa4184ae1543c1a2d135bcaf1ed8d3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/fa4182014ab25875491a3a3d/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 1caa4184ae1543c1a2d135bcaf1ed8d3
completed-at: '2026-11-25T05:21:20Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/1caa4184ae1543c1a2d135bcaf1ed8d3/outputs/review-undefined-terms.md
raw-output-sha256: ec4ca6c4ab5fe0727c106c4fdf3295342a47fd245383e1f30861899c18db6a62
format: 2
---

# Review

## Summary

Most technical terms receive an inline gloss on first use: explanatory-reach (with a gloss and a link, which this KB's active vocabulary requires), answerable, validity versus learning value, test record versus fit in a working theory, warranted reader update and counterfactual use. "Reader-need labels" is explained by its examples, and root questions are described before the note relies on them. "Goodharting" is standard enough to leave as it is.

The problems cluster in the Unsettled section. That section introduces "subroutines" for notes and later lists "subroutine reuse" and "demand-root coverage" as signals to weigh. Neither signal is defined, so a first-time reader cannot follow the open problem about combining dimensions. "Fixed oracle" and "link strength" are smaller gaps that a short gloss would close.
