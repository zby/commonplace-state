---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning."]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's scope disclaimer needs a premise: fixed-weight selection depends on a frozen base model already above the 'competence floor needed to operate the loop'. The note's Scope states that clearing the three competences is necessary, not sufficient, for operating the loop autonomously, which matches the article's conditional framing. The note uses 'base-model floor' only in its evidence paragraph and Open Questions, not as a defined term, but the necessary-condition claim the article relies on is explicit."
  - scope: passage
    quotes: ["our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article names and paraphrases the three competences (interpreting unformalized text into action; diagnosing novel failures and synthesizing candidate fixes in text or code; judging unformalized trade-offs while recognizing missing evidence) and labels the split a working hypothesis. The note's numbered list supplies all three under the same names and the same hedge."
  - scope: passage
    quotes: ["harness code can take over much of the loop's machinery"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article needs the claim that harness code handles much of the loop's machinery (enforcing codified validators, capturing traces, replaying past cases, tracking bloat, executing rollbacks). The note's three bullet categories (enforcement and context assembly; evidence capture and replay; store bookkeeping) cover each item the article lists."
  - scope: passage
    quotes: ["an inadequate base model can block outer-loop learning before the store itself saturates"]
    reason: "PARTLY SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article attaches to its link the consequence 'Below that competence floor, edits to prompts or tools cannot substitute for capabilities the loop itself needs; weight training still builds the base learner.' The note supplies the first half through the semantic-work-relocation claim and the bounded harness-evolution evidence. It does not state that weight training is what builds or raises the base learner; that appears only in the linked ingest's title, not in the note's text."
  - scope: document
    quotes: []
    reason: "DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's second passage restates the note's core in one paragraph: the harness offloading list, the 'working hypothesis' hedge, and the three competences in near-identical wording. The note states it better for reuse because it groups the harness work into categories, explains each competence and grounds it in a linked concept, and bounds the claim in Scope; the article's compressed version suits its external lead-article reader and defers to the note via the link."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's further-reading list cites the note by its title as 'our working hypothesis on the base-model floor'. The note's title, opening 'Working hypothesis' label and Scope supply that characterization."
outcome: report
---

# Role in the KB: Harness code may offload much of a selection loop, leaving three base LLM competences

## Role
The note is the premise behind the base-model-floor condition in one lead article, `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`, which links it three times: as the scope condition for its fixed-weight bet, as the source of the harness/LLM split and the three named competences, and as further reading. The note has no other inbound links under `kb/`, so its role is to ground and elaborate a conditional that this one article argues from.
Relied on: the harness-offloading claim, the three named competences, the "working hypothesis" framing, and the necessary-but-not-sufficient floor for autonomous operation. Unused: the reduction of store maintenance and criterion revision to competences 2 and 3; the independent-failure and different-threshold claim with the human-assisted bootstrap; the Harness Evolution Hits a Ceiling evidence; and the Open Questions.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` needs a premise (frozen base model above a competence floor), a claim (harness code takes much of the loop's machinery), a term set (the three competences), and a consequence (below the floor, prompt or tool edits cannot substitute and weight training builds the base learner). The note supplies all of these except the weight-training consequence, which it only partly supplies.

## Duplication
The article's second inbound passage restates the note's harness list and three competences almost verbatim. The note is the fuller statement: it categorizes the harness work, explains each competence with a linked concept, and bounds the claim. The article's version is a compressed summary that points to the note.

## Untaken recommendations
None. The only linking file is an article, and its passages make no recommendation to change the note.

## Reach
- Changing the three competences' names, count, or the "irreducible" / "working hypothesis" framing reaches `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`, which names all three and repeats the hedge.
- Changing the harness-offloading claim or its listed jobs (validators, traces, replay, bloat tracking, rollbacks) reaches the same article, which lists those jobs.
- Changing the Scope claim that the competences are necessary for autonomous operation reaches the article's scope disclaimer and its "above that floor" conditional.
- Changing the note's title reaches the article's further-reading entry, which quotes it.
- The criterion-revision reduction, the independent-failure and bootstrap paragraph, the harness-evolution evidence and the Open Questions reach no dependent.
