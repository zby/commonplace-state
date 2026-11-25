---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/types/note.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 306a988f55e741dc9141f8d344223c1e
completed-at: '2026-11-25T05:25:19Z'
findings:
- scope: document
  quotes: []
  reason: The note has no `## Scope` section. The type spec permits omitting it when
    no limit is known, and the note's applicability conditions (mixed natural-language
    and code systems, Commonplace's current mechanisms) and its retirement condition
    are stated in `## Stakes`, so this is acceptable. A short Scope section could
    still make the boundary against pure-software bloat easier to rescope without
    editing the Stakes.
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/306a988f55e741dc9141f8d344223c1e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/3e0545ea80513bfb3470e5ae/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/306a988f55e741dc9141f8d344223c1e/outputs/review.md
raw-output-sha256: 1557c6f532e916ac55e292c534f91894f0388eb9741905f0719607b363265124
---

# Review

## Summary

The note does what the `note` type spec's authoring instructions ask. The type spec has no `## Review` section, so the Writing Shape bullets and the template are the operative test.

- **Title as compressed handle.** The question title names the note's subject exactly: bloat control in agent-produced systems. Whether a question title satisfies the proposition and claim conventions is left to the catalog title gates, as the invocation directs. The note declares no `title-as-claim` trait.
- **Main claim or mechanism near the top.** `## Stakes` opens with the problem and the three compounding channels. `## Current answer` follows immediately with the five mechanisms Commonplace uses. For a standing-query note, this puts the substantive answer near the top.
- **Links to adjacent notes.** Every mechanism and every open problem that rests on another artifact links to it inline. The footer gives each link a relationship gloss (`see-also`, `evidenced-by`) that helps traversal.
- **Rationale versus procedure.** The note contains design rationale and open problems, not imperative procedure. It does not attempt to be an instruction.
- **Scope and open questions.** The template's Open Questions role is filled by `## Unsettled`; the template does not require an exact heading name. There is no `## Scope` heading. The spec allows that when no limit is known, and the note puts its applicability and retirement conditions in Stakes (see the info finding).
