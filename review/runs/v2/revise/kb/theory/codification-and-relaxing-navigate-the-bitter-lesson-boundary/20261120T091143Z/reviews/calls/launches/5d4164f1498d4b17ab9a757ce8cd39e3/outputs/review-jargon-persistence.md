---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A workflow that enforces \"always decompose agents into these three phases\" is probably a vision feature relative to broader task success."
    reason: "The bare label \"vision feature\" reappears in the heuristics several sections after the regimes were defined. The surrounding sentence partly re-grounds it (\"relative to broader task success\"), and the contrast with the arithmetic example carries meaning, so a returning reader can follow it. A short refresher such as \"a plausible theory of task success rather than the task itself\" would make the label self-sufficient."
    level: info
outcome: pass
---

# Review

The note's KB-specific vocabulary is the arithmetic regime versus the vision-feature regime, "relaxing", and "code-extraction codification". Each is defined locally before reuse.

- The arithmetic and vision-feature regimes are defined in the bullet list under "The trade-off depends on which regime you're in". Later uses usually restate the gloss in place. For example, "In the arithmetic regime, the bet is safe: the spec IS the problem" and "In the vision-feature regime, the bet is risky: the spec is a theory". The Ebrahimi paragraph uses "arithmetic regime" right after "calculator-class state tracking", which supplies context.
- "Relaxing" is defined as replacing an extracted component with a more general one. Later uses are either links with gloss ("Relaxing signals ... are how you detect a losing bet") or restatements of the definition ("the signal to relax — replace the rigid decomposition with a more general one"). The term names the note's central operation and has no shorter plain equivalent, so keeping it is right.
- "Code-extraction" is reused with the same qualifier each time. That qualifier carries the scope restriction stated in the second section, so this gate does not ask to strip it.

The only weak spot is the bare "vision feature" label in heuristic 1, which is recorded as informational.
