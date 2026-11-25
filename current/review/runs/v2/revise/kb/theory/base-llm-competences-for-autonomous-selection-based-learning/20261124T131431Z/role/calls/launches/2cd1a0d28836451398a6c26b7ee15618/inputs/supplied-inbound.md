# Inbound contexts of `kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md`

1 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/workflow-state/, kb/work/, hidden directories and the note itself.

## `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`

- Title: Continual Learning with Fixed Model Weights: LLM-Selected Updates Without a Single Score
- Description: Lead article: the bet that autonomous selection-based learning over text, hypotheses, and code can clear four continual-learning bars with fixed weights without a single score, plus its base-model floor, Bitter Lesson scaling, and hypothesis payoffs

> This is not a claim that fixed-weight selection can learn anything; it depends
> on a frozen base model already above the
> [competence floor needed to operate the loop](../theory/base-llm-competences-for-autonomous-selection-based-learning.md),
> detailed below. If the bet holds above that floor, a fully automated loop can
> sit on the compute side of the Bitter Lesson, and retaining testable
> hypotheses alongside winning updates may buy sample efficiency under
> structured shifts plus bounded, testable explanations of what the system
> learned.

> Closing this loop autonomously still depends on what the frozen weights supply
> up front. Harness code can handle much of the loop's machinery—enforcing
> codified validators, capturing traces, replaying past cases, tracking bloat,
> and executing rollbacks—but our working hypothesis is that
> [three irreducible semantic competences remain on the frozen base LLM](../theory/base-llm-competences-for-autonomous-selection-based-learning.md):
> interpreting unformalized text into action, diagnosing novel failures and
> synthesizing candidate fixes in text or code, and judging unformalized
> trade-offs while recognizing missing evidence. Below that competence floor,
> edits to prompts or tools cannot substitute for capabilities the loop itself
> needs; weight training still builds the base learner. Above that floor, the
> two arguments below are conditional on the bet holding.

> - [Harness code may offload much of a selection loop, leaving three base LLM competences](../theory/base-llm-competences-for-autonomous-selection-based-learning.md)
>   and
>   [Credit assignment without a chain rule is a debugging problem over an interdependent store](../theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md)
>   — our working hypothesis on the base-model floor and how debugging governs credit assignment as the store grows.
