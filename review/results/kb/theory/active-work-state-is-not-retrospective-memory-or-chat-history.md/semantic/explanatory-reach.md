---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
note-sha256: 3e7759255f65a11f9ff3153d71924ccc396c0fb06f9b102299619a6b04d223a6
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: cc957d3f07c54d38882aedb1ab764406
completed-at: '2026-11-16T11:26:46Z'
findings:
- scope: passage
  quotes:
  - unless it is extended with the required control fields
  reason: This qualifier concedes that a retrospective-memory surface with the right
    control fields could carry live state. That makes the distinction one of fields
    and lifecycle, not of surface kind. The concession improves the explanation rather
    than merely dodging counterexamples, but the title still reads as a distinction
    of kinds. The mechanism ('what the surface stores and when it deletes') could
    be stated as the core claim so the qualifier is no longer needed as an exception.
  level: info
contract: verdict
target-sha256: 8a85c650bd4b4d5d87aec905cd5158d082723035defc6f5e48a8490d50b93c1d
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/a2806c7c541525d380953203/inputs/target/kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/a2806c7c541525d380953203/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/cc957d3f07c54d38882aedb1ab764406/outputs/review-explanatory-reach.md
raw-output-sha256: 7aaaab5db1f3a126560c435f645565af2314a4b04317f2f5d9fb595ce73c5b04
---

# Review

The central claim is that active work state differs from retrospective memory and chat history. The note gives a mechanism: each surface answers a different question, and each lacks something the others provide.

- Chat history is ordered by time, so a resuming session must reconstruct the live state from a trace.
- Retrospective memory stores lessons or episodes and lacks pointers, open gates, dependencies and a success state.
- A growing instruction file lacks any deletion trigger, so done work remains ambient.

Varying a premise changes the conclusion. If chat history were organised by liveness, or if retrospective memory carried closure criteria, the distinction would weaken. The note itself acknowledges the second case. The claim is falsifiable: a system that resumes multi-session work reliably from retrospective memory alone, with no control fields, would count against it.

The one qualifier that could look like an escape hatch, "unless it is extended", actually sharpens the mechanism: the needed fields and lifecycle are what matter. The mechanism is present and reasonably hard to vary.
