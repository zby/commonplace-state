---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "yet all three stay local to the binding because callers depend only on the interface"
    reason: "This summary sentence contradicts the leak section. There, LLM callers rely on the prompt's tolerance of loose arguments, and code callers rely on latency, cost and deterministic failure, none of which the interface expresses. That section concludes that 'interface parity alone is not enough for safe swapping'. The Scope section adds that callers relying on prior decisions or error behavior need testing after a swap. Saying that callers depend only on the interface compresses away the tension the note itself establishes."
    level: warn
  - scope: passage
    quotes:
      - "Only the first move is a behavior-preserving refactoring."
    reason: "The prompt-to-code move is called behavior-preserving. The leak section says that the same move makes LLM callers that relied on prompt tolerance 'begin failing or triggering literal misreads', which is a behavior change visible to callers. The move description also preserves only 'the rule' the team chose to keep. The term may have drifted from preserving the selected routing rule to preserving behavior in general. This needs the author's confirmation."
    level: info
outcome: warn
---

# Review

## Summary

Key claims by section:

- **Opening:** A shared interface hides implementation, and the abstraction leaks asymmetrically.
- **Leak section:** Callers acquire dependencies beyond the interface, namely input tolerance and runtime profile. Interface parity is insufficient.
- **Scope:** Call invariance is not behavioral invariance, and swaps need testing.
- **Constraining section:** The three moves stay local "because callers depend only on the interface". The first move is behavior-preserving.

The opening, leak section and Scope section agree. The closing summary of the constraining section restates the simple information-hiding picture that the leak section qualified, which contradicts it (WARN). "Behavior-preserving" for prompt-to-code also sits uneasily with the leak described for that same direction (INFO).
