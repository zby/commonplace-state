---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: b539edf22531462f8318ad9760d1c0ff
completed-at: '2026-11-25T05:24:49Z'
findings:
- scope: passage
  quotes:
  - Empirically, agents default to additive changes — adding a helper, guard, section,
    or new note — rather than deleting or consolidating existing structure.
  reason: The sentence presents the additive bias as an empirical finding but cites
    no study, log entry or evidence note and gives no observation scope (which agents,
    which tasks, how observed). A reader cannot judge whether this is measured behaviour
    or operator impression. Either link the observations that support it or mark it
    as an operator observation with its scope.
  level: warn
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/396d9160be28312339c8d4a2/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/outputs/review-orphan-references.md
raw-output-sha256: f3372440d1e627fb54772a80711be7ed077d0172b218fba529d19197e139a8d0
---

# Review

## Summary

Most specific figures and empirical claims are sourced. The 53 percent reduction and two retirements link to the seven-documentation-cases evidence note, which records the byte counts for the six measured cases. The two quoted findings on AI-generated language link to their ingest, and the note states that human reading cost was inferred rather than measured. The `kb/log.md` conjecture is labelled unconfirmed.

The one orphan is the "Empirically" claim about the additive bias. It is the premise of the final Unsettled item, which asks why the bias exists, yet the note gives no source or scope for it.
