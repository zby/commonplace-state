---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a codification step that moves a component from one surface to the other is a breaking change"
    reason: "The mechanism is that agents and tools sit on different invocation surfaces, so any move between them breaks call sites. The sentence frames it as a codification step only. The next paragraph shows that the unified interface also spares the two code-to-prompt moves (prototyping and relaxing), and those would be equally breaking under split surfaces. The framing excludes cases the mechanism covers; 'a move between surfaces in either direction' would match it."
    level: warn
  - scope: passage
    quotes:
      - "Enforcing input schemas strictly at the call boundary while the implementation is still a prompt prevents callers from accumulating this hidden coupling"
    reason: "The coupling described includes 'loosely phrased' and 'context-dependent' arguments that a prompt resolves by inferring intent. Schema enforcement catches malformed arguments, but schema-valid arguments that depend on the prompt's interpretation can still accumulate coupling. The remedy is framed as covering the whole mechanism when it covers the structural part."
    level: info
  - scope: passage
    quotes:
      - "Code to prompt exposes runtime assumptions in code callers."
    reason: "The latency, cost and error-handling mechanism also applies to LLM callers, such as an agent loop with a token budget that calls the rebound name repeatedly. The Scope bullet on call-site headroom states it generally ('the caller's latency budget'). The bullet emphasizes code callers without explicitly excluding LLM callers."
    level: info
outcome: warn
---

# Review

The note's central mechanism is framed correctly. A unified interface hides how an operation is implemented but not which execution regime handles it, and the leak differs by swap direction.

One framing excludes cases its own mechanism covers. In "Why this matters for constraining", the breaking-change problem of split invocation surfaces is attributed to "a codification step". The same section then shows the unified binding sparing callers in code-to-prompt moves. Split surfaces would make those moves break call sites too. The sentence should name a move in either direction.

Two narrower framings are recorded at info level. The schema-enforcement remedy is presented as preventing the whole loose-caller coupling, but it addresses only its structural part. The code-to-prompt leak is framed around code callers, though LLM callers with budgets face the same latency and cost exposure.
