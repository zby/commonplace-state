---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning."]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — needs a premise: fixed-weight selection depends on a frozen base model above a \"competence floor needed to operate the loop\". The note states the competences as necessary, not sufficient, for autonomous operation, which matches the article's use of a floor that bounds rather than guarantees the bet."
  - scope: passage
    quotes: ["our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — needs the claim that three semantic competences stay on the frozen model, named as interpreting unformalized text into action, diagnosing novel failures and synthesizing candidate fixes in text or code, and judging unformalized trade-offs while recognizing missing evidence. The note's numbered list supplies all three in the same sense and with the same working-hypothesis status the article gives them."
  - scope: passage
    quotes: ["Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."]
    reason: "PARTLY SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the linking passage continues: \"Below that competence floor, edits to prompts or tools cannot substitute for capabilities the loop itself needs; weight training still builds the base learner.\" The note supports the first half only as a bounded illustration from one benchmark and loop; it does not state the general non-substitution claim, and it says nothing about weight training building the base learner."
  - scope: passage
    quotes: ["not an established impossibility result"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — its reading list cites the note as \"our working hypothesis on the base-model floor\". The note's title and Scope section frame the split as a working hypothesis about the base-model floor, so the citation gets what it labels."
  - scope: document
    quotes: []
    reason: "DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article restates the note's harness-offload list (\"enforcing codified validators, capturing traces, replaying past cases, tracking bloat, and executing rollbacks\") and the three competences in one sentence each. The note states them better for a reader who must judge the split, because it groups the harness jobs into enforcement, evidence capture and store bookkeeping and gives each competence its condition and link; the article's compression suits its own external-reader summary."
outcome: report
---

# Role: Harness code may offload much of a selection loop, leaving three base LLM competences

## Role
The note supplies one article with its base-model competence floor: the premise that fixed-weight selection-based learning works only above a floor of three semantic competences that harness code cannot take over. Only the lead article `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` links to it, three times; no theory note argues from it.
Relied on: the harness-offload split, the three named competences, the floor as a necessary condition for autonomous operation, and the working-hypothesis status. Unused: the store-maintenance and criterion-revision reduction to competences 2 and 3, the independent-failure and human-assisted-bootstrap paragraph, the detailed harness job groups (ablations, bisects, coverage annotation), and the open questions.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` — needs the floor premise, the three competences, the harness-offload list, and a citation for the working hypothesis; it also attaches a stronger claim about non-substitution and weight training to the link.

## Duplication
The article restates the harness-offload list and the three competences in compressed form. The note's version is fuller and carries the conditions; the article's suits its summary role.

## Untaken recommendations
None.

## Reach
- The names and boundaries of the three competences reach the article, which lists them by name.
- The harness-offload list (validators, trace capture, replay, bloat tracking, rollback) reaches the article, which restates it.
- The working-hypothesis status and the "necessary, not sufficient" scope reach the article's framing of the bet and its reading-list label.
- The title's claim reaches the article's reading list, which quotes it as link text.
- The criterion-revision reduction, the bootstrap paragraph and the open questions reach no dependent.
