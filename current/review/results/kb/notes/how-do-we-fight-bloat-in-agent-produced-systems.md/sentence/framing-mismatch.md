---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 907f6982077b4bd5b8605cae1b34ca01
completed-at: '2026-11-25T05:26:41Z'
findings:
- scope: passage
  quotes:
  - every retained artifact, copy, or structure must be reconciled when neighboring
    code or claims change; [maintenance capacity must match harmful-artifact inflow]
  reason: The bullet frames drift load as a burden imposed by every retained artifact.
    The mechanism it cites concerns the risk-weighted inflow of harmful artifacts
    and treats gross volume as only a proxy. The sibling note on cheap adoption also
    distinguishes accumulation of locally sound structure from that harmful backlog.
    The framing emphasizes raw volume where the cited mechanism is defect inflow.
    It does not exclude any case, so this is info.
  level: info
- scope: passage
  quotes:
  - Local rewrites confirm that raw brevity is the wrong target
  reason: Both cited experiments targeted simpler or clearer prose, not brevity, and
    one of the 'two rewrites' passes made the text longer. The evidence shows that
    simplification trades against precision or length. 'Brevity is the wrong target'
    is a fair inference from it but frames the experiments around a goal they did
    not pursue. This is emphasis, not exclusion.
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/907f6982077b4bd5b8605cae1b34ca01/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/bd1323f28a9f6ff2ccbf19f9/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/907f6982077b4bd5b8605cae1b34ca01/outputs/review-framing-mismatch.md
raw-output-sha256: c8010aba4a9e6043e8f167c914b4abc2b916c7551c1a89d074777d5531346ab2
---

# Review

## Summary

The note's mechanistic sentences mostly frame their claims at the right level of generality:

- The three Stakes channels state their mechanisms directly.
- The "No reachability oracle" item states the gap in terms of reachability checks, which matches the code-side contrast it draws.
- The brevity-pressure item separates encoding distortion from content bloat, as its source does.

Two sentences frame their evidence slightly off the mechanism it carries: drift load is framed as raw volume, and the rewrite experiments as brevity targets. Neither framing excludes cases the mechanism covers, so both findings are info and the gate passes.
