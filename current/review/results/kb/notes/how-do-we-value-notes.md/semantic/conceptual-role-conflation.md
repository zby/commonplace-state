---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
findings:
- scope: passage
  quotes:
  - Commonplace currently spreads note valuation across five partial lenses rather
    than one rule
  reason: Mild blur between the object of application and the source accounts. 'Commonplace'
    could name the operating system that applies these lenses when it admits and ranks
    notes. It could also name the KB whose theory notes articulate them, some only
    as proposals. The bullets resolve most of this by attributing each lens to a named
    note ('asks', 'looks for', 'separates'), and the vocabulary defines Commonplace
    as 'This KB and framework', which covers both. The residual blur does not clearly
    change what this note contributes, because the note claims only to survey the
    lenses.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/c262dcc96c6b510223a54240/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-conceptual-role-conflation.md
raw-output-sha256: cd63e42fcea3485ebc569cc161cc79f4ebfb4e3cf86a7b0b780e6b74909c4200
---

# Review

## Summary

I inspected the passages that import or apply concepts: the explanatory-reach gloss, the answerability lens, the five lens bullets, and the mapping of sub-question reuse onto link-vocabulary labels.

- **Explanatory-reach.** The passage gives the registered term, a short gloss and a link, and treats it as an example of a collection quality bar. Term, concept and application stay distinct.
- **Lens bullets.** Each bullet names the linked note as the source account and states what that account "asks" or "separates". The current note frames itself as surveying these accounts, not as extending them. The opening "Commonplace currently spreads" sentence leaves a small ambiguity about whether the system applies the lenses or the KB articulates them. This is recorded as INFO because the bullets settle attribution to the source notes.
- **Link labels.** "what Commonplace's reader-need labels ... already express" applies registered labels to the sub-question relation. It does not redefine them, and the roles are clear.

No passage clears the materiality threshold.
