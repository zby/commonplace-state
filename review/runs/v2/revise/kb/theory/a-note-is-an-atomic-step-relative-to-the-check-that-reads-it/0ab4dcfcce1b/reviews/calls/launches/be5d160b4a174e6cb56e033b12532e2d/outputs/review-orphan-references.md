---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Across 344 notes in `kb/notes/` as of 2026-08-27, eight cite more than five"
    reason: "The corpus count is the note's main evidence that the two bounds come apart. It has no linked report, script or method, so the reader cannot inspect it. The note does not say how 'distinct sources' were counted (links? ingests only? quoted versus unquoted?). That definition matters because the note's own unit is the unquoted source. The count is also scoped to `kb/notes/`, while the note itself lives in `kb/theory/`, which leaves the counted population unclear. Link the measurement or state its method and population."
    level: warn
  - scope: passage
    quotes:
      - "Commonplace's own measurement that language-model verdicts disagree with themselves on unchanged input"
    reason: "A named measurement is offered as 'the reason auditability is worth paying for', but no link, size or result is given. The reader cannot evaluate how large or frequent the self-disagreement is. Link the retained report or state the observed rate."
    level: warn
  - scope: passage
    quotes:
      - "the review-side proposal *Exceeding a review budget splits the task*"
    reason: "A named, archived proposal is cited for what it 'identified' and 'concluded', without a link or location. The reader cannot check that it reached the by-claim partition conclusion attributed to it."
    level: warn
outcome: warn
---

# Review

Most specific figures are anchored. The paired-experiment numbers (twelve notes, a five-link cap, four findings, six/eleven/fourteen/sixteen artifacts) are attached to a linked retained report. The later "twenty-two artifacts and 322 kilobytes" figure is explicitly placed "in the same experiment". ADR 046, 073 and 079 are linked. The Descartes and Lamport quotations cite their ingests and sections.

Three specific references lack a source or enough context: the corpus count, the self-disagreement measurement and the archived proposal. The corpus count carries the most weight, because the section "The two bounds come apart in the corpus" rests on it. Each reference is local and fixable by a link or a method statement, so the result is WARN.
