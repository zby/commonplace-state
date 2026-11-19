---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - current task pointers, unresolved gates, directional dependencies, and a success
    state
  reason: The list of active-work-state contents drifts across the note. The definition
    gives goal, next action, blockers, still-binding decisions, open evidence gates
    and closure criteria. This later list adds directional dependencies, which are
    absent from the definition, and drops decisions. The final paragraph's design
    list (project scope, resume pointer, explicit gates, lifecycle closure, extraction)
    is a third variant. The lists are compatible rather than contradictory, but a
    reader cannot tell which set is constitutive.
  level: info
- scope: passage
  quotes:
  - The stronger design is a workshop surface
  reason: The note says 'workshop surface' here and 'workshop layer' in the next paragraph.
    The context makes them read as the same thing, but the shift is a likely terminology
    drift that needs confirmation.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 3e7759255f65a11f9ff3153d71924ccc396c0fb06f9b102299619a6b04d223a6
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 8a85c650bd4b4d5d87aec905cd5158d082723035defc6f5e48a8490d50b93c1d
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/ae78de0946fe9c6f37a50239/inputs/target/kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/ae78de0946fe9c6f37a50239/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: cc957d3f07c54d38882aedb1ab764406
completed-at: '2026-11-16T11:26:46Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/cc957d3f07c54d38882aedb1ab764406/outputs/review-internal-consistency.md
raw-output-sha256: d8a18d0e6f08d022140c3fb6ada1bbc4f4d0327267e36f6b69aba5463c80c0a8
format: 2
---

# Review

The title, description and body agree. Active work state is memory in a broad sense but not retrospective memory or chat history, and it needs pointers, gates and closure. The opening concession ("memory in the broad sense") does not contradict the title, because the title qualifies the memory it excludes as retrospective. The handling of decisions is also consistent: still-binding decisions belong to active state, and durable notes receive extracted decisions after closure.

There is no contradiction. The only drift is in which component lists are constitutive and in a minor workshop surface/layer wording shift.
