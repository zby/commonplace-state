---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Testing or centralizing a validator lowers the cost of assurance but does not prove the validator correct."
    reason: "The general requirement list names the role \"checker\", but this sentence switches to \"validator\", the KB-specific tool from the mark example. Using \"checker\" keeps the condition general. This is minor because a validator is clearly one kind of checker."
    level: info
outcome: pass
---

# Review

The title and opening state a general claim about any retained derived result. The KB-specific material is explicitly framed as illustration: "Two retained results in this KB land differently", followed by sections named for each example. The frontloading link is explicitly extended "to persisted artifacts". The general sections use general terms ("retained result", "checker", "source"), and the one place that ties back to the mark marks itself as such ("The mark's contract supplies the first three"). The only slip is "validator" in the fourth condition, recorded as INFO.
