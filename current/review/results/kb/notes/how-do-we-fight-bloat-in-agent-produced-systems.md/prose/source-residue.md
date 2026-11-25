---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: b539edf22531462f8318ad9760d1c0ff
completed-at: '2026-11-25T05:24:49Z'
findings: []
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/9f1d6ce0034e8de90954c2e3/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/b539edf22531462f8318ad9760d1c0ff/outputs/review-source-residue.md
raw-output-sha256: 8648108a887eda7405aba83a278ff1c77d3468f9954e5ee533b7a96e64f6d4ca
---

# Review

## Summary

The title and Stakes claim generality over agent-produced mixed code and natural-language systems. Commonplace-specific material is explicitly framed as a case. The Stakes section says "Systems like Commonplace", the Current answer says "Commonplace currently counters bloat", and the documentation result is labelled "a bounded sweep". The external study is introduced as "One producer-side study". Software-engineering vocabulary such as dead-code elimination, YAGNI and unused-symbol checks is used deliberately as the contrast domain, not as leaked framing. No unframed narrower-domain residue was found.
