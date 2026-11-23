---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

The central claim is "A unified interface lets programmers choose prompts or code without changing callers". Its leaks are asymmetric.

- **"unified interface":** The concrete term would be "llm-do's shared callable binding". Downgrade test: the argument comes from information hiding and from properties of the two execution regimes, not from llm-do specifics. The note says why it does not depend on llm-do. Any shared name, arguments, result format and description produces the effect. Forbids test: the general wording rules out swaps without call-site edits in any system that exposes agents and tools through separate invocation surfaces. The note explicitly contrasts that case. The abstraction is earned by argument.
- **"prompts or code":** These are concrete terms that the mechanism uses directly.
- **"callers":** The note works both instance classes, LLM callers and code callers, and each drives one leak direction. The generality is load-bearing.

Abstraction is concentrated in the one place the argument needs it. It is not spread across the prose.
