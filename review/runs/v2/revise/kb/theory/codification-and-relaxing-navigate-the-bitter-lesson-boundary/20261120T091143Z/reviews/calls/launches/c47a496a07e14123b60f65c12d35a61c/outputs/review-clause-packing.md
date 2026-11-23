---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "seen from the author's side rather than the survivor's: a codification that commits an accident asserts a scope that nothing assessed, and relaxing is what happens to it later"
    reason: "About 50 words carrying five ideas: an identity claim, a characterization of the linked note as a case-level diagnosis, an author/survivor perspective contrast, the claim that a committed accident asserts unassessed scope, and the claim that relaxing follows later. The reader must hold the long link-text clause open before reaching the colon's payload. Split after the identity claim: 'That is the same property the linked conjecture diagnoses, seen from the author's side. A codification that commits an accident asserts a scope nothing assessed; relaxing is what later happens to it.'"
    level: warn
  - scope: passage
    quotes:
      - "replacing an extracted component with a more general one, often a model call, when scale makes that viable, accepting higher cost and lower reliability in exchange for regaining generality"
    reason: "The definition of relaxing chains an appositive ('often a model call'), a condition ('when scale makes that viable') and a trade-off participle ('accepting higher cost ... regaining generality') after the term is introduced, so four ideas hang off one dash. Keep the definition and condition in this sentence and move the trade-off into its own sentence: 'Relaxing accepts higher cost and lower reliability to regain generality.'"
    level: warn
  - scope: passage
    quotes:
      - "The bet shifts from \"will these pieces compose?\" (which the vision researchers lost) to \"is this specific pattern load-bearing?\""
    reason: "The parenthetical sits between 'from' and 'to', and the sentence then appends an appositive and a because-clause. Each dependency is short, so this is tolerable; moving '(which the vision researchers lost)' out of the from/to frame would ease it."
    level: info
outcome: warn
---

# Review

Most sentences in the note stay under the threshold and carry one or two ideas; the bulleted regime definitions and the heuristics are well segmented. Two sentences overload. The bitter-lesson identity sentence in "Every code-extraction codification is a bet" packs an identity, a description of the linked note, a perspective contrast and two further claims behind a long link-text clause. The relaxing definition hangs a condition and a trade-off off one appositive dash. Both can be split without losing content. The spec-mining from/to sentence has a mild interruption that a reordering would fix but does not require one.
