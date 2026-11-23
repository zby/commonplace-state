---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/c4395d1fa0b126956835c101/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 3eb26f9df34f411faf101251b0454a5c
completed-at: '2026-11-20T09:42:06Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/3eb26f9df34f411faf101251b0454a5c/outputs/review-jargon-persistence.md
raw-output-sha256: b9a985677f2583f63a5122a7af44d990060e54f1c672f866d0f625091069925d
format: 2
---

# Review

## Summary

No KB-internal term is reused often enough after its definition point to lose its grounding.

The candidate terms are "hybrid VM", "constraining", "codification" and "relaxing". "Hybrid VM" appears three times in the body. Its first use explains it as the place where agents and tools share one namespace. Its second use, "On top of the hybrid VM", opens a section that is clearly about llm-do's runtime. Its third use, in an open question, names the same runtime. A reader can follow each use without scrolling back.

"Constraining" and "codification" are glossed together where they are linked. After that, their few later uses are tied to concrete actions: "Codify — extract `sanitize_filename()` to Python". "Relaxing" occurs once in the body, next to a concrete gloss: "Add an LLM call for the new cases". "Neural" and "symbolic" recur often, but every use contrasts LLM-backed agents with Python code, and the diagram labels them that way. The gate therefore does not apply.
