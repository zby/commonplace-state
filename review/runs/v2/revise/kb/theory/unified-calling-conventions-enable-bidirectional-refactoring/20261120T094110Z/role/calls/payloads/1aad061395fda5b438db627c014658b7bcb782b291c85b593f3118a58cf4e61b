---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation"]
    reason: "SUPPLIED — kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md — needs the claim that a common call surface lets components be exchanged, as the landing point its qualification attaches to; the note states that claim."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md — the ingest qualifies the note: 'a common call surface needs semantic mappings, not only shared names'. The note grounds the shared interface in name-based dispatch and says nothing about semantic mappings between the two sides. The passage presents this as a qualification rather than an explicit edit instruction."
  - scope: passage
    quotes: ["if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation"]
    reason: "SUPPLIED — kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md — needs the shared-callable-surface claim that its qualification attaches to; the note states it."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md — the ingest 'adds a useful qualification': sharing a callable surface requires both data mappings and protocol mappings when regimes disagree about values and behavior. The note mentions neither data nor protocol mappings; its interface is the name plus the callable shape."
  - scope: passage
    quotes: ["This requires **name-based dispatch**: components are identified by string name rather than direct object reference."]
    reason: "SUPPLIED — kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md — needs the mechanism (uniform calling convention, name-based dispatch, independently refactorable links) that iii's bus-level function ids are cited as production evidence for, and that a proposed kb/notes/ note would link to as 'mechanism'. The first passage is cut at 1200 characters mid-sentence ('production evidence that name-b'), so part of this dependent's need is unseen."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md — the ingest offers iii's 11→7-state turn-orchestrator rewrite as concrete production evidence for the note, 'which currently grounds the claim only on llm-do'. The note still grounds the claim only on llm-do. The passage tags the edge [just-a-reference], so it may intend only a reference rather than an edit; the cut first passage may say more."
  - scope: document
    quotes: []
    reason: "PARTLY SUPPLIED — kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md — cites the note as 'evidence for why stable interfaces matter' and says the note 'predicts' a brittleness from model/harness co-training overfitting. The note supplies the value of stable call sites for refactoring components, but says nothing about model weights coupling to a harness's interface; the predicted failure mode is not in its text."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md — compares UPML with the note on the shared point that an explicit interface vocabulary is the boundary permitting recomposition; the note's unified interface and name-based dispatch supply the comparison base."
  - scope: passage
    quotes: ["A call to `ticket_classifier` might dispatch to an agent today and a Python function tomorrow"]
    reason: "SUPPLIED — kb/tags/computational-model-README.md — a tag-head citation needing only that the convention lets components move between neural and symbolic implementations; supplied."
  - scope: passage
    quotes: ["A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement."]
    reason: "SUPPLIED — kb/tags/constraining-README.md — a tag-head citation framing the note as 'how to commit reversibly: neural and symbolic components behind the same callable interface'; the shared interface and the switch-back case supply the reversibility."
  - scope: passage
    quotes: ["extract `sanitize_filename()` to Python. The agent still handles ambiguous cases. The call site doesn't change."]
    reason: "PARTLY SUPPLIED — kb/theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md — needs the claim that one can start with a prompt and 'later extract to a skill without changing call sites'. The note supplies call-site stability under extraction, but its extraction target is Python code, not a skill; extraction to a skill is not stated."
  - scope: passage
    quotes: ["Each link can be independently refactored without disturbing the rest."]
    reason: "SUPPLIED — kb/theory/code-complements-weight-prompt-with-symbolic-operations.md — extends the note: needs the claim that movement between model interpretation and symbolic execution is local while the interface is preserved; supplied."
  - scope: passage
    quotes: ["the same name can resolve to either neural or symbolic"]
    reason: "SUPPLIED — kb/theory/llm-context-interprets-instructions-and-content-through-one-medium.md — applies the note's claim that one interface can resolve names to neural or symbolic implementations; stated verbatim in substance."
  - scope: passage
    quotes: ["Local scope — each agent gets only its arguments"]
    reason: "SUPPLIED — kb/theory/llm-context-is-composed-without-scoping.md — cites llm-do as an existing approximation where per-agent system prompts and arguments are frame-local context; the scheduler table's state row supplies the argument-local scope, and the typed-callables section names the per-agent system prompt."
  - scope: passage
    quotes: ["if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation"]
    reason: "SUPPLIED — kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md — needs the claim that refactoring from codified to learned is a local operation, so acting on a relaxing signal is cheap. The note states locality in both directions; its own code-to-prompt examples are extension (step 4) and trial switching rather than replacing brittle code, but the general claim covers the dependent's use."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/theory/reflective-coverage-is-graded-across-representational-forms.md — uses the note as the mechanism that supplies one interface-level mapping, while itself keeping aspect coverage, authority and lineage as separate obligations; the note supplies the interface-level mechanism and claims nothing beyond it that would conflict."
  - scope: document
    quotes: []
    reason: "PARTLY SUPPLIED — kb/theory/research/adaptation-agentic-ai-analysis.md — needs the claim that moving learned behavior between neural, natural-language and symbolic surfaces is cheaper when call boundaries stay stable. The note covers two sides only, and its 'neural' means an LLM-backed prompt (`.agent` file), so the dependent's separate neural (weights) and natural-language surfaces collapse into one in the note; movement into or out of weights is not covered."
  - scope: passage
    quotes: ["implements this through a hybrid VM where agents (`.agent` files, LLM-backed) and tools (Python functions) share a single namespace"]
    reason: "SUPPLIED — kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md — grounds the llm-do call-boundary side of its comparison; the hybrid VM, shared namespace and name-based dispatch supply it. The note's footer marks that note as its abstraction."
  - scope: passage
    quotes: ["Imperative: Agent A calls Agent B as a function"]
    reason: "SUPPLIED — kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md — cites the graph-DSL versus imperative-scheduler comparison as one instance of the chart-versus-code choice; the scheduler table supplies the comparison."
