---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: 3e7759255f65a11f9ff3153d71924ccc396c0fb06f9b102299619a6b04d223a6
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: 8a85c650bd4b4d5d87aec905cd5158d082723035defc6f5e48a8490d50b93c1d
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/d0054551d0810923973091d3/inputs/target/kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/d0054551d0810923973091d3/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 32d86c19c20348a7bd7953165451d419
completed-at: '2026-11-16T11:24:59Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/32d86c19c20348a7bd7953165451d419/outputs/review-anthropomorphic-framing.md
raw-output-sha256: 580fe13a73c975c1a3639b72a3032b0599724986a1de618aca0c268de30d7ba0
format: 2
---

# Review

The note makes no claims about model internals or model cognition. Its subjects are storage surfaces (active work state, retrospective memory, chat history, a project instruction file) and a reviewed software kit.

Phrases such as "Retrospective memory answers 'what happened?'", "Active work state answers a different question" and "Those surfaces fail differently" are conventional metonymy for what a stored surface supplies to its reader. "Each resumed session reconstruct the real state" describes work that the agent session must do, not an attributed mental property. The sentence "it has no built-in reason to delete work that is done" says that the file format has no deletion mechanism; it does not claim the file has reasons in a cognitive sense. None of these phrases calls for a technical replacement.
