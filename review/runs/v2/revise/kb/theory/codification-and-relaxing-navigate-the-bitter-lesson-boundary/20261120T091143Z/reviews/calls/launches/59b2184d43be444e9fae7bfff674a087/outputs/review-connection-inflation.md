---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the bottom-up extraction method that avoids the vision-feature failure mode"
    reason: "The body already links spec mining and fully states this relationship: it starts from a working system and so avoids the vision researchers' composition bet. The footer adds no typed relationship label and no new framing. It also states the relationship more strongly ('avoids') than the body's hedged 'improves the odds ... But it's still a bet'."
    level: warn
  - scope: passage
    quotes:
      - "detects when codified components are encoding vision features"
    reason: "The body already links relaxing signals and states the same relationship, that they are how you detect a codified component that encodes an accident rather than a spec. The footer entry has no typed relationship label and adds no navigational context beyond that inline use."
    level: warn
  - scope: passage
    quotes:
      - "grounds: the case-level diagnosis this note reads from the author's side"
    reason: "This mostly restates the body's inline framing ('seen from the author's side rather than the survivor's', and that it is conjectural). It is not inflated, because it adds the typed 'grounds' relation and the note that the target does not restore the foresight this note denies. It is close to the line, however."
    level: info
outcome: warn
---

# Review

## Summary

Six Relevant Notes entries were checked against the body's inline links.

- **exact-implementation-does-not-validate-a-requirement**: not inflated. The body uses it to introduce the distinction, and the footer adds the typed `foundation` relation and the "operationalizes" framing.
- **verifiability-gradient**: not linked in the body, so the footer adds a new navigation edge.
- **constraining-and-extraction-both-trade-generality-for-reliability**: the footer's wording is close to the inline citation, but it adds the typed `grounds` relation, so it is not inflated.
- **bitter-lesson-selects-against-unearned-reach-not-against-structure**: borderline but acceptable (see the info finding).
- **spec-mining-as-codification** and **operational-signals-that-a-component-is-a-relaxing-candidate**: both fail both tests. The body fully articulates the relationship, and each footer entry is untyped prose that paraphrases it. Typing them would make them useful, for example with `extends` or `see-also` and a context phrase the body lacks, such as what the target contains beyond this note's use. Otherwise they could be dropped. The spec-mining entry should also match the body's hedge rather than claim the method "avoids" the failure mode.
