---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Each callable receives only its declared arguments rather than the caller's full conversation history"
    reason: "The section headed 'The mechanism' describes llm-do's particular design: one callable namespace, context isolation through declared arguments, and per-run binding chosen by the programmer. The heading presents this as the general mechanism rather than as one implementation. Context isolation, for example, is not required for caller-invariant swapping. Retitling the section or marking llm-do as an example (e.g. 'One implementation: llm-do') would keep the general claim from appearing to depend on llm-do's choices. Readers can still see that llm-do is a concrete instance, and the opening paragraph states the claim independently, so the risk is low."
    level: info
outcome: pass
---

# Review

## Summary

The title and opening paragraph claim generality: any unified interface over
prompt-backed and code implementations. Most of the specific material is framed
as illustration:

- `ticket_classifier` is introduced with "such as" and a "Suppose the team..."
  scenario.
- llm-do's `.agent` files are introduced with "llm-do implements this pattern".

The one narrower element is the mechanism section. It presents llm-do's specific
runtime choices under a generic heading. This is recorded as info rather than
warn, because the general claim is stated independently and llm-do is
recognisable as an instance.
