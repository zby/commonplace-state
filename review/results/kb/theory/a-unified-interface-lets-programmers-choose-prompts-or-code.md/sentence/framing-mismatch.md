---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
findings:
- scope: passage
  quotes:
  - a codification step that moves a component from one surface to the other is a
    breaking change
  reason: The mechanism is that agents and tools sit on different invocation surfaces,
    so any move between them breaks call sites. The sentence frames it as a codification
    step only. The next paragraph shows that the unified interface also spares the
    two code-to-prompt moves (prototyping and relaxing), and those would be equally
    breaking under split surfaces. The framing excludes cases the mechanism covers;
    'a move between surfaces in either direction' would match it.
  level: warn
- scope: passage
  quotes:
  - Enforcing input schemas strictly at the call boundary while the implementation
    is still a prompt prevents callers from accumulating this hidden coupling
  reason: The coupling described includes 'loosely phrased' and 'context-dependent'
    arguments that a prompt resolves by inferring intent. Schema enforcement catches
    malformed arguments, but schema-valid arguments that depend on the prompt's interpretation
    can still accumulate coupling. The remedy is framed as covering the whole mechanism
    when it covers the structural part.
  level: info
- scope: passage
  quotes:
  - Code to prompt exposes runtime assumptions in code callers.
  reason: The latency, cost and error-handling mechanism also applies to LLM callers,
    such as an agent loop with a token budget that calls the rebound name repeatedly.
    The Scope bullet on call-site headroom states it generally ('the caller's latency
    budget'). The bullet emphasizes code callers without explicitly excluding LLM
    callers.
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/4fc5ec5d51b19fbdb5120ddc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-framing-mismatch.md
raw-output-sha256: a74abb6be5b994d82e800a0809c215f85da6fc165f0bf72b55370a818ea0b9fe
---

# Review

The note's central mechanism is framed correctly. A unified interface hides how an operation is implemented but not which execution regime handles it, and the leak differs by swap direction.

One framing excludes cases its own mechanism covers. In "Why this matters for constraining", the breaking-change problem of split invocation surfaces is attributed to "a codification step". The same section then shows the unified binding sparing callers in code-to-prompt moves. Split surfaces would make those moves break call sites too. The sentence should name a move in either direction.

Two narrower framings are recorded at info level. The schema-enforcement remedy is presented as preventing the whole loose-caller coupling, but it addresses only its structural part. The code-to-prompt leak is framed around code callers, though LLM callers with budgets face the same latency and cost exposure.
