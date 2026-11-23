---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest."
    reason: "The derivation covers refactorings that keep a component's interface fixed. This sentence, and the 'progression is smooth' framing, invite reliance across all neural/symbolic refactorings, including ones where codification changes arguments or outputs. No transfer relation or boundary covers that surplus. The central claim's 'enable' wording is modest, and the mechanism partly carries the transfer, so this is a supporting-claim overreach rather than a central one."
    level: info
  - scope: document
    quotes: []
    reason: "The note's empirical support is one system's design (llm-do), described rather than observed in use, plus hypothetical worked examples. The central claim is stated generally. The transfer relation is gestured at rather than articulated: interface substitution is independent of the implementation. Open Questions marks scale and host-language transfer as open, which covers part of the surplus."
    level: info
outcome: pass
---

# Review

**Claimed scope.** Systems in which neural and symbolic components share a calling convention. In such systems, components can move in either direction without call-site changes.

**Presented support.**

- A derivation: same interface plus name resolution means callers are insulated from implementation changes.
- One reported design, llm-do, with no reported usage episodes.
- Constructed examples: `sanitize_filename` and `ticket_classifier`.

**Exercised domain.** The derivation covers every case where its premise holds, which means the interface really is preserved across the swap. That premise is general, not tied to llm-do. It works as a stated transfer relation for the headline "enable" claim, which asserts an enabling condition rather than a guaranteed outcome.

**Surplus.** The surplus is in supporting sentences that drop the precondition ("each link can be independently refactored", "the progression is smooth"), and in the general claim's reliance on a single system. Open Questions marks scale and host-language transfer as open. Because the central claim is carried by its mechanism and the overreach is in supporting claims, the result is PASS with INFO.
