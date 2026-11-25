---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning."]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — its framing passage needs a 'competence floor needed to operate the loop' that the frozen base model must already clear before the fixed-weight bet applies. The note supplies a necessary-not-sufficient floor for autonomous operation, framed as a working hypothesis, which matches the article's conditional use ('If the bet holds above that floor')."
  - scope: passage
    quotes: ["three irreducible semantic competences remain on the frozen base LLM"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — its base-model-floor passage needs the claim that harness code handles much of the loop's machinery while three named semantic competences stay on the frozen LLM, held as a working hypothesis. The note's three bullets of offloadable machinery and its numbered list of the three competences supply this; the article's wording of each competence matches the note's headings."
  - scope: passage
    quotes: ["Even within one benchmark and loop, an inadequate base model can block outer-loop learning before the store itself saturates."]
    reason: "PARTLY SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the sentence after the linked clause states that below the floor 'edits to prompts or tools cannot substitute for capabilities the loop itself needs; weight training still builds the base learner.' The note supplies a bounded illustration that weak base models produced no held-out gains under one harness-evolution loop, but it does not state the general non-substitutability claim, and it says nothing about weight training building the base learner. The article's sentence is not itself linked, so whether it leans on the note here is inferred from adjacency."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — its reading-list entry needs only a citation: 'our working hypothesis on the base-model floor'. The note's title, description and 'Working hypothesis' framing supply that."
  - scope: document
    quotes: []
    reason: "DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's base-model-floor passage restates the note's offloading list (enforcing codified validators, capturing traces, replaying past cases, tracking bloat, executing rollbacks) and its three competences in one sentence each. The note states them better for argument, since it gives each competence's content, its grounding link and the separability claim. The article's compressed version is better for its external readers, who need only the names and the conditional."
outcome: report
---

# Role in the KB: Harness code may offload much of a selection loop, leaving three base LLM competences

## Role
The note supplies the "base-model floor" that the lead article on fixed-weight continual learning makes its bet conditional on: harness code can take over much of the loop, but three named semantic competences stay on the frozen LLM, and clearing them is necessary for operating the loop autonomously. Only that one article links to it, and it cites it in three places: the framing condition, a summary of the offload/competence split, and a reading-list entry. No dependent argues from the note's finer structure.
Relied on: the working-hypothesis status; "base-model floor" / competence floor as necessary for autonomous operation; the list of harness-offloadable machinery; the names of the three competences. Unused: the reduction of store maintenance and criterion revision to competences 2 and 3; the claim that the competences fail independently at different thresholds and the human-assisted bootstrap that follows from it; the scheduler–LLM grounding; the open questions.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` — needs the competence floor as a precondition of its bet, the offload/three-competence split as a summarized working hypothesis, and a citation in its reading list. It also places an adjacent claim, that below the floor prompt or tool edits cannot substitute and weight training still builds the base learner, beside the link.

## Duplication
The article restates the note's harness-offload list and the three competences in compressed form. The note's version is the fuller statement for anyone arguing from the split; the article's suits its external readers. The two currently agree in wording.

## Untaken recommendations
None. The single linking file is an article, not a source ingest, and makes no recommendation for changing the note.

## Reach
- The working-hypothesis status and the necessary-for-autonomous-operation floor reach `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`, whose bet ("If the bet holds above that floor") is conditional on them.
- The list of offloadable harness work and the names and number of the three competences reach the same article, which restates them; the note's title, which encodes "three", also appears verbatim in the article's reading list.
- The bounded weak-model illustration reaches the same article only through its adjacent, unlinked non-substitutability sentence.
- The criterion-revision reduction, the independence and threshold claim, the bootstrap, and the open questions reach no dependent.
