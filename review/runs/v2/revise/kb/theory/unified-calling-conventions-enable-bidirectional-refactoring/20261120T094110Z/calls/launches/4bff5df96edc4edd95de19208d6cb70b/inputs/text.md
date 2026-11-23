---
description: When agents and tools share a calling convention, components can move between neural and symbolic without changing call sites — llm-do demonstrates this with name-based dispatch over a hybrid VM
type: types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# Unified calling conventions enable bidirectional refactoring between neural and symbolic

The [English account of prompting](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) treats an instruction as permitting a set of readings, from which an LLM executor produces one; it treats extracting a repeated operation into code as a separate intervention whose trade-off must be assessed. This note extends that into a premise of its own: components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — constrain patterns to code, relax rigid code back to LLM. But that premise doesn't say how to make the boundary movable in practice. The answer is a unified calling convention: if neural and symbolic components present the same interface — the same name, the same argument and output schema, and the same description the LLM caller sees — callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation.

## The mechanism

[llm-do](https://github.com/zby/llm-do) implements this through a hybrid VM where agents (`.agent` files, LLM-backed) and tools (Python functions) share a single namespace. The LLM sees both as callable functions. A call to `ticket_classifier` might dispatch to an agent today and a Python function tomorrow — the prompt that invokes it doesn't change.

llm-do achieves this shared interface through **name-based dispatch**: components are identified by string name rather than direct object reference. Names enable dynamic resolution (the LLM outputs a string, the runtime looks it up), late binding (the callee needn't exist when the caller is defined), and implementation-agnostic interfaces (the same name can resolve to either neural or symbolic).

```
Agent ──calls──▶ Tool ──calls──▶ Agent ──calls──▶ Tool ...
neural          symbolic         neural          symbolic
```

The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest.

## Why this matters for constraining

[Constraining](./definitions/constraining.md) and [codification](./definitions/codification.md) describe the learning mechanisms — narrowing the interpretation space, changing medium. But in a system that exposes agents and tools through different invocation surfaces, a codification step that moves a component from one surface to the other is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts. This friction can be expected to discourage incremental refactoring and push toward big-bang rewrites; that effect is an expectation, not an observed result.

With unified calling, the call site stays fixed at each step of a progression such as this illustrative one:

1. **Start neural** — define an agent to handle a task. Quick to add, handles ambiguity.
2. **Observe patterns** — the agent consistently lowercases and replaces spaces with underscores. This is [spec-mining](./spec-mining-as-codification.md) — discovering that an underspecified spec consistently resolves to one interpretation, then committing to it in code.
3. **Codify** — extract `sanitize_filename()` to Python. The agent still handles ambiguous cases. The call site doesn't change.
4. **Extend via relaxing** — new requirements emerge (handle Unicode, detect dates). Add an LLM call for the new cases. Again, the call site doesn't change.

A team can also switch back to a prompt to test a proposed change while the code still meets its current requirement. Suppose `ticket_classifier` routes each ticket by topic, but the team wants to try routing by the action the customer needs. In a test run, the same caller can send sample tickets to a prompt under the same name and receive the same set of queue labels. The team can try several routing rules by editing the prompt rather than implementing each candidate in Python. If that is the quicker way to discover which rule works, the prompt has served its purpose even if the team puts the chosen rule back into code.

## The scheduler layer

On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL. This is a deliberate contrast with graph-defined orchestration, such as LangGraph's, where orchestration is defined as node-edge graphs.

| Aspect | Graph DSLs | llm-do Scheduler |
|--------|------------|----------------|
| Orchestration | Declarative: Node A → Node B | Imperative: Agent A calls Agent B as a function |
| State | Global context through graph | Local scope — each agent gets only its arguments |
| Refactoring | Redraw edges, update graph | Change code — extract functions, inline agents |
| Control flow | DSL constructs | Native Python: `if`, `for`, `try/except` |

The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring — extract function, inline, rename. No graph topology to update.

## The connection to typed callables

[Instructions are typed callables](./instructions-are-typed-callables.md) argues that skills, tasks and workflows are callable in a limited sense: they take and return typed documents and can declare signatures, though a signature does not turn a natural-language procedure into a conventional function. This note extends that callable structure to tools. llm-do operationalises it: `.agent` files are YAML frontmatter (type signature) plus system prompt (implementation), and tools are Python functions with type annotations. Both are callables with defined interfaces. The unified calling convention is what makes this callable view practical across the neural-symbolic boundary rather than just analogical.

## Open Questions

- Does unified calling break down at scale, when the namespace grows to hundreds of components and name collisions become likely?
- How does debugging work when a call chain crosses the neural-symbolic boundary multiple times — do existing observability tools handle this, or does the hybrid VM need its own tracing?
- Is the imperative scheduler pattern specific to Python, or does it transfer to other host languages?

---

Relevant Notes:

- Abstracted into: [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md)
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the English account, under which an instruction permits several readings, that this note makes architecturally concrete
- [constraining](./definitions/constraining.md) — the mechanism that unified calling makes frictionless
- [codification](./definitions/codification.md) — the phase transition from neural to symbolic that unified calling makes a local operation
- [spec-mining-as-codification](./spec-mining-as-codification.md) — the operational mechanism: observe agent behavior, extract to code — enabled by stable call sites
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — the type-theoretic view that llm-do operationalises
- [Programming practices for prompts need evidence matched to the question](./programming-practices-for-prompts-need-question-specific-evidence.md) — extends: extract-function and inline refactoring transfer directly when calling conventions are unified
- [operational-signals-that-a-component-is-a-relaxing-candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — extends: relaxing signals answer "when should you relax?" — unified calling makes the relaxing refactoring cheap once the signal fires
