---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: d3da4a3c30de4976a1a303be040ad79f
completed-at: '2026-11-20T09:47:27Z'
findings:
- scope: passage
  quotes:
  - callers don't need to know which they're talking to
  reason: 'DOUBTFUL — (universal, unstated mode) a shared name and signature are enough
    for callers not to depend on whether the callee is neural or symbolic — the interface
    fixes only the shape of a call, not its behavioral contract. An agent and a Python
    function under the same name differ in determinism, latency, cost, output distribution
    and failure mode (an exception versus a fluent wrong answer). A caller that retries,
    caches, budgets or tolerates noise depends on these properties, so swapping implementations
    can change caller behavior while leaving the call site textually unchanged. The
    repair is a boundary condition: call-site stability is syntactic, and callers
    that depend on the behavioral contract must be revalidated. The core mechanism
    survives — LOCAL — instance'
- scope: passage
  quotes:
  - But without a unified interface, each codification step is a breaking change
  reason: DOUBTFUL — (universal) without llm-do-style unification, every codification
    step breaks call sites and so pushes toward big-bang rewrites — wrapping an LLM
    call in an ordinary host-language function is common practice. Such a wrapper
    is a plain function whose body calls a model, and it can later be replaced by
    code without touching callers. It gives the same call-site stability without a
    hybrid VM or shared agent/tool namespace. The causal claim that this friction
    pushes toward big-bang rewrites is asserted without evidence. The premise should
    be restated as a comparison against systems that expose agents and tools through
    different invocation surfaces, not against all systems without llm-do — LOCAL
    — prevalence
- scope: passage
  quotes:
  - components are identified by string name rather than direct object reference
  reason: 'DEFEATED — (universal: ''This requires name-based dispatch'') implementation-agnostic
    interfaces require string-name dispatch rather than object references — a code
    caller that holds a reference typed as `Callable[[str], str]`, or depends on an
    injected protocol object, can switch from an LLM-backed to a pure-code implementation
    at a single binding site without changing any call site. Ordinary polymorphism
    therefore supplies implementation-agnosticism without string names. Name-based
    dispatch is required only when the caller is an LLM that emits a string, which
    is the case the note actually needs. The fix is to limit the requirement to LLM
    callers — LOCAL — instance'
- scope: passage
  quotes:
  - the prompt that invokes it doesn't change
  reason: DOUBTFUL — (universal) the LLM caller's view of an operation stays the same
    when its implementation crosses the boundary — the LLM sees each callable through
    a tool schema and description. For an agent, these come from `.agent` frontmatter;
    for a function, from its signature and docstring. Unless the runtime derives both
    from one declaration, or someone keeps them identical by hand, codification changes
    the description the calling LLM reads. That change is exactly the 'agent's view
    of available operations shifts' friction the note says unification removes. The
    note should state the condition that the exposed schema is preserved across the
    swap — LOCAL — instance
- scope: passage
  quotes:
  - The agent still handles ambiguous cases.
  reason: DOUBTFUL — (unstated, universal) after partial codification, routine and
    ambiguous inputs can be routed between code and agent under one name without the
    caller's involvement — something must decide which cases are ambiguous. A try-code-then-fall-back-to-agent
    design works only when the code fails detectably. In `sanitize_filename`, a date-like
    or non-Latin name that the code transforms wrongly but without error is never
    routed to the agent. The router is a third component, and its neural or symbolic
    status, error rate and location the note leaves unexamined. The repair is to name
    the routing requirement and its detectability condition — LOCAL — instance
- scope: passage
  quotes:
  - Each link can be independently refactored without disturbing the rest.
  reason: DOUBTFUL — (universal) each link in a mixed agent/tool chain can be refactored
    without affecting its neighbours — error handling crosses links. An agent callee
    can absorb failures from its own tool calls by retrying or rephrasing. When it
    is replaced by code that raises, those exceptions reach the upstream agent, which
    must now handle a failure mode it never saw. In the other direction, relaxing
    code to an agent can turn hard errors into plausible wrong outputs that propagate
    downstream silently. Local argument scope, the table's 'each agent gets only its
    arguments', limits data coupling but not failure coupling. This qualification
    preserves the claim — LOCAL — instance
