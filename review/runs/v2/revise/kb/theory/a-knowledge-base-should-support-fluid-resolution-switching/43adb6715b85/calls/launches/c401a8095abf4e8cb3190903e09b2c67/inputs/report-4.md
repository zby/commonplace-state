---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/synthesis
launch: 5d8865fb62564e61a93f5803cd88de97
completed-at: '2026-11-16T22:32:56Z'
findings:
- scope: document
  quotes: []
  reason: 'The note repeats that the criterion is qualitative and task-relative in
    four places: the opening qualifier, the sentence after the four questions, the
    second Boundaries paragraph and the Open questions. Each repeat rules out a misreading
    an earlier sentence has already ruled out, so the reader keeps meeting defensive
    caveats instead of new content. A revision could keep the opening qualifier and
    the Open questions, add backlinks to the third question''s list of routes, and
    delete the post-question caveat and the second Boundaries paragraph.'
- scope: passage
  quotes:
  - asks whether a reader can move among the views a task needs without paying avoidable
    transition cost or losing the relationship between them
  reason: 'The criterion''s sharpest statement has two conditions: low transition
    cost and a preserved relationship between views. It appears only after the mechanism
    inventory, under a second label, ''resolution-switching fluidity''. The opening
    states the cost condition but not the relationship condition, so a reader first
    meets the full claim halfway through the note. A revision could state both conditions
    in the second opening paragraph and let the criterion section reuse that statement
    and the existing term.'
contract: report
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/synthesis/artifact/reviews/077cc509aa56b152faf196fe/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/synthesis/artifact/reviews/077cc509aa56b152faf196fe/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/synthesis/calls/launches/5d8865fb62564e61a93f5803cd88de97/outputs/review.md
raw-output-sha256: 09e3dd1445ba6ae86bb65b4710c4936fc9bf34d56a1d2f3a40d6322f0d6407f6
---

# Simplification synthesis: A knowledge base should support fluid resolution-switching

The note is compact, and its central claim appears early. Three of the four
checks passed. The remaining value is structural: the scope caveats are spread
across the note, and the full criterion is stated only in the middle. The
abstraction caveat in the link-context paragraph, which two checks flagged as
INFO, is a one-sentence local trim. It falls below this synthesis's threshold.

## Opportunities

### 1. Consolidate the qualitative and task-relative caveats

- Location: opening, "This is a qualitative design criterion, not yet a metric
  or a claim that every task needs the same sequence of views"; The evaluative
  criterion, "These questions identify possible friction. They do not yet supply
  a scoring rule or universal threshold."; the second paragraph of Boundaries,
  "An artifact does not need an outbound link in every case. … Fluidity is
  relative to the task and to the navigation operations actually available to
  the reader."; and the second Open question.
- Combines: both WARN findings from marginal-value-redundancy (the post-question
  caveat and the second Boundaries paragraph).
- Reader problem: the same limitation appears four times. A reader cannot tell
  whether each repeat adds a new restriction, and the section ends in caveats
  rather than in the distinction from neighbouring concepts.
- Direction: keep the opening qualifier as the single statement of status and
  task-relativity. Add backlinks to the third question's routes ("an authored
  link, index, backlinks, or search"). Delete the post-question sentence and the
  second Boundaries paragraph. Boundaries would then hold only the distinctions
  from grain, pointer accuracy and retrieval recall.
- Preserve or decide: two phrases may carry points the opening does not quite
  cover. The author should decide whether to fold them into the opening or let
  them go. "Universal threshold" says more than "not yet a metric": a metric
  could still exist without one fixed cutoff. "Nor does every task need to return
  to a broad view after reading detail" qualifies the bidirectional claim
  itself, not just the sequence of views. If the author means the "both
  directions" requirement as a capability the KB offers rather than a path every
  task follows, that should stay explicit near the opening claim. The second Open
  question assumes the reader already knows that search or backlinks can supply
  the outward route, so the third question must name them once the Boundaries
  paragraph is gone.

### 2. State the full criterion in the opening

- Location: The evaluative criterion, "**Resolution-switching fluidity** asks
  whether a reader can move among the views a task needs without paying
  avoidable transition cost or losing the relationship between them", compared
  with the opening's second paragraph, "A knowledge base should make
  task-relevant switches inexpensive in both directions."
- Combines: the INFO finding from core-claim-obscured.
- Reader problem: the opening gives the cost condition and the return route,
  but not the condition that the transition keeps the relationship between views.
  That condition appears first in the link-context paragraph and is stated as
  part of the criterion only after the inventory, under a newly coined term.
  So the reader assembles the claim in stages and meets two labels for one idea.
- Direction: add the relationship condition to the second opening paragraph,
  so the claim reads as cheap transitions that keep their relationship. The
  criterion section could then introduce the four questions directly and not
  restate the criterion under a new name. One possible resolution, offered only
  as an illustration: "A knowledge base should make task-relevant switches
  inexpensive in both directions without losing why the two views belong
  together."
- Preserve or decide: decide whether "resolution-switching fluidity" names a
  distinct concept, an evaluative property of the KB as opposed to the reader's
  operation, or just restates the title's "fluid". If it is distinct, keep the
  term and define it in the opening. If not, reuse "resolution-switching". The
  link-context paragraph and the fourth question both rely on the relationship
  condition, so it is part of the note's claim and must survive any compression
  of the opening.
