---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 304ff2b910374d728798b623f2a4a074
completed-at: '2026-11-18T16:02:23Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/a66f53da3bbca36c551f8b6e/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/a66f53da3bbca36c551f8b6e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/304ff2b910374d728798b623f2a4a074/outputs/review-anthropomorphic-framing.md
raw-output-sha256: 6225b903c67b340246012f6a79b3ba2234f79f662721773346296253779541be
---

# Review

## Summary

The note's statements about models stay technical. "A model may need several reads to check a source that exceeds its context budget" and "text that happens to sit in a model's context" describe retrieval and context limits. They make no claim about what the model knows or understands. "The checker must retrieve that context before judging support" assigns a function to a checking role, and "judging support" names the task, not a mental state. Where the note uses "intended" ("that the author intended this occurrence"), it refers to the human author of a citation, not a model. "Context needs a reader of both texts" names a role that a human or a model could fill. It makes no claim about cognition. No passage meets the failure mode.
