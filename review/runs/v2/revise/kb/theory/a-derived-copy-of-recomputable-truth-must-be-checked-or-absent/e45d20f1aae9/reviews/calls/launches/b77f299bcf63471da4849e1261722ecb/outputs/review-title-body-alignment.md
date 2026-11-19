---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "mechanically recomputable from a ground-truth source"
    reason: "The body limits the rule to copies that can be re-derived mechanically and checked deterministically (Level A). It says that judgment-level dependent artifacts, such as natural-language summaries or instructions derived from sources, are not forbidden and stay under managed staleness. The H1 relies on the word 'recomputable' alone to carry that limit. A reader might count an LLM-regenerated summary as 'recomputable'. The body excludes that case, so the alignment holds, but the qualifier 'mechanically' lives only in the body. This is a minor precision point, not drift."
    level: info
outcome: pass
---

# Review

## Summary

The body supports the title's claim. It names exactly two valid states for a derived copy: checked (a validator re-derives the copy and fails on mismatch) or absent (deleted, or replaced by a live read). It justifies the excluded middle through the asymmetry between a bounded recomputation and silent, unbounded wrongness. It also states the preconditions for "checked" and gives instances in four states of application. The scope section, the preconditions and the consequences all keep to the title's subject, derived copies of recomputable truth. The section on what enforcement buys argues that checked copies beat omission, which refines the title's disjunction rather than drifting from it. There is no claim drift or material scope drift.
