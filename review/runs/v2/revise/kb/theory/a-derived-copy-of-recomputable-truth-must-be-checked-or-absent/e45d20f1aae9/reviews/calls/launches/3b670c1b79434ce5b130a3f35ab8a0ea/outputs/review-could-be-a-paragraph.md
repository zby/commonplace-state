---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

A one-paragraph version could state the core rule: a derived copy of recomputable truth must be machine-checked or absent. It would lose several load-bearing parts:

- **The asymmetry argument.** Bounded recomputation against silent, unbounded wrongness is what makes hand-maintained-and-trusted forbidden rather than merely risky.
- **The regime boundary.** The rule applies only where mechanical derivation makes verification Level A. Where verification is judgment, managed staleness applies and the hand-maintained dependent artifact is unavoidable. This boundary case is non-obvious.
- **The third class.** Recomputable-and-checked reconciles two otherwise conflicting notes, frontloading and fix-what-the-executor-can't-determine.
- **The four preconditions.** These are failure conditions. Precondition 3 excludes execution-generated evidence. Precondition 4 argues that the validator bottoms out instead of reopening the regress, and that a judgment-based derivation rule relocates the forbidden state.
- **Instances in different states of application.** These are the evidence for generalization.

Compressing the note to one paragraph would drop boundary cases and inferences, so the multi-section structure is justified.
