---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

The title "Unified calling conventions enable bidirectional refactoring between neural and symbolic" makes a contestable claim. An informed practitioner could argue the opposite: matching a call signature does not make an LLM-backed component and a Python function interchangeable. Nondeterminism, cost, latency and failure modes differ, so swapping implementations behind one name might still force changes at call sites or in callers' error handling. Someone could also argue that the main barrier to moving the boundary is behavioural equivalence, not interface shape. Because a knowledgeable reader could dispute the title, it is not a truism.

The claim also goes beyond the familiar point that a stable interface hides its implementation. It says that a shared convention makes movement possible in both directions (codifying and relaxing) and makes each move a local operation. That is the non-obvious point the note sets out to establish.
