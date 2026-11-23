---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This note extends that callable structure to tools.
  reason: 'The typed-callables section carries the thinnest separate claim: it restates
    the unified-interface idea in typed-callable vocabulary and mostly serves as a
    connection. Its llm-do detail (`.agent` files as signature plus prompt) adds a
    little concreteness, so it is not pure repetition, but it could fold into the
    mechanism section without loss.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/0d0f43d22cff71d65dfb4c23/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 33bc96d018eb47759199e2647dea7376
completed-at: '2026-11-20T11:09:32Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/outputs/review-claim-to-section-ratio.md
raw-output-sha256: 23610999b7ac04f314d2c724bf8e127c71d894c8c6ea95e4e95f744a653f0444
format: 2
---

# Review

## Summary

The note has six headed sections plus a lead. It supports them with about five distinct non-obvious claims and two justified support units, so its sections do not outnumber its substance.

Distinct non-obvious claims:

1. A shared name, signature and description gives information hiding across the prompt–code boundary, so implementations swap without caller edits (lead).
2. Unlike code-to-code hiding, the abstraction leaks asymmetrically. Prompt-to-code exposes loose LLM callers, while code-to-prompt exposes the cost, latency and error assumptions of code callers (What the interface hides and what leaks).
3. Practical consequence: enforce schemas at the boundary before codification, and write call sites that may revert to prompts for fallible, higher-latency calls (same section).
4. Without a unified interface, codification is a breaking change that probably pushes teams toward big-bang rewrites. The note marks this as an expectation (Why this matters for constraining).
5. The three moves differ: refactoring by codification, prototyping in a prompt, and relaxing. Only the first preserves behavior, yet all three stay local to the binding (same section).

Support units that need separate treatment:

- **The mechanism** grounds the abstract claim in a concrete runtime binding. It also states that the programmer chooses the implementation per run rather than per call, which is a boundary condition.
- **Scope** carries three boundary conditions: call invariance is not behavioral invariance, adapters are needed for structural changes, and call sites need headroom.

The typed-callables section is the only one close to restating framing (see the finding). Open Questions is a conventional tail, not a restating section. The ratio passes.
