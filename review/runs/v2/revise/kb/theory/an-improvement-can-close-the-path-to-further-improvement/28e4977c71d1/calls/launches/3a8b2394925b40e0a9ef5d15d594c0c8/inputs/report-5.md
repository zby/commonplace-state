---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/role
launch: c42df8939f3c4f9f9a734893ce709b2b
completed-at: '2026-11-17T07:26:18Z'
findings:
- scope: passage
  quotes:
  - A system can improve at its current work while losing the ability to improve itself
    again.
  reason: 'SUPPLIED — kb/theory/README.md — needs only a citation: an index entry
    that labels the note a supplement to the better-factory comparison that explains
    why a current gain can remove future revision capability. The note''s supplement
    line and opening paragraph match that label.'
contract: report
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/role/artifact/reviews/a9a57b10e0be4006131b1c54/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/role/artifact/reviews/a9a57b10e0be4006131b1c54/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/role/calls/launches/c42df8939f3c4f9f9a734893ce709b2b/outputs/review.md
raw-output-sha256: 780b62336e6c2afb1b5b490cbae6d394c0e8f4d08b35bdceee0dbd8eabe86ae5
---

# Role in the KB: An improvement can close the path to further improvement

## Role
The note supplements the better-factory comparison. It explains why a gain in current production can remove the capability to revise the system again, and when non-regression would prevent that. In the supplied inbound contexts, only the theory collection index (`kb/theory/README.md`) links to it. That link is a navigation citation, and no dependent argues from the note or uses its terms.
Relied on: only the note's headline claim, for the index label: a current gain can remove future revision capability, framed as a supplement to the better-factory comparison. Unused: the hypothetical agent example; the claim that non-regression protects only capabilities in its checked scope; the claim that a replacement workflow can preserve the capability while editable files alone do not; the distinction between remaining able to improve and actually improving again; the scope limits (deliberate fixed deployments, boundary-relative loss, alternative paths).

## Dependents
- `kb/theory/README.md`: needs a citation that matches its index label, "supplement to the better-factory comparison: explains why a current gain can remove future revision capability".

## Duplication
None. The index entry is a one-line label. It does not restate the note's argument.

## Untaken recommendations
None. No linking source recommends a change to the note.

## Reach
A change to the note's headline claim or to its framing as a supplement to the better-factory comparison would reach `kb/theory/README.md`, whose entry paraphrases both. A change to any other claim or term reaches no dependent, because none argues from the note. The note links outward to the better-factory comparison (`kb/theory/a-better-factory-claim-compares-operative-states.md`), the repeatable-operative-path note and the compounding note. Those outbound links make it depend on them; they do not make those notes dependents of this one.
