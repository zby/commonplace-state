---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/39dd1bd6e3f63b5f10b9f046/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:58Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 9482adfe7cb2f0e3621125e1f094f429de649921846986ecb186a7a37a2af0d5
format: 2
---

# Review

## Summary

The note cites no external studies or empirical results. Its main cross-domain
transfer is the software-engineering concept of information hiding, applied to
the prompt–code boundary. That transfer is explicitly bridged:

- It states the shared mechanism. Callers depend on the interface, not on the
  implementation.
- It names where the analogy breaks: unlike code-to-code swaps, this boundary
  crosses execution regimes and serves both code and LLM callers.
- It derives the asymmetric leaks from that difference.

The link to programming-practice transfer (extract-function and inline
refactorings) is delegated to a linked note. The note does not use that link as
evidence. No unbridged transfer remains.
