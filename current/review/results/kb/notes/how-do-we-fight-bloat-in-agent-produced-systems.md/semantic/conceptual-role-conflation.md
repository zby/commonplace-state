---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: warn
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
  - Commonplace currently counters bloat with five partial mechanisms across prose,
    structure, and the code–prose boundary
  reason: 'The sentence presents the five items as mechanisms Commonplace applies
    (object of application: the running system), but each bullet is carried by a linked
    theory note''s account (source account), and the bullet verbs attribute the countering
    to the notes themselves (''trims'', ''targets'', ''diagnoses'', ''distinguishes'').
    Two readings fit: (a) Commonplace has operative practices, gates or procedures
    that implement each principle; (b) Commonplace''s KB contains accounts that would
    counter bloat if applied. The fifth bullet leans toward (b): it says that ''without
    a value gate, valid redundant artifacts still accumulate'', describing a needed
    gate rather than one in operation. The choice changes what the note claims the
    system already contributes and therefore how the query''s retirement condition
    (''relies on periodic manual sweeps and ad-hoc restraint'') is assessed. The author
    must decide, per bullet, whether it reports an applied mechanism or a theory the
    system holds.'
  level: warn
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/231564e2a67a5fb4ec3a4b7f/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 88e88dcef17487a21f1aa9c28643c0706366965130587890c65b834f7230000b
---

# Review

## Summary

Most passages keep their roles clear: links are introduced by their titles, and the Unsettled section distinguishes what is known from what is not. The one material blur is in the Current answer's framing.

The section heading and lead sentence frame the list as how "Commonplace currently counters bloat", i.e. applied mechanisms in the system. The bullets, however, are mostly summaries of theory notes, and their subjects are the notes ("Reverse compression … targets selection bloat"; "Cheap adoption and weak retirement … diagnoses structural bloat"). Only the first bullet's evidence clause (the documentation sweep) and arguably the reference-collection consequence report something Commonplace did. The value-gate bullet explicitly describes the absence of a value gate as the problem.

A reader therefore cannot tell whether the note claims Commonplace operates five anti-bloat mechanisms or holds five relevant accounts. That matters for a standing query, whose Current answer is meant to say what the system presently does and whose retirement condition depends on whether bloat control is still manual. No other passage clears the materiality threshold.
