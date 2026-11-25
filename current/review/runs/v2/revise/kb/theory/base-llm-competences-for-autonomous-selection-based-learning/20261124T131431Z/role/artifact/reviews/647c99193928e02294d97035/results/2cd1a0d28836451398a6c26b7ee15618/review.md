---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Clearing these competences is proposed as necessary for operating the loop autonomously,
    not sufficient for sustained continual learning.
  reason: SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md
    — the article needs a premise that fixed-weight selection depends on a frozen
    base model already above a "competence floor needed to operate the loop", and
    treats that floor as a precondition rather than a guarantee. The note's Scope
    states the competences as necessary for autonomous operation and not sufficient,
    which matches the article's conditional use ("If the bet holds above that floor").
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md
    — the article needs the claim that harness code handles much of the loop's machinery
    (validators, traces, replay, bloat tracking, rollbacks) while three named semantic
    competences stay on the frozen model, framed as a working hypothesis. The note
    supplies the offload list, the three competences under the same names, and the
    same working-hypothesis framing; the article's footer entry cites the note for
    the same "working hypothesis on the base-model floor".
- scope: passage
  quotes:
  - an inadequate base model can block outer-loop learning before the store itself
    saturates
  reason: PARTLY SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md
    — the article asserts, beside its link, that "Below that competence floor, edits
    to prompts or tools cannot substitute for capabilities the loop itself needs;
    weight training still builds the base learner." The note supplies only a bounded
    illustration (weak models gained nothing under one harness-evolution loop on one
    benchmark). It does not state the general claim that prompt or tool edits cannot
    substitute below the floor, and it says nothing about weight training building
    the base learner; the note's own Open Questions even ask how far better harness
    interfaces can lower the floor.
- scope: document
  quotes: []
  reason: 'DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md
    — the article''s second passage restates the note''s core: the harness offload
    list (codified validators, trace capture, replay, bloat tracking, rollbacks) and
    the three competences in near-identical wording (interpreting unformalized text
    into action; diagnosing novel failures and synthesizing candidate fixes in text
    or code; judging unformalized trade-offs while recognizing missing evidence).
    The article''s one-sentence version serves its external readers'' need for the
    gist; the note''s version is the better statement for any reader who must apply
    the split, since it gives each competence''s scope, its linked mechanism, and
    the reassignment of store maintenance and criterion revision.'
outcome: report
description: Retained report review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: 1181f261a8ee86614d6e432a316715fe90534ea271ad19b4783ed89c9cea04b3
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/role/calls/launches/2cd1a0d28836451398a6c26b7ee15618/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/role/artifact/reviews/647c99193928e02294d97035/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/role
launch: 2cd1a0d28836451398a6c26b7ee15618
completed-at: '2026-11-24T13:24:05Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/role/calls/launches/2cd1a0d28836451398a6c26b7ee15618/outputs/review.md
raw-output-sha256: d41ce3b7cfc4fe234a9d44970483be66b4984fcd032bb9c1c9563a7350f2a249
format: 2
---

# Role in the KB: base-llm-competences-for-autonomous-selection-based-learning

## Role
The note supplies the "base-model floor" premise for the lead article on continual learning with fixed weights: the article argues its bet holds only above a competence floor and cites this note for what that floor consists of. It is the article's only stated basis for splitting loop work between harness code and three semantic competences of the frozen LLM; no theory note argues from it.
Relied on: the harness-offload claim; the three named competences; the working-hypothesis framing; the "necessary, not sufficient" scope; the base-model-floor idea. Unused: the reduction of store maintenance and criterion revision to competences 2 and 3; the claim that the competences fail independently at different thresholds and the human-assisted bootstrap; the revisability clause in Scope; both Open Questions; the specific links to operative change, diagnostic richness and on-balance judgment.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` — three passages: the floor as a precondition of the bet, the restated offload/three-competence split, and a footer citation. It needs the premise and the split (supplied) and leans on the note for a below-floor claim about prompt/tool edits and weight training (partly supplied).

Only one file links to the note; no cap cut files or passages.

## Duplication
The article restates the offload list and the three competences nearly verbatim. The note is the fuller statement for applying the split; the article's compressed sentence suffices for its own purpose of naming the floor.

## Untaken recommendations
None. The only linking file is an article, and its passages recommend no change to the note.

## Reach
- The names and wording of the three competences, and the list of harness-offloadable jobs, reach the article, which restates them.
- The working-hypothesis status and the "necessary, not sufficient" scope reach the article, whose argument is conditional on the floor.
- The weak-model illustration and the "base-model floor" phrasing reach the article's below-floor sentence, which already says more than the note does.
- The criterion-revision reduction, the independence and bootstrap paragraph, the Scope revisability clause and the Open Questions reach no dependent.
