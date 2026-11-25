---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 97ca715986f94b258b5f76d768f736d5
completed-at: '2026-11-25T05:24:32Z'
findings:
- scope: passage
  quotes:
  - checked routing catalogues
  reason: '"Routing" is the one KB-flavoured term that recurs throughout the body
    (routing surfaces, routing cost, unknown-name routing, routing and migration debt,
    route obsolete prose, routing catalogues). It is never formally defined, so there
    is no definition point for it to drift from. Most later uses keep enough local
    context (lookup cost, migration debt, retirement review) to be read alone. This
    late use leans hardest on the reader remembering what a route is in a KB. Consider
    a short plain gloss such as "catalogues that point agents to the right file".'
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/97ca715986f94b258b5f76d768f736d5/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/d7d530e8911ce045561540e2/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/97ca715986f94b258b5f76d768f736d5/outputs/review-jargon-persistence.md
raw-output-sha256: 621f445ca23ba54e5a72af2b018f50ec1a6d872c0e3b316d9c211b78dee3d167
---

# Review

The note introduces several KB-internal phrases: zero-structure expansion, selection bloat, value gate, reachability oracle, fixed-difficulty scaffolding and encoding distortion. Each appears once or twice, usually in the bullet that grounds it. None is reused more than twice after it is introduced, so this gate's failure mode does not occur.

The only term that recurs is "routing". Its uses are spread across sections but mostly come with local cues that keep them readable. The single INFO finding marks the use where a plain-language gloss would help most. It does not block the note.
