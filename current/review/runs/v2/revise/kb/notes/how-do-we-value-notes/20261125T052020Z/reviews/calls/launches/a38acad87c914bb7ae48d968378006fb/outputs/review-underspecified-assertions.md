---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Commonplace currently spreads note valuation across five partial lenses rather than one rule"
    reason: "Unresolved mechanism and scope. Reading A: Commonplace's operating workflows (admission contracts, review gates, ranking) apply these five lenses when deciding about notes. Reading B: the KB's theory notes articulate five lenses, some of them only proposals not yet used in selection (for example the quality score). The readings need different evidence: A needs shipped mechanisms, B only needs the linked notes. They also change what follows. Under A, the Stakes retirement condition ('relies on ad-hoc judgment rather than a tested valuation practice') is partly met. Under B, selection is still almost entirely ad hoc. The bullets mix shipped and proposed items, so nearby context does not decide between the readings."
    level: warn
  - scope: passage
    quotes:
      - "it would narrow or retire once Commonplace adopts and validates an explicit selection mechanism"
    reason: "'Validates' leaves the retirement threshold open. It could mean passing review, or showing counterfactual benefit in live use as the system-use lens describes. The choice affects when the query retires. This is not shown to be material to the note's current argument, so it is INFO."
    level: info
outcome: warn
---

# Review

## Summary

Most load-bearing assertions are specific enough. Each lens bullet names its test, and the conjecture states its condition ("if production favors fluent local additions"). The root-question item explains its closed-loop failure. The cold-start item names the timing gap.

The main underspecified assertion is the sentence that frames Current answer. It does not say whether "spreads note valuation" describes what Commonplace's machinery does or what its notes argue. The bullets combine a shipped invariant (answerability) with proposed mechanisms (quality scores). The two readings need different evidence and imply different distances from the Stakes retirement condition. That is the WARN.

The retirement condition's "validates" is open in a similar way, but it does not drive the current argument, so it is recorded as INFO.
