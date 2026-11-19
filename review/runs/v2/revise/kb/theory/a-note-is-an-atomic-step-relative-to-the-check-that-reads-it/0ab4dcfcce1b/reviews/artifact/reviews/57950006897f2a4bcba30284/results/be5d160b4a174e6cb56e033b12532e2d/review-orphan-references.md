---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Across 344 notes in `kb/notes/` as of 2026-08-27, eight cite more than five
  reason: The corpus count is the note's main evidence that the two bounds come apart.
    It has no linked report, script or method, so the reader cannot inspect it. The
    note does not say how 'distinct sources' were counted (links? ingests only? quoted
    versus unquoted?). That definition matters because the note's own unit is the
    unquoted source. The count is also scoped to `kb/notes/`, while the note itself
    lives in `kb/theory/`, which leaves the counted population unclear. Link the measurement
    or state its method and population.
  level: warn
- scope: passage
  quotes:
  - Commonplace's own measurement that language-model verdicts disagree with themselves
    on unchanged input
  reason: A named measurement is offered as 'the reason auditability is worth paying
    for', but no link, size or result is given. The reader cannot evaluate how large
    or frequent the self-disagreement is. Link the retained report or state the observed
    rate.
  level: warn
- scope: passage
  quotes:
  - the review-side proposal *Exceeding a review budget splits the task*
  reason: A named, archived proposal is cited for what it 'identified' and 'concluded',
    without a link or location. The reader cannot check that it reached the by-claim
    partition conclusion attributed to it.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/prose/orphan-references.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/prose/orphan-references.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/57950006897f2a4bcba30284/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/57950006897f2a4bcba30284/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: be5d160b4a174e6cb56e033b12532e2d
completed-at: '2026-11-16T22:37:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/be5d160b4a174e6cb56e033b12532e2d/outputs/review-orphan-references.md
raw-output-sha256: 6629801438bde5dd0bd9a7b62447706240a36714445e0d00f9e000a966551b86
format: 2
---

# Review

Most specific figures are anchored. The paired-experiment numbers (twelve notes, a five-link cap, four findings, six/eleven/fourteen/sixteen artifacts) are attached to a linked retained report. The later "twenty-two artifacts and 322 kilobytes" figure is explicitly placed "in the same experiment". ADR 046, 073 and 079 are linked. The Descartes and Lamport quotations cite their ingests and sections.

Three specific references lack a source or enough context: the corpus count, the self-disagreement measurement and the archived proposal. The corpus count carries the most weight, because the section "The two bounds come apart in the corpus" rests on it. Each reference is local and fixable by a link or a method statement, so the result is WARN.
