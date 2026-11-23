---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/complexity/could-be-a-paragraph.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 808b4e1d3db21875b29916fcc9631eb0dc71dd954e9115c08c137becc6f1ff96
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/f71702d2f52d392eb0525874/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 33bc96d018eb47759199e2647dea7376
completed-at: '2026-11-20T11:09:32Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/outputs/review-could-be-a-paragraph.md
raw-output-sha256: e5e3ea3fdbe43df3b4957fcae6efebd4c9b6f27f1f366f5b3145e665fd5732e3
format: 2
---

# Review

## Summary

A one-paragraph version would keep the headline, that one interface lets programmers swap prompts and code without editing callers. It would lose most of the load-bearing content:

- **The asymmetric leak.** Each swap direction breaks a different caller assumption, through a different mechanism. Prompt-to-code breaks LLM callers that relied on the prompt tolerating loose arguments. Code-to-prompt breaks code callers' latency, cost and determinism assumptions, for example in loops or with exception handling. This is the note's main non-obvious claim, and it needs both mechanisms spelled out.
- **The derived prescriptions.** Enforce schemas before codification, and write movable call sites for fallible, higher-latency calls. These follow from the leak analysis.
- **Boundary conditions.** Call invariance is not behavioral invariance, structural signature changes still need adapters, and swapping back requires call-site headroom.
- **The three-move distinction.** Refactoring, prototyping and relaxing are separated. Only the first preserves behavior, yet all three stay local to the binding.

These are distinct claims, support paths and failure conditions, so the multi-section structure is justified.
