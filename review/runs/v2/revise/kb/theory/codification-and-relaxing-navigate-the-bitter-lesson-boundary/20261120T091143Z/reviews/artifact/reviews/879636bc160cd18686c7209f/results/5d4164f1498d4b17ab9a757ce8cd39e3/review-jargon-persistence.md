---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A workflow that enforces "always decompose agents into these three phases" is
    probably a vision feature relative to broader task success.
  reason: The bare label "vision feature" reappears in the heuristics several sections
    after the regimes were defined. The surrounding sentence partly re-grounds it
    ("relative to broader task success"), and the contrast with the arithmetic example
    carries meaning, so a returning reader can follow it. A short refresher such as
    "a plausible theory of task success rather than the task itself" would make the
    label self-sufficient.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/accessibility/jargon-persistence.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/accessibility/jargon-persistence.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 386074809a9cd2540746a963a84a5bf1f956f7eecea6d32384c5c702709e51d5
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/879636bc160cd18686c7209f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 5d4164f1498d4b17ab9a757ce8cd39e3
completed-at: '2026-11-20T09:13:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/5d4164f1498d4b17ab9a757ce8cd39e3/outputs/review-jargon-persistence.md
raw-output-sha256: c27fbf1794b51f6e51c78d1d8ae8715717def4d63f7fa401c21cf9637103d5f9
format: 2
---

# Review

The note's KB-specific vocabulary is the arithmetic regime versus the vision-feature regime, "relaxing", and "code-extraction codification". Each is defined locally before reuse.

- The arithmetic and vision-feature regimes are defined in the bullet list under "The trade-off depends on which regime you're in". Later uses usually restate the gloss in place. For example, "In the arithmetic regime, the bet is safe: the spec IS the problem" and "In the vision-feature regime, the bet is risky: the spec is a theory". The Ebrahimi paragraph uses "arithmetic regime" right after "calculator-class state tracking", which supplies context.
- "Relaxing" is defined as replacing an extracted component with a more general one. Later uses are either links with gloss ("Relaxing signals ... are how you detect a losing bet") or restatements of the definition ("the signal to relax — replace the rigid decomposition with a more general one"). The term names the note's central operation and has no shorter plain equivalent, so keeping it is right.
- "Code-extraction" is reused with the same qualifier each time. That qualifier carries the scope restriction stated in the second section, so this gate does not ask to strip it.

The only weak spot is the bare "vision feature" label in heuristic 1, which is recorded as informational.
