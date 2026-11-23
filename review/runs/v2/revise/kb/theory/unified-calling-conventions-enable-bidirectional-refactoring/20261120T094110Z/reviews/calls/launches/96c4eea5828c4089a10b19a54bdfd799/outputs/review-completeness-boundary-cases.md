---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest."
    reason: "The framework covers swaps that preserve the component's interface, but the note claims every link can be refactored independently. A common boundary case falls outside: codification often narrows the input (an agent accepts free text; the extracted function needs structured arguments) or changes the output type. Then the name stays the same but the call does not, and callers or the invoking prompt must change. The note does not state that interface preservation is a precondition, so this case falls outside the claimed coverage without being marked."
    level: warn
  - scope: passage
    quotes:
      - "3. **Codify** — extract `sanitize_filename()` to Python. The agent still handles ambiguous cases. The call site doesn't change."
    reason: "The intermediate case between the enumerated steps, a component that is partly codified and partly neural, maps onto name-based dispatch only with strain. One name resolves to one implementation, so a split needs either a wrapper that routes between them or a new name for the function. The note does not say which. If it needs a new name, the claim that the call site does not change fails for this step."
    level: info
outcome: warn
---

# Review

The note's framework is name-based dispatch over one namespace, which makes neural and symbolic implementations interchangeable behind a name. It comes with a four-step progression (start neural, observe, codify, extend via relaxing) and a reverse case (relaxing to test a routing rule).

Boundary cases tested:

- **Simplest instance:** replacing a whole agent with a function that has the same arguments and return. This maps cleanly.
- **Reverse direction:** the `ticket_classifier` test run returns the same set of queue labels. The note explicitly keeps the interface fixed here, so this maps cleanly.
- **Interface-changing codification:** this falls outside the claimed coverage (WARN). The note's guarantee holds only when the interface is preserved, but the passages that claim local, independent refactoring never state that condition.
- **Partial codification (step 3):** this is strained. It is unclear how one name serves both the extracted function and the residual agent.
- **Scale:** the note already marks this boundary in Open Questions, so it raises no finding.

The fix need not add a category. A stated precondition (interface-preserving swaps) would bound the claim at the right size.
