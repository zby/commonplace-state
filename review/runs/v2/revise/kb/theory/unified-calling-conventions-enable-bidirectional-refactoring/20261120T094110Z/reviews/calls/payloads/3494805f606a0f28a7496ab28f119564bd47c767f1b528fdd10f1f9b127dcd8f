---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that owns control flow rather than a graph DSL."
    reason: "The scheduler section supports the title only indirectly. It argues that imperative orchestration lets neural-symbolic refactoring use ordinary code refactorings, and it adds a comparison with graph DSLs that the title does not promise. This is extra material, not drift: the body still mainly establishes that a shared name-based calling convention keeps call sites stable when a component moves in either direction."
    level: info
outcome: pass
---

# Review

## Summary

The body supports the title's claim and scope. It argues that a shared calling convention, implemented through name-based dispatch, keeps call sites stable when a component's implementation changes. That makes moving across the neural-symbolic boundary a local operation.

The body covers both directions named by "bidirectional." The numbered progression covers neural to symbolic: start with an agent, spot a pattern, codify it as `sanitize_filename()`, and leave the call site unchanged. The relaxing step and the `ticket_classifier` example cover symbolic to neural: the same caller sends work to a prompt under the same name while the team tries routing rules. The title's general claim is shown with one system, llm-do. The opening paragraph and the mechanism section present llm-do as an implementation of a general principle, so this is not scope drift.

The only loose fit is the scheduler section, recorded as an info finding.
