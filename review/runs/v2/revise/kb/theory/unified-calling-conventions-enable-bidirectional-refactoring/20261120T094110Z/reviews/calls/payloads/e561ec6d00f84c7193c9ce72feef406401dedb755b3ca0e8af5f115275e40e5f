---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "But without a unified interface, each codification step is a breaking change: call sites must be updated, prompt structure must change, the agent's view of available operations shifts. This friction discourages incremental refactoring and pushes toward big-bang rewrites."
    reason: "This is an empirical-sounding causal claim about what friction does to development practice ('discourages incremental refactoring', 'pushes toward big-bang rewrites'). It is stated in the same declarative register as the design description, but the note presents no observation and cites no evidence for it. It also overstates the derivation: without a unified interface a codification step changes call sites, but 'each ... is a breaking change' asserts this universally."
    level: warn
  - scope: passage
    quotes:
      - "With unified calling, the progression is smooth:"
    reason: "The progression is a constructed scenario: the `sanitize_filename` steps are hypothetical, and the observation step ('the agent consistently lowercases...') reads like a report. The note presents the scenario as an established outcome ('is smooth', 'the call site doesn't change'). Nothing shows whether llm-do users actually followed this progression, or whether it is a design-level derivation. Support for llm-do's architecture (shared namespace, name dispatch) is thereby presented as support for the experienced smoothness of refactoring."
    level: warn
  - scope: passage
    quotes:
      - "Each link can be independently refactored without disturbing the rest."
    reason: "This derived consequence holds only when interfaces are preserved, yet it reads as an established property of the architecture. The status is recoverable as a derivation from the stated premise, but only by effortful reading."
    level: info
outcome: warn
---

# Review

The note mixes three kinds of claim:

- A reported design: llm-do's shared namespace, `.agent` files, name-based dispatch and imperative scheduler.
- A derived consequence: a shared interface means callers need not change.
- Proposed or empirical claims about development practice: friction pushes toward big-bang rewrites, and the progression is smooth.

The design description and the derivation are presented at an appropriate status. The practice-level claims are not. They carry the same declarative confidence as the design description, although the note offers no observation of refactoring episodes, and the worked progression is a constructed scenario written as if it had been observed. Support for "llm-do has this architecture" thus spreads to "refactoring with it is smooth".

The Open Questions section marks scale, debugging and language transfer as open. That correctly hedges those claims but leaves the flagged ones untouched.