- scope: passage
  quotes:
  - No graph topology to update.
  reason: DOUBTFUL — (universal contrast) graph DSLs make neural-symbolic refactoring
    require topology changes that imperative scheduling avoids — in LangGraph-style
    frameworks, a node is a named function. Replacing an LLM-backed node body with
    pure code leaves edges and node names unchanged. The topology cost appears only
    when orchestration itself is restructured, such as by extracting, inlining or
    splitting nodes; that is a different refactoring from the neural-to-symbolic swap
    this note addresses. The table's claim of 'global context through graph' also
    understates graph frameworks with typed, scoped state. The contrast holds for
    structural refactors but not for implementation swaps — LOCAL — instance
- scope: passage
  quotes:
  - receive the same set of queue labels
  reason: HOLDS — (scoped to a test run) a prompt substituted under the same name
    can return outputs drawn from the code version's label set — the hunt considered
    off-set labels. However, an enum-typed output schema or structured decoding enforces
    the label set, and the note limits this use to exploratory test runs where occasional
    validation failures are acceptable.
- scope: passage
  quotes:
  - Both are callables with defined interfaces.
  reason: HOLDS — (at the level of interface shape) `.agent` files with frontmatter
    and annotated Python functions both expose typed callable interfaces — the hunt
    found no case where one side lacks a declared input/output shape in llm-do as
    described. The semantic gap between shape and behavior is handled under the first
    premise rather than here.
contract: report
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/d3da4a3c30de4976a1a303be040ad79f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/fa0e69bfbdcb40d5d6a3afbf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/d3da4a3c30de4976a1a303be040ad79f/outputs/review.md
raw-output-sha256: e721d0e8df1e90d2dc6b5dac3fb266761695cd53080787688e7f7afe1e239417
---

# Premise decomposition: unified calling conventions enable bidirectional refactoring

**Register:** claim
**Central commitment (one sentence):** When neural (agent) and symbolic (code) components share a calling convention via name-based dispatch, a component can move across the neural-symbolic boundary in either direction without changing call sites, turning codification and relaxing into local refactorings rather than breaking changes.

## Premises and counterexamples

The commitment has three parts. Each part consumes different premises.

1. **Sufficiency of the interface.** A shared name and signature are enough for callers, including LLM callers that read tool schemas, to remain unaffected. This consumes the caller-independence premise, the prompt-invariance premise and the chain-independence premise.
2. **Necessity and contrast.** Without this convention, codification is a breaking change, and name-based dispatch is what supplies the convention. This consumes the breaking-change baseline and the name-dispatch requirement. The scheduler section adds a further contrast with graph DSLs.
3. **The worked progression.** The `sanitize_filename` steps depend on an unstated routing premise: partially codified and residual-neural behavior can coexist under one name. That premise is where the progression is least specified.

The typed-callables connection and the prompt-testing example consume their own premises, and both hold.

The pattern across the non-`HOLDS` premises is consistent. The convention secures **syntactic** call-site stability. The note reads that as **behavioral** locality. The behavioral contract consists of the failure modes, output distribution, exposed tool description and case routing. None of these failures breaks the core mechanism. Each one asks for a boundary condition saying that unified calling keeps call sites unchanged but does not exempt callers from revalidation.

The one defeated premise, that name-based dispatch is required, is defeated in its universal form by ordinary polymorphism. It survives if it is limited to LLM callers. The necessity contrast is weaker than stated because function wrappers around model calls are common, ordinary practice.

## For the human

Look first at the gap between syntactic call-site stability and behavioral locality: the first premise, caller independence. It is the load-bearing doubtful premise behind "refactoring across the boundary becomes a local operation", and adding its boundary condition also addresses the chain-independence, prompt-invariance and routing premises.
