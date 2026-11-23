---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
note-sha256: fb2e8f5c0c25c9112acc66c6b787a0ec64df303dcc0e8b3fb5f57fea0cccfc87
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/8ef3f75482ff86d7654185fc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 3520e864e524489aa2b8264997528ccc
completed-at: '2026-11-20T11:09:20Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/outputs/review-description-discrimination.md
raw-output-sha256: c2c2bf49050c3d997245a60e67c6e2dac28703563c96523e7278aba764aea193
format: 2
---

# Review

## Summary

The description adds substantial retrieval value beyond the title. The title says only that a unified interface allows prompt/code choice without caller changes. The description adds:

- **Mechanism and implication:** the abstraction "leaks asymmetrically".
- **Concrete scope for each direction:** prompt-to-code exposes loose LLM callers; code-to-prompt exposes cost, latency and error assumptions.

These distinctions would help an agent pick this note over a sibling about typed callables, codification or relaxing in a short result list. The description does not merely paraphrase the title.
