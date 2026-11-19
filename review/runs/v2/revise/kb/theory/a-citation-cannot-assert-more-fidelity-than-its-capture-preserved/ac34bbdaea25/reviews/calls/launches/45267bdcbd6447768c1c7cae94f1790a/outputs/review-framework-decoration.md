---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "**Second-hand** — the captured text is itself another party's restatement"
    reason: "The third category is introduced as part of the forced stratification but the argument never uses it again: the notation mechanism, the locator corollary (\"differ in provenance quality by a full layer\") and the scope boundary all turn only on verbatim versus paraphrase. The category carries its own local decision rule (name the intermediary), but it is not a product of the lossy-extraction constraints the section says force the layering. Second-hand status is a property of the captured source and can coexist with a verbatim capture. The taxonomy therefore introduces more categories than the stated claim uses."
    level: warn
  - scope: passage
    quotes:
      - "Fidelity is fixed at ingest and is **non-increasing** downstream"
    reason: "The formal-sounding term is load-bearing rather than decorative. It states the monotonicity that the notation section and the 're-capture is the only raising operation' conclusion both rely on. Recorded for completeness; no change needed."
    level: info
outcome: warn
---

# Review

## Summary

The verbatim/paraphrase distinction is load-bearing, but the third layer, second-hand, is decorative with respect to the note's argument.

## Structures examined

**The three-layer capture taxonomy.** Verbatim versus paraphrase drives every later inference. Verbatim has a mechanical derivation rule (substring match) and paraphrase does not, which is why notation cannot raise fidelity. The same split is the "full layer" difference a position-only locator would erase, and it is what collapses in the lossless-capture boundary case. Those two categories cannot be reduced to one sentence without losing those inferences.

The second-hand category is never used after it is introduced. Deleting it leaves the notation argument, the corollary and the scope section unchanged. It also sits awkwardly in a list that the section says is forced by finite context and copyright: a second-hand passage reaches the KB through an intermediary, not through trimming, and it can be captured verbatim. It provides a useful citation rule (name the intermediary), but that rule is a separate point the argument does not need. Either drop it from the stratification and mention it as an orthogonal provenance dimension, or show where the fidelity-ceiling argument depends on it.

**"Non-increasing".** This is formal-looking notation that does real work. It names the monotonicity property from which "only re-capture raises fidelity" follows, and it supports the prediction that no downstream gate or locator can raise a passage's grade.

**Fidelity versus authority.** This two-term distinction is load-bearing. It resolves an apparent conflict with the linked authority note and gives the composition rule: capture sets a ceiling, and authority is earned beneath it.
