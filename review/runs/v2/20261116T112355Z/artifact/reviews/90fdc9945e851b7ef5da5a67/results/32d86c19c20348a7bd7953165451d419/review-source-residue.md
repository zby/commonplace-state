---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'The stronger design is a workshop surface: a compact current pointer plus a richer
    active ledger, both scoped to the project and removed from startup context when
    the work closes.'
  reason: The two-artifact shape (a compact pointer plus a richer ledger, scoped to
    the project and loaded at startup) closely matches the Workstream Kit's ACTIVE.md/workstream.md
    design. The note states it as the general stronger design before naming the kit.
    The following sentence presents the kit as an implementation, which partly marks
    the shape as a case. Still, the general claim needs only the required control
    fields (a current pointer, gates, closure and removal from ambient context), not
    this specific two-file arrangement. Phrasing the design by its required properties,
    or marking the pointer-plus-ledger split as the kit's realization, would avoid
    committing the note to one system's layout.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 3e7759255f65a11f9ff3153d71924ccc396c0fb06f9b102299619a6b04d223a6
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 8a85c650bd4b4d5d87aec905cd5158d082723035defc6f5e48a8490d50b93c1d
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/90fdc9945e851b7ef5da5a67/inputs/target/kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/90fdc9945e851b7ef5da5a67/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 32d86c19c20348a7bd7953165451d419
completed-at: '2026-11-16T11:24:59Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/32d86c19c20348a7bd7953165451d419/outputs/review-source-residue.md
raw-output-sha256: 4cebf5e8aeb1f94d5eda958052f7ba288bcd67ee47bb5b90e35c2314f85b21e8
format: 2
---

# Review

The title and opening paragraph claim a general distinction about the retained state of unfinished work. The note is abstracted from the Claude Workstream Kit ingest and grounded in a code review of that kit.

Most source-specific detail is marked explicitly as a case. `ACTIVE.md`, `workstream.md`, user approval and archive/tag/removal all appear inside the sentence that names the kit, and the kit's limits are stated as its limits. The "growing project instruction file" in the third paragraph probably comes from the source context, but project instruction files are a general surface in agent systems, so it does not overcommit the note.

The only residue is the shape of the recommended design, recorded above as INFO. The note generalizes the kit's pointer-plus-ledger layout slightly ahead of its evidence. Because the next sentence ties the layout to the kit, this does not reach WARN.
