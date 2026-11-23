---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

Qualifiers in the title, description and opening claim:

- **"unified interface":** This is load-bearing. The argument depends on a shared name, arguments, result format and description. The constraining section contrasts it with systems that expose agents and tools through different invocation surfaces, where a swap is a breaking change.
- **"programmers choose":** This is load-bearing. The mechanism section separates a programmer's binding choice from a runtime that decides per input. The claim about callers staying unchanged concerns a deliberate rebinding.
- **"prompts or code":** This is load-bearing for the asymmetry. Both leaks depend on the two regimes differing: prompt tolerance against code strictness, and model latency and fallibility against function execution. Deleting the qualifier would turn the claim into ordinary information hiding, which the note explicitly contrasts with its own case. The wording is also intentional LLM-domain scoping.
- **"without changing callers":** This is the claim's content, and the Scope section qualifies it with adapters and call-site headroom.

Removing any of these qualifiers would either falsify the asymmetry claim or erase the contrast the note draws. None narrows the claim without doing work.
