---
description: A unified interface lets programmers swap prompts and code without editing callers, but leaks asymmetrically — prompt-to-code exposes loose LLM callers, while code-to-prompt exposes cost, latency, and error assumptions
type: types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, computational-model, constraining]
---

# A unified interface lets programmers choose prompts or code without changing callers

A caller uses the same name, arguments, and result format whether a prompt-backed agent or a function handles the call. An LLM caller also sees the same description of the operation. This is **information hiding**: the interface tells callers how to use the operation without making them depend on how the programmer implements it. The programmer can replace a prompt with code once a rule is clear, or swap code back to a prompt to test a changed requirement or relax an overly rigid rule. Unlike ordinary code-to-code information hiding, however, this boundary crosses two different execution regimes and serves both code and LLM callers, so the abstraction leaks asymmetrically in the two swap directions.

The [English account of prompting](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) treats an instruction as permitting a set of readings, from which an LLM executor produces one, and treats extracting a repeated operation into code as a separate intervention whose trade-off must be assessed. As a system evolves, components move in both directions across that boundary: recurring patterns move from prompts into code, and code moves back to prompts when requirements change or a coded rule proves too brittle. A unified interface is what makes that boundary movable without rewriting callers.

## The mechanism

[llm-do](https://github.com/zby/llm-do) is a runtime in which prompt-backed agents and Python functions share one callable namespace and invoke each other by name. Each callable receives only its declared arguments rather than the caller's full conversation history; an agent combines its own system prompt with that declared signature. The programmer binds a name such as `ticket_classifier` to either a prompt-backed agent or a Python function, and the runtime resolves the binding on each call. The programmer chooses the implementation for the run; the runtime does not decide ticket by ticket whether to use code or a model.

```
Caller (agent or code) ──▶ ticket_classifier ──▶ binding ──┬──▶ prompt-backed agent
                                                           └──▶ Python function
```

## What the interface hides and what leaks

Ordinary information hiding swaps two implementations that share the same execution substrate and caller model: changing a sorting algorithm or storage backend preserves the basic nature of a function call. Across the prompt–code boundary, a shared interface hides *how the rule is implemented*—avoiding call-site edits—but cannot hide *which execution regime handles the call*. Because both code and LLMs can act as callers, the two swap directions break different caller assumptions:

- **Prompt to code exposes loose LLM callers.** An LLM caller invokes an operation through its natural-language description as well as its schema. A prompt-backed callee often absorbs loosely phrased, slightly malformed, or context-dependent arguments by inferring intent. When the programmer replaces that prompt with strict code, the call signature stays identical, yet LLM callers that relied on that tolerance begin failing or triggering literal misreads. Enforcing input schemas strictly at the call boundary while the implementation is still a prompt prevents callers from accumulating this hidden coupling.
- **Code to prompt exposes runtime assumptions in code callers.** A signature does not express latency, token cost, determinism, or failure mode. A Python caller that invokes a fast function inside a loop can multiply latency and token spend when that name is rebound to a prompt. Code written to catch deterministic exceptions can also break when a prompt-backed callee returns a model refusal, drifts across retries, or produces a schema-valid but wrong result.

The practical consequence is that interface parity alone is not enough for safe swapping. Call boundaries must enforce schemas before codification, and call sites that may move back to prompts must be written for fallible, higher-latency calls.

## Scope

- **Call invariance is not behavioral invariance:** What stays unchanged is the call, not its effect. A classifier that returns the same queue labels can still route a ticket to a different queue, so callers that relied on prior decisions or error behavior need testing after a swap.
- **Structural signature changes still require adapters:** If a new implementation requires structured arguments instead of free text, the call itself must change unless an adapter preserves the old interface.
- **Bidirectional swapping requires call-site headroom:** Moving code back to a prompt behind an unchanged call site works only where the caller's latency budget, cost budget, and error handling can absorb model execution; tight inner loops and hard deterministic paths do not qualify.

## Why this matters for constraining

[Constraining](./definitions/constraining.md) and [codification](./definitions/codification.md) describe the learning mechanisms — narrowing the interpretation space, changing medium. But in a system that exposes agents and tools through different invocation surfaces, a codification step that moves a component from one surface to the other is a breaking change: call sites must be updated, prompt structure must change, and the agent's view of available operations shifts. This friction would likely discourage incremental refactoring and push toward big-bang rewrites. That effect is an expectation, not an observed result.

Suppose the team starts with a prompt for `ticket_classifier` while it learns how tickets should be assigned. The same unified binding then supports three distinct moves without editing callers:

- **Prompt to code (codification as refactoring).** By checking the agent's decisions against the queues that actually resolve the tickets, the team identifies a topic-based rule it wants to keep—[spec mining](./spec-mining-as-codification.md). If the team wants to preserve that routing behavior, replacing the prompt with a Python function is a refactoring: the programmer changes the implementation, not the rule, and rebinds `ticket_classifier` to the function.
- **Code to prompt for a changed requirement (prototyping).** Later the team wants to test routing tickets by the action the customer needs rather than by topic. The Python function still meets the old requirement. For a test run, the programmer binds `ticket_classifier` to a prompt instead, edits the prompt, and compares assignments on sample tickets without implementing each candidate policy in Python. Even if the winning rule goes back into code for production, the prompt let the team explore alternatives cheaply.
- **Code to prompt for [relaxing](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) (regaining generality).** Separately, the team's goal may not have changed, yet the extracted Python rule proves to be a brittle proxy theory that fails on edge cases or distribution shift—or a stronger, cheaper model now handles the broader task well enough ([relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md)). Here rebinding `ticket_classifier` to a prompt reverses the earlier code extraction to recover generality, accepting higher runtime cost and variance.

Only the first move is a behavior-preserving refactoring. Both code-to-prompt moves intentionally change behavior—one because the requirement changed, the other because the coded approximation proved too narrow—yet all three stay local to the binding because callers depend only on the interface.

## The connection to typed callables

[Instructions are typed callables](./instructions-are-typed-callables.md) argues that skills, tasks and workflows are callable in a limited sense: they take and return typed documents and can declare signatures, though a signature does not turn a natural-language procedure into a conventional function. This note extends that callable structure to tools. llm-do implements this pattern: `.agent` files are YAML frontmatter (type signature) plus system prompt (implementation), and tools are Python functions with type annotations. The unified interface is what makes this callable view practical across prompts and code rather than merely analogical.

## Open Questions

- How does a unified callable surface scale for LLM callers once hundreds of components exist, where tool-description selection degrades even when names are namespaced?
- How should tracing and error attribution work when a call chain alternates between prompts and code — do standard observability tools suffice, or does the boundary require dedicated trace semantics?
- Should a unified interface expose non-functional annotations (cost, latency, determinism) to callers, or does that re-expose the implementation detail the interface is meant to hide?

---

Relevant Notes:

- Abstracted into: [RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence](./rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md)
- [Prompting changes failure diagnosis with the semantic reference](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) — grounds: the English account, under which an instruction permits several readings, that this note makes architecturally concrete
- [The practical scheduler is the host language, not a reified select](./the-practical-scheduler-is-the-host-language.md) — contrasts: host-language orchestration governs control flow and state scoping independently of whether callables hide prompts or code behind one interface
- [Constraining](./definitions/constraining.md) — defined-in: the mechanism whose movement across prompts and code a unified interface lowers call-site friction for
- [Codification](./definitions/codification.md) — defined-in: the transition from natural language to symbolic form that a unified interface keeps local to the binding
- [Spec mining is codification's operational mechanism](./spec-mining-as-codification.md) — mechanism: observe agent behavior and extract rules to code while call sites stay stable
- [Instructions are typed callables with document type signatures](./instructions-are-typed-callables.md) — extends: extends typed-callable signatures across both prompt-backed agents and code functions
- [Programming practices for prompts need evidence matched to the question](./programming-practices-for-prompts-need-question-specific-evidence.md) — extends: extract-function and inline refactoring transfer more directly when prompts and code share an interface
- [Codification and relaxing navigate the bitter lesson boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — grounds: defines relaxing as reversing code extraction to regain generality, distinct from swapping to a prompt to test a changed requirement
- [Operational signals that a component is a relaxing candidate](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — enables: relaxing signals identify brittle coded rules; a unified interface makes swapping them back to prompts local to the binding
