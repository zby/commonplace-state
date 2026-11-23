---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The practical consequence is that interface parity alone is not enough for safe swapping."
    reason: "Claim drift by omission. The body establishes a qualified claim: a unified interface keeps a prompt–code swap local to the binding at the call site, but the abstraction leaks asymmetrically. Prompt-to-code breaks LLM callers that relied on lenient interpretation. Code-to-prompt breaks code callers' latency, cost and error-handling assumptions. Caller-free swapping therefore holds only when schemas are enforced before codification and call sites have headroom for fallible, slower model execution. The unqualified H1 says choice is possible 'without changing callers', which the body explicitly limits. The title should carry the leak or its condition, for example that the interface keeps swaps local only where callers were written for both regimes."
    level: warn
outcome: warn
---

# Review

## Summary

The body supports the title's core mechanism. The llm-do binding, the `ticket_classifier` walkthrough and the three swap moves all show implementation changes that stay local to the binding without call-site edits.

However, about half of the body sets limits on that claim. The opening paragraph ends by saying the abstraction "leaks asymmetrically". The "What the interface hides and what leaks" section shows how each swap direction breaks callers. The Scope section says call invariance is not behavioral invariance and that bidirectional swapping needs call-site headroom. The body therefore establishes a qualified claim, while the H1 states an unqualified one. The drift is not severe, because the call text truly stays unchanged. Still, a reader who links on the title alone would take away a stronger promise than the body delivers.
