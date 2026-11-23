---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Because both code and LLMs can act as callers, the two swap directions break different caller assumptions"
    reason: "The two-direction leak framework pairs each swap direction with one caller kind (prompt-to-code with LLM callers, code-to-prompt with code callers). Boundary cases strain that pairing: a code caller that forwards raw user text to a prompt-backed callee also relies on prompt tolerance and breaks on prompt-to-code; an LLM caller that invokes a tool repeatedly in its loop also absorbs the latency, cost and nondeterminism of a code-to-prompt swap. Both cases still map onto the direction-to-assumption pairing, so coverage holds, but the caller labels read as exhaustive when they are illustrative."
    level: info
outcome: pass
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
