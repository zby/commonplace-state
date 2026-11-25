---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: accelerating store bloat into an accretion plateau
  change: 'Replace the coined term with ordinary words: "accelerating store bloat
    until further additions stop improving the system". This is the term''s only occurrence
    in the note.'
  reason: '"Accretion plateau" is coined in the continual-learning article. This note
    does not define it, and the linked note (raw accumulation does not create usable
    memory) does not use it, so here it is unexplained jargon. No occurrence needs
    the distinction: the sentence already names the cause (appending local exceptions,
    store bloat), so "accretion" adds nothing that the ordinary wording loses. The
    plain phrasing states the same consequence, a stall in improvement caused by accumulation,
    without widening or narrowing the claim. kb-role does not list the term as relied
    on. Counter-consideration for the operator: the article that links here uses "accretion
    plateau" twice, so keeping it would preserve cross-artifact wording. If kept,
    it should be glossed at this use (opening-and-title pass).'
description: Retained proposed result of kb/instructions/simplification-passes/abstractions.md
  on kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
format: 1
operation: kb/instructions/simplification-passes/abstractions.md
operation-sha256: 66c1e66712553330a826d33689fc281147d52ac6c08ae6f8510f4eb0cd9238a4
note: kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md
input-sha256: 5ebf2b7f00fd2290167f4d32743338a3d459fe52ccb8a8e565177acddf42617e
candidate: null
candidate-sha256: null
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/artifact/edits/9c8826b9a72c72ef72fea139/observation.json
contract-sha256: cb15395b5b139f4e2c03d3a8bc974b6cdf52f0a427c623b8341fa6cb0835883a
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z
launch: 9689a263d833403682bfb60a443b16f6
completed-at: '2026-11-24T13:45:50Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/credit-assignment-without-a-chain-rule-bounds-selection-based-learning/20261124T133328Z/calls/launches/9689a263d833403682bfb60a443b16f6/outputs/result.md
raw-output-sha256: 393f73bee29972c0763a296d2ba88b587f8a8d084bd9a016ac5cbf1095c369e3
---

# Report

The scope covers the opening's second sentence and the clause "accelerating store bloat into an accretion plateau". I checked each abstraction in those spans.

- **Selection-based learning** — keep (no proposal). The deciding occurrence is the in-scope sentence "Selection-based learning over a store of instructions, hypotheses, checks, and scripts has no chain rule, so its credit assignment is far less scalable than gradient learning." There, the bare word "learning" would also cover gradient learning, which is exactly what the sentence contrasts it with. The term is registered, is linked at its first use, appears in must-keep and is relied on per kb-role. 0 replacements.
- **Accretion plateau** — propose replacing it with ordinary words (see proposal). It has one occurrence, so the change would make 1 replacement.
- **Credit assignment**, **chain rule**, **gradient learning**, **store bloat** — keep (no proposal). These are conventional technical terms or plain words, not coined abstractions. Credit assignment and the chain-rule framing are relied on and protected by must-keep. 0 replacements.

Noticed but not applied: none outside scope.
