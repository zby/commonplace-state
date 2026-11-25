---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["over a store of instructions, hypotheses, checks, and scripts has no chain rule, so its credit assignment is far less scalable than gradient learning. Yet that does not block full automation: large software codebases have no chain rule either, and engineers and coding agents routinely localize faults across hundreds of interdependent modules by **debugging**"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's first passage needs the claim that credit assignment without a chain rule is done by debugging, that this is far less scalable than backpropagation across billions of coupled weights, and that coding agents already automate much of that debugging on large codebases. The note's opening paragraph states all three."
  - scope: passage
    quotes: ["What makes a mixed prose-and-code store harder to debug than ordinary software is not the lack of gradients, but three properties that weaken ordinary debugging tools"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's first passage needs a basis for its open question: whether automated debugging stays reliable when natural-language instructions make traces, coupling and failures softer. The note's three properties (softer traces, implicit coupling, noisier diffuse failures) map one-to-one onto the article's three terms, and the note's first open question poses the same question."
  - scope: passage
    quotes: ["As the store grows, artifacts become interdependent"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's reading-list passage cites the note as the working hypothesis on how debugging governs credit assignment as the store grows. The note's second paragraph ties growth to interdependence, and its debuggability paragraph states what keeps credit assignment tractable at scale."
  - scope: document
    quotes: []
    reason: "DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's first passage restates in four sentences the note's opening contrast with backpropagation, the coding-agent analogy and the three softening properties. The article's version serves its external reader better as a compact statement of the open challenge; the note states it better for anyone who needs the mechanisms, because only the note names the properties' causes and the debuggability levers."
outcome: report
---

# Role in the KB: credit assignment without a chain rule

## Role
The note is the single cited statement, for the lead continual-learning article, of the key open challenge in scaling selection-based learning: credit assignment without a chain rule must be done by debugging, and natural-language artifacts weaken debugging. Only that one article links to it, in two passages: an inline statement of the challenge and a reading-list entry naming it as a working hypothesis. No theory note argues from it.
Relied on: the debugging framing of credit assignment; "far less scalable than backpropagation"; the coding-agent/codebase analogy; the three softening properties (traces, coupling, failures); growth of the store making credit assignment harder; the first open question. Unused: validation radius as the forward inverse of credit assignment; the three naive workarounds (local exceptions, trusting rationales, exhaustive ablation); the debuggability levers (execution traces, near-decomposability and dependency links, addressable theory, targeted replay, codification into scripts); the "plausible path to fully automated credit assignment" conclusion; the Scope bullets; the second open question.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` — needs the debugging claim, its scalability contrast with backpropagation, the coding-agent analogy, the three softening properties as the basis of the open question, and the store-growth hypothesis. All supplied.

## Duplication
The article's first passage restates the note's opening paragraph and its three properties in compressed form. The compact version suits the article's lead-reader use; the note is the better statement of mechanism (see the DUPLICATED finding).

## Untaken recommendations
None. The linking article makes no recommendation to change the note.

## Reach
- The claim that credit assignment without a chain rule is a debugging problem, and its contrast with backpropagation's scale, reach the article's inline passage and its reading-list entry.
- The coding-agent analogy ("coding agents already automate much of that debugging") reaches the article's inline passage.
- The three properties, softer traces, implicit coupling and noisier failures, and the first open question reach the article's open question, which names the same three terms.
- The store-growth framing reaches the article's reading-list gloss ("as the store grows").
- The title reaches the article's reading-list link text, which quotes it verbatim.
- Changes to the validation-radius inverse, the naive workarounds, the debuggability levers, the Scope bullets or the second open question reach no dependent.
