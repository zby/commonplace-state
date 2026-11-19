---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/theory/agent-memory-requirements/create-memory-directly.md
note-sha256: e48ccb37e9005bc8f25752c9f35dd0108b6100452adafbee888967912399c0bc
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 46f7e46ad52a4cef93827df87f98030b
completed-at: '2026-11-16T11:25:30Z'
findings:
- scope: passage
  quotes:
  - Direct memory creation is the context-efficient path when understanding is already
    available during work.
  reason: 'The opening comparative claim is the note''s own derivation: writing while
    context is live avoids re-spending context on rediscovery. The next sentence gives
    that mechanism, and ''risks losing structure'' keeps the loss hedged, so the claim''s
    status is recoverable. The definite article (''the context-efficient path'') does
    read slightly stronger than a reasoned comparison with no cited measurement supports,
    but the claim remains qualitative and conditioned.'
  level: info
contract: verdict
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/abbd66cd888eb5ede047f7f6/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/abbd66cd888eb5ede047f7f6/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/46f7e46ad52a4cef93827df87f98030b/outputs/review-epistemic-status-blur.md
raw-output-sha256: 1b57fe155d66c1d370e9b4d28d13928f675533546820853f956f148f4f971628
---

# Review

## Summary

This is a requirement note. Its material claims are of three kinds:

- A derived comparative claim: direct creation is cheaper in context than later trace extraction when understanding is live. The note supplies its mechanism inline.
- Normative design requirements: the system "should help," and destinations "should expose their creation contract." The modal verbs mark these as requirements, not reports.
- Illustrative failure possibilities, worded with "can": a note can be hard to find, an instruction can steer wrongly, a check can fossilize a workaround.

The note does not present quantitative or empirical-sounding claims without evidence. The Methods list is offered as a set of destinations, not as an established decomposition. No support for one claim is spread to another, and no well-supported finding is over-hedged. A reader can recover each claim's status. The one INFO notes that the opening sentence's definite article reads slightly stronger than the reasoned comparison behind it.
