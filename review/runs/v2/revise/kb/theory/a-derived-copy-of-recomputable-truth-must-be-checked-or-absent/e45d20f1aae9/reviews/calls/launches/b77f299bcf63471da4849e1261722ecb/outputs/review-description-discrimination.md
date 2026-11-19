---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The description mostly restates the title. It expands 'derived copy of recomputable truth' to 'a copy of information recomputable from a ground-truth source', 'checked' to 'machine-checked against that source', and 'absent' to 'not exist'. It then states the excluded middle ('hand-maintained-and-trusted is forbidden'), which the title already implies. It does not give the mechanism (an absent copy costs one bounded recomputation, while a false copy causes silent, unbounded wrongness). It also omits the scope boundary (the rule applies only where verification is a deterministic Level A check; judgment-level dependencies stay under managed staleness) and the implication (omission is the fallback when a copy cannot be checked). Any of these would help an agent choose this note over neighbouring lineage and staleness notes."
    level: warn
outcome: warn
---

# Review

## Summary

The description adds a little: "machine-checked" makes "checked" precise, and it names the forbidden state. Most of it is still a paraphrase of the title. In a short result list next to the lineage, make-like staleness and compiled-view notes, it would not show what this note specifically argues: the asymmetry between the cost of an absent copy and the cost of a false one, and the limit of the rule to mechanically derivable copies. Replacing part of the paraphrase with that mechanism or scope would make the description discriminate.
