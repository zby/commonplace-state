---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The first half of the title, that callers need no change when the binding changes, follows almost definitionally from a shared name, arguments and result format. Its explanatory content lies in the asymmetric-leak account, which the title does not name and only the description states. The mechanism is present and constrained; the headline simply foregrounds its least informative part."
    level: info
outcome: pass
---

# Review

## Summary

**Mechanism.** The note explains that a shared binding hides how the rule is implemented. The binding cannot hide which execution regime handles the call. Because LLM callers rely on natural-language descriptions and on tolerance, and code callers rely on latency, cost and deterministic failure, each swap direction exposes a different assumption.

**Variation test.** Suppose prompt-backed callees were as strict as code. Then the prompt-to-code leak would disappear, and the asymmetry claim would change. Suppose prompt calls had the latency and failure profile of functions. Then the code-to-prompt leak would disappear. The conclusion therefore depends on the premises the note uses, so it is not easy to vary.

**Falsifiability.** Two observations would contradict the claim: swaps that required call-site edits despite a shared binding, or leaks that did not differ by direction.

**Ad-hoc accommodation.** The Scope bullets on behavioral invariance, adapters and call-site headroom follow from the stated mechanism. They are not escape hatches. The headroom condition is a direct consequence of the code-to-prompt leak.

The explanation is adequate. The INFO finding concerns emphasis in the title, not a missing mechanism.
