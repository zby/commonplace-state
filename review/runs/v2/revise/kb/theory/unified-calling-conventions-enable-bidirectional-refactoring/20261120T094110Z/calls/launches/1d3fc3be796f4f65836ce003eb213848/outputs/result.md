---
type: types/edit-result.md
outcome: changed
changes:
  - "Opening paragraph: defined 'the same interface' as the same name, argument and output schema, and LLM-visible description, keeping the unchanged-call-site / local-operation claim intact."
  - "Why this matters for constraining: replaced 'without a unified interface, each codification step is a breaking change' with a comparison against systems that expose agents and tools through different invocation surfaces, and marked the big-bang-rewrite effect as an expectation, not an observed result."
  - "Why this matters for constraining: replaced the lead-in 'the progression is smooth' with a statement that the call site stays fixed at each step of an illustrative progression."
  - "The scheduler layer: narrowed 'declarative agent frameworks (LangGraph, CrewAI)' to 'graph-defined orchestration, such as LangGraph's', keeping the contrast."
removed-links: []
---

# Report

Four sentence-level edits, all inside the four passages the scope names. No links, quoted spans, numbered steps, test-run paragraph or table were touched.

1. Opening paragraph.
   - Before: "if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation."
   - After: "if neural and symbolic components present the same interface — the same name, the same argument and output schema, and the same description the LLM caller sees — callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation."
   - Evidence that bounds it: the mechanism section's name-based dispatch and the typed-callables section (frontmatter type signature vs. annotated Python functions). The definition names what must actually match for a caller not to notice the swap. Must-keep item 2 and the kb-role's relied-on claim (unchanged call sites, local operation) remain at full strength.

2. Breaking-change sentences.
   - Before: "But without a unified interface, each codification step is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts. This friction discourages incremental refactoring and pushes toward big-bang rewrites."
   - After: "But in a system that exposes agents and tools through different invocation surfaces, a codification step that moves a component from one surface to the other is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts. This friction can be expected to discourage incremental refactoring and push toward big-bang rewrites; that effect is an expectation, not an observed result."
   - Evidence that bounds it: the breaking change follows from the interface difference by construction, so it stays asserted, but only for a move across surfaces. The note cites no observation of teams choosing big-bang rewrites, so the behavioural effect is now marked as an expectation. The kb-role lists the big-bang-rewrite claim as unused; it was narrowed, not cut.

3. Progression lead-in.
   - Before: "With unified calling, the progression is smooth:"
   - After: "With unified calling, the call site stays fixed at each step of a progression such as this illustrative one:"
   - Evidence that bounds it: the steps are a constructed `sanitize_filename()` example, not a reported case. Each step itself states that the call site doesn't change, so the lead-in now claims that and nothing vaguer ("smooth").

4. Scheduler contrast.
   - Before: "This is a deliberate contrast with declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs."
   - After: "This is a deliberate contrast with graph-defined orchestration, such as LangGraph's, where orchestration is defined as node-edge graphs."
   - Evidence that bounds it: the note supplies no evidence that CrewAI defines orchestration as node-edge graphs, so it is dropped as an example. The contrast with graph-defined orchestration (must-keep item 3, kb-role relied-on) is kept, as is the table's "Graph DSLs" column.

Noticed but not applied (outside scope): the "Relevant Notes" annotation "the mechanism that unified calling makes frictionless" is also strong; "Each link can be independently refactored without disturbing the rest" in the mechanism section could be bounded by the same interface definition. The title was not changed and no title change is proposed.
