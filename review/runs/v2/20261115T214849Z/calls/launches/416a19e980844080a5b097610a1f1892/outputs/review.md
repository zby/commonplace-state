---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "In that regime the hand-maintained dependent artifact is not forbidden; it is unavoidable"
      - "And the interrupt-placement problem dissolves"
    reason: "The scoping section 'Where the rule applies' is the densest part of the note and leans on related-note machinery (managed staleness, make-like timestamps, holistic rework, Level A/B checks, interrupt placement). It supports the claim, since it explains why enforce-or-omit holds only where checks are mechanical. But it is longer than the claim it scopes, and its second paragraph introduces terms (detector plus judge, interrupt placement) that the reader must decode before returning to the rule. A shorter version would protect the claim: one sentence saying that judgment-checked dependents stay under managed staleness, and one saying that a Level A check flips the regime. The rest could be cut or left to the linked notes."
    level: info
  - scope: passage
    quotes:
      - "a compiled cue (a memory system's derived retrieval hint)"
    reason: "The opening sentence lists four example kinds, two with parenthetical glosses, before the paragraph states the rule ('Such a copy has exactly two valid states'). The title and description already carry the claim, so the claim is still findable. Moving the two-states sentence first, or shortening the example list, would make the opening paragraph lead with the rule rather than with examples."
    level: info
outcome: pass
---

# Review

## Core claim

In one sentence: a copy of information that can be mechanically recomputed from a ground-truth source must either be checked by a validator against that source or not exist, because a hand-maintained copy that consumers trust can make them silently and unboundedly wrong.

## Assessment

The claim is easy to find. The title states it as a claim. The description repeats it. The first paragraph ends by stating it plainly: "Such a copy has exactly two valid states," and "There is no safe middle." The next section gives the asymmetry that justifies the word *forbidden*, which makes the claim easy to remember. The later sections each serve the rule. "What enforcement buys" gives the reason to prefer checking over omitting. The precondition list says when checking is possible. The consequences and the four instances apply the rule. None of them competes with it.

The two findings are INFO-level shape issues. Neither hides the claim:

- **The scoping section is heavy.** "Where the rule applies" carries the most apparatus in the note, and much of that apparatus comes from neighbouring notes. Compressing it to the regime flip would make the claim more memorable: judgment-checked dependents are managed for staleness, while mechanically checkable copies follow enforce-or-omit.
- **The opening leads with examples.** The first paragraph lists examples before it states the rule. The title and description offset this, but starting the paragraph with the two-states sentence would make the claim more prominent.

No WARN applies. The core claim does not need to be moved, restated or protected: it already appears early and plainly, and the later material is organized around it.
