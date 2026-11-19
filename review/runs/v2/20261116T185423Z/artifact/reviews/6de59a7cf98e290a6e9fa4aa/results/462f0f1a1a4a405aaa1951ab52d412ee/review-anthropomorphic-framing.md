---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A system can reward its own misconceptions.
  reason: '"Misconceptions" attributes beliefs to the system. The next sentence gives
    the literal mechanism (earlier design choices and neighbouring artifacts encode
    the same error), and the system here is the human-inclusive system under construction
    rather than a model, so this reads as conventional metonymy. A literal form would
    be "A system can reward mistaken claims it already encodes."'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/6de59a7cf98e290a6e9fa4aa/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/6de59a7cf98e290a6e9fa4aa/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 462f0f1a1a4a405aaa1951ab52d412ee
completed-at: '2026-11-16T18:55:34Z'
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/462f0f1a1a4a405aaa1951ab52d412ee/outputs/review-anthropomorphic-framing.md
raw-output-sha256: a1eb9c20edbed6c147e76963c0fc32c00ef5bc0f1c48145c9c8ede9c0c206648
format: 2
---

# Review

The note is about selecting theory claims through use of a system under construction, not about model cognition. Its mental-state vocabulary is mostly conventional shorthand for software or agent systems: "helps the system reason, modify, or recover" and "where an agent searches for a defect" describe system behaviour without claims about internals. The one mental-state noun, "misconceptions," is explained immediately by encoded design choices and artifacts. No phrase implies an internals or agency claim the note would need to defend.
