---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

A one-paragraph version would keep the headline, that one interface lets programmers swap prompts and code without editing callers. It would lose most of the load-bearing content:

- **The asymmetric leak.** Each swap direction breaks a different caller assumption, through a different mechanism. Prompt-to-code breaks LLM callers that relied on the prompt tolerating loose arguments. Code-to-prompt breaks code callers' latency, cost and determinism assumptions, for example in loops or with exception handling. This is the note's main non-obvious claim, and it needs both mechanisms spelled out.
- **The derived prescriptions.** Enforce schemas before codification, and write movable call sites for fallible, higher-latency calls. These follow from the leak analysis.
- **Boundary conditions.** Call invariance is not behavioral invariance, structural signature changes still need adapters, and swapping back requires call-site headroom.
- **The three-move distinction.** Refactoring, prototyping and relaxing are separated. Only the first preserves behavior, yet all three stay local to the binding.

These are distinct claims, support paths and failure conditions, so the multi-section structure is justified.
