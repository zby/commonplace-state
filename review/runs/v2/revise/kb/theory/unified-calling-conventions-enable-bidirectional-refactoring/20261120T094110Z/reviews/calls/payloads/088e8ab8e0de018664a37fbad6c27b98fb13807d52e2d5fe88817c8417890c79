---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "if neural and symbolic components present the same interface, callers don't need to know which they're talking to"
    reason: "DOUBTFUL — (universal, unstated mode) a shared call interface hides everything a caller depends on, so a caller need not know whether the callee is neural or symbolic — Callers depend on more than the signature. An LLM-backed callee is non-deterministic, slower and costlier, and degrades softly on odd inputs. A Python callee is deterministic and raises exceptions on inputs it does not handle. A caller built around one profile can break on the other: retry loops written for agent variance, timeouts set for code latency, or a caller that relied on the agent tolerating malformed input. The same signature does not give the same behavioural contract (the Liskov substitution problem). The repair is to state that the convention removes interface friction while the behavioural contract still has to be matched, with no loss to the core mechanism — LOCAL — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — (unstated, read as the note's practical claim) changing call sites is the main cost of moving a component across the neural-symbolic boundary, so removing that cost makes the move 'a local operation' — The note answers how to make the boundary movable 'in practice' with call-site stability alone. In common practice, the larger cost of codification or relaxing is checking that the new implementation matches the old one across the input distribution: evals, regression sets, monitoring for drift. A unified convention does not reduce that cost. A stable call site can even hide a behaviour change, because nothing at the caller signals that the implementation moved. The edit is local, but its verification is not. The fix is to separate locality of edit from locality of verification. The convention still keeps its role in removing interface churn — LOCAL — prevalence"
  - scope: passage
    quotes:
      - "the prompt that invokes it doesn't change"
    reason: "DOUBTFUL — (universal) when `ticket_classifier` is moved from agent to Python function, the LLM caller's view stays the same — The LLM sees a tool schema. For an agent, the schema comes from frontmatter; for a function, from type annotations and docstring. Codification usually narrows inputs: the agent took free text, while the function needs structured arguments or enumerated values. That changes the schema the calling LLM sees, so call behaviour can shift even though the invoking prompt text is unchanged. The note's own step 3 keeps the agent for ambiguous cases, so the callee behind the name becomes a composite with a router. It is no longer a simple swap. This holds when the extracted function preserves the agent's schema exactly, a boundary condition that can be stated — LOCAL — instance"
  - scope: passage
    quotes:
      - "Each link can be independently refactored without disturbing the rest."
    reason: "DOUBTFUL — (universal) links in an Agent→Tool→Agent chain can be swapped independently — Downstream components come to depend on incidental features of an upstream component's output: phrasing, extra explanation, ordering, how missing fields are filled. This is Hyrum's law, which is widely observed in ordinary APIs. Downstream agents are especially sensitive to it, because they consume whatever text arrives. Replacing an agent with code changes the output distribution even when the declared type is unchanged, and that can disturb the next link. Adding a condition that outputs are normalised or schema-validated at each link keeps the claim — LOCAL — prevalence"
  - scope: passage
    quotes:
      - "components are identified by string name rather than direct object reference"
    reason: "DEFEATED — (universal: 'This requires name-based dispatch') implementation-agnostic swapping across the boundary requires string-name dispatch — Counterexample: a Python caller holds a `Callable[[Ticket], Label]` injected by dependency injection or a Protocol. The injected object can be an LLM-backed wrapper or a rule-based function, and the call site does not change, with no string lookup involved. Ordinary polymorphism already gives an implementation-agnostic interface. Names are required only when the caller is an LLM, because an LLM can emit only text. The premise holds under the condition the chain diagram implies (neural callers) but fails as stated. Restricting it to LLM callers keeps the mechanism — LOCAL — instance"
  - scope: passage
    quotes:
      - "without a unified interface, each codification step is a breaking change"
    reason: "DOUBTFUL — (universal: 'each') without a unified interface, codification breaks call sites, and that friction pushes toward big-bang rewrites — Many codebases wrap each LLM call in an ordinary typed function from the start, for example `classify(ticket) -> Label`. Replacing its body with rules is not a breaking change, and no hybrid VM or shared namespace is involved. Such a setup is a de facto unified convention. The premise is therefore close to tautological unless 'unified interface' names something narrower, such as LLM-visible tool parity, and the note does not specify which. The causal claim that the friction 'pushes toward big-bang rewrites' gets no evidence. Narrowing 'unified interface' to the LLM-caller case and reading the rewrite effect as a tendency would fix this — LOCAL — instance"
  - scope: passage
    quotes:
      - "receive the same set of queue labels"
    reason: "DOUBTFUL — (universal) a prompt substituted for code under the same name returns values within the code's output type — An LLM can return a label outside the enumerated set, a near-synonym, or free text around the label, unless the runtime constrains decoding or validates the output against the declared type. Agent frontmatter declares a type but does not enforce it. In the note's test-run framing this is a bounded risk, but relaxing in the reverse direction relies on it. The repair is to make output validation a stated condition of the relax direction — LOCAL — instance"
  - scope: passage
    quotes:
      - "The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring"
    reason: "DOUBTFUL — (comparative) the imperative scheduler, rather than a graph DSL, is what makes cross-boundary refactoring ordinary refactoring with 'no graph topology to update' — In LangGraph-style graphs, nodes are also functions. Swapping a node's body from an LLM call to code changes no edges. Redrawing edges is needed only for structural refactors such as extract or inline, and those are not the neural-symbolic swap this note is about. So graph DSLs also support the swap, and the contrast in the table does not bear on the central commitment. Scoping the scheduler claim to structural refactors keeps it — LOCAL — instance"
  - scope: passage
    quotes:
      - "Both are callables with defined interfaces."
    reason: "DOUBTFUL — (universal) an `.agent` file's frontmatter defines its interface in the same sense as a typed Python function — A Python annotation can be checked statically and at runtime. An agent's declared output type is a request to the model, and the model meets it only probabilistically unless the runtime adds validation. The two interfaces are 'defined' in different strengths, which limits how far the note's claim that the convention makes the typed-callables view 'practical rather than just analogical' reaches. Qualifying the claim with runtime validation keeps it — LOCAL — instance"
  - scope: passage
    quotes:
      - "The agent still handles ambiguous cases. The call site doesn't change."
    reason: "HOLDS — a codified function and a residual agent can sit behind one name, with the function handling the mined pattern and deferring ambiguous inputs to the agent — The hunt looked for a case where the split forces a call-site change. In the note's model tools can call agents, so the function can delegate its fallback internally, and callers still see one name. The extra router is a cost borne by the callee (see the schema finding), not a defeater of this step"
