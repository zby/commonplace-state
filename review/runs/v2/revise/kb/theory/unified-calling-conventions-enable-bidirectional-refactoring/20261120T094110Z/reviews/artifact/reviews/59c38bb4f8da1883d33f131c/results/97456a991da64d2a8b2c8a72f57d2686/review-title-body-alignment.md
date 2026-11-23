---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - On top of the hybrid VM, llm-do adds an imperative scheduler — Python code that
    owns control flow rather than a graph DSL.
  reason: 'The scheduler section supports the title only indirectly. It argues that
    imperative orchestration lets neural-symbolic refactoring use ordinary code refactorings,
    and it adds a comparison with graph DSLs that the title does not promise. This
    is extra material, not drift: the body still mainly establishes that a shared
    name-based calling convention keeps call sites stable when a component moves in
    either direction.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 4f8a5cf9ee762005ab989c0c56fe98f89d15fd8d8fca568c8419a3649c2db7a0
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/59c38bb4f8da1883d33f131c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 97456a991da64d2a8b2c8a72f57d2686
completed-at: '2026-11-20T09:42:00Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/97456a991da64d2a8b2c8a72f57d2686/outputs/review-title-body-alignment.md
raw-output-sha256: 3494805f606a0f28a7496ab28f119564bd47c767f1b528fdd10f1f9b127dcd8f
format: 2
---

# Review

## Summary

The body supports the title's claim and scope. It argues that a shared calling convention, implemented through name-based dispatch, keeps call sites stable when a component's implementation changes. That makes moving across the neural-symbolic boundary a local operation.

The body covers both directions named by "bidirectional." The numbered progression covers neural to symbolic: start with an agent, spot a pattern, codify it as `sanitize_filename()`, and leave the call site unchanged. The relaxing step and the `ticket_classifier` example cover symbolic to neural: the same caller sends work to a prompt under the same name while the team tries routing rules. The title's general claim is shown with one system, llm-do. The opening paragraph and the mechanism section present llm-do as an implementation of a general principle, so this is not scope drift.

The only loose fit is the scheduler section, recorded as an info finding.
