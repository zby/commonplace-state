---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 8f05aba89d28e81694031337bcbcbd44c8acc31a62a36cfac4e644310ab78a73
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/c66c13bb678685ed5c095067/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-unearned-generality.md
raw-output-sha256: b0486e328e5331f2c2c371290ea5fb74aec2c1633090db35b4b04979365c828c
format: 2
---

# Review

## Summary

The central claim is "A unified interface lets programmers choose prompts or code without changing callers". Its leaks are asymmetric.

- **"unified interface":** The concrete term would be "llm-do's shared callable binding". Downgrade test: the argument comes from information hiding and from properties of the two execution regimes, not from llm-do specifics. The note says why it does not depend on llm-do. Any shared name, arguments, result format and description produces the effect. Forbids test: the general wording rules out swaps without call-site edits in any system that exposes agents and tools through separate invocation surfaces. The note explicitly contrasts that case. The abstraction is earned by argument.
- **"prompts or code":** These are concrete terms that the mechanism uses directly.
- **"callers":** The note works both instance classes, LLM callers and code callers, and each drives one leak direction. The generality is load-bearing.

Abstraction is concentrated in the one place the argument needs it. It is not spread across the prose.
