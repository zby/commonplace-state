---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: 8f05aba89d28e81694031337bcbcbd44c8acc31a62a36cfac4e644310ab78a73
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
findings: []
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/50211b5b85bd219f54aa175d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: 92273908e1faca748d8d51586bd895d5aad6afeaf1b122d7746e0c3b9a40d299
---

# Review

## Summary

Qualifiers in the title, description and opening claim:

- **"unified interface":** This is load-bearing. The argument depends on a shared name, arguments, result format and description. The constraining section contrasts it with systems that expose agents and tools through different invocation surfaces, where a swap is a breaking change.
- **"programmers choose":** This is load-bearing. The mechanism section separates a programmer's binding choice from a runtime that decides per input. The claim about callers staying unchanged concerns a deliberate rebinding.
- **"prompts or code":** This is load-bearing for the asymmetry. Both leaks depend on the two regimes differing: prompt tolerance against code strictness, and model latency and fallibility against function execution. Deleting the qualifier would turn the claim into ordinary information hiding, which the note explicitly contrasts with its own case. The wording is also intentional LLM-domain scoping.
- **"without changing callers":** This is the claim's content, and the Scope section qualifies it with adapters and call-site headroom.

Removing any of these qualifiers would either falsify the asymmetry claim or erase the contrast the note draws. None narrows the claim without doing work.
