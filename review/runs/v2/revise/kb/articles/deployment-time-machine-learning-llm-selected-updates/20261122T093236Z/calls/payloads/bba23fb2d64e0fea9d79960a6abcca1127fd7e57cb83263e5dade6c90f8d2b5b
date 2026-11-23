---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 11dc69181fe0448e92a191477673a3f7
completed-at: '2026-11-22T09:34:02Z'
findings:
- scope: passage
  quotes:
  - represents the hard-oracle extreme
  reason: '"Hard-oracle" is used without definition. The reader must infer from the
    later sentences that it means an admission test that accepts a change only on
    formal proof. Either gloss it ("the extreme where a change is admitted only by
    a strict, infallible-in-form check") or replace it with that plain description.'
  level: warn
- scope: passage
  quotes:
  - edits to the system's own readable, addressable store
  reason: '"Addressable" corresponds to the active vocabulary term addressable theory,
    but its first meaningful mention has neither a gloss nor a link. The link appears
    later in the comparison table, still without a gloss. A short gloss at first mention
    (for example, "whose entries can each be pointed to and edited individually")
    plus the definition link would let an external reader keep going.'
  level: warn
- scope: passage
  quotes:
  - and it is double-loop when it can
  reason: Double-loop is active vocabulary. Its first mention is glossed inline ("also
    revise what it selects by"), but the definition link appears only in the closing
    reading list. Adding the link at first mention would meet the gloss-plus-link
    convention.
  level: info
- scope: passage
  quotes:
  - 'confuses **production method** with **representational

    form**'
  reason: Representational form is active vocabulary. The following sentences let
    the reader infer the meaning (whether the retained result lives in weights or
    in other forms), and the sentence links to a theory note, but there is no explicit
    gloss and no link to the definition note.
  level: info
- scope: passage
  quotes:
  - an automated harness-evolution loop
  reason: '"Harness" (the code and prompts surrounding a model) is not defined. Agent
    practitioners will know it; ML readers addressed by this section may not. A few-word
    gloss would remove the doubt.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/11dc69181fe0448e92a191477673a3f7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/0ba57e35ba1ca6cdf6c34c54/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/11dc69181fe0448e92a191477673a3f7/outputs/review-undefined-terms.md
raw-output-sha256: 4363922817ea6a2015f1ac9329c53aa1de3338eac39cfecc8cf38f2200524ea4
---

# Review

Most technical terms are defined well at first encounter. Selection-based learning, the preference model, robust comparison, self-improving system, targeted correction, single-loop learning, workshop, operative change, the Bitter Lesson, stochastic dominance and the theory-builder special case are each glossed inline. The opening is careful to define its central terms before using them.

Two first encounters leave the reader without a local meaning. "Hard-oracle extreme" is new jargon that the Gödel machine paragraph only explains indirectly. "Addressable" is an active vocabulary term introduced in the opening without gloss or link, and the later table link still lacks a gloss. Both warrant a fix before an external reader meets them. The info findings concern active vocabulary that is understandable in context but lacks the definition link at first mention, and one field term ("harness") that some of the intended readers may not know.
