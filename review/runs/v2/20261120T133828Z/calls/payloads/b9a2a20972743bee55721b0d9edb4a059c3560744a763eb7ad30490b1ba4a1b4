---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Mocking the tool boundary makes instruction behavior testable in isolation"
    reason: "The title asserts the ordinary purpose of mocking: replacing a dependency makes behavior at that boundary testable in isolation. A reader can grant that point without accepting any claim about which instruction failures the test can detect. The note supports a sharper claim about how capturing attempted tool effects exposes protocol violations that a plausible final artifact can hide."
    level: fail
outcome: fail
---

# Review

The source-note example shows what a trace adds to an instruction test. A report can satisfy its output requirements while the agent attempts a forbidden edit. Capturing that attempt supplies evidence about compliance, provided the test observes every available route for modifying the source.
