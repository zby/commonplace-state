---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'extends: extends typed-callable signatures across both prompt-backed agents and
    code functions'
  reason: The body section 'The connection to typed callables' already links this
    note and states the same relation in the same words ('This note extends that callable
    structure to tools'). The footer's 'extends' label and context phrase repeat that
    framing rather than adding to it. The only value left is a machine-typed edge,
    which is marginal.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/complexity/connection-inflation.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/complexity/connection-inflation.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: d70dbd3fac32c33a5eb126cf5381736a103c9f5d33234b8ad869f4207d405ab0
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/0a8ce506fc6c373cb5f49782/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 33bc96d018eb47759199e2647dea7376
completed-at: '2026-11-20T11:09:32Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/33bc96d018eb47759199e2647dea7376/outputs/review-connection-inflation.md
raw-output-sha256: c662075debb99910dec2cce499e57c81eab2cd488645c63036874ee62051a56f
format: 2
---

# Review

## Summary

Nine of the ten Relevant Notes entries add navigational value. Three targets are not linked in the body at all: the abstraction into the RLM/Tendril comparison, the host-language scheduler contrast and the programming-practices evidence note. These are pure navigation gains.

The remaining body-linked entries each add relationship semantics or framing that the inline use lacks:

- **Prompting changes failure diagnosis**: the footer types the relation as `grounds` and frames this note as making that account architecturally concrete.
- **Constraining** and **Codification**: the footer adds `defined-in` and ties each concept to what the unified interface does for it, such as lowering call-site friction or keeping the change local to the binding.
- **Spec mining**: the footer states the mechanism, which is that rules are extracted while call sites stay stable. The body only names spec mining inside the example.
- **Codification and relaxing**: the footer marks the target as the definition of relaxing and draws the contrast with prototyping.
- **Relaxing signals**: the footer adds an `enables` relation and explains how the signals feed swapping back to prompts.

Only the typed-callables entry restates what the body already says (see the finding). Because it still serves as a typed edge, it is recorded as info, not a warning.