outcome: report
---

# Role in the KB: Unified calling conventions enable bidirectional refactoring between neural and symbolic

## Role
The note is the KB's mechanism statement for movable neural/symbolic boundaries: theory notes cite it for the claim that a shared, name-dispatched interface makes moving a component between LLM-backed and code implementations a local operation, and source ingests attach external evidence and qualifications (inter-language symbiosis, UPML bridges, the iii harness) to that claim. A second, smaller role is as the KB's description of llm-do's hybrid VM and imperative scheduler, which comparison and scoping notes use as a concrete instance.
Relied on: the shared-interface/local-refactoring claim; name-based dispatch (one name resolving to neural or symbolic); reversibility of the move in both directions; llm-do's hybrid VM and shared namespace; the argument-local scope row and the graph-DSL vs imperative-scheduler table. Unused: the four-step progression and `sanitize_filename()` example as such, spec-mining linkage, the breaking-change/big-bang-rewrite friction argument, the typed-callables section beyond the per-agent system prompt, the Agent→Tool chain diagram, and the open questions.

## Dependents
- `kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md` — the shared-call-surface claim, as landing point for a semantic-mapping qualification.
- `kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md` — the same claim, as landing point for a data/protocol-mapping qualification.
- `kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md` — the mechanism that iii is production evidence for (first passage cut at 1200 characters).
- `kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md` — the value of stable interfaces, and a prediction of co-training brittleness the note does not make.
- `kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md` — an explicit interface as recomposition boundary, for comparison.
- `kb/tags/computational-model-README.md` — citation only.
- `kb/tags/constraining-README.md` — citation framed as reversible commitment.
- `kb/theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md` — prompt-to-skill extraction without call-site change.
- `kb/theory/code-complements-weight-prompt-with-symbolic-operations.md` — local movement between execution paths behind an interface.
- `kb/theory/llm-context-interprets-instructions-and-content-through-one-medium.md` — names resolving to either implementation.
- `kb/theory/llm-context-is-composed-without-scoping.md` — llm-do's frame-local prompts and arguments.
- `kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md` — codified-to-learned refactoring as a local operation.
- `kb/theory/reflective-coverage-is-graded-across-representational-forms.md` — one interface-level mapping as mechanism.
- `kb/theory/research/adaptation-agentic-ai-analysis.md` — stable call boundaries across three surfaces.
- `kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md` — the llm-do call-boundary facts.
- `kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md` — the graph-DSL vs imperative-scheduler comparison.

## Duplication
None visible. The supplied passages are footer lines and short ingest paragraphs that cite the note rather than restate it. `kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md` is marked in the note's footer as the note's abstraction and may restate llm-do material, but its supplied passage does not show this.

## Untaken recommendations
- Brichau et al. ingest: a common call surface needs semantic mappings, not only shared names — absent from the note (a qualification, not an explicit edit instruction).
- Gybels et al. ingest: a shared callable surface needs data mappings and protocol mappings when regimes disagree — absent from the note.
- iii harness ingest: the note "currently grounds the claim only on llm-do"; iii is offered as production evidence — the note still cites only llm-do. Tagged [just-a-reference]; the cut first passage may carry more.

## Reach
- The core claim that a shared interface makes neural/symbolic refactoring local reaches: the brichau, gybels, iii and UPML ingests; `kb/tags/constraining-README.md`; `kb/tags/computational-model-README.md`; `ad-hoc-prompts-extend-the-system-without-schema-changes.md`; `code-complements-weight-prompt-with-symbolic-operations.md`; `operational-signals-that-a-component-is-a-relaxing-candidate.md`; `reflective-coverage-is-graded-across-representational-forms.md`; `research/adaptation-agentic-ai-analysis.md`.
- Name-based dispatch (one name resolving to either side) reaches `llm-context-interprets-instructions-and-content-through-one-medium.md` and the iii ingest.
- Reversibility (code back to prompt) reaches `kb/tags/constraining-README.md` and `operational-signals-that-a-component-is-a-relaxing-candidate.md`.
- The term "neural" as used here (LLM-backed prompt) reaches `research/adaptation-agentic-ai-analysis.md`, which separates neural from natural-language surfaces, and the brichau and gybels ingests, which point to representational form when generalizing.
- llm-do's hybrid VM and shared namespace reach `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md`; the argument-local scope row reaches `llm-context-is-composed-without-scoping.md`; the graph-DSL vs imperative-scheduler table reaches `statecharts-and-programs-differ-in-what-they-show-not-compute.md`.
- The stable-interface framing reaches the anatomy-of-an-agent-harness ingest, which reads a co-training-brittleness prediction into it.
- The four-step progression, spec-mining linkage, breaking-change friction argument, chain diagram and open questions reach no dependent.
