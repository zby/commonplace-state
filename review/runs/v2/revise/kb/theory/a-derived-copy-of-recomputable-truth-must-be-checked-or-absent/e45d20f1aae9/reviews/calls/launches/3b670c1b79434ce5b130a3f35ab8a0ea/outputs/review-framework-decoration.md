---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "already enforced, stated but unenforced, resolved by omission, and not yet applied"
    reason: "The instances section introduces a four-state classification and says the spread across states shows generalization, but the bullets do not use it consistently. Only the tag-README mark ('enforced and shipped') and the hot-path contract values ('currently resolved by omission') are labelled. The compiled-views bullet is never marked 'stated but unenforced', and the duplicated-template bullet never says the byte-identity check is 'not yet applied'; it says only that the files must be byte-identical. A reader cannot confirm the claimed spread from the bullets, so the classification promises more than the section delivers. Either label each bullet with its state or drop the four-state framing."
    level: warn
outcome: warn
---

# Review

## Summary

Most of the note's structures do real work:

- **Checked/absent dichotomy.** This is the rule itself; each branch has distinct consequences.
- **Level A/B check-cost distinction.** Borrowed from the text testing pyramid, it locates where the regime changes from managed staleness to enforce-or-omit. It supports a decision about which rule applies.
- **Arbitrary / situational / recomputable-and-checked.** The third class resolves a stated conflict between two notes, so the categories enable an inference.
- **Four numbered preconditions.** Each is a decision rule or boundary condition. Precondition 4 is cited again in instance 1, and preconditions 1 and 3 are cited in the footer's contrast with the history note. The list cannot be reduced to one sentence without losing exclusions.

The exception is the four-state labelling of the instances section. It is presented as the evidence of generalization, but two of the four states are never attached to their bullets. The instance list is load-bearing as evidence; the state vocabulary over it is partly decorative as written.
