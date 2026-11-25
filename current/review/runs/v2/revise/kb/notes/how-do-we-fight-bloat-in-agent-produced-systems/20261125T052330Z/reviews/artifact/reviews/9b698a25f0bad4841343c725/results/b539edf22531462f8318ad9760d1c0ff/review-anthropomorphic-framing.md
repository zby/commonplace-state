---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - local risk aversion around unknown dependents
  reason: '''Risk aversion'' attributes a preference-like disposition to agents. The
    note offers it only as one candidate mechanism for the additive bias, alongside
    training incentives and narrow context, and explicitly says the mechanism is not
    understood, so it does not assert agent internals. A behavioural phrasing (for
    example, ''avoiding edits whose dependents are not visible in context'') would
    remove the residual implication.'
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/9b698a25f0bad4841343c725/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: b539edf22531462f8318ad9760d1c0ff
completed-at: '2026-11-25T05:24:49Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/outputs/review-anthropomorphic-framing.md
raw-output-sha256: c6f60d08dcda4daa39a73787a40a046af7296e8e298a70549db25e23bdfe3b14
format: 2
---

# Review

## Summary

The note mostly describes models and agents in behavioural or technical terms: agents "default to additive changes", a model "can keep all the content while squeezing the wording", retained material "becomes future model input". "Bounded agent attention" uses attention in its context-budget sense, and "what the executor can't determine" is the title of a linked note about specification, not a cognition claim.

The only candidate is "local risk aversion", which appears inside an explicitly hedged list of possible causes. It does not commit the note to a claim about model cognition, so it is recorded as INFO.
