---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - yet all three stay local to the binding because callers depend only on the interface
  reason: This summary sentence contradicts the leak section. There, LLM callers rely
    on the prompt's tolerance of loose arguments, and code callers rely on latency,
    cost and deterministic failure, none of which the interface expresses. That section
    concludes that 'interface parity alone is not enough for safe swapping'. The Scope
    section adds that callers relying on prior decisions or error behavior need testing
    after a swap. Saying that callers depend only on the interface compresses away
    the tension the note itself establishes.
  level: warn
- scope: passage
  quotes:
  - Only the first move is a behavior-preserving refactoring.
  reason: The prompt-to-code move is called behavior-preserving. The leak section
    says that the same move makes LLM callers that relied on prompt tolerance 'begin
    failing or triggering literal misreads', which is a behavior change visible to
    callers. The move description also preserves only 'the rule' the team chose to
    keep. The term may have drifted from preserving the selected routing rule to preserving
    behavior in general. This needs the author's confirmation.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/035ba8b0928160e1c3fdfd50/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-internal-consistency.md
raw-output-sha256: 8f6a8147b157cd66c9fc1c424fc2be14f813b2d82435a2dbb94e0fadc2918961
format: 2
---

# Review

## Summary

Key claims by section:

- **Opening:** A shared interface hides implementation, and the abstraction leaks asymmetrically.
- **Leak section:** Callers acquire dependencies beyond the interface, namely input tolerance and runtime profile. Interface parity is insufficient.
- **Scope:** Call invariance is not behavioral invariance, and swaps need testing.
- **Constraining section:** The three moves stay local "because callers depend only on the interface". The first move is behavior-preserving.

The opening, leak section and Scope section agree. The closing summary of the constraining section restates the simple information-hiding picture that the leak section qualified, which contradicts it (WARN). "Behavior-preserving" for prompt-to-code also sits uneasily with the leak described for that same direction (INFO).