outcome: report
---

# Premise decomposition: Unified calling conventions enable bidirectional refactoring between neural and symbolic

**Register:** claim
**Central commitment (one sentence):** When neural (LLM-backed) and symbolic (code) components share one calling convention through name-based dispatch, a component can be moved across the boundary in either direction without changing call sites. That makes codification and relaxing local, incremental operations rather than breaking rewrites.

## Premises and counterexamples

The commitment rests on three groups of premises.

**Substitutability.** A shared interface is all a caller depends on. The LLM caller's view survives the swap. Chained links are independent. The relax direction preserves the output type. This group carries the most weight, and it is where the doubts gather. Interface identity does not give behavioural identity: latency, determinism, error modes, schema narrowing and incidental output features all leak through a stable name.

**Mechanism.** Name-based dispatch is required, and the counterfactual holds that without a unified interface every codification step breaks call sites. The first is defeated as a universal: ordinary polymorphism gives implementation-agnostic swapping for code callers. String names are needed only because an LLM caller emits text. The counterfactual is close to tautological, because wrapping an LLM call in a typed function is already a unified convention.

**Supporting contrasts.** These are the imperative scheduler versus graph DSLs, and the agent file versus the typed function as equally "defined" interfaces. Both are peripheral to the commitment. Each over-claims slightly: graph DSLs also allow node-body swaps, and agent output types are not enforced.

The note never states the most consequential premise: that call-site churn is the main obstacle to moving the boundary. If verifying behavioural equivalence is the larger cost, as it usually is in practice, the convention is necessary but far from sufficient, and "local operation" describes the edit rather than the change. No failure is global. Each is repaired by scoping (LLM callers), adding conditions (schema preservation, output validation) or separating edit locality from verification locality. All of these keep the core mechanism.

## For the human

Look first at the unstated premise that call-site stability is the main cost of crossing the boundary. Then separate "the edit is local" from "the behaviour change is verified", and state that a shared interface does not give a shared behavioural contract.
