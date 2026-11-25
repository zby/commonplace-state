---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Systems like Commonplace combine **natural language and code**, which adds prose,
    conventions, links, and routing surfaces that lack static reachability checks.
  reason: The note's distinctive claim (software anti-bloat defenses do not carry
    over to mixed natural-language and code systems, because prose, conventions and
    routes have no static reachability check) is the third sentence of the Stakes
    paragraph, after two sentences of general setup. The same idea comes back only
    as the first Unsettled bullet ('No reachability oracle for natural language').
    The claim can be found, but the two halves are far apart. Lead Stakes with this
    sentence, or fold the Unsettled bullet's framing into it, so the reader keeps
    the 'why software defenses fall short' point.
  level: info
- scope: passage
  quotes:
  - One producer-side study reports that
  reason: The brevity-pressure bullet is much longer than its sibling Unsettled bullets.
    It carries two verbatim quotes, a repeated source citation, an evidence caveat
    and a log conjecture. Its open question ('how to apply selection pressure cleanly
    without triggering that encoding distortion') comes only at the end. The bullet
    stays on topic, but this apparatus makes it read as the note's centre of gravity.
    Lead with the open question, keep one quote and leave the rest to the linked ingest.
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/19853361272c4faa83f3bfe9830686cc/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/63b2c5b2e96353489415550d/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 19853361272c4faa83f3bfe9830686cc
completed-at: '2026-11-25T05:26:15Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/19853361272c4faa83f3bfe9830686cc/outputs/review.md
raw-output-sha256: a6686d7d51a5e28d3df63182cf6cef3ad4363ec3b30dbb9710967402dbd150a6
format: 2
---

# Review

## Summary

The note's strongest claim, stated using only its own commitments, is this: bloat in agent-produced mixed natural-language and code systems compounds through context, maintenance and recursive-exposure costs. Software anti-bloat defenses do not cover it, because prose and conventions lack reachability checks. Commonplace counters it today with five partial mechanisms, and retirement triggers, cross-boundary detection and the additive bias of agents remain unsolved.

The standing-query structure (Stakes, Current answer, Unsettled) makes this claim easy to find. The Current answer section opens with a one-line count and scope, "five partial mechanisms across prose, structure, and the code–prose boundary". Each bullet leads with a bold imperative before its supporting links. Later material clearly serves the question. Nothing hides what the note is for, so the outcome is PASS.

Two shape issues make the claim less memorable than it could be. Both are recorded as info findings above.

- The "falls short of software advice" thesis sits mid-paragraph in Stakes. Its partner point, no reachability oracle for natural language, appears only in Unsettled.
- The brevity-pressure bullet holds most of the note's quoted evidence. It outweighs the other open questions, and its question comes last.

Neither problem needs restructuring. Moving one sentence and trimming one bullet would fix both.
