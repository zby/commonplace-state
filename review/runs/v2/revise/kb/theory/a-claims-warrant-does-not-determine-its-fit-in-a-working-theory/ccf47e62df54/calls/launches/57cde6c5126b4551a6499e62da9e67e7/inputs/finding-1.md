---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: dc5ffcc2c5169f8aa8505bb7dd6e5a7a862f912c40c8c63cae9c7b23350e4066
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: 83397e71fa79e7650e9da8e5e021ce5155fc7e5dc6bd22a80e77e2590f809e91
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews
launch: 521a98e92b6b49da9c89dc9e6f3db900
completed-at: '2026-11-16T11:28:22Z'
findings:
- scope: passage
  quotes:
  - It says neither evaluation determines the other.
  - Apparent fit does not imply warrant either.
  reason: 'Scope drift: the H1 asserts only one direction, that warrant does not determine
    fit. The body establishes a symmetric claim: neither evaluation determines the
    other, and neither may substitute for the other. The converse direction, that
    fit or coherence does not establish warrant, gets its own paragraph and the ''prohibition
    is substitution'' section, and the Scope section states the symmetric form as
    the note''s claim. A reader composing the title as a link would miss half of what
    the note establishes. A title such as ''Warrant and fit in a working theory are
    separate evaluations that neither determines nor substitutes for the other'' would
    match the body.'
  level: warn
contract: verdict
target-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/ed5c757b08dae0e3d3003c49/inputs/target/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/ed5c757b08dae0e3d3003c49/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/calls/launches/521a98e92b6b49da9c89dc9e6f3db900/outputs/review-title-body-alignment.md
raw-output-sha256: 64001ab908254b8f3b5cb309563983e5a99d2a65f4b95866c9af53ff99dda768
---

# Review

## Summary

The body supports the title's claim. Its second paragraph argues that a warranted claim can fit poorly. However, the body establishes more than the title promises. The note's central claim is two-way independence: warrant does not determine fit, and apparent fit does not establish warrant. It also develops two consequences. First, a contradiction between a warranted claim and the theory may indicate a defect elsewhere in the theory rather than in the new claim. Second, the two evaluations may exchange evidence but must not substitute for each other.

What the body now establishes: warrant and fit are distinct evaluations, neither determines the other, and they may inform but not replace each other. The title states only the first half of this, so it is narrower than the body.
