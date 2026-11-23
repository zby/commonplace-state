---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2507e629a34445439219d3dc27929d21/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/0d979eb5645ea980622ea8c9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 2507e629a34445439219d3dc27929d21
completed-at: '2026-11-20T11:10:04Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/2507e629a34445439219d3dc27929d21/outputs/review-jargon-persistence.md
raw-output-sha256: 956c0323925cd3dc4b755668c9a0ce6906e42f625a102c06986a90048c08321e
format: 2
---

# Review

## Summary

No KB-internal term is defined once and then reused often enough to lose its grounding.

The candidate KB-specific terms are codification, relaxing, constraining, spec mining and "the English account of prompting". After its linked introduction, codification recurs once, in the bolded label "codification as refactoring", and that bullet explains the move in plain words ("replacing the prompt with a Python function"). Relaxing is glossed inline as "regaining generality" at its single body use. Constraining and spec mining each appear once in the body. "The English account" appears once and is paraphrased on the spot. The note's recurring vocabulary is binding, prompt-backed agent, caller and execution regime. These terms are either plain language or explained locally, and the running `ticket_classifier` example keeps them concrete.
