---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a completeness [mark](../types/tag-readme.md) (a frontmatter field caching a recomputable index property), a compiled cue (a memory system's derived retrieval hint), a hardcoded contract list inlined in a hot-path instruction, a duplicated file."
    reason: "The opening sentence front-loads a four-item example list with parenthetical glosses before the claim arrives in the next sentence. The claim is still in the first paragraph and the title states it, so it stays findable. Moving the examples after the two-state rule, or cutting them to one or two, would let the rule open the body."
    level: info
  - scope: passage
    quotes:
      - "It is the general form of \"a cache must never be the only copy\" — applied not only to caches but to every derived copy of recomputable truth."
    reason: "The note's most memorable framing of the claim sits at the end, after the instance list, where it reads as an afterthought. Placing the cache analogy beside the opening statement of the rule would make the claim easier to remember. No new commitment is needed."
    level: info
outcome: pass
---

# Review

The note's strongest claim, stated in one sentence from its own commitments, is: a copy of information recomputable from a ground-truth source must either be machine-checked against that source or not exist, because a hand-maintained copy that consumers trust risks silent, unbounded wrongness, while an absent copy costs only a bounded recomputation.

The structure makes this claim prominent. The title states the rule. The description repeats it. The first paragraph ends with "exactly two valid states" and "no safe middle." The first section then gives the asymmetry that justifies the word "forbidden." Later sections are subordinate to the rule. They scope it to the deterministic end of derived knowledge, say what enforcement buys, list the preconditions for "checked," draw consequences and give instances. Each section heading says what job the section does for the rule.

The heaviest apparatus is the section "Where the rule applies." It is one dense paragraph covering managed staleness, lineage, make-like detection, holistic rework and Level A/B checks. It still serves the claim by marking where the rule stops applying, and it comes after the claim and its justification, so it does not hide the claim. Two smaller shape issues make the claim slightly less memorable than it could be; they are recorded as INFO findings. Neither hides the claim, so the outcome is PASS.
