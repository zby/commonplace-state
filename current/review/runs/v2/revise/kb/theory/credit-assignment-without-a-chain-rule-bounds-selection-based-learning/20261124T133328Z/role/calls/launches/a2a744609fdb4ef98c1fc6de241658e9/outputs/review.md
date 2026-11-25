---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Selection-based learning](./definitions/selection-based-learning.md) over a store of instructions, hypotheses, checks, and scripts has no chain rule, so its credit assignment is far less scalable than gradient learning. Yet that does not block full automation: large software codebases have no chain rule either, and engineers and coding agents routinely localize faults across hundreds of interdependent modules by **debugging**"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's first passage needs the premise that credit assignment by debugging is far less scalable than backpropagation across coupled weights, yet coding agents already automate much of that debugging on large codebases. The note's opening paragraph states both halves of that contrast."
  - scope: passage
    quotes: ["What makes a mixed prose-and-code store harder to debug than ordinary software is not the lack of gradients, but three properties that weaken ordinary debugging tools"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article needs the distinction that a store mixing code with natural-language instructions has softer traces, coupling and failures. The note's three listed properties (softer traces, implicit coupling, noisier diffuse failures) supply exactly that triple. The article frames reliability under these conditions as an open question; the note's first Open Question carries the same question, while its body leans further, calling debugging 'a plausible path to fully automated credit assignment', which the article's 'working hypothesis' label accommodates."
  - scope: passage
    quotes: ["Scaling credit assignment therefore turns on making the retained store **debuggable**"]
    reason: "SUPPLIED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's reading list cites the note as the working hypothesis on 'how debugging governs credit assignment as the store grows'. The note's second paragraph (interdependence growing with store size) and its conclusion that scaling turns on store debuggability supply that claim."
  - scope: document
    quotes: []
    reason: "DUPLICATED — kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md — the article's first passage restates the note's core claim in compressed form: debugging is less scalable than backpropagation, coding agents already automate it on deterministic codebases, and prose-heavy stores have softer traces, coupling and failures. The article's version suits its use as a one-paragraph pointer within a broader argument; the note states the mechanism (what each weakened debugging tool is and why) that the summary depends on."
outcome: report
---

# Role in the KB: Credit assignment without a chain rule is a debugging problem over an interdependent store

## Role
The note is cited by one dependent, the lead article on continual learning with fixed model weights, which uses it as the KB's statement of a key open challenge to scaling selection-based learning. The article relies on its framing of credit assignment as debugging, its contrast with backpropagation and with debugging of ordinary codebases, and its claim that prose instructions weaken traces, coupling and failure isolation. No theory note argues from it.
Relied on: credit assignment as debugging; far less scalable than backpropagation; coding agents already debug large codebases; softer traces, implicit coupling and noisier failures in mixed prose-and-code stores; debugging governs credit assignment as the store grows. Unused: credit assignment as the backward inverse of validation radius; the naive workarounds (local exceptions, trusting rationales, exhaustive ablation); the specific debuggability mechanisms (execution traces, near-decomposability, addressable theory, targeted replay, codification into scripts); the Scope section; the second Open Question.

## Dependents
- `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md` — needs the debugging-vs-backpropagation contrast, the three properties that soften debugging in prose-heavy stores, and the claim that debugging governs credit assignment as the store grows. All supplied.

## Duplication
The article's "key open challenge" paragraph restates the note's core claim in compressed form. The note states the mechanism better; the article's summary is adequate for its pointer role.

## Untaken recommendations
None.

## Reach
- The claim that debugging-based credit assignment is far less scalable than backpropagation yet already automated by coding agents on codebases reaches `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`.
- The three softening properties (traces, coupling, failures) reach the same article, which names all three.
- The framing of the problem as debugging over a growing store, and the note's title wording, reach the same article, which quotes the title as link text in its reading list and calls the note a "working hypothesis"; a shift toward a more confident or more pessimistic conclusion would strain the article's "open challenge" framing.
- Validation-radius inversion, the naive workarounds, the specific debuggability mechanisms and the Scope section reach no dependent.
