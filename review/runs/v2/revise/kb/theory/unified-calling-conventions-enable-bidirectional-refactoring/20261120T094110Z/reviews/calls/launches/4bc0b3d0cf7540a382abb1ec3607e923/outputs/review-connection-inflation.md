---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the type-theoretic view that llm-do operationalises"
    reason: "The body already links instructions-are-typed-callables and says \"llm-do operationalises this\". The footer entry repeats that relationship nearly word for word, with no relationship label and no added navigational context."
    level: warn
  - scope: passage
    quotes:
      - "the operational mechanism: observe agent behavior, extract to code — enabled by stable call sites"
    reason: "Step 2 of the body links spec-mining and explains it as observing that a spec consistently resolves one way and committing that to code; step 3 states that the call site does not change. The footer restates that framing without a relationship label or new context."
    level: warn
  - scope: passage
    quotes:
      - "the mechanism that unified calling makes frictionless"
    reason: "The body links constraining and argues that unified calling removes the breaking-change friction from each step. The footer compresses that argument without adding a label. This entry is borderline because a definition link in the footer still has some lookup value."
    level: info
  - scope: passage
    quotes:
      - "the phase transition from neural to symbolic that unified calling makes a local operation"
    reason: "The body links codification and the intro already says refactoring across the boundary \"becomes a local operation\". The footer adds the 'phase transition' gloss but no relationship label. This entry is borderline for the same reason as the constraining entry."
    level: info
outcome: warn
---

# Review

The footer has eight entries. Three add value the body lacks. The "Abstracted into" entry and the two "extends:" entries for programming-practices and relaxing signals point to notes the body does not link and have typed relationships. The prompting-changes entry repeats an inline link, but it adds a `grounds:` label and an explicit framing of the dependency, so it passes the gate's second question.

The four remaining entries carry no relationship label and repeat the body's inline framing for the same targets. Two do so closely: typed-callables, where the footer echoes the body's "operationalises", and spec-mining, where the footer paraphrases steps 2 and 3. Those two are inflated. Constraining and codification are near-restatements as well, but footer links to core definitions keep slight lookup value, so they are recorded as info. Adding a typed label with a distinct reader-facing reason, or dropping the entries, would resolve the findings.
