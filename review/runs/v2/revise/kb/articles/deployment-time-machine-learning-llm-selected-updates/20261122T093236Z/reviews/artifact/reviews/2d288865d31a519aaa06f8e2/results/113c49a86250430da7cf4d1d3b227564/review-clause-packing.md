---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'That buys an optimality guarantee conditional on those axioms and that utility,
    at a steep price: the machine must ignore every useful improvement it cannot prove,
    and a valid proof does not establish that the axioms adequately describe the real-world
    domain—under an inadequate formalization, a proved switch need not deliver what
    its user wanted.'
  reason: 'About 55 words carrying four ideas: the conditional guarantee, the price
    of ignoring unprovable improvements, the gap between a valid proof and adequate
    axioms, and the consequence for the user. The colon and the dash open two nested
    continuations. Split after ''cannot prove'' and start a new sentence at ''A valid
    proof does not establish…''.'
  level: warn
- scope: passage
  quotes:
  - It requires the model not only to compare proposed edits and diagnose which retained
    edit caused a later failure, but also to recognize when an existing gate, validator,
    or review criterion is misleading and revise it
  reason: About 48 words with four required capabilities in a not-only/but-also frame,
    followed by a 'while' clause about the fixed objective and a parenthetical link.
    The reader must hold the 'not only' branch open across the whole list. Put the
    fixed-objective condition in its own sentence, or list the capabilities without
    the not-only/but-also frame.
  level: warn
- scope: passage
  quotes:
  - Yet the authors' own diagnosis attributed the stall to what the proposer was not
    shown (its scorer saw a failure mode in a quarter of runs that never reached the
    proposer), though their single remedy run stayed within noise.
  reason: 'About 40 words: the diagnosis, a parenthetical with its own relative clause,
    and a concessive ''though'' clause about the remedy run. The parenthetical interrupts
    the main clause before the concession. Move the parenthetical content into its
    own sentence and give the remedy-run result a separate sentence.'
  level: warn
- scope: passage
  quotes:
  - When compatible value functions pull in opposite directions or evidence has not
    yet arrived, the comparison stays open—and the system can still act as a bounded
    decision, using
  reason: 'About 42 words with four pieces: two alternative open conditions, the open
    verdict, the permission to act, the reversibility mechanism with its link, and
    a back-reference to the example. Ending the sentence after ''stays open'' and
    starting a new one for acting under reversibility keeps every relation.'
  level: warn
- scope: passage
  quotes:
  - So the comparison is between two states of the system that differ only in what
    the change did, whether it added, revised or removed content, with entries that
    depend on it adjusted to match.
  reason: A relative clause, an appended 'whether' alternation, and a trailing absolute
    phrase about dependent entries stack onto one noun phrase. Each addition qualifies
    the two states differently, and the trailing 'with … adjusted to match' is far
    from the noun it modifies. Split the adjustment of dependent entries into its
    own sentence.
  level: warn
- scope: passage
  quotes:
  - 'Companion drafts in this collection—written before this framing was adopted and
    currently being re-anchored from the narrower *theory builder* special case (where
    the store holds explicit, criticized theories):'
  reason: 'Distance problem: a long dash clause with a nested parenthetical separates
    the subject ''Companion drafts'' from the three linked titles it introduces. Reorder:
    name the three drafts first, then say they predate this framing and are being
    re-anchored from the theory-builder case.'
  level: warn
- scope: passage
  quotes:
  - On later tasks, the new line directs proposal writes accurately—until a longer
    maintenance run fails because the rule matched a migration plan that belonged
    instead in a
  reason: Under the word threshold but chains 'until … because … that …' and then
    an appositive gloss of 'workshop'. Readable as narrative, but the appositive could
    move to its own short sentence.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/sentence/clause-packing.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/review-gates/sentence/clause-packing.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/2d288865d31a519aaa06f8e2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 113c49a86250430da7cf4d1d3b227564
completed-at: '2026-11-22T09:37:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/113c49a86250430da7cf4d1d3b227564/outputs/review-clause-packing.md
raw-output-sha256: 3d6648a40cb457d086b2596b2074d60894630e010bf66f143a2f00c43b62b9d8
format: 2
---

# Review

## Summary

The article mostly uses short sentences with one point each. Six sentences
exceed the gate's load limit, either by stacking three or more clauses past
about 40 words or by putting a long interruption between a subject and what it
introduces. All six can be reordered or split without losing a relation. They
cluster in the explanatory sections: the Gödel machine precedent, the statement
of the bet, the harness-evolution evidence, the open-comparison clause, the
improvement criterion, and the companion-drafts bullet.

Several other long sentences carry one dependency or a parallel list, such as
the PRODIGY retention sentence and the Bitter Lesson compute list. The gate
tolerates those, so they are not reported.
