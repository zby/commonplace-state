---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/types/note.md
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/reviews
launch: 2c8dea3161c3408bb21b55cab48faabc
completed-at: '2026-11-18T19:03:08Z'
findings:
- scope: document
  quotes: []
  reason: The template ends with a `Relevant Notes:` footer, which the note omits.
    The writing-shape instruction only asks for links where they help traversal, and
    the note meets it with two inline links that state their relationships. The footer's
    absence is therefore a template deviation, not an unmet instruction.
  level: info
contract: verdict
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/reviews/artifact/reviews/ec50fb917e02bb1f9ccf4461/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/reviews/artifact/reviews/ec50fb917e02bb1f9ccf4461/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/reviews/calls/launches/2c8dea3161c3408bb21b55cab48faabc/outputs/review.md
raw-output-sha256: 42432c3c663dc3842effb8ef266cabc8f2e51874b568b554f4b29ca733b2e463
---

# Review

## Summary

The note does what the `note` type spec's authoring instructions ask.

- **Main claim near the top.** The first paragraph states the claim: removing an approval wait differs from removing a specified evaluation task. The second paragraph defines the mechanism, a blocking dependency versus an unfulfilled requirement.
- **Transferable rationale, not procedure.** The note explains a distinction and what an automation claim must say. It does not prescribe an operational procedure, so it keeps design rationale in a note rather than an instruction.
- **Links to adjacent notes.** Two inline links state their relationships. The note complements the operative-state comparison note, and it cites the routine-approvals note for why repeated acceptance does not settle whether a check can be dropped.
- **Limits under `## Scope`.** The Scope section gives two applicability limits. The distinction covers required intervention, not every human influence, and a habitual unwritten wait is a wait to remove, not evidence of a requirement. The body also bounds its weekly-review example: it "establishes a gap against the specification, not that skipping review causes harm."
- **Description.** The description is one sentence. It separates the note from neighbouring automation and approval notes by naming its specific contrast.
- **Traits.** `has-comparison` fits: the note sets the required-approval case against the optional-assessment case, and it lists alternative fates for a check.

The note omits the template's optional `## Open Questions` section, which is allowed when no open questions exist. The missing `Relevant Notes` footer is recorded as an informational finding only.
