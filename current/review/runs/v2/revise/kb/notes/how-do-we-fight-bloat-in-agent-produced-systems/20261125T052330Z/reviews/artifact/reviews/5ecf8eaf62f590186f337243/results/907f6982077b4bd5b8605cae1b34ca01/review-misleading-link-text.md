---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '[two rewrites exposed a syntax-or-repetition tradeoff](../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md)
    and [three simplification passes'
  reason: In context, the reader expects both linked notes to show that 'naive shortening
    dropped technical relations while clearer rewrites sometimes added words'. The
    'two rewrites' target shows a different thing. Its unguarded pass was sentence
    splitting, which lost relations and also lengthened the note by 3.7 percent. Its
    guarded pass added 4.9 percent. That supports 'clearer rewrites added words' but
    not 'naive shortening dropped relations'. Only the 'three simplification passes'
    target supports the shortening half. The sentence should separate what each link
    supports.
  level: warn
- scope: passage
  quotes:
  - '[maintenance capacity must match harmful-artifact inflow](../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md).'
  reason: The link appears in a sentence that says every retained artifact, copy,
    or structure must be reconciled. The target's opening says that gross volume is
    only a proxy and that the load is the risk-weighted inflow of harmful artifacts.
    The link text is accurate, but the sentence implies the target supports an all-artifacts
    burden. The footer gloss ('turns bloat into a queue-stability problem') has the
    same tilt.
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/907f6982077b4bd5b8605cae1b34ca01/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/5ecf8eaf62f590186f337243/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 907f6982077b4bd5b8605cae1b34ca01
completed-at: '2026-11-25T05:26:41Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/907f6982077b4bd5b8605cae1b34ca01/outputs/review-misleading-link-text.md
raw-output-sha256: 30beb7995b918d1eaf6b6ce463f296b436bcf621129fdf1128721a6d51aecfed
format: 2
---

# Review

## Summary

I checked each distinct link target against its title and opening, and against its interior where the head did not settle the question. All targets resolve. The following links match what their sentences lead the reader to expect:

- Fix what the executor can't determine
- Seven documentation cases: the six-page 53 percent figure and the two retirements are both in the casebook
- Reverse compression: it has a section on code generation
- Cheap adoption and weak retirement
- Current-task fit
- Scaling absorbs scaffolding
- How do we value notes?
- Choosing what to learn
- The AI-generated-language ingest: both quotations are present verbatim

One link pairing makes a reader expect evidence that one target does not provide. The "two rewrites" target shows a syntax-or-repetition tradeoff under simplification, not naive shortening losing relations. One further link is accurate but sits in a sentence that broadens its scope. The gate warns on the first.
