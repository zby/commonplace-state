---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 8db905baf3094b5185b9d357cb80ec16
completed-at: '2026-11-25T05:26:39Z'
findings:
- scope: passage
  quotes:
  - compete for bounded agent attention and raise lookup cost
  reason: The context-and-routing channel is stated in terms of agent attention. Bloat
    that costs a human maintainer or operator reading time (reviewing a diff, auditing
    a note) maps here only by stretching 'lookup cost'; it maps more naturally to
    maintenance load, but that channel is framed as reconciliation after change, not
    ordinary reading. Coverage is possible but strained.
  level: info
- scope: passage
  quotes:
  - Bloat in these mixed systems compounds through three channels
  reason: 'Boundary case between channels: execution cost of bloated code and tests
    (slower suites, longer CI, more tool calls per task) is neither attention/routing
    cost, reconciliation after change, nor recursive model exposure. It can be forced
    into ''maintenance load'' only loosely. The three-channel list reads as covering
    how bloat compounds, so this case strains it, though the note''s argumentative
    weight is on the prose-side channels where it is less relevant.'
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/39c50a3d4c2b819a5b309676/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 3fc1fc44c2a3ab8d35bb572149dbb91d557c216f7645b3da3c349e543c785a4c
---

# Review

## Summary

The note has three enumerations: the three channels through which bloat compounds (Stakes), the five mechanisms in the Current answer, and the Unsettled list. The five mechanisms are explicitly "partial" and scoped to "prose, structure, and the code–prose boundary", so they do not claim to cover the space. The Unsettled list is an open-problems list. Neither makes a closed coverage claim that a boundary case could break.

The three-channel list is the only enumeration that reads as covering a space: how bloat imposes compounding cost. Tested cases:

- **Simplest instance** — one redundant paragraph in a note: maps to context/routing cost and recursive exposure. Clean.
- **Extreme instance** — a large overlapping taxonomy with many dependants: maps to maintenance and drift load. Clean.
- **Between channels** — slower test suites and CI from bloated code and tests: not clearly in any channel (INFO).
- **Adjacent concept** — human reviewer reading cost: strained fit, since channel one names agent attention (INFO).
- **Adjacent concept** — storage cost: negligible in this setting and plausibly outside the note's concern; not flagged.

No case clearly falls outside the claimed coverage in a way that breaks the note's argument, and the list is already short relative to its role in the Stakes section; scope clarification (e.g. "for agent-operated KBs, the main channels are…") would suffice rather than adding a fourth channel.
