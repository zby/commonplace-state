---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/critique-note.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: fa8c22ccd4624c2ca9328bd1bfb55720
completed-at: '2026-11-20T09:45:17Z'
findings:
- scope: passage
  quotes:
  - refactoring across the boundary becomes a local operation
  reason: 'A shared name and signature keeps the call site unchanged, but it does
    not keep the caller''s behaviour unchanged. Neural and symbolic implementations
    differ in determinism, failure modes (refusals, malformed or partial output, timeouts),
    latency and cost, and callers come to depend on those properties. State the condition
    that makes the swap local: the callee''s behavioural contract, not only its name
    and type, must be preserved, or the caller must already tolerate both behaviours.
    Name what has to be verified at the caller when the implementation crosses the
    boundary.'
- scope: passage
  quotes:
  - Each link can be independently refactored without disturbing the rest.
  reason: This is the strongest form of the overreach. An upstream agent that learned
    to compensate for a downstream agent's variability, or a downstream tool that
    was tolerant of an upstream agent's loose output, is disturbed when its neighbour
    becomes strict or loose. Qualify the sentence to syntactic independence, or add
    the contract condition that gives behavioural independence.
- scope: passage
  quotes:
  - But without a unified interface, each codification step is a breaking change
  reason: Overstated contrast. Without a native unified namespace, a thin wrapper
    or adapter (an agent exposed as a tool, or a function exposed to a prompt) also
    keeps call sites stable; many agent frameworks ship such an adapter. The note
    should say what a native unified convention buys over an adapter, such as no per-component
    wrapping or no divergence between the two descriptions, or else weaken 'each ...
    is a breaking change'.
- scope: passage
  quotes:
  - The agent still handles ambiguous cases. The call site doesn't change.
  reason: The codify step splits one component into a code path and an agent fallback,
    which needs a router that decides which inputs count as ambiguous. The note does
    not say where that router lives or who maintains it. That routing is the new,
    consequential decision in the step, and its misclassifications are a new failure
    mode the unchanged call site hides.
- scope: passage
  quotes:
  - '| State | Global context through graph | Local scope — each agent gets only its
    arguments |'
  reason: 'The comparison with graph DSLs is unsourced and may be dated: LangGraph
    offers subgraphs with their own state and a functional, decorator-based API, and
    CrewAI offers Python-code Flows. Either cite the versions compared or narrow the
    contrast to the property that matters for this note (whether a component swap
    requires editing orchestration).'
contract: report
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/fa8c22ccd4624c2ca9328bd1bfb55720/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/05a67833f2e75579e15520b7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/fa8c22ccd4624c2ca9328bd1bfb55720/outputs/review.md
raw-output-sha256: 1ca509c16e11fb603f8b43b43939b51851a564977a66e679af647721fc0530bc
attack-outcome: partially lands
---

# Critique: Unified calling conventions enable bidirectional refactoring between neural and symbolic

**Note:** kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
**Central commitment:** If neural (LLM-backed) and symbolic (code) components present the same calling interface, behind name-based dispatch, then moving a component across the neural-symbolic boundary does not change call sites and so becomes a local refactoring operation.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is the distributed-systems tradition that rejected *location transparency* in RPC. Waldo et al.'s "A Note on Distributed Computing" (1994) is the standard statement. Its argument is that a uniform call interface over implementations with fundamentally different semantics is a hazard rather than an enabler. In RPC the differences were latency, partial failure and memory model. The interface hides them, so callers are written against the local semantics and break when the implementation is remote. Hyrum's law adds that with enough use, every observable behaviour of a callee becomes part of its contract, whatever the declared signature says.

Applied here: an LLM-backed `ticket_classifier` and a Python `ticket_classifier` share a name and a type, but they differ along exactly the axes a caller depends on.

- **Determinism:** the agent varies run to run; the function does not.
- **Failure semantics:** the agent can refuse, hallucinate a label outside the enum, return malformed output, time out or get rate-limited. The function raises typed exceptions or returns.
- **Coverage:** the agent degrades gracefully on odd inputs; the function rejects them or silently misclassifies them.
- **Cost and latency:** these differ by orders of magnitude.

Callers adapt to whichever implementation they have. An upstream agent learns to retry or to phrase arguments loosely. A downstream tool is written to tolerate loose output. Swapping the callee therefore preserves the call site but not the caller's correctness. The note's mechanism hides the most important fact a caller needs: which side of the boundary it is on.

On this view, the claim that refactoring becomes "local" is false in the sense that matters. Only the syntactic edit is local; verification remains global. "Each link can be independently refactored without disturbing the rest" is the location-transparency fallacy restated. A rigorous design would make the boundary *visible*, for example through typed effects, separate retry and validation policies, or explicit nondeterminism markers, rather than unify it away.

## How the note engages it

Partially engaged, and only implicitly. The prompt-testing paragraph requires the prompt to "receive the same set of queue labels". This concedes that output-type compatibility is a precondition and shows that the author treats the interface as more than a name. The note's typed-callables section points the same way, since frontmatter is described as a type signature. The Open Questions raise debugging across the boundary but not the behavioural contract.

Nowhere does the note say what callers may assume about a callee's determinism, failure modes or coverage, or that these must be preserved for the swap to be local. The sentences "refactoring across the boundary becomes a local operation" and "Each link can be independently refactored without disturbing the rest" are stated without that condition.

The attack does not defeat the core mechanism. Stable call sites really do remove one friction: editing every caller and its prompt on each codification. The progression in "Why this matters for constraining" is plausible on that basis. The attack therefore lands against the scope of "local" and "independent", not against the claim that unified calling makes boundary moves cheaper. That is why the outcome is *partially lands*.

## Constructive findings

- State the locality condition explicitly. Moving a component is local when the replacement preserves the caller-relied-on behavioural contract: output type, error and refusal behaviour, and the coverage of inputs the caller sends. Otherwise the caller must be checked. This turns the claim from an overstatement into a bounded one.
- Distinguish syntactic locality (no call-site edit) from behavioural locality (no caller re-verification). Claim the first unconditionally and the second only under the condition above.
- Engage the location-transparency precedent directly. Say why the neural-symbolic case differs from RPC, or concede the parallel and describe the mitigation llm-do uses, if any: output validation at the boundary, schema-constrained agent output, or uniform error types.
- In the four-step progression, name the router introduced in step 3 and treat its misclassification as the new failure mode of the codify step.
- Say what a native unified namespace buys over an adapter that exposes an agent as a tool, so the contrast "without a unified interface, each codification step is a breaking change" is not an overstatement.

## Secondary objections (optional)

- The graph-DSL comparison table is unsourced and may describe older versions of LangGraph and CrewAI, both of which now offer imperative, code-first orchestration. The note's argument needs only the narrower point that a component swap should not require editing orchestration structure.
- Name-based dispatch is presented as a requirement ("This requires **name-based dispatch**"). However, any stable indirection (a protocol, an interface, a registry keyed by something other than a string) would keep call sites stable for code callers. Strings are required specifically because the caller is an LLM emitting text. Scoping the requirement to LLM callers would make it accurate.
- When the caller is an LLM, the callee's description is part of its interface. If the agent and function versions of `ticket_classifier` carry different descriptions or argument schemas, the prompt-level call site has changed even though the name has not. The note should say that the description must also be held fixed.
