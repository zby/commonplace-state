---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cead3a2ab3223a39a27d524d121b933c37329874d980e453c9124a146044e75a
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:59Z'
findings:
- scope: passage
  quotes:
  - The calling convention is uniform across the chain. Each link can be independently
    refactored without disturbing the rest.
  reason: The derivation covers refactorings that keep a component's interface fixed.
    This sentence, and the 'progression is smooth' framing, invite reliance across
    all neural/symbolic refactorings, including ones where codification changes arguments
    or outputs. No transfer relation or boundary covers that surplus. The central
    claim's 'enable' wording is modest, and the mechanism partly carries the transfer,
    so this is a supporting-claim overreach rather than a central one.
  level: info
- scope: document
  quotes: []
  reason: 'The note''s empirical support is one system''s design (llm-do), described
    rather than observed in use, plus hypothetical worked examples. The central claim
    is stated generally. The transfer relation is gestured at rather than articulated:
    interface substitution is independent of the implementation. Open Questions marks
    scale and host-language transfer as open, which covers part of the surplus.'
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/03803ac55cafa43c19b75e64/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-unwarranted-scope.md
raw-output-sha256: 0cd9bebce04ac8740499f7dd8a9cbf9056d6b59114ac0b3f460f70ff3e0dc94a
---

# Review

**Claimed scope.** Systems in which neural and symbolic components share a calling convention. In such systems, components can move in either direction without call-site changes.

**Presented support.**

- A derivation: same interface plus name resolution means callers are insulated from implementation changes.
- One reported design, llm-do, with no reported usage episodes.
- Constructed examples: `sanitize_filename` and `ticket_classifier`.

**Exercised domain.** The derivation covers every case where its premise holds, which means the interface really is preserved across the swap. That premise is general, not tied to llm-do. It works as a stated transfer relation for the headline "enable" claim, which asserts an enabling condition rather than a guaranteed outcome.

**Surplus.** The surplus is in supporting sentences that drop the precondition ("each link can be independently refactored", "the progression is smooth"), and in the general claim's reliance on a single system. Open Questions marks scale and host-language transfer as open. Because the central claim is carried by its mechanism and the overreach is in supporting claims, the result is PASS with INFO.
