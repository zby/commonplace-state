---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 4d542c7baa45c2fc7feed113b12b2a2983d5a77121478b8b3871e69c02e035d3
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 8db905baf3094b5185b9d357cb80ec16
completed-at: '2026-11-25T05:26:40Z'
findings:
- scope: passage
  quotes:
  - Empirically, agents default to additive changes
  reason: The word 'Empirically' presents the additive-default claim as an established
    observation, but the note presents and cites no evidence for it (no log entry,
    study or case). The surrounding text correctly marks the mechanism as unknown,
    yet the observation it is meant to explain carries an empirical label without
    support on the page, so a reader cannot tell whether it is a measured finding
    or a working impression.
  level: warn
- scope: passage
  quotes:
  - Local rewrites confirm that raw brevity is the wrong target
  reason: '''Confirm'' gives the general claim the confidence of an established result,
    while the support is two single-article rewrite experiments that their own notes
    describe as bounded evidence (''not a general ranking''). Evidence about how particular
    instructions behaved on one note or article is presented as establishing the broader
    targeting principle.'
  level: warn
- scope: passage
  quotes:
  - in agent-operated systems, retained prose and code become future model input,
    so verbose or obsolete material anchors later generations
  reason: The recursive-exposure channel states a proposed mechanism (retained material
    anchors later generations) in the same declarative register as the observation
    that retained material becomes model input. The note gives no support for the
    anchoring effect; the KB's own linked maintenance-capacity note treats the anchoring
    reports as unverified anecdotes that do not establish later defects. The mechanism
    therefore inherits the confidence of the uncontroversial premise.
  level: warn
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/df3c6179cef61ed99826b031/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8db905baf3094b5185b9d357cb80ec16/outputs/review-epistemic-status-blur.md
raw-output-sha256: e68ed33d621bd0e59d7d8e50de6d4f924e78962598c359f36478af9529dec8c9
---

# Review

## Summary

The note handles status well in several places. Its Current answer calls the mechanisms "partial"; the Unsettled section is explicitly a list of open problems; and the brevity-pressure bullet is carefully calibrated. It names the study as producer-side, states that human reading cost was inferred rather than measured, and labels the log entry an "unconfirmed conjecture". The documentation sweep is described as "bounded".

Three load-bearing claims do not get the same treatment:

- The additive-default claim is labelled "Empirically" without any presented evidence. Its placement in Unsettled covers the mechanism question, not the observation.
- "Local rewrites confirm" spreads single-case rewrite evidence onto a general principle about targeting.
- The recursive-exposure channel asserts an anchoring mechanism as fact in a Stakes list whose other channels are plausible derivations. Its premise (retained material becomes model input) is safe; the anchoring consequence is a hypothesis.

The three-channel decomposition itself is a light qualitative construction and is not flagged on that ground alone.
