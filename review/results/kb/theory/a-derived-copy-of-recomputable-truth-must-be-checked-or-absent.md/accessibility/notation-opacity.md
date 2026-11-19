---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/accessibility/notation-opacity.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/accessibility/notation-opacity.md
criterion-sha256: 1169b01cde2019fc32462be33de88364d0eebd8a030621ab4fd4143257dc17fe
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 2109fd13a1b443ea92bf66f9f4e2a9d1
completed-at: '2026-11-16T22:18:32Z'
findings:
- scope: passage
  quotes:
  - mechanical derivation makes verification Level A — deterministic, near-zero cost,
    binary, runnable on every pass
  reason: '"Level A" and "Level B" are labels imported from the text testing pyramid
    note. Both are glossed where they appear, so the sentences decode locally. The
    note uses no formal argument that needs the labels, so plain wording ("a deterministic
    check" / "an LLM judgment check") would carry the same point without the imported
    notation; this is optional.'
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/62e9a9364781f3bad4eba9e2/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/62e9a9364781f3bad4eba9e2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/2109fd13a1b443ea92bf66f9f4e2a9d1/outputs/review-notation-opacity.md
raw-output-sha256: 22875d71897cdb83e24c0a943448339eb569b5d5556b0d6dfacace51deedc1be
---

# Review

## Summary

The note contains almost no formal notation. The only imported labels are "Level A" and "Level B" from the text testing pyramid, and each is glossed in place: Level B as "an LLM reading both and judging fidelity or support", and Level A as "deterministic, near-zero cost, binary, runnable on every pass". A reader who has not read the source note can still decode both sentences.

The "N" in "N independently hand-maintained instances" is a generic count, not borrowed notation. Backticked items such as `complete`, `status:`, `pyproject` and `src/commonplace/_data` are literal field, file and path names, not symbols from another note's model.
