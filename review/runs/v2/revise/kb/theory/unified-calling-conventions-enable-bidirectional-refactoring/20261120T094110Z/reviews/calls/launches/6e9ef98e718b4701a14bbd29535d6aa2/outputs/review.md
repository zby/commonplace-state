---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["The agent still handles ambiguous cases. The call site doesn't change."]
    reason: "UNSUPPORTED — Splitting one component into a Python function plus an agent fallback needs something that decides which inputs are ambiguous and routes them. The note does not say where that routing lives. If it is a wrapper registered under the old name, the call site is preserved by an added dispatcher, not by the shared convention alone. If the caller must pick between two names, the call site does change. The same gap recurs in step 4 ('Add an LLM call for the new cases. Again, the call site doesn't change')."
  - scope: passage
    quotes: ["Each link can be independently refactored without disturbing the rest."]
    reason: "THIN — A uniform convention keeps the name and signature stable, but downstream links depend on the callee's behaviour, not only its interface. A neural callee and its symbolic replacement differ in output variability, failure modes, and handling of out-of-pattern inputs. A caller that relied on the agent's tolerance of ambiguity can be disturbed even though nothing at the call site changed. The note establishes syntactic stability and asserts behavioural independence."
  - scope: passage
    quotes: ["But without a unified interface, each codification step is a breaking change"]
    reason: "THIN — The counterfactual is asserted, not shown. Ordinary adapters, wrappers, or tool descriptions can keep call sites stable without a single neural-symbolic namespace, so it does not follow that every codification step without unified calling is breaking. The following claim, that this friction 'pushes toward big-bang rewrites', is a behavioural claim about teams with no cited case or mechanism beyond the friction itself."
  - scope: passage
    quotes: ["The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring"]
    reason: "THIN — An imperative scheduler makes orchestration code refactorable with ordinary moves, but the neural-to-symbolic move itself is not a mechanical extract-function: turning a prompt's behaviour into code requires observing and committing to one interpretation (the note's own spec-mining step). The table contrast with graph DSLs also does not show that swapping a node's implementation in a graph requires a topology change; only reorganising control flow does."
  - scope: passage
    quotes: ["The unified calling convention is what makes the type-theoretic view practical rather than just analogical."]
    reason: "THIN — A shared convention supplies names and declared signatures (frontmatter, annotations). Making the type-theoretic view practical would also require that outputs actually conform to the declared types, which for LLM-backed agents depends on validation or constrained output the note does not mention. The step from 'both have declared interfaces' to 'the typing is practical, not analogical' is unearned."
outcome: report
---

# Friction check: Unified calling conventions enable neural-symbolic refactoring

**Central claim (one sentence):** When LLM-backed agents and code tools are invoked through one name-dispatched calling convention, a component can be moved from neural to symbolic or back without changing its call sites, so refactoring across the boundary becomes a local operation.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent thing: interface stability across an implementation change. The properties it wants together are a shared name and signature, freedom to swap the implementation medium, and unchanged call sites. These can coexist at the interface level, and llm-do's name-based dispatch is a concrete witness. The pressure point is that "local" is established for the syntactic contract only. The behavioural contract (output distribution, ambiguity handling, failure modes) changes when the medium changes. That tension does not dissolve the claim, but it bounds what "without disturbing the rest" can honestly mean.

## Thinnest joints

The codify step ranks first because it is the note's worked example of the mechanism, and it silently introduces a split (code for the regular cases, agent for the ambiguous ones) whose routing is exactly the call-site question the note claims has disappeared. The "each link independently" joint ranks next because it generalises from interface stability to behavioural independence, the central slide in the note. The breaking-change counterfactual and big-bang claim come third: they motivate the mechanism by contrast with an alternative the note never shows to be as rigid as described. The imperative-scheduler and typed-callables joints are weaker supporting inferences. Each conflates a structural property (refactorable orchestration code, declared signatures) with the harder property it is offered for (mechanical neural-to-symbolic extraction, enforced types). The ticket-classifier switch-back paragraph was considered and not surfaced: it is conditional ("If that is the quicker way...") and claims only that a prompt can stand in during a test run, which its premises support.

## For the human

Look first at step 3 of the progression: say where the code-versus-agent routing lives once `sanitize_filename()` is extracted, because that answer decides whether the call site really stays unchanged.
