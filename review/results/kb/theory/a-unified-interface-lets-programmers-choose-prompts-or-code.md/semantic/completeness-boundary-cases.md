---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
findings:
- scope: passage
  quotes:
  - Because both code and LLMs can act as callers, the two swap directions break different
    caller assumptions
  reason: 'The two-direction leak framework pairs each swap direction with one caller
    kind (prompt-to-code with LLM callers, code-to-prompt with code callers). Boundary
    cases strain that pairing: a code caller that forwards raw user text to a prompt-backed
    callee also relies on prompt tolerance and breaks on prompt-to-code; an LLM caller
    that invokes a tool repeatedly in its loop also absorbs the latency, cost and
    nondeterminism of a code-to-prompt swap. Both cases still map onto the direction-to-assumption
    pairing, so coverage holds, but the caller labels read as exhaustive when they
    are illustrative.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/67a98bec08d2a3cb953b85f5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-completeness-boundary-cases.md
raw-output-sha256: cbe9d014f07c359fb3f33dfe642ce567a292672a0fb43d4749b91c3a3f1413eb
---

# Review

## Summary

The note states three enumerations: the two swap directions and the caller assumptions each exposes, the three moves the binding supports (codification as refactoring, prototyping, relaxing), and three scope boundaries.

Boundary cases tested against the swap-direction framework:

- **Simplest instance:** a code caller calls a pure function, and the programmer rebinds it to a prompt. This is the code-to-prompt bullet and maps cleanly.
- **Between items:** a code caller relies on the tolerance of a prompt-backed callee and is then swapped to code. The assumption it breaks is the one named in the prompt-to-code bullet, although that bullet names only LLM callers. Conversely, LLM callers inherit cost and latency from a code-to-prompt swap. The direction-to-assumption mapping survives; the caller attribution is strained (INFO).
- **Adjacent concept:** a prompt-to-prompt swap, such as a model change, is outside the stated boundary, which is prompts versus code. It does not need to be covered.
- **Extreme instance:** a signature change. The Scope section's adapter bullet covers it explicitly.

Boundary cases tested against the three moves:

- A prompt-to-code move made for a changed requirement is not listed, but the note claims only that the binding "supports three distinct moves". It does not claim exhaustiveness, so the omission is not a coverage failure.

The taxonomies are short and match their argumentative role. No expansion is warranted.
