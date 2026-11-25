---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - an autonomous [selection-based learning](./definitions/selection-based-learning.md)
    loop does not need the frozen LLM
  reason: Selection-based learning is an active vocabulary term, so it needs an inline
    gloss at its first meaningful mention, not just a link. The previous sentence
    describes updating a store while weights stay fixed, but it never says that this
    is selection-based learning, and it never names the selection step (keeping or
    discarding candidate changes by tests). Add a short gloss, e.g. 'a loop that improves
    by proposing candidate changes to the store and keeping those that survive tests'.
  level: warn
- scope: passage
  quotes:
  - Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md),
    harness code can take over
  reason: '''Scheduler–LLM separation'' is a KB-internal principle, introduced only
    by a link. The sentence depends on it (''Following ...''), yet the reader is not
    told what is separated from what or why. A one-clause gloss would fix it, e.g.
    ''the principle that deterministic code, not the model, should handle bookkeeping
    and control flow because code errors are easier to catch''.'
  level: warn
- scope: passage
  quotes:
  - while transfer tests check each kind of decision on its own
  reason: '''Transfer tests'' is used as if the reader already knows it. The note
    does not say what is transferred to where, for example whether a competence demonstrated
    with human help carries over to unassisted runs or to new cases. Gloss the term
    or replace it with a plain description.'
  level: warn
- scope: passage
  quotes:
  - an inadequate base model can block outer-loop learning before the store itself
    saturates
  reason: '''Outer-loop learning'' appears here for the first time in the body (otherwise
    only in a link title) and is never defined. A reader can guess that it means the
    selection loop described above, but the note does not say so. Use ''the selection
    loop'' or gloss ''outer loop'' as the loop that revises the store around a fixed
    model.'
  level: warn
- scope: passage
  quotes:
  - ([diagnostic richness](./diagnostic-richness-constrains-outer-loop-learning-quality.md))
  reason: '''Diagnostic richness'' is a link-only parenthetical with no gloss. The
    competence remains understandable without it, but a reader cannot tell what the
    term adds. A brief gloss such as ''how much causal detail the evidence exposes''
    would help.'
  level: info
- scope: passage
  quotes:
  - store-level maintenance and [criterion revision](./definitions/single-loop-and-double-loop-learning.md)
    do not require
  reason: '''Criterion revision'' links to the single-loop/double-loop definition
    but has no gloss, and it does not use the active term ''double-loop''. Plain English
    and the later phrase ''proposing a revised check'' partly recover its meaning,
    so this is minor. A short gloss, e.g. ''changing the checks the loop selects against
    (double-loop learning)'', would make the link to the definition explicit.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/e082a1070c3c4fb8a00ccfafd9d4d2ed/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/17a719a9398d6f2f4d3b51d2/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: e082a1070c3c4fb8a00ccfafd9d4d2ed
completed-at: '2026-11-24T13:15:38Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/e082a1070c3c4fb8a00ccfafd9d4d2ed/outputs/review-undefined-terms.md
raw-output-sha256: 6f5dc52ad9af961a54a23e909188984869d8eb7b0d984cb5741a575525fc4a67
format: 2
---

# Review

## Summary

The note introduces several KB-internal concepts mainly through links. Four first mentions leave the sentence harder to follow without the linked note:

- "selection-based learning", which is active vocabulary and needs a gloss as well as its link;
- "scheduler–LLM separation", which the sentence explicitly depends on;
- "transfer tests";
- "outer-loop learning".

Two more link-only terms, "diagnostic richness" and "criterion revision", are recoverable from context and are recorded as info.

Several other terms pass because the surrounding text defines or paraphrases them. "Operative change" sits in a sentence that already states the requirement (prose must "govern its behavior"). "Base-model floor", "human-assisted bootstrap" and "harness-evolution loop" are inferable from plain English. "Harness code" is grounded by the concrete jobs listed in the opening bullets.
