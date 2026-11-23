---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Mocking the tool boundary makes instruction behavior testable in isolation
  reason: 'The title asserts the ordinary purpose of mocking: replacing a dependency
    makes behavior at that boundary testable in isolation. A reader can grant that
    point without accepting any claim about which instruction failures the test can
    detect. The note supports a sharper claim about how capturing attempted tool effects
    exposes protocol violations that a plausible final artifact can hide.'
  level: fail
outcome: fail
description: Retained verdict review of kb/theory/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: 8e5fdc819149feb18cf107a951be050036004387bbde161b572f527218d58a85
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
target-sha256: f8da1c4b0bbc1eaba9a5dceda67136e75dbf1d0c876d675e9f4e0e7b00d051d3
target-capture: kb/reports/state/review/runs/v2/20261120T133828Z/calls/launches/b618811245c8453db684eb099e9649ad/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T133828Z/artifact/reviews/0503681daf977bacc7f2bdcc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/20261120T133828Z
launch: b618811245c8453db684eb099e9649ad
completed-at: '2026-11-20T13:39:26Z'
raw-output: kb/reports/state/review/runs/v2/20261120T133828Z/calls/launches/b618811245c8453db684eb099e9649ad/outputs/review.md
raw-output-sha256: b9a2a20972743bee55721b0d9edb4a059c3560744a763eb7ad30490b1ba4a1b4
format: 2
---

# Review

The source-note example shows what a trace adds to an instruction test. A report can satisfy its output requirements while the agent attempts a forbidden edit. Capturing that attempt supplies evidence about compliance, provided the test observes every available route for modifying the source.
