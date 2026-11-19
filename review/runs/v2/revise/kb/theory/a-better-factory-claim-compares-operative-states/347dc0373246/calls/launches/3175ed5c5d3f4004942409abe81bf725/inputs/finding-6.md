---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/prose/mannered-prose.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion: kb/instructions/review-gates/prose/mannered-prose.md
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 8894cc518e7e46b89dba40dc6bb4ed6b
completed-at: '2026-11-16T21:57:48Z'
findings:
- scope: passage
  quotes:
  - Getting any of them from the record after the fact is where the claim goes soft.
  reason: 'Literal meaning: if any declaration is read off the record after the fact,
    the claim stops being determinate and stops being able to fail. Replacement: ''Reading
    any of them off the record after the fact leaves the claim indeterminate and unable
    to fail.'' ''Goes soft'' does not say which property is lost, so the reader has
    to translate the image. The note later names the precise defect (close to unfalsifiable;
    the comparison stops being capable of failing), and the literal wording would
    state that here, in the sentence that frames the four declarations.'
  level: warn
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/4b1a00d020bee82833120b41/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/4b1a00d020bee82833120b41/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/8894cc518e7e46b89dba40dc6bb4ed6b/outputs/review-mannered-prose.md
raw-output-sha256: aa577298aacf7f61304f4908386e0d6bdf4710e26b52dfae0a0b2bd83603cd32
---

# Review

The note is mostly literal. One figurative phrase in the framing paragraph meets the test.

Other candidates were checked and kept. "Falls out of scope indexing" is conventional shorthand for "follows from", and the section shows the derivation. "Bolted onto" sharpens the contrast between an added requirement and a consequence of an existing one. "Consumes the capacity for further improvement" and "closing the route" use "route" and "path" in the sense the note defines: the factory-development path. "A passing successor is cheap" means easy to obtain at that boundary, and the following clause explains why. "That is all antecedence buys" scopes the claim precisely. "Who was in the room" is a conventional idiom; the sentence contrasts it directly with the gating role. "Re-enters at the headline result rather than at a labelled input" is a compact contrast between two positions in the evidence chain, and the note uses that contrast.
