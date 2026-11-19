---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A model may need several reads to check a source that exceeds its context budget."
    reason: "This paragraph sits under 'Which evidence a pass is relative to' but concerns the context question, which the note has already assigned to a reader rather than to the wording check. Its first point supports the main claim: an exact excerpt can still omit the context needed to judge use, so a wording pass does not establish support. The closing procedural rule (the checker must retrieve context; the full source can stay outside the model's context) describes how to run a support-judging checker. That is a different mechanism and needs different evidence. Consider keeping only the bounding point, perhaps next to the four-questions section, and rehoming the procedure. Where the procedure should go is unclear."
    level: info
  - scope: passage
    quotes:
      - "Semantic hops compound instead: checking a paraphrase against a paraphrase adds a judgment at each hop, and rewording at either hop can change the proposition."
    reason: "The provenance-chain paragraph supports the main claim: an exact check verifies only its own pair, and exactness is independent of second-hand provenance. The contrast with semantic hops, and the recommendation to check against verified source extracts, concern paraphrase checking. The note's opening places paraphrase outside what the check can match. The contrast briefly sharpens why exact hops do not compound, so it can stay. The recommendation is a branch, and its destination is unclear."
    level: info
outcome: pass
---

# Review

The main claim, taken from the title, description and section structure, is that a quote check establishes only wording agreement with the specific evidence it compared. A pass is relative to that capture or extract. Attribution upstream of the capture, contextual support and truth stay unverified.

Most side material supports this claim in place:

- The four-questions list separates what the check answers from what it does not.
- The cost-versus-risk sentence bounds when a mismatch may count as a failure.
- The normalization and uniqueness paragraphs say what "exact" means.
- The paragraphs on identity binding, and on retained versus accessible material, show what a pass is relative to.
- The scope bullets set boundary conditions.

None of these is a removable branch.

Two passages go beyond the main claim, into how a checker should judge context or paraphrase. Each has a sentence that bounds the main claim and is worth keeping. Each also has procedural or recommendatory content whose destination is unclear. Neither competes with the main claim strongly enough to warrant a WARN, so both are recorded as INFO.
