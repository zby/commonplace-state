---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["extract `sanitize_filename()` to Python. The agent still handles ambiguous cases. The call site doesn't change."]
    reason: "UNSUPPORTED — The step needs one name to resolve to two implementations at once: Python for the mined cases and the agent for the ambiguous ones. The mechanism section describes name-based dispatch that resolves a name to one implementation, either neural or symbolic. The note does not say what decides which inputs are ambiguous or where that routing lives. If a wrapper does the routing, the wrapper is the new call target, and the claim that the call site is unchanged depends on that wrapper, not on the shared convention. Step 4 ('Add an LLM call for the new cases. Again, the call site doesn't change.') inherits the same gap."
  - scope: passage
    quotes: ["The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest."]
    reason: "UNSUPPORTED — A uniform calling convention keeps the call syntax and the name stable. It does not keep behaviour stable. Swapping an agent for a function changes determinism, output distribution, error modes and latency. Downstream links, especially LLM callers that adapted to the old outputs, can be disturbed even when no call site is edited. The inference goes from interface sameness to independent refactorability without a behavioural-contract condition, such as output validation or a typed result, that would make 'without disturbing the rest' true."
  - scope: passage
    quotes: ["But without a unified interface, each codification step is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts."]
    reason: "THIN — The contrast case is asserted, not shown. 'Each' is too broad: codification inside an existing tool body, or behind an adapter, needs no call-site change even without a system-wide unified convention. The next sentence, that this friction 'pushes toward big-bang rewrites', is a further causal claim with no example or evidence. The joint sets up the benefit by overstating the cost of the alternative."
  - scope: passage
    quotes: ["The imperative style means refactoring between neural and symbolic uses the same patterns as normal code refactoring — extract function, inline, rename."]
    reason: "THIN — The table contrasts orchestration styles but does not show that the code-refactoring patterns carry across the neural-symbolic boundary. 'Inline' an agent has no evident code analogue: an agent body is a prompt, so inlining it into Python requires codification, not the mechanical inline refactoring. The joint establishes that the scheduler's control flow is ordinary Python. It does not establish that crossing the boundary is ordinary refactoring."
  - scope: passage
    quotes: ["The unified calling convention is what makes the type-theoretic view practical rather than just analogical."]
    reason: "THIN — The preceding sentences show that both kinds of component declare signatures: YAML frontmatter and Python annotations. A declared signature on an LLM-backed callable does not ensure its outputs inhabit the declared type unless something validates them. The note does not say whether llm-do enforces output types. So the step from 'both have defined interfaces' to 'the type-theoretic view is practical' is missing the enforcement condition that would make the type more than an annotation."
outcome: report
---

# Friction check: Unified calling conventions enable bidirectional refactoring between neural and symbolic

**Central claim (one sentence):** If neural (agent) and symbolic (code) components share one calling convention through name-based dispatch, a component can move across the neural-symbolic boundary in either direction without changing its call sites, so codification and relaxing become local refactorings.

## Filter
**Filter:** SURVIVES

The claim commits to a coherent thing: stable names and signatures across implementations of either kind. The properties it wants together are a shared interface, call-site stability and bidirectional movement. These can coexist at the level of call syntax. Concretization exposes a pressure that the note leaves unpriced, but the pressure does not dissolve the claim. The claim stays consistent if "local operation" means "no call-site edits". It becomes doubtful only if read as "no downstream effect", which the note's phrase "without disturbing the rest" invites. That pressure is routed to the joints below rather than counted as a contradiction.

## Thinnest joints

The worked progression is ranked first because it is the note's main demonstration, and its third step quietly needs a capability that the mechanism section does not provide: one name serving a hybrid of code and agent with input-dependent routing. Second is the chain claim, because it carries the jump from interface uniformity to behavioural independence, which the central claim relies on most. Third is the contrast case, which sets up the benefit by overstating the cost of the alternative. The scheduler and typed-callables joints rank lower. They are secondary sections whose gaps, the meaning of "inline" across the boundary and output-type enforcement, would weaken connections to other notes rather than the central claim.

Joints that were checked and not surfaced include "This requires name-based dispatch". That joint holds for LLM callers, which emit strings, but is overstated as a general requirement because interface polymorphism over object references would also work. The prompt-testing paragraph is not surfaced because its conclusion is explicitly conditional ("If that is the quicker way…").

## For the human

Look first at step 3 of the progression: say what routes ambiguous inputs to the agent and mined inputs to `sanitize_filename()` under one name, and whether that router, not the convention, is what keeps the call site unchanged.
