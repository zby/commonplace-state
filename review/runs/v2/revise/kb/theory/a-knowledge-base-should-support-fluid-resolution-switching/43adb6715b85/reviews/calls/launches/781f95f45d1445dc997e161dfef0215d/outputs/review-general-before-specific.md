---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Commonplace mechanisms"
    reason: "The system-specific mechanisms section, named by a proper noun, comes before 'The evaluative criterion', which states the general criterion those mechanisms serve. The mechanisms exemplify the criterion rather than qualifying it. However, the opening section already states the general rule: views at different scopes, and cheap switches in both directions. So the reader meets the rule before the instances, and the later section only formalizes it. The order is defensible. Moving the criterion section first would also be acceptable."
    level: info
outcome: pass
---

# Review

## Summary

There are five adjacent section pairs after the introduction. Only one pair
places a more specific section before a more general one: "Commonplace
mechanisms" before "The evaluative criterion". That pair gets an INFO
finding, not a WARN. The introduction already states the general pattern,
so the reader does not see the instances before the rule.

The other pairs pose no ordering problem:

- "Connection to discovery" follows the criterion and extends it.
- "Boundaries" qualifies the concept after it has been stated.
- "Open questions" comes last, as expected.
